# Git Standard

## Governance

- The default branch MUST be protected.
- Material changes MUST enter through Pull Requests.
- Required checks MUST pass before merge.
- Commits MUST use concise English descriptions and MUST NOT include secrets.
- Generated changes MUST remain reviewable; large mechanical changes SHOULD be isolated.
- Policy and Skill changes MUST identify reviewers through CODEOWNERS or equivalent organization rules.
- Force pushes to protected branches MUST be disabled.

## Branch and worktree cleanup

For public GitHub repositories, apply the mandatory [public repository security contract](#public-github-repository-security) before normal delivery. Cleanup authority does not override its administrator-only reference rules or main protection.

- After a confirmed merge, work branches SHOULD be deleted when no unfinished work or dependent PR needs them. Default, release and other intentionally long-lived branches are excluded. Repository administrators MAY enable automatic deletion of merged PR head branches.
- Remote branches, local branches and worktrees MUST be assessed separately. Deleting a remote branch does not remove a local branch or checkout. Before local cleanup, account for uncommitted changes, unpushed commits, needed ignored files and other users or processes relying on the checkout. Detach or switch an associated worktree before deleting its local branch.
- A suitable active worktree MAY be reused for later work from the appropriate base. When retiring an app-managed worktree, use its supported archive/cleanup mechanism and preserve recoverable work. A merge alone does not require retiring a worktree or closing its chat; preserve worktrees that remain in use, pinned or shared.

## Public GitHub repository security

The index-resolved [public security policy](public-repository-security.yaml) defines the versioned baseline for every profile and criticality. Its values are canonical and MUST be included in exact Standards locks. Public readiness MUST include a fresh, complete live assessment using the version-matched [security verifier](../../validators/security/README.md).

- The canonical default branch MUST exist and accept changes only through PRs with the policy's minimum approval count, required code-owner review, stale-review dismissal and approval of the latest reviewable push by someone other than its pusher.
- Required main protections MUST apply to everyone, including administrators, without user, team, app or other bypass. Force pushes and deletion MUST be blocked. Existing stronger compatible review requirements and required checks MUST be preserved.
- The base-branch CODEOWNERS file MUST cover all files, including itself, with the policy's designated eligible owners. Each MUST have write access or stronger. Either eligible owner's approval satisfies the one-owner baseline; automatic review requests to other owners do not create an all-owners approval requirement.
- Creation, update and deletion of all upstream branches and tags, including future and nested names, MUST be restricted to repository administrators. The administrator exception for reference management MUST NOT bypass the independent main protections.
- External contributors MUST retain a usable public fork-to-PR route without upstream write or merge authority. Administrative credentials MUST NOT be exposed to untrusted fork code.
- Bootstrap MUST distinguish scaffolding and initial reference creation from verified public readiness. Audit MUST report violations and unknowns. Maintenance MUST stage differences, preserve stronger controls and verify authorized remediation. A local/package pass or saved snapshot MUST NOT establish current remote readiness.

Classic protection and active rulesets MAY compose when their effective guarantees are provable. Unsupported or inaccessible settings remain unverified. Repository administrators can edit settings later; an observation is not perpetual assurance. Policy changes remain governed by PR review and exact-version adoption. See [setup, verification and recovery](../../docs/guides/public-repository-security.md).

## Story branch names

New branches associated with a Shortcut Story MUST use:

```text
<shortcut-id>_<story-type>_<description>
```

- `shortcut-id` is the actual numeric Story ID, without `ch` or `#`.
- `story-type` MUST match the Shortcut Story type: `bug`, `feature` or `chore`.
- `description` MUST briefly describe the Story objective in English, with words separated by underscores. Prefer lowercase words.

Examples (illustrative IDs):

```text
305319_bug_score_calculation
305400_feature_date_filter
305500_chore_update_dependencies
```

This format applies to Story work branches, not default, integration or release branches. Work with no associated Story MAY retain the repository's existing branch convention. Contributors MUST NOT invent a Story ID or infer its type from incomplete information; record missing Story context in the proposal or PR and resolve it before presenting the work as Story-linked.

## Commit messages

Commits associated with a Shortcut Story MUST begin with its marker followed by a typed description:

```text
[ch<shortcut-id>] <type>: <description>
```

The initial vocabulary and Story mapping are:

| Shortcut Story type | Commit type | Change |
|---|---|---|
| Feature (`feature`) | `feat` | New functionality |
| Bug (`bug`) | `fix` | Bug correction |
| Chore (`chore`) | `chore` | Maintenance |

Use the type that describes the logical change. The branch type continues to describe the Story; it is not renamed for an individual maintenance commit within a feature Story. Documentation, tests, refactoring and dependency maintenance can use `chore` during initial adoption. Additional types such as `refactor`, `test`, `docs`, `perf`, `revert` and `build` are deferred to a future policy revision.

Descriptions MUST be concise, specific and English, following the [Language Standard](language.md). Start with a base-form action verb, such as `fix`, `add` or `update`, rather than past tense, third-person narration or vague text such as `change`.

```text
[ch305319] fix: prevent division by zero in liquidity calculation
[ch305400] feat: add date filter
[ch305500] chore: update dependencies
```

Commits with no associated Story MUST use the same typed format without a fabricated marker, for example `chore: update Git documentation`.

### Optional scope and body

A scope is optional, never a prerequisite for committing. Prefer the simple form above; when useful, a scope MAY follow the type in parentheses, for example `[ch305319] fix(credit): prevent division by zero`.

A body MAY explain the reason, behavior or validation of the change. Separate it from the subject with a blank line and write it in English:

```text
[ch305319] fix: prevent division by zero in liquidity calculation

The calculation failed when the available balance was zero.
Add a guard and cover the zero-balance case.
```

When a change is breaking, identify it using Conventional Commits `!` syntax or a `BREAKING CHANGE:` footer. Scope and body remain optional; these markers do not introduce another commit type.

## Story, Task, commit and Pull Request traceability

- A Story represents the functional work; a Task is part of that work; a commit is a logical code or repository change; a PR delivers the work for review.
- A Story MAY contain multiple Tasks and multiple commits. There MUST NOT be a mandatory one-Task-to-one-commit mapping.
- Each commit MUST represent a logical change related to its associated Story, retaining the Story marker when applicable.
- A Story-linked PR MUST identify the Story and provide its link. Internal PR titles and descriptions remain Spanish. For example: `#305319 - Corregir el cálculo de liquidez`.
- When using squash merge, the resulting commit MUST follow the commit convention, including English text and the Story marker when applicable. Do not reuse a Spanish PR title unchanged as the squash subject.

## Compatibility and gradual adoption

The typed portion follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The leading `[ch<shortcut-id>]` marker is a Versat extension preserving the supplied Shortcut convention: the complete subject is not strict Conventional Commits syntax, which starts with the type. Before enabling commit linting, changelog generation or release inference, tooling MUST explicitly recognize the marker or remove it from parser input while preserving it in Git history and traceability output.

The branch pattern and a bare `#ID` in a PR title do not by themselves prove automatic Shortcut association. Verify branch, commit and PR linkage in the configured workspace; preserve the Story URL in the PR for explicit traceability. This policy does not change Shortcut event handlers or claim that their behavior has been tested.

Adopt these rules for new work without rewriting existing history or renaming historical branches. Keep the current delivery lifecycle and merge strategy. Initially, review the convention in PRs; the Harness structural validator does not enforce branch or commit syntax. Automated enforcement and additional commit types require subsequent governed changes.
