"""Network-free collection and CLI boundary tests."""

import base64
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests/fixtures/security"))
from security_fixtures import REPO, SHA, data, snapshot  # noqa: E402 - standalone provider/test path bootstrap
from scripts.security.github import GitHub, MAX_RESPONSE, ObservationError, collect  # noqa: E402 - standalone provider/test path bootstrap
from validators.security.policy import load_policy  # noqa: E402 - standalone provider/test path bootstrap
from validators.security.validate import assess, main, write_report  # noqa: E402 - standalone provider/test path bootstrap


class FixtureTransport(GitHub):
    def __init__(self):
        super().__init__(REPO)
        self.value = snapshot()
        self.calls = []
        self.failures = {}
        self.change_second = False
        self.samples = 0

    def get(self, path):
        self.calls.append(path)
        if path in self.failures:
            raise ObservationError(self.failures[path])
        base = self.base
        if path == base:
            self.samples += 1
            result = deepcopy(data(self.value, "repository"))
            if self.change_second and self.samples == 2:
                result["allow_forking"] = False
            return result, {}
        if path == base + "/branches/main":
            return {"name": "main", "commit": {"sha": SHA}}, {}
        if path.endswith("/protection"):
            return deepcopy(data(self.value, "protection")), {}
        if "/rules/branches/" in path:
            return deepcopy(data(self.value, "main_rules")), {}
        if "/rulesets?" in path:
            return deepcopy(data(self.value, "rulesets")), {}
        if "/rulesets/" in path:
            number = int(path.split("/rulesets/")[1].split("?")[0])
            return deepcopy(
                next(x for x in data(self.value, "rulesets") if x["id"] == number)
            ), {}
        if "/contents/" in path:
            content = "# Do not export this comment\n* @elviszoz @evertonspohrversat\n"
            return {
                "type": "file",
                "size": len(content),
                "encoding": "base64",
                "content": base64.b64encode(content.encode()).decode(),
            }, {}
        if "/codeowners/errors?" in path:
            return deepcopy(data(self.value, "codeowners_errors")), {}
        if "/collaborators/" in path:
            return {
                "permission": "admin",
                "user": {"email": "not-for-export@example.test"},
            }, {}
        raise AssertionError(path)


class SecurityCollectionTests(unittest.TestCase):
    def setUp(self):
        self.policy, self.identity = load_policy()

    def report(self, value, mode="live"):
        return assess(value, self.policy, self.identity, {"mode": "source"}, REPO, mode)

    def test_complete_stable_collection_and_redaction(self):
        transport = FixtureTransport()
        value = collect(REPO, self.policy, transport)
        self.assertTrue(self.report(value)["public_ready"])
        self.assertEqual(transport.samples, 2)
        self.assertNotIn("Do not export", json.dumps(value))
        self.assertNotIn("not-for-export", json.dumps(value))
        self.assertTrue(any(f"ref={SHA}" in x for x in transport.calls))

    def test_instability_prevents_readiness(self):
        transport = FixtureTransport()
        transport.change_second = True
        value = collect(REPO, self.policy, transport)
        self.assertFalse(value["stable"])
        self.assertNotEqual(value["sample_digests"][0], value["sample_digests"][1])
        self.assertEqual(self.report(value)["result"], "unable-to-verify")

    def test_each_transport_failure_preserves_unknowns(self):
        for error in (
            "http-401",
            "http-403",
            "http-404",
            "http-429",
            "http-500",
            "request-unavailable",
            "invalid-api-response",
            "response-size-limit",
        ):
            transport = FixtureTransport()
            transport.failures[transport.base + "/branches/main/protection"] = error
            value = collect(REPO, self.policy, transport)
            self.assertEqual(
                value["observations"]["protection"]["status"], "unverified"
            )
            self.assertFalse(self.report(value)["public_ready"])

    def test_confirmed_absence_differs_from_ambiguous_404(self):
        transport = FixtureTransport()
        transport.failures[transport.base + "/branches/main/protection"] = (
            "branch-not-protected"
        )
        value = collect(REPO, self.policy, transport)
        self.assertEqual(value["observations"]["protection"]["status"], "absent")
        self.assertEqual(self.report(value)["result"], "fail")

    def test_hidden_bypass_and_missing_features_cannot_pass(self):
        transport = FixtureTransport()
        del data(transport.value, "rulesets")[0]["bypass_actors"]
        del data(transport.value, "repository")["security_and_analysis"]
        self.assertEqual(
            self.report(collect(REPO, self.policy, transport))["result"],
            "unable-to-verify",
        )

    def test_pagination_collects_every_page(self):
        transport = GitHub(REPO)
        path = transport.base + "/rulesets?per_page=100"
        next_path = transport.base + "/rulesets?page=2&per_page=100"
        with patch.object(
            transport,
            "get",
            side_effect=[
                (
                    [{"id": 1}],
                    {"link": f'<https://api.github.com{next_path}>; rel="next"'},
                ),
                ([{"id": 2}], {}),
            ],
        ) as get:
            self.assertEqual(transport.pages(path), [{"id": 1}, {"id": 2}])
            self.assertEqual(get.call_args.args[0], next_path)

    def test_unsafe_and_truncated_pagination(self):
        transport = GitHub(REPO, max_pages=1)
        path = transport.base + "/rulesets?per_page=100"
        for url in ("https://evil.test/steal", f"https://api.github.com{path}&page=2"):
            with patch.object(
                transport,
                "get",
                return_value=([{"id": 1}], {"link": f'<{url}>; rel="next"'}),
            ):
                with self.assertRaises(ObservationError):
                    transport.pages(path)

    def test_transport_only_uses_scoped_get_and_disables_debug(self):
        transport = GitHub(REPO)
        transport.executable = "/trusted/gh"
        completed = subprocess.CompletedProcess(
            [], 0, b'HTTP/2.0 200 OK\nContent-Type: application/json\n\n{"id":1}', b""
        )
        with patch(
            "scripts.security.github.subprocess.run", return_value=completed
        ) as run:
            with patch.dict("os.environ", {"GH_DEBUG": "api"}):
                value, _ = transport.get(transport.base)
            self.assertEqual(value, {"id": 1})
            args = run.call_args.args[0]
            self.assertEqual(args[args.index("--method") + 1], "GET")
            self.assertNotIn("GH_DEBUG", run.call_args.kwargs["env"])
            self.assertFalse(run.call_args.kwargs.get("shell", False))
            self.assertNotIn("--input", args)
        for path in (
            "https://evil.test/",
            transport.base + "/actions/secrets",
            transport.base + "/contents/../../secret",
            "/repos/another/repo",
            transport.base + "?token=secret",
        ):
            with self.assertRaises(ObservationError):
                transport.get(path)

    def test_transport_limits_and_sanitized_errors(self):
        transport = GitHub(REPO)
        transport.executable = "/trusted/gh"
        examples = [
            (b"x" * (MAX_RESPONSE + 1), "response-size-limit"),
            (b"not-json", "invalid-api-response"),
            (b'HTTP/2.0 403 Forbidden\n\n{"message":"sensitive-text"}', "http-403"),
        ]
        for stdout, expected in examples:
            with patch(
                "scripts.security.github.subprocess.run",
                return_value=subprocess.CompletedProcess(
                    [], 1, stdout, b"secret stderr"
                ),
            ):
                with self.assertRaises(ObservationError) as error:
                    transport.get(transport.base)
                self.assertEqual(error.exception.code, expected)
        transport.deadline = 0
        with self.assertRaisesRegex(ObservationError, "collection-timeout"):
            transport.get(transport.base)

    def test_offline_success_never_establishes_live_readiness(self):
        report = self.report(snapshot(), "snapshot")
        self.assertEqual(report["result"], "pass")
        self.assertFalse(report["public_ready"])

    def test_cli_modes_exit_codes_and_invalid_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "snapshot.json"
            output = Path(directory) / "report.json"
            cases = [
                (snapshot(), 0, "pass"),
                ({"not": "a snapshot"}, 2, "unable-to-verify"),
            ]
            broken = snapshot()
            data(broken, "repository")["security_and_analysis"]["secret_scanning"][
                "status"
            ] = "disabled"
            cases.append((broken, 1, "fail"))
            private = snapshot()
            data(private, "repository")["visibility"] = "private"
            cases.append((private, 3, "not-applicable"))
            for value, code, result in cases:
                source.write_text(json.dumps(value))
                with patch("sys.stdout", new=StringIO()):
                    actual = main(
                        [
                            "--repository",
                            REPO,
                            "--snapshot",
                            str(source),
                            "--output",
                            str(output),
                        ]
                    )
                report = json.loads(output.read_text())
                self.assertEqual(actual, code)
                self.assertEqual(report["result"], result)
                self.assertFalse(report["public_ready"])
            with patch("sys.stdout", new=StringIO()) as stdout:
                self.assertEqual(main(["--check-policy"]), 0)
                self.assertFalse(json.loads(stdout.getvalue())["public_ready"])

    def test_report_refuses_symlinks_and_is_atomic(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            original = path / "original"
            original.write_text("preserve")
            link = path / "link"
            link.symlink_to(original)
            with self.assertRaises(ValueError):
                write_report(link, {})
            self.assertEqual(original.read_text(), "preserve")
            write_report(path / "new/report.json", {"result": "pass"})
            self.assertEqual(
                json.loads((path / "new/report.json").read_text()), {"result": "pass"}
            )


if __name__ == "__main__":
    unittest.main()
