"""Exercise the Claude manifest, Claude catalog and CLAUDE.md package contracts."""

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPOSITORY = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "claude_package_validator", REPOSITORY / "validators/plugin/validate.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

PACKAGE_FILES = [
    "VERSION",
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "AGENTS.md",
    "CLAUDE.md",
    "project-templates/base/AGENTS.md",
    "project-templates/base/CLAUDE.md",
    "project-templates/base/.versat/standards.lock",
]


class ClaudePackageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="harness-claude-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for directory in VALIDATOR.CANONICAL_DIRECTORIES:
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        files = PACKAGE_FILES + [
            f"skills/{name}/SKILL.md" for name in VALIDATOR.EXPECTED_SKILLS
        ]
        for relative in files:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, destination)
        self.version = (REPOSITORY / "VERSION").read_text().strip()
        patcher = patch.object(VALIDATOR, "ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def read(self, relative):
        return json.loads((self.root / relative).read_text())

    def write(self, relative, data):
        (self.root / relative).write_text(json.dumps(data))

    def assert_rejected(self, fragment):
        errors = VALIDATOR.validate()
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_current_package_is_valid(self):
        self.assertEqual(VALIDATOR.validate(), [])

    def test_manifest_mirrors_portable_identity(self):
        for field, value in (
            ("name", "versat"),
            ("version", "0.0.0"),
            ("description", "Other"),
            ("repository", "https://example.invalid/other"),
        ):
            with self.subTest(field=field):
                manifest = json.loads(
                    (REPOSITORY / ".claude-plugin/plugin.json").read_text()
                )
                manifest[field] = value
                self.write(".claude-plugin/plugin.json", manifest)
                self.assert_rejected(f"Claude Plugin {field}")

    def test_manifest_must_not_register_role_guidance(self):
        for agents in (None, ["./agents/architect.md"]):
            with self.subTest(agents=agents):
                manifest = self.read(".claude-plugin/plugin.json")
                if agents is None:
                    manifest.pop("agents", None)
                else:
                    manifest["agents"] = agents
                self.write(".claude-plugin/plugin.json", manifest)
                self.assert_rejected("Claude Plugin agents")

    def test_missing_claude_files_are_rejected(self):
        for relative in (
            ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json",
        ):
            with self.subTest(relative=relative):
                backup = (self.root / relative).read_bytes()
                (self.root / relative).unlink()
                self.assert_rejected(f"missing {relative}")
                (self.root / relative).write_bytes(backup)

    def test_catalog_identity_and_owner(self):
        catalog = self.read(".claude-plugin/marketplace.json")
        catalog["name"] = "versat-internal"
        self.write(".claude-plugin/marketplace.json", catalog)
        self.assert_rejected("Claude marketplace name")
        for owner in (None, {}, {"name": ""}):
            with self.subTest(owner=owner):
                catalog = self.read(".claude-plugin/marketplace.json")
                catalog["name"] = "versat"
                catalog["owner"] = owner
                self.write(".claude-plugin/marketplace.json", catalog)
                self.assert_rejected("Claude marketplace owner")

    def test_catalog_requires_exactly_one_entry(self):
        catalog = self.read(".claude-plugin/marketplace.json")
        entry = catalog["plugins"][0]
        for plugins in ([], [entry, dict(entry)], [{**entry, "name": "other"}]):
            with self.subTest(count=len(plugins)):
                catalog["plugins"] = plugins
                self.write(".claude-plugin/marketplace.json", catalog)
                self.assert_rejected("exactly one versat-ai-harness entry")

    def test_catalog_source_must_be_exact_github_tag(self):
        cases = (
            ("source", "url", "Claude marketplace source type"),
            ("source", "./", "Claude marketplace source type"),
            ("repo", "someone/fork", "Claude marketplace repository"),
            ("ref", "main", "Claude marketplace release reference"),
            ("ref", "latest", "Claude marketplace release reference"),
            ("ref", "v0.3.0", "Claude marketplace release reference"),
            ("ref", None, "Claude marketplace release reference"),
        )
        for field, value, fragment in cases:
            with self.subTest(field=field, value=value):
                catalog = json.loads(
                    (REPOSITORY / ".claude-plugin/marketplace.json").read_text()
                )
                catalog["plugins"][0]["source"][field] = value
                self.write(".claude-plugin/marketplace.json", catalog)
                self.assert_rejected(fragment)

    def test_catalogs_select_the_same_release(self):
        codex = self.read(".agents/plugins/marketplace.json")
        claude = self.read(".claude-plugin/marketplace.json")
        self.assertEqual(
            codex["plugins"][0]["source"]["ref"], claude["plugins"][0]["source"]["ref"]
        )
        claude["plugins"][0]["source"]["ref"] = "v9.9.9"
        self.write(".claude-plugin/marketplace.json", claude)
        self.assert_rejected("must select the same release")

    def test_claude_instruction_entry_points(self):
        for base in ("", "project-templates/base/"):
            for content, fragment in (
                (None, "CLAUDE.md is missing"),
                ("# Rules\n", "does not import @AGENTS.md"),
                ("@AGENTS.md\nAlways use tabs.\n", "beyond the @AGENTS.md import"),
            ):
                with self.subTest(base=base, content=content):
                    path = self.root / f"{base}CLAUDE.md"
                    if content is None:
                        path.unlink()
                    else:
                        path.write_text(content)
                    self.assert_rejected(f"{base}CLAUDE.md")
                    self.assert_rejected(fragment)
                    path.write_text("@AGENTS.md\n")

    def test_agents_md_remains_required(self):
        (self.root / "project-templates/base/AGENTS.md").unlink()
        self.assert_rejected("missing project-templates/base/AGENTS.md")


if __name__ == "__main__":
    unittest.main()
