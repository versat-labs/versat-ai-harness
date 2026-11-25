"""Control-specific regressions for actual supported GitHub enforcement shapes."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests/fixtures/security"))
from security_fixtures import REPO, data, rule_set, snapshot  # noqa: E402 - standalone provider/test path bootstrap
from validators.security.policy import aggregate, evaluate, load_policy  # noqa: E402 - standalone provider/test path bootstrap


class SecurityPolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy, _ = load_policy()
        self.snapshot = snapshot()

    def controls(self, value=None):
        controls, _ = evaluate(value or self.snapshot, self.policy, REPO)
        return {x["id"]: x for x in controls}

    def test_classic_main_and_admin_reference_exceptions_compose(self):
        controls, applicability = evaluate(self.snapshot, self.policy, REPO)
        self.assertEqual(aggregate(controls, applicability), "pass")
        self.assertEqual(
            self.controls()["main.check-contexts"]["evidence"],
            ["custom-required-check"],
        )

    def test_each_review_control_is_independently_required(self):
        for field in (
            "required_approving_review_count",
            "require_code_owner_reviews",
            "dismiss_stale_reviews",
            "require_last_push_approval",
        ):
            with self.subTest(field=field):
                value = snapshot()
                data(value, "protection")["required_pull_request_reviews"][field] = (
                    0 if field == "required_approving_review_count" else False
                )
                control = (
                    "main.approvals"
                    if field == "required_approving_review_count"
                    else "main." + field
                )
                self.assertEqual(self.controls(value)[control]["result"], "fail")

    def test_stronger_reviews_preserved_and_one_owner_is_minimum(self):
        self.assertEqual(self.controls()["main.approvals"]["result"], "pass")
        data(self.snapshot, "protection")["required_pull_request_reviews"][
            "required_approving_review_count"
        ] = 2
        self.assertEqual(self.controls()["main.approvals"]["result"], "pass")

    def test_admin_and_review_bypass_do_not_establish_main_protection(self):
        for mutation in ("admin", "user", "app", "team"):
            value = snapshot()
            if mutation == "admin":
                data(value, "protection")["enforce_admins"]["enabled"] = False
            else:
                data(value, "protection")["required_pull_request_reviews"][
                    "bypass_pull_request_allowances"
                ] = {mutation: ["actor"]}
            self.assertEqual(self.controls(value)["main.approvals"]["result"], "fail")

    def test_force_and_deletion_controls(self):
        for name in ("allow_force_pushes", "allow_deletions"):
            value = snapshot()
            data(value, "protection")[name]["enabled"] = True
            self.assertEqual(self.controls(value)["main." + name]["result"], "fail")

    def all_ruleset(self):
        value = snapshot()
        main = rule_set(12, "branch", main=True)
        main["rules"] = [
            {
                "type": "pull_request",
                # Independent GitHub ruleset wire fixture, not classic protection keys.
                "parameters": {
                    "required_approving_review_count": 1,
                    "require_code_owner_review": True,
                    "dismiss_stale_reviews_on_push": True,
                    "require_last_push_approval": True,
                    "required_review_thread_resolution": False,
                },
            },
            {"type": "non_fast_forward"},
            {"type": "deletion"},
        ]
        data(value, "rulesets").append(main)
        data(value, "main_rules").extend(
            {"ruleset_id": 12, "type": x["type"]} for x in main["rules"]
        )
        value["observations"]["protection"] = {"status": "absent"}
        return value

    def test_all_ruleset_deployment(self):
        value = self.all_ruleset()
        controls, applicability = evaluate(value, self.policy, REPO)
        self.assertEqual(aggregate(controls, applicability), "pass")

    def test_ruleset_wire_review_flags_are_independently_required(self):
        for wire, control in (
            ("require_code_owner_review", "require_code_owner_reviews"),
            ("dismiss_stale_reviews_on_push", "dismiss_stale_reviews"),
            ("require_last_push_approval", "require_last_push_approval"),
        ):
            value = self.all_ruleset()
            data(value, "rulesets")[-1]["rules"][0]["parameters"][wire] = False
            self.assertEqual(self.controls(value)["main." + control]["result"], "fail")
            del data(value, "rulesets")[-1]["rules"][0]["parameters"][wire]
            self.assertEqual(
                self.controls(value)["main." + control]["result"], "unable-to-verify"
            )

    def test_inherited_rules_and_split_guarantees(self):
        value = self.all_ruleset()
        source = data(value, "rulesets")[-1]
        moved = source["rules"].pop()
        another = deepcopy(source)
        another.update(
            id=13, source_type="Organization", source="example-owner", rules=[moved]
        )
        data(value, "rulesets").append(another)
        data(value, "main_rules").append({"ruleset_id": 13, "type": "deletion"})
        self.assertEqual(self.controls(value)["main.allow_deletions"]["result"], "pass")

    def test_permissive_source_cannot_weaken_strict_independent_source(self):
        value = self.all_ruleset()
        value["observations"]["protection"] = snapshot()["observations"]["protection"]
        data(value, "rulesets")[-1]["bypass_actors"] = [
            {"actor_type": "RepositoryRole", "actor_id": 5, "bypass_mode": "always"}
        ]
        self.assertEqual(self.controls(value)["main.approvals"]["result"], "pass")

    def test_missing_or_hidden_main_protection(self):
        for status, expected in (
            ("absent", "fail"),
            ("unverified", "unable-to-verify"),
        ):
            value = snapshot()
            value["observations"]["protection"] = {"status": status}
            self.assertEqual(self.controls(value)["main.approvals"]["result"], expected)
        value = self.all_ruleset()
        del data(value, "rulesets")[-1]["bypass_actors"]
        self.assertEqual(
            self.controls(value)["main.approvals"]["result"], "unable-to-verify"
        )

    def test_main_ruleset_bypass_or_non_active_state(self):
        for state in ("disabled", "evaluate", "bypass"):
            value = self.all_ruleset()
            rule = data(value, "rulesets")[-1]
            if state == "bypass":
                rule["bypass_actors"] = [
                    {
                        "actor_type": "Integration",
                        "actor_id": 7,
                        "bypass_mode": "always",
                    }
                ]
            else:
                rule["enforcement"] = state
            self.assertEqual(self.controls(value)["main.approvals"]["result"], "fail")

    def test_each_ref_target_and_operation(self):
        for index, target in enumerate(("branch", "tag")):
            for operation in ("creation", "update", "deletion"):
                value = snapshot()
                rule = data(value, "rulesets")[index]
                rule["rules"] = [r for r in rule["rules"] if r["type"] != operation]
                self.assertEqual(
                    self.controls(value)[f"refs.{target}.{operation}"]["result"], "fail"
                )

    def test_reference_bypass_is_only_repository_administrators(self):
        for actor in (
            {"actor_type": "RepositoryRole", "actor_id": 4, "bypass_mode": "always"},
            {"actor_type": "Integration", "actor_id": 1, "bypass_mode": "always"},
            {
                "actor_type": "RepositoryRole",
                "actor_id": 5,
                "bypass_mode": "pull_request",
            },
            {"actor_type": "RepositoryRole", "actor_id": 5, "bypass_mode": "exempt"},
        ):
            value = snapshot()
            data(value, "rulesets")[0]["bypass_actors"] = [actor]
            self.assertEqual(
                self.controls(value)["refs.branch.update"]["result"], "fail"
            )

    def test_partial_patterns_and_exclusions_do_not_prove_future_nested_refs(self):
        for condition in (
            {"include": ["refs/heads/*"], "exclude": []},
            {"include": ["~ALL"], "exclude": ["refs/heads/private/**"]},
        ):
            value = snapshot()
            data(value, "rulesets")[0]["conditions"]["ref_name"] = condition
            self.assertEqual(
                self.controls(value)["refs.branch.creation"]["result"],
                "unable-to-verify",
            )

    def test_permissive_fetch_and_merge_fails(self):
        data(self.snapshot, "rulesets")[0]["rules"][1]["parameters"] = {
            "update_allows_fetch_and_merge": True
        }
        self.assertEqual(self.controls()["refs.branch.update"]["result"], "fail")

    def test_owners_overrides_errors_permissions_and_base(self):
        mutations = [
            lambda s: data(s, "codeowners")["rows"].append(
                {"pattern": "/docs/", "owners": []}
            ),
            lambda s: data(s, "codeowners")["rows"].append(
                {"pattern": "/docs/", "owners": ["@stranger"]}
            ),
            lambda s: data(s, "codeowners_errors")["errors"].append(
                {"kind": "Invalid owner"}
            ),
            lambda s: data(s, "owner_permissions").update(elviszoz="read"),
            lambda s: data(s, "codeowners").update(sha="b" * 40),
            lambda s: data(s, "codeowners")["rows"].clear(),
        ]
        for mutation in mutations:
            value = snapshot()
            mutation(value)
            self.assertNotEqual(self.controls(value)["codeowners"]["result"], "pass")
        data(self.snapshot, "codeowners")["rows"].append(
            {
                "pattern": "/.github/CODEOWNERS",
                "owners": ["@elviszoz", "@evertonspohrversat"],
            }
        )
        self.assertEqual(self.controls()["codeowners"]["result"], "pass")

    def test_secret_and_participation_controls(self):
        for feature in ("secret_scanning", "secret_scanning_push_protection"):
            value = snapshot()
            data(value, "repository")["security_and_analysis"][feature]["status"] = (
                "disabled"
            )
            self.assertEqual(
                self.controls(value)["secrets." + feature]["result"], "fail"
            )
        for key, actual in (
            ("allow_forking", False),
            ("pull_request_creation_policy", "collaborators_only"),
        ):
            value = snapshot()
            data(value, "repository")[key] = actual
            self.assertEqual(
                self.controls(value)["participation." + key]["result"], "fail"
            )

    def test_missing_fields_are_not_success(self):
        del data(self.snapshot, "repository")["security_and_analysis"]
        self.assertEqual(
            self.controls()["secrets.secret_scanning"]["result"], "unable-to-verify"
        )
        self.snapshot["observations"]["owner_permissions"] = {"status": "unverified"}
        self.assertEqual(self.controls()["codeowners"]["result"], "unable-to-verify")

    def test_identity_applicability_and_unknowns(self):
        controls, applicability = evaluate(self.snapshot, self.policy, "different/repo")
        self.assertEqual(aggregate(controls, applicability), "fail")
        data(self.snapshot, "repository")["visibility"] = "private"
        self.assertEqual(
            evaluate(self.snapshot, self.policy, REPO)[1], "not-applicable"
        )
        controls, applicability = evaluate(self.snapshot, self.policy, REPO, "public")
        self.assertEqual(aggregate(controls, applicability), "fail")

    def test_incomplete_or_unstable_collection_cannot_pass(self):
        for key in ("complete", "stable"):
            value = snapshot()
            value[key] = False
            self.assertEqual(
                self.controls(value)["collection." + key]["result"], "unable-to-verify"
            )


if __name__ == "__main__":
    unittest.main()
