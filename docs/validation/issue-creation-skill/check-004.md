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
