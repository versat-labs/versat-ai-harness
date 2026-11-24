# Bootstrap a project

[English](project-bootstrap.md) | [Português](project-bootstrap.pt.md) | [Español](project-bootstrap.es.md)

Use bootstrap for a new or empty project. Supply its purpose, owner, profile, domain, criticality, technologies and exact Harness provider. Existing repositories with content use maintenance instead.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $project-bootstrap for this empty repository. Reuse the supplied product brief, ask about missing identity, and present a reviewable skeleton and product context. Do not create remote repositories or PRs.
```

## Expected result

Expect a composed base/profile skeleton, specs/product/overview.md with evidence gaps, .versat/project.yaml, an exact .versat/standards.lock and a project-bootstrap SDD change. The provider index resolves Standards; users do not choose a subset of mandatory policy. Review product assumptions before treating them as requirements.

## Recovery and limits

An empty scaffold does not prove a usable application. Record unavailable runtime checks and avoid empty guides or fictional runnable steps. Conflicting existing content means stop and classify the repository before composing templates.

## Public GitHub security

Use the exact provider's [security procedure](../../guides/public-repository-security.md). Stage assets with `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging`, then run `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` from that provider. Add `--project-root /absolute/consumer` for an installed consumer with a matching exact lock. Review configuration differences and preserve stronger checks and ownership conflicts; only authorized administrative operations apply them.

A public-ready result requires a complete fresh live pass with `public_ready: true`. A local skeleton, policy check, saved snapshot or exit 0 alone is insufficient. Missing permissions or observations remain unverified. Audit does not authorize edits; maintenance verifies authorized remediation and never selects `latest` silently. One eligible code owner's approval satisfies the baseline even when both owners received review requests. External contributors use forks and PRs; no administrative credentials are exposed to fork CI. Release publication and adoption remain separate.

## References

- [Skill (English)](../../../skills/project-bootstrap/SKILL.md)
- [Templates (English)](../../../project-templates/README.md)
- [Project schema (English)](../../../schemas/project.schema.yaml)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
