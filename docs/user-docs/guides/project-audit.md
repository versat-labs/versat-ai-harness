# Audit a project

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Use an audit to assess compliance, readiness or drift. Prepare repository instructions, .versat/project.yaml, .versat/standards.lock, active specifications and the selected provider. This is broader than an ordinary code review.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $project-audit to assess this repository against its declared profile and resolved Standards. Report evidence, severity and remediation options. Do not modify files.
```

## Expected result

Expect findings that distinguish verified compliance, non-compliance and unavailable verification, with affected contracts and concrete next steps. Deterministic validation supplies bounded evidence; qualitative review also considers security, tests/evals, documentation, operations and profile/criticality.

## Recovery and limits

Missing identity or provider context is a visible gap, not evidence of compliance. An audit request does not authorize remediation. Use maintenance or an SDD change to address approved findings.

## Public GitHub security

Use the exact provider's [security procedure](../../guides/public-repository-security.md). Stage assets with `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging`, then run `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` from that provider. Add `--project-root /absolute/consumer` for an installed consumer with a matching exact lock. Review configuration differences and preserve stronger checks and ownership conflicts; only authorized administrative operations apply them.

A public-ready result requires a complete fresh live pass with `public_ready: true`. A local skeleton, policy check, saved snapshot or exit 0 alone is insufficient. Missing permissions or observations remain unverified. Audit does not authorize edits; maintenance verifies authorized remediation and never selects `latest` silently. One eligible code owner's approval satisfies the baseline even when both owners received review requests. External contributors use forks and PRs; no administrative credentials are exposed to fork CI. Release publication and adoption remain separate.

## References

- [Skill (English)](../../../skills/project-audit/SKILL.md)
- [Standards index (English)](../../../standards/index.yaml)
- [Validators (English)](../../../validators/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
