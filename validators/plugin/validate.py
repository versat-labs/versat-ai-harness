#!/usr/bin/env python3
"""Validate the portable Versat AI Harness Plugin package."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
PLUGIN_NAME = "versat-ai-harness"
MARKETPLACE_NAME = "versat"
MARKETPLACE_LABEL = "Versat Plugins"
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
EXPECTED_SKILLS = {
    "architecture-review",
    "project-audit",
    "project-bootstrap",
    "project-maintenance",
    "versat-sdd",
    "sifen-electronic-documentation",
}
CANONICAL_DIRECTORIES = {
    "agents",
    "project-templates",
    "schemas",
    "sdd",
    "skills",
    "standards",
    "validators",
}


def load_json(relative_path: str, errors: list[str]) -> dict[str, Any] | None:
    path = ROOT / relative_path
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing {relative_path}")
        return None
    except json.JSONDecodeError as error:
        errors.append(f"invalid JSON in {relative_path}: {error}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{relative_path} must contain a JSON object")
        return None
    return value


def require_equal(
    left: Any,
    right: Any,
    description: str,
    errors: list[str],
) -> None:
    if left != right:
        errors.append(f"{description}: expected {right!r}, found {left!r}")


def validate_skill(skill_name: str, errors: list[str]) -> None:
    path = ROOT / "skills" / skill_name / "SKILL.md"
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing skills/{skill_name}/SKILL.md")
        return
    match = re.search(r"^name:\s*(\S+)\s*$", content, re.MULTILINE)
    if match is None or match.group(1) != skill_name:
        errors.append(f"skills/{skill_name}/SKILL.md must declare name: {skill_name}")


def validate() -> list[str]:
    errors: list[str] = []
    portable = load_json("plugin.json", errors)
    compatibility = load_json(".codex-plugin/plugin.json", errors)
    marketplace = load_json(".agents/plugins/marketplace.json", errors)

    try:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        errors.append("missing VERSION")
        version = ""
    if SEMVER.fullmatch(version) is None:
        errors.append(f"VERSION must be strict semantic versioning: {version!r}")

    try:
        standards_lock = (
            ROOT / "project-templates/base/.versat/standards.lock"
        ).read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append("missing project-templates/base/.versat/standards.lock")
    else:
        lock_version = re.search(
            r"^harness:\s*\n(?:^[ \t]+.*\n)*?^[ \t]+version:\s*(\S+)\s*$",
            standards_lock,
            re.MULTILINE,
        )
        if lock_version is None:
            errors.append(
                "project template standards.lock must declare harness.version"
            )
        else:
            require_equal(
                lock_version.group(1),
                version,
                "project template Harness version",
                errors,
            )

    for directory in sorted(CANONICAL_DIRECTORIES):
        if not (ROOT / directory).is_dir():
            errors.append(f"missing canonical directory: {directory}/")

    for skill_name in sorted(EXPECTED_SKILLS):
        validate_skill(skill_name, errors)

    legacy_paths = ("plugin/versat-ai-harness",)
    for relative_path in legacy_paths:
        if (ROOT / relative_path).exists():
            errors.append(f"legacy nested Plugin path must be removed: {relative_path}")

    if portable is not None:
        require_equal(
            portable.get("$schema"), PORTABLE_SCHEMA, "portable schema", errors
        )
        require_equal(portable.get("name"), PLUGIN_NAME, "portable Plugin name", errors)
        require_equal(
            portable.get("version"), version, "portable Plugin version", errors
        )
        extensions = portable.get("extensions")
        openai_extension = (
            extensions.get("com.openai") if isinstance(extensions, dict) else None
        )
        portable_interface = (
            openai_extension.get("interface")
            if isinstance(openai_extension, dict)
            else None
        )
        if not isinstance(portable_interface, dict):
            errors.append("plugin.json must define extensions.com.openai.interface")
    else:
        portable_interface = None

    if compatibility is not None:
        require_equal(
            compatibility.get("name"), PLUGIN_NAME, "compatibility Plugin name", errors
        )
        require_equal(
            compatibility.get("version"),
            version,
            "compatibility Plugin version",
            errors,
        )
        require_equal(
            compatibility.get("skills"),
            "./skills/",
            "compatibility skills path",
            errors,
        )
        compatibility_interface = compatibility.get("interface")
        if not isinstance(compatibility_interface, dict):
            errors.append(".codex-plugin/plugin.json must define interface")
    else:
        compatibility_interface = None

    if portable_interface is not None and compatibility_interface is not None:
        require_equal(
            portable_interface,
            compatibility_interface,
            "portable and compatibility interface metadata",
            errors,
        )

    if marketplace is not None:
        require_equal(
            marketplace.get("name"), MARKETPLACE_NAME, "marketplace name", errors
        )
        interface = marketplace.get("interface")
        if not isinstance(interface, dict):
            errors.append("marketplace interface must be an object")
        else:
            require_equal(
                interface.get("displayName"),
                MARKETPLACE_LABEL,
                "marketplace display name",
                errors,
            )
        entries = marketplace.get("plugins")
        if not isinstance(entries, list):
            errors.append("marketplace plugins must be an array")
        else:
            matching = [
                entry
                for entry in entries
                if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME
            ]
            if len(matching) != 1:
                errors.append(
                    "marketplace must contain exactly one versat-ai-harness entry"
                )
            else:
                entry = matching[0]
                source = entry.get("source")
                if not isinstance(source, dict):
                    errors.append("marketplace Plugin source must be an object")
                else:
                    require_equal(
                        source.get("source"), "url", "marketplace source type", errors
                    )
                    require_equal(
                        source.get("url"),
                        "https://github.com/versat-labs/versat-ai-harness.git",
                        "marketplace repository URL",
                        errors,
                    )
                    require_equal(
                        source.get("ref"),
                        f"v{version}",
                        "marketplace release reference",
                        errors,
                    )
                policy = entry.get("policy")
                if not isinstance(policy, dict):
                    errors.append("marketplace Plugin policy must be an object")
                else:
                    if policy.get("installation") not in {
                        "NOT_AVAILABLE",
                        "AVAILABLE",
                        "INSTALLED_BY_DEFAULT",
                    }:
                        errors.append("marketplace installation policy is invalid")
                    if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                        errors.append("marketplace authentication policy is invalid")
                category = entry.get("category")
                if not isinstance(category, str) or not category.strip():
                    errors.append(
                        "marketplace Plugin category must be a non-empty string"
                    )

    return errors


def main() -> None:
    errors = validate()
    if errors:
        print("Plugin package validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Portable Plugin package validation passed.")


if __name__ == "__main__":
    main()
