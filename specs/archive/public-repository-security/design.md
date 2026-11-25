---
sdd_version: 3
change: public-repository-security
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013]
adrs: [docs/decisions/0018-public-repository-security-verification.md]
validation:
  - id: CHECK-001
    description: Verify canonical policy resolution, schemas, generated assets and consumer composition.
    requirements: [REQ-001, REQ-007, REQ-011]
    required: true
    method:
      kind: automated
      procedure: Run python -m unittest discover -s tests/validators -p test_security_contract.py. Assert policy/index and provider lock consistency across every profile and criticality, visibility handling, rendering from policy, conflict refusal, and exact-version consumer behavior. Missing or zero executed tests do not pass.
    inputs: &security_inputs
      include: [AGENTS.md, VERSION, requirements-validation.txt, standards, skills, validators, scripts, schemas, project-templates, tests, .github, docs/architecture, docs/decisions, docs/guides, docs/user-docs, CHANGELOG.md, plugin.json, .codex-plugin/plugin.json]
      exclude: []
    outputs: &security_outputs [docs/validation/public-repository-security]
    execution: local
  - id: CHECK-002
    description: Exercise compliant control composition and independent policy violations.
    requirements: [REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-010, REQ-012]
    required: true
    method:
      kind: automated
      procedure: Run python -m unittest discover -s tests/validators -p test_security_policy.py. Verify classic and ruleset main protections, no-bypass provenance, CODEOWNERS coverage, all-ref restrictions, secret controls and participation; independently weaken each control and assert the relevant failed or unverifiable result without changing policy or tests.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
  - id: CHECK-003
    description: Verify bounded read-only collection, report contracts and failure semantics.
    requirements: [REQ-001, REQ-003, REQ-004, REQ-005, REQ-006, REQ-009, REQ-010, REQ-012, REQ-013]
    required: true
    method:
      kind: automated
      procedure: Run python -m unittest discover -s tests/validators -p test_security_collection.py. Use synthetic transport responses to check endpoint/method restrictions, authenticated data omissions, pagination, errors, unstable observations, mode/identity binding, redaction, reports and exit codes. Assert snapshots cannot satisfy live readiness and no mutation is requested.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
  - id: CHECK-004
    description: Observe bootstrap, audit and maintenance using the actual revised Skills on synthetic projects.
    requirements: [REQ-006, REQ-007, REQ-008, REQ-009, REQ-011, REQ-012]
    required: true
    method:
      kind: review
      reason: Real agent orchestration and truthful readiness statements require supervised behavioral evidence; deterministic helper tests do not establish Skill behavior.
      procedure: Run the three bounded native-agent scenarios specified under Supervised Skill evidence, using tests/skills/security fixtures and actual version-matched Skills. Preserve original attempts and independently inspect reports, diffs, commands, permission boundaries and source/provider integrity. Require all expected observations; unavailable telemetry or unsupported behavior remains unverified.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
  - id: CHECK-005
    description: Review usable EN/PT/ES guidance, policy consistency and contributor trust boundaries.
    requirements: [REQ-006, REQ-009, REQ-010, REQ-011, REQ-012]
    required: true
    method:
      kind: review
      reason: Translation alignment, policy meaning, preservation of stronger settings and trust-boundary adequacy need semantic review in addition to structural tests.
      procedure: Follow the documented local rendering and verification commands on synthetic consumers; compare outputs, permissions and recovery instructions across EN/PT/ES. Inspect Skills, CI triggers/permissions/checkout, policy references and migration diffs for duplicated policy, privileged fork execution or implicit rollout. Verify fork-to-PR guidance and unchanged reporting/licensing boundaries.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
  - id: CHECK-006
    description: Observe the actual Harness protections with the implemented live verifier.
    requirements: [REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-009, REQ-010, REQ-013]
    required: true
    method:
      kind: manual
      reason: Live administrative settings require the trusted operator's available GitHub access and cannot be replaced by offline CI or simulated responses.
      procedure: From the reviewed provider source and a trusted operator session, run python validators/security/validate.py --repository versat-labs/versat-ai-harness --live --output docs/validation/public-repository-security/live-report.json. Retain sanitized observations and independently compare their main/review/owners/ref/security/participation fields with authenticated GET results. Require a current complete pass and unchanged required checks; preserve any failed attempt. Do not create forks, PRs, tags, secrets or destructive probes.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
  - id: CHECK-007
    description: Retain the complete Harness quality, package, SDD and execution checks.
    requirements: [REQ-010, REQ-012]
    required: true
    method:
      kind: automated
      procedure: Run PYTHONDONTWRITEBYTECODE=1 PYTHON=<prepared-python> ./scripts/validate/run.sh --quality-base origin/main with requirements-validation.txt installed. Require quality, policy validation and all existing plus new discovered tests to pass without skipped required suites. Observe final required remote CI separately before merge.
    inputs: *security_inputs
    outputs: *security_outputs
    execution: local
coverage:
  - {scenario: {requirement: REQ-001, scenario: 1}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-001, scenario: 2}, applicability: required, checks: [CHECK-001, CHECK-003]}
  - {scenario: {requirement: REQ-002, scenario: 1}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-002, scenario: 2}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-002, scenario: 3}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-003, scenario: 1}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-003, scenario: 2}, applicability: required, checks: [CHECK-002, CHECK-003]}
  - {scenario: {requirement: REQ-004, scenario: 1}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-004, scenario: 2}, applicability: required, checks: [CHECK-002, CHECK-003]}
  - {scenario: {requirement: REQ-005, scenario: 1}, applicability: required, checks: [CHECK-002, CHECK-006]}
  - {scenario: {requirement: REQ-005, scenario: 2}, applicability: required, checks: [CHECK-002, CHECK-003]}
  - {scenario: {requirement: REQ-006, scenario: 1}, applicability: required, checks: [CHECK-003, CHECK-006]}
  - {scenario: {requirement: REQ-006, scenario: 2}, applicability: required, checks: [CHECK-002, CHECK-003]}
  - {scenario: {requirement: REQ-006, scenario: 3}, applicability: required, checks: [CHECK-003, CHECK-004]}
  - {scenario: {requirement: REQ-006, scenario: 4}, applicability: required, checks: [CHECK-003, CHECK-005]}
  - {scenario: {requirement: REQ-007, scenario: 1}, applicability: required, checks: [CHECK-001, CHECK-004]}
  - {scenario: {requirement: REQ-007, scenario: 2}, applicability: required, checks: [CHECK-004]}
  - {scenario: {requirement: REQ-008, scenario: 1}, applicability: required, checks: [CHECK-004]}
  - {scenario: {requirement: REQ-008, scenario: 2}, applicability: required, checks: [CHECK-004]}
  - {scenario: {requirement: REQ-009, scenario: 1}, applicability: required, checks: [CHECK-004, CHECK-005]}
  - {scenario: {requirement: REQ-009, scenario: 2}, applicability: required, checks: [CHECK-003, CHECK-004, CHECK-006]}
  - {scenario: {requirement: REQ-010, scenario: 1}, applicability: required, checks: [CHECK-002, CHECK-005, CHECK-006]}
  - {scenario: {requirement: REQ-010, scenario: 2}, applicability: required, checks: [CHECK-003, CHECK-005, CHECK-007]}
  - {scenario: {requirement: REQ-011, scenario: 1}, applicability: required, checks: [CHECK-001, CHECK-004]}
  - {scenario: {requirement: REQ-011, scenario: 2}, applicability: required, checks: [CHECK-005]}
  - {scenario: {requirement: REQ-011, scenario: 3}, applicability: required, checks: [CHECK-001, CHECK-005]}
  - {scenario: {requirement: REQ-012, scenario: 1}, applicability: required, checks: [CHECK-002]}
  - {scenario: {requirement: REQ-012, scenario: 2}, applicability: required, checks: [CHECK-003, CHECK-004, CHECK-005]}
  - {scenario: {requirement: REQ-012, scenario: 3}, applicability: required, checks: [CHECK-007]}
  - {scenario: {requirement: REQ-013, scenario: 1}, applicability: required, checks: [CHECK-006]}
  - {scenario: {requirement: REQ-013, scenario: 2}, applicability: required, checks: [CHECK-003, CHECK-006]}
regression:
  - {obligation: {impact: 1, scenario: 0}, checks: [CHECK-002], rationale: Retain protected main and required checks while adding explicit public enforcement.}
  - {obligation: {impact: 2, scenario: 1}, checks: [CHECK-005, CHECK-006], rationale: Preserve the public contribution route and distinguish participation from upstream write authority.}
  - {obligation: {impact: 2, scenario: 2}, checks: [CHECK-003, CHECK-006], rationale: Require actual accessible control evidence and retain unknowns as readiness blockers.}
  - {obligation: {impact: 2, scenario: 3}, checks: [CHECK-004, CHECK-005, CHECK-006], rationale: Keep observation separate from authorized mutations and verify actual operational outcomes.}
  - {obligation: {impact: 3, scenario: 0}, checks: [CHECK-004], rationale: Retain the distinct bootstrap/audit/maintenance capabilities and truthful readiness boundaries.}
  - {obligation: {impact: 4, scenario: 0}, checks: [CHECK-001, CHECK-004], rationale: Preserve base composition and exact provider adoption while adding conditional security assets.}
  - {obligation: {impact: 5, scenario: 0}, checks: [CHECK-003, CHECK-007], rationale: Extend validation without replacing existing suites or claiming remote compliance from local checks.}
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 50b4b5a3bf0759a420fa5833569295f44b0b76a40f05b8ad14de2036899f84eb
  approval:
    source: Developer reply in this Codex chat approving Design R1 and ADR-0018 and requesting Tasks.
    quote: Aprovo o Design R1 e o ADR-0018. Avance para as Tasks.
    revision: 1
    digest: a63f195eedd6c04621fa38c7b8cecb98b0c6d66c8a393005ee474d08299736bf
---

# Design

## Current state

Proposal/Requirements R1 is approved. The current provider source is Harness 0.4.0 on `codex/public-repository-security`, based on `c191f3b126c659fbabfd4ed3d40b474407cfd26a`. The three Skills resolve Standards but lack a complete executable public-security gate. `validators/security/` has no implementation. The existing provider verifier already resolves index paths and verifies exact version/commit/content digests; it accepts YAML Standards as well as Markdown paths, so a second resolution algorithm is unnecessary.

The authorized GitHub operation was completed before this Design: two active administrator-only rulesets, both secret features enabled, unchanged classic main protection and fork/PR participation. Those observations are not evidence that the proposed implementation exists. CHECK-006 will re-observe them with the actual verifier. No new remote mutation is part of Design preparation.

The architectural addition is proposed in ADR-0018. This document specifies behavior and checks; every new module/command below remains planned until the later implementation gate.

## Proposed design

### Canonical policy and component ownership

| Component | Responsibility |
| --- | --- |
| `standards/core/git.md`, `standards/core/security.md` | Human-readable mandatory public baseline, its applicability, authority and evidence limits. |
| `standards/core/public-repository-security.yaml` | Typed canonical policy values: policy ID/version, host/visibility/default branch, owners, review requirements, admin role, reference operations, secret features and participation settings. |
| `standards/index.yaml` | Include that policy under `core.always` for every profile and criticality; applicability remains a condition inside the policy. |
| `schemas/public-repository-security.schema.yaml` | Validate policy shape and supported semantics, with no duplicate owner lists or configurable policy thresholds in schema code. |
| `schemas/repository-security-snapshot.schema.yaml`, `schemas/repository-security-report.schema.yaml` | Versioned observation and result formats; unknown data remains explicit. |
| `validators/security/policy.py` | Pure policy loading/validation and control evaluation with no network or configuration writes. |
| `scripts/security/github.py` | Bounded authenticated GET-only collector using GitHub CLI; returns normalized observations and collection diagnostics. |
| `validators/security/validate.py` | Explicit command modes, source/consumer identity, report output and exit status; orchestrates collection and pure evaluation. |
| `scripts/bootstrap/public_security.py` | Local renderer of CODEOWNERS and baseline settings from policy; no GitHub API calls and no destructive overwrite. |
| `project-templates/artifacts/github-public-security/README.md` | Conditional adoption instructions for generated assets, linked from the existing composition guide. |
| Existing three Skills and bootstrap lifecycle reference | Resolve the contract, invoke verification, preserve authorization and use its result in readiness reporting. |

The YAML policy has `schema_version: 1`, a stable policy ID, an explicit semantic `policy_version`, and a `kind` identifying this contract. Values live there once. The index includes its path exactly like other Standards; consumer locks include the file's exact provider version and SHA-256. Package checks enforce one matching policy and reject an absent, duplicated, unsupported or invalid policy. Git and Security prose reference that entry and explain the rules. Skills link to resolution and execution guidance rather than repeat usernames/settings.

Consumer mode invokes the existing exact-provider verification contract before assessment; it does not infer a different provider or downgrade a bad lock. Direct provider-source mode is allowed for this repository and development evaluation, records actual version/commit/dirty state and policy digest, and never claims an installed consumer was migrated. No broad refactor of provider verification is required.

### Public command and result contract

The entry point has three mutually exclusive modes:

```sh
# Local contract check; no GitHub access or public-readiness claim.
python validators/security/validate.py --check-policy

# Current read-only assessment from a trusted operator session.
python validators/security/validate.py --repository owner/repository --live --output /tmp/security-report.json

# Offline assessment, always labeled as supplied snapshot evidence.
python validators/security/validate.py --repository owner/repository --snapshot /tmp/settings.json --output /tmp/security-offline.json
```

`--project-root /absolute/consumer` adds manifest/lock verification for installed consumers. The provider is the package containing the invoked entry point, not a path or executable supplied by the consumer. No API write/apply option exists. The repository is explicit and validated as a GitHub owner/name; optional guidance may help the operator inspect origin, but the command does not choose a remote silently.

Reports include schema version, repository numeric ID/name/host, requested mode, applicability, provider and policy identities/digests, observation start/end, pinned main commit, collection completeness, per-control result/evidence/diagnostic/remediation, aggregate result and `public_ready`. Normal output is concise; `--output` writes the explicit JSON report atomically to an allowed local path. Tokens, secret values, full process environments and arbitrary raw API errors never enter it.

For applicable assessments, results are `pass`, `fail` or `unable-to-verify`. A demonstrated violation takes aggregate precedence over unknown controls, while all unknowns remain listed. An observed out-of-scope private repository is `not-applicable` only when it does not contradict a declared public consumer. Missing identity/visibility is unknown; declared-versus-observed visibility mismatch fails and cannot skip the public rules. Unsupported hosts are explicitly outside the implemented transport and cannot yield public readiness.

Exit codes are 0 for a successful requested assessment, 1 for demonstrated non-compliance, 2 for invalid input or unverifiable required evidence, and 3 for a genuinely non-applicable target. Only a complete passing `--live` assessment of an applicable target sets `public_ready: true`. `--check-policy` and `--snapshot` can exit 0 for their limited purpose but always set `public_ready: false`. Skills must check both the mode and readiness field, not just process success. A saved report cannot satisfy a later readiness decision; a new live run is required.

### Authenticated observations and consistency

The collector executes `gh api --hostname github.com --method GET` with argument arrays, JSON Accept headers and an explicit supported REST API version. It does not use a shell, consumer-defined commands, arbitrary hosts, token command-line arguments or write verbs. Authentication is supplied by the trusted session through normal GitHub CLI mechanisms. Debug output is disabled and stderr is converted to allowlisted diagnostics. The transport is injectable only in tests, not through a production `--trust-fixture-as-live` switch.

Collect these observations:

1. Repository metadata: immutable ID, actual visibility, default branch, secret control status, fork and PR creation settings.
2. `branches/main` and `branches/main/protection`: main identity, classic enforcement/reviews, bypass allowances, deletion/force-push settings and required checks.
3. Paginated `rules/branches/main`, the full repository ruleset list with `includes_parents=true`, and details for every relevant ruleset, including enforcement, conditions, provenance, parameters and bypass actors.
4. The effective CODEOWNERS file at the observed main SHA, using GitHub precedence `.github/CODEOWNERS`, `CODEOWNERS`, then `docs/CODEOWNERS`; CODEOWNERS errors at that same SHA; permissions for both designated accounts.

Follow pagination only on the same allowed host and scoped route. Preserve endpoint status and completeness rather than treating a failed request as an empty collection. Default limits are a 30-second per-request timeout, 180-second total collection budget, 100 pages per endpoint and 4 MiB per response; hitting a limit yields unverified observations and no readiness. No automatic retry loop or fallback to an untrusted source is used. Exact values are transport bounds, not corporate security policy.

Explicitly classify 401/403, rate limiting, timeout, malformed JSON, unexpected redirects, missing fields, ambiguous 404s and unavailable inherited details. A confirmed missing main/protection is a policy finding; a permission-obscured endpoint is unknown. Optional empty fields may be normalized only where the supported API contract establishes empty semantics on a complete authorized response. In particular, an omitted ruleset `bypass_actors` is unknown, not an empty bypass list.

For a candidate pass, perform a second complete normalized collection and require identical repository identity, main SHA and control-relevant fields. Ignore only observation timestamps and non-control response metadata. Changes during collection yield `unable-to-verify`, retain both observation digests and ask for a fresh run; do not silently select a favorable sample. This bounds inconsistency without claiming a GitHub transaction or immunity to drift after the run.

Snapshot export contains only the allowlisted fields required for assessment, response status/completeness and source identities, plus parsed ownership evidence. It excludes raw headers, tokens, unrelated repository metadata and comments from CODEOWNERS. Imported snapshots are schema-checked, repository-bound and always marked supplied/offline; editable hashes or timestamps do not authenticate them.

### Deterministic enforcement assessment

**Main.** Evaluate effective protection per required control with provenance. A classic source contributes a no-bypass guarantee only with administrator enforcement and no permitted review bypass. Active applicable rulesets contribute only the controls for which their bypass list is explicitly empty. The effective branch endpoint establishes applicability of rulesets to main; details establish bypass and enforcement. Aggregate sufficiently strong no-bypass contributions across sources. A permissive source cannot weaken another source's verified restriction, and an administrator exception in an all-branches management ruleset does not itself invalidate independently protected main.

Require PR review, minimum one approval, code-owner review, stale-review dismissal and last-push approval, plus blocked force push and deletion. More required approvals/checks are preserved. Retain and report existing required status checks; generated main settings never replace a consumer's check contexts with a Harness-specific name. A missing canonical main/default mismatch, incomplete source or unsupported bypass semantics cannot pass. Unknown applicable semantics that could affect a required guarantee remain unverified; unrelated additive restrictions are retained, not stripped.

**Branches and tags.** For each target and each of creation/update/deletion, require an active universal ruleset witness with `include: ["~ALL"]`, no exclusions and the repository administrator role 5 as its only bypass actor in `always` mode. Separate compatible witnesses may supply different operations. `pull_request`/`exempt` bypass, extra actor classes, custom role assumptions or permissive update exceptions are not accepted as the baseline. In particular, an update parameter permitting fetch-and-merge outside this restriction is not equivalent to administrator-only updates. Rules matching only observed references never prove future-name coverage. Alternative pattern unions are unverified unless a future reviewed evaluator explicitly proves their complete semantics; diagnostics distinguish unsupported proof from demonstrated holes.

**Owners.** The supported canonical layout begins with global `* @elviszoz @evertonspohrversat`; comments and redundant path rows retaining both owners are allowed. GitHub's same-SHA CODEOWNERS error response must be empty, and both accounts must have at least write permission. For this proof shape, any path and CODEOWNERS itself retain the designated eligible owners without reimplementing GitHub glob matching. Missing global coverage, active empty ownership or unrelated-owner overrides cannot pass. Complex/shadowed overrides that the evaluator cannot safely interpret are unverified and require reviewed normalization; the renderer never overwrites them. The documented limitation prevents claiming an arbitrary syntactically valid file has complete effective coverage.

**Secrets and participation.** Require both repository secret features explicitly `enabled`; public defaults and account-level push protection are insufficient. Require public visibility, allowed forks and PR creation for all contributors. Branch/tag rules are scoped to the upstream repository; no push ruleset over the fork network is generated. The result establishes the observed participation configuration, not an actual submission by an external person. Existing contribution, provenance, license and confidential-reporting requirements remain applicable.

### Local rendering and lifecycle integration

`scripts/bootstrap/public_security.py --output <empty-staging-directory>` reads the index-resolved policy and renders `.github/CODEOWNERS`, main/branches/tags ruleset JSON and a repository secret-settings payload. It writes a manifest containing provider/policy identity and asset digests. Output is staging material, not an applied configuration. Refuse symlink destinations, traversal, nonempty conflicting files and implicit overwrite; deterministic identical content is reported as already matching. Ruleset names are stable labels, never proof of identity or compliance.

The main ruleset has no bypass actors and supplies PR/review/deletion/non-fast-forward controls. Branch/tag rulesets use administrator-only bypass solely for reference administration. A new repository can use all three. Existing classic main protection, such as the Harness's, need not migrate when its effective guarantees already pass. The renderer is deliberately limited to these assets; it neither composes an entire project nor calls GitHub.

The existing composition guide gains a conditional public-GitHub security section. Public assets are generated once over the shared base and not copied into each profile. Private projects do not receive an accidental public-governance assertion. Consumer-specific ownership, checks or ruleset conflicts are compared in staging and reconciled through review; generated defaults are never blindly PUT over existing GitHub configuration.

| Skill | Required integration and stopping behavior |
| --- | --- |
| `project-bootstrap` | Resolve policy and actual target, stage assets, use existing operational authorization for configuration, then run live verification before public readiness. A local skeleton, missing main or inaccessible remote remains incomplete. |
| `project-audit` | Run exact-provider verification and live control assessment, report severity/evidence/remediation per gap and unknown, and remain read-only unless remediation was requested. |
| `project-maintenance` | Compare the exact target baseline with observed state, preserve stronger controls/content, stage concrete differences, apply only authorized changes and rerun live verification. Never mark failed or unavailable remediation complete. |

Skills retain their existing product, SDD, profile, versioning and test responsibilities. Preparation of a new main reference is explicitly distinct from public readiness; no standing initial-push bypass is introduced. The operational command sequence remains a documented administrative procedure using existing authorized tools, not a second mutation implementation hidden inside the validator.

## Boundaries and contracts

ADR-0018 extends the current root package architecture. `standards/index.yaml` remains the resolution authority. Schema validation checks syntax; pure policy evaluation checks supported observations; the collector observes GitHub; Skills orchestrate; GitHub enforces; reviewers approve policy and delivery. None substitutes for another layer.

No SDD schema/gate or executor language is changed. Consumer identity stays in the existing manifest and lock; the repository target is an explicit command argument, so no speculative provider/remote fields are added to the manifest. `scripts/validate/run.sh` gains the network-free policy-contract check, and normal unittest discovery includes the security suites. The live command remains a separately required public-readiness check, not an implicit network dependency of every local/package test.

## Data, security and permissions

Use least-privilege credentials sufficient for the required metadata/content/collaborator and administrative reads. Insufficient access is an honest incomplete result. The verifier does not create credentials, inspect secret alerts/values, grant roles or mutate rules. Configuration operations remain separate and explicitly authorized. The prior Harness operation grants no organization-wide rollout.

Existing PR CI keeps `contents: read`, nonpersistent checkout credentials and no administrative secrets. No `pull_request_target` execution of contribution code, privileged checkout, model credential or automatic write-capable workflow is introduced. Automated transport tests use synthetic responses in process; no production token is needed. Supervised fixtures contain synthetic identities and locally generated reports, never exported authenticated sessions.

## Operations and observability

Each control reports observed versus required settings, a stable diagnostic identifier, provenance and remediation action. Readiness requires all mandatory controls and required observations, not merely a count of successful tests. Preserve failing attempts; live reruns replace no prior evidence. Local evidence under `docs/validation/public-repository-security/` is scrubbed and bound to actual tested input digests through the existing SDD records.

The current readbacks for rulesets 28023884/28023891 and enabled secrets are useful baseline facts, but CHECK-006 executes the new verifier and captures fresh observations. It compares required main check contexts to the preexisting baseline rather than deciding new required check names. No destructive push, real secret, artificial fork or external PR is needed. Later GitHub drift invalidates current readiness and requires fresh observation; this scope does not create an always-on monitor.

## Migration, rollout and rollback

Implement on the existing governed branch after Tasks approval and execution authority. Retain provider metadata at 0.4.0 during source development, add an accurate Unreleased entry for the delivered behavior, update architecture/ADR index and affected technical/user guides, run required checks, prepare the dossier and submit through authorized PR review. Design-time release notes describe only the proposed ADR and must not imply shipped functionality.

The new mandatory readiness baseline warrants a subsequent reviewed semantic release (expected next minor 0.5.0); publication and exact metadata/tag selection remain a separate release operation. No installed 0.4.0 package, marketplace reference or consumer lock is modified by this work. New-release consumers include the YAML policy digest; existing consumers migrate through `project-maintenance` with exact target refs and preserved custom checks.

Update maintained bootstrap, audit, maintenance and GitHub-delivery user guides in EN/PT/ES, the template composition guide, security validator README and architecture overview. Explain commands, supported proof shapes, permissions, status/exit semantics, incomplete/bootstrap outcomes and safe recovery. A user must be able to follow the documented example without private-only context.

Rollback preserves reports and reviewed history. Revert source/consumer integration through review and restore the prior exact provider/configuration together if necessary. Do not disable already-correct GitHub security settings as a side effect of rolling back a client validator. For a legitimate configuration conflict, prepare the minimum authorized adjustment while retaining required main protections; never use broad bypass as recovery. There is no data migration or user data store.

## Alternatives considered

ADR-0018 records the main alternatives. Reuse the existing exact-provider resolver instead of adding another Standards list. Use additive readiness commands instead of credentials in fork CI. Render minimal reviewable assets instead of adding a provisioning engine. Accept provable classic/ruleset combinations instead of forcing migration of the correctly protected Harness main. Prefer explicit unsupported/unverified diagnostics to an approximate complete GitHub rules engine.

## Validation plan

All 31 acceptance positions and seven impact obligations are mapped above, with no not-applicable exclusions. CHECK-001 through CHECK-003 add maintained offline suites under `tests/validators/`; synthetic fixtures live under `tests/fixtures/security/`. CHECK-007 retains every existing suite and CI eligibility constraint. Required automated tests are discovered by current local/CI validation; no test needs an authenticated external service.

Control mutations cover review count zero, missing code-owner/stale/last-push settings, disabled admin enforcement, bypass entries, force/deletion permissions, disabled/evaluate rulesets, excluded/nested/future refs, missing ref operations, extra bypass roles/apps, permissive update parameters, missing or erroneous owners, unavailable owner permissions, disabled secrets and restricted participation. Positive cases include current classic-main-plus-two-rulesets, all-ruleset deployment, split sufficient no-bypass control sources and stronger compatible review/check requirements. Mutation assertions identify the affected control, rather than merely checking any nonzero exit.

Collection tests cover complete mult-page data, hidden bypass actors, missing fields, confirmed versus ambiguous 404, 401/403/429/5xx, time/size/page limits, wrong repository/host, malformed JSON, changing main/settings between samples, sanitized errors, safe explicit report output, forbidden write methods and an offline success that still cannot satisfy readiness. Renderer tests cover every profile through shared composition, deterministic content, conflicting files, unsafe paths and preservation of existing assets. Policy and snapshot tests reject unsupported versions and invalid structures.

### Supervised Skill evidence

Add versioned case prompts and fixture/verification support under `tests/skills/security/`, reusing the existing snapshot/attempt-record procedure where compatible. At implementation validation, run exactly one fresh native subagent per case, sequentially, with no inherited implementation conversation. Supply the actual revised Skill path, fixture/provider identity, prepared Python and allowed local scope. No remote connector calls or credentials are authorized for these cases.

| Case | Observable assertions |
| --- | --- |
| `public-bootstrap-unavailable` | A prepared synthetic public project has product context and version-bound development evidence, but no live administrative access. The Skill resolves the contract, stages safe assets, invokes the relevant check, preserves existing product/profile material and explicitly withholds public readiness without inventing authorization. |
| `public-audit-drift` | A synthetic project supplies a snapshot with separately observable missing stale-review protection and disabled push protection while local tests pass. The Skill reports both failures and offline/current-evidence limits, preserves all project files and proposes concrete remediation. |
| `public-maintenance-conflict` | A synthetic consumer has custom stronger required checks, a conflicting ownership file and an exact target source fixture. Authorized local migration preparation produces a reviewable diff without overwriting the conflict or weakening checks. Independent replay of before/after snapshots remains labeled offline, unknown live remediation remains open, and no implicit provider upgrade or GitHub write occurs. |

Use a monitored 600-second limit per case and 1800 seconds for the three-case suite, including independent review. Interrupt on limits and retain failures/unknowns; do not retry automatically or select a favorable attempt. Capture actual prompts, available tool/action observations, original reports/diffs, manifests and input digests. After each agent stops, preserve its outputs, independently replay the relevant verifier/renderer on separate copies, inspect file integrity and compare the specific assertions. A narrative alone or a simulated live response cannot pass the case. Unavailable native runtime/observations leaves required evidence unverified; any later rerun requires explicit recorded scope.

CHECK-005 reviews actual documentation and security meaning; CHECK-006 supplies the separate authenticated production observation. Together they preserve the historical contribution/control/authorization scenarios without manufacturing a new external contribution or treating offline Skill cases as live GitHub enforcement. Final required remote CI and human PR review remain delivery facts outside local evidence.

## Planning review

The developer approved Design R1 and ADR-0018 in this Codex chat: "Aprovo o Design R1 e o ADR-0018. Avance para as Tasks." The Design approval binds digest `a63f195eedd6c04621fa38c7b8cecb98b0c6d66c8a393005ee474d08299736bf`; substantive design, coverage and regression mappings remain unchanged. Proposal/Requirements R1 remains approved at digest `50b4b5a3bf0759a420fa5833569295f44b0b76a40f05b8ad14de2036899f84eb`. This response authorizes Tasks preparation only. Implementation and execution of the planned security checks await the next gate and execution instruction.
