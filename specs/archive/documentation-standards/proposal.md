---
sdd_version: 3
change: documentation-standards
status: draft
owner: Versat Team
summary: Make feature documentation explain purpose and use, and give consumer teams a consistent way to maintain, publish and review it.
risk: medium
impact:
  state: assessed
  summary: Replace the default consumer guide paths and extend documentation planning across the lifecycle. Preserve existing working guides, bootstrap discovery, documented usage verification and exact release adoption.
  items:
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-001
        scenarios: [1]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: supersede
      targets: [REQ-001]
      reason: Adopt the issue's user documentation path for the default guide.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-001
        scenarios: [2, 3]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001]
      reason: Keep equivalent guides and avoid empty scaffolds.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-002
        scenarios: [3]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: supersede
      targets: [REQ-001]
      reason: Use the new default detailed-guide path and keep links from the quickstart.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-002
        scenarios: [1, 2, 4]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001]
      reason: Retain navigation, proportionality and stable living documentation.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-003
        scenarios: [1, 2, 3]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-002]
      reason: Identify the audience and purpose earlier while retaining updates alongside delivery.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-004
        scenarios: [1, 2, 3, 4]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-002]
      reason: Keep observed verification, including reuse and unverified outcomes.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-006
        scenarios: [1, 2, 3, 4]
        requirements_digest: "e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001, REQ-002, REQ-003]
      reason: Keep the existing dossier, templates, adoption and language and security boundaries.
    - source:
        change: bootstrap-product-context
        requirement: REQ-002
        scenarios: [1, 4]
        requirements_digest: "995b643f7cd2bf40832a4afb1f9e984fec31bd1450b392db9fea3c3af42f8cf3"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001]
      reason: Keep the canonical shared discovery artifact and link supporting material.
    - source:
        change: harness-user-documentation
        requirement: REQ-005
        scenarios: [1, 2, 3]
        requirements_digest: "d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773"
      current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-003]
      reason: Apply the established Markdown localization pattern to consumer guides.
    - current_contract:
        change: documentation-standards
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-001, REQ-004, REQ-005]
      reason: Define the applicable consumer layout, publication process and PR reporting evaluation while keeping existing ownership and review boundaries.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: "Developer approval in this Codex conversation after the Portuguese reading translation of Issue #23 revision 1"
    quote: "Aprovo a proposta e os requisitos da revisão 1 da issue #23. Pode avançar para o desenho técnico."
    revision: 1
    digest: "2fef179090a22f6c31db50ccf4fd99d7638fc559d5c176ecbb455b4f2493e2a4"
---

# Proposal

## Context and problem

[GitHub Issue #23](https://github.com/versat-labs/versat-ai-harness/issues/23) describes legacy documentation that explains steps without explaining why a feature exists or when to use it. Developers need to capture those decisions while planning. Users need to find the answer and complete a representative workflow independently.

## Expected outcome and scope

Define the applicable consumer documentation layout in the canonical Documentation Standard. Guide developers through planning, writing and verifying user and technical material in the existing SDD stages. Apply the existing language policy to user guides and define an owned publication process for product documentation and feature marketing pages. Evaluate whether a GitHub Actions report can help reviewers identify which rules are met and what needs attention.

Use Harness source version 0.4.0 and resolve policy through the Standards index. Keep the existing SDD gates, template composition and exact release adoption. A new consumer path is an adoption default. Existing equivalent documents can remain at working paths as described in the requirements.

## Out of scope

Product-by-product backfill, publication or deployment operations, selection of a mandatory hosting platform, and automatic consumer migrations. [Issue #26](https://github.com/versat-labs/versat-ai-harness/issues/26) tracks the broader translation workflow and CI across product interfaces and user documentation. This change applies the existing language policy to its own documentation scope.

## Work tracking

GitHub Issue #23 is the work reference. No Shortcut Story was provided. Branch: `codex/23-documentation-standards`.

## Current contract baseline

- [Documentation Standard](../../../standards/core/documentation.md) requires repository orientation, current architecture, ADRs, synchronized living specifications and verification of changed usage. It defaults new first-use and detailed guides to `docs/quickstart.md` and `docs/guides/`, allows equivalent existing locations and omits placeholder guides.
- [Bootstrap and composition](../../../project-templates/README.md) put product discovery at `specs/product/overview.md` through the shared base. The provider already uses `docs/product/overview.md` and `docs/user-docs/` for reader material and `docs/decisions/` for its ADRs. The proposed consumer default for new ADRs is `docs/architecture/decisions/`. Design must account for existing ADR links and validator lookup.
- The [Language Standard](../../../standards/core/language.md) requires canonical English and aligned Portuguese and Spanish for community documentation. The provider user guides already use `.pt.md` and `.es.md` siblings.
- The [SDD process](../../../sdd/process.md) already ties living documentation and observed checks to delivery. The [provider workflow](../../../.github/workflows/validate.yml) runs package and SDD checks. It does not report consumer documentation compliance. The existing [Licensing and Publication Standard](../../../standards/core/licensing-publication.md) governs permitted exposure but does not give product teams a process for publishing these two surfaces.

## Impact and risks

The consumer layout changes expectations for new docs. Keeping equivalent legacy paths and testing navigation limits churn. Publication guidance must account for who can see the material and who approves its use. Automated checks can verify facts such as file presence. Reviewers still assess whether the explanation is useful, accurate and semantically aligned across languages. Design will present the PR reporting recommendation and its implications before implementation is planned.

## Planning review

The developer approved revision 1 in the Codex conversation and requested the Design stage.
