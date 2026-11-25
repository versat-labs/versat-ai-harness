---
sdd_version: 3
change: public-repository-security
requirements:
  - id: REQ-001
    statement: Define one mandatory public GitHub security contract in index-resolved Standards.
    acceptance:
      - For every supported profile and criticality, a public GitHub repository resolves the same required baseline without caller opt-out or parallel normative lists in Skills.
      - Policy and its deterministic representation remain version-matched and consistent; private or non-GitHub projects retain applicable existing policy without a false claim of public GitHub compliance.
  - id: REQ-002
    statement: Protect main against direct changes, stale approvals, unreviewed latest pushes, force pushes and deletion, including administrators.
    acceptance:
      - Every update to refs/heads/main requires a PR, at least one approval, code-owner review, dismissal of approvals after new reviewable commits and approval of the most recent reviewable push by someone other than its pusher.
      - Force push and deletion of main are blocked and no administrator, user, team, app or other actor can bypass its mandatory protection; classic administrator enforcement and applicable rulesets are evaluated together.
      - Existing required checks remain enforced; absence of main or an ineffective, disabled or permissive protection cannot pass public readiness.
  - id: REQ-003
    statement: Require effective code-owner coverage by elviszoz or evertonspohrversat for every contribution.
    acceptance:
      - The effective CODEOWNERS file on the PR base branch covers all files, including itself, with elviszoz and evertonspohrversat available as the designated owners; either eligible owner's approval satisfies the one-owner minimum.
      - Invalid syntax, owner accounts without the required write access, an empty ownership override or an override permitting only unrelated owners cannot establish compliance; unavailable permission evidence remains unverified.
  - id: REQ-004
    statement: Restrict creation, update and deletion of all upstream branches and tags to repository administrators without bypassing main protections.
    acceptance:
      - Active protections cover all existing and future branch and tag names, including names containing slashes, and permit these operations only to administrators subject to main's independent restrictions.
      - A missing target, excluded pattern, disabled rule, incomplete creation/update/deletion restriction or bypass granted to non-administrators is rejected; the administrator exception in broad reference rules never counts as a main-protection exception.
  - id: REQ-005
    statement: Require repository-level secret scanning and push protection to be enabled.
    acceptance:
      - Authenticated repository settings explicitly report secret_scanning and secret_scanning_push_protection as enabled before public readiness passes.
      - Either disabled feature is non-compliant; missing fields, insufficient permissions or unavailable API access remain unverified, and account-level defaults or scanning partner alerts do not substitute for the repository settings.
  - id: REQ-006
    statement: Provide executable, read-only security verification with explicit compliant, non-compliant and unverifiable results.
    acceptance:
      - A live assessment reads the intended repository identity and visibility, main protection, inherited and repository rulesets, effective CODEOWNERS and permissions, secret controls and participation settings, and reports evidence per control with repository, policy version and observation time.
      - A known violation produces a failing result; missing credentials, API errors, absent required fields, truncated pagination, unsupported rule semantics or ambiguous evidence cannot produce an overall pass and receive actionable diagnostics.
      - Offline fixtures or saved snapshots are clearly labeled and cannot be presented as current remote compliance; static/package success cannot satisfy the live public-readiness requirement.
      - The verifier performs no remote writes, exposes no tokens or secret values, and separates deterministic policy evaluation from authenticated data collection.
  - id: REQ-007
    statement: Make project-bootstrap require verified security before declaring a public repository ready.
    acceptance:
      - Bootstrap resolves the canonical contract, composes its applicable assets over base, identifies the actual remote, and runs the remote verifier after authorized configuration before reporting public readiness.
      - A local-only skeleton, an uninitialized remote or unavailable administrative access remains explicitly incomplete; configuration work respects the user's actual authorization and does not infer approval to create repositories or change visibility.
  - id: REQ-008
    statement: Make project-audit assess public GitHub security as a mandatory capability.
    acceptance:
      - Auditing a public GitHub project invokes the version-matched verifier and reports each violation or unavailable observation with severity, evidence and a concrete remediation path.
      - A green local validation run cannot conceal a failing or unverifiable remote control, and audit remains read-only unless remediation has been authorized.
  - id: REQ-009
    statement: Make project-maintenance detect security drift and verify authorized remediation.
    acceptance:
      - Maintenance compares effective remote settings with the exact target contract, preserves stronger compatible protections and project-specific content, and makes required configuration differences reviewable.
      - Authorized changes are followed by fresh readback and verification; failed or unavailable changes retain explicit gaps, and installed consumers are never silently moved to latest.
  - id: REQ-010
    statement: Preserve safe external participation through fork-to-PR.
    acceptance:
      - External contributors can use their own fork branches and open PRs into the upstream repository while upstream branch/tag operations remain restricted and main review requirements still apply.
      - Untrusted fork code never receives administrative verification or configuration credentials, cannot execute through a privileged checkout, and retains existing least-privilege workflow protections.
  - id: REQ-011
    statement: Provide composable assets, usable documentation and explicit versioned adoption.
    acceptance:
      - Public security assets compose with base and every profile without copying profile trees or overwriting valid consumer content; conflicting existing CODEOWNERS or settings are surfaced for reviewed reconciliation.
      - Canonical technical instructions explain setup, verification, remediation, permission requirements and evidence limits; affected community documentation has aligned English, Portuguese and Spanish content.
      - Source completion, reviewed PR delivery, release publication and adoption by existing consumers remain distinct; no installed package, release tag or consumer lockfile is implicitly upgraded.
  - id: REQ-012
    statement: Maintain meaningful positive and negative regression coverage for the security contract and lifecycle integration.
    acceptance:
      - Tests demonstrate a compliant configuration and independently detect missing or weakened main protections, unauthorized bypass, uncovered refs, ineffective owners and disabled secret controls, including valid classic/ruleset composition.
      - Tests cover unavailable APIs, permission failures, pagination and omitted fields without contacting production or granting privileges to fork jobs; actual Skill behavior is evaluated with versioned scenarios and observable evidence under the resolved Testing Standard.
      - Existing package, SDD, quality and execution checks remain required, and their successful results are reported separately from the new remote-security result.
  - id: REQ-013
    statement: Verify the authorized Harness GitHub corrections using the implemented contract.
    acceptance:
      - A fresh authenticated read-only run against versat-labs/versat-ai-harness confirms enabled secret controls, both administrator-only reference restrictions, eligible CODEOWNERS, unchanged mandatory main protections and fork-to-PR participation settings.
      - Evidence records the repository, observed configuration and time without secrets; any drift or unavailable observation remains open, and prior manual readback is not relabeled as execution of the new validator.
---

# Requirements

## Actors and context

Repository administrators configure the upstream service. Elvis Zoz and Everton Spohr are the designated code owners. External contributors work through forks. Bootstrap, audit and maintenance agents consume version-matched Standards; reviewers assess the policy and implementation through the existing SDD and PR gates.

## Functional requirements

The structured requirement statements and acceptance arrays above are authoritative. Compliance covers all seven controls in the developer's table and continued external participation. It is assessed from actual settings, not from configuration-file presence or a successful package test alone.

## Non-functional requirements

Assessments are read-only, deterministic given the same complete input and versioned policy, explicit about incomplete evidence, and safe to inspect without exposing credentials. Policy, capabilities, process and enforcement retain their existing directory responsibilities. Existing checks and stronger compatible controls are preserved.

## Acceptance scenarios

Design must map every one-based acceptance position to meaningful checks and carry forward the recorded impact obligations. The current production changes are operational observations only; the future verifier requires its own tests and live readback. Destructive pushes, branch deletion probes, production secret submissions and artificial external PRs are not required to verify the requested configuration.

## Constraints and assumptions

- Scope is GitHub-hosted public Versat repositories. No organization-wide settings or additional repository rollout is implicitly authorized.
- `main` is the canonical default branch for new repositories. An existing repository using another default branch must expose the mismatch for explicit migration; the verifier must not silently substitute an unprotected branch.
- Repository administrators may manage ordinary branches/tags, but remain subject to the independent main protections. This controls Git operations; it does not claim administrators are technically unable to edit repository settings later.
- A newly initialized repository can require an initial main reference before protection is configured. That initialization is not public readiness or a standing bypass exception; bootstrap must verify the completed controls before claiming readiness.
- No approval is inferred from this document, the prior audit, the implementation request or the separately authorized GitHub operation. Gate 1 approval unlocks Design; the existing subsequent gates remain applicable.
