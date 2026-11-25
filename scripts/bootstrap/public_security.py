"""Render security assets into local staging without changing GitHub."""

import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
PACKAGE = Path(__file__).resolve().parents[2]
if str(PACKAGE) not in sys.path:
    sys.path.insert(0, str(PACKAGE))

from validators.security.policy import RULESET_REVIEW_FIELDS, load_policy, output_path  # noqa: E402 - standalone provider/test path bootstrap


def assets(policy):
    conditions = {"ref_name": {"include": ["~ALL"], "exclude": []}}
    result = {
        ".github/CODEOWNERS": "* "
        + " ".join("@" + x for x in policy["codeowners"])
        + "\n"
    }
    for target in policy["references"]["targets"]:
        result[f".github/security/{target}-administration.json"] = {
            "name": f"Versat administrators manage {target}s",
            "target": target,
            "enforcement": "active",
            "bypass_actors": [policy["references"]["bypass_actor"]],
            "conditions": conditions,
            "rules": [
                {
                    "type": x,
                    **(
                        {"parameters": {"update_allows_fetch_and_merge": False}}
                        if x == "update"
                        else {}
                    ),
                }
                for x in policy["references"]["operations"]
            ],
        }
    result[".github/security/main-protection.json"] = {
        "name": "Versat main protection",
        "target": "branch",
        "enforcement": "active",
        "bypass_actors": [],
        "conditions": {
            "ref_name": {
                "include": ["refs/heads/" + policy["default_branch"]],
                "exclude": [],
            }
        },
        "rules": [
            {
                "type": "pull_request",
                "parameters": {
                    "required_approving_review_count": policy["main"][
                        "required_approvals"
                    ],
                    **{
                        RULESET_REVIEW_FIELDS[key]: value
                        for key, value in policy["main"]["review_flags"].items()
                    },
                    # Required API field; this baseline adds no conversation-resolution policy.
                    "required_review_thread_resolution": False,
                },
            },
            {"type": "deletion"},
            {"type": "non_fast_forward"},
        ],
    }
    result[".github/security/secret-settings.json"] = {
        "security_and_analysis": {
            key: {"status": "enabled"} for key in policy["secret_features"]
        }
    }
    return {
        path: value if isinstance(value, str) else json.dumps(value, indent=2) + "\n"
        for path, value in result.items()
    }


def render(output, package=PACKAGE):
    policy, identity = load_policy(package)
    rendered = assets(policy)
    manifest = {
        "schema_version": 1,
        "provider_version": (package / "VERSION").read_text().strip(),
        "policy": identity,
        "assets": {
            path: hashlib.sha256(content.encode()).hexdigest()
            for path, content in rendered.items()
        },
    }
    rendered[".github/security/manifest.json"] = json.dumps(manifest, indent=2) + "\n"
    output = output_path(output)
    # Preflight every destination before creating any files.
    for name, content in rendered.items():
        dest = output / name
        for part in (dest, *dest.parents):
            if part.is_symlink():
                raise ValueError("Symlink destination")
            if part != dest and part.exists() and not part.is_dir():
                raise ValueError("Parent is not a directory")
        if dest.exists() and (not dest.is_file() or dest.read_text() != content):
            raise ValueError(f"Conflicting existing asset: {name}")
    for name, content in rendered.items():
        dest = output / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            with dest.open("x", encoding="utf-8") as handle:
                handle.write(content)
    return {
        "result": "pass",
        "applied_to_github": False,
        "public_ready": False,
        "output": str(output),
        **manifest,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(render(args.output)))
        return 0
    except (ValueError, OSError) as exc:
        print(
            json.dumps(
                {"result": "fail", "diagnostic": str(exc), "public_ready": False}
            )
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
