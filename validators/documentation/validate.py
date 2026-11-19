"""Report mechanical documentation checks for two Git snapshots."""

import argparse
from dataclasses import dataclass
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

MAX_SUMMARY_BYTES = 900_000
VARIANTS = (
    ("", "English source"),
    (".pt", "Portuguese sibling"),
    (".es", "Spanish sibling"),
)
TRANSLATION = re.compile(r"\.(pt|es)\.md$")
REGULAR_MODES = {"100644", "100755"}


@dataclass(frozen=True)
class Row:
    status: str
    rule: str
    path: str
    reason: str


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=root, stdin=subprocess.DEVNULL, capture_output=True
    )
    if result.returncode:
        raise ValueError(f"Git could not read the repository ({args[0]}).")
    return result.stdout


def commit(root: Path, ref: str, label: str) -> str:
    try:
        return (
            git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
            .decode("ascii")
            .strip()
        )
    except ValueError as exc:
        raise ValueError(
            f"{label} revision unavailable. Fetch the required Git history."
        ) from exc


def canonical(path: str) -> str | None:
    name = TRANSLATION.sub(".md", path)
    if name.endswith(".md") and (
        name.startswith("docs/user-docs/")
        or name in {"docs/product/overview.md", "docs/quickstart.md"}
    ):
        segments = path.split("/")
        if ".." in segments or "." in segments or "" in segments:
            raise ValueError("Git supplied an unsafe documentation path.")
        return name
    return None


def tree_entries(root: Path, target: str) -> dict[str, tuple[str, str]]:
    data = git(
        root,
        "ls-tree",
        "-rz",
        "--full-tree",
        target,
        "--",
        "docs",
    )
    entries = {}
    for record in data.split(b"\0")[:-1]:
        metadata, path = record.split(b"\t", 1)
        mode, _, oid = metadata.decode("ascii").split()
        entries[os.fsdecode(path)] = (mode, oid)
    return entries


def obstruction(entries: dict[str, tuple[str, str]], path: str) -> bool:
    return any(parent.as_posix() in entries for parent in PurePosixPath(path).parents)


def document_row(
    root: Path, entries: dict[str, tuple[str, str]], path: str, rule: str
) -> Row:
    if obstruction(entries, path):
        return Row(
            "Fail", rule, path, "A parent path in the target is not a directory."
        )
    if path not in entries:
        return Row("Fail", rule, path, "Required file is missing.")
    mode, oid = entries[path]
    if mode not in REGULAR_MODES:
        return Row(
            "Fail", rule, path, "Expected a regular Git file. Links are not followed."
        )
    try:
        content = git(root, "cat-file", "blob", oid).decode("utf-8-sig")
    except UnicodeDecodeError:
        return Row("Fail", rule, path, "Expected readable UTF-8 Markdown.")
    if not content.strip():
        return Row("Fail", rule, path, "File contains no text.")
    return Row("Pass", rule, path, "Readable, nonempty Markdown file.")


def compare(root: Path, base: str, target: str) -> list[Row]:
    # Disabling rename detection retains both endpoints as changed paths.
    changed = git(
        root,
        "diff",
        "--name-only",
        "-z",
        "--no-renames",
        "--no-ext-diff",
        "--ignore-submodules=none",
        base,
        target,
        "--",
    )
    sets = {
        name
        for path in changed.split(b"\0")[:-1]
        if (name := canonical(os.fsdecode(path))) is not None
    }
    if not sets:
        return [
            Row(
                "Not applicable",
                "Documentation scope",
                "",
                "No recognized Markdown paths changed.",
            )
        ]
    entries = tree_entries(root, target)
    rows = []
    for name in sorted(sets):
        variants = [(name[:-3] + suffix + ".md", rule) for suffix, rule in VARIANTS]
        if not any(
            path in entries or obstruction(entries, path) for path, _ in variants
        ):
            rows.append(
                Row(
                    "Not applicable",
                    "Language file set",
                    name,
                    "All files removed. Review navigation.",
                )
            )
            continue
        rows.extend(document_row(root, entries, path, rule) for path, rule in variants)
    return rows


def safe_path(path: str) -> str:
    visible = "".join(
        char if char.isprintable() else ascii(char)[1:-1] for char in path
    )
    encoded = "".join(
        char if char.isalnum() or char in " ./-" else f"&#{ord(char)};"
        for char in visible
    )
    return f"<code>{encoded}</code>"


def render(base: str, target: str, rows: list[Row]) -> str:
    header = (
        "# Documentation standards report\n\n"
        f"Base: `{base}`  \n"
        f"Target: `{target}`\n\n"
        "| Result | Rule | Path | Reason |\n| --- | --- | --- | --- |\n"
    )
    footer = (
        "\n## Human review\n\n"
        "- Confirm applicability, README and guide navigation, and publication access.\n"
        "- Review feature rationale, factual accuracy and semantic alignment across languages.\n"
        "- This advisory report measures only the listed mechanical rules.\n"
    )
    truncation = "| Omitted | Output limit | | Some rows were omitted. |\n"
    budget = MAX_SUMMARY_BYTES - len((header + footer + truncation).encode("utf-8"))
    lines = [header]
    for row in rows:
        line = f"| {row.status} | {row.rule} | {safe_path(row.path)} | {row.reason} |\n"
        size = len(line.encode("utf-8"))
        if size > budget:
            lines.append(truncation)
            break
        lines.append(line)
        budget -= size
    return "".join(lines) + footer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--base", required=True)
    parser.add_argument("--target", default="HEAD")
    parser.add_argument("--summary", type=Path, help="Append the report to this file.")
    args = parser.parse_args()

    base = target = "unavailable"
    exit_code = 0
    try:
        base = commit(args.root, args.base, "Base")
        target = commit(args.root, args.target, "Target")
        rows = compare(args.root, base, target)
    except (OSError, ValueError) as exc:
        reason = (
            str(exc)
            if isinstance(exc, ValueError)
            else "The repository or Git could not be read."
        )
        rows = [Row("Unverified", "Comparison", "", reason)]
        exit_code = 2

    report = render(base, target, rows)
    if args.summary is None:
        sys.stdout.write(report)
    else:
        try:
            with args.summary.open("a", encoding="utf-8") as summary:
                summary.write(report)
        except OSError:
            sys.stderr.write("Could not write the documentation report summary.\n")
            return 2
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
