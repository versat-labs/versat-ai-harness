# Architecture Decision Records

ADRs preserve the context and consequences of structural Harness decisions.

## States

- `Proposed`: under discussion;
- `Accepted`: current decision;
- `Superseded`: replaced by another ADR;
- `Deprecated`: retained only for historical purposes.

## Evolution rule

Do not silently rewrite an accepted decision. Create a new ADR, reference the previous one and update its state when a decision is replaced.

## Index

- [ADR-0001 — Use a single repository as the source of truth](0001-single-source-repository.md) (superseded by ADR-0011)
- [ADR-0002 — Separate policy, capability, process and enforcement](0002-separate-policy-capability-process-enforcement.md) (superseded by ADR-0011)
- [ADR-0003 — Resolve context through declarative metadata](0003-declarative-context-resolution.md)
- [ADR-0004 — Distribute versioned snapshots with a lockfile](0004-versioned-snapshots-and-lockfiles.md)
- [ADR-0005 — Govern knowledge at three levels](0005-three-level-knowledge-governance.md)
- [ADR-0006 — Adopt one SDD lifecycle for all profiles](0006-unified-sdd-lifecycle.md)
- [ADR-0007 — Compose templates from a base](0007-composable-project-templates.md)
- [ADR-0008 — Adopt a hybrid language policy](0008-hybrid-language-policy.md) (superseded by ADR-0010)
- [ADR-0009 — Keep the Harness executor-independent](0009-execution-adapters.md)
- [ADR-0010 — Refine the language policy](0010-refine-language-policy.md)
- [ADR-0011 — Make the repository root the portable Plugin package](0011-root-portable-plugin-package.md)
- [ADR-0012 — Separate consumer agent artifacts from Plugin packaging](0012-consumer-agent-artifacts.md) (proposed; policy review pending)
- [ADR-0013 — Consolidate SDD routing and prepare documentary closure before merge](0013-consolidated-sdd-workflow.md)
- [ADR-0014 — Bind SDD acceptance and retained behavior to current validation evidence](0014-sdd-acceptance-and-regression.md)
- [ADR-0015 — Separate explicit test execution from validation and evaluate real skill behavior](0015-explicit-test-execution-and-skill-evaluations.md)
- [ADR-0016 — Separate public Harness preparation from adoption and publication](0016-public-harness-preparation-boundary.md) (accepted; preparation implementation in progress)
- [ADR-0017 — Validate code and changelog changes against a reviewable Git baseline](0017-revision-based-code-quality-checks.md)
- [ADR-0018 — Verify public repository security through a versioned policy and read-only observations](0018-public-repository-security-verification.md) (branch administration provision superseded by ADR-0020)
- [ADR-0020 — Retire universal branch administration from the public GitHub baseline](0020-retire-universal-branch-administration.md)
