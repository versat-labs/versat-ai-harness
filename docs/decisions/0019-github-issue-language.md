# ADR-0019 — Use English for GitHub issue definitions

- Status: Accepted
- Refines: [ADR-0010](0010-refine-language-policy.md), for GitHub issues
- Tracking: [Feature request #50](https://github.com/versat-labs/versat-ai-harness/issues/50)

## Context

ADR-0010 groups internal issues and pull requests under Spanish. An issue also helps an external developer decide whether to contribute. A developer who can read the technical guide in English should be able to read the problem and determine when the work is complete.

## Decision

Use English by default for the GitHub issue title and authored description, including answers entered through issue forms. Team members may use Spanish for discussion in comments. When they agree to change the scope or acceptance criteria, a maintainer records the decision in the English description. Identifiers and quoted diagnostics keep their original spelling.

The issue-specific refinement applies when creating an issue or substantively revising its definition. ADR-0010 continues to govern its other artifact classes, including internal pull requests. The [Language Standard](../../standards/core/language.md#github-issues) defines the authoring rule.

## Consequences

Contributors can assess the work from the title and description. Maintainers carry decisions back into the description, while routine conversation requires no translation. Adoption adds a review convention for new and revised issue definitions. It requires no GitHub integration or bulk edit of the backlog.
