# Security Standard

- Apply least privilege to humans, agents, service accounts and tools.
- Secrets MUST use an approved secret manager and MUST NOT be committed.
- Untrusted input MUST be validated at trust boundaries.
- High-impact or irreversible actions MUST require explicit authorization and auditable execution.
- Dependencies and build provenance MUST be reviewable.
- Projects handling sensitive data MUST document classification, retention, access and deletion.
- Security controls that can be deterministic MUST be enforced by CI or platform policy.

## Public GitHub security verification

For public GitHub repositories, both repository-level Secret scanning and Push protection MUST be explicitly enabled under the index-resolved [public security policy](public-repository-security.yaml). Account defaults or partner notifications do not substitute for observed repository settings. Missing permissions/fields are unverified; disabled controls are non-compliant. Neither permits a public-readiness claim. The [Git Standard](git.md#public-github-repository-security) defines the complementary review/reference controls.

Security verification MUST be read-only, version-bound, complete and current. Do not fetch secret values or alerts to verify feature enablement, export credentials in reports, or give privileged credentials to untrusted PR jobs. Configuration changes remain separately authorized and require fresh readback. Preserve failed attempts and stronger controls. Local rollback MUST NOT silently disable already-correct remote protections.

## Confidential vulnerability reporting

The following reporting extension is preparation source extending H02; each route still requires its own governed adoption and verification.

- Each adopted reporting route MUST identify its actual destination, accountable owner, intended reporters, permitted recipients and supported repository/product scope.
- Do not describe a route as verified until actual configuration/access observations and an explicitly authorized non-sensitive synthetic submission/receipt support that claim.
- An owner assignment, working URL, authenticated administrator view or written guide alone is insufficient evidence of intended-reporter access or confidentiality.
- Missing, failed or changed verification MUST remain visible. Guidance MUST retain a safe fallback: request private instructions through an existing maintainer/repository contact without posting exploit details, credentials or customer information publicly.
- A fallback-only guide does not complete a requirement for a verified confidential route. Do not invent an endpoint, response commitment or retention period.
- Real vulnerability payloads and credentials MUST NOT enter test fixtures, public issues or routine validation reports. Record minimal safe evidence and use approved restricted storage for sensitive material.
- Channel setup, permission changes and synthetic messages require their actual scoped authorization. Planning or documentary implementation approval does not authorize them automatically.
- Each product MUST verify the route applicable to its own scope; common guidance is not automatic adoption or evidence of an operational service.

Existing pilot/internal receipt evidence MUST retain its original repository and audience scope. It MUST NOT establish a public Harness route or replace post-visibility verification. Control assessment MUST examine actual reviews, branch protection/rulesets, required checks and fork token/secret boundaries; local configuration alone is insufficient.

See the [reporting guide](../../docs/user-docs/guides/security-reporting.md) for the current documented status and safe steps.
