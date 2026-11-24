# ADR-0018 — Verify public repository security through a versioned policy and read-only observations

- Status: Accepted with `public-repository-security` Design R1; implementation pending
- Date: 2026-11-24
- Related: ADR-0003, ADR-0004, ADR-0007, ADR-0011, ADR-0014, ADR-0015, ADR-0017
- Scope: Public GitHub security policy, validation and lifecycle readiness. No existing ADR is superseded.

## Context

Local package checks do not establish GitHub enforcement. The approved requirements call for mandatory public-repository protections throughout bootstrap, audit and maintenance, without copying policy into Skills or giving privileged credentials to external contribution code. The current public Harness combines classic main protection with two active administrator-only reference rulesets; a validator must understand their combined effect.

## Proposed decision

Keep the authoritative policy in `standards/`. Add a typed YAML policy to `standards/index.yaml` so the existing exact-version resolver and lock digest contract include it. Human-readable Git and Security Standards explain its requirements. A schema describes format, while the policy supplies names, thresholds and expected settings. Skills consume the resolved contract and invoke checks; they do not maintain alternative policy tables.

Separate authenticated observation from deterministic evaluation. A bounded GitHub CLI adapter under `scripts/security/` performs only allowlisted GET requests. Pure evaluation and the public verification entry point live under `validators/security/`, with versioned policy, snapshot and report schemas under `schemas/`. The evaluator accepts complete collected observations or explicitly labeled offline fixtures. Neither component configures GitHub. A separate local renderer under `scripts/bootstrap/` produces reviewable configuration assets from the same policy and refuses conflicting overwrites.

Support strict main enforcement through classic protection, active rulesets or their combination. Each mandatory main control needs evidence from a source that applies to everyone; an administrative exception in a different reference-management ruleset cannot weaken it. Broad branch and tag restrictions cover all names without exclusions and reserve creation, update and deletion to administrators. Their bypass list is intentionally separate from main review protections. Other compatible restrictions are retained.

Use a conservative, documented proof boundary. Prefer GitHub's effective branch-rule endpoint to infer applicability to main, inspect full ruleset details and inherited rules, and require universal coverage for future branches/tags. Unsupported pattern combinations, hidden bypass lists, missing permissions or ambiguous CODEOWNERS coverage remain unverified rather than passing optimistically. A normalized snapshot is evidence of observed configuration, not an authenticated attestation, a destructive behavior test or a guarantee against later drift.

Public readiness requires a fresh live result with complete observations. Offline/package validation and local rendering never establish it. Bootstrap stops short of public readiness on a gap; audit reports it; maintenance compares changes and re-observes authorized remediation. Existing consumers adopt the changed policy through reviewed exact releases; direct source verification explicitly identifies its development source.

Keep ordinary PR CI credential-free for these controls: validate policy, renderer and evaluator with offline automated tests, alongside every existing required suite. Run authenticated live assessment from a trusted operator session. This change does not add an administrative token, scheduled service, privileged PR workflow or automated remediation engine. External contributors continue using forks and ordinary PR checks.

## Alternatives considered

- Prose-only checklists: preserve the present gap between stated intent and repeatable assessment.
- Hard-coded settings in every Skill or in the validator: create competing policy sources and unreliable versioned adoption.
- One ruleset combining main protections and administrator bypass: would also allow bypass of mandatory main review controls.
- Migrate every existing classic protection to rulesets: unnecessary configuration churn; effective equivalent enforcement can be verified without weakening existing checks.
- Approximate every GitHub pattern and custom bypass role locally: risks false passes. The supported proof shapes cover the requested deployment; unfamiliar shapes are unverified with concrete remediation guidance.
- Give fork CI an administrative token: expands the trust boundary unnecessarily. Offline required tests and explicit trusted live assessment serve different purposes.
- Implement organization-wide provisioning or periodic drift services: outside the approved scope; the verifier can later be integrated through separately reviewed operations.

## Consequences

- Developers receive actionable per-control results and reviewed settings assets; actual enforcement remains in GitHub.
- An API permission problem or unsupported secure configuration may block readiness until it can be observed or normalized. Diagnostics must distinguish this from demonstrated non-compliance.
- The CLI adapter depends on an authenticated GitHub CLI and sufficient repository read permissions. No privileged credential is provisioned by this change.
- New schema and policy files are part of the exact provider/lock boundary. Existing provider verification and profile composition remain intact.
- Configurations can change after observation. Consumers must rerun live assessment at the relevant readiness/maintenance decision; copied reports have no standing readiness authority.
- Runtime, policy, template and documentation changes remain subject to current SDD gates, PR review, checks and separately authorized release adoption.

## Verification and review boundary

Design R1 defines seven required checks covering policy/composition, control evaluation, collection failure modes, three supervised Skill scenarios, documentation/trust review, actual Harness readback and all existing suites. Approval of this ADR and Design unlocks Tasks planning only. It neither implements the validator nor modifies GitHub settings. The earlier, separately authorized GitHub correction remains a dated operational fact in Proposal.

## Administrative acceptance record — 2026-11-24

The developer approved Design R1 and ADR-0018 in this Codex chat: "Aprovo o Design R1 e o ADR-0018. Avance para as Tasks." The accepted Design digest is `a63f195eedd6c04621fa38c7b8cecb98b0c6d66c8a393005ee474d08299736bf`; the reviewed ADR bytes had SHA-256 `c0ed53b4a5e79d78ca93574d04724b6320006eeec8f8414033a04b9dcaf2fc4b`. Only the status line and this acceptance record were changed. Restoring the original status line and removing this section reconstructs the reviewed bytes. Earlier conditional language remains the historical presentation of the accepted decision. This approval authorizes Tasks preparation; implementation and release remain pending.
