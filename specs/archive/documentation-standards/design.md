---
sdd_version: 3
change: documentation-standards
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005]
adrs: [docs/decisions/0018-consumer-documentation-and-pr-reporting.md]
validation:
  - id: CHECK-001
    description: Review consumer layout, bootstrap and reference compatibility
    requirements: [REQ-001]
    required: true
    method:
      kind: manual
      procedure: >-
        Walk through new usable, empty scaffold and legacy consumer fixtures using the standards, bootstrap and composition guidance. Confirm discoverable navigation, applicable directories, one discovery source, equivalent paths, unchanged pins and successful SDD validation of explicit and legacy ADR references.
      reason: Layout applicability and guided bootstrap decisions require observation.
    inputs:
      include: [standards, project-templates, skills/project-bootstrap, skills/project-maintenance, sdd, validators/sdd, docs/decisions/0018-consumer-documentation-and-pr-reporting.md]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
  - id: CHECK-002
    description: Walk through SDD documentation planning, implementation and verification
    requirements: [REQ-002]
    required: true
    method:
      kind: manual
      procedure: >-
        Use a representative changed feature with a living guide, a blocked usage check and an internal change without usage impact. Inspect the planned audiences and rationale, same-change guide updates, reused evidence, unverified result and proportional task selection. Confirm that moving the dossier leaves reader links intact.
      reason: Readability, suitability of examples and equivalence of retained evidence require human assessment.
    inputs:
      include: [standards, sdd, skills/versat-sdd, docs/user-docs]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
  - id: CHECK-003
    description: Review language, navigation and example parity
    requirements: [REQ-003]
    required: true
    method:
      kind: review
      procedure: >-
        Inspect a trilingual feature example and an English technical reference reached from a translated guide. Verify links, matching user outcomes, accuracy of operational constraints and applicability of the Language Standard.
      reason: Presence of translations does not establish semantic parity.
    inputs:
      include: [standards, sdd, docs/user-docs]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
  - id: CHECK-004
    description: Rehearse publication guidance for public and restricted products
    requirements: [REQ-004]
    required: true
    method:
      kind: manual
      procedure: >-
        Follow the guide with a publishable sample feature and a restricted sample without an approved destination. Trace ownership, approvals, three language variants, navigation, source revision, post-publication verification and the pending disposition without deploying either sample.
      reason: The exercise checks the process and audience decisions.
    inputs:
      include: [standards, docs/user-docs, docs/product]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
  - id: CHECK-005
    description: Exercise documentation reporting and check the GitHub adapter
    requirements: [REQ-005]
    required: true
    method:
      kind: automated
      procedure: >-
        Run python -m unittest discover -s tests/validators -p test_documentation.py. Expect passing verdicts for complete variants, failures for missing or empty counterparts and localized orphans, not-applicable for unrelated or fully removed sets, and unavailable reporting for incomplete inputs. Verify sanitized Markdown, bounded output and the sample workflow contract.
    inputs:
      include: [standards, validators/documentation, scripts/validate/documentation.sh, tests/validators/test_documentation.py, project-templates/artifacts/validation, .github/workflows, docs/guides/project-validation.md, docs/decisions/0018-consumer-documentation-and-pr-reporting.md]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
  - id: CHECK-006
    description: Review PR presentation, access boundaries and retained governance
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005]
    required: true
    method:
      kind: review
      procedure: >-
        Inspect the workflow and render sample mixed and empty reports. Compare the Checks and summary path with official GitHub documentation, and verify read-only execution, unchanged required job names, manual review labels, evidence limits and unchanged SDD approval rules. Run the full Harness validation script with an explicit quality base.
      reason: Live PR presentation is a separate observation, and static review is needed for permissions and policy boundaries.
    inputs:
      include: [AGENTS.md, VERSION, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, ruff.toml, standards, sdd, schemas, skills, project-templates, validators, scripts, tests, .github/workflows, docs/guides/project-validation.md, docs/decisions/0018-consumer-documentation-and-pr-reporting.md]
      exclude: []
    outputs: [docs/validation/documentation-standards]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 3}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-002, scenario: 3}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-004, scenario: 1}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-004, scenario: 2}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-005, scenario: 1}
    applicability: required
    checks: [CHECK-005, CHECK-006]
  - scenario: {requirement: REQ-005, scenario: 2}
    applicability: required
    checks: [CHECK-005, CHECK-006]
regression:
  - obligation: {impact: 2, scenario: 2}
    checks: [CHECK-001]
    rationale: Preserve working documentation and avoid placeholders.
  - obligation: {impact: 2, scenario: 3}
    checks: [CHECK-001]
    rationale: Preserve working documentation and avoid placeholders.
  - obligation: {impact: 4, scenario: 1}
    checks: [CHECK-001]
    rationale: Retain README navigation, proportional detail and stable locations.
  - obligation: {impact: 4, scenario: 2}
    checks: [CHECK-001]
    rationale: Retain README navigation, proportional detail and stable locations.
  - obligation: {impact: 4, scenario: 4}
    checks: [CHECK-001]
    rationale: Retain README navigation, proportional detail and stable locations.
  - obligation: {impact: 5, scenario: 1}
    checks: [CHECK-002]
    rationale: Verify planning and updates to the existing guide.
  - obligation: {impact: 5, scenario: 2}
    checks: [CHECK-002]
    rationale: Verify planning and updates to the existing guide.
  - obligation: {impact: 5, scenario: 3}
    checks: [CHECK-002]
    rationale: Verify planning and updates to the existing guide.
  - obligation: {impact: 6, scenario: 1}
    checks: [CHECK-002]
    rationale: Verify observed usage, blocked verification and evidence reuse.
  - obligation: {impact: 6, scenario: 2}
    checks: [CHECK-002]
    rationale: Verify observed usage, blocked verification and evidence reuse.
  - obligation: {impact: 6, scenario: 3}
    checks: [CHECK-002]
    rationale: Verify observed usage, blocked verification and evidence reuse.
  - obligation: {impact: 6, scenario: 4}
    checks: [CHECK-002]
    rationale: Verify observed usage, blocked verification and evidence reuse.
  - obligation: {impact: 7, scenario: 1}
    checks: [CHECK-006]
    rationale: Retain the existing governance and four-file dossier.
  - obligation: {impact: 7, scenario: 2}
    checks: [CHECK-001]
    rationale: Retain composed templates and explicit exact-release adoption.
  - obligation: {impact: 7, scenario: 3}
    checks: [CHECK-001]
    rationale: Retain composed templates and explicit exact-release adoption.
  - obligation: {impact: 7, scenario: 4}
    checks: [CHECK-006]
    rationale: Retain the standards boundaries for language and security.
  - obligation: {impact: 8, scenario: 1}
    checks: [CHECK-001]
    rationale: Retain the derived reader overview and the canonical shared discovery record.
  - obligation: {impact: 8, scenario: 4}
    checks: [CHECK-001]
    rationale: Retain the derived reader overview and the canonical shared discovery record.
  - obligation: {impact: 9, scenario: 1}
    checks: [CHECK-003]
    rationale: Verify language sibling navigation and equivalent semantics.
  - obligation: {impact: 9, scenario: 2}
    checks: [CHECK-003]
    rationale: Verify language sibling navigation and equivalent semantics.
  - obligation: {impact: 9, scenario: 3}
    checks: [CHECK-003]
    rationale: Verify language sibling navigation and equivalent semantics.
  - obligation: {impact: 10, scenario: 0}
    checks: [CHECK-006]
    rationale: Review publication and reporting boundaries alongside the consumer layout.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: "2fef179090a22f6c31db50ccf4fd99d7638fc559d5c176ecbb455b4f2493e2a4"
  approval:
    source: "Developer approval in this Codex conversation after the Portuguese reading translation of Issue #23 Design revision 1"
    quote: "Aprovo o desenho técnico e o ADR-0018 proposto da revisão 1 da issue #23. Pode avançar para as tarefas."
    revision: 1
    digest: "5643c1db95db9109e0f159a55a6083537fbecc33ab414a1626f1ff096e210a40"
---

# Design

## Documentation and SDD

Use Harness source 0.4.0. Put normative layout and applicability in the index-resolved Documentation Standard. Reference the Language, Security, Licensing and Publication, Testing, and Git Standards for their existing responsibilities. Keep the following behavior in existing stages.

| Stage | Change |
| --- | --- |
| Proposal and Requirements | Capture documentation impact by affected audience, user goal, feature purpose and living material. Record a short reason when no documentation work applies. |
| Design and Tasks | Map applicable updates and usage verification into existing requirements, checks and tasks. Identify useful examples, localization and any publication readiness work. |
| Implementation and Validation | Update the relevant living documents with the behavior. Compare commands or UI steps with their documented results and reuse adequate functional evidence. Record gaps as unverified under the existing evidence contract. |

Use compact prompts in the current templates and workflow guidance. No new dossier fields, approval stage or Skill. Guide content covers why, when, prerequisites, a representative action, expected outcome and relevant limits or recovery. Technical references focus on rationale and the applicable contracts or operational impact. Provide a worked feature example in the publication guide with aligned English, Portuguese and Spanish versions.

Use the approved directory layout for new applicable material. README links to the actual quickstart. Quickstart links to detailed guides when needed. Base composition continues to supply `specs/product/overview.md` for discovery. The reader overview at `docs/product/overview.md` presents publishable context and links approved sources. Bootstrap creates it and reader guides only when suitable material exists. Existing equivalent paths remain usable. Use explicit repository-relative SDD ADR references for new consumer records under `docs/architecture/decisions/`. The validator already accepts them. Existing provider and consumer `ADR-0001` lookups under `docs/decisions/` continue to work.

## Publication

Add a public-facing publication guide in `docs/user-docs/guides/` with English, Portuguese and Spanish siblings. Make it discoverable from existing reader documentation. A product team selects the documentation and marketing destinations, names an owner and maps each publishable feature to its page and applicable guide. The guide describes how to keep locales aligned, review audience and disclosure, publish an approved revision through the team's chosen process, verify access and links from the intended audience, and maintain or roll back the published revision. Restricted destinations and content receive the appropriate access decision before exposure. Pending or inapplicable publication records its reason and owner. The worked example includes a publishable feature and a restricted case. Production publishing and choice of hosting platform remain with the team.

## PR reporting

Implement a deterministic, advisory report for the first set of mechanical rules. The provider uses it on its own PRs. Add an opt-in example alongside existing validation adoption assets for GitHub consumers with an exact provider pin.

- Add a standard-library CLI under `validators/documentation/` and an entry point under `scripts/validate/`. Reuse the existing safe Git comparison conventions where applicable. Accept an explicit baseline and target checkout, and report missing baseline or incomplete inputs as unverified. In CI, use the PR base SHA and checked-out merge snapshot with sufficient history. Process additions, edits, moves and deletions by taking the union of affected paths and evaluating the final snapshot.
- Scope the mechanical rules to maintained Markdown under `docs/user-docs/`, reader overviews at `docs/product/overview[.pt|.es].md` and the known legacy quickstart paths `docs/quickstart[.pt|.es].md`. Group by canonical path. Check for the canonical English file and both readable, nonempty locale counterparts. A localized orphan or missing counterpart fails. A set removed in full is not applicable and calls out navigation review. Other legacy paths and technical docs have no automatic translation verdict. A PR with no recognized paths reports not applicable with the reason.
- Include the tested revision and baseline, each evaluated rule and its result, and paths or reasons for follow-up. List applicability, README navigation, rationale, factual accuracy, semantic alignment, and publication/access as review items. A completed report containing failed policy rows remains advisory. An execution failure is visible in the optional job with an unverified result when the job can produce output. Keep the existing required job names, gates and rulesets.
- Use a separate PR-only job with `pull_request`, `contents: read`, checkout without persisted credentials and a GitHub-hosted runner. Write Markdown to `GITHUB_STEP_SUMMARY`. Reviewers open the report from the PR check details. The job uses no secrets, privileged event or API write. Escape path text for Markdown and logs, limit output with a visible truncation marker, and reject symlink/traversal paths when reading files. Do not include document contents. Fork workflows follow repository approval settings.

References for the proposed presentation and permissions: [GitHub job summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary), [workflow check runs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), and [fork pull request behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request).

## Alternatives and rollout

A bot comment would place all results on the conversation tab. It adds write permission and lifecycle work for updates, and the same token contract would not cover normal fork PRs. A required check would turn mechanical policy rows into merge gates before applicability has been exercised across consumers. An entirely manual checklist would leave file-presence checks to reviewers. The advisory summary gives reviewers an actionable result with read access and preserves the option of a later governed change to enforcement.

The provider exercises the report first. Consumers choose whether to adopt the example and the versioned policy through the existing maintenance flow. Private provider checkouts that require credentials unavailable to PR jobs remain unverified for that integration. This change grants no credentials and establishes no new public access. Rollback is removal of the optional job or an explicit consumer pin rollback, with generated guidance reviewed alongside any wrapper change. Existing guidance and valid paths remain usable during adoption.

The principal implementation risk is inferring compliance from file naming or an empty report. Every row names the rule being measured, and review-only or unverified outcomes stay visible. Local fixtures and workflow contract review provide pre-submission evidence. Live PR rendering is confirmed only if observed on a separately authorized PR.

## Validation plan

CHECK-001 through CHECK-004 exercise layout compatibility, the complete documentation path through SDD, localized examples and the publication walkthrough. CHECK-005 covers mixed repository snapshots and adapter output. CHECK-006 reviews integration and governance and runs `./scripts/validate/run.sh --quality-base <comparison-ref>` using the observed base. In Tasks, record actual check evidence and current input snapshots. No implementation or live PR check has been run for this Design revision.

## Planning review

The developer approved Design revision 1 and the proposed ADR-0018 in the Codex conversation and requested the Tasks stage.
