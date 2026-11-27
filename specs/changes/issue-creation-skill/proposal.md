---
sdd_version: 3
change: issue-creation-skill
status: proposed
owner: versat
summary: Provide a Harness Skill that drafts and creates a complete English GitHub issue from a developer prompt, asking only for what it cannot infer.
risk: medium
impact:
  state: assessed
  summary: No living contract defines agent-assisted issue creation. The new Skill must apply existing contracts without changing them, namely the English issue rule, the use of the repository's actual issue forms, the confidential vulnerability reporting rule and the organization's default issue forms and security guidance captured in the Proposal baseline.
  items:
    - source:
        change: english-issue-definitions
        requirement: REQ-001
        scenarios: [1, 2]
        requirements_digest: 9230d0eb8ff0374ddc9827445fa466f57737362a0c5a6a8f8135a59e5bcfee8d
      current_contract:
        path: standards/core/language.md
        locator: "## GitHub issues"
        digest: 9ac7d50050021daa1c9afb6f3c4fb193a6d597b1fbdaf5f95216cbc70ad630af
      effect: preserve
      targets: [REQ-001]
      reason: Issues the Skill creates follow the existing English rule for titles and descriptions, including issue-form responses.
    - current_contract:
        path: standards/core/contribution.md
        locator: "## Entry and precedence"
        digest: dd1748e2f35b45a79fcff75254b2e56fa56e8a0d0b4dbfb7adfc72020fd26869
      effect: preserve
      targets: [REQ-002, REQ-003]
      reason: The Skill uses the target repository's actual issue forms, with repository-specific forms taking precedence over organization defaults.
    - current_contract:
        path: standards/core/security.md
        locator: "## Confidential vulnerability reporting"
        digest: e854aa3434dcd732e8ffeeae54f97a72a698abe5a97f4cffc053579a42878e0c
      effect: preserve
      targets: [REQ-006]
      reason: Vulnerability details must stay out of public issues, so the Skill routes those reports to the confidential channel.
    - current_contract:
        change: issue-creation-skill
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-002, REQ-003, REQ-005, REQ-006]
      reason: The organization's default issue forms and security reporting guidance in versat-labs/.github define the forms, required fields, title prefixes, issue types, project and vulnerability routes the Skill must follow without changing them.
review:
  revision: 2
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Issue creation Skill

## Context and problem

Writing a GitHub issue by hand takes a developer too long when they have a new idea or have found a problem. They have to pick the correct issue form, fill in every required field in English, add the issue to the "Portfolio" project and set the organization's "Origin" field. Issue [#53](https://github.com/versat-labs/versat-ai-harness/issues/53) records this need.

The Harness has no Skill for this. Existing Skills cover SDD, audits, bootstrap, maintenance, architecture review and SIFEN. The [Language Standard](../../../standards/core/language.md), the [Contribution Standard](../../../standards/core/contribution.md) and the [Security Standard](../../../standards/core/security.md) already set the rules an issue must follow.

## Expected outcome

A developer who collaborates in the `versat-labs` organization describes an idea or problem in a prompt, in any language. The Harness Skill works out which issue form applies. It asks short questions only about missing required information, about the form when the intent is ambiguous, and about the origin. It shows a preview and creates the issue after the developer confirms. The created issue is in English, uses the selected form's structure and type, belongs to the "Portfolio" project and has its "Origin" field set. The Skill reports the issue link and any step that could not be completed.

## Scope

- A new installable Skill in the Harness Plugin under `skills/`, usable from any `versat-labs` repository where the developer has the Harness installed.
- Selection among the issue forms that apply to the target repository: its own forms when it defines them, otherwise the organization defaults Bug report, Feature request and Chore.
- Recognition of a "Report a security vulnerability" intent and routing to the private reporting flow, which is not an issue form.
- Interactive clarification of an ambiguous form, missing required fields and "Origin".
- Creation of the issue with its type, the "Origin" field value and membership in the "Portfolio" project.
- A safe route for security vulnerability reports that keeps details out of public issues.
- Usage documentation, prerequisites and failure conditions.

## Out of scope

- Creating, changing or publishing issue forms, issue types, custom fields or projects.
- Submitting vulnerability reports on the developer's behalf, through Private Vulnerability Reporting or email.
- Attaching files, such as the Bug report's optional screenshots.
- Setting other project fields, such as status, iteration, priority or dates, beyond what the project's own automation does.
- Assigning people, labels, milestones or parent issues.
- Searching for duplicate issues, and editing, triaging, translating or closing existing issues.
- Changes to the language, contribution or security policies.
- Shortcut Story creation.

## Work tracking

[GitHub feature request #53](https://github.com/versat-labs/versat-ai-harness/issues/53) tracks this change. No Shortcut Story is associated. The SDD change ID is `issue-creation-skill`.

## Impact and risks

The impact items in the frontmatter list the contracts the Skill must preserve. No living contract changes.

- **Unsafe disclosure:** a vulnerability report could end up in a public issue. The Skill must detect vulnerability intent and create no public issue in that case.
- **Unintended publication:** creating an issue is outward-facing. The Skill shows a preview and requires explicit confirmation before it creates anything.
- **Invented content:** the Skill could fill required fields with guesses. It must ask instead, and keep the developer's facts separate from its own wording.
- **Partial results:** the issue may be created while the project link or the "Origin" value fails, for example because of missing token scopes. The Skill must report each part's actual result and never claim a complete issue it has not confirmed.
- **Drift:** issue forms, the "Origin" options or the project may change. The Skill must read the current definitions at run time instead of keeping a copy of them.
- **Lost form metadata:** a form's `projects` and `type` keys are applied when an issue is submitted through the web form. An issue created through the API may not receive them, so the Skill must apply the issue type and project itself and confirm the result.

## Current contract baseline

No living specification covers agent-assisted issue creation. Today a developer opens **Issues → New issue** on GitHub, picks a form, writes the content and sets "Origin" in the issue sidebar.

The organization's public [`versat-labs/.github`](https://github.com/versat-labs/.github) repository provides the default issue forms, following GitHub's convention. A repository with its own valid issue forms overrides them. Observed on 2026-11-27 at the default branch:

| Form | File | Title prefix | Issue type | Required fields | Optional fields |
|---|---|---|---|---|---|
| Bug report | `.github/ISSUE_TEMPLATE/bug_report.yaml` | `fix: ` | Bug | Describe the bug, To Reproduce, Expected behavior | Screenshots (upload), Desktop, Smartphone, Additional context |
| Feature request | `.github/ISSUE_TEMPLATE/feature_request.yaml` | `feat: ` | Feature | Problem, Job To Be Done, Persona | Additional context |
| Chore | `.github/ISSUE_TEMPLATE/chore.yaml` | `chore: ` | Task | Description, Scope, Done when | None |

All three forms declare `projects: ["versat-labs/1"]`.

"Report a security vulnerability" is not an issue form. The organization's `SECURITY.md` and `.github/VULNERABILITY_REPORT.yml` define it as follows:

- In a public repository, the reporter uses GitHub's private **Report a vulnerability** flow when Private Vulnerability Reporting is enabled. The private form asks for the affected component and version, a summary, a safe reproduction, the impact and an optional mitigation. A repository-specific form takes precedence.
- In a private repository, the reporter emails the relevant CODEOWNERS through existing internal Versat channels. A private issue does not substitute for this route.
- When the route is unavailable or unclear, the reporter asks a maintainer for private instructions without disclosing details. Vulnerability details never go into an ordinary issue.

## Proposal acceptance criterion

A `versat-labs` collaborator can turn a short idea or problem description into a complete, English, correctly classified issue in the "Portfolio" project with "Origin" set, answering only the questions the Skill cannot resolve from the prompt and the repository.

## Planning review

Revision 1 was presented on 2026-11-27 and was not approved. The developer pointed out that the issue forms are organization defaults in `versat-labs/.github`. Revision 2 records those forms, the vulnerability routes and the need to apply the type and project explicitly. Proposal and Requirements revision 2 are awaiting the developer's review.
