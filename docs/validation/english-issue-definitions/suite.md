# Full Harness validation

Tested commit `ecaa6463550d032d9fb77cbc055df1d713a4575b` from a clean checkout against `origin/main` at `577512598afe2f9a296f3b7a92acff9f40b961f2`. The local environment was Darwin arm64, Python 3.11.4, with the pinned validation dependencies and bytecode generation disabled.

`./scripts/validate/run.sh --quality-base origin/main` exited 1. The changelog check found the Unreleased entry. Plugin validation, security policy validation and SDD inventory passed.

| Suite | Tests | Passed | Failed |
|---|---:|---:|---:|
| Validators | 197 | 196 | 1 |
| Execution | 48 | 48 | 0 |
| SIFEN documentation | 15 | 15 | 0 |
| Total | 260 | 259 | 1 |

The [marketplace package-copy test](../../../tests/validators/test_plugin_marketplace.py) asserts that the expected skill count is five. The [package validator](../../../validators/plugin/validate.py) declares six. The test reported `AssertionError: 6 != 5` at line 173. Both files match the comparison revision. This failure was also observed during task planning.

The documentation review passed. CHECK-002 remains failed and prevents completion of TASK-004.
