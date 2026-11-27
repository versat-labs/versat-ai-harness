"""Deterministic tests for the github-issue-creation form helper."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills/github-issue-creation/scripts/issue_form.py"
FIXTURES = ROOT / "tests/skills/fixtures/github-issue-creation"
ORG = FIXTURES / "organization"
ORG_FORMS = ORG / ".github/ISSUE_TEMPLATE"

sys.path.insert(0, str(SCRIPT.parent))
import issue_form  # noqa: E402


class IssueFormTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def form(self, name):
        return issue_form.load_form(ORG_FORMS / name)

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_organization_defaults_apply_without_repository_forms(self):
        result = issue_form.resolve(FIXTURES / "empty-repository", ORG)
        self.assertEqual(result["source"], "organization")
        summary = {
            form["name"]: (form["title_prefix"], form["type"], form["projects"])
            for form in result["forms"]
        }
        self.assertEqual(
            summary,
            {
                "Bug report": ("fix: ", "Bug", ["versat-labs/1"]),
                "Feature request": ("feat: ", "Feature", ["versat-labs/1"]),
                "Chore": ("chore: ", "Task", ["versat-labs/1"]),
            },
        )

    def test_repository_forms_take_precedence(self):
        result = issue_form.resolve(FIXTURES / "repository", ORG)
        self.assertEqual(result["source"], "repository")
        self.assertEqual([form["name"] for form in result["forms"]], ["Incident"])

    def test_no_forms_available(self):
        result = issue_form.resolve(FIXTURES / "empty-repository", None)
        self.assertEqual(result, {"source": "none", "forms": []})

    def test_required_fields_per_form(self):
        expected = {
            "bug_report.yaml": [
                "Describe the bug",
                "To Reproduce",
                "Expected behavior",
            ],
            "feature_request.yaml": ["Problem", "Job To Be Done", "Persona"],
            "chore.yaml": ["Description", "Scope", "Done when"],
        }
        for name, labels in expected.items():
            with self.subTest(form=name):
                self.assertEqual(issue_form.missing(self.form(name), {}), labels)

    def test_missing_reports_absent_and_blank_answers(self):
        form = self.form("bug_report.yaml")
        answers = {
            "description": "Login fails.",
            "reproduction": "  \n",
            "expected": "x",
        }
        self.assertEqual(issue_form.missing(form, answers), ["To Reproduce"])
        answers = {"problem": "p", "job-to-be-done": "j"}
        self.assertEqual(
            issue_form.missing(self.form("feature_request.yaml"), answers), ["Persona"]
        )

    def test_complete_answers_have_nothing_missing(self):
        answers = {"description": "d", "scope": "s", "done-when": "w"}
        self.assertEqual(issue_form.missing(self.form("chore.yaml"), answers), [])

    def test_render_refuses_missing_required_answer(self):
        with self.assertRaisesRegex(issue_form.FormError, "Persona"):
            issue_form.render(
                self.form("feature_request.yaml"),
                {"problem": "p", "job-to-be-done": "j"},
                "Add export",
            )

    def test_render_layout_prefix_and_type(self):
        answers = {
            "problem": "Creating issues takes too long.",
            "job-to-be-done": "WHEN I find a problem\nI WANT an issue drafted",
            "persona": "User persona: Versat developer",
        }
        result = issue_form.render(
            self.form("feature_request.yaml"), answers, "Add an issue creation Skill"
        )
        self.assertEqual(result["title"], "feat: Add an issue creation Skill")
        self.assertEqual(result["type"], "Feature")
        self.assertEqual(result["projects"], ["versat-labs/1"])
        self.assertEqual(
            result["body"],
            "### Problem\n\nCreating issues takes too long.\n\n"
            "### Job To Be Done\n\nWHEN I find a problem\nI WANT an issue drafted\n\n"
            "### Persona\n\nUser persona: Versat developer\n\n"
            "### Additional context\n\n_No response_\n",
        )

    def test_render_keeps_existing_prefix(self):
        answers = {"description": "d", "scope": "s", "done-when": "w"}
        result = issue_form.render(self.form("chore.yaml"), answers, "chore: Bump deps")
        self.assertEqual(result["title"], "chore: Bump deps")

    def test_upload_fields_are_skipped_with_notice(self):
        answers = {"description": "d", "reproduction": "r", "expected": "e"}
        result = issue_form.render(self.form("bug_report.yaml"), answers, "Crash")
        self.assertNotIn("### Screenshots", result["body"])
        self.assertEqual(len(result["notices"]), 1)
        self.assertIn("Screenshots", result["notices"][0])
        self.assertEqual(result["type"], "Bug")
        self.assertTrue(result["title"].startswith("fix: "))

    def test_verbatim_answers_are_preserved(self):
        trace = (
            "```\nTraceback (most recent call last):\n"
            '  File "app.py", line 3, in <module>\n'
            "KeyError: 'usuário_id'\n```"
        )
        answers = {
            "description": trace,
            "reproduction": "Run `make test`",
            "expected": "e",
        }
        result = issue_form.render(self.form("bug_report.yaml"), answers, "KeyError")
        self.assertIn(trace, result["body"])
        self.assertIn("Run `make test`", result["body"])

    def test_cli_resolve_missing_and_render(self):
        resolved = self.run_cli(
            "resolve", "--repo-dir", FIXTURES / "empty-repository", "--org-dir", ORG
        )
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual(json.loads(resolved.stdout)["source"], "organization")

        answers = self.work / "answers.json"
        answers.write_text(json.dumps({"description": "d"}), encoding="utf-8")
        form = ORG_FORMS / "chore.yaml"
        absent = self.run_cli("missing", "--form", form, "--answers", answers)
        self.assertEqual(json.loads(absent.stdout), {"missing": ["Scope", "Done when"]})

        refused = self.run_cli(
            "render", "--form", form, "--answers", answers, "--title", "x"
        )
        self.assertEqual(refused.returncode, 2)
        self.assertIn("Scope", json.loads(refused.stdout)["error"])

        answers.write_text(
            json.dumps({"description": "d", "scope": "s", "done-when": "w"}),
            encoding="utf-8",
        )
        rendered = self.run_cli(
            "render", "--form", form, "--answers", answers, "--title", "x"
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertEqual(json.loads(rendered.stdout)["title"], "chore: x")

    def test_invalid_answers_are_reported(self):
        answers = self.work / "answers.json"
        answers.write_text("[]", encoding="utf-8")
        result = self.run_cli(
            "missing", "--form", ORG_FORMS / "chore.yaml", "--answers", answers
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("JSON object", json.loads(result.stdout)["error"])


if __name__ == "__main__":
    unittest.main()
