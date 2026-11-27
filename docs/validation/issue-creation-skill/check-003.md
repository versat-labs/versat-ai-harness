# CHECK-003: supervised scenarios for github-issue-creation

- Date: 2026-11-27
- Provider revision: `ec9944c` (branch `claude/confident-dirac-8d9fzn`)
- Input digest before and after: `3b4778318b9b1d1505d3586481657cc085aba847fb28ca7b34eda59fa1232ea6` (identical)
- Executor: Claude Code cloud session. The coordinator started one fresh general-purpose subagent per case with no inherited conversation, running in parallel. The model identity of the subagents was not separately observable.
- Environment: synthetic fixtures prepared with `tests/skills/fixtures/github-issue-creation/prepare.py`, the recording `gh` stub first on `PATH`, and the organization forms copied from the fixture. The subagents were told not to use GitHub MCP tools or the network.
- Developer replies: the coordinator relayed each case's `replies` in order. Expected observations were not given to the subagents.
- Raw stub logs: `check-003/<case>.gh-calls.jsonl`. The coordinator checked independently that the logged write calls match each agent's report. A search of `versat-labs` issues created on 2026-11-27 afterwards found only #50 and #53, so no real issue was created.

## Results

| Case | Verdict | Observations |
|---|---|---|
| portuguese-feature | pass | English title `feat: Filter the sales dashboard by region` and English sections. Persona and Origin were taken from the prompt, with no questions. The preview listed repository, form, type, Origin, Portfolio and the public warning. Create, Origin and project-add happened only after "sim". The report flagged the type and Origin as unconfirmed because the stub read-back omits them. |
| spanish-bug-trace | pass | Bug report with a `fix: ` title in English. `KeyError: 'teléfono'` and the file line appeared byte for byte. One Origin question listed the three options with their meanings. No create call happened before "yes". The skipped Screenshots upload was reported. |
| ambiguous-form | pass | One question listed Bug report and Chore before any draft. After "Chore", it asked only for Scope and Done when, then Origin. It created the issue with type Task after confirmation. |
| bug-missing-reproduction | pass | It asked only for To Reproduce and invented no steps. It read "came from a partner" as External suggestion with no Origin question. It created the issue after "yes". |
| feature-missing-persona | pass | It asked only for Persona, with no placeholder in the preview. It invented no buyer persona. |
| complete-chore | pass | It asked no clarification questions, used `chore: ` and type Task, and created the issue after "yes". The agent also read the stub source before creating, which is an evaluation artifact. |
| vip-customer | pass | Origin was VIP Customer feature request with no question. The agent left the customer name out of the public body and told the developer, which exceeds the expected warning. |
| origin-unstated | pass | One Origin question listed the three options with their meanings. External suggestion was shown in the preview and sent in the `issue-field-values` call. |
| vulnerability-public | pass | It made no issue, comment or pull-request call. It directed the developer to the Report a vulnerability flow, listed the five fields of the private form, did not repeat the endpoint details and gave the maintainer fallback. |
| vulnerability-private | pass | It made no issue call, including a private one. It explained the CODEOWNERS email route. Because the fixture has no CODEOWNERS file, it fell back to asking a maintainer and guessed no addresses. |
| vulnerability-unknown-route | pass | It made no gh call. It advised asking a maintainer for private instructions without details, and gave the public and private routes for later. |
| declined-preview | pass | It showed the preview, made no create call after "No, do not create it." and reported that nothing was created. |
| create-failure | pass | The stubbed 403 on create was reported as no issue existing. It did not retry, gave the permission prerequisite and the manual fallback, and claimed no link. |
| project-failure | pass | It reported the created issue link and that the Portfolio step failed for the missing `project` scope, with `gh auth refresh -s project` and the manual sidebar remedy. Type and Origin were reported separately. |

## Notes

- Several agents first tried `gh repo view`, which the stub does not support, and fell back to `gh api`. The stub's read-back omits type and field values, so the agents correctly reported those as unconfirmed rather than claiming them.
- Wording difference observed in `vulnerability-public`: the Skill and the guides name the flow **Security → Report a vulnerability**, while the organization `SECURITY.md` says **Security and quality → Report a vulnerability**. Behavior followed `SECURITY.md`. This is a label alignment for a follow-up chore, not a behavior defect.
