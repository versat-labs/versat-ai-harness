---
sdd_version: 3
change: english-issue-definitions
requirements: [REQ-001, REQ-002, REQ-003]
adrs:
  - docs/decisions/0010-refine-language-policy.md
  - docs/decisions/0019-github-issue-language.md
validation:
  - id: CHECK-001
    description: Apply the published authoring guidance to representative issues and comments.
    requirements: [REQ-001, REQ-002, REQ-003]
    required: true
    method:
      kind: review
      procedure: >-
        Follow the issue-filing paragraph of each contribution guide and its link to the Language Standard.
        Using the walkthrough below, assess a feature form, a bug report, a mixed-language issue and
        two Spanish comments. Compare the results with the root agent instructions, ADR lineage and
        internal PR template. Record the supporting passages and the outcome for each case.
      reason: The distinction depends on what a comment decides and what an issue author wrote. A language classifier cannot establish either.
    inputs:
      include:
        - standards/core/language.md
        - AGENTS.md
        - docs/user-docs/guides/contributing.md
        - docs/user-docs/guides/contributing.pt.md
        - docs/user-docs/guides/contributing.es.md
        - docs/decisions/README.md
        - docs/decisions/0010-refine-language-policy.md
        - docs/decisions/0019-github-issue-language.md
        - .github/pull_request_template.md
      exclude: []
    outputs: &evidence [docs/validation/english-issue-definitions]
    execution: local
  - id: CHECK-002
    description: Run the maintained Harness validation and regression suites.
    requirements: [REQ-003]
    required: true
    method:
      kind: automated
      procedure: >-
        From a clean source checkout with the pinned validation dependencies and bytecode generation
        disabled, run ./scripts/validate/run.sh --quality-base origin/main. Expect exit zero from
        the complete suite. Record the comparison revision, test counts, failures and exit status.
    inputs:
      include: [AGENTS.md, README.md, CHANGELOG.md, VERSION, plugin.json, .agents/plugins, .codex-plugin, .github, agents, docs, project-templates, resources, schemas, scripts, sdd, skills, specs, standards, tests, validators, requirements-validation.txt, ruff.toml]
      exclude: *evidence
    outputs: *evidence
    execution: local
coverage:
  - {scenario: {requirement: REQ-001, scenario: 1}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-001, scenario: 2}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-001, scenario: 3}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-002, scenario: 1}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-002, scenario: 2}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-003, scenario: 1}, applicability: required, checks: [CHECK-001, CHECK-002]}
  - {scenario: {requirement: REQ-003, scenario: 2}, applicability: required, checks: [CHECK-001]}
regression:
  - obligation: {impact: 2, scenario: 0}
    checks: [CHECK-001]
    rationale: The comment walkthrough checks continued use of Spanish by teammates and English capture of decisions that redefine the work.
  - obligation: {impact: 3, scenario: 1}
    checks: [CHECK-001]
    rationale: Read the maintained Spanish internal PR template alongside the operative PR language rule.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 047103f7a943df216c9c21f3bede9e777bf9c6ea6f12ea45ccfc29abf4e68f49
  approval:
    source: Developer reply in the Codex chat after presentation of Design revision 1 and proposed ADR-0019 for GitHub issue 50.
    quote: "Aprovo a revisão 1 do Design da issue #50, incluindo o ADR-0019 proposto. Pode avançar para o planejamento das tarefas."
    revision: 1
    digest: c9d296096f4e0f0be614f03961b699acbead21b1a6a0db1adba832b1e114ce65
---

# Design for English issue definitions

## Policy and authoring surfaces

The current [Language Standard](../../../standards/core/language.md) assigns Spanish to internal issues and pull requests in one row. Split that row so that issue titles and authored descriptions default to English and internal pull requests keep their Spanish rule. Qualify the collaborator-discussion rule for issue comments. A maintainer who accepts a scope or acceptance change in a Spanish discussion updates the description in English. Routine discussion can stay entirely in Spanish.

Align the language summary in the root [agent instructions](../../../AGENTS.md). At the issue-filing step of the existing [contribution guide](../../../docs/user-docs/guides/contributing.md), tell authors which fields to write in English and link to the canonical rule. Give readers of the Portuguese and Spanish editions the same instruction in their own language. Use the existing form fields, including free-text responses. A quoted error inside an English bug report may retain its original text.

The policy belongs to the Harness 0.4.0 source tree. The [Standards index](../../../standards/index.yaml) already resolves the Language, Documentation, Contribution, Coding, Testing and Git standards. The draft [ADR-0019](../../../docs/decisions/0019-github-issue-language.md) records the issue-specific refinement of ADR-0010. At implementation, index the decision and add a cross-reference to the historical record that identifies the affected clause. Preserve ADR-0010's original decision text.

## Adoption and alternatives

Apply the guidance when a maintainer files an issue or substantively revises its definition. A comment on an old issue alone creates no obligation to translate the backlog. Document adoption in the Unreleased changelog and use the normal reviewed policy PR. Consumers adopt through their selected Harness release. A rollback would restore the previous authoring instructions in a reviewed change and record the decision history. It would require no rewrite of GitHub records.

Requiring English in every comment would add translation work for routine team exchanges. Bilingual descriptions would create two versions for maintainers to reconcile. Reviewing the existing title and description provides a single place to read the current scope. GitHub permissions, issue forms, runtime data and telemetry require no changes.

## Validation walkthrough

Use local examples, without posting test issues. For each row, verify that a reviewer can reach the expected decision from the maintained instructions.

| Example | Expected decision |
|---|---|
| A contributor requests CSV export through a feature form. | The title, problem, expected outcome and any acceptance criteria are authored in English. |
| A bug report quotes the diagnostic `Archivo no encontrado`. | The title, reproduction steps, expected and observed behavior are in English. Preserve the diagnostic verbatim. |
| A new issue has an English title and its entire description in Spanish. | Request an English description and point to the applicable language rule. |
| A teammate asks in Spanish where to find a fixture. | The comment and reply may stay in Spanish. The issue definition needs no edit. |
| Teammates agree in Spanish that CSV exports must include archived records. | Update the English description with that acceptance criterion. An external reader can discover it without reading the thread. |
| A maintainer reads the three guide editions and the agent instructions, then prepares an internal PR. | Each guide communicates the same issue rule and links to the standard. The root instructions agree, and the standard and Spanish PR template still support filing the internal PR in Spanish. |

The review also checks the decision index and both ADR links. The automated package suite provides structural and regression coverage alongside this semantic review. Its previously observed marketplace skill-count failure must be reported while present. Delivery still requires the full suite and the repository's required CI checks to pass.

## Planning review

The developer approved Design revision 1, including proposed ADR-0019, and authorized task planning.
