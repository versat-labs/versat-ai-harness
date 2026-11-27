#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Create a fresh synthetic repository for one github-issue-creation case."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
CASES = HERE.parents[1] / "cases" / "github-issue-creation"


def prepare(case_id: str, output: Path) -> dict[str, str]:
    case = json.loads((CASES / f"{case_id}.json").read_text(encoding="utf-8"))
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"{output} must be a new empty directory")
    repo = output / "synthetic-app"
    shutil.copytree(HERE / "empty-repository", repo)
    (repo / "README.md").write_text("# Synthetic app\n\nSynthetic fixture.\n")
    shutil.copytree(HERE / "organization", output / "organization")
    shutil.copytree(HERE / "stub", output / "bin")
    for command in (
        ["git", "init", "-q"],
        [
            "git",
            "remote",
            "add",
            "origin",
            "https://github.com/versat-labs/synthetic-app.git",
        ],
    ):
        subprocess.run(command, cwd=repo, check=True)
    env = {
        "PATH_PREFIX": str(output / "bin"),
        "GH_STUB_LOG": str(output / "gh-calls.jsonl"),
        "GH_STUB_FAIL": case.get("stub_failure", ""),
        "GH_STUB_VISIBILITY": case.get("visibility", "public"),
        "REPOSITORY": str(repo),
        "ORGANIZATION_FORMS": str(output / "organization"),
    }
    (output / "environment.json").write_text(json.dumps(env, indent=2) + "\n")
    return env


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    print(json.dumps(prepare(args.case, args.output), indent=2))


if __name__ == "__main__":
    main()
