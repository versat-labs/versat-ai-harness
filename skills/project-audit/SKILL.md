---
name: project-audit
description: Assess a Versat repository against its declared profile, resolved Standards, SDD state and readiness contracts. Use for compliance, readiness or drift reviews, not ordinary code review.
---

# Project Audit

## Audit method

1. Locate the installed Plugin root two directories above this file.
2. Read `.versat/project.yaml`, `.versat/standards.lock`, repository instructions and active SDD changes from the target project.
3. Resolve the expected context with the Plugin root [Standards index](../../standards/index.yaml) and compare it with the lockfile.
4. Run applicable deterministic validators from the Plugin root before making qualitative judgments.
5. Evaluate required documentation, security, tests, evals, observability and operations according to profile and criticality. Review project artifacts against the resolved contracts, distinguishing package layout from consumer layout and declared dependencies from verified execution readiness. Record checks without a deterministic validator as manual or unverified.
6. For public GitHub targets, execute the version-matched [security verification procedure](../../docs/guides/public-repository-security.md) required by the resolved Standards. Verify the actual remote identity and exact consumer provider; inspect per-control findings, observation completeness, mode and `public_ready`. A passing package run cannot conceal remote violations or unknowns. If only a supplied snapshot or insufficient access is available, perform the permitted assessment and label its evidence limits explicitly; do not claim current remote compliance.
7. Report findings by severity with evidence, affected contract and a concrete remediation path. The security check and this audit remain read-only unless remediation was explicitly authorized.

Do not change the audited repository unless remediation was explicitly requested. A successful audit distinguishes verified compliance, non-compliance and items that could not be verified.
