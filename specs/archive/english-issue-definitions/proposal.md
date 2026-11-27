---
sdd_version: 3
change: english-issue-definitions
status: accepted
owner: versat
summary: Make English the default for GitHub issue definitions and allow Spanish in team discussion comments.
risk: low
impact:
  state: assessed
  summary: The current standard groups issues with pull requests and assigns Spanish to collaborator discussions. The proposal changes the authoring rule for issues and preserves the internal pull request rule.
  items:
    - current_contract: &language
        path: standards/core/language.md
        locator: "## Required language by artifact"
        digest: a287cabaf0609331541afd18cc1b3f3d1aead42642446263fe44bc3bc9100f3f
      effect: supersede
      targets: [REQ-001, REQ-003]
      reason: External contributors need the same working language for an issue definition as for technical documentation.
    - current_contract: *language
      effect: extend
      targets: [REQ-002]
      reason: Explicitly permit Spanish discussion in issue comments while keeping decisions that define the work accessible in English.
    - source:
        change: align-language-standard
        requirement: REQ-002
        scenarios: [1]
        requirements_digest: cdc97969d81fcdebe2e470e01d4bec5299f1aae1fef041c41ea2e658a93d50e3
      current_contract: *language
      effect: preserve
      targets: [REQ-003]
      reason: Internal pull requests retain their Spanish authoring rule and template.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply in the Codex chat after presentation of Proposal and Requirements revision 1 for GitHub issue 50.
    quote: "Aprovo a revisão 1 da proposta e dos requisitos da issue #50. Pode avançar para o Design."
    revision: 1
    digest: 047103f7a943df216c9c21f3bede9e777bf9c6ea6f12ea45ccfc29abf4e68f49
---

# English for GitHub issue definitions

## Context and expected outcome

An external developer can read Versat's technical documentation in English and still need a translation to decide whether to pick up a related issue. The current [Language Standard](../../../standards/core/language.md) assigns Spanish to internal issues and pull requests. [ADR-0010](../../../docs/decisions/0010-refine-language-policy.md) records that choice, and the root [agent instructions](../../../AGENTS.md) repeat it.

Contributors should be able to read the issue title and description in English to understand the problem, intended outcome and criteria for completion. Teammates can use Spanish for discussion in issue comments.

## Scope and boundaries

Cover GitHub issue titles and authored descriptions, including issue-form responses and later edits to the definition. Align maintained instructions that state the issue language rule and trace the change to ADR-0010. The existing rules for internal pull requests, other corporate communications and community documentation stay in force.

The proposal applies to new issues and substantive edits after adoption. Bulk translation of the backlog, language-detection automation and changes to external repositories are outside this change.

## Work tracking

[GitHub feature request #50](https://github.com/versat-labs/versat-ai-harness/issues/50) tracks this change. No Shortcut Story is associated.

## Impact and risks

If a decision lives only in a Spanish discussion, contributors may implement the original scope. The maintainer who revises the scope captures that decision in the English description. Routine conversational comments need no translation. Separating the issue and pull request rules also avoids inadvertently changing the language of internal pull requests.

## Proposal acceptance criterion

A contributor following the maintained guidance can write or update the issue in English, identify when Spanish is appropriate for a team comment, and locate the agreed definition after a discussion.

## Planning review

The developer approved Proposal and Requirements revision 1 together and authorized Design.
