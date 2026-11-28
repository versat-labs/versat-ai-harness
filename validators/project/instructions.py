#!/usr/bin/env python3
"""Check that a project's CLAUDE.md only imports its canonical AGENTS.md.

The rule is defined by the Agent Artifact Standard
(standards/core/agent-artifacts.md, "Claude instruction entry point"). This
check is read-only: it never creates, edits or removes project files.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

STANDARD = "standards/core/agent-artifacts.md#claude-instruction-entry-point"
IMPORT_LINE = "@AGENTS.md"
REMEDIATION = (
    "Provide CLAUDE.md containing only the line @AGENTS.md and keep all "
    "instructions in AGENTS.md; adopt it through a reviewed migration."
)


@dataclass(frozen=True)
class Finding:
    path: str
    problem: str
    standard: str = STANDARD
    remediation: str = REMEDIATION


def check(root: Path) -> list[Finding]:
    """Return non-compliance findings for the project rooted at ``root``."""
    agents = root / "AGENTS.md"
    claude = root / "CLAUDE.md"
    findings: list[Finding] = []
    for path in (agents, claude):
        if path.is_symlink():
            findings.append(Finding(path.name, "must be a regular file, not a symlink"))
    if findings:
        return findings
    if not agents.exists():
        return []
    if not claude.exists():
        return [Finding("CLAUDE.md", "is missing while AGENTS.md exists")]
    if not claude.is_file():
        return [Finding("CLAUDE.md", "must be a regular file")]
    lines = [
        line.strip()
        for line in claude.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if IMPORT_LINE not in lines:
        findings.append(Finding("CLAUDE.md", "does not import @AGENTS.md"))
    if any(line != IMPORT_LINE for line in lines):
        findings.append(
            Finding("CLAUDE.md", "contains instructions beyond the @AGENTS.md import")
        )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", required=True, type=Path, help="project root")
    parser.add_argument("--json", action="store_true", help="print JSON findings")
    arguments = parser.parse_args(argv)
    root = arguments.root
    if not root.is_dir():
        parser.error(f"--root is not a directory: {root}")
    findings = check(root)
    if arguments.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    elif findings:
        for finding in findings:
            print(
                f"NON-COMPLIANT {finding.path}: {finding.problem} "
                f"(Standard: {finding.standard}). Remediation: {finding.remediation}"
            )
    else:
        print("Claude instruction entry point: compliant or not applicable.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
