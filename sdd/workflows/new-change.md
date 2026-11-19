# New change

Use for a new intent, revision of planning, or implementation requested without a current approved plan. Read the canonical [process](../process.md) and [metadata contract](../metadata.md). This phase writes planning artifacts and necessary ADR drafts; it does not execute the implementation tasks.

## Entry and context

Identify the project and one stable change ID. Read its instructions, selected Harness version, resolved Standards, relevant specifications and enough code/tests to ground the intent. Inspect existing active/archive dossiers before creating anything. Resume a matching change; preserve unrelated edits. Resolve ambiguity that materially changes the target or desired behavior.

Use the matching [templates](../templates/) and [schemas](../schemas/). Record real work-tracking context in Proposal and apply the resolved Git Standard. An absent issue or branch alone does not block analysis of intent. Git mutations follow the project's policy and actual authorization; do not create remote work merely because planning started.

## Stage 1: Proposal and Requirements

Create only `proposal.md` and `requirements.md`. Establish the observable need, actors, intended outcome, scope, exclusions, constraints, risks and acceptance scenarios. Use stable requirement IDs. Separate repository-backed facts from assumptions and unresolved decisions; clarify material ambiguities before approval. For a greeting button, establish its screen, label and accessible presentation rather than silently choosing a screen or blocking alert.

Consider relevant success, error and boundary scenarios under the resolved [Testing Standard](../../standards/core/testing.md), keeping their depth proportional to risk.

Use the resolved [Documentation Standard](../../standards/core/documentation.md) to identify the affected readers, their goal, the purpose of the feature and the living material that needs an update. Record why no documentation work applies when appropriate.

Set the combined review on Proposal to `awaiting-approval` when reviewable, or `blocked` with actual blockers. Check document consistency and run the planning validator for this change. Present both files and their current revision, then stop at Gate 1. Record the actual approval and matching Proposal/Requirements digest only after the developer accepts that revision. Approval unlocks Design.

## Stage 2: Design

Prerequisites: current Gate 1 approval, no material blockers, and resolved applicable Standards. Create `design.md` grounded in the existing architecture. Describe affected components/contracts, reuse, meaningful alternatives and the relevant data, security, operations, migration, rollout and rollback concerns. Explain briefly when a template concern is not applicable.

Map all approved requirements to the design and at least one required, identifiable check per requirement in `validation`. Identify actual test/eval/validator entry points and distinguish proposed checks from existing ones. Reference the applicable Standards/version. For significant structural decisions, follow the project's ADR convention; prepare and present real ADR drafts and references with this review. A required unresolved ADR remains a blocker.

Explain how the checks cover relevant acceptance scenarios and affected documented usage, including examples, applicable locales and publication readiness, under the resolved [Documentation Standard](../../standards/core/documentation.md). Reuse adequate existing checks; one method can cover multiple scenarios or serve both functional and documentation validation without new identifiers or reports.

Set Design's upstream Proposal digest, check references/coverage, and run the planning validator. Present Design, checks, alternatives and ADRs; stop at Gate 2. Record approval for the reviewed Design digest before proceeding. If design discovery changes requirements, reopen Gate 1 using the process's revision rules.

## Stage 3: Tasks

Prerequisite: current Gate 2 approval and its current upstream approval. Create `tasks.md` with ordered, independently verifiable tasks, stable task IDs, valid requirement references, dependencies and completion conditions. Cover the implementation, testing and documentation required by the approved scope. Do not add a task that can only complete after merge to the pre-merge completion gate; record authorized post-delivery operational follow-up separately.

Include affected usage instructions and examples with the work that changes their behavior. Reuse living guides and existing task completion checks; changes without documented usage impact need no documentation task solely for ceremony.

Keep future tasks `pending` and unchecked; use `blocked` with explanation for an actual unavailable prerequisite. Writing a plan completes no implementation task. Keep validation results empty and closure `active`. Bind Tasks to the current Proposal and Design digests, check requirement coverage and run the planning validator. Present the tasks, checks, dependencies and risks; stop at Gate 3.

After approval, record the actual source, quote and matching Tasks digest, then check implementation readiness. If all gates are current and blockers absent, report planning complete. Implementation begins only with an explicit execution instruction after review of the current plan; the Gate 3 approval reply may contain that instruction. In that case read [Implement change](implement-change.md) before transitioning. Otherwise stop with the artifact links and the next permitted action.

## Corrections and handoff

Use the process's gate and revision rules for feedback and resumption; do not create later-stage placeholders to satisfy validation. Keep only the earliest unfinished stage active while dependent drafts are superseded. Every handoff states change ID, stage/revision, files, unresolved decisions, the requested approval and what it unlocks. Do not claim implementation or test success from a completed planning phase.

## v3 planning records

At Gate 1, populate Proposal `impact`: inspect affected living contracts, code and maintained tests, then related active/archive requirements. Record a qualified source and canonical Requirements digest when available, plus the current contract path/locator and pre-change file digest, or a captured Proposal baseline. Classify preserve, extend or intentional supersede with local targets and reasons. A reviewed no-impact conclusion uses assessed/empty items with a concrete summary; unresolved impact cannot advance readiness.

At Gate 2, map all one-based acceptance positions in Design `coverage`, including justified not-applicable rows. Map every preserved/extended source scenario in `regression` by impact item position and source scenario (use zero only without a historical source). Specify check method, expected observations, input roots/exclusions, output paths and local/CI context. Reuse adequate maintained tests; plan missing regression work. Supersession needs reviewed replacement behavior/checks, not merely removal of failing tests. Inspect scope adequacy; the validator only verifies declared relationships.

At Gate 3, keep `validation.results`, `assessments` and `findings` empty until actual execution/review. Changes to any substantive mapping reopen the relevant gate. An existing bounded v2 plan can finish unchanged, but new or materially replanned work adopts v3 through genuine review.
