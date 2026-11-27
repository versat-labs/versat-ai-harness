---
name: github-issue-creation
description: Draft and create a complete English GitHub issue in a versat-labs repository from a developer's idea or problem description, selecting the issue form, asking only for missing required information and Origin, linking the Portfolio project, and routing suspected vulnerabilities to private reporting. Use when a developer asks to open, file or create an issue, bug report, feature request or chore.
---

# GitHub issue creation

## When to use

Use this Skill when a developer wants to turn an idea or a detected problem into a GitHub issue in a repository owned by the `versat-labs` organization. The developer can write the request in any language. Do not use it to edit, triage, close or search existing issues, or to change issue forms, fields or projects.

## Inputs

- The developer's prompt, describing the idea or problem.
- The current repository, identified from its Git `origin` remote.
- The issue forms that apply to that repository, read at run time.
- The organization's "Origin" issue field and "Portfolio" project, read at run time.

## Result

Either an issue link with the actual status of its type, Origin and Portfolio membership, or, for a suspected vulnerability, private-reporting instructions with no issue created.

## Prerequisites

- GitHub access from the executor, either through a GitHub MCP server or an authenticated GitHub CLI (`gh auth status`).
- Push access to the repository, which is needed to set issue field values.
- For organization projects with the CLI, the `project` scope (`gh auth refresh -s project`).
- Python with PyYAML, as listed in the Harness `requirements-validation.txt`, to run `scripts/issue_form.py`.

## Procedure

The Harness root is two directories above this file. `scripts/issue_form.py` below is relative to this Skill's directory.

### 1. Resolve context

1. Read the target repository's `AGENTS.md` when present.
2. Resolve the applicable Standards through `standards/index.yaml`. Apply the Language Standard for issue content, the Contribution Standard for the use of the repository's actual issue forms and the Security Standard for confidential reporting. Do not restate their policy to the developer beyond what the step needs.
3. Identify the repository owner and name from `git remote get-url origin`. Stop and explain if the owner is not `versat-labs`.
4. Obtain the organization defaults from the public `versat-labs/.github` repository at its default branch, for example with `git clone --depth 1 https://github.com/versat-labs/.github <temporary directory>`.
5. Run `python scripts/issue_form.py resolve --repo-dir <repository root> --org-dir <organization clone>`. The repository's own forms take precedence. If the source is `none`, stop and report that no issue forms are available.

### 2. Detect a suspected vulnerability first

If the prompt describes a suspected security vulnerability, such as an exploitable flaw, exposed credential, authentication bypass or data exposure, create nothing and go to step 7. When it is unclear whether the problem is a security issue, ask before drafting anything.

### 3. Select the form

Match the intent to one resolved form. For the organization defaults:

- **Bug report:** existing behavior that is broken or differs from what is expected.
- **Feature request:** a new capability or idea for users.
- **Chore:** technical maintenance with no new user-facing behavior.

Without asking, pick the form when exactly one fits. When more than one fits, ask one question listing the candidate forms with a short reason for each, and wait for the answer before drafting.

### 4. Draft in English

Write the title and every answer in English, whatever language the prompt uses. Keep identifiers, file paths, commands, code blocks, log lines and other verbatim diagnostics exactly as given. Use only facts from the prompt, the developer's answers and the repository. Never invent reproduction steps, personas, scope or results. Do not include the form's title prefix in the drafted title; the helper adds it.

Write the answers to a temporary JSON file keyed by the form's field IDs, as listed by `resolve`.

### 5. Clarify missing information and Origin

1. Run `python scripts/issue_form.py missing --form <form file> --answers <answers file>`. Ask for every listed field in one message, naming each field and what it needs. Repeat until nothing is missing. Do not ask about fields the prompt already answers.
2. Read the "Origin" field and its options from the organization's issue fields, for example with `gh api /orgs/versat-labs/issue-fields`. If the prompt states the origin explicitly, use it. Otherwise ask one question listing each option with its meaning:
   - **Internal Idea:** an idea from a repository codeowner or a Versat team member.
   - **External suggestion:** a suggestion from an external contributor, customer or partner.
   - **VIP Customer feature request:** a request from a VIP customer who pays for development.

   If the organization's options differ from this list, present the current options and report the difference.

### 6. Preview, confirm and create

1. Run `python scripts/issue_form.py render --form <form file> --answers <answers file> --title "<title>"`. Relay any notices, such as skipped upload fields.
2. Show the preview: repository, form, title, body, issue type, Origin and the "Portfolio" project. Mention that issues in a public repository are publicly visible, so the developer can remove customer names or other sensitive details.
3. Ask for explicit confirmation. On requested changes, revise and preview again. On a decline, stop and create nothing. Confirmation authorizes this single issue only.
4. Create the issue with its title, body and type. For example, use the MCP `issue_write` tool with `type` and `issue_fields`, or `gh api --method POST /repos/<owner>/<repo>/issues` with `title`, `body` and `type`.
5. Set "Origin" if creation did not already set it, for example with `gh api --method POST /repos/<owner>/<repo>/issues/<number>/issue-field-values` and an `issue_field_values` entry holding the field ID and the option name.
6. Find the organization project titled "Portfolio", for example with `gh project list --owner versat-labs --format json`, and add the issue with `gh project item-add <number> --owner versat-labs --url <issue URL>`. If that project's number differs from the form's `projects` value, include the difference in the report.
7. Read the issue back and report the link and the actual status of the type, Origin and Portfolio membership.

### 7. Route a suspected vulnerability privately

Do not create an issue, comment or pull request, public or private. Do not repeat the vulnerability details beyond what is needed. Follow the target repository's `SECURITY.md`, or the organization's `SECURITY.md` when the repository has none:

- **Public repository:** direct the developer to the repository's **Security → Report a vulnerability** flow and list the information its private form asks for. When the repository has its own form, use that form's fields. Otherwise use the fields of the organization's `.github/VULNERABILITY_REPORT.yml`.
- **Private repository:** direct the developer to email the relevant CODEOWNERS of the affected paths through existing internal Versat channels. Never guess email addresses from GitHub usernames.
- **Unavailable or unclear route:** tell the developer to ask a maintainer for private reporting instructions without disclosing details.

## Failure conditions

Report each failure with its reason and a manual remedy, and never claim a step that GitHub did not confirm.

- **Missing authentication or push access:** report that no issue was created and name the prerequisite.
- **Creation failed:** report that no issue exists. Do not retry automatically, to avoid duplicates.
- **Type, Origin or project step failed after creation:** report the issue link, the failed step and how to complete it in the issue sidebar.
- **"Portfolio" not found or the `project` scope missing:** report the issue link and ask the developer to add the issue to the project manually or refresh the scope.
- **Forms or Origin field unavailable:** stop before creating anything and report what could not be read.
- **Repository outside `versat-labs`:** stop without creating anything.
