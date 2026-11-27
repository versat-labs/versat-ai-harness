# Issue creation fixtures

Synthetic inputs for `test_github_issue_creation.py` and the supervised cases.

- `organization/` copies the default issue forms of `versat-labs/.github` observed on 2026-11-27. Refresh the copies when those forms change.
- `repository/` holds a synthetic repository-specific form to test precedence.
- `empty-repository/` has no forms, so the organization defaults apply.
