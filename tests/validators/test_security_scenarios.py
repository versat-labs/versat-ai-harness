"""Verify scenario defects and independent replay without claiming agent behavior."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "security_scenarios", ROOT / "tests/skills/security/fixtures.py"
)
fixtures = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fixtures)


class SecurityScenarioTests(unittest.TestCase):
    def test_all_scenarios_replay_expected_evidence_without_touching_original(self):
        for case, code in zip(fixtures.CASES, (2, 1, 2)):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as directory:
                base = Path(directory)
                original = base / "project"
                before = fixtures.prepare(original, case, "a" * 64)
                result = fixtures.replay(original, base / "replay")
                self.assertEqual(result["snapshot"]["exit_code"], code)
                self.assertEqual(result["render"]["exit_code"], 0)
                self.assertEqual(result["tests"]["exit_code"], 0)
                self.assertTrue(result["original_unchanged"])
                self.assertEqual(fixtures.manifest(original), before)
                report = json.loads((base / "replay/report.json").read_text())
                self.assertFalse(report["public_ready"])
                self.assertEqual(report["mode"], "snapshot")
                controls = {c["id"]: c for c in report["controls"]}
                if case == "public-audit-drift":
                    for name in (
                        "main.dismiss_stale_reviews",
                        "secrets.secret_scanning_push_protection",
                    ):
                        self.assertEqual(controls[name]["result"], "fail")
                if case == "public-maintenance-conflict":
                    self.assertEqual(
                        controls["codeowners"]["result"], "unable-to-verify"
                    )
                    self.assertEqual(
                        controls["main.check-contexts"]["evidence"],
                        ["consumer-security", "consumer-tests"],
                    )

    def test_fixture_and_replay_refuse_existing_destinations_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "project"
            fixtures.prepare(root, fixtures.CASES[0], "b" * 64)
            with self.assertRaises(ValueError):
                fixtures.prepare(root, fixtures.CASES[0], "b" * 64)
            with self.assertRaises(ValueError):
                fixtures.replay(root, root / "nested")
            (root / "link").symlink_to(root / "inputs/settings.json")
            with self.assertRaises(ValueError):
                fixtures.manifest(root)


if __name__ == "__main__":
    unittest.main()
