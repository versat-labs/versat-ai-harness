#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Resolve GitHub issue forms, detect missing answers and render issue content.

The helper reads local files and prints results. It never calls GitHub.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import yaml

FORM_DIRECTORY = Path(".github") / "ISSUE_TEMPLATE"
FORM_SUFFIXES = (".yml", ".yaml")
ANSWER_TYPES = {"textarea", "input", "dropdown", "checkboxes"}
NO_RESPONSE = "_No response_"


class FormError(Exception):
    """Raised when a form or answer set cannot be used."""


def form_files(root: Path) -> list[Path]:
    """Return issue form files under a repository root, sorted by name."""
    directory = root / FORM_DIRECTORY
    if not directory.is_dir():
        return []
    return sorted(
        path
        for path in directory.iterdir()
        if path.is_file() and path.suffix in FORM_SUFFIXES
    )


def load_form(path: Path) -> dict[str, Any]:
    """Load an issue form and return its usable metadata and fields."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise FormError(f"{path}: cannot read issue form: {error}") from error
    if not isinstance(data, dict) or not data.get("name"):
        raise FormError(f"{path}: issue form must define a name")
    body = data.get("body")
    if not isinstance(body, list):
        raise FormError(f"{path}: issue form must define a body list")
    fields = []
    for item in body:
        if not isinstance(item, dict) or item.get("type") == "markdown":
            continue
        attributes = item.get("attributes") or {}
        validations = item.get("validations") or {}
        fields.append(
            {
                "id": item.get("id"),
                "type": item.get("type"),
                "label": attributes.get("label"),
                "description": attributes.get("description"),
                "required": bool(validations.get("required", False)),
            }
        )
    return {
        "file": str(path),
        "name": data["name"],
        "description": data.get("description"),
        "title_prefix": data.get("title", ""),
        "type": data.get("type"),
        "projects": list(data.get("projects") or []),
        "labels": list(data.get("labels") or []),
        "fields": fields,
    }


def resolve(repo_dir: Path, org_dir: Path | None) -> dict[str, Any]:
    """Return the forms that apply: repository forms first, else organization."""
    repo_forms = form_files(repo_dir)
    if repo_forms:
        source, files = "repository", repo_forms
    elif org_dir is not None and form_files(org_dir):
        source, files = "organization", form_files(org_dir)
    else:
        source, files = "none", []
    return {"source": source, "forms": [load_form(path) for path in files]}


def answer_text(value: Any) -> str:
    """Return an answer as text; lists render as one item per line."""
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(str(item) for item in value)
    return str(value)


def missing(form: dict[str, Any], answers: dict[str, Any]) -> list[str]:
    """Return labels of required answer fields that are absent or blank."""
    return [
        field["label"]
        for field in form["fields"]
        if field["required"]
        and field["type"] in ANSWER_TYPES
        and not answer_text(answers.get(field["id"])).strip()
    ]


def render(form: dict[str, Any], answers: dict[str, Any], title: str) -> dict[str, Any]:
    """Return the prefixed title, body and notices in GitHub's response layout."""
    absent = missing(form, answers)
    if absent:
        raise FormError("missing required answers: " + ", ".join(absent))
    if not title.strip():
        raise FormError("missing title")
    prefix = form["title_prefix"]
    full_title = title if title.startswith(prefix) else prefix + title
    sections, notices = [], []
    for field in form["fields"]:
        if field["type"] not in ANSWER_TYPES:
            notices.append(
                f"Skipped {field['type']} field '{field['label']}'; "
                "add it on GitHub after creation if needed."
            )
            continue
        text = answer_text(answers.get(field["id"]))
        sections.append(
            f"### {field['label']}\n\n{text if text.strip() else NO_RESPONSE}"
        )
    return {
        "title": full_title,
        "body": "\n\n".join(sections) + "\n",
        "type": form["type"],
        "projects": form["projects"],
        "notices": notices,
    }


def load_answers(path: Path) -> dict[str, Any]:
    """Load answers keyed by field ID from a JSON file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise FormError(f"{path}: cannot read answers: {error}") from error
    if not isinstance(data, dict):
        raise FormError(f"{path}: answers must be a JSON object keyed by field ID")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    resolve_parser = commands.add_parser("resolve", help="list applicable forms")
    resolve_parser.add_argument("--repo-dir", type=Path, required=True)
    resolve_parser.add_argument("--org-dir", type=Path)
    for name in ("missing", "render"):
        command = commands.add_parser(name)
        command.add_argument("--form", type=Path, required=True)
        command.add_argument("--answers", type=Path, required=True)
        if name == "render":
            command.add_argument("--title", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "resolve":
            result: Any = resolve(args.repo_dir, args.org_dir)
        else:
            form = load_form(args.form)
            answers = load_answers(args.answers)
            if args.command == "missing":
                result = {"missing": missing(form, answers)}
            else:
                result = render(form, answers, args.title)
    except FormError as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
