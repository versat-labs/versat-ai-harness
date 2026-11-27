---
sdd_version: 3
change: retire-branch-administration-ruleset
requirements:
  - id: REQ-001
    statement: Stop prescribing, rendering or requiring the universal administrator-only branch rule for public GitHub repositories.
    acceptance:
      - Fresh bootstrap assets omit branch-administration.json and still include tag administration and independent main protection.
      - The indexed policy and schema accept the revised tag-only reference baseline. Audit and maintenance follow that baseline and do not report the removed branch rule as missing or propose recreating it.
      - Current operator and translated user instructions that describe this rule reflect ordinary upstream branch permissions and mandatory PRs on main. Bootstrap continues to consume shared policy.
  - id: REQ-002
    statement: Remove verified copies of this branch rule while keeping main protected by mandatory pull requests.
    acceptance:
      - Before each deletion, identify the repository-owned all-branches rule by ID and contents and confirm a separate active PR requirement on main. Any inaccessible or materially different configuration is recorded for that target.
      - After deletion, a fresh GitHub settings read shows the targeted ID absent, the independent main protection still effective, and the existing tag protection and required checks preserved. Record the outcome separately for each repository.
      - Repeated inventory of a repository where the rule has already been removed requires no further write. Leave unrelated branch rules, inherited rules, refs, permissions and workflows intact.
---

# Requirements

Administrators perform the scoped removal. Collaborators use their existing GitHub permissions on ordinary branches and GitHub's normal merge action on qualifying PRs. Public contributors retain the fork-to-PR path. Settings readback supplies the operational record without performing a test merge, push or branch deletion.
