---
sdd_version: 3
change: public-repository-security
status: proposed
owner: elviszoz
summary: Require verified GitHub security controls for public Versat repositories throughout bootstrap, audit and maintenance.
risk: high
impact:
  state: assessed
  summary: Extend the Git and Security contracts and lifecycle readiness checks while retaining contribution access, versioned adoption, existing validation and human review boundaries.
  items:
    - current_contract:
        path: standards/core/git.md
        locator: '## Governance'
        digest: 4c8959b2640e22dfc3a392a6183c39fd4725cadcf3bb79e19cbf70df12ac2308
      effect: extend
      targets: [REQ-001, REQ-002, REQ-003, REQ-004]
      reason: Preserve protected branches and required checks while making review, administrator enforcement and all-reference restrictions explicit.
    - source:
        change: harness-publication-readiness
        requirement: REQ-006
        scenarios: [1, 2, 3]
        requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
      current_contract:
        path: standards/core/security.md
        locator: '## Confidential vulnerability reporting'
        digest: 9ffd01b20b90e4b592305f63055624f229bf8b79ef06a02d4e07963faef9aa80
      effect: extend
      targets: [REQ-005, REQ-006, REQ-010, REQ-013]
      reason: Retain actual-control verification, explicit operational authority and public participation while requiring enabled repository secret controls and executable verification.
    - current_contract:
        change: public-repository-security
        artifact: proposal
        locator: '## Current contract baseline'
      effect: extend
      targets: [REQ-007, REQ-008, REQ-009]
      reason: Add mandatory public-security readiness to the existing three Skills without copying policy into their instructions.
    - current_contract:
        path: project-templates/README.md
        locator: '## Composition'
        digest: 647350de506e4d8ed2d30e26e8572da0879ab1126701062bebbd83df361e39f9
      effect: extend
      targets: [REQ-007, REQ-011]
      reason: Preserve base-plus-profile composition, project-specific content and exact provider adoption while adding conditional public-repository security assets.
    - current_contract:
        path: validators/README.md
        locator: '# Validators'
        digest: ad4928a3dbc1d4863ce99e80fba8b4fa6c5dbdb7575f2fe16e0157a096e56c23
      effect: extend
      targets: [REQ-006, REQ-010, REQ-012]
      reason: Add deterministic remote-control assessment without equating local contract checks with GitHub enforcement or weakening existing suites.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply in this Codex chat approving Proposal/Requirements R1 and requesting Design.
    quote: Aprovo Proposal/Requirements R1. Avance para o Design.
    revision: 1
    digest: 50b4b5a3bf0759a420fa5833569295f44b0b76a40f05b8ad14de2036899f84eb
---

# Proposal

## Context and problem

The developer requested seven GitHub protections for new public Versat repositories, with external participation through fork-to-PR. The audit found generic Git and security guidance, but no complete canonical baseline, generated security assets or executable remote-control validator. Consequently, local validation can pass without proving repository security.

The implementation baseline is Harness 0.4.0 at `c191f3b126c659fbabfd4ed3d40b474407cfd26a`, checked out on `codex/public-repository-security`. This is the current local `origin/main`, replacing the older detached audit checkout without modifying another worktree. No matching active dossier existed. Related archived publication/contribution and ownership work was inspected; historical approvals remain unchanged.

## Expected outcome

Every new public GitHub repository governed by the new contract has verifiable platform enforcement of the requested protections. Bootstrap cannot claim public readiness without it; audit reports deviations and unavailable evidence; maintenance checks and remediates authorized drift, then verifies the resulting state.

Policy remains under `standards/`, resolved through `standards/index.yaml`. Skills orchestrate the contract, templates compose it, and validators enforce observable requirements. Passing local package checks alone never establishes remote security.

## Scope

- Canonical Git/security policy and any versioned machine-readable policy representation needed by validators, owned by Standards and resolved through the index.
- `project-bootstrap`, `project-audit`, `project-maintenance` and their directly related guidance.
- Conditional public-repository template assets, including complete CODEOWNERS coverage and reference protection configuration.
- Executable read-only verification of effective GitHub settings, machine-readable and human-readable results, failure/unknown behavior and safe integration with readiness workflows.
- Maintained positive, negative and regression tests, meaningful Skill evaluation, and aligned user documentation.
- Verification of the separately authorized operational corrections to the existing public Harness repository.

## Out of scope

- Organization-wide rollout, changes to other repositories, account membership or granting new access.
- Changing repository visibility, deleting references, rewriting Git history, creating test credentials, or destructive enforcement probes against `main`.
- Automatic release publication, retagging, marketplace activation or implicit installed-consumer upgrades.
- A general GitHub provisioning engine, changes to SDD human gates, licensing terms or confidential reporting channels.
- Disabling required checks or bypassing PR review to deliver this change.

## Work tracking

No Shortcut Story or GitHub issue was supplied. The stable change ID is `public-repository-security`; no external identifier is fabricated. Source policy changes require the existing branch, PR and mandatory review workflow. This Proposal does not create a PR or authorize merge.

## Impact and risks

Incorrect rule composition could grant administrators bypass of `main` or block all legitimate administration. The contract must distinguish strict main protection from the administrator exception used only for broad reference restrictions. Inherited rules and classic protection must be considered together. Missing permissions, omitted API fields, incomplete pagination and unsupported rule semantics cannot produce a pass.

CODEOWNERS presence alone is insufficient: the effective base-branch file, full path coverage, account permissions and required code-owner approval must be checked. Rules protecting only currently existing branches cannot establish protection of future names. Public readiness is distinct from creating a local skeleton or initially establishing an empty repository's main branch.

Administrative read permissions required for verification must not leak into untrusted fork execution. Verification must not fetch secret values or execute contribution code with privileged credentials. Configuration readback proves observed settings, not a destructive behavioral test or permanent immunity to later administrator edits.

## Current contract baseline

- `standards/core/git.md` requires default-branch protection, PRs for material changes, required checks, review ownership and disabled force pushes, but lacks the complete requested public baseline.
- `standards/core/security.md` prohibits committed secrets and requires actual platform-control assessment; it does not explicitly require repository secret scanning and push protection to be enabled.
- `skills/project-bootstrap/SKILL.md` resolves Standards and composes a profile-specific skeleton; `references/project-lifecycle.md` generically checks ownership, protection and secret scanning. The result distinguishes scaffolding from readiness but lacks the complete remote checklist.
- `skills/project-audit/SKILL.md` reports manual/unverified checks and does not mutate an audited project without remediation authority. It lacks mandatory executable public-security assessment.
- `skills/project-maintenance/SKILL.md` preserves content and exact version references during reviewed migration, without an explicit remote-security drift check.
- The shared template has no CODEOWNERS or reference-ruleset assets. `validators/security/` contains only a README. Existing package, SDD, quality and execution suites do not establish these remote controls.
- Current main CODEOWNERS names both `@elviszoz` and `@evertonspohrversat` globally. Both accounts were observed with admin permissions during the audit.

## Authorized GitHub operation observed on 2026-11-24

The developer separately requested correction of the Harness settings in the same message that requested source implementation. That concrete operational action was executed without interpreting it as approval of unseen SDD artifacts:

- Enabled `security_and_analysis.secret_scanning` and `security_and_analysis.secret_scanning_push_protection`; authenticated readback returned `enabled` for both.
- Created active branch ruleset [28023884](https://github.com/versat-labs/versat-ai-harness/rules/28023884) and tag ruleset [28023891](https://github.com/versat-labs/versat-ai-harness/rules/28023891). Both target `~ALL` with no exclusions, restrict creation/update/deletion, and allow only repository administrator role 5 to bypass that ruleset.
- Read back the classic `main` protection and compared the complete response with the pre-operation snapshot: unchanged. It retains one required code-owner approval, stale approval dismissal, last-push approval, administrator enforcement, blocked force pushes/deletion and the existing required status check.
- Confirmed `allow_forking: true` and `pull_request_creation_policy: all` after the operation. No test fork, PR, secret or destructive push was created.

These are dated operational observations, not implementation or acceptance evidence for the proposed validator. The maintained validator must later re-observe the live state under REQ-013. Exact API request/response snapshots are temporarily available under `/private/tmp/versat-public-security-*`; they are not durable acceptance artifacts or links required by this plan. Design must specify a minimal durable evidence format without tokens or secret payloads.

## Proposal acceptance criterion

Approve the observable requirements and boundaries in Requirements R1, including the distinction between local scaffolding, remote configuration, observed enforcement, future drift and reviewed versioned adoption. Approval unlocks Design only. No unresolved product decision is currently recorded.

## Planning review

The developer approved Proposal/Requirements R1 in this Codex chat: "Aprovo Proposal/Requirements R1. Avance para o Design." The approval binds the combined stage digest `50b4b5a3bf0759a420fa5833569295f44b0b76a40f05b8ad14de2036899f84eb` and authorizes Design preparation. Requirements and substantive Proposal content remain unchanged. Design R1 is being prepared; Tasks and implementation remain subject to their subsequent gates.
