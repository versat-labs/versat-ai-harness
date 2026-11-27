# Create a GitHub issue

[English](issue-creation.md) | [Português](issue-creation.pt.md) | [Español](issue-creation.es.md)

Use the `github-issue-creation` Skill to turn an idea or a detected problem into a complete GitHub issue in a `versat-labs` repository. You can describe it in English, Portuguese or Spanish; the issue is always written in English.

## Prerequisites

- The Harness Plugin installed and the target repository checked out, with its `origin` remote in `versat-labs`.
- GitHub access from your agent, either a GitHub MCP server or the GitHub CLI authenticated with `gh auth login`.
- Push access to the repository, which is needed to set the "Origin" issue field.
- For the GitHub CLI, the `project` scope to add issues to the organization's "Portfolio" project: `gh auth refresh -s project`.
- Python with PyYAML, as in the Harness `requirements-validation.txt`.

## Try it

```text
Use $github-issue-creation to open an issue: exporting the monthly report to CSV fails with a timeout when it has more than 10,000 rows. It should finish in under a minute.
```

## What happens

1. The Skill reads the repository's own issue forms, or the organization defaults from `versat-labs/.github`: Bug report, Feature request and Chore.
2. It picks the form. If your intent fits more than one form, it asks which one you mean.
3. It drafts the title and fields in English, keeping code, commands and error output exactly as you wrote them.
4. It asks, in one message, for any required field it could not fill, such as reproduction steps for a bug or the persona for a feature.
5. It asks for "Origin" unless you already said it: **Internal Idea**, for a codeowner or Versat team member; **External suggestion**, for an external contributor, customer or partner; or **VIP Customer feature request**, for a VIP customer who pays for development.
6. It shows a preview with the repository, form, title, body, type, Origin and the "Portfolio" project. Nothing is created until you confirm. Issues in a public repository are public, so remove customer names or other sensitive details before confirming.
7. It creates the issue, sets its type and Origin, adds it to "Portfolio" and reports the link and the result of each step.

## Results and failures

The Skill reports only what GitHub confirmed. When a step after creation fails, such as a missing `project` scope, you receive the issue link and instructions to finish that step in the issue sidebar. When creation itself fails, no issue exists and the Skill names the missing prerequisite. It never retries creation on its own, to avoid duplicates.

The Skill does not attach files. Add screenshots on GitHub after creation.

## Security vulnerabilities

Do not report a suspected vulnerability as an issue. When your description looks like one, the Skill creates nothing and points you to the private route in the [security reporting guidance](https://github.com/versat-labs/.github/blob/main/SECURITY.md):

- In a public repository, use **Security → Report a vulnerability**.
- In a private repository, email the relevant CODEOWNERS through existing internal Versat channels.
- When the route is unavailable, ask a maintainer for private instructions without sharing details.
