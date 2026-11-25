---
sdd_version: 3
change: public-repository-security
tasks:
- id: TASK-001
  description: Add the index-resolved public-security policy and versioned policy, snapshot and report contracts.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-010
  - REQ-011
  status: completed
- id: TASK-002
  description: Implement pure effective-control assessment with positive and independent negative regression tests.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-010
  - REQ-012
  status: completed
- id: TASK-003
  description: Implement bounded GET-only GitHub collection, explicit CLI modes and trustworthy readiness reporting.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-009
  - REQ-010
  - REQ-012
  - REQ-013
  status: completed
- id: TASK-004
  description: Render reviewable public security assets and integrate their conditional base composition.
  requirements:
  - REQ-001
  - REQ-007
  - REQ-011
  status: completed
- id: TASK-005
  description: Integrate remote security readiness into bootstrap, audit and maintenance with aligned user guidance.
  requirements:
  - REQ-006
  - REQ-007
  - REQ-008
  - REQ-009
  - REQ-010
  - REQ-011
  status: completed
- id: TASK-006
  description: Integrate required offline validation and update architecture, release notes and regression coverage.
  requirements:
  - REQ-001
  - REQ-010
  - REQ-011
  - REQ-012
  status: completed
- id: TASK-007
  description: Prepare and execute the three bounded supervised Skill scenarios with independent verification.
  requirements:
  - REQ-006
  - REQ-007
  - REQ-008
  - REQ-009
  - REQ-011
  - REQ-012
  status: completed
- id: TASK-008
  description: Review documented usage, translations, preserved controls and contribution trust boundaries.
  requirements:
  - REQ-006
  - REQ-009
  - REQ-010
  - REQ-011
  - REQ-012
  status: completed
- id: TASK-009
  description: Verify the actual Harness configuration with the implemented live verifier and independent readback.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-009
  - REQ-010
  - REQ-013
  status: completed
- id: TASK-010
  description: Complete current acceptance and regression evidence and prepare documentary archival for delivery
    review.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  - REQ-009
  - REQ-010
  - REQ-011
  - REQ-012
  - REQ-013
  status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 50b4b5a3bf0759a420fa5833569295f44b0b76a40f05b8ad14de2036899f84eb
    design: a63f195eedd6c04621fa38c7b8cecb98b0c6d66c8a393005ee474d08299736bf
  approval:
    source: Developer reply in this Codex chat approving Tasks R1 and explicitly authorizing implementation.
    quote: Aprovo as Tasks R1 e autorizo iniciar a implementação.
    revision: 1
    digest: ffff9f3998e5b58a5c43a852a403afa248ba7cdbc34bb851f7f2d8ec3df0f2a6
validation:
  plan_digest: ffff9f3998e5b58a5c43a852a403afa248ba7cdbc34bb851f7f2d8ec3df0f2a6
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-001.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; local offline
        validation/review
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-002.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; local offline
        validation/review
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-003.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; local offline
        validation/review
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-004.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; native sequential
        scenarios and independent replay, bounded interruptions recorded
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-005.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; local offline
        validation/review
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-006.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; trusted process-scoped
        elviszoz administrative GET observations
      observed: true
  - check: CHECK-007
    result: pass
    evidence: docs/validation/public-repository-security/CHECK-007.json
    revision: public-security-corrected-source-2026-11-24/9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_before: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    input_digest_after: 9142f1310d62a46b2dfcd00fae3c1845bb776c12fb05debe00351b0069b2614c
    context:
      execution: local
      environment: macOS; prepared Python validation environment; corrected working source on c191f3b; local offline
        validation/review
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/public-repository-security/README.md
    explanation: Canonical typed policy resolves through core.always for every supported profile/criticality; exact-provider
      fixture checks include its digest, and supervised agents resolve the same index.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/public-repository-security/README.md
    explanation: Policy/schema validation rejects missing, duplicate and unsupported contracts; private-target and
      identity tests cannot assert public readiness, and exact-provider failures stay explicit.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Independent classic and real-wire ruleset mutations check each approval flag; fresh main observations
      require one review, CODEOWNER, stale dismissal and last-push approval.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Independent no-bypass witnesses compose across sources; admin/reviewer bypass and force/deletion
      mutations cannot pass. Live classic protection enforces administrators and blocks both operations.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Custom required contexts survive assessment and staging; absent/disabled/permissive protection
      cannot establish readiness. Independent live comparison preserves structural-validation.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Canonical global and overriding rows retain both designated owners, verified at the main SHA with
      clean syntax and admin permissions; review threshold is one, consistent with GitHub any-owner semantics.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/public-repository-security/README.md
    explanation: Empty/unrelated overrides, syntax errors, wrong base and insufficient/missing owner permission
      evidence fail or remain unverified; none establishes compliance.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Both active branch/tag witnesses include ~ALL without exclusions and only RepositoryRole 5 always
      bypass for all three operations; main remains independently protected.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/public-repository-security/README.md
    explanation: Removed operations, non-admin or unsupported bypass, partial patterns/exclusions and permissive
      fetch-and-merge settings cannot pass the relevant control.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Fresh authenticated repository observations and independent GET comparison confirm both secret
      feature statuses enabled.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/public-repository-security/README.md
    explanation: Each disabled feature is independently detected; omitted feature metadata and unavailable administrative
      responses stay unverified rather than inheriting account defaults.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: The actual GET-only collector records repository identity, pinned main, effective/inherited rule
      details, owners and permissions, secret and participation settings, policy/provider identity and observation
      interval.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/public-repository-security/README.md
    explanation: Controlled transport/CLI tests preserve errors, hidden fields, unsafe/truncated pagination and
      instability without readiness; per-control diagnostics identify known violations and unknowns.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Policy and offline snapshot reports always keep public_ready false; fresh native bootstrap/audit/maintenance
      observations preserve that distinction even when local tests pass.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 4
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/public-repository-security/README.md
    explanation: Transport tests assert explicit scoped GET arguments and sanitized errors; inspection confirms
      no mutation endpoint, secret-alert read or credential export, and CI remains unprivileged.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Real bootstrap Skill resolves the index and stages actual renderer assets over the prepared shared-base
      consumer; its guide requires live verification after authorized configuration, and the case with unavailable
      access withholds readiness.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: The native bootstrap case preserves product/profile material and reports unavailable administrative
      identity, controls and exact installed-provider adoption without inventing authorization.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Real audit Skill executes the version-matched snapshot verifier and reports separately stale-review
      and push-protection failures with severity, evidence and remediation, plus live/provider gaps.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Audit fixture local tests pass while security assessment fails; all original files remain unchanged,
      as independently verified and replayed.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/public-repository-security/README.md
    explanation: Real maintenance Skill compares the exact source contract, stages a reviewable migration and surfaces
      ownership conflicts while preserving stronger required checks and existing content.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Unavailable live remediation remains an explicit gap in maintenance; original provider lock/content
      is unchanged. Actual authorized Harness configuration is freshly verified through separate read-only collection.
  - obligation:
      local:
        requirement: REQ-010
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Current public repository settings permit forks and PR creation for all; restrictions target upstream
      branches/tags, with independent strict main protection. Documentation preserves the contribution route without
      granting upstream write access.
  - obligation:
      local:
        requirement: REQ-010
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/public-repository-security/README.md
    explanation: 'Workflow comparison confirms unchanged pull_request handling, contents: read and persist-credentials:
      false; no privileged fork checkout, administrative secret or write-capable job was introduced.'
  - obligation:
      local:
        requirement: REQ-011
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Renderer is conditional over shared base rather than duplicated profiles; idempotence/conflict
      tests and native cases preserve ownership/custom content and stage differences outside originals.
  - obligation:
      local:
        requirement: REQ-011
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/public-repository-security/README.md
    explanation: Actual command walkthrough matches the technical procedure; all four affected guides have aligned
      EN/PT/ES instructions for mode, provider, permissions, recovery and one eligible owner.
  - obligation:
      local:
        requirement: REQ-011
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-005
    evidence: docs/validation/public-repository-security/README.md
    explanation: VERSION/plugin/marketplace pins are unchanged; exact consumer verification remains enforced, source
      reports disclose dirty development identity, and native maintenance does not rewrite the consumer lock.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/public-repository-security/README.md
    explanation: Independent control mutations include classic/ruleset composition and actual GitHub wire names,
      review flags, bypass, ref coverage, ownership and both secret features.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/public-repository-security/README.md
    explanation: Mock transport tests require no production access; corrected-source native cases retain original
      artifacts, command records and independent copies/replays within bounded attempts. Stale earlier attempts
      remain preserved.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 3
    result: pass
    checks:
    - CHECK-007
    evidence: docs/validation/public-repository-security/README.md
    explanation: Complete required validation passes quality, package, policy, SDD and all validator/execution suites;
      these results remain separate from authenticated live readiness.
  - obligation:
      local:
        requirement: REQ-013
        scenario: 1
    result: pass
    checks:
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Implemented live verifier and independent authenticated GET comparison confirm the actual Harness
      policy, unchanged main/checks and participation, with actual admin read access established.
  - obligation:
      local:
        requirement: REQ-013
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Final report carries repository/provider/policy identity, observation times, pinned SHA and stable
      sample hashes; prior development readbacks are retained separately and never relabeled as final execution.
  - obligation:
      regression:
        impact: 1
        scenario: 0
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/public-repository-security/README.md
    explanation: Classic and independent ruleset controls preserve strict main; per-control bypass, force, deletion
      and review mutations cannot pass, and required contexts remain visible.
  - obligation:
      regression:
        impact: 2
        scenario: 1
    result: pass
    checks:
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Public fork/PR settings are live-enabled; scope stays on upstream branch/tag rules, with unchanged
      contribution guidance and no privileged fork execution.
  - obligation:
      regression:
        impact: 2
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Inaccessible API data and ambiguous permission errors remain unknown; complete live settings are
      confirmed through actual admin access and independent GET comparison.
  - obligation:
      regression:
        impact: 2
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/public-repository-security/README.md
    explanation: Native Skills remain within local preparation/read-only scopes, authorized Harness state is freshly
      observed, and configuration mutations remain outside verifier execution.
  - obligation:
      regression:
        impact: 3
        scenario: 0
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: Fresh actual bootstrap/audit/maintenance cases preserve their separate responsibilities and withhold
      readiness under unavailable evidence, known drift and unresolved conflict.
  - obligation:
      regression:
        impact: 4
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/public-repository-security/README.md
    explanation: One conditional base extension and index-resolved exact provider/lock checks apply across profiles;
      original consumer identity/custom content survives native staging.
  - obligation:
      regression:
        impact: 5
        scenario: 0
    result: pass
    checks:
    - CHECK-003
    - CHECK-007
    evidence: docs/validation/public-repository-security/README.md
    explanation: All existing tests, package/SDD and quality checks remain required; local policy/snapshot success
      stays distinct from fresh authenticated readiness.
  findings:
  - id: FIND-001
    source:
      plan: GitHub ruleset wire-format compatibility
    category: contradicts
    state: resolved
    evidence: docs/validation/public-repository-security/development-observations.md
    description: Initial renderer and all-ruleset evaluator used classic review keys; official API review identified
      distinct ruleset keys and required payload fields.
    tasks:
    - TASK-002
    - TASK-004
    - TASK-010
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-004
    - CHECK-005
    - CHECK-007
    resolution: Explicit API field translation, independent real-wire positive/negative fixtures and payload assertions
      now pass. Earlier results remain preserved; corrected-source checks and native cases have current matching
      input digests.
closure: prepared
---

# Tasks

## Execution baseline and boundaries

Tasks R1 implements the approved Proposal/Requirements R1, Design R1 and ADR-0018 on `codex/public-repository-security`, based on Harness 0.4.0 at `c191f3b126c659fbabfd4ed3d40b474407cfd26a`. All tasks remain pending. Planning validation is not implementation evidence.

The approved Design owns the seven CHECK definitions, all 31 acceptance positions and seven retained regression obligations. These tasks sequence that work without changing requirements, mappings, architectural boundaries, execution limits or release scope. Existing stronger compatible protections and required suites must remain intact.

No Story or issue was supplied. The change ID remains `public-repository-security`; do not invent tracking identifiers. Remote GitHub corrections already performed are dated operational observations, not completed tasks or tests of the future verifier. The subsequent PR #47 investigation confirmed that one eligible owner's approval was sufficient; it adds no all-owners requirement and does not authorize merging that PR.

## Dependencies

| Task | Prerequisites | Completion checks |
| --- | --- | --- |
| TASK-001 | Current Tasks approval and explicit implementation instruction | CHECK-001 policy/schema/resolution assertions |
| TASK-002 | TASK-001 | CHECK-002 |
| TASK-003 | TASK-001, TASK-002 | CHECK-003 |
| TASK-004 | TASK-001 | CHECK-001 composition/rendering assertions |
| TASK-005 | TASK-002, TASK-003, TASK-004 | Local command walkthroughs; CHECK-004 and CHECK-005 at their execution tasks |
| TASK-006 | TASK-001 through TASK-005 | CHECK-001, CHECK-002, CHECK-003, CHECK-007 |
| TASK-007 | TASK-005, TASK-006; current offline suites passing | CHECK-004 plus retained fixture/helper tests |
| TASK-008 | TASK-005, TASK-006, TASK-007 | CHECK-005 |
| TASK-009 | TASK-003, TASK-006, TASK-007, TASK-008; suitable authenticated read access | CHECK-006 |
| TASK-010 | TASK-001 through TASK-009 and current complete evidence | All seven CHECKs, all scenario assessments and selected delivery/archive validation |

The table expresses artifact dependencies, not permission to start implementation or delegate before approval. Independent implementation tasks can be sequenced efficiently; the three supervised cases remain sequential under the approved limits. Required evidence is accepted only against current inputs.

## Implementation tasks

- [x] TASK-001 — Define the canonical public security policy and schemas.

  **Deliverables:** `standards/core/public-repository-security.yaml`, the approved updates to `standards/core/git.md` and `standards/core/security.md`, the `core.always` entry in `standards/index.yaml`, and the three schemas specified by Design. Add the policy/schema/resolution portion of `tests/validators/test_security_contract.py` with synthetic fixtures under `tests/fixtures/security/`.

  **Done when:** the policy contains the single versioned source for the requested owners, minimum approval, main protections, administrator-only reference restrictions, secret controls and public participation. Every profile/criticality resolves it, an invalid/missing/duplicate policy or unsupported version fails, private/out-of-scope handling cannot bypass a declared public target, and exact provider/lock verification remains correct. Document what the schemas establish and what requires live evidence. CHECK-001 assertions run with actual nonzero test counts; rendering assertions are completed in TASK-004.

- [x] TASK-002 — Implement pure policy evaluation and control regressions.

  **Deliverables:** `validators/security/policy.py`, `tests/validators/test_security_policy.py` and maintained synthetic observations covering the supported proof shapes.

  **Done when:** compliant classic-main-plus-rulesets and all-ruleset configurations pass, including independently sufficient no-bypass sources and stronger compatible reviews/checks. Mutations of each requested protection identify the affected failed or unverified control. Coverage includes ambiguous CODEOWNERS layouts, owner permission gaps, hidden bypass lists, disabled/evaluate rules, future/nested refs, missing operations, extra bypass actors, permissive update exceptions, disabled secrets and restricted participation. Either eligible designated owner satisfies the approval minimum; requested-reviewer notifications are not interpreted as an all-owners approval requirement. Unsupported semantics cannot pass. Evaluation has no network or mutation side effects, and CHECK-002 passes.

- [x] TASK-003 — Implement authenticated collection, command modes and result reporting.

  **Deliverables:** `scripts/security/github.py`, `validators/security/validate.py`, `tests/validators/test_security_collection.py`, command/report examples and the security validator README.

  **Done when:** only allowlisted GitHub GET routes execute through bounded argument-array CLI calls. Repository identity, pinned main, classic and inherited rules, CODEOWNERS/errors/permissions, secret controls and participation are observed with completeness and provenance. The second complete collection detects instability. Pagination, time/size limits, permission errors, malformed/omitted data, redirects, endpoint absence and ambiguous 404s follow the approved failure semantics. Explicit `--check-policy`, `--snapshot` and `--live` modes, optional exact consumer verification, safe report output and exit codes work as designed; only complete live compliance sets `public_ready: true`. Tokens, secret values and unsafe error payloads are absent from evidence. CHECK-003 passes, including assertions that no write method or fixture-as-live escape exists.

- [x] TASK-004 — Generate conditional public security assets without destructive composition.

  **Deliverables:** `scripts/bootstrap/public_security.py`, the conditional artifact guide under `project-templates/artifacts/github-public-security/`, the composition guide update and renderer/composition assertions in `test_security_contract.py`.

  **Done when:** rendering from the same policy produces CODEOWNERS, separate main/branches/tags rulesets, the secret-settings payload and a provider/policy/digest manifest in explicit staging. Main has no bypass; reference-management bypass is administrator-only. Identical output is deterministic and conflicting files, symlinks or unsafe destinations cannot be overwritten. Every profile uses the same base extension; private projects do not receive a false public-ready assertion. Existing stronger consumer checks, ownership conflicts and classic protections are surfaced for review instead of replaced. The renderer makes no GitHub calls and CHECK-001 passes in full.

- [x] TASK-005 — Integrate all three Skills and their user-facing workflows.

  **Deliverables:** updates to `skills/project-bootstrap/SKILL.md`, its lifecycle reference, `skills/project-audit/SKILL.md`, `skills/project-maintenance/SKILL.md`, and the maintained bootstrap/audit/maintenance/GitHub-delivery user guides in EN/PT/ES.

  **Done when:** the Skills resolve the canonical policy and invoke the actual version-matched verifier. Bootstrap distinguishes local scaffolding/configuration from live public readiness; audit reports every violation/unknown and remains read-only without remediation authority; maintenance stages differences, preserves stronger protections/content and verifies authorized remediation. All check mode and `public_ready` fields, not just exit 0. Local walkthroughs use the documented actual commands. Guidance explains one eligible owner's approval versus automatic review requests, permissions, incomplete evidence, fork-to-PR participation and exact-version adoption. No normative username/settings list is duplicated in Skills. Behavioral and semantic acceptance remain subject to TASK-007 and TASK-008.

- [x] TASK-006 — Integrate required checks and reconcile living architecture and release notes.

  **Deliverables:** the network-free policy check in `scripts/validate/run.sh`, maintained validation/fixture tests, appropriate validator/template/test guidance, `docs/architecture/overview.md`, the ADR index and an accurate Unreleased entry replacing the planning-only note.

  **Done when:** all new deterministic security suites run through existing test discovery and required CI, alongside existing quality, package, SDD and execution checks. CI retains read-only tokens and nonpersistent checkout credentials; no privileged fork job or administrative token is introduced. Architecture describes implemented responsibilities and links accepted ADR-0018. User-facing release notes distinguish implemented source from unreleased/unaltered consumers. Provider version, marketplace and consumer pins remain unchanged. CHECK-001, CHECK-002, CHECK-003 and CHECK-007 pass with preserved outputs and actual test counts.

- [x] TASK-007 — Exercise the real Skills under supervised synthetic scenarios.

  **Deliverables:** versioned prompts and fixture/verification helpers under `tests/skills/security/`, meaningful automated helper coverage, and per-attempt evidence under `docs/validation/public-repository-security/`.

  **Done when:** helper tests pass and the approved `public-bootstrap-unavailable`, `public-audit-drift` and `public-maintenance-conflict` cases each have one fresh native-agent invocation with the actual revised Skill, sequentially. Enforce the monitored 600-second case and 1800-second suite limits, including independent verification. Preserve prompts, available action observations, original reports/artifacts, input manifests/digests, outcomes and interruptions. Independently replay on separate copies and verify truthful readiness, both injected audit findings, conflict preservation, exact provider boundaries and absence of unauthorized remote writes. No production data, connectors or credentials enter the cases. Do not retry automatically or replace failures with selected successful attempts. CHECK-004 passes only when every expected observation is supported; missing runtime/telemetry remains unverified. Helper changes require current relevant offline suites before scenario execution.

- [x] TASK-008 — Review usable guidance and security boundaries against actual behavior.

  **Deliverables:** the CHECK-005 review record, exercised documented examples, translation comparison and any in-scope corrections with rerun evidence.

  **Done when:** an independent walkthrough of rendering/verification on synthetic consumers agrees with the EN/PT/ES instructions, result/exit semantics and recovery steps. Semantic review finds no policy duplication in Skills, weakened required checks, blind settings replacement, privileged execution of fork code or implicit release/consumer migration. Public contribution, provenance, licensing and confidential reporting boundaries remain usable and unchanged in meaning. Accepted one-owner behavior is clear without requiring removal of other requested reviewers. CHECK-005 passes; corrections invalidate and rerun affected earlier evidence instead of merely refreshing hashes.

- [x] TASK-009 — Run fresh live verification against the public Harness.

  **Deliverables:** actual execution of the Design CHECK-006 command from the reviewed source, minimal sanitized observation records, and an independent authenticated comparison.

  **Done when:** a current complete live assessment confirms both secret features enabled, administrator-only creation/update/deletion coverage for all branches and tags, eligible CODEOWNERS, all required main protections, preserved existing check contexts and public fork/PR settings. Confirm the operator's actual available read permissions before relying on the response; account names, an old administrative session or an empty/404 result do not prove effective access or missing protection. Keep source identity, policy digest, repository identity and observation time with the report. Earlier manual readbacks and the unrelated PR #47 approval are not relabeled as verifier execution. Missing administrative observations leave this task incomplete. New drift remains an explicit finding; any separately authorized correction uses an administrative operation outside the read-only verifier and is followed by a fresh run. No destructive probe, test secret, artificial fork/PR, account switch or permission grant is inferred from this task.

- [x] TASK-010 — Reconcile current evidence and prepare documentary archival.

  **Deliverables:** complete truthful task progress, current seven-check results, all 31 local scenario and seven regression assessments, resolved findings, and the uniquely archived dossier prepared for implementation review.

  **Done when:** all implementation tasks and required checks are complete with actual evidence, current matching before/after input digests and no unresolved material finding. Reuse adequate current executions; rerun affected checks on source/configuration/runtime/external-state changes rather than repeat unaffected tests or relabel stale runs. Selected delivery passes before archival; then move the unique dossier to `specs/archive/public-repository-security/`, set `closure: prepared` truthfully, and pass selected delivery with `--require-archive` plus the applicable final repository checks. Ensure artifact references survive the move. This completes local documentary preparation only; remote PR checks, human review, merge, release and consumer rollout are separate facts.

## Validation and execution prerequisites

Use a prepared Python environment with `requirements-validation.txt`, the actual selected provider and the existing quality comparison base. New checks do not replace existing suites. CHECK-001 through CHECK-003 and CHECK-007 require no production credentials. CHECK-004 requires the native collaboration runtime and observable bounded attempts; it is local supervised evidence, not an automated CI pass.

CHECK-006 requires a trusted session able to read all required administrative fields and owner permissions. The latest diagnostic CLI session observed during the PR #47 question identified `elvisapple` with repository `READ`; classic protection returned 404 and a GraphQL protection listing was empty from that session. Those responses do not prove protection was removed. Treat credential availability as an execution prerequisite and re-establish actual read access at execution time. Do not change GitHub authentication or roles silently. This does not prevent local implementation or make the planning artifacts inconsistent; live acceptance remains pending until accessible evidence exists.

Any new behavior outside the approved policy/evaluator proof shapes, broader deployment, changed CHECK mapping or scenario scope reopens the appropriate SDD gate. Routine in-scope fixes retain original failed attempts and current completion conditions. Semantic acceptance remains separate from schema success.

## Planning review

The developer approved Tasks R1 and explicitly authorized implementation: "Aprovo as Tasks R1 e autorizo iniciar a implementação." The approval binds digest `ffff9f3998e5b58a5c43a852a403afa248ba7cdbc34bb851f7f2d8ec3df0f2a6`. Design R1 and ADR-0018 retain their actual earlier approval. Implementation may proceed within this reviewed plan; publication, merge and release remain separate operations.

## Progress

Documentary closure is prepared in `specs/archive/public-repository-security/`; the unique dossier was moved after selected delivery passed. This is local preparation for review, not evidence of merge or release.

Implementation and current acceptance are complete on the corrected source. All ten tasks are checked; the execution-baseline paragraphs above preserve their historical planning state. The approved Tasks digest is unchanged. The API wire-format finding was fixed within scope, with prior attempts preserved and a separately recorded bounded source-change rerun.

The current seven CHECKs pass, covering all 31 local scenarios and seven regression obligations. CHECK-007 passes 197 validator tests and 48 execution tests (245 total), including 41 security tests. Three actual Skill scenarios have original reports and independent replay; the bootstrap agent was stopped after functional completion to keep review within its bound, as explicitly recorded. Final live and independent administrative readback pass without account switching or remote mutation.

## Validation evidence

See `docs/validation/public-repository-security/README.md`, the seven CHECK JSON records/logs, original scenario archives, replay archives, `live-report.json` and `independent-readback.json`. Source identity is the corrected working-tree snapshot; the commit remains the development base, not a fabricated release. Every final check has matching before/after/current input hashes. Earlier runs and their invalidation are retained under `attempt-01` and in development observations.

Local completion prepares documentary closure and review only. Remote PR checks, human approval, merge, release publication and exact consumer adoption remain separate facts.

## Delivery

No remote submission, merge, release or consumer update is part of this planning turn. After local completion and archive preflight, any authorized PR submission must preserve required review and final remote checks. Required CI observation, review and eventual merge confirmation stay outside pre-merge task completion; later release publication and consumer adoption require their own scoped operations. No task depends on a post-merge write to complete this dossier.
