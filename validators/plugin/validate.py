#!/usr/bin/env python3
"""Validate the portable Versat AI Harness Plugin package."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
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
REPOSITORY_SLUG = "versat-labs/versat-ai-harness"
CLAUDE_MIRRORED_FIELDS = ("name", "version", "description", "author", "repository")
INSTRUCTION_ROOTS = ("", "project-templates/base")
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
EXPECTED_SKILLS = {
    "architecture-review",
    "project-audit",
    "project-bootstrap",
    "project-maintenance",
    "versat-sdd",
    "sifen-electronic-documentation",
    "github-issue-creation",
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


def load_instruction_check():
    """Load the consumer instruction check shipped next to this validator."""
    path = Path(__file__).resolve().parents[1] / "project" / "instructions.py"
    spec = importlib.util.spec_from_file_location("project_instructions", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(spec.name, module)
    spec.loader.exec_module(module)
    return module


def validate_instruction_entry_points(errors: list[str]) -> None:
    instructions = load_instruction_check()
    for relative in INSTRUCTION_ROOTS:
        base = ROOT / relative if relative else ROOT
        prefix = f"{relative}/" if relative else ""
        if not (base / "AGENTS.md").is_file() or (base / "AGENTS.md").is_symlink():
            errors.append(f"missing {prefix}AGENTS.md")
            continue
        for finding in instructions.check(base):
            errors.append(f"{prefix}{finding.path} {finding.problem}")


def validate_claude_manifest(
    manifest: dict[str, Any] | None,
    portable: dict[str, Any] | None,
    errors: list[str],
) -> None:
    if manifest is None:
        return
    require_equal(manifest.get("name"), PLUGIN_NAME, "Claude Plugin name", errors)
    if portable is not None:
        for field in CLAUDE_MIRRORED_FIELDS:
            require_equal(
                manifest.get(field),
                portable.get(field),
                f"Claude Plugin {field}",
                errors,
            )
    require_equal(
        manifest.get("agents"),
        [],
        "Claude Plugin agents (role guidance must not register as subagents)",
        errors,
    )


def validate_claude_marketplace(
    catalog: dict[str, Any] | None, version: str, errors: list[str]
) -> str | None:
    if catalog is None:
        return None
    require_equal(
        catalog.get("name"), MARKETPLACE_NAME, "Claude marketplace name", errors
    )
    owner = catalog.get("owner")
    if (
        not isinstance(owner, dict)
        or not isinstance(owner.get("name"), str)
        or not owner["name"].strip()
    ):
        errors.append("Claude marketplace owner must define a non-empty name")
    entries = catalog.get("plugins")
    if not isinstance(entries, list):
        errors.append("Claude marketplace plugins must be an array")
        return None
    matching = [
        entry
        for entry in entries
        if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME
    ]
    if len(matching) != 1:
        errors.append(
            "Claude marketplace must contain exactly one versat-ai-harness entry"
        )
        return None
    source = matching[0].get("source")
    if not isinstance(source, dict):
        errors.append("Claude marketplace Plugin source must be an object")
        return None
    require_equal(
        source.get("source"), "github", "Claude marketplace source type", errors
    )
    require_equal(
        source.get("repo"), REPOSITORY_SLUG, "Claude marketplace repository", errors
    )
    require_equal(
        source.get("ref"), f"v{version}", "Claude marketplace release reference", errors
    )
    ref = source.get("ref")
    return ref if isinstance(ref, str) else None


def validate() -> list[str]:
    errors: list[str] = []
    portable = load_json("plugin.json", errors)
    compatibility = load_json(".codex-plugin/plugin.json", errors)
    marketplace = load_json(".agents/plugins/marketplace.json", errors)
    claude_manifest = load_json(".claude-plugin/plugin.json", errors)
    claude_marketplace = load_json(".claude-plugin/marketplace.json", errors)
    codex_ref: str | None = None

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
                    if isinstance(source.get("ref"), str):
                        codex_ref = source["ref"]
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

    validate_claude_manifest(claude_manifest, portable, errors)
    claude_ref = validate_claude_marketplace(claude_marketplace, version, errors)
    if codex_ref is not None and claude_ref is not None and codex_ref != claude_ref:
        errors.append(
            f"Codex and Claude catalogs must select the same release: {codex_ref!r} != {claude_ref!r}"
        )
    validate_instruction_entry_points(errors)

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
