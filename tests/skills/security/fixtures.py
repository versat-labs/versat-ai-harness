"""Disposable public-security scenarios; no production access or live assertions."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

import yaml

sys.dont_write_bytecode = True
PACKAGE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PACKAGE / "tests/fixtures/security"))
from security_fixtures import REPO, data, snapshot  # noqa: E402 - standalone fixture path

CASES = (
    "public-bootstrap-unavailable",
    "public-audit-drift",
    "public-maintenance-conflict",
)


def manifest(root):
    result = {}
    for path in sorted(Path(root).rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlink in fixture")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return result


def prepare(root, case, source_digest):
    root = Path(root)
    if case not in CASES or root.is_symlink() or root.exists():
        raise ValueError("Expected a fresh fixture path and supported case")
    root.mkdir(parents=True)
    for name in (".versat", ".github", "specs/product", "tests", "inputs"):
        (root / name).mkdir(parents=True)
    identity = {
        "schema_version": 1,
        "project": {
            "name": "security-fixture",
            "description": "Synthetic public payment library",
            "profile": "library",
            "domain": "finance",
            "owner": "Synthetic evaluator",
            "visibility": "public",
            "criticality": "medium",
        },
        "technologies": ["python"],
    }
    index = yaml.safe_load((PACKAGE / "standards/index.yaml").read_text())
    paths = set(index["core"]["always"])
    for group, key in (
        ("profiles", "library"),
        ("domains", "finance"),
        ("criticality", "medium"),
        ("technologies", "python"),
    ):
        paths.update(index[group][key])
    version = (PACKAGE / "VERSION").read_text().strip()
    lock = {
        "schema_version": 1,
        "harness": {
            "version": version,
            "commit": "development-snapshot:" + source_digest,
        },
        "resolved_at": "synthetic-evaluation",
        "standards": [
            {
                "path": name,
                "version": version,
                "digest": hashlib.sha256(
                    (PACKAGE / "standards" / name).read_bytes()
                ).hexdigest(),
            }
            for name in sorted(paths)
        ],
    }
    (root / ".versat/project.yaml").write_text(yaml.safe_dump(identity))
    (root / ".versat/standards.lock").write_text(yaml.safe_dump(lock))
    (root / "AGENTS.md").write_text(
        "Synthetic evaluation only. Use the supplied provider source and its index. "
        "The development lock records a source digest, not a published clean release. "
        "No external service, authentication, credentials or remote operations are authorized. "
        "Preserve existing files; put review artifacts in the supplied separate output directory.\n"
    )
    (root / "specs/product/overview.md").write_text(
        "# Synthetic payment library\n\nProvide integrators a pure positive-amount validation "
        "helper. Python library, no persistence, credentials, deployment or external services. "
        "Product discovery and library profile are already selected for this fixture.\n"
    )
    (root / "tests/test_amount.py").write_text(
        "import unittest\n\ndef validate(amount):\n"
        "    if amount <= 0: raise ValueError('positive amount required')\n"
        "    return amount\n\nclass Amount(unittest.TestCase):\n"
        "    def test_positive(self): self.assertEqual(validate(1), 1)\n"
        "    def test_boundary(self):\n"
        "        with self.assertRaises(ValueError): validate(0)\n"
    )
    observed = snapshot()
    if case == "public-bootstrap-unavailable":
        observed["complete"] = observed["stable"] = False
        observed["observations"] = {
            key: {"status": "unverified", "diagnostic": "no-administrative-access"}
            for key in observed["observations"]
        }
    elif case == "public-audit-drift":
        data(observed, "protection")["required_pull_request_reviews"][
            "dismiss_stale_reviews"
        ] = False
        data(observed, "repository")["security_and_analysis"][
            "secret_scanning_push_protection"
        ]["status"] = "disabled"
    else:
        data(observed, "protection")["required_pull_request_reviews"][
            "required_approving_review_count"
        ] = 2
        data(observed, "protection")["required_status_checks"]["contexts"] = [
            "consumer-security",
            "consumer-tests",
        ]
        data(observed, "codeowners")["rows"].append(
            {"pattern": "/special/", "owners": ["@synthetic-specialist"]}
        )
        (root / ".github/CODEOWNERS").write_text(
            "* @elviszoz @evertonspohrversat\n/special/ @synthetic-specialist\n"
        )
    (root / "inputs/settings.json").write_text(json.dumps(observed, indent=2) + "\n")
    (root / "inputs/context.json").write_text(
        json.dumps(
            {
                "case": case,
                "repository": REPO,
                "provider_source_digest": source_digest,
                "provider_version": version,
                "live_access": False,
            },
            indent=2,
        )
        + "\n"
    )
    return manifest(root)


def replay(original, output):
    """Copy preserved inputs and independently run the actual CLI and renderer."""
    original, output = Path(original), Path(output)
    manifest(original)
    if output.exists() or output.is_relative_to(original):
        raise ValueError("Replay needs a fresh independent destination")
    shutil.copytree(original, output / "project")
    project = output / "project"
    commands = {
        "snapshot": [
            sys.executable,
            "-B",
            str(PACKAGE / "validators/security/validate.py"),
            "--repository",
            REPO,
            "--snapshot",
            str(project / "inputs/settings.json"),
            "--output",
            str(output / "report.json"),
        ],
        "render": [
            sys.executable,
            "-B",
            str(PACKAGE / "scripts/bootstrap/public_security.py"),
            "--output",
            str(output / "staging"),
        ],
        "tests": [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"],
    }
    results = {}
    for name, argv in commands.items():
        run = subprocess.run(
            argv, cwd=project, capture_output=True, text=True, timeout=30
        )
        (output / f"{name}.stdout").write_text(run.stdout)
        (output / f"{name}.stderr").write_text(run.stderr)
        results[name] = {"argv": argv, "exit_code": run.returncode}
    results["original_unchanged"] = manifest(original) == manifest(project)
    (output / "replay.json").write_text(json.dumps(results, indent=2) + "\n")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=CASES, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-digest", required=True)
    args = parser.parse_args()
    print(json.dumps(prepare(args.output, args.case, args.source_digest), indent=2))
