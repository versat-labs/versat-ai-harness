"""Assess public repository controls without modifying GitHub."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
PACKAGE = Path(__file__).resolve().parents[2]
if str(PACKAGE) not in sys.path:
    sys.path.insert(0, str(PACKAGE))

from scripts.security.github import GitHub, collect  # noqa: E402 - standalone provider/test path bootstrap
from validators.security.policy import (  # noqa: E402 - standalone provider path bootstrap
    aggregate,
    evaluate,
    load_policy,
    output_path,
    read_yaml,
    schema_check,
)


def write_report(path, report):
    path = output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
        json.dump(report, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def provider_identity(project_root=None):
    version = (PACKAGE / "VERSION").read_text().strip()
    commit = subprocess.run(
        ["git", "-C", str(PACKAGE), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    dirty = (
        subprocess.run(
            [
                "git",
                "-C",
                str(PACKAGE),
                "status",
                "--porcelain",
                "--untracked-files=all",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        != ""
    )
    identity = {"version": version, "commit": commit, "dirty": dirty, "mode": "source"}
    visibility = None
    if project_root is not None:
        # Reuse the exact installed provider resolver; never import consumer code.
        result = subprocess.run(
            [
                sys.executable,
                "-B",
                str(PACKAGE / "scripts/testing/provider.py"),
                "--root",
                str(project_root),
            ],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise ValueError("Exact consumer provider verification failed")
        identity["mode"] = "locked-consumer"
        visibility = read_yaml(Path(project_root) / ".versat/project.yaml")["project"][
            "visibility"
        ]
    return identity, visibility


def assess(
    snapshot,
    policy,
    policy_identity,
    provider,
    repository,
    mode,
    declared_visibility=None,
):
    schema_check(snapshot, "repository-security-snapshot.schema.yaml")
    controls, applicability = evaluate(
        snapshot, policy, repository, declared_visibility
    )
    result = aggregate(controls, applicability)
    report = {
        "schema_version": 1,
        "repository": repository,
        "mode": mode,
        "applicability": applicability,
        "result": result,
        "public_ready": mode == "live"
        and result == "pass"
        and applicability == "applicable",
        "policy": policy_identity,
        "provider": provider,
        "controls": controls,
        "evidence": snapshot,
    }
    schema_check(report, "repository-security-report.schema.yaml")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check-policy", action="store_true")
    mode.add_argument("--snapshot", type=Path)
    mode.add_argument("--live", action="store_true")
    parser.add_argument("--repository")
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    selected_mode = (
        "policy" if args.check_policy else "snapshot" if args.snapshot else "live"
    )
    report = {
        "schema_version": 1,
        "repository": args.repository or "",
        "mode": selected_mode,
        "applicability": "unknown",
        "result": "unable-to-verify",
        "public_ready": False,
        "policy": {},
        "provider": {},
        "controls": [],
        "evidence": {},
    }
    try:
        policy, policy_identity = load_policy()
        provider, visibility = provider_identity(args.project_root)
        report.update(policy=policy_identity, provider=provider)
        if args.check_policy:
            report["result"] = "pass"
        else:
            if not args.repository:
                raise ValueError("An explicit repository is required")
            GitHub(args.repository)  # Identity validation also applies to offline mode.
            snapshot = (
                json.loads(args.snapshot.read_text())
                if args.snapshot
                else collect(args.repository, policy)
            )
            report = assess(
                snapshot,
                policy,
                policy_identity,
                provider,
                args.repository,
                selected_mode,
                visibility,
            )
    except Exception as exc:
        # Do not print exceptions containing API bodies, invalid inputs or credentials.
        report["controls"].append(
            {
                "id": "execution",
                "result": "unable-to-verify",
                "diagnostic": type(exc).__name__,
                "remediation": "Check policy/schema, explicit repository, provider identity and required read access.",
                "evidence": None,
            }
        )
        report.update(result="unable-to-verify", public_ready=False)
    if args.output:
        try:
            write_report(args.output, report)
        except (OSError, ValueError):
            print("Unable to write a safe report destination.", file=sys.stderr)
            return 2
    print(
        json.dumps(
            report
            if not args.output
            else {
                "result": report["result"],
                "mode": selected_mode,
                "public_ready": report["public_ready"],
                "report": str(args.output),
            },
            ensure_ascii=True,
        )
    )
    return {"pass": 0, "fail": 1, "unable-to-verify": 2, "not-applicable": 3}[
        report["result"]
    ]


if __name__ == "__main__":
    sys.exit(main())
