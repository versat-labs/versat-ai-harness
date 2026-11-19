"""Exercise the documentation report against committed Git snapshots."""

from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

from validators.documentation import validate

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "scripts/validate/documentation.sh"
EXAMPLE = (
    ROOT
    / "project-templates/artifacts/validation/documentation"
    / ".github/workflows/documentation-report.yml"
)


class SnapshotReportTest(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.git("init", "-q")
        self.git("config", "user.email", "fixture@example.com")
        self.git("config", "user.name", "Documentation fixture")
        self.git("commit", "-qm", "empty", "--allow-empty")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], text=True)

    def write(self, name, content="A useful guide.\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD").strip()

    def report(self, *args, base=None):
        return subprocess.run(
            [
                "bash",
                str(CLI),
                "--root",
                str(self.root),
                "--base",
                base or self.base,
                *args,
            ],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_reports_mixed_results_without_reading_worktree_or_printing_contents(self):
        for name in (
            "docs/user-docs/quickstart.md",
            "docs/user-docs/quickstart.pt.md",
            "docs/user-docs/quickstart.es.md",
            "docs/product/overview.es.md",
        ):
            self.write(name, "CONTENTS MUST NOT BE PRINTED")
        self.write("docs/product/overview.pt.md", "\ufeff\n\t")
        self.write("docs/runbooks/operator.md")
        target = self.commit("Mixed example")
        (self.root / "docs/user-docs/quickstart.es.md").unlink()
        report = self.report("--target", target)
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertIn(
            "| Pass | Spanish sibling | <code>docs/user-docs/quickstart.es.md",
            report.stdout,
        )
        self.assertIn(
            "| Fail | English source | <code>docs/product/overview.md", report.stdout
        )
        self.assertIn(
            "| Fail | Portuguese sibling | <code>docs/product/overview.pt.md",
            report.stdout,
        )
        self.assertIn("File contains no text.", report.stdout)
        self.assertIn("Required file is missing.", report.stdout)
        self.assertNotIn("operator.md", report.stdout)
        self.assertNotIn("CONTENTS MUST NOT BE PRINTED", report.stdout)
        self.assertIn("## Human review", report.stdout)

    def test_moves_report_both_endpoints_and_full_removals(self):
        for locale in ("", ".pt", ".es"):
            self.write(f"docs/quickstart{locale}.md")
        base = self.commit("Legacy guidance")
        for locale in ("", ".pt", ".es"):
            old = self.root / f"docs/quickstart{locale}.md"
            new = self.root / "docs/user-docs" / old.name
            new.parent.mkdir(exist_ok=True)
            old.rename(new)
        self.commit("Move the complete set")
        report = self.report(base=base)
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertIn(
            "| Not applicable | Language file set | <code>docs/quickstart.md",
            report.stdout,
        )
        self.assertIn(
            "| Pass | English source | <code>docs/user-docs/quickstart.md",
            report.stdout,
        )
        self.assertIn("Review navigation.", report.stdout)

    def test_nonapplicable_and_unavailable_snapshots_are_distinct(self):
        self.write("docs/runbooks/operations.md")
        self.commit("Unrelated technical reference")
        report = self.report()
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertIn("No recognized Markdown paths changed.", report.stdout)
        for args, base, label in (
            ((), "missing", "Base"),
            (("--target", "missing"), self.base, "Target"),
        ):
            with self.subTest(label=label):
                report = self.report(*args, base=base)
                self.assertEqual(report.returncode, 2)
                self.assertIn(f"{label} revision unavailable", report.stdout)
                self.assertIn("| Unverified |", report.stdout)
                self.assertNotIn("| Pass |", report.stdout)

    def test_unsafe_paths_are_displayed_as_text_and_links_are_not_followed(self):
        name = "docs/user-docs/guide [link](https:|example)\n&.md"
        source = self.write(name)
        source.unlink()
        source.symlink_to("/outside/private.md")
        summary = self.root / "summary.md"
        self.commit("Malformed guide")
        report = self.report("--summary", str(summary))
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertEqual(report.stdout, "")
        body = summary.read_text()
        self.assertIn("Links are not followed.", body)
        self.assertIn("&#124;", body)
        self.assertIn("&#92;n", body)
        self.assertNotIn("[link]", body)
        self.assertNotIn("/outside/private.md", body)
        self.assertNotIn("\n&.md", body)

    def test_replacing_docs_directory_with_a_symlink_is_not_a_clean_removal(self):
        self.write("docs/user-docs/quickstart.md")
        base = self.commit("Initial guide")
        self.git("rm", "-r", "docs")
        (self.root / "docs").symlink_to("/outside/docs", target_is_directory=True)
        self.commit("Replace docs directory")
        report = self.report(base=base)
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertIn("A parent path in the target is not a directory.", report.stdout)
        self.assertNotIn("All files removed.", report.stdout)

    def test_truncation_preserves_the_human_review_section(self):
        row = validate.Row("Fail", "Rule", "x" * 200, "Missing file.")
        with patch.object(validate, "MAX_SUMMARY_BYTES", 1000):
            report = validate.render("base", "target", [row] * 100)
        self.assertLessEqual(len(report.encode()), 1000)
        self.assertIn("Some rows were omitted.", report)
        self.assertIn("## Human review", report)


class WorkflowContractTest(unittest.TestCase):
    def test_provider_and_consumer_workflows_pass_explicit_snapshots_to_read_only_report(
        self,
    ):
        paths = (ROOT / ".github/workflows/validate.yml", EXAMPLE)
        for path in paths:
            with self.subTest(path=path):
                workflow = yaml.safe_load(path.read_text())
                event = workflow.get("on", workflow.get(True))
                self.assertIn("pull_request", event)
                self.assertNotIn("pull_request_target", event)
                job = workflow["jobs"]["documentation-report"]
                self.assertEqual(
                    job.get("permissions", workflow.get("permissions")),
                    {"contents": "read"},
                )
                self.assertEqual(job["runs-on"], "ubuntu-latest")
                self.assertFalse(job["steps"][0]["with"]["persist-credentials"])
                self.assertEqual(job["steps"][0]["with"]["fetch-depth"], 0)
                step = job["steps"][-1]
                self.assertIn("scripts/validate/documentation.sh", step["run"])
                self.assertIn(' --summary "$GITHUB_STEP_SUMMARY"', step["run"])
                self.assertIn("pull_request.base.sha", step["env"]["DOCS_BASE"])
                self.assertIn("github.sha", step["env"]["DOCS_TARGET"])
                if path == EXAMPLE:
                    self.assertEqual(
                        job["steps"][2]["with"]["ref"],
                        "REPLACE_WITH_REVIEWED_FULL_COMMIT_SHA",
                    )
                    self.assertIn("scripts/testing/provider.py", job["steps"][3]["run"])
                else:
                    self.assertIn("structural-validation", workflow["jobs"])
                    self.assertIn("quality", workflow["jobs"])


if __name__ == "__main__":
    unittest.main()
