---
sdd_version: 3
change: issue-creation-skill
requirements:
  - id: REQ-001
    statement: The Skill writes the title and description of every issue it creates in English, whatever the language of the developer's prompt.
    acceptance:
      - A developer who describes a feature in Portuguese or Spanish receives a preview and a created issue whose title and form responses are in English.
      - Identifiers, commands and verbatim diagnostic output in the prompt keep their original spelling in the issue.
  - id: REQ-002
    statement: The Skill selects the issue form from the forms that currently apply to the target repository, namely its own forms when it defines them and otherwise the organization defaults in `versat-labs/.github`, and asks the developer to choose when the prompt does not make the intent clear.
    acceptance:
      - A prompt that describes broken behavior with observed and expected results leads to the Bug report form without a question about the form.
      - A prompt that could be either a new capability or maintenance work leads to one question listing the candidate forms before any draft is shown.
      - "In a repository without its own forms, the created issue uses the organization form's title prefix, issue type and field labels as section headings, such as the `feat: ` prefix with type Feature and the Problem, Job To Be Done and Persona sections."
      - In a repository that defines its own forms, the Skill offers those forms instead of the organization defaults.
  - id: REQ-003
    statement: The Skill asks for every required field of the selected form that it cannot fill from the prompt, and does not invent missing facts.
    acceptance:
      - When a bug prompt omits the reproduction steps that the form requires, the Skill asks for them before it shows the preview.
      - When a feature prompt does not identify who needs the feature, the Skill asks for the Persona before it shows the preview.
      - When the prompt already supplies every required field, the Skill asks no question about those fields.
      - The preview shows no placeholder or guessed value for a required field.
  - id: REQ-004
    statement: The Skill sets the organization's "Origin" issue field on every created issue, asking the developer to choose between "Internal Idea", "External suggestion" and "VIP Customer feature request" unless the prompt already states which one applies.
    acceptance:
      - Without an explicit origin in the prompt, the Skill asks one question that lists the three options with their meanings, namely an idea from a codeowner or Versat team member, a suggestion from an external contributor, customer or partner, and a request from a VIP customer who pays for development.
      - A prompt stating that a paying VIP customer requested the feature results in "VIP Customer feature request" being shown in the preview and set on the created issue.
  - id: REQ-005
    statement: The Skill adds every created issue to the "Portfolio" project of the `versat-labs` organization, which the organization's issue forms reference as `versat-labs/1`.
    acceptance:
      - After creation through the API, the issue appears as an item of the "Portfolio" project even though GitHub does not apply the form's `projects` key outside the web form.
      - When the project cannot be found or the developer lacks permission, the Skill reports the created issue's link and that the project link failed, with the reason and the manual remedy.
  - id: REQ-006
    statement: When the developer reports a suspected security vulnerability, the Skill creates no issue and directs the developer to the private route that applies to the target repository.
    acceptance:
      - In a public repository, the Skill creates no issue and directs the developer to the repository's Report a vulnerability flow, listing the information its private form requires.
      - In a private repository, the Skill creates no issue, including a private one, and directs the developer to email the relevant CODEOWNERS through existing internal Versat channels without guessing addresses.
      - When the route is unavailable or unclear, the Skill gives the safe fallback of asking a maintainer for private instructions and does not place vulnerability details in any issue, comment or pull request.
  - id: REQ-007
    statement: The Skill creates the issue only after the developer confirms a preview, then reports the actual result of each step.
    acceptance:
      - The preview shows the repository, form, title, body, issue type, "Origin" and the "Portfolio" project. Declining or requesting changes creates nothing.
      - After confirmation, the Skill reports the issue link and whether the type, "Origin" and project link were applied, based on what GitHub returned.
      - When creation itself fails, for example from missing authentication or permission, the Skill reports the failure and the prerequisite to fix, and does not claim that an issue exists.
  - id: REQ-008
    statement: The Skill is packaged and documented so that any `versat-labs` collaborator using the Harness can run it.
    acceptance:
      - The Skill lives at `skills/<skill-name>/SKILL.md`, defines when to use it, its inputs, result and failure conditions, and resolves policy through `standards/index.yaml` without copying it.
      - A collaborator can find the prerequisites, such as GitHub access and the permissions needed for projects and issue fields, and an example prompt in the maintained documentation.
      - "`./scripts/validate/run.sh` passes with the Skill in place."
---

# Requirements for the issue creation Skill

## Actors and context

- **Developer:** any `versat-labs` collaborator running the Harness in a target repository. They describe an idea or problem and answer the Skill's questions.
- **Skill:** reads the target repository's issue forms and the organization's issue settings, drafts the issue and creates it on GitHub after confirmation.
- **GitHub:** hosts the issue forms, issue types, the "Origin" issue field and the "Portfolio" project.

## Functional requirements

REQ-001 to REQ-007 define the observable behavior: English content, form selection, clarification, "Origin", "Portfolio", vulnerability handling, and confirmation with truthful reporting.

## Non-functional requirements

REQ-008 covers packaging and documentation. The Skill keeps a short dialogue and asks only questions whose answers change the issue. It reads forms, options and the project at run time so that their changes do not require a Skill release.

## Acceptance scenarios

The scenarios are listed under each requirement in the frontmatter.

## Constraints and assumptions

- **Facts:** the organization's default forms live in `versat-labs/.github`, as recorded in the Proposal's current contract baseline. This repository defines no forms of its own. "Report a security vulnerability" is the private reporting flow, not an issue form. The organization defines the issue types Task, Bug, Feature, Epic and OKR, and a single-select "Origin" field with exactly the three options in REQ-004.
- **Assumption:** the project `versat-labs/1` that the forms reference is the "Portfolio" project. Design will confirm this.
- **Assumption:** the target repository is the one the developer is working in, within `versat-labs`. Creating issues in another organization is not supported.
- **Assumption:** the developer has GitHub access with permission to create issues, write the "Origin" field and add items to the "Portfolio" project. Design will determine the exact tooling and token scopes.
- **Assumption:** confirming the preview is the explicit authorization to publish the issue. It authorizes nothing else.
