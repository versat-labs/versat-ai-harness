---
sdd_version: 3
change: english-issue-definitions
tasks:
  - id: TASK-001
    description: Update the canonical issue language rule and align the root agent instructions.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: pending
  - id: TASK-002
    description: Update the issue-filing step in the English, Portuguese and Spanish contribution guides.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: pending
  - id: TASK-003
    description: Record the policy decision in the ADR history and the Unreleased changelog.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: pending
  - id: TASK-004
    description: Assess issue and comment examples against the maintained guidance and run the full Harness suite.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: pending
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 047103f7a943df216c9c21f3bede9e777bf9c6ea6f12ea45ccfc29abf4e68f49
    design: c9d296096f4e0f0be614f03961b699acbead21b1a6a0db1adba832b1e114ce65
  approval:
    source: Developer reply in the Codex chat after presentation of Tasks revision 1 for GitHub issue 50.
    quote: "Aprovo a revisão 1 do plano de tarefas da issue #50 e autorizo a implementação conforme o Design aprovado."
    revision: 1
    digest: c08c4f84838ec031616ce4c7d3fe3787dd3b3c7b9fb970719b2e4d321a332168
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks for English issue definitions

- [ ] TASK-001 — Revise the [Language Standard](../../../standards/core/language.md) and [root agent instructions](../../../AGENTS.md). Both must distinguish English issue titles and authored descriptions from team discussion comments, where Spanish is optional. The standard must cover form responses, verbatim diagnostics, and updating the English description when a discussion changes scope or acceptance criteria. Verify prospective application to new and substantively revised issues and the separate Spanish rule for internal pull requests.
- [ ] TASK-002 — Edit the issue-filing step in the [English](../../../docs/user-docs/guides/contributing.md), [Portuguese](../../../docs/user-docs/guides/contributing.pt.md) and [Spanish](../../../docs/user-docs/guides/contributing.es.md) guides. In each language a contributor must be able to identify which fields to write in English, where Spanish discussion is welcome, and where to record a changed decision. Confirm that each edition links to the canonical rule.
- [ ] TASK-003 — Integrate [ADR-0019](../../../docs/decisions/0019-github-issue-language.md) into the [decision index](../../../docs/decisions/README.md) and record the issue-specific refinement in [ADR-0010](../../../docs/decisions/0010-refine-language-policy.md). Verify that the references resolve in both directions, the historical decision text is preserved and the [Unreleased changelog](../../../CHANGELOG.md) describes the new convention.
- [ ] TASK-004 — Perform both checks specified in the [Design](design.md). For CHECK-001, follow the walkthrough against the edited files and cite the passages supporting each outcome. For CHECK-002, run the full repository suite against the comparison revision and retain the exit status and test counts. Record the observed environment, input snapshots and evidence for both checks. Assess all seven acceptance scenarios and both regression obligations. Completion requires passing checks, current evidence and resolution of any open findings.

## Dependencies and known risk

TASK-001 establishes the wording used by TASK-002 and TASK-003. Those two tasks can proceed independently once the rule is in place. TASK-004 runs after all three edits so its evidence covers the final wording, links and decision history.

During Design review the full suite reported one pre-existing marketplace failure: the test expected five packaged skills and found six. If it recurs, record CHECK-002 as failed and keep delivery pending until a passing rerun. The implementation scope of this issue covers language policy and its documentation.

## Planning review

The developer approved Tasks revision 1 and authorized its implementation.
