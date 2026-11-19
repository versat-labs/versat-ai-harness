# Implement change

Use when the developer has explicitly authorized implementation of the current reviewed plan. Read the [process](../process.md), [metadata](../metadata.md) and the four artifacts before executing tasks.

## Entry checks

Confirm the accepted outcome still matches the request and current repository. Verify all three planning approvals, upstream digests, required ADRs and absence of material blockers. Run the SDD validator with `--change <change-id> --phase implementation`. Legacy exemption or missing approval is not execution readiness; report the missing review/migration and route to [New change](new-change.md).

Apply the resolved Standards, including Git workflow and work tracking. Preserve unrelated work. An approved plan permits only its scope; publication, merge and deployment remain subject to the actual authorization and platform policies.

## Execute and maintain coherence

1. Implement tasks in reviewable increments, including tests, evals, migrations and operational assets actually required by the profile and approved design.
2. Keep task metadata and rendered checkboxes consistent: mark completed only when the task's completion check is met. Record blockers truthfully; use the Progress section for execution notes rather than changing the approved task descriptions to match partial work.
3. Update living product and architecture specifications and affected usage instructions/examples alongside the implemented behavior on the branch. Apply the resolved [Documentation Standard](../../standards/core/documentation.md) for reader context, guide creation and discovery, and applicable locales, using the existing task completion conditions. Preserve the original intent and decision history. Do not defer these updates until after merge.
4. Run appropriate development checks and preserve actual results at stable evidence locations. For v3, capture the check input digest immediately before and after actual execution, with runtime/service context. Maintain regression tests in normal suites, outside historical dossiers. Never update an old result with a newly computed hash. After implementation changes, rerun affected checks; do not reuse an old pass solely because the planning digest is unchanged.
5. If material scope/design/task-plan changes become necessary, reopen the earliest affected gate using the process. Mark dependent approvals/evidence stale and stop dependent execution until the revised artifacts are accepted. Routine fixes inside the approved approach can proceed under existing implementation authority.

## Exit and next action

Report completed tasks, remaining work, changed living specifications and actual checks. Distinguish implementation complete from delivery-ready and merged. If validation was also authorized, read and follow [Validate change](validate-change.md). Otherwise hand off the implementation and identify validation as the next action; do not silently publish, archive or merge.

## Executable project checks

Use the index-resolved Testing Standard to create/update assertions for changed behavior and uncovered retained obligations, or record adequate reuse/manual rationale. Consult [project validation](../../docs/guides/project-validation.md) when adopting or using the explicit executor. Inspect configured commands, run targeted checks while developing and run complete required suites before claiming readiness. Review exported SDD fragments and record actual evidence; do not treat a fragment as task completion or semantic approval. For Harness Skill changes, use [supervised Skill evaluations](../../docs/guides/skill-evaluations.md) where required by the approved plan.
