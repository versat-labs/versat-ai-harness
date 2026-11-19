# Project validation

Use this guide to adopt quality checks and explicit test execution in a consumer project. Run `./scripts/validate/run.sh --quality-base origin/main` to validate the Harness source itself. Consumer validation requires a reviewed provider revision containing the integration.

## Prerequisites and adoption

Use Python 3.11 on Linux or macOS and a virtual environment with the selected provider's `requirements-validation.txt` installed. Provision application dependencies separately. The executor never installs dependencies. Windows process cancellation is currently unverified and execution is rejected.

1. Select a reviewed exact Harness version and full Git commit containing this feature. Supply a clean local checkout at that commit; set `VERSAT_HARNESS_ROOT` to its absolute path. No fallback to `latest` occurs.
2. Keep the project's `.versat/project.yaml` and `.versat/standards.lock` consistent with that checkout. Resolve Standards through `standards/index.yaml`; record each selected path, version and SHA-256 digest. The wrapper checks identity schemas, index resolution, version, commit, clean provider state and Standard digests before execution. A Plugin installation without verifiable Git provenance is not sufficient for this wrapper.
3. Follow [template composition](../../project-templates/README.md), adding the optional [Python validation assets](../../project-templates/artifacts/validation/README.md) over the existing base/profile. Include hidden files. Review conflicts instead of overwriting existing wrappers, CI or configurations. Preserve custom framework commands by adding a report adapter when needed.
4. Configure `.versat/validation.yaml` with every required suite, maintained tests and actual source/configuration inputs. Add meaningful project tests. The reference assets deliberately contain no placeholder passing tests.
5. Inspect and run from the consumer root. Select the dependency environment's interpreter explicitly:

```bash
export VERSAT_HARNESS_ROOT=/absolute/path/to/reviewed-harness
export PYTHON=/absolute/path/to/validation-venv/bin/python
"$PYTHON" "$VERSAT_HARNESS_ROOT/scripts/testing/provider.py" --root .
"$PYTHON" "$VERSAT_HARNESS_ROOT/scripts/testing/run.py" inspect --root .
bash scripts/validate/run.sh --quality-base origin/main
```

`inspect` checks configuration and command prerequisites without executing project commands. A missing identity, mismatched pin or unavailable executable must be fixed before a usable consumer run. For Harness development fixtures only, invoking `scripts/testing/run.py` directly records the provider source digest without asserting a released clean installation. Do not describe those fixtures as a deployed consumer.

## Coding conventions and changelog

Review the [Coding and Changelog Standard](../../standards/core/coding.md) and the applicable technology Standard. Reviewers assess SOLID, clarity and note accuracy. Ruff checks lint and formatting for complete added, modified and renamed Python files using the pinned dependency and the project's `ruff.toml`. The command checks the tracked working tree, including staged additions and tracked edits without a commit. Stage new files before checking. Review any formatter exclusions with their rationale.

Local full validation needs an explicit comparison revision. Use a fetched `origin/main` for integration review or `HEAD` for edits relative to the current commit. Replace `origin/main` if your project uses a different base. For a quality-only diagnostic, use `bash "$VERSAT_HARNESS_ROOT/scripts/validate/quality.sh" --root . --base origin/main` with the same interpreter. For a missing Ruff or base error, install the pinned dependencies or fetch the required history and rerun. A format diagnostic identifies files to format and recheck. Neither check writes changes.

A change limited to a planning dossier under `specs/changes/` is exempt from an Unreleased entry. A change to application behavior under `src/` requires a new bullet under `## [Unreleased]` in `CHANGELOG.md`. Updating a prior release entry alone fails. The check reports its classification and any missing entry.

## Configuration

[The schema](../../schemas/validation.schema.yaml) is authoritative for version 1. The Python reference uses:

```yaml
schema_version: 1
required_suites: [unit]
suites:
  - id: unit
    kind: tests
    argv: ['{python}', '-m', unittest, discover, '-s', tests]
    cwd: .
    timeout_seconds: 300
    result: unittest
inputs:
  include: [.versat/validation.yaml, .versat/standards.lock, .versat/project.yaml, scripts, src, tests]
  exclude: []
```

Commands are argument arrays, executed without implicit shell expansion. Only whole arguments `{python}`, `{harness_root}` and `{report}` are substituted. Paths are project-relative, without traversal, symlinks or special files. Review the complete input scope, including imported helpers, fixtures and dependency lockfiles; the executor detects known command files outside the scope, but cannot discover every transitive dependency. Keep outputs outside reviewed inputs or explicitly exclude their stable directory. The default is `.versat/validation-runs/`.

`kind: tests` requires `unittest` or `json-v1`. A custom framework wrapper writes the fresh `{report}` file according to [the count schema](../../schemas/validation-result.schema.yaml): `schema_version`, `collected`, `executed`, `skipped`, `failed`, `errors`. Collected equals executed plus skipped; failures and errors count distinct executed cases. Empty/all-skipped discovery, malformed counts, assertions or a nonzero command exit fail. A passing exit alone is reserved for `kind: check`, `result: exit-code`, such as lint or a schema check. Reports are producer claims; review the adapter and assertions.

The executor inherits only basic process environment (PATH, locale and temporary-directory settings), plus explicit noncredential `environment` names. Credential-like names are rejected. It does not inject service credentials or provide general service orchestration. Do not place secrets in arguments or output; retained logs are capped, not secret-redacted. Configure application checks requiring other capabilities through a reviewed integration.

## Full, targeted and SDD runs

The full project wrapper runs the quality check and all `required_suites` independently. The JSON report describes the suites. Check the quality diagnostics and final wrapper exit status for the aggregate outcome. During development, `bash scripts/validate/run.sh --suite unit` is targeted even when it selects the only required suite. Targeted success never claims full readiness and cannot export SDD evidence. Independent required suites still execute after an assertion failure; cancellation stops the attempt. No automatic retries occur.

For an approved automated SDD v3 check with matching inputs, execution context and stable outputs:

```bash
bash scripts/validate/run.sh --quality-base origin/main --change example-change --check CHECK-001
```

The full attempt exports `sdd-result.json` containing the Tasks plan digest and one observed result. Review it before recording it in Tasks. The executor does not edit the dossier, approve plans, complete tasks, assess scenarios or resolve findings. A manual check cannot be exported as automated execution. CI uses `--execution ci` only for checks approved in that context.

Each attempt has a unique directory with `result.json`, per-suite bounded stdout/stderr, structured counts and, when eligible, the SDD fragment. The terminal reports its path. Exit codes are 0 pass, 1 failure, 2 unavailable/unverified. A `running` file without finalization is incomplete, never passing. A timeout/interruption terminates the process group. Configuration, provider or input changes during execution prevent fresh success and SDD export. Preserve failed attempts; an explicit rerun creates another directory.

Successful full validation means the quality check and configured suites passed. Assess new behavior, retained regressions, errors and boundaries against actual assertions. Add missing coverage; reuse adequate tests. A new happy-path test cannot replace retained checks. Apply the index-resolved Testing Standard for manual checks and reviewed retirement. See [SDD usage](../../sdd/README.md).

## CI and rollback

Adapt the reference CI to existing project authentication and framework setup. Replace its explicit commit placeholder with the reviewed provider commit; do not add broad credentials or an unpinned fallback. CI runs the complete wrapper. Give the project checkout full Git history and pass the GitHub event file through `VERSAT_QUALITY_EVENT`. The base is the PR base for its merge revision, the previous tip for an existing branch push, or the merge base against the remote default branch for a new branch. A first single root commit on the default branch can use an empty-tree comparison. A multi-commit push checks its final revision. Missing history fails the quality check. The Harness keeps structural and archive checks scoped to PRs and main pushes. Check the remote ruleset before relying on required-check enforcement. The Harness source also has separate [supervised Skill evaluations](skill-evaluations.md).

Before adoption, retain the original wrapper, Ruff and suite configuration, CI and lockfile in the reviewable Git change. Roll back those files and the provider reference together; rerun the restored original suite. Do not delete maintained regressions or failed evidence to make adoption appear successful. Source changes alone neither publish a release nor migrate consumers.

## Documentation reporting

Open the PR's **Checks** tab, select the documentation report, and open its details to see the job summary. It identifies the tested Git revisions and checks for readable, nonempty English, Portuguese and Spanish Markdown files in changed guide sets. Its scope covers `docs/user-docs/`, the product reader overview, and the known legacy quickstart paths. The report also lists what reviewers need to judge, including navigation, factual accuracy, feature rationale, translation meaning and publication access.

To see the same output locally, commit the snapshot to compare and run the following from the target repository. Use an available base revision.

```sh
bash /path/to/exact-harness/scripts/validate/documentation.sh --root . --base origin/main
```

For optional GitHub adoption, review and copy the [workflow example](../../project-templates/artifacts/validation/documentation/.github/workflows/documentation-report.yml). Replace the placeholder with the reviewed full commit from `.versat/standards.lock`. The example verifies the provider and its selected Standards before comparing the consumer repository. Use a separately reviewed checkout integration if the provider requires private access. A fork run with unavailable access remains unverified. Return to the failed step and verify access, the pin and the comparison history before retrying.

Policy row failures remain advisory. An unavailable comparison or runner failure is visible in the optional check. A summary does not establish semantic compliance or satisfy the required suites. To roll back, remove the optional workflow or restore the reviewed prior integration and its matching lockfile. Use normal repository review for either change.
