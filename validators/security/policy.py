"""Pure evaluation of the index-resolved public GitHub security contract."""

import hashlib
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator
import yaml

PACKAGE = Path(__file__).resolve().parents[2]
KIND = "github-public-repository-security"
UNKNOWN = "unable-to-verify"
# GitHub uses different wire names for classic protection and ruleset reviews.
# These are API translations, not independent policy values.
RULESET_REVIEW_FIELDS = {
    "require_code_owner_reviews": "require_code_owner_review",
    "dismiss_stale_reviews": "dismiss_stale_reviews_on_push",
    "require_last_push_approval": "require_last_push_approval",
}


def output_path(value):
    path = Path(value)
    if ".." in path.parts:
        raise ValueError("Traversal in output path")
    path = path.absolute()
    # macOS exposes its standard temporary directories through these OS aliases.
    if sys.platform == "darwin":
        for alias, target in (("/tmp", "/private/tmp"), ("/var", "/private/var")):
            if (
                path.is_relative_to(alias)
                and Path(alias).is_symlink()
                and Path(alias).resolve() == Path(target)
            ):
                path = Path(target) / path.relative_to(alias)
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError("Symlink output destination")
    return path


def read_yaml(path):
    """Reject duplicate keys rather than letting later values replace policy."""

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError("Duplicate YAML key")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping
    )
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)


def schema_check(data, name, package=PACKAGE):
    Draft202012Validator(read_yaml(package / "schemas" / name)).validate(data)


def safe_file(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("Unsafe package path")
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError("Symlink package input")
    return path


def load_policy(package=PACKAGE):
    index = read_yaml(package / "standards/index.yaml")
    paths = index["core"]["always"]
    if len(paths) != len(set(paths)):
        raise ValueError("Duplicate core Standard")
    candidates = []
    for name in paths:
        path = safe_file(package / "standards", name)
        if not path.is_file():
            raise ValueError("Missing indexed Standard")
        if path.suffix in (".yaml", ".yml"):
            data = read_yaml(path)
            if isinstance(data, dict) and data.get("kind") == KIND:
                candidates.append((name, path, data))
    if len(candidates) != 1:
        raise ValueError("Expected exactly one indexed public security policy")
    name, path, data = candidates[0]
    schema_check(data, "public-repository-security.schema.yaml", package)
    return data, {
        "id": data["policy_id"],
        "version": data["policy_version"],
        "path": name,
        "digest": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def observation(snapshot, name, expected=dict):
    value = snapshot["observations"].get(name, {})
    data = value.get("data")
    return data if value.get("status") == "ok" and isinstance(data, expected) else None


def evaluate(snapshot, policy, repository, declared_visibility=None):
    """Return control evidence; callers decide mode and current-readiness authority."""
    controls = []

    def add(
        name,
        result,
        diagnostic,
        evidence=None,
        remediation="Run a fresh authorized assessment.",
    ):
        controls.append(
            dict(
                id=name,
                result=result,
                diagnostic=diagnostic,
                evidence=evidence,
                remediation=remediation,
            )
        )

    def field(name, actual, expected, remediation):
        result = (
            UNKNOWN
            if actual is None or type(actual) is not type(expected)
            else "pass"
            if actual == expected
            else "fail"
        )
        add(
            name,
            result,
            "missing-evidence" if actual is None else "observed-setting",
            actual,
            remediation,
        )

    repo = observation(snapshot, "repository")
    if snapshot["repository"].lower() != repository.lower():
        add("identity", "fail", "snapshot-repository-mismatch")
        return controls, "applicable"
    if repo is None:
        add("identity", UNKNOWN, "repository-unavailable")
        return controls, "unknown"
    if (
        repo.get("full_name", "").lower() != repository.lower()
        or type(repo.get("id")) is not int
    ):
        add("identity", UNKNOWN, "repository-identity-incomplete")
        return controls, "unknown"
    visibility = repo.get("visibility")
    if (
        visibility in ("private", "internal")
        and declared_visibility != policy["visibility"]
    ):
        return controls, "not-applicable"
    field(
        "visibility",
        visibility,
        policy["visibility"],
        "Resolve declared and observed repository visibility.",
    )
    if declared_visibility is not None and declared_visibility != visibility:
        add(
            "declared-visibility",
            "fail",
            "manifest-visibility-mismatch",
            declared_visibility,
        )
    field(
        "default-branch",
        repo.get("default_branch"),
        policy["default_branch"],
        "Review migration to the canonical default branch.",
    )
    main = observation(snapshot, "main")
    field(
        "main-exists",
        main.get("name") if main else None,
        policy["default_branch"],
        "Initialize and protect main before claiming public readiness.",
    )
    if snapshot["observations"].get("main", {}).get("status") == "absent":
        controls[-1]["result"] = "fail"

    protection = observation(snapshot, "protection")
    sets = observation(snapshot, "rulesets", list)
    effective = observation(snapshot, "main_rules", list)
    safe_sets = []
    main_unknown = False
    if sets is None or effective is None:
        main_unknown = True
    else:
        ids = {r.get("ruleset_id") for r in effective if isinstance(r, dict)}
        for rule_set in sets:
            if rule_set.get("id") not in ids:
                continue
            if "bypass_actors" not in rule_set:
                main_unknown = True
            elif (
                rule_set.get("enforcement") == "active"
                and rule_set["bypass_actors"] == []
            ):
                safe_sets.append(rule_set)
        if ids - {r.get("id") for r in sets}:
            main_unknown = True
    classic_safe = False
    if protection is not None:
        reviews = protection.get("required_pull_request_reviews")
        allowances = (reviews or {}).get("bypass_pull_request_allowances", {})
        classic_safe = (
            protection.get("enforce_admins", {}).get("enabled") is True
            and isinstance(allowances, dict)
            and not any(allowances.values())
        )
    elif snapshot["observations"].get("protection", {}).get("status") != "absent":
        main_unknown = True

    review_sources = []
    rules = []
    for rule_set in safe_sets:
        for rule in rule_set.get("rules", []):
            rules.append((rule_set["id"], rule))
            if rule.get("type") == "pull_request":
                parameters = rule.get("parameters", {})
                review_sources.append(
                    (
                        rule_set["id"],
                        {
                            "required_approving_review_count": parameters.get(
                                "required_approving_review_count"
                            ),
                            **{
                                key: parameters.get(wire)
                                for key, wire in RULESET_REVIEW_FIELDS.items()
                            },
                        },
                    )
                )
    if classic_safe and isinstance(
        protection.get("required_pull_request_reviews"), dict
    ):
        review_sources.append(("classic", protection["required_pull_request_reviews"]))

    def witness(name, values, predicate):
        successes = [
            source for source, value in values if value is not None and predicate(value)
        ]
        unknown = main_unknown or any(value is None for _, value in values)
        result = "pass" if successes else UNKNOWN if unknown else "fail"
        add(
            name,
            result,
            "no-bypass-witness" if successes else "missing-no-bypass-guarantee",
            successes,
            "Require this main control for everyone, without administrative or actor bypass.",
        )

    witness(
        "main.pull-request", [(s, True) for s, _ in review_sources], lambda v: v is True
    )
    witness(
        "main.approvals",
        [(s, r.get("required_approving_review_count")) for s, r in review_sources],
        lambda v: type(v) is int and v >= policy["main"]["required_approvals"],
    )
    for flag, expected in policy["main"]["review_flags"].items():
        witness(
            "main." + flag,
            [(s, r.get(flag)) for s, r in review_sources],
            lambda v, e=expected: v is e,
        )
    for setting, rule_type in (
        ("allow_force_pushes", "non_fast_forward"),
        ("allow_deletions", "deletion"),
    ):
        values = [(s, False) for s, r in rules if r.get("type") == rule_type]
        if classic_safe:
            values.append(("classic", protection.get(setting, {}).get("enabled")))
        witness("main." + setting, values, lambda v, e=policy["main"][setting]: v is e)
    # Inventory check contexts for preservation; no consumer-specific names are invented.
    checks = []
    if protection:
        checks.extend(
            (protection.get("required_status_checks") or {}).get("contexts", [])
        )
    for _, rule in rules:
        if rule.get("type") == "required_status_checks":
            checks.extend(
                x.get("context")
                for x in rule.get("parameters", {}).get("required_status_checks", [])
            )
    add(
        "main.check-contexts",
        UNKNOWN if main_unknown else "pass",
        "preserve-observed-contexts",
        sorted(set(c for c in checks if isinstance(c, str))),
        "Preserve these contexts when applying reviewed changes; compare before and after.",
    )

    for target in policy["references"]["targets"]:
        for operation in policy["references"]["operations"]:
            witnesses = []
            unsupported = sets is None
            for rule_set in sets or []:
                if (
                    rule_set.get("target") != target
                    or rule_set.get("enforcement") != "active"
                ):
                    continue
                matching = [
                    r for r in rule_set.get("rules", []) if r.get("type") == operation
                ]
                if not matching:
                    continue
                condition = rule_set.get("conditions", {}).get("ref_name")
                if condition != {"include": ["~ALL"], "exclude": []}:
                    unsupported = True
                    continue
                if "bypass_actors" not in rule_set:
                    unsupported = True
                    continue
                actor_match = rule_set["bypass_actors"] == [
                    policy["references"]["bypass_actor"]
                ]
                restricted = all(
                    not r.get("parameters", {}).get(
                        "update_allows_fetch_and_merge", False
                    )
                    for r in matching
                )
                if actor_match and restricted:
                    witnesses.append(rule_set["id"])
            result = "pass" if witnesses else UNKNOWN if unsupported else "fail"
            add(
                f"refs.{target}.{operation}",
                result,
                "universal-admin-only-witness"
                if witnesses
                else "missing-universal-admin-only-proof",
                witnesses,
                "Use an active all-ref rule without exclusions, with only the repository administrator role bypass.",
            )

    owners = observation(snapshot, "codeowners")
    errors = observation(snapshot, "codeowners_errors")
    permissions = observation(snapshot, "owner_permissions")
    expected_owners = {"@" + name.lower() for name in policy["codeowners"]}
    owner_result = UNKNOWN
    if owners is not None and errors is not None and permissions is not None:
        rows = owners.get("rows", [])
        if errors.get("errors"):
            owner_result = "fail"
        elif not isinstance(errors.get("errors"), list) or not isinstance(rows, list):
            owner_result = UNKNOWN
        elif not rows or not any(r.get("pattern") == "*" for r in rows):
            owner_result = "fail"
        elif any(
            set(o.lower() for o in r.get("owners", [])) != expected_owners for r in rows
        ):
            owner_result = UNKNOWN
        elif owners.get("sha") != (main or {}).get("sha"):
            owner_result = UNKNOWN
        elif any(name not in permissions for name in policy["codeowners"]):
            owner_result = UNKNOWN
        elif any(
            permissions[name] not in ("write", "maintain", "admin")
            for name in policy["codeowners"]
        ):
            owner_result = "fail"
        else:
            owner_result = "pass"
    if snapshot["observations"].get("codeowners", {}).get("status") == "absent":
        owner_result = "fail"
    add(
        "codeowners",
        owner_result,
        "same-base-coverage-and-permissions",
        {"path": owners.get("path") if owners else None, "permissions": permissions},
        "Keep both designated owners in global and overriding rows, validate syntax and verify their write access.",
    )

    security = repo.get("security_and_analysis", {})
    for feature in policy["secret_features"]:
        field(
            "secrets." + feature,
            security.get(feature, {}).get("status"),
            "enabled",
            "Enable the repository-level secret feature and read back its status.",
        )
    for setting, expected in policy["participation"].items():
        field(
            "participation." + setting,
            repo.get(setting),
            expected,
            "Preserve public fork-to-PR participation without upstream write access.",
        )
    if repo.get("has_pull_requests") is False:
        add("participation.pull-requests", "fail", "pull-requests-disabled")
    field(
        "collection.complete",
        snapshot["complete"],
        True,
        "Resolve every missing observation before readiness.",
    )
    field(
        "collection.stable",
        snapshot["stable"],
        True,
        "Repeat live assessment after concurrent settings changes stop.",
    )
    for control in controls:
        if control["id"].startswith("collection.") and control["result"] == "fail":
            control["result"] = UNKNOWN
    return controls, "applicable"


def aggregate(controls, applicability):
    if applicability == "not-applicable":
        return "not-applicable"
    results = {c["result"] for c in controls}
    return (
        "fail"
        if "fail" in results
        else UNKNOWN
        if UNKNOWN in results or not controls
        else "pass"
    )
