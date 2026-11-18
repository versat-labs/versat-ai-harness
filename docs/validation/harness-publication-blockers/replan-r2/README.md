# GitHub Free replanning — R2 diagnostics

Scope: local Proposal/Requirements revision for `harness-publication-blockers`; no remote execution. Gate 1 is awaiting approval. Design/Tasks remain substantive R1 documents with superseded reviews. The handoff carries a historical-status notice.

- [Current proposal](../../../../specs/changes/harness-publication-blockers/proposal.md) and [requirements](../../../../specs/changes/harness-publication-blockers/requirements.md).
- [Exact R1 snapshot hashes](r1/integrity.json) and [pre-edit file hashes](before.json). The five raw Markdown snapshots retain their original bytes, including relative links that resolve from their original repository locations; they are evidence copies, not relocated living guides or a second active/archive dossier.
- [First planning attempt](planning.json): failed because the previously used environment lacked jsonschema.
- [Planning diagnostic with restored dependencies](planning-02.json): exit 1; no schema/reference/coverage findings, but three approvals required, one retained failed check, two stale evidence inputs and six unresolved acceptance findings.
- [Required suite result](suite-result.json), [stdout](suite.stdout), [stderr](suite.stderr): exit 1 from SDD readiness; 131 validator and 48 execution tests passed. Existing legacy/v2 inventory warnings remain.
- [Local review](local-review.json): scope, source preservation, stage digests and environment.

The old temporary interpreter was not reused after dependency failure. An initial ordinary install could not resolve packages; an isolated public-PyPI install of the existing requirements in a new temporary environment succeeded. No repository dependency pins, provider version or GitHub permissions changed.

These results are planning/structural regression evidence, not control enforcement, reviewer consent, rights clearance or publication success. Historical CHECK-004 and other acceptance findings remain open. Public-first execution awaits revised planning and separate operation-specific authority. Final review must include this newly added evidence surface.
