---
sdd_version: 3
change: issue-creation-skill
tasks:
- id: TASK-001
  description: Implement the issue form helper with resolve, missing and render commands, plus synthetic
    form fixtures and its focused unittest suite.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  status: completed
- id: TASK-002
  description: Write the Skill procedure in SKILL.md covering context resolution, vulnerability detection,
    form selection, English drafting, clarification, Origin, preview, creation, Portfolio linking, result
    reporting and failure conditions.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-003
  description: Register the Skill in the validation runner and plugin validator, add the focused unittest
    invocation and the changelog Unreleased entry.
  requirements:
  - REQ-008
  status: completed
- id: TASK-004
  description: Write the issue creation user guide in English with aligned Portuguese and Spanish translations,
    covering prerequisites, permissions, an example prompt, results, failures and the vulnerability route.
  requirements:
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-005
  description: Add the supervised evaluation cases, the synthetic repository fixture and the recording
    GitHub stub for CHECK-003.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  status: completed
- id: TASK-006
  description: Execute CHECK-001 to CHECK-005, with separate authorization for the live issue in CHECK-004,
    record results and assess every acceptance and regression obligation.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-007
  description: Prepare the validated dossier for documentary delivery under specs/archive in the same
    branch.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: blocked
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 4348c5831e8ff05e64d2a251aaf949c5039f9f6305a9a2975c2fed6cb790be6f
    design: 72225a72ef8158bb66ef34653ad1f6e226388ac1e6dce5bafbd0b99bb8a7984c
  approval:
    source: Developer reply in the Claude Code chat after presentation of Tasks revision 1 for GitHub
      issue 53, which also authorized implementation.
    quote: Aprovado. Avance.
    revision: 1
    digest: dd500fd909b39bee3adacd964c756cd566209c1d7a94d69418855a1fc0aad480
validation:
  plan_digest: dd500fd909b39bee3adacd964c756cd566209c1d7a94d69418855a1fc0aad480
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/issue-creation-skill/check-001.txt
    revision: Commit ec9944c on claude/confident-dirac-8d9fzn
    input_digest_before: c33fc3ac9c2cfdbb3b03251b902321f92db835230e91fd789091f74cb0331e6d
    input_digest_after: c33fc3ac9c2cfdbb3b03251b902321f92db835230e91fd789091f74cb0331e6d
    context:
      execution: local
      environment: Python 3.11 virtual environment with requirements-validation.txt, Linux container
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/issue-creation-skill/check-002.txt
    revision: Commit ec9944c on claude/confident-dirac-8d9fzn
    input_digest_before: 4c1986d020fb0b7a2b01b993250b0278a1cae556452aad8193d6745a1131b0ab
    input_digest_after: 4c1986d020fb0b7a2b01b993250b0278a1cae556452aad8193d6745a1131b0ab
    context:
      execution: local
      environment: Python 3.11 virtual environment with requirements-validation.txt and Ruff 0.14.14,
        Linux container, quality base origin/main
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/issue-creation-skill/check-003.md
    revision: Commit ec9944c on claude/confident-dirac-8d9fzn
    input_digest_before: 3b4778318b9b1d1505d3586481657cc085aba847fb28ca7b34eda59fa1232ea6
    input_digest_after: 3b4778318b9b1d1505d3586481657cc085aba847fb28ca7b34eda59fa1232ea6
    context:
      execution: local
      environment: Claude Code cloud session, 14 fresh general-purpose subagents, synthetic fixtures and
        recording gh stub, no network
      observed: true
  - check: CHECK-004
    result: unverified
    evidence: docs/validation/issue-creation-skill/check-004.md
    revision: Commit ec9944c on claude/confident-dirac-8d9fzn
    input_digest_before: d12c660b55ff9bce468f2256a6eacd787501b61e61933adcd86815ba06e45e20
    input_digest_after: d12c660b55ff9bce468f2256a6eacd787501b61e61933adcd86815ba06e45e20
    context:
      execution: local
      environment: Claude Code cloud session with GitHub MCP issue tools and no projects tool, live versat-labs/versat-ai-harness
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/issue-creation-skill/check-005.md
    revision: Commit ec9944c on claude/confident-dirac-8d9fzn
    input_digest_before: 53721c8113587711d28cdf3f9866e0c9dcd4650ef6501f37c232eba8955fd6fa
    input_digest_after: 53721c8113587711d28cdf3f9866e0c9dcd4650ef6501f37c232eba8955fd6fa
    context:
      execution: local
      environment: Agent document review in the Claude Code cloud session
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Portuguese and Spanish prompts produced English titles and sections.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Tests preserve code and traces byte for byte; the Spanish trace kept teléfono verbatim.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Bug prompts selected Bug report without a form question.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: The ambiguous prompt received one question listing Bug report and Chore before drafting.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: unverified
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/issue-creation-skill/check-004.md
    explanation: 'Helper tests pass and #54 used the chore prefix, Task type and form sections, but CHECK-004
      is unverified as a whole.'
  - obligation:
      local:
        requirement: REQ-002
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/issue-creation-skill/check-001.txt
    explanation: Resolution tests show repository forms replacing organization defaults.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Missing To Reproduce was detected and asked for, with no invented steps.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Missing Persona was detected and asked for.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Complete prompts produced no field questions.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/issue-creation-skill/check-001.txt
    explanation: Rendering is refused while a required answer is missing or blank.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Without an origin, one question listed the three options with their meanings.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: The VIP prompt set VIP Customer feature request without a question.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: unverified
    checks:
    - CHECK-004
    evidence: docs/validation/issue-creation-skill/check-004.md
    explanation: 'The executor had no projects tool, so the Skill did not add #54 to Portfolio; the developer
      added it manually and confirmed Portfolio is project 1.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: The stubbed project failure was reported with the issue link, reason and remedies.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: 'Public vulnerability: no issue, private flow with the form fields.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: 'Private vulnerability: no issue, CODEOWNERS route and maintainer fallback without guessed
      addresses.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: 'Unknown route: no gh call, maintainer fallback without details.'
  - obligation:
      local:
        requirement: REQ-007
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: Previews listed all items; the decline created nothing.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/issue-creation-skill/check-004.md
    explanation: 'Reports matched stub results and the live read-back of #54 for type and Origin.'
  - obligation:
      local:
        requirement: REQ-007
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: The stubbed create failure was reported without retry or a claimed link.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-005
    evidence: docs/validation/issue-creation-skill/check-005.md
    explanation: Plugin validator discovers the Skill; the contract sections and Standards resolution
      were reviewed.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/issue-creation-skill/check-005.md
    explanation: Trilingual guides list prerequisites, permissions and an example.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/issue-creation-skill/check-002.txt
    explanation: ./scripts/validate/run.sh passed.
  - obligation:
      regression:
        impact: 1
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: English feature issues from Portuguese and Spanish prompts.
  - obligation:
      regression:
        impact: 1
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: English bug sections with verbatim diagnostics.
  - obligation:
      regression:
        impact: 2
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/issue-creation-skill/check-001.txt
    explanation: Repository forms take precedence over organization defaults.
  - obligation:
      regression:
        impact: 3
        scenario: 0
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/issue-creation-skill/check-003.md
    explanation: No issue for any vulnerability case.
  - obligation:
      regression:
        impact: 4
        scenario: 0
    result: unverified
    checks:
    - CHECK-001
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/issue-creation-skill/check-004.md
    explanation: Prefixes, types, fields and vulnerability routes were observed, but Portfolio linking
      by the Skill was not exercised live.
  findings:
  - id: FIND-001
    source:
      local:
        requirement: REQ-005
        scenario: 1
    category: partial
    state: open
    evidence: docs/validation/issue-creation-skill/check-004.md
    description: In an executor that offers only GitHub MCP issue tools, the Skill cannot add the issue
      to Portfolio and falls back to the manual remedy. Live Portfolio linking by the Skill has not been
      observed.
    tasks:
    - TASK-006
    checks:
    - CHECK-004
closure: active
---

# Tasks

- [x] TASK-001 — Implement the issue form helper, fixtures and unit tests
- [x] TASK-002 — Write the Skill procedure in SKILL.md
- [x] TASK-003 — Register the Skill, add the test invocation and changelog entry
- [x] TASK-004 — Write the trilingual user guide
- [x] TASK-005 — Add supervised evaluation cases, fixture and GitHub stub
- [x] TASK-006 — Execute the checks and assess every obligation
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

The developer approved Tasks revision 1 and asked to proceed, which authorizes implementation.

## Progress

- TASK-001: `skills/github-issue-creation/scripts/issue_form.py`, fixtures under `tests/skills/fixtures/github-issue-creation/` and 13 passing tests in `tests/skills/test_github_issue_creation.py`. The organization fixture copies the `versat-labs/.github` forms observed on 2026-11-27.
- TASK-002: `skills/github-issue-creation/SKILL.md`. Origin values are set through the GitHub issue field values API, which GitHub documents as a public preview.
- TASK-003: Skill registered in `scripts/validate/run.sh` and `validators/plugin/validate.py`, focused suite added to the runner, changelog entry added. A development run of `./scripts/validate/run.sh --quality-base origin/main` with Ruff 0.14.14 passed; it is not yet recorded as CHECK-002 evidence.
- TASK-004: guides `docs/user-docs/guides/issue-creation.md`, `.pt.md` and `.es.md`, linked from the three READMEs.
- TASK-005: 14 cases in `tests/skills/cases/github-issue-creation/`, the fixture preparer `prepare.py` and the recording `gh` stub.
- TASK-006: all five checks executed and every obligation assessed. CHECK-004 is unverified for Portfolio linking (FIND-001).
- TASK-007 is blocked until CHECK-004 passes in an executor with a projects capability.

## Validation evidence

| Check | Result | Evidence |
|---|---|---|
| CHECK-001 | pass | `docs/validation/issue-creation-skill/check-001.txt` (13 tests) |
| CHECK-002 | pass | `docs/validation/issue-creation-skill/check-002.txt` (full runner with Ruff) |
| CHECK-003 | pass | `docs/validation/issue-creation-skill/check-003.md` (14 supervised cases, stub logs) |
| CHECK-004 | unverified | `docs/validation/issue-creation-skill/check-004.md` (issue #54; Portfolio link added manually) |
| CHECK-005 | pass | `docs/validation/issue-creation-skill/check-005.md` |

FIND-001 remains open. Rerun CHECK-004 with the GitHub CLI holding the `project` scope, or with an MCP server that exposes projects, to verify REQ-005 scenario 1.

## Delivery

Closure is active.
