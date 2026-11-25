#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Search the installed SIFEN text corpus with bounded contextual output."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

TEXT_SUFFIXES = {".md", ".txt", ".xml", ".csv"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("term", help="Literal text (or a regular expression with --regex)")
    parser.add_argument("--regex", action="store_true")
    parser.add_argument("--case-sensitive", action="store_true")
    parser.add_argument("--context", type=int, default=2, help="Lines before and after each match")
    parser.add_argument("--max", type=int, default=50, dest="max_matches")
    parser.add_argument("--include", help="Case-insensitive substring of the relative source path")
    args = parser.parse_args()
    if not args.term or args.context < 0 or args.max_matches < 1:
        parser.error("term must be nonempty; --context must be >= 0 and --max must be >= 1")
    try:
        matcher = re.compile(args.term if args.regex else re.escape(args.term),
                             0 if args.case_sensitive else re.IGNORECASE)
    except re.error as error:
        parser.error(f"Invalid regex: {error}")
    references = Path(__file__).resolve().parent.parent / "references"
    corpus = references / "extracted-text"
    if not corpus.is_dir() or not any(corpus.rglob("*.txt")):
        print("ERROR: Missing or empty extracted-text corpus; no source conclusion is available.", file=sys.stderr)
        return 2
    paths = sorted(path for path in references.rglob("*")
                   if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
                   and "original-sources" not in path.relative_to(references).parts
                   and path.name not in {"technical-manual-v150-full.txt", "source-manifest.csv"}
                   and (not args.include or args.include.casefold() in path.relative_to(references).as_posix().casefold()))
    if not paths:
        print("ERROR: No searchable sources for this selection; check --include and installed resources.", file=sys.stderr)
        return 2
    found = 0
    for path in paths:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as error:
            print(f"ERROR: Cannot read {path.relative_to(references)}: {error}", file=sys.stderr)
            return 2
        for index, line in enumerate(lines):
            if not matcher.search(line):
                continue
            print(f"\n### {path.relative_to(references)}:{index + 1}")
            for position in range(max(0, index - args.context), min(len(lines), index + args.context + 1)):
                print(f"{'>' if position == index else ' '} {position + 1:>6}: {lines[position]}")
            found += 1
            if found == args.max_matches:
                print(f"\nResult limit {args.max_matches} reached; narrow the query or raise --max for further matches.")
                return 0
    print(f"\n{found} match(es)." if found else "No matches found in the selected available sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
