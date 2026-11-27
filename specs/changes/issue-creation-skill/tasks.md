---
sdd_version: 3
change: issue-creation-skill
tasks:
  - id: TASK-001
    description: Implement the issue form helper with resolve, missing and render commands, plus synthetic form fixtures and its focused unittest suite.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: pending
  - id: TASK-002
    description: Write the Skill procedure in SKILL.md covering context resolution, vulnerability detection, form selection, English drafting, clarification, Origin, preview, creation, Portfolio linking, result reporting and failure conditions.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008]
    status: pending
  - id: TASK-003
    description: Register the Skill in the validation runner and plugin validator, add the focused unittest invocation and the changelog Unreleased entry.
    requirements: [REQ-008]
    status: pending
  - id: TASK-004
    description: Write the issue creation user guide in English with aligned Portuguese and Spanish translations, covering prerequisites, permissions, an example prompt, results, failures and the vulnerability route.
    requirements: [REQ-005, REQ-006, REQ-007, REQ-008]
    status: pending
  - id: TASK-005
    description: Add the supervised evaluation cases, the synthetic repository fixture and the recording GitHub stub for CHECK-003.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007]
    status: pending
  - id: TASK-006
    description: Execute CHECK-001 to CHECK-005, with separate authorization for the live issue in CHECK-004, record results and assess every acceptance and regression obligation.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008]
    status: pending
  - id: TASK-007
    description: Prepare the validated dossier for documentary delivery under specs/archive in the same branch.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008]
    status: pending
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 4348c5831e8ff05e64d2a251aaf949c5039f9f6305a9a2975c2fed6cb790be6f
    design: 72225a72ef8158bb66ef34653ad1f6e226388ac1e6dce5bafbd0b99bb8a7984c
  approval: null
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks

- [ ] TASK-001 — Implement the issue form helper, fixtures and unit tests
- [ ] TASK-002 — Write the Skill procedure in SKILL.md
- [ ] TASK-003 — Register the Skill, add the test invocation and changelog entry
- [ ] TASK-004 — Write the trilingual user guide
- [ ] TASK-005 — Add supervised evaluation cases, fixture and GitHub stub
- [ ] TASK-006 — Execute the checks and assess every obligation
- [ ] TASK-007 — Prepare the dossier for documentary delivery

## Dependencies

- TASK-002 depends on TASK-001 because the procedure calls the helper's commands.
- TASK-003 depends on TASK-001 and TASK-002.
- TASK-004 depends on TASK-002 so the guides describe the final procedure.
- TASK-005 depends on TASK-002.
- TASK-006 depends on TASK-001 to TASK-005.
- TASK-007 depends on TASK-006.

## Completion conditions

- **TASK-001:** `python -m unittest discover -s tests/skills -p test_github_issue_creation.py` passes locally with the assertions listed in CHECK-001.
- **TASK-002:** `SKILL.md` declares `name: github-issue-creation`, states when to use it, its inputs, result and failure conditions, and references the Standards through `standards/index.yaml` without copying policy, forms or Origin options.
- **TASK-003:** the plugin validator and the runner's skill list include the Skill, and the runner executes the new suite.
- **TASK-004:** the three guides exist and agree on prerequisites, permissions, failures and the vulnerability route.
- **TASK-005:** the cases in `tests/skills/cases/github-issue-creation/` cover every scenario listed in CHECK-003, and the stub records calls without reaching GitHub.
- **TASK-006:** each check has a recorded result with evidence under `docs/validation/issue-creation-skill/`, and every acceptance and regression obligation has an assessment. CHECK-004 runs only after the developer authorizes the live issue.
- **TASK-007:** delivery validation passes for the dossier in `specs/archive/issue-creation-skill/`.

## Planning review

Tasks revision 1 is awaiting the developer's review. Tasks approval ends planning; implementation requires an explicit request.

## Progress

No task has started.

## Validation evidence

No check has been executed.

## Delivery

Closure is active.
