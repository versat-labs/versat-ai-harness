---
sdd_version: 3
change: english-issue-definitions
requirements:
  - id: REQ-001
    statement: English is the default language for the title and authored description of GitHub issues.
    acceptance:
      - A maintainer filing a feature writes its title, problem, expected outcome and any acceptance criteria in English, including text entered through issue forms.
      - A contributor filing a bug writes the title, reproduction steps and expected and observed behavior in English. Identifiers and verbatim diagnostic output can retain their original spelling.
      - A reviewer of an English-titled issue with a Spanish description can cite the standard to request an English description.
  - id: REQ-002
    statement: Team members may use Spanish in issue discussion comments. The issue description communicates the current definition in English.
    acceptance:
      - A teammate may ask or answer an implementation question in Spanish in a comment. A routine discussion requires no parallel translation.
      - When a discussion in Spanish changes scope or acceptance criteria, a maintainer updates the English issue description so a contributor can discover the decision there.
  - id: REQ-003
    statement: Maintained repository instructions agree with the canonical issue policy and retain the existing language rule for internal pull requests.
    acceptance:
      - A maintainer consulting the Language Standard and root agent instructions finds the same distinction between issue definitions and team discussion comments.
      - A maintainer preparing an internal pull request finds Spanish still prescribed for that artifact and its template still in Spanish.
---

# Requirements for issue authoring

## Actors and context

External contributors use the title and description to decide whether to take on an issue. Issue authors and maintainers keep those fields current. Teammates can choose English or Spanish when discussing the work in issue comments.

## Constraints and assumptions

The rule covers existing fields when applicable. An issue type gains no new mandatory fields. This proposal assumes prospective adoption for newly filed or substantively revised definitions, with no bulk migration of historical issues or comments.
