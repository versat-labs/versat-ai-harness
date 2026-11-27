"""Policy resolution, exact consumer identity and safe template composition."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.bootstrap.public_security import assets, render  # noqa: E402 - standalone provider/test path bootstrap
from validators.security.policy import load_policy, schema_check  # noqa: E402 - standalone provider/test path bootstrap


class SecurityContractTests(unittest.TestCase):
    def setUp(self):
        self.policy, self.identity = load_policy()

    def package(self, path):
        for name in (
            "standards",
            "schemas",
            "scripts/testing",
            "validators/testing",
            "validators/sdd",
        ):
            shutil.copytree(
                ROOT / name, path / name, ignore=shutil.ignore_patterns("__pycache__")
            )
        shutil.copy2(ROOT / "VERSION", path / "VERSION")
        return path

    def test_policy_is_in_core_for_every_profile_and_criticality(self):
        index = yaml.safe_load((ROOT / "standards/index.yaml").read_text())
        for profile in index["profiles"]:
            for criticality in index["criticality"]:
                selected = (
                    index["core"]["always"]
                    + index["profiles"][profile]
                    + index["criticality"][criticality]
                )
                self.assertIn(self.identity["path"], selected)
        schema_check(self.policy, "public-repository-security.schema.yaml")

    def test_missing_duplicate_invalid_and_unsupported_policy(self):
        for mutation in ("missing", "duplicate", "invalid", "version", "duplicate-key"):
            with tempfile.TemporaryDirectory() as directory:
                package = self.package(Path(directory))
                path = package / "standards" / self.identity["path"]
                if mutation == "missing":
                    path.unlink()
                elif mutation == "duplicate":
                    index_path = package / "standards/index.yaml"
                    index = yaml.safe_load(index_path.read_text())
                    index["core"]["always"].append(self.identity["path"])
                    index_path.write_text(yaml.safe_dump(index))
                elif mutation == "duplicate-key":
                    path.write_text(path.read_text() + "schema_version: 1\n")
                else:
                    value = yaml.safe_load(path.read_text())
                    value[
                        "schema_version" if mutation == "version" else "unexpected"
                    ] = 99
                    path.write_text(yaml.safe_dump(value))
                with self.assertRaises(Exception):
                    load_policy(package)

    def test_rendered_assets_are_separate_layers_and_not_applied(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            result = render(output)
            self.assertFalse(result["applied_to_github"])
            self.assertFalse(result["public_ready"])
            main = json.loads(
                (output / ".github/security/main-protection.json").read_text()
            )
            self.assertEqual(main["bypass_actors"], [])
            self.assertEqual(
                main["rules"][0]["parameters"]["required_approving_review_count"], 1
            )
            self.assertEqual(
                main["rules"][0]["parameters"],
                {
                    "required_approving_review_count": 1,
                    "require_code_owner_review": True,
                    "dismiss_stale_reviews_on_push": True,
                    "require_last_push_approval": True,
                    "required_review_thread_resolution": False,
                },
            )
            security = output / ".github/security"
            self.assertFalse((security / "branch-administration.json").exists())
            tag = json.loads((security / "tag-administration.json").read_text())
            self.assertEqual(tag["target"], "tag")
            self.assertEqual(
                tag["conditions"]["ref_name"], {"include": ["~ALL"], "exclude": []}
            )
            self.assertEqual(tag["bypass_actors"][0]["actor_id"], 5)
            self.assertEqual(
                tag["rules"][1],
                {
                    "type": "update",
                    "parameters": {"update_allows_fetch_and_merge": False},
                },
            )
            self.assertEqual(
                (output / ".github/CODEOWNERS").read_text(),
                "* @elviszoz @evertonspohrversat\n",
            )
            before = {
                str(p.relative_to(output)): p.read_bytes()
                for p in output.rglob("*")
                if p.is_file()
            }
            render(output)
            after = {
                str(p.relative_to(output)): p.read_bytes()
                for p in output.rglob("*")
                if p.is_file()
            }
            self.assertEqual(before, after)
            manifest = json.loads(
                (output / ".github/security/manifest.json").read_text()
            )
            for name, digest in manifest["assets"].items():
                self.assertEqual(
                    hashlib.sha256((output / name).read_bytes()).hexdigest(), digest
                )

    def test_render_follows_policy_not_parallel_owner_list(self):
        policy = dict(self.policy, codeowners=["synthetic-owner"])
        self.assertEqual(assets(policy)[".github/CODEOWNERS"], "* @synthetic-owner\n")

    def test_conflicts_prevent_partial_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / ".github").mkdir()
            (path / ".github/CODEOWNERS").write_text("* @custom-owner\n")
            with self.assertRaises(ValueError):
                render(path)
            self.assertEqual(
                (path / ".github/CODEOWNERS").read_text(), "* @custom-owner\n"
            )
            self.assertFalse((path / ".github/security").exists())

    def test_symlink_destination_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "real").mkdir()
            (path / "link").symlink_to(path / "real", target_is_directory=True)
            with self.assertRaises(ValueError):
                render(path / "link")
            self.assertEqual(list((path / "real").iterdir()), [])

    def test_exact_provider_reuses_yaml_standard_locks_for_all_profiles(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            package = self.package(base / "provider")
            for argv in (
                ["init", "-q"],
                ["add", "."],
                [
                    "-c",
                    "user.name=Fixture",
                    "-c",
                    "user.email=fixture@example.test",
                    "commit",
                    "-qm",
                    "fixture",
                ],
            ):
                subprocess.run(
                    ["git", "-C", str(package), *argv], check=True, capture_output=True
                )
            commit = subprocess.check_output(
                ["git", "-C", str(package), "rev-parse", "HEAD"], text=True
            ).strip()
            version = (package / "VERSION").read_text().strip()
            index = yaml.safe_load((package / "standards/index.yaml").read_text())
            consumer = base / "consumer"
            (consumer / ".versat").mkdir(parents=True)
            for profile in index["profiles"]:
                for criticality in index["criticality"]:
                    project = {
                        "schema_version": 1,
                        "project": {
                            "name": "fixture",
                            "description": "Synthetic consumer",
                            "profile": profile,
                            "domain": "marketing",
                            "owner": "synthetic",
                            "visibility": "public",
                            "criticality": criticality,
                        },
                        "technologies": [],
                    }
                    paths = set(
                        index["core"]["always"]
                        + index["profiles"][profile]
                        + index["domains"]["marketing"]
                        + index["criticality"][criticality]
                    )
                    lock = {
                        "schema_version": 1,
                        "harness": {"version": version, "commit": commit},
                        "resolved_at": "synthetic",
                        "standards": [
                            {
                                "path": name,
                                "version": version,
                                "digest": hashlib.sha256(
                                    (package / "standards" / name).read_bytes()
                                ).hexdigest(),
                            }
                            for name in sorted(paths)
                        ],
                    }
                    (consumer / ".versat/project.yaml").write_text(
                        yaml.safe_dump(project)
                    )
                    (consumer / ".versat/standards.lock").write_text(
                        yaml.safe_dump(lock)
                    )
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-B",
                            str(package / "scripts/testing/provider.py"),
                            "--root",
                            str(consumer),
                        ],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(
                        result.returncode, 0, result.stdout + result.stderr
                    )
            lock["standards"][0]["digest"] = "0" * 64
            (consumer / ".versat/standards.lock").write_text(yaml.safe_dump(lock))
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(package / "scripts/testing/provider.py"),
                    "--root",
                    str(consumer),
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
