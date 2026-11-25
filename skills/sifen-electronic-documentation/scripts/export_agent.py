#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Export optional SIFEN guidance; the installed knowledge corpus remains separate."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

PLATFORMS = ("claude", "gemini", "copilot", "cursor", "generic")


def render(platform: str, core: str) -> dict[str, str]:
    """Return relative output paths and content without writing files."""
    if platform == "claude":
        return {".claude/agents/sifen-electronic-documentation.md":
                "---\nname: sifen-electronic-documentation\ndescription: Consult the installed SIFEN documentary snapshot with source traceability.\nmodel: inherit\n---\n\n" + core}
    if platform == "gemini":
        return {".gemini/sifen-core.md": core,
                "GEMINI.md": "# SIFEN documentation\n\n@./.gemini/sifen-core.md\n"}
    if platform == "copilot":
        return {".github/sifen-core.md": core,
                ".github/copilot-instructions.md": "# SIFEN documentation\n\nRead [SIFEN guidance](sifen-core.md) before working with SIFEN.\n"}
    if platform == "cursor":
        return {".cursor/rules/sifen-electronic-documentation.mdc":
                '---\ndescription: Consult SIFEN sources for DE/DTE, CDC, signatures, events, KuDE and QR.\nglobs: "**/*.{xml,xsd,wsdl,json,ts,tsx,js,jsx,java,kt,cs,py,php,go,rs,md}"\nalwaysApply: false\n---\n\n' + core}
    return {"AGENTS.md": core}


def export(destination: Path, files: dict[str, str], force: bool) -> None:
    """Preflight every target before writing; reject redirected or non-file outputs."""
    destination = destination.expanduser().resolve()
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination must be a directory")
    targets = [(destination / relative, content) for relative, content in files.items()]
    for path, _ in targets:
        for component in [path, *path.parents]:
            if component == destination:
                break
            if component.is_symlink():
                raise ValueError(f"Refusing symlink output component: {component.relative_to(destination)}")
            if component != path and component.exists() and not component.is_dir():
                raise ValueError(f"Output parent is not a directory: {component.relative_to(destination)}")
        if path.exists():
            if not path.is_file():
                raise ValueError(f"Output is not a regular file: {path.relative_to(destination)}")
            if not force:
                raise ValueError(f"File already exists: {path.relative_to(destination)}. Use --force to replace it.")
    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        print(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=PLATFORMS)
    parser.add_argument("--destination", required=True, type=Path)
    parser.add_argument("--force", action="store_true", help="Explicitly replace existing regular output files")
    args = parser.parse_args()
    try:
        core = (Path(__file__).resolve().parent.parent / "agents/shared/sifen-core.md").read_text(encoding="utf-8")
        export(args.destination, render(args.platform, core), args.force)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
