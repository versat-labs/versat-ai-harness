# CHECK-004: live issue creation

- Date: 2026-11-27
- Provider revision: `ec9944c`. Input digest before and after: `d12c660b55ff9bce468f2256a6eacd787501b61e61933adcd86815ba06e45e20` (identical).
- Authorization: the developer authorized the live issue and, after the Skill's Origin question and preview, answered "Origin: Internal Idea: Pode criar a Issue."
- Executor: Claude Code cloud session. GitHub access was the GitHub MCP server only. The session's `gh` was limited to search, and no projects tool was available.

## Procedure and observations

1. The Skill was followed in `versat-labs/versat-ai-harness`. `issue_form.py resolve` against `versat-labs/.github` at `4e01b6e` returned source `organization`. The Chore form had prefix `chore: `, type Task and projects `versat-labs/1`. `missing` returned `[]`, and `render` returned no notices.
2. The preview was shown with the Origin question and the public-visibility notice.
3. After confirmation, MCP `issue_write` created [#54](https://github.com/versat-labs/versat-ai-harness/issues/54) with type Task and Origin `Internal Idea`.
4. The read-back through MCP `issue_read` showed:
   - title `chore: Align the vulnerability reporting label in the issue creation Skill`;
   - `issue_type: Task`;
   - `field_values: [{field: Origin, value: Internal Idea}]`;
   - Description, Scope and Done when sections.
5. The Portfolio step was **not performed**, because the executor had no tool to add items to organization projects. The developer was told so and given the manual remedy.
6. The developer then reported: "Adicionei agora o projeto manualmente. Sim é o projeto 1." This confirms that the organization project number 1, which the forms reference, is "Portfolio", and that #54 was not in it until the manual addition.

## Result

**unverified.** Title prefix, type, body sections, Origin and the reported link match expectations. The Skill's own addition of the issue to "Portfolio" (REQ-005 scenario 1) was not exercised, because this executor lacks a projects capability. It must be rerun with the GitHub CLI holding the `project` scope, or with an MCP server that exposes projects.

## Later note on attempt 1

On 2026-11-27, after attempt 2, the developer deleted issue #54. Its content was recreated as [#56](https://github.com/versat-labs/versat-ai-harness/issues/56) through the GitHub MCP server, with the same title, body, type Task and Origin Internal Idea. The observations recorded for #54 above are retained as they were made.

## Attempt 2: developer's computer with the GitHub CLI

- Date: 2026-11-27
- Executor: the developer's local agent with the Harness checked out at branch `claude/confident-dirac-8d9fzn`. The agent product and model were not reported. The agent used GitHub CLI `gh version 2.94.0 (2026-06-10)` with the `project` scope added through `gh auth refresh -s project`.
- Input digest before and after, run by the developer: `d12c660b55ff9bce468f2256a6eacd787501b61e61933adcd86815ba06e45e20` (identical, and equal to attempt 1).
- Prompt: a real chore asking to support `gh repo view` in the evaluation stub, with Origin Internal Idea. The developer confirmed the preview.
- Skill report: "I created the issue: versat-labs/versat-ai-harness#55. I read it back from GitHub, and everything was set". It reported Type Task, Origin Internal Idea and Project Portfolio (number 1, which matches the form's `versat-labs/1`).
- Developer verification output, from screenshots shared in the chat:
  - `gh api repos/versat-labs/versat-ai-harness/issues/55 --jq '{title, type: .type.name}'` returned title `chore: support \`gh repo view\` in the issue creation evaluation stub` and type `Task`.
  - `gh api repos/versat-labs/versat-ai-harness/issues/55/issue-field-values` returned Origin (`issue_field_id` 48813453) with `single_select_option.name` `Internal Idea`.
  - `gh issue view 55 --repo versat-labs/versat-ai-harness --json projectItems` returned one item titled `Portfolio` with status `Todo`.
- Coordinator verification: MCP `issue_read` of [#55](https://github.com/versat-labs/versat-ai-harness/issues/55) confirmed the title, `issue_type: Task`, Origin `Internal Idea` and the Description, Scope and Done when sections in English.

## Result

**pass.** The Skill created the issue with the form's prefix, type and sections, set Origin, and added the issue to "Portfolio" itself. That project is `versat-labs/1`. Attempt 1 remains recorded above as unverified.
