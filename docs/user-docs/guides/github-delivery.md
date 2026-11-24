# GitHub delivery

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Use this guide when preparing an issue-linked change for human review. You need the real issue URL, repository instructions, approved scope and the repository’s validation environment.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $versat-sdd to inspect <change-id>, prepare its delivery summary and identify missing archive or validation prerequisites. Do not publish a PR or merge.
```

## Expected result

Work on a branch using the resolved Git convention. Keep issue, requirements and commits traceable; never invent a Shortcut ID. Planning or incomplete work is reviewed in a draft PR. Before submitting completed implementation, prepare the documentary archive in the same branch and pass the selected archive preflight. Request PR publication explicitly, then obtain human review and final required CI before merge.

## Recovery and limits

Report failed or unavailable checks in the PR. Review feedback stays with the same change ID; scope changes reopen the relevant review. Verify actual merge separately from local readiness. A merge neither publishes a release nor upgrades installed consumers.

## Public GitHub security

Use the exact provider's [security procedure](../../guides/public-repository-security.md). Stage assets with `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging`, then run `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` from that provider. Add `--project-root /absolute/consumer` for an installed consumer with a matching exact lock. Review configuration differences and preserve stronger checks and ownership conflicts; only authorized administrative operations apply them.

A public-ready result requires a complete fresh live pass with `public_ready: true`. A local skeleton, policy check, saved snapshot or exit 0 alone is insufficient. Missing permissions or observations remain unverified. Audit does not authorize edits; maintenance verifies authorized remediation and never selects `latest` silently. One eligible code owner's approval satisfies the baseline even when both owners received review requests. External contributors use forks and PRs; no administrative credentials are exposed to fork CI. Release publication and adoption remain separate.

## References

- [Git (English)](../../../standards/core/git.md)
- [SDD (English)](../../../sdd/README.md)
- [SDD validation (English)](../../../validators/sdd/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
