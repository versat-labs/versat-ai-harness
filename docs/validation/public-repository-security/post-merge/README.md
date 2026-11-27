# Post-merge validation of public repository security

The push workflow on squash commit `577512598afe2f9a296f3b7a92acff9f40b961f2` reported two independent errors. Main had incorporated the SIFEN Skill in PR #42 after the source of PR #48 was tested. The relocation test expected five entries although the validator catalog contained six. The archived security change also declared broad input scopes covering Skills, validators and tests. Its seven previous snapshots described the earlier package. [Failed structural job](https://github.com/versat-labs/versat-ai-harness/actions/runs/45688900556/job/139468798655)

The original marketplace suite reproduced the cardinality error locally (one failure in 14 tests). The repair compares actual package Skill directories containing SKILL.md to the validator's expected names, then resolves each Skill's resources after relocation. All 14 marketplace tests passed after the repair. The validation plan, input scopes, approvals, CI gates and release version are unchanged.

## Current observations

- CHECK-001 through CHECK-003 executed the contract, policy and collection suites. The suites check exact resolution and safe composition, independent failures for each protection, and read-only collection and evidence limits.
- CHECK-004 uses the three versioned prompts from tests/skills/security and the corresponding actual provider Skills, each in a fresh native agent with a separate synthetic fixture. Per-case original archives include reports and execution records. The coordinator checked original consumer hashes and replayed the verifier, renderer and tests in separate copies. Timing and control results are recorded with the case identifiers.
- CHECK-005 exercised the documented renderer and both local verification modes. The 12 maintained EN/PT/ES guides include the same provider, command, permission and readiness boundaries. One eligible owner's approval is sufficient. Fork CI uses ordinary PR events and read-only checkout. Review of the integration changes showed no change to those contracts.
- CHECK-006 executed live verification and an independent authenticated GET comparison at the new main SHA. Both samples agreed. Main still requires one eligible owner's review, stale review dismissal, independent approval of the latest push and the existing structural-validation status check. The two universal ref-management rules and repository secret protections remain active. The independent report records fork/PR participation and both owner permissions.
- CHECK-007 executed the full package entry point with the quality base pinned by origin/main at 5775125. All 197 validator, 48 execution and 15 SIFEN tests passed. The job also checked formatting, lint, package structure and policy.

Each CHECK record includes the input digest from before and after its execution. Earlier evidence in the parent directory retains the original PR's observed environment and results. The archived Tasks file points to the new records.

## Supervised case outcomes

| Case | Independent observation |
| --- | --- |
| Bootstrap without administrative access | All six rendered files matched. The verifier returned exit 2 because it could not establish repository identity. |
| Audit with two injected failures | The verifier returned exit 1. Of 24 controls, only stale-review dismissal and secret-scanning push protection failed. |
| Maintenance with conflicting ownership | The proposal preserved the specialist, the exact lock, two approvals and both strict required checks. Its additional specialist left ownership unresolved. The agent's initial expectation of a passing modeled snapshot was incorrect. The agent recorded the actual exit 2 and the independent replay confirmed it. |

All three offline cases kept `public_ready` false. [Case prompts](native-prompts.json), [execution windows](CHECK-004.json) and [independent comparisons](scenario-review.json) accompany the original and replay archives. The [live Harness report](live-report.json) records a separate administrative observation.

## Archive verification

The [delivery check](delivery.json) assessed all 31 scenarios and seven regression obligations with zero stale results and zero open findings. The [original push baseline](original-baseline.json) selected the same archived change and passed. The [full preflight log](preflight.txt) records the package checks against the PR base with archive validation required.
