"""Synthetic GitHub observations, independent of the renderer and evaluator."""

from copy import deepcopy

REPO = "example-owner/security-fixture"
SHA = "a" * 40


def rule_set(rule_id, target, main=False):
    return {
        "id": rule_id,
        "target": target,
        "enforcement": "active",
        "source_type": "Repository",
        "source": REPO,
        "conditions": {
            "ref_name": {
                "include": ["refs/heads/main"] if main else ["~ALL"],
                "exclude": [],
            }
        },
        "bypass_actors": []
        if main
        else [{"actor_type": "RepositoryRole", "actor_id": 5, "bypass_mode": "always"}],
        "rules": [{"type": name} for name in ("creation", "update", "deletion")],
    }


def snapshot():
    values = {
        "repository": {
            "id": 123,
            "full_name": REPO,
            "visibility": "public",
            "default_branch": "main",
            "allow_forking": True,
            "has_pull_requests": True,
            "pull_request_creation_policy": "all",
            "security_and_analysis": {
                "secret_scanning": {"status": "enabled"},
                "secret_scanning_push_protection": {"status": "enabled"},
            },
        },
        "main": {"name": "main", "sha": SHA},
        "protection": {
            "enforce_admins": {"enabled": True},
            "allow_force_pushes": {"enabled": False},
            "allow_deletions": {"enabled": False},
            "required_pull_request_reviews": {
                "required_approving_review_count": 1,
                "require_code_owner_reviews": True,
                "dismiss_stale_reviews": True,
                "require_last_push_approval": True,
            },
            "required_status_checks": {
                "contexts": ["custom-required-check"],
                "strict": True,
            },
        },
        "rulesets": [rule_set(10, "branch"), rule_set(11, "tag")],
        "main_rules": [
            {"type": name, "ruleset_id": 10}
            for name in ("creation", "update", "deletion")
        ],
        "codeowners": {
            "path": ".github/CODEOWNERS",
            "sha": SHA,
            "rows": [{"pattern": "*", "owners": ["@elviszoz", "@evertonspohrversat"]}],
        },
        "codeowners_errors": {"errors": []},
        "owner_permissions": {"elviszoz": "admin", "evertonspohrversat": "admin"},
    }
    return {
        "schema_version": 1,
        "repository": REPO,
        "started_at": "2026-01-01T00:00:00+00:00",
        "finished_at": "2026-01-01T00:00:01+00:00",
        "complete": True,
        "stable": True,
        "observations": {
            key: {"status": "ok", "data": deepcopy(value)}
            for key, value in values.items()
        },
    }


def data(value, name):
    return value["observations"][name]["data"]
