"""Bounded GitHub GET observations. Never configure repositories or read secrets."""

import base64
from datetime import datetime, timezone
import json
import os
import re
import shutil
import subprocess
import time
from urllib.parse import parse_qs, quote, urlparse

from validators.security.policy import digest

REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
MAX_RESPONSE = 4 * 1024 * 1024


class ObservationError(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def now():
    return datetime.now(timezone.utc).isoformat()


class GitHub:
    def __init__(
        self, repository, request_timeout=30, total_timeout=180, max_pages=100
    ):
        if not REPOSITORY.fullmatch(repository) or any(
            x in (".", "..") for x in repository.split("/")
        ):
            raise ValueError("Expected GitHub owner/repository")
        self.base = f"/repos/{repository}"
        self.request_timeout = request_timeout
        self.deadline = time.monotonic() + total_timeout
        self.max_pages = max_pages
        self.executable = shutil.which("gh")

    def permitted(self, path):
        parsed = urlparse(path)
        if parsed.scheme or parsed.netloc or parsed.fragment:
            return False
        suffix = parsed.path.removeprefix(self.base)
        if parsed.path != self.base + suffix or not parsed.path.startswith(self.base):
            return False
        return bool(
            re.fullmatch(
                r"(?:|/branches/[A-Za-z0-9._%-]+(?:/protection)?|/rules/branches/[A-Za-z0-9._%-]+|/rulesets(?:/[0-9]+)?|/contents/(?:\.github/CODEOWNERS|CODEOWNERS|docs/CODEOWNERS)|/codeowners/errors|/collaborators/[A-Za-z0-9-]+/permission)",
                suffix,
            )
        ) and set(parse_qs(parsed.query)) <= {
            "ref",
            "page",
            "per_page",
            "includes_parents",
        }

    def get(self, path):
        if not self.permitted(path):
            raise ObservationError("forbidden-endpoint")
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise ObservationError("collection-timeout")
        if self.executable is None:
            raise ObservationError("github-cli-unavailable")
        environment = dict(os.environ)
        environment.pop("GH_DEBUG", None)
        environment["GH_PROMPT_DISABLED"] = "1"
        argv = [
            self.executable,
            "api",
            "--hostname",
            "github.com",
            "--method",
            "GET",
            "--include",
            "-H",
            "Accept: application/vnd.github+json",
            "-H",
            "X-GitHub-Api-Version: 2022-11-28",
            path,
        ]
        try:
            result = subprocess.run(
                argv,
                stdin=subprocess.DEVNULL,
                capture_output=True,
                env=environment,
                timeout=min(self.request_timeout, remaining),
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ObservationError("request-unavailable") from exc
        if len(result.stdout) > MAX_RESPONSE or len(result.stderr) > MAX_RESPONSE:
            raise ObservationError("response-size-limit")
        try:
            response = result.stdout.decode("utf-8").replace("\r\n", "\n")
            header, body = response.split("\n\n", 1)
            status = int(header.splitlines()[0].split()[1])
            data = json.loads(body)
        except (UnicodeError, ValueError, IndexError) as exc:
            raise ObservationError("invalid-api-response") from exc
        if status != 200 or result.returncode:
            code = (
                "branch-not-protected"
                if status == 404
                and isinstance(data, dict)
                and data.get("message") == "Branch not protected"
                else f"http-{status}"
            )
            raise ObservationError(code)
        headers = {}
        for line in header.splitlines()[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.lower()] = value.strip()
        return data, headers

    def pages(self, path):
        rows = []
        seen = set()
        for _ in range(self.max_pages):
            if path in seen:
                raise ObservationError("pagination-cycle")
            seen.add(path)
            data, headers = self.get(path)
            if not isinstance(data, list) or any(not isinstance(x, dict) for x in data):
                raise ObservationError("invalid-collection")
            rows.extend(data)
            link = headers.get("link", "")
            matches = re.findall(r'<([^>]+)>;\s*rel="next"', link)
            if not matches:
                if 'rel="next"' in link:
                    raise ObservationError("invalid-pagination")
                return rows
            parsed = urlparse(matches[0])
            if (
                parsed.scheme != "https"
                or parsed.netloc != "api.github.com"
                or parsed.path != urlparse(path).path
                or parsed.fragment
            ):
                raise ObservationError("unsafe-pagination")
            path = parsed.path + "?" + parsed.query
        raise ObservationError("pagination-limit")


def select(data, keys):
    if not isinstance(data, dict):
        raise ObservationError("invalid-object")
    return {key: data[key] for key in keys if key in data}


def clean_rule(data):
    # API rule parameters are bounded settings, not secret values.
    return select(data, ("type", "parameters", "ruleset_id"))


def collect_sample(transport, repository, policy):
    base = f"/repos/{repository}"
    branch = quote(policy["default_branch"], safe="")
    observations = {}

    def observe(name, callback, absent=()):
        try:
            observations[name] = {"status": "ok", "data": callback()}
        except ObservationError as exc:
            observations[name] = {
                "status": "absent" if exc.code in absent else "unverified",
                "diagnostic": exc.code,
            }
        except (KeyError, TypeError, ValueError, AttributeError):
            observations[name] = {
                "status": "unverified",
                "diagnostic": "invalid-observation",
            }
        return observations[name].get("data")

    def repo_data():
        data, _ = transport.get(base)
        result = select(
            data,
            (
                "id",
                "full_name",
                "visibility",
                "default_branch",
                "allow_forking",
                "has_pull_requests",
                "pull_request_creation_policy",
            ),
        )
        if "security_and_analysis" in data:
            result["security_and_analysis"] = {
                key: select(value, ("status",))
                for key, value in data["security_and_analysis"].items()
                if key in policy["secret_features"]
            }
        return result

    observe("repository", repo_data)

    def main_data():
        data, _ = transport.get(f"{base}/branches/{branch}")
        return {"name": data["name"], "sha": data["commit"]["sha"]}

    main = observe("main", main_data)

    def protection_data():
        data, _ = transport.get(f"{base}/branches/{branch}/protection")
        result = select(
            data,
            (
                "enforce_admins",
                "allow_force_pushes",
                "allow_deletions",
                "required_pull_request_reviews",
                "required_status_checks",
            ),
        )
        for name in ("enforce_admins", "allow_force_pushes", "allow_deletions"):
            if name in result:
                result[name] = select(result[name], ("enabled",))
        reviews = result.get("required_pull_request_reviews")
        if isinstance(reviews, dict):
            result["required_pull_request_reviews"] = select(
                reviews,
                (
                    "required_approving_review_count",
                    *policy["main"]["review_flags"],
                    "bypass_pull_request_allowances",
                ),
            )
            allowances = reviews.get("bypass_pull_request_allowances")
            if isinstance(allowances, dict):
                # Only presence matters; do not export personal/team/app metadata.
                result["required_pull_request_reviews"][
                    "bypass_pull_request_allowances"
                ] = {k: bool(v) for k, v in allowances.items()}
        if isinstance(result.get("required_status_checks"), dict):
            result["required_status_checks"] = select(
                result["required_status_checks"], ("contexts", "strict")
            )
        return result

    observe("protection", protection_data, ("branch-not-protected",))
    observe(
        "main_rules",
        lambda: [
            clean_rule(x)
            for x in transport.pages(f"{base}/rules/branches/{branch}?per_page=100")
        ],
    )

    def ruleset_data():
        rows = transport.pages(f"{base}/rulesets?includes_parents=true&per_page=100")
        ids = [x.get("id") for x in rows]
        if any(type(x) is not int for x in ids) or len(set(ids)) != len(ids):
            raise ObservationError("invalid-ruleset-identities")
        result = []
        for rule_id in ids:
            data, _ = transport.get(f"{base}/rulesets/{rule_id}?includes_parents=true")
            if data.get("id") != rule_id:
                raise ObservationError("ruleset-identity-mismatch")
            entry = select(
                data,
                (
                    "id",
                    "target",
                    "source_type",
                    "source",
                    "enforcement",
                    "conditions",
                    "bypass_actors",
                ),
            )
            if "rules" in data:
                entry["rules"] = [clean_rule(x) for x in data["rules"]]
            result.append(entry)
        return result

    observe("rulesets", ruleset_data)

    def codeowners_data():
        sha = (main or {}).get("sha", "")
        if not re.fullmatch("[a-f0-9]{40}|[a-f0-9]{64}", sha):
            raise ObservationError("base-commit-unavailable")
        for path in (".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"):
            try:
                data, _ = transport.get(f"{base}/contents/{path}?ref={sha}")
            except ObservationError as exc:
                if exc.code == "http-404":
                    continue
                raise
            if (
                data.get("type") != "file"
                or data.get("encoding") != "base64"
                or data.get("size", MAX_RESPONSE) >= 3 * 1024 * 1024
            ):
                raise ObservationError("unsupported-codeowners-file")
            content = base64.b64decode(data["content"], validate=False).decode("utf-8")
            if len(content.encode()) >= 3 * 1024 * 1024:
                raise ObservationError("codeowners-size-limit")
            rows = []
            for line in content.splitlines():
                parts = line.split("#", 1)[0].split()
                if parts:
                    rows.append({"pattern": parts[0], "owners": parts[1:]})
            return {"path": path, "sha": sha, "rows": rows}
        raise ObservationError("codeowners-absent")

    observe("codeowners", codeowners_data, ("codeowners-absent",))

    def errors_data():
        if not main:
            raise ObservationError("base-commit-unavailable")
        data, _ = transport.get(f"{base}/codeowners/errors?ref={main['sha']}")
        return {
            "errors": [select(e, ("line", "column", "kind")) for e in data["errors"]]
        }

    observe("codeowners_errors", errors_data)

    def permissions_data():
        result = {}
        for owner in policy["codeowners"]:
            data, _ = transport.get(f"{base}/collaborators/{owner}/permission")
            if data.get("permission") not in (
                "read",
                "triage",
                "write",
                "maintain",
                "admin",
                "none",
            ):
                raise ObservationError("unknown-owner-permission")
            result[owner] = data["permission"]
        return result

    observe("owner_permissions", permissions_data)
    return observations


def collect(repository, policy, transport=None):
    transport = transport or GitHub(repository)
    started = now()
    first = collect_sample(transport, repository, policy)
    complete = all(x["status"] != "unverified" for x in first.values())
    second = collect_sample(transport, repository, policy) if complete else None
    stable = second is not None and first == second
    return {
        "schema_version": 1,
        "repository": repository,
        "started_at": started,
        "finished_at": now(),
        "observations": first,
        "complete": complete
        and second is not None
        and all(x["status"] != "unverified" for x in second.values()),
        "stable": stable,
        "sample_digests": [digest(x) for x in (first, second) if x is not None],
    }
