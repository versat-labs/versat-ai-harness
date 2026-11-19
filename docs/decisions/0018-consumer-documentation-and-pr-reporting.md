# ADR-0018 — Define consumer documentation paths and report mechanical PR checks

- Status: Accepted
- Decision evidence: Design revision 1 and this ADR were approved in the Issue #23 development conversation.
- Related: ADR-0007, ADR-0011, ADR-0013, ADR-0017

## Context

Issue #23 asks for consistent consumer documentation, guidance on feature purpose and a way to see documentation compliance from the PR. The current quickstart defaults differ from the proposed reader layout. Bootstrap already owns a shared discovery record. SDD supports explicit decision paths, while short ADR IDs resolve under the established decisions directory.

## Decision

Make the Documentation Standard the consumer layout authority. Use the user-documentation subtree for new quickstarts and detailed guides. Keep shared bootstrap discovery in `specs/product/overview.md` and use a reader overview for publication-ready context. Use explicit SDD paths for new consumer decisions under `docs/architecture/decisions/`. Preserve working legacy documentation and decision references.

Use a read-only GitHub Actions check summary for advisory, deterministic documentation results. Evaluate the actual PR comparison and report both satisfied and unmet mechanical rules, with explicit review items for content judgment. Keep the validator independent of GitHub and make consumer adoption explicit. GitHub presents the result. The product team owns publication decisions, and reviewers own semantic assessment.

## Consequences

Consumer templates remain composed from base. Existing documentation locations and version pins require no automatic migration. Reviewers can open the report from the PR check without giving the job write access. The first reporting rules cover presence of applicable counterparts and leave the quality of the explanation and translation to human review. Existing required jobs continue to control delivery. A future decision to enforce documentation rules at merge or add publishing infrastructure needs its own scope and review.
