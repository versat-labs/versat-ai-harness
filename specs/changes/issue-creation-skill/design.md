---
sdd_version: 3
change: issue-creation-skill
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008]
adrs: []
validation:
  - id: CHECK-001
    description: Verify deterministic form resolution, required-field detection and issue rendering by the Skill helper.
    requirements: [REQ-001, REQ-002, REQ-003]
    required: true
    method:
      kind: automated
      procedure: >-
        Run python -m unittest discover -s tests/skills -p test_github_issue_creation.py.
        Expect the tests to pass against synthetic fixtures copied from the organization forms
        and a synthetic repository-specific form. They assert that repository forms take
        precedence over organization defaults, that the Bug report, Feature request and Chore
        forms yield the title prefixes fix, feat and chore with types Bug, Feature and Task,
        that missing required answers are reported by field label, that rendering is refused
        while a required answer is missing or blank, that optional empty fields render as
        "_No response_", that field labels become level-three headings in form order, that
        upload fields are skipped with a notice, and that code blocks and identifiers in answers
        are preserved byte for byte.
    inputs:
      include: [skills/github-issue-creation, tests/skills/test_github_issue_creation.py, tests/skills/fixtures/github-issue-creation]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/issue-creation-skill]
    execution: local
  - id: CHECK-002
    description: Retain the package, SDD, validator and execution suites with the new Skill registered.
    requirements: [REQ-008]
    required: true
    method:
      kind: automated
      procedure: >-
        Run ./scripts/validate/run.sh with the documented validation Python environment, including
        Ruff 0.14.14 from requirements-validation.txt, after adding the Skill to the runner's skill
        list, the plugin validator's required Skills and the focused unittest invocation. Expect
        all suites to pass, the plugin validator to find skills/github-issue-creation/SKILL.md
        declaring name github-issue-creation, and the changelog check to find the Unreleased entry.
    inputs:
      include: [skills, standards, validators, scripts, tests, sdd, schemas, project-templates, plugin.json, .codex-plugin, VERSION, requirements-validation.txt, CHANGELOG.md, README.md, README.pt.md, README.es.md, docs/user-docs]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/issue-creation-skill]
    execution: local
  - id: CHECK-003
    description: Exercise the Skill's dialogue and authorization boundaries in supervised scenarios that stop before publication.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007]
    required: true
    method:
      kind: review
      procedure: >-
        Following docs/guides/skill-evaluations.md, run one fresh native agent per case in
        tests/skills/cases/github-issue-creation/ against a synthetic repository fixture, with
        GitHub write tools unavailable or replaced by a recording stub. Cases are a Portuguese
        feature prompt, a Spanish bug prompt with a stack trace, an ambiguous feature-or-chore
        prompt, a bug prompt without reproduction steps, a feature prompt without a persona, a
        complete chore prompt, a prompt naming a paying VIP customer, a prompt without origin,
        a vulnerability in a public repository, a vulnerability in a private repository, a
        vulnerability with no known route, a declined preview, and stubbed failures for issue
        creation and for the project link. Expect English titles and bodies with the stack trace
        unchanged, one form question only for the ambiguous case, questions only for the missing
        required fields, an origin question listing the three options and their meanings unless
        stated, a preview listing repository, form, title, body, type, Origin and Portfolio, no
        create call before confirmation or after a decline, no issue for any vulnerability case
        with the matching private route and no vulnerability details in public output, and final
        reports that match the stub's recorded results, including partial failures with remedies.
      reason: Dialogue quality, translation and authorization behavior of an agent cannot be asserted by deterministic tests; they need supervised observation of actual runs.
    inputs:
      include: [skills/github-issue-creation, tests/skills/cases/github-issue-creation, tests/skills/fixtures/github-issue-creation, standards]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/issue-creation-skill]
    execution: local
  - id: CHECK-004
    description: Create one real issue end to end and confirm type, Origin and Portfolio membership on GitHub.
    requirements: [REQ-002, REQ-005, REQ-007]
    required: true
    method:
      kind: manual
      procedure: >-
        With the developer's explicit authorization for this publication, run the Skill in
        versat-labs/versat-ai-harness with a real chore prompt and confirm the preview. Then read
        the created issue and the organization's "Portfolio" project through the GitHub API.
        Expect the reported link to resolve to an issue whose title starts with "chore: ", whose
        type is Task, whose body has the Description, Scope and Done when sections, whose Origin
        value matches the answer, and which is an item of the project titled "Portfolio". Record
        whether that project's number is 1, as the forms reference. Close the issue afterwards
        only if the developer asks.
      reason: Project membership, issue fields and token scopes depend on the live GitHub organization and cannot be reproduced locally.
    inputs:
      include: [skills/github-issue-creation]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/issue-creation-skill]
    execution: local
  - id: CHECK-005
    description: Review the Skill contract and the trilingual usage guide.
    requirements: [REQ-008]
    required: true
    method:
      kind: review
      procedure: >-
        Read skills/github-issue-creation/SKILL.md and docs/user-docs/guides/issue-creation.md
        with its Portuguese and Spanish versions. Expect the Skill to state when to use it, its
        inputs, result and failure conditions, to locate language, contribution and security
        policy through standards/index.yaml and the organization's SECURITY.md instead of copying
        them, and to keep no copy of the forms or Origin options. Expect the guides to list the
        prerequisites, including GitHub authentication and the permissions for issues, issue
        fields and organization projects, to give an example prompt, and to agree with each
        other on permissions, failure handling and the vulnerability route.
      reason: Contract completeness, non-duplication of policy and translation alignment are documentation qualities that need human review.
    inputs:
      include: [skills/github-issue-creation, docs/user-docs/guides, standards/index.yaml]
      exclude: []
    outputs: [docs/validation/issue-creation-skill]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-004]
  - scenario: {requirement: REQ-002, scenario: 4}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 4}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-004, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-004, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-005, scenario: 1}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-005, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-006, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-006, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-006, scenario: 3}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-007, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-007, scenario: 2}
    applicability: required
    checks: [CHECK-003, CHECK-004]
  - scenario: {requirement: REQ-007, scenario: 3}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-008, scenario: 1}
    applicability: required
    checks: [CHECK-002, CHECK-005]
  - scenario: {requirement: REQ-008, scenario: 2}
    applicability: required
    checks: [CHECK-005]
  - scenario: {requirement: REQ-008, scenario: 3}
    applicability: required
    checks: [CHECK-002]
regression:
  - obligation: {impact: 1, scenario: 1}
    checks: [CHECK-003]
    rationale: The Portuguese and Spanish prompt cases confirm that feature issues are written in English, including form responses.
  - obligation: {impact: 1, scenario: 2}
    checks: [CHECK-001, CHECK-003]
    rationale: The bug cases confirm English reproduction and expected behavior while diagnostics keep their original spelling.
  - obligation: {impact: 2, scenario: 0}
    checks: [CHECK-001]
    rationale: Form resolution tests confirm that the repository's own forms take precedence over organization defaults.
  - obligation: {impact: 3, scenario: 0}
    checks: [CHECK-003]
    rationale: The vulnerability cases confirm that no issue is created and details stay out of public output.
  - obligation: {impact: 4, scenario: 0}
    checks: [CHECK-001, CHECK-003, CHECK-004]
    rationale: Tests and the live run confirm the organization forms' prefixes, types, required fields, Portfolio project and vulnerability routes.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 4348c5831e8ff05e64d2a251aaf949c5039f9f6305a9a2975c2fed6cb790be6f
  approval: null
---

# Design

## Current state

The Plugin package at the repository root publishes Skills from `skills/` through `plugin.json` and `.codex-plugin/plugin.json`. `scripts/validate/run.sh` and `validators/plugin/validate.py` each list the required Skills. Skill tests live in `tests/skills/`, with supervised evaluations following [Skill evaluations](../../../docs/guides/skill-evaluations.md). User guides live in `docs/user-docs/guides/` in English, Portuguese and Spanish. No Skill interacts with GitHub issues.

The organization forms and security routes are recorded in the Proposal's current contract baseline. Creating issue #53 in this session showed that the REST/MCP issue creation accepts `type` and the "Origin" issue field, and that a form's `projects` key is not applied outside the web form.

## Proposed design

### Skill package

Add `skills/github-issue-creation/`:

- `SKILL.md` defines the procedure below, its inputs (the developer's prompt and the current repository), its result (an issue link with per-step results, or a private-route instruction) and its failure conditions.
- `scripts/issue_form.py` is a dependency-light Python helper using PyYAML, already in `requirements-validation.txt`. It provides a CLI with three commands:
  - `resolve --repo-dir <path> --org-dir <path>` lists the applicable forms with name, title prefix, type, `projects` and fields. It prefers `.github/ISSUE_TEMPLATE/*.y{a,}ml` in the repository and falls back to the organization directory.
  - `missing --form <file> --answers <json>` lists required field labels that are absent or blank.
  - `render --form <file> --answers <json> --title <text>` prints the title with the form's prefix and the body in GitHub's form-response layout, with `### <label>` headings in form order and `_No response_` for empty optional fields. It skips upload fields with a notice, refuses to render while a required answer is missing, and never alters answer text.

The helper only reads local files and prints. It never calls GitHub.

### Procedure in SKILL.md

1. **Resolve context.** Identify the target repository from the Git remote and require the `versat-labs` owner. Resolve the language, contribution and security Standards through `standards/index.yaml`. Fetch the organization forms from `versat-labs/.github` at its default branch, using a shallow clone or the GitHub contents API, and run `resolve`.
2. **Classify intent.** Detect a suspected vulnerability first. In that case go to step 7 and create nothing. Otherwise pick Bug report, Feature request or Chore, or the repository's own forms when present. Ask one question listing the candidate forms when more than one fits.
3. **Draft in English.** Translate the developer's content into English for the title and each field. Keep identifiers, commands, code blocks and diagnostics verbatim. Do not invent facts.
4. **Clarify.** Run `missing` and ask in one message for every missing required field. Ask for "Origin" with the three options and their meanings unless the prompt states it. Read the options from the organization's issue fields at run time.
5. **Preview.** Render the issue and show the repository, form, title, body, type, Origin and project. Proceed only after explicit confirmation. Revise on request, and stop without creating anything on a decline.
6. **Create and report.** Create the issue with the type, then set "Origin", then add the issue to the organization project titled "Portfolio". The order guarantees that an existing issue is reported even when a later step fails. Read the issue back and report the link plus the actual status of type, Origin and project. Report a failed step with the reason and the manual remedy, and never retry creation automatically, to avoid duplicates. Warn if the "Portfolio" project's number differs from the forms' `projects` value.
7. **Vulnerability route.** For a public repository, direct the developer to **Security → Report a vulnerability** and list the private form's fields. For a private repository, direct them to email the relevant CODEOWNERS through internal Versat channels without guessing addresses. When the route is unclear, tell them to ask a maintainer for private instructions. Do not repeat the vulnerability details in the answer beyond what is needed.

### GitHub access

The Skill is executor-independent, following [ADR-0009](../../../docs/decisions/0009-execution-adapters.md). It uses the GitHub tools the executor already has and documents two equivalent routes:

- **GitHub MCP server:** `issue_write` with `type` and `issue_fields`, then a projects tool when available.
- **GitHub CLI:**
  - `gh api` for `POST /repos/{owner}/{repo}/issues` with `type` and the issue field value.
  - `gh project list --owner versat-labs` and `gh project item-add` for "Portfolio".

When neither route can perform a step, the Skill reports the step and the manual remedy. The guide lists the required permissions: issues write on the repository, the organization's issue fields, and the `project` scope for organization projects.

### Registration and documentation

- Add `github-issue-creation` to the required Skills in `scripts/validate/run.sh` and `validators/plugin/validate.py`, and add the focused unittest invocation to the runner.
- Add `docs/user-docs/guides/issue-creation.md` with `.pt.md` and `.es.md` translations, covering prerequisites, an example prompt, the dialogue, results and failures.
- Add a changelog `Unreleased` entry.

## Boundaries and contracts

The Skill applies the existing [Language](../../../standards/core/language.md), [Contribution](../../../standards/core/contribution.md) and [Security](../../../standards/core/security.md) Standards, and the organization's forms and `SECURITY.md`, without changing them. It keeps no copy of form content, Origin options or policy text. It touches no other repository settings, and creates issues only in the current `versat-labs` repository. Consumer project layouts are unaffected because this is a Plugin Skill, as described in the [architecture overview](../../../docs/architecture/overview.md).

## Data, security and permissions

The Skill uses the developer's existing GitHub authentication and stores no credentials. The preview is the publication gate, and confirmation authorizes only that one issue. Vulnerability details never reach issue-creation calls. Prompts may contain customer names, so the preview lets the developer remove sensitive information before publication. In a public repository the issue is public, and the guide warns about this.

## Operations and observability

There is no runtime service. The per-step result report is the operational record. Failures report GitHub's error message without tokens.

## Migration, rollout and rollback

The Skill ships in the next Harness release. Consumers receive it when they adopt that exact version. Rollback removes the Skill directory, its registrations, guides and changelog entry. Issues already created remain on GitHub.

## Alternatives considered

- **Bundling a copy of the forms in the Skill.** Rejected because it would drift from `versat-labs/.github` and violate the rule against duplicated sources.
- **Opening the prefilled web form URL** (`issues/new?template=…`). That route applies the form's `projects` and `type` automatically, but cannot set Origin, depends on URL length limits and requires the developer to finish in the browser. It is kept as the documented manual fallback.
- **A GitHub Action or bot.** Rejected because it needs new credentials and infrastructure and is outside the Harness's capability boundary.
- **No helper script, with only agent instructions.** Rejected because form resolution, required-field detection and the rendering layout are deterministic and testable, and agent-only behavior would make REQ-002 and REQ-003 unverifiable offline.

No ADR is needed. The change adds a capability inside the existing Plugin structure and execution-adapter decisions.

## Validation plan

- **CHECK-001** covers deterministic helper behavior: precedence, prefixes, types, required fields, layout and verbatim text.
- **CHECK-002** keeps every existing package check and proves registration.
- **CHECK-003** observes the agent's dialogue for every behavioral scenario without publishing, using a recording stub to simulate GitHub results and failures.
- **CHECK-004** is the only live publication and requires separate explicit authorization. It confirms project membership, the issue field, the type and the `versat-labs/1` = "Portfolio" assumption.
- **CHECK-005** reviews the Skill contract and the trilingual guides.

Coverage maps all 23 acceptance positions. The regression rows map the English-issue origin scenarios and the three baseline contracts.

## Planning review

Design revision 1 is awaiting the developer's review.
