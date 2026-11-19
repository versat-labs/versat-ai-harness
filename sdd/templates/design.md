---
sdd_version: 3
change: change-id
requirements: [REQ-001]
adrs: []
validation:
  - id: CHECK-001
    description: Observable verification with a reproducible method
    requirements: [REQ-001]
    required: true
    method:
      kind: automated
      procedure: Replace with the maintained check entry point, steps and expected observations.
    inputs:
      include: [REPLACE_WITH_REVIEWED_INPUT_ROOT]
      exclude: []
    outputs: [docs/validation/change-id]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
regression: []
review:
  revision: 1
  state: draft
  blockers: []
  upstream:
    proposal: REPLACE_WITH_APPROVED_PROPOSAL_DIGEST
  approval: null
---

# Design

## Current state

## Proposed design

## Boundaries and contracts

## Data, security and permissions

## Operations and observability

## Migration, rollout and rollback

## Alternatives considered

## Validation plan

Identify affected examples, applicable language variants and publication readiness. Map the observed usage check to the documented result.

Describe how each CHECK verifies its mapped acceptance and retained regression scenarios. Include all acceptance array positions; justify approved exclusions with reason. Map preserve/extend impact items in regression. Reuse maintained tests and retain profile-required CI suites. Replace input placeholders with reviewed source/test/fixture/configuration roots; explicitly exclude outputs nested under broad roots. Manual/review methods need a reason and reproducible observations. Replace the upstream placeholder with the current approved Proposal/Requirements digest before saving the draft.

## Planning review

Record the actual human review of this revision. Keep design decisions in the sections above.
