# ADR-0020 — Retire universal branch administration from the public GitHub baseline

- Status: Accepted with Design R1 on 2026-11-27
- Related decision: [ADR-0018](0018-public-repository-security-verification.md)
- Scope: The reference-management policy for public GitHub repositories

## Context

The administrator-only update rule covers every branch. GitHub treats a PR merge as an update of the base branch, so administrators must exercise bypass on a qualifying PR. The Harness and the organization metadata repository each have a separate protection requiring PRs on main. The original issue concerned PR approval. [PR #48](https://github.com/versat-labs/versat-ai-harness/pull/48) · [Issue #17](https://github.com/versat-labs/versat-ai-harness/issues/17)

## Decision

Supersede the part of ADR-0018 that requires administrator-only creation, update and deletion for all upstream branches. Keep that restriction for tags. Require reviewed PRs on main, including for administrators. Ordinary upstream branch operations use the repository's existing permissions and any branch-specific protections. The indexed policy continues to supply the reference targets for rendering and verification.

## Consequences

Writers can manage ordinary unprotected branches and merge eligible PRs using their existing permissions. Contributors with read access can continue contributing by fork and PR. A repository-specific rule protecting a release branch can coexist with this baseline. During migration an operator removes only the retired repository-owned rule and compares independent main and tag protections before and after. Older pinned providers still apply their original baseline.
