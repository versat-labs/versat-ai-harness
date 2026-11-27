# Full Harness validation

## Initial run

Tested commit `ecaa6463550d032d9fb77cbc055df1d713a4575b` from a clean checkout against `origin/main` at `577512598afe2f9a296f3b7a92acff9f40b961f2`. The local environment was Darwin arm64, Python 3.11.4, with the pinned validation dependencies and bytecode generation disabled.

`./scripts/validate/run.sh --quality-base origin/main` exited 1. The changelog check found the Unreleased entry. Plugin validation, security policy validation and SDD inventory passed.

| Suite | Tests | Passed | Failed |
|---|---:|---:|---:|
| Validators | 197 | 196 | 1 |
| Execution | 48 | 48 | 0 |
| SIFEN documentation | 15 | 15 | 0 |
| Total | 260 | 259 | 1 |

The [marketplace package-copy test](../../../tests/validators/test_plugin_marketplace.py) asserts that the expected skill count is five. The [package validator](../../../validators/plugin/validate.py) declares six. The test reported `AssertionError: 6 != 5` at line 173. Both files match the comparison revision. This failure was also observed during task planning.

The documentation review passed. This first CHECK-002 failure blocked TASK-004.

## Corrected run

Commit `a5860da` replaces the fixed skill count with a comparison of the copied skill names and the package validator's expected names. All 14 marketplace tests passed. A local substitution of one expected name also produced the intended assertion failure while preserving the total count.

The full retry used a clean checkout of the originally approved implementation (`ecaa646`) with that correction applied (`85ba7c8a223220e37b6f16b97f0f8703bd44938b`). This allowed the suite to validate the code before the previous failed result in the active dossier was superseded. The declared CHECK-002 inputs matched the working branch and had digest `62b5109f74b31339296042651851830039b7f379127307136375cd2f296ab994` both before and after execution.

With the same environment and comparison revision as the initial run, `./scripts/validate/run.sh --quality-base origin/main` exited 0. All 197 validator tests, 48 execution tests and 15 SIFEN documentation tests passed (260 total). The changelog check, Ruff lint and formatting checks, package validation, security policy check and SDD inventory passed. This resolves FIND-001.
