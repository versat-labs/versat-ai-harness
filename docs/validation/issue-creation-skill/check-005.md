# CHECK-005: Skill contract and guide review

- Date: 2026-11-27
- Provider revision: `ec9944c`. Input digest before and after: `53721c8113587711d28cdf3f9866e0c9dcd4650ef6501f37c232eba8955fd6fa` (identical).
- Reviewer: Claude Code session coordinator. This is an agent review, and human review in the PR remains required.

## Observations

- **`SKILL.md` frontmatter:** declares `name: github-issue-creation` and a description with trigger phrases.
- **`SKILL.md` sections:** When to use, Inputs, Result, Prerequisites, Procedure and Failure conditions.
- **Policy references:** language, contribution and security policy are located through `standards/index.yaml` and the repository or organization `SECURITY.md`. Neither the policy text nor the form content is copied.
- **Origin options:** the three names and their meanings are listed because GitHub stores no option descriptions. The procedure reads the current options at run time and reports any difference. Every supervised run confirmed the field and options at run time.
- **Guide structure:** `issue-creation.md`, `.pt.md` and `.es.md` have the same five sections and the same language switcher.
- **Guide content:** each guide contains the same prerequisites, including GitHub access, push access, the `project` scope with `gh auth refresh -s project`, and PyYAML. Each also has an example prompt, the seven-step dialogue, the results and failures, the absence of attachments, and the three vulnerability routes. The Portuguese and Spanish guides link the matching translated organization `SECURITY` pages.
- **README links:** the guides are linked from `README.md`, `README.pt.md` and `README.es.md`.
- **Known wording difference:** the Skill and the guides say "Security → Report a vulnerability", while the organization `SECURITY.md` says "Security and quality → Report a vulnerability". This is tracked as follow-up chore [#56](https://github.com/versat-labs/versat-ai-harness/issues/56), which replaces the deleted #54. It does not change the route or the behavior.

## Result

**pass.**
