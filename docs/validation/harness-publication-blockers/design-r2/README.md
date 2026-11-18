# Design R2 local diagnostics

Date: 2026-11-16. Scope: record the actual approved Proposal/Requirements R2 and prepare Design R2 at Gate 2, with no implementation or remote changes.

- [Design R2](../../../../specs/changes/harness-publication-blockers/design.md), awaiting approval.
- [Proposal R2 approval](../../../../specs/changes/harness-publication-blockers/proposal.md), same approved combined digest.
- [Planning diagnostics](planning.json): exit 1, two missing downstream approvals, one retained check failure, two stale input results and six open acceptance findings; no schema/reference/coverage errors.
- [Required suite result](suite-result.json), [stdout](suite.stdout), [stderr](suite.stderr): Plugin validation passed; 131 validator and 48 execution tests passed. Aggregate remains failed because the retained dossier is not ready for execution/delivery. Existing legacy/v2 inventory warnings remain.
- [Local review record](local-review.json) and [entry inventory](source-before.json).
- Exact entry copies: [Proposal](before/proposal.md.txt), [Requirements](before/requirements.md.txt), [Design](before/design.md.txt), [Tasks](before/tasks.md.txt), [handoff](before/handoff.md.txt). These are raw evidence copies; relative references retain their original file context. They are not duplicate active/archive dossiers.

The restored temporary environment uses Python 3.11.4 and repository-pinned PyYAML 6.0.2/jsonschema 4.23.0. No dependency declaration, validator, test, exception manifest, canonical Standard, license or runtime behavior changed. No client rehearsal, synthetic PR, workflow, message, GitHub mutation or publication was executed. No result was relabelled from R1 to R2.

The handoff's status notice is updated only to avoid presenting the superseded R1 procedure as current authority. Its operational content and existing task/acceptance ledger await later approved implementation. All old frozen `replan-r2` evidence remains unchanged. This packet is local planning evidence, not service enforcement or a new rights/exposure clearance.
