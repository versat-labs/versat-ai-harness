"""Exercise marketplace identity and retained package contracts in disposable roots."""

import importlib.util
import json
import re
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


REPOSITORY = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "marketplace_package_validator", REPOSITORY / "validators/plugin/validate.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class MarketplaceContractTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="harness-marketplace-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for directory in VALIDATOR.CANONICAL_DIRECTORIES:
            (self.root / directory).mkdir(parents=True)
        files = [
            "VERSION",
            "plugin.json",
            ".codex-plugin/plugin.json",
            "project-templates/base/.versat/standards.lock",
        ] + [f"skills/{name}/SKILL.md" for name in VALIDATOR.EXPECTED_SKILLS]
        for relative in files:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, destination)
        self.catalog_path = self.root / ".agents/plugins/marketplace.json"
        self.catalog_path.parent.mkdir(parents=True)
        self.catalog = json.loads(
            (
                REPOSITORY / "tests/fixtures/marketplace-transition/catalog.json"
            ).read_text()
        )
        self.root_patch = patch.object(VALIDATOR, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def errors(self):
        self.catalog_path.write_text(json.dumps(self.catalog))
        return VALIDATOR.validate()

    def assert_rejected(self, description):
        errors = self.errors()
        self.assertTrue(any(description in error for error in errors), errors)

    def test_target_identity_preserves_valid_package(self):
        self.assertEqual(self.errors(), [])

    def test_legacy_or_unrelated_identity_is_not_an_alias(self):
        for name in ("versat-internal", "another-marketplace"):
            with self.subTest(name=name):
                self.catalog["name"] = name
                self.assert_rejected("marketplace name")

    def test_empty_missing_or_non_string_name_is_rejected(self):
        for name in ("", None, 42):
            with self.subTest(name=name):
                self.catalog["name"] = name
                self.assert_rejected("marketplace name")
        del self.catalog["name"]
        self.assert_rejected("marketplace name")

    def test_wrong_empty_or_missing_label_is_rejected(self):
        for label in ("Versat Internal Plugins", "", None):
            with self.subTest(label=label):
                self.catalog["interface"]["displayName"] = label
                self.assert_rejected("marketplace display name")
        del self.catalog["interface"]["displayName"]
        self.assert_rejected("marketplace display name")

    def test_malformed_or_missing_interface_is_rejected(self):
        for interface in (None, "Versat Plugins", []):
            with self.subTest(interface=interface):
                self.catalog["interface"] = interface
                self.assert_rejected("marketplace interface must be an object")
        del self.catalog["interface"]
        self.assert_rejected("marketplace interface must be an object")

    def test_changed_plugin_entry_name_is_rejected(self):
        self.catalog["plugins"][0]["name"] = "another-plugin"
        self.assert_rejected("exactly one versat-ai-harness entry")

    def test_duplicate_harness_entry_is_rejected(self):
        self.catalog["plugins"].append(self.catalog["plugins"][0].copy())
        self.assert_rejected("exactly one versat-ai-harness entry")

    def test_package_reference_drift_or_latest_is_rejected(self):
        for reference in ("v0.3.0", "latest", "main", None):
            with self.subTest(reference=reference):
                self.catalog["plugins"][0]["source"]["ref"] = reference
                self.assert_rejected("marketplace release reference")

    def test_repository_redirect_is_rejected(self):
        self.catalog["plugins"][0]["source"]["url"] = (
            "https://example.invalid/other.git"
        )
        self.assert_rejected("marketplace repository URL")

    def test_manifest_name_drift_is_rejected(self):
        path = self.root / "plugin.json"
        data = json.loads(path.read_text())
        data["name"] = "versat"
        path.write_text(json.dumps(data))
        self.assert_rejected("portable Plugin name")

    def test_manifest_version_drift_is_rejected(self):
        path = self.root / ".codex-plugin/plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "0.0.0"
        path.write_text(json.dumps(data))
        self.assert_rejected("compatibility Plugin version")

    def test_root_resource_and_skill_contracts_remain_required(self):
        (self.root / "schemas").rmdir()
        (self.root / "skills/versat-sdd/SKILL.md").unlink()
        errors = self.errors()
        self.assertIn("missing canonical directory: schemas/", errors)
        self.assertIn("missing skills/versat-sdd/SKILL.md", errors)


class CopiedPackageResourceTests(unittest.TestCase):
    """Resolve actual Skill links after relocation, without invoking a native client."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="harness-copied-package-")
        self.addCleanup(temporary.cleanup)
        self.root = (Path(temporary.name) / "package").resolve()
        shutil.copytree(
            REPOSITORY,
            self.root,
            ignore=shutil.ignore_patterns(".git", "__pycache__"),
        )

    def unresolved_resources(self):
        missing = []
        for name in VALIDATOR.EXPECTED_SKILLS:
            skill = self.root / "skills" / name / "SKILL.md"
            # Every capability resolves its matching package via this relative root.
            package = (skill.parent / "../..").resolve()
            self.assertEqual(package, self.root.resolve())
            paths = [
                package / "VERSION",
                package / "standards/index.yaml",
                package / "sdd/process.md",
            ]
            paths.extend(package / part for part in VALIDATOR.CANONICAL_DIRECTORIES)
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", skill.read_text()):
                if ":" not in target:
                    paths.append((skill.parent / target.split("#", 1)[0]).resolve())
            for resource in paths:
                self.assertTrue(resource.is_relative_to(self.root.resolve()))
                if not resource.exists():
                    missing.append((name, str(resource.relative_to(self.root))))
                elif resource.is_file():
                    self.assertEqual(
                        resource.read_bytes(),
                        (REPOSITORY / resource.relative_to(self.root)).read_bytes(),
                    )
        return missing

    def test_packaged_skills_resolve_matching_resources_after_package_copy(self):
        packaged = {
            path.parent.name for path in (self.root / "skills").glob("*/SKILL.md")
        }
        self.assertSetEqual(packaged, set(VALIDATOR.EXPECTED_SKILLS))
        self.assertEqual(self.unresolved_resources(), [])

    def test_missing_index_is_detected_from_each_skill_directory(self):
        (self.root / "standards/index.yaml").unlink()
        failures = set(self.unresolved_resources())
        for name in VALIDATOR.EXPECTED_SKILLS:
            self.assertIn((name, "standards/index.yaml"), failures)


if __name__ == "__main__":
    unittest.main()
