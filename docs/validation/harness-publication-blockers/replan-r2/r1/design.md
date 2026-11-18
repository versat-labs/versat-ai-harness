---
sdd_version: 3
change: harness-publication-blockers
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
adrs:
- ADR-0011
- ADR-0016
validation:
- id: CHECK-001
  description: Restricted evidence identity, access, ownership and current baseline
  requirements:
  - REQ-001
  - REQ-004
  - REQ-007
  - REQ-009
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-001 below: verify the existing restricted system and current reviewer access, compare
      the two HPR-PRIVATE-01 hashes, reconcile exact candidate/source identities and all blocker fields, and test
      changed/missing evidence decisions. Expect accessible attributable review and explicit failures, never clearance
      from an opaque ID.'
    reason: Rights and restricted access require actual authorized review; local hash equality is only an integrity
      aid.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-002
  description: Complete exposure review and attributable confidentiality resolution
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-009
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-002 below: reconcile all 16 predecessor categories and new exposure, review inaccessible
      package/cache/external payloads through scoped reads, classify historical findings, and verify every approved
      treatment against exact affected surfaces. Exercise incomplete pagination, inaccessible payload, sensitive-history
      and drift cases. Pass only after all pre-publication exposure blockers close with evidence.'
    reason: Actual remote content, sensitivity and permitted treatment cannot be established by a clean scan or repository
      unit test.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-003
  description: Rights delta and unchanged candidate applicability
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-008
  - REQ-009
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-003 below: compare source/distribution delta, actual grants and notices, all 16 approved
      candidate texts, seven preserved dependency texts and nine patch preimages; check exact patch applicability
      in a disposable private root. Review missing-grant, incompatible-term and changed-text/preimage cases. Expect
      no root adoption and no transferred approval.'
    reason: A reviewer must establish rights and exact text scope; deterministic file and patch checks complement
      that review.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-004
  description: Effective private-repository controls and contribution trust boundaries
  requirements:
  - REQ-005
  - REQ-007
  - REQ-008
  required: true
  method:
    kind: manual
    procedure: 'Follow CHECK-004 below: obtain the unavailable private-repository capability through owner-approved
      arrangements, configure only the reviewed authorized correction, inspect actual protection/readbacks and run
      a bounded synthetic PR enforcement test without merging. Missing review/check must block; eligible review plus
      actual passing check may become mergeable. Recheck bypass, force-push and fork token/secret boundaries. HTTP
      403 or an unenforced rule is unverified, not pass.'
    reason: Local CI tests cannot establish remote enforcement. Service changes and test PRs require their own scoped
      authorization.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-005
  description: Reporting prerequisites and explicit public-audience follow-up
  requirements:
  - REQ-006
  - REQ-007
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-005 below: verify current platform visibility constraints, destination/owner/recipient/reporting-actor
      contract, safe fallback and separately authorized private prerequisites where feasible. Review missing access/receipt
      and wrong-repository cases. Bind public PVR activation, intended-reporter receipt and unauthorized-viewer exclusion
      to later authorized visibility; do not execute or claim those public tests now.'
    reason: Public PVR is visibility-dependent; review the executable follow-up and actual available prerequisites
      rather than fabricate a public observation.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-006
  description: Exact private candidate, documented use, failures and recovery
  requirements:
  - REQ-004
  - REQ-007
  - REQ-008
  - REQ-009
  required: true
  method:
    kind: manual
    procedure: 'Follow CHECK-006 below: validate the unchanged preparation root and exact patched private candidate;
      exercise installation/resource resolution and the six existing bounded client cases on the selected runtime,
      with exact old/new synthetic provider pairs. Independently inspect first-use Gate 1, missing provider/resource/ref,
      migration and failed-update recovery artifacts. Preserve every attempt and the real workspace installation.'
    reason: Package parsing alone cannot establish client loading, first-use behavior or recovery; reuse the existing
      bounded client protocol with fresh evidence.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-007
  description: Safe multilingual guidance, independent boundaries and immutable history
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-008
  - REQ-009
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-007 below: compare frozen predecessor/candidate files with the merged baseline, review
      changed English/Portuguese/Spanish meaning and actual documented steps, check local links/anchors and public-safe
      content, and confirm unchanged product/organization boundaries. Private evidence, altered historical approval
      or unsupported availability claims fail.'
    reason: Semantic translation, audience safety and preserved historical meaning require review in addition to mechanical
      comparisons.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-008
  description: Blocker closure decision and non-circular operational handoff
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  - REQ-009
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-008 below: reconcile every blocker with verified exit evidence, cross-check required
      checks and actual reviewer decisions, and walk through exact later adoption/visibility/release/external-use/reporting/control
      steps with drift and containment branches. Inject an open pre-publication blocker and expect deferred/incomplete;
      genuine public-only observations remain explicitly unverified follow-up.'
    reason: A human decision over rights, sensitivity and external prerequisites cannot be reduced to a document-presence
      check.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-009
  description: Complete maintained package and regression suites
  requirements:
  - REQ-008
  - REQ-009
  required: true
  method:
    kind: automated
    procedure: Run PYTHONDONTWRITEBYTECODE=1 PYTHON=/private/tmp/versat-pr36-validation-venv/bin/python ./scripts/validate/run.sh
      from both preparation and exact disposable candidate roots using the verified pinned environment; preserve stdout/stderr,
      exit status and actual nonzero counts for tests/validators and tests/execution. Expect Plugin/SDD pass and all
      required tests pass; no targeted/empty/skipped-only substitute. Use the final trusted-baseline archive guard
      only at later authorized delivery.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
- id: CHECK-010
  description: Scenario evidence, authorization and planning-chain integrity
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-008
  - REQ-009
  - REQ-010
  required: true
  method:
    kind: review
    procedure: 'Follow CHECK-010 below: verify unchanged upstream digest and actual approvals/authority, all 31 local
      and 40 retained mappings, historical sources, actual check inputs/outputs and individual assessments. Missing
      required evidence or unknown remote state remains unverified; a synthetic blocked case is not closure of a real
      blocker. Run selected SDD diagnostics for the actual phase; no Tasks/implementation ledger is created during
      Design.'
    reason: Mechanical consistency does not authenticate approvals, actual operation authority or semantic scenario
      coverage.
  inputs:
    include:
    - AGENTS.md
    - README.md
    - README.pt.md
    - README.es.md
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - standards
    - skills
    - agents
    - sdd
    - schemas
    - project-templates
    - validators
    - scripts
    - tests
    - .github
    - docs
    - specs
    - requirements-validation.txt
    - CHANGELOG.md
    exclude:
    - docs/validation/harness-publication-blockers
  outputs:
  - docs/validation/harness-publication-blockers
  execution: local
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-001
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
  - CHECK-010
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-007
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-008
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-010
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-008
- scenario:
    requirement: REQ-003
    scenario: 4
  applicability: required
  checks:
  - CHECK-002
  - CHECK-008
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
  - CHECK-008
- scenario:
    requirement: REQ-006
    scenario: 1
  applicability: required
  checks:
  - CHECK-005
- scenario:
    requirement: REQ-006
    scenario: 2
  applicability: required
  checks:
  - CHECK-005
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks:
  - CHECK-005
  - CHECK-008
- scenario:
    requirement: REQ-007
    scenario: 1
  applicability: required
  checks:
  - CHECK-008
- scenario:
    requirement: REQ-007
    scenario: 2
  applicability: required
  checks:
  - CHECK-004
  - CHECK-005
  - CHECK-008
- scenario:
    requirement: REQ-007
    scenario: 3
  applicability: required
  checks:
  - CHECK-008
- scenario:
    requirement: REQ-008
    scenario: 1
  applicability: required
  checks:
  - CHECK-006
  - CHECK-009
- scenario:
    requirement: REQ-008
    scenario: 2
  applicability: required
  checks:
  - CHECK-007
- scenario:
    requirement: REQ-008
    scenario: 3
  applicability: required
  checks:
  - CHECK-007
  - CHECK-010
- scenario:
    requirement: REQ-009
    scenario: 1
  applicability: required
  checks:
  - CHECK-007
  - CHECK-010
- scenario:
    requirement: REQ-009
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-010
- scenario:
    requirement: REQ-009
    scenario: 3
  applicability: required
  checks:
  - CHECK-009
  - CHECK-010
- scenario:
    requirement: REQ-010
    scenario: 1
  applicability: required
  checks:
  - CHECK-010
- scenario:
    requirement: REQ-010
    scenario: 2
  applicability: required
  checks:
  - CHECK-010
- scenario:
    requirement: REQ-010
    scenario: 3
  applicability: required
  checks:
  - CHECK-010
regression:
- obligation:
    impact: 1
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-007
  rationale: Retain approved wording, third-party scope and actual text-review capacity; new work resolves current
    applicability rather than recreating the delivered candidate. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 1
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-007
  rationale: Retain approved wording, third-party scope and actual text-review capacity; new work resolves current
    applicability rather than recreating the delivered candidate. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 1
    scenario: 3
  checks:
  - CHECK-003
  - CHECK-010
  rationale: Retain approved wording, third-party scope and actual text-review capacity; new work resolves current
    applicability rather than recreating the delivered candidate. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 2
    scenario: 1
  checks:
  - CHECK-001
  - CHECK-003
  rationale: Extend the bounded rights assessment to resolution of remaining and changed evidence for the final candidate.
    Assess the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 2
    scenario: 2
  checks:
  - CHECK-001
  - CHECK-003
  rationale: Extend the bounded rights assessment to resolution of remaining and changed evidence for the final candidate.
    Assess the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 2
    scenario: 3
  checks:
  - CHECK-001
  - CHECK-003
  rationale: Extend the bounded rights assessment to resolution of remaining and changed evidence for the final candidate.
    Assess the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 3
    scenario: 1
  checks:
  - CHECK-002
  rationale: Complete inaccessible-surface and confidentiality disposition work, retaining the full exposure boundary
    and explicit remediation gates. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 3
    scenario: 2
  checks:
  - CHECK-002
  rationale: Complete inaccessible-surface and confidentiality disposition work, retaining the full exposure boundary
    and explicit remediation gates. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 3
    scenario: 3
  checks:
  - CHECK-002
  - CHECK-008
  rationale: Complete inaccessible-surface and confidentiality disposition work, retaining the full exposure boundary
    and explicit remediation gates. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 4
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-006
  rationale: Retain canonical package identity, exact references, migration and recovery; no new release or root adoption
    is selected here. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 4
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-006
  rationale: Retain canonical package identity, exact references, migration and recovery; no new release or root adoption
    is selected here. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 4
    scenario: 3
  checks:
  - CHECK-006
  rationale: Retain canonical package identity, exact references, migration and recovery; no new release or root adoption
    is selected here. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 5
    scenario: 1
  checks:
  - CHECK-006
  rationale: Retain observed private rehearsal scope, failure/update behavior and separately mandatory public verification;
    historical scenarios are not reenacted as new public successes. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 5
    scenario: 2
  checks:
  - CHECK-006
  rationale: Retain observed private rehearsal scope, failure/update behavior and separately mandatory public verification;
    historical scenarios are not reenacted as new public successes. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 5
    scenario: 3
  checks:
  - CHECK-006
  rationale: Retain observed private rehearsal scope, failure/update behavior and separately mandatory public verification;
    historical scenarios are not reenacted as new public successes. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 5
    scenario: 4
  checks:
  - CHECK-008
  rationale: Retain observed private rehearsal scope, failure/update behavior and separately mandatory public verification;
    historical scenarios are not reenacted as new public successes. Assess the retained outcome against current inputs;
    preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 6
    scenario: 1
  checks:
  - CHECK-004
  - CHECK-007
  rationale: Resolve effective control gaps while retaining self-contained contributions, provenance and operation-specific
    authorization. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 6
    scenario: 2
  checks:
  - CHECK-004
  rationale: Resolve effective control gaps while retaining self-contained contributions, provenance and operation-specific
    authorization. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 6
    scenario: 3
  checks:
  - CHECK-004
  - CHECK-010
  rationale: Resolve effective control gaps while retaining self-contained contributions, provenance and operation-specific
    authorization. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 7
    scenario: 1
  checks:
  - CHECK-005
  - CHECK-007
  rationale: Resolve route prerequisites and bind genuinely visibility-dependent checks to later operations without
    widening prior pilot evidence. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 7
    scenario: 2
  checks:
  - CHECK-005
  rationale: Resolve route prerequisites and bind genuinely visibility-dependent checks to later operations without
    widening prior pilot evidence. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 7
    scenario: 3
  checks:
  - CHECK-005
  - CHECK-008
  rationale: Resolve route prerequisites and bind genuinely visibility-dependent checks to later operations without
    widening prior pilot evidence. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 8
    scenario: 1
  checks:
  - CHECK-007
  rationale: Retain safe multilingual maintained guides and actual usage verification if changes affect them. Assess
    the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 8
    scenario: 2
  checks:
  - CHECK-007
  rationale: Retain safe multilingual maintained guides and actual usage verification if changes affect them. Assess
    the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 8
    scenario: 3
  checks:
  - CHECK-007
  rationale: Retain safe multilingual maintained guides and actual usage verification if changes affect them. Assess
    the retained outcome against current inputs; preserve historical execution as provenance rather than replaying
    its approval event.
- obligation:
    impact: 9
    scenario: 1
  checks:
  - CHECK-001
  - CHECK-008
  rationale: Advance from a completed defer assessment to resolving pre-publication blockers; old preparation remains
    valid history, not clearance. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 9
    scenario: 2
  checks:
  - CHECK-008
  rationale: Advance from a completed defer assessment to resolving pre-publication blockers; old preparation remains
    valid history, not clearance. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 9
    scenario: 3
  checks:
  - CHECK-008
  rationale: Advance from a completed defer assessment to resolving pre-publication blockers; old preparation remains
    valid history, not clearance. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 9
    scenario: 4
  checks:
  - CHECK-008
  rationale: Advance from a completed defer assessment to resolving pre-publication blockers; old preparation remains
    valid history, not clearance. Assess the retained outcome against current inputs; preserve historical execution
    as provenance rather than replaying its approval event.
- obligation:
    impact: 10
    scenario: 1
  checks:
  - CHECK-007
  - CHECK-010
  rationale: Obtain an attributable confidentiality treatment while preserving delivered approvals and restricted
    evidence; destructive remedies remain outside the approved scope. Assess the retained outcome against current
    inputs; preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 10
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-007
  rationale: Obtain an attributable confidentiality treatment while preserving delivered approvals and restricted
    evidence; destructive remedies remain outside the approved scope. Assess the retained outcome against current
    inputs; preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 10
    scenario: 3
  checks:
  - CHECK-002
  - CHECK-007
  rationale: Obtain an attributable confidentiality treatment while preserving delivered approvals and restricted
    evidence; destructive remedies remain outside the approved scope. Assess the retained outcome against current
    inputs; preserve historical execution as provenance rather than replaying its approval event.
- obligation:
    impact: 11
    scenario: 1
  checks:
  - CHECK-007
  rationale: Retain independent product and organization boundaries and required enforcement suites. Assess the retained
    outcome against current inputs; preserve historical execution as provenance rather than replaying its approval
    event.
- obligation:
    impact: 11
    scenario: 2
  checks:
  - CHECK-007
  rationale: Retain independent product and organization boundaries and required enforcement suites. Assess the retained
    outcome against current inputs; preserve historical execution as provenance rather than replaying its approval
    event.
- obligation:
    impact: 11
    scenario: 3
  checks:
  - CHECK-007
  - CHECK-009
  rationale: Retain independent product and organization boundaries and required enforcement suites. Assess the retained
    outcome against current inputs; preserve historical execution as provenance rather than replaying its approval
    event.
- obligation:
    impact: 12
    scenario: 1
  checks:
  - CHECK-010
  rationale: Apply the same three gates and exact authorization boundaries to the new change without transferring
    predecessor approvals. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 12
    scenario: 2
  checks:
  - CHECK-010
  rationale: Apply the same three gates and exact authorization boundaries to the new change without transferring
    predecessor approvals. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 12
    scenario: 3
  checks:
  - CHECK-010
  rationale: Apply the same three gates and exact authorization boundaries to the new change without transferring
    predecessor approvals. Assess the retained outcome against current inputs; preserve historical execution as provenance
    rather than replaying its approval event.
- obligation:
    impact: 13
    scenario: 0
  checks:
  - CHECK-008
  rationale: Retain the effective operational boundary and complete validation entry point; no change to these sources
    is authorized at Gate 1. Assess the retained outcome against current inputs; preserve historical execution as
    provenance rather than replaying its approval event.
- obligation:
    impact: 14
    scenario: 0
  checks:
  - CHECK-009
  rationale: Retain the effective operational boundary and complete validation entry point; no change to these sources
    is authorized at Gate 1. Assess the retained outcome against current inputs; preserve historical execution as
    provenance rather than replaying its approval event.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: d3552c1655c58d08d56c9c0178c75c50e804c171087b6d62a2f8be1e6147e5eb
  approval:
    source: User reply in this chat on 2026-11-14 explicitly approving Design R1 and authorizing Tasks preparation
      only
    quote: Sim, aprovo o Design R1 de harness-publication-blockers. Prepare somente as Tasks, sem iniciar a implementação
      ou publicar.
    revision: 1
    digest: 67d7645746e0cd955cffc3e0a110a708b8bb99e25859bead72fcc2400fb93ea7
---

# Design

## Current state

Proposal/Requirements R1 was explicitly approved on 2026-11-14, with Design-only authority and combined digest `d3552c1655c58d08d56c9c0178c75c50e804c171087b6d62a2f8be1e6147e5eb`. No substantive upstream text changed. The source is `4a56181d3597c5d345a7639f013547e1700420cb`, branch `codex/harness-publication-blockers`. The Proposal's five provider anchors match; declared source version remains 0.3.0 with SDD v3. Use this exact checkout, not the installed release provider.

The delivered `harness-publication-readiness` candidate is retained. Its private preparation passed while publication remained deferred. New observations in this Design are bounded metadata/integrity reads; they are neither acceptance execution nor a new sensitive-payload collection:

- The existing restricted repository was observed private; the accountable owner has admin access. Local copies of the assessment and integrity manifest match both hashes bound by HPR-PRIVATE-01. This proves local readability and identity, not remote durability of those exact files or substantive reviewer acceptance. No raw contents were copied into Harness.
- The actual `main` branch reports `protected: false`, at the baseline commit. Both protection and ruleset reads return HTTP 403 with a plan-capability limitation. This is a real execution prerequisite, not an empty ruleset or a passed control. No settings changed.
- The merged commit's observed check run is `structural-validation`, application `github-actions`, completed/success. This identifies the intended required check; it does not establish enforcement or this successor's CI result.
- Local runtime remains Codex desktop 26.915.31945/build 9922, macOS 26.5.2 arm64; validation environment is Python 3.11.4, PyYAML 6.0.2 and jsonschema 4.23.0. Compatibility beyond that target is not claimed.

GitHub documents private-repository branch protection on supported paid plans and PVR for public repositories. These dated capability facts distinguish the private control prerequisite from the genuinely public-only reporting test: [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [repository security advisories/PVR](https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories), consulted 2026-11-14. No plan purchase, billing action or public conversion is selected as an automatic operation.

## Proposed design

### Resolution workflow and exact exit

Use an evidence-led review workflow, not a new runtime service or general scanner. Reuse canonical Standards, existing validators, guides, candidate patch and client fixtures. The accountable owner coordinates actual technical, rights and security reviewers in their recorded capacities. Preserve CODEOWNERS assignments; do not invent independent specialist review or silently assign a new legal reviewer.

The workflow is: freeze a current review boundary; open attributable blocker records; obtain missing evidence within authorized scope; review and verify permitted treatment; re-freeze changed inputs; run acceptance checks; reconcile the pre-publication decision. `defer` remains the outcome if any required pre-publication blocker is open. Completing a review memo cannot satisfy a failed resolution requirement.

| Workstream | Required exit evidence | Failure disposition |
|---|---|---|
| Evidence access and identity | Authorized reviewers can inspect the exact restricted revision; source/candidate and old/new observation boundaries are explicit. | Missing access or unverifiable original remains open. |
| Inaccessible surfaces | Complete scoped listings and actual payload review or demonstrated absence, with pagination and limits recorded. | API failure, partial search or cache metadata alone remains unverified. |
| Confidential history | Actual classification and attributable permitted treatment verified over every affected exposure surface. | Destructive/history/destination conflict triggers replanning; no public exposure. |
| Rights and candidate | Current distribution delta, actual grants/notices and review capacity; unchanged text approval and applicable patch preimages. | Missing rights, changed wording or mismatch blocks adoption readiness. |
| Effective private controls | Supported private capability, reviewed correction, actual enforcement and eligible review/check evidence. | Current 403/unprotected state prevents completion; no public-first workaround. |
| Reporting prerequisites | Feasible private prerequisites and safe fallback verified; exact public PVR activation/receipt test assigned to later visibility operation. | Feasible private gaps remain open; public outcomes remain unverified. |

Ready for separately authorized operations is allowed only when those private prerequisites are met and the mandatory public follow-up is executable. It is not a public availability, license-adoption, release or completed-H03 claim.

### Restricted and safe artifacts

Only this Design is created now. The following are proposed implementation outputs, not existing capabilities:

| Location | Contract |
|---|---|
| Existing restricted evidence system, new `docs/validation/harness-publication-blockers/` area | New immutable runs with restricted blocker register, payload references, classification/treatment decisions, access records and actual operation evidence. Reuse ADR-0016's system; no new service or sharing expansion. Preserve the prior HPR-PRIVATE-01 area untouched. |
| `docs/handoffs/harness-publication-blockers/review-inputs.json` in Harness | Minimal scrubbed immutable input manifest: opaque restricted record/revision and content digest, source/candidate identities, observed category states, actual reviewers/capacities and external observation times. No raw URLs, internal addresses, private payloads, secrets or self-hash. |
| `docs/handoffs/harness-publication-blockers/README.md` in Harness | Safe current blocker disposition, prerequisites, exact later operation boundaries, drift checks and mandatory public follow-up. Link from maintained guidance only during authorized implementation. |
| `docs/validation/harness-publication-blockers/<run>/` in Harness | Scrubbed check reports, actual suite outputs, individual scenario assessments and minimal provenance. Failed runs remain; no old report is overwritten. |
| Existing EN/PT/ES guides, only if outcome changes their claims | Update actual status and usage together; keep canonical detailed guidance and safe fallback. No bulk documentation rewrite. |

The restricted blocker record has stable ID, category, exact exposure/source, evidence revision and access, observed/absent/unverified state, sensitivity classification, owner, actual reviewer/capacity, proposed treatment and authority, precondition/exit test, result, date and superseded-observation reference. Closure requires verified evidence, not merely `status: closed`. The safe manifest exposes only what is necessary to bind checks to that restricted revision. It does not publish individual sensitive findings or private strategy links.

The already selected system and hashes resolve the Design's storage choice. Before implementation relies on them, verify current reviewer access to the exact records and durable restricted preservation; local readability and repository admin permission alone do not prove either. Access failure stops dependent work without choosing another destination silently. No sensitive evidence collection or repository write in that system is performed in this phase.

### Surface and history treatment

Reuse the predecessor's 16-category inventory and extend it to the current proposed tree, new records and remote delta. Partition queries by exact repository/object/ref and retain pagination/completeness evidence. Review all previously inaccessible package types, cache payloads, alternate attachment bodies and external integration payloads through scoped authorized reads or an authorized custodian's inspectable record. Do not request blanket permissions or download unrelated histories. A feature flag or empty listing proves only its observed scope.

Classify internal-reference indicators semantically: a benign reference can close only with accountable review; an actually confidential record cannot be waived into a public tree. Document a feasible non-destructive treatment and verify all affected copies/surfaces. Preserve originals and their review/approval provenance in the restricted system. Moving a file in the current tree does not clear past blobs, forks, comments or artifacts.

This Design selects no destructive rewrite, deletion of historical evidence, new repository/mirror, modified licensing model or confidentiality waiver. If actual classification requires such a remedy, record the concrete conflict and reopen Gate 1 or Design as applicable, with a successor ADR where the architectural boundary changes. The current ADR-0016 already requires that stop. No speculative new ADR is needed merely to apply its existing boundary.

### Effective controls before exposure

Selected approach: obtain and verify effective protection while Harness remains private. The owner must arrange supported private-repository capability before control correction; this Design authorizes neither spending nor subscription changes. Lack of that capability blocks CHECK-004 and successor completion. Publishing to unlock protection is rejected because it exposes uncleared history and bypasses the approved prerequisite. A different timing/compensating-control approach requires explicit replanning, not an agent fallback.

After separate scoped operational authorization, use the smallest supported protection mechanism for `main`; retain existing rules if they satisfy the same verified contract. Proposed target: PR-based integration, at least one eligible non-author approval, applicable CODEOWNER review, stale approval dismissal, actual `structural-validation` required from the observed GitHub Actions source, no ordinary admin/role bypass, force pushes disabled and branch deletion disabled. Keep existing read-only workflow tokens; no secret forwarding to untrusted fork code and no privileged `pull_request_target` execution of contributor content. Do not add signing, release automation or unrelated branch policy.

Review actor eligibility before enabling controls: the existing owners are not interchangeable with independent approvers, and sole-owner/self-authored changes may otherwise deadlock. Use a valid existing reviewer/author arrangement; do not silently change CODEOWNERS or grant blanket bypass. If unavailable, stop for a concrete reviewed correction.

Read configuration back from the service. Under separate authorization, use one disposable non-sensitive branch/PR targeting main, with a reversible invalid manifest to produce the actual failing required CI check; observe blocked mergeability with missing check/review, then correct the manifest and obtain an eligible real review to observe the permitted state. Do not merge. Configuration readbacks, actor permissions and service mergeability must agree. Do not attempt a force push, deletion or unauthorized merge against main to prove denial. A mirror rule on a disposable branch is supporting evidence only, not proof of main enforcement. Test-branch/PR cleanup is separately scoped; preserve evidence. Public fork behavior is rechecked after visibility in the later operational follow-up.

### Reporting and audience split

Retain the intended repository-native GitHub PVR destination and existing accountable maintainer/recipient arrangement. Pre-publication work verifies that the service capability still has the documented public-only boundary, confirms accountable triage, permitted recipient and intended reporter roles, safe fallback and exact activation/notification procedure. Do not invent a new mailbox or transfer the earlier organization's pilot result.

If an already authorized private route test is needed for a feasible private prerequisite, present the exact audience/destination/marker first; observe actual private receipt and exclusion without real vulnerability data. Approval of this Design does not send such a message. For native public PVR, actual activation, intended external reporter submission/receipt and unauthorized-viewer exclusion are mandatory post-visibility observations; there is no misleading private PVR pass. The later operator must separately authorize configuration and non-sensitive submission, record the actual report identifier, keep it private and avoid advisory publication/CVE requests. Missing/failed verification withdraws availability claims and keeps the safe maintainer-instructions fallback.

## Boundaries and contracts

Apply the Proposal's resolved Standards and [architecture](../../../docs/architecture/overview.md). [ADR-0011](../../../docs/decisions/0011-root-portable-plugin-package.md) and [ADR-0016](../../../docs/decisions/0016-public-harness-preparation-boundary.md) remain unchanged and govern this design; no new architectural responsibility or public surface is selected. Skills, Standards, SDD and validators keep their respective roles. No schema/exemption/test weakening is proposed.

Preserve all predecessor dossiers, frozen approvals, candidate terms and historical evidence byte-for-byte. Current status changes belong to the new handoff; they do not rewrite the predecessor's dated no-merge or deferred observations. Other products and organization defaults retain independent delivery/licensing/access boundaries. Effective root adoption, visibility, release/tag and real consumer migration remain outside this successor.

## Data, security and permissions

Use minimal inspectable evidence and existing least-privilege access. Freeze restricted originals before producing scrubbed summaries; record actual reviewer access without copying credentials or private links into Harness. Any remote correction/test has an operation envelope: exact target, permitted actor, before-state, proposed delta, bounded test, expected result, rollback/containment, evidence location and actual user authorization. Administrative authority is not authorization to execute.

No new sensitive collection, sharing, reporting channel, invitation, message or permission change occurs during Design. Later broad/raw collection must be narrowed and authorized; inaccessible evidence remains unverified. Preserve failed attempts and avoid automatic retries or success-only selection. No retention duration, legal qualification or incident conclusion is invented. Existing restricted retention/access responsibilities continue.

## Operations and observability

Record per-blocker and per-check status, exact inputs, actual environment/actor, service response category, reviewer/capacity and next accountable action. Distinguish draft/approved, implemented, verified-private, deferred, ready-for-authorized-operations, adopted, public and migrated. The last three states are not outputs of this successor.

Known execution dependencies are private protection capability, any missing scoped payload access and required actual reviewers. Their absence is not a Design scope ambiguity: the selected approach stops and leaves acceptance incomplete until supplied. No purchase or privilege expansion is preapproved. A change in treatment strategy, control timing, reporting destination or evidence system requires renewed planning review.

## Migration, rollout and rollback

Keep root/version/installed workspace at 0.3.0 and the reviewed candidate intent at 0.4.0, preserving marketplace `versat-internal` and Plugin identity. Check tag availability before future adoption; never retag or use latest. Validate the exact nine-file patch/base/preimages and approved text inventory in a disposable private copy of the same root. Refresh rights/inventory for new files rather than changing old approval hashes. A mismatch stops; regeneration requires review of the changed candidate.

Local regression target is the reobserved Codex desktop build and macOS architecture above, using the existing separately namespaced private test installation and synthetic consumer; verify it exists and is usable before rehearsal. Do not replace workspace settings. Missing test context yields unverified, not an improvised installer. Python 3.11.4/pinned dependencies are the local validator target; existing CI retains Python 3.11 Ubuntu and reports its actual image only when run.

Rehearse exact installation/resource resolution, first-use Gate 1, missing provider, missing resources, unavailable version, explicit synthetic migration and failed-update retention/recovery using the predecessor's six-case protocol (installation is setup). Reuse maintained [supervised fixtures and verification](../../../docs/guides/skill-evaluations.md); one fresh native new-intent invocation in later authorized implementation, no automatic retry, at most 600 seconds for that invocation, 300 seconds for each remaining bounded case and 2,400 seconds for the suite. Preserve each outcome; unknown telemetry and shared-permission limitations remain explicit. A material runtime/method change reopens Design. No agent or client rehearsal is launched now.

A later adopted release needs fresh exact-surface review and its own authority, followed by anonymous acquisition/install/update/contribution and public reporting/control checks. Consumers opt into exact provider/lock pairs separately. Rollback here restores an authorized reversible control/documentation change or the last verified private test pair while preserving evidence; it cannot erase existing public copies or grants. Destructive containment or public visibility changes require a separate decision.

## Alternatives considered

- Reuse the predecessor's completed defer assessment as clearance: rejected; it records the gaps this successor must close.
- Publish first to unlock controls/PVR: rejected for protection; public-only PVR verification is a separate later observation, not permission to expose uncleared material.
- Introduce a new private evidence service, public mirror or SDK: unnecessary and outside the approved boundary.
- Delete historical records or accept confidential exposure to finish: rejected; preserve attributable originals and replan a material remedy.
- Treat synthetic failure cases as actual blocker resolution: rejected; synthetic cases verify stop behavior while real closure needs actual review and enforcement.
- Rewrite validators or add a general audit engine: unnecessary; reuse existing mechanical checks and add bounded actual review evidence where automation cannot establish the claim.

## Validation plan

### Common input and evidence contract

All ten checks are required. Frontmatter maps all 31 local scenarios and 40 retained obligations; no exclusion is proposed. Historical stage events are assessed as provenance/invariant preservation, not reenacted as new approvals. Predecessor public-only scenarios are mapped to executable handoff completeness, explicitly not public success.

Declared source roots cover package, policy, guides, tests, current/historical specs and manifests; the current dossier is excluded by the canonical snapshot contract and bound by stage/plan digests. `docs/validation/harness-publication-blockers/` is an explicitly excluded output subtree. The proposed safe review-input manifest under the handoff is included, not excluded. No external private path is supplied to the snapshot tool.

Before a run, complete and review the candidate/status artifacts and freeze the restricted evidence revision plus scrubbed manifest. Do not mutate them while recording a pass. Capture the actual source and (where applicable) patched-root `--input-digest CHECK-NNN` separately before/after each check; a root cannot borrow another root's hash. Subsequent source, safe-manifest or remote-state drift invalidates affected results even if a local digest is unchanged. External observation identities/times and restricted record hashes are compared separately; local hashes do not authenticate services or reviewers.

Generate reports only under a new excluded run directory, with stdout/stderr/exit/counts, environment, actual actions, result and limitations. Record one individual assessment per mapped obligation when Tasks exists; no implementation ledger is populated in Design. Preserve failed/partial attempts. A changed control operation is followed by a refreshed frozen manifest and final verification run, not relabelled earlier evidence. Current final ledger/output paths never form their own input prerequisite.

### CHECK-001 — Evidence and baseline

Confirm private system visibility and actual reviewer access to the exact record, verify the predecessor hashes, and preserve originals. Reconcile source/tree/candidate/patch identities and the complete register fields. Exercise a missing record, changed digest and unconfirmed reviewer capacity using synthetic references; each must remain unverified. Actual inaccessible evidence blocks resolution. Manual review is necessary because platform permission and hash checks cannot prove substantive rights/security review.

### CHECK-002 — Surface and treatment

Use the exact scoped inventory and pagination contract above; retain endpoint success/failure and content review privately. Review every category, including new planning files, old blobs and external payloads. For each real history finding verify classification, authority, original preservation, treatment and reinspection. Walk incomplete-listing, inaccessible cache, sensitive old-blob and newly-added-ref cases and require stop/invalidation. The real exposure verdict passes only with all required findings resolved; a correct synthetic defer response cannot pass an unresolved real category. A material remedy stops for replanning.

### CHECK-003 — Rights and candidate

Compare the merged source and proposed distribution delta, actual rights evidence, notices, all 16 approved text files and seven dependency texts. Recompute candidate/patch identities; compare each of nine preimages and run `git apply --check` in a disposable copy before any authorized private application. Validate resulting tree/manifests and unchanged original root. Missing grant, incompatible term, changed wording and patch mismatch must block; no approval or effective date is invented. Actual reviewer capacity and inspectable evidence are required.

### CHECK-004 — Controls

Record the private capability prerequisite and stop while unavailable. After specific authority, inspect/apply/read back the minimal control configuration above and execute the synthetic PR protocol with real check/review transitions. Verify author/reviewer permissions and mergeability without merging or attempting destructive denial tests. Inspect token/secret flow for every workflow used by untrusted contributions. Local `tests/execution/test_ci.py` supports workflow-command behavior but is not enforcement evidence. Public fork/visibility rechecks remain a separate mandatory handoff.

### CHECK-005 — Reporting

Verify the current platform boundary from authoritative documentation and actual available metadata, existing accountable responder/recipient roles and safe fallback. Prepare the exact later public PVR activation and marker-receipt/exclusion protocol with authority requirements and containment. Review wrong-repository, unavailable route, missing receipt and changed audience cases; none can reuse the old pilot as a pass. Execute only feasible separately authorized private prerequisites. Public activation/submission is not required to merge this private resolution work and remains unverified until its later operation.

### CHECK-006 — Private package/client

Use the exact reviewed candidate, observed compatible runtime and synthetic consumers, applying the bounded protocol above. Independently inspect generated first-use artifacts (only Proposal/Requirements, null approval, application/tests unchanged), exact installed resources and explicit old/new provider/lock pairs. Observe errors and retained previous pair for missing provider/resources/ref or failed update. Preserve failures and do not mutate real consumers. Source/candidate checks and client outcomes are separate observations; a private installation never proves anonymous access.

### CHECK-007 — Guides/history/boundaries

Compare the four predecessor dossier files, frozen candidate/approval records and historical evidence against the merged baseline. Check root and maintained EN/PT/ES guidance for equivalent permissions, pending-state wording, fallback and exact version/recovery steps. Check all changed local paths/anchors and execute affected usage steps with CHECK-006 rather than a separate duplicate walkthrough. Review each new public-facing file independently for sensitive payloads/private dependencies. Verify other product terms, organization routes and consumer configurations are unchanged. No tests solely asserting prose wording are needed.

### CHECK-008 — Decision and operational handoff

Require real exit evidence for every pre-publication blocker and actual accountable review. Walk the later sequence: drift/rights/control reconciliation, separate root adoption, separately authorized visibility/release, anonymous use and public PVR/control verification, independent consumer migration. Identify concrete actors, exact inputs, authorization, expected observations and failure containment at each step. Inject open rights/history/control or drift and expect incomplete/defer. Public-only observations must remain pending with a runnable protocol; they cannot conceal a feasible private gap or be marked not-applicable.

### CHECK-009 — Required suites

Run the exact full command in frontmatter against both preparation and patched roots with verified Python dependencies. Retain actual counts and failures; the current baseline contains 131 validator and 48 execution tests. Existing v3 gate/impact/freshness, CI/archive and consumer/recovery tests remain mandatory. No empty or targeted suite replaces them. Later authorized PR delivery additionally uses the trusted baseline and selected `--phase delivery --require-archive`; final remote CI must be separately observed. Local success does not grant PR or merge authority.

### CHECK-010 — Semantic and gate review

Recompute canonical upstream/stage digests, confirm exact actual approvals and permitted actions, and reconcile every local/retained scenario with current source-bound evidence and explanations. Preserve the historical Gate 1 stop while recording its genuine later approval. Treat changed inputs, absent actual review, unavailable operation or unrequested behavior as findings; no not-applicable shortcut. For retained predecessor scenarios about earlier implementation, compare preserved outcome and current behavior, not old test labels alone. Check branch/work-tracking/language conventions and no transferred publication authority.

## Planning review

Design R1 is awaiting approval with approval null and the approved Proposal digest bound above. No unresolved Design alternative is hidden: the selected approach requires effective private protection and stops if the owner cannot provide it; no budget, access expansion or operation is approved here. Other operational evidence remains work for later authorized implementation, not a Design pass or a resolved blocker.

No new ADR is proposed because the design applies ADR-0011/0016 without changing architecture, destination, license direction or evidence boundary. A required material remedy will reopen the appropriate gate before implementation. Only Design and Gate 1 approval bookkeeping are written now. Tasks, implementation, sensitive collection, messages, remote changes and publication remain suspended.

Actual preparation diagnostics on 2026-11-14:

- Selected `validators/sdd/validate.py --root . --change harness-publication-blockers --phase planning --json`, using the verified pinned Python environment: exit 0/pass, no findings or warnings; 31 local scenarios and 40 retained obligations.
- `PYTHONDONTWRITEBYTECODE=1 PYTHON=/private/tmp/versat-pr36-validation-venv/bin/python ./scripts/validate/run.sh`: exit 0; Plugin/SDD pass, 131 validator tests and 48 execution tests pass. Existing historical legacy/v2 inventory warnings remain; no exemption, suite or validator changed.
- Full review of this Design and approval bookkeeping; 19 local Markdown links resolve across the dossier, explicit new-file whitespace checks and `git diff --check` pass. All 1,551 pre-existing tracked files remain byte-identical. Requirements bytes and the combined approved Proposal digest remain unchanged. Coverage contains each of 31 local and 40 retained obligations exactly once, with no exclusions.
- Canonical Design R1 digest: `67d7645746e0cd955cffc3e0a110a708b8bb99e25859bead72fcc2400fb93ea7`. It identifies the presented revision and is not approval.

The bounded metadata reads and local regression tests above are Design preparation only; CHECK-001 through CHECK-010 remain planned implementation checks. No Task file, implementation ledger, changed living guide, new ADR, candidate application, sensitive collection, test message, remote write or publication occurred. Gate 2 remains awaiting the user's approval, which permits Tasks preparation only.

### Gate 2 approval — 2026-11-14

The user explicitly approved the presented Design: “Sim, aprovo o Design R1 de harness-publication-blockers. Prepare somente as Tasks, sem iniciar a implementação ou publicar.” The Design and upstream Proposal digests were reverified unchanged before recording approval. This authorizes Tasks preparation only; implementation and publication remain suspended. Earlier pending statements preserve presentation history. No operational prerequisite is resolved by this approval.
