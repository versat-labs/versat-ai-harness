"""Exercise the read-only consumer CLAUDE.md entry-point check."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
SCRIPT = REPOSITORY / "validators/project/instructions.py"
SPEC = importlib.util.spec_from_file_location("project_instructions_test", SCRIPT)
INSTRUCTIONS = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = INSTRUCTIONS
SPEC.loader.exec_module(INSTRUCTIONS)


class ProjectInstructionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="project-instructions-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "AGENTS.md").write_text("# Project instructions\n")

    def run_cli(self, *extra):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), *extra],
            capture_output=True,
            text=True,
            check=False,
        )

    def snapshot(self):
        return {
            path.name: (path.is_symlink(), path.read_bytes() if path.is_file() else b"")
            for path in sorted(self.root.iterdir())
        }

    def test_import_only_file_is_compliant(self):
        for content in ("@AGENTS.md\n", "\n@AGENTS.md\n\n", "  @AGENTS.md"):
            with self.subTest(content=content):
                (self.root / "CLAUDE.md").write_text(content)
                self.assertEqual(INSTRUCTIONS.check(self.root), [])
                self.assertEqual(self.run_cli().returncode, 0)

    def test_project_without_agents_md_is_not_applicable(self):
        (self.root / "AGENTS.md").unlink()
        self.assertEqual(INSTRUCTIONS.check(self.root), [])
        (self.root / "CLAUDE.md").write_text("Custom rules\n")
        self.assertEqual(INSTRUCTIONS.check(self.root), [])
        self.assertEqual(self.run_cli().returncode, 0)

    def test_non_compliant_cases_report_standard_and_remediation(self):
        cases = (
            (None, "is missing while AGENTS.md exists"),
            ("# Rules\nUse tabs.\n", "does not import @AGENTS.md"),
            (
                "@AGENTS.md\nUse tabs.\n",
                "contains instructions beyond the @AGENTS.md import",
            ),
        )
        for content, problem in cases:
            with self.subTest(problem=problem):
                claude = self.root / "CLAUDE.md"
                if content is None:
                    claude.unlink(missing_ok=True)
                else:
                    claude.write_text(content)
                findings = INSTRUCTIONS.check(self.root)
                self.assertIn(problem, [finding.problem for finding in findings])
                for finding in findings:
                    self.assertIn("agent-artifacts.md", finding.standard)
                    self.assertIn("@AGENTS.md", finding.remediation)
                before = self.snapshot()
                result = self.run_cli()
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertIn("NON-COMPLIANT CLAUDE.md", result.stdout)
                self.assertIn("Remediation:", result.stdout)
                self.assertEqual(self.snapshot(), before)
                report = json.loads(self.run_cli("--json").stdout)
                self.assertIn(problem, [item["problem"] for item in report])

    def test_symlinks_are_rejected(self):
        outside = tempfile.TemporaryDirectory(prefix="outside-")
        self.addCleanup(outside.cleanup)
        target = Path(outside.name) / "CLAUDE.md"
        target.write_text("@AGENTS.md\n")
        (self.root / "CLAUDE.md").symlink_to(target)
        findings = INSTRUCTIONS.check(self.root)
        self.assertEqual(
            [f.problem for f in findings], ["must be a regular file, not a symlink"]
        )
        self.assertEqual(self.run_cli().returncode, 1)
        self.assertEqual(target.read_text(), "@AGENTS.md\n")

    def test_invalid_root_is_a_usage_error(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root / "absent")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
