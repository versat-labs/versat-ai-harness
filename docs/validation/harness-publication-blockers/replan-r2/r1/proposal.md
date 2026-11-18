---
sdd_version: 3
change: harness-publication-blockers
status: proposed
owner: '@elviszoz'
summary: Resolve the outstanding pre-publication evidence, confidentiality, control and reporting prerequisites for
  the existing Harness, preserving separate adoption and publication authority.
risk: high
impact:
  state: assessed
  summary: Classify all 38 predecessor scenarios once as preserve or extend, plus the effective operational handoff
    and validation entry point. Preserve delivered history and the approved publication boundary; no requirement is
    retired and no public outcome is claimed.
  items:
  - source:
      change: harness-publication-readiness
      requirement: REQ-001
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-009
    reason: Retain approved wording, third-party scope and actual text-review capacity; new work resolves current
      applicability rather than recreating the delivered candidate.
  - source:
      change: harness-publication-readiness
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-001
    - REQ-004
    reason: Extend the bounded rights assessment to resolution of remaining and changed evidence for the final candidate.
  - source:
      change: harness-publication-readiness
      requirement: REQ-003
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-001
    - REQ-002
    - REQ-003
    reason: Complete inaccessible-surface and confidentiality disposition work, retaining the full exposure boundary
      and explicit remediation gates.
  - source:
      change: harness-publication-readiness
      requirement: REQ-004
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-008
    reason: Retain canonical package identity, exact references, migration and recovery; no new release or root adoption
      is selected here.
  - source:
      change: harness-publication-readiness
      requirement: REQ-005
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-007
    - REQ-008
    - REQ-009
    reason: Retain observed private rehearsal scope, failure/update behavior and separately mandatory public verification;
      historical scenarios are not reenacted as new public successes.
  - source:
      change: harness-publication-readiness
      requirement: REQ-006
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-005
    - REQ-008
    reason: Resolve effective control gaps while retaining self-contained contributions, provenance and operation-specific
      authorization.
  - source:
      change: harness-publication-readiness
      requirement: REQ-007
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-006
    reason: Resolve route prerequisites and bind genuinely visibility-dependent checks to later operations without
      widening prior pilot evidence.
  - source:
      change: harness-publication-readiness
      requirement: REQ-008
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-008
    - REQ-009
    reason: Retain safe multilingual maintained guides and actual usage verification if changes affect them.
  - source:
      change: harness-publication-readiness
      requirement: REQ-009
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-001
    - REQ-007
    - REQ-009
    reason: Advance from a completed defer assessment to resolving pre-publication blockers; old preparation remains
      valid history, not clearance.
  - source:
      change: harness-publication-readiness
      requirement: REQ-010
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-003
    - REQ-009
    reason: Obtain an attributable confidentiality treatment while preserving delivered approvals and restricted evidence;
      destructive remedies remain outside the approved scope.
  - source:
      change: harness-publication-readiness
      requirement: REQ-011
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-008
    reason: Retain independent product and organization boundaries and required enforcement suites.
  - source:
      change: harness-publication-readiness
      requirement: REQ-012
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 5b0d0bc483ce8c45094ee7f09dd41ed0f0d416d84565d1d3646cf69881b70004
    current_contract:
      change: harness-publication-blockers
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-010
    reason: Apply the same three gates and exact authorization boundaries to the new change without transferring predecessor
      approvals.
  - current_contract:
      path: docs/handoffs/harness-publication-readiness/README.md
      locator: '## Separately authorized operational sequence'
      digest: 1a77e7645fb1674d91d0e4d68516eb539e72bedab43a0a4b368a9d4e2ea5c0d8
    effect: preserve
    targets:
    - REQ-001
    - REQ-007
    reason: Retain the effective operational boundary and complete validation entry point; no change to these sources
      is authorized at Gate 1.
  - current_contract:
      path: scripts/validate/run.sh
      locator: validation_python=
      digest: 7cc5d5a3f20927618b613b37090cf792669e0920ffbbf9c60db8f0147e43c013
    effect: preserve
    targets:
    - REQ-008
    - REQ-009
    reason: Retain the effective operational boundary and complete validation entry point; no change to these sources
      is authorized at Gate 1.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: User reply in this chat on 2026-11-14 explicitly approving Proposal/Requirements R1 and authorizing Design
      only
    quote: Sim, aprovo a Proposal e os Requirements R1 de harness-publication-blockers. Avance somente ao Design,
      sem iniciar a implementação ou publicar.
    revision: 1
    digest: d3552c1655c58d08d56c9c0178c75c50e804c171087b6d62a2f8be1e6147e5eb
---

# Proposal

## Context and problem

The public-Harness preparation was already delivered in [PR #39](https://github.com/versat-labs/versat-ai-harness/pull/39), merged on 2026-11-13 at `4a56181d3597c5d345a7639f013547e1700420cb`. The predecessor is [harness-publication-readiness](../../archive/harness-publication-readiness/proposal.md), with three recorded R1 approvals and completed private preparation. Its outcome remains `prepared / defer-publication`: inaccessible surfaces, confidential-history disposition, effective controls and public reporting are unresolved. Repeating its Proposal or declaring its preparation tests to be public clearance would not resolve those gaps.

This new change addresses the outstanding prerequisites of H01-H03. It preserves the existing repository/root Plugin, the selected Apache direction for eligible first-party material, third-party terms and the separate preparation/adoption/publication boundary in [ADR-0016](../../../docs/decisions/0016-public-harness-preparation-boundary.md). It does not supersede that ADR or the predecessor's historical approvals. The eventual current blocker status may supersede dated observations only through new attributable evidence.

## Expected outcome

An exact, reviewable resolution of pre-publication blockers, supported by accessible restricted evidence and actual rights/security/control review, plus a bounded handoff for later authorized adoption/publication and mandatory external verification. The exit is stronger than another completed assessment marked defer: every in-scope pre-publication blocker must meet its exit condition before this successor can claim completion. If the existing-repository approach cannot be cleared within scope, report the unresolved decision and replan; do not manufacture completion.

Some observations inherently require public visibility. This change must establish their feasible private prerequisites and test handoff, while retaining the public outcomes as unverified. It cannot assert overall publish-ready/public availability or completed H03 by moving feasible pre-publication work into that follow-up.

The current deliverable is only this Proposal and [Requirements](requirements.md). All substantive resolution work below is proposed future implementation after the three gates and explicit execution authority.

## Scope

- Reconcile the merged source, approved wording/patch and prior restricted record; refresh each blocker with owner, actual review capacity, evidence access and observable exit condition.
- Complete unavailable-surface review and establish a reviewed treatment for confidentiality/history findings without exposing their contents in Harness.
- Refresh rights, notices and candidate applicability against the final proposed distribution scope; retain exact candidate approval and historical evidence.
- Assess effective contribution controls, prepare necessary corrections and verify them only under later scoped authority; establish reporting prerequisites and audience-specific verification.
- Preserve package behavior, multilingual guidance and independent products; define current validation and explicit later operational acceptance without adopting or publishing anything in this successor.

## Out of scope

Current authorization: no implementation, Design/Tasks placeholders, ADR draft, candidate regeneration, changed guides/Standards/manifests, license application, sensitive payload collection, tests that send messages, controls/permissions changes, commit/push/PR/merge, tag/release, visibility operation or consumer migration. Local planning files, a local branch/worktree and bounded diagnostics are permitted. Existing approval for a different collection or operation is not transferred.

Proposed future scope excludes effective root-license adoption, public visibility, tag/release publication, real consumer migration, cross-product/organization rollout, new destinations/mirrors/SDKs and destructive history remediation. An exact control correction, reporting setup/test or newly scoped restricted collection may be planned here, but requires its own operational authority before execution. A material remedy affecting history, original approvals, destination or licensing reopens the applicable gate and, where necessary, a successor decision; Gate 1 does not preapprove that remedy.

## Work tracking

- Stable new change ID: `harness-publication-blockers`. No matching active/archive dossier existed at inspection. The predecessor remains uniquely archived and unchanged.
- Related delivered work: [PR #39](https://github.com/versat-labs/versat-ai-harness/pull/39), H01 [#34](https://github.com/versat-labs/versat-ai-harness/issues/34), H02 [#35](https://github.com/versat-labs/versat-ai-harness/issues/35). These are provenance, not new work authorizations or issues to reopen.
- No new issue or Shortcut Story is assigned or created. No fabricated ID. No open Harness PR was returned by the scoped query on 2026-11-14.
- Local branch `codex/harness-publication-blockers`, isolated worktree, based on fetched main `4a56181d3597c5d345a7639f013547e1700420cb`. The existing predecessor checkout was preserved. Fetch changed only local refs; no remote write occurred.

## Repository and Standards context

Harness is the provider repository; no root consumer project identity or lockfile exists to invent. Declared VERSION/manifests remain 0.3.0, but this exact merged source implements SDD v3. Use its own [skill](../../../skills/versat-sdd/SKILL.md), [process](../../../sdd/process.md), [New change procedure](../../../sdd/workflows/new-change.md), [metadata](../../../sdd/metadata.md), v3 templates/schemas and [validator](../../../validators/sdd/README.md). An installed 0.3.0 release is not a substitute for this source snapshot. No provider upgrade occurs.

Resolve applicable core Standards through [the index](../../../standards/index.yaml), including licensing/publication, contribution, security, Git, testing, documentation and language. Root [AGENTS](../../../AGENTS.md) applies; no more-specific instruction applies to this dossier. Preserve the [architecture](../../../docs/architecture/overview.md), root-package ADR-0011 and ADR-0016 boundaries. Python is the observed validation runtime; no consumer profile or application stack is fabricated.

| Provider anchor | SHA-256 at the selected source |
|---|---|
| `sdd/process.md` | `488b63b3ad26e4779db69d4b6ea9bd28b629936f58ccb42493cdaa99c940ccdb` |
| `sdd/metadata.md` | `788c3a0ae8ac265a66546d3dddbf35e2c0c81bfa932940f3e5eae34990a0a064` |
| `sdd/workflows/new-change.md` | `3fed9300f21ecc17d799b188179efb5a149a0afec4a91098f613a007c40f7cd4` |
| `standards/index.yaml` | `0a70db972dc3ba14cecf27a1617e404f63ab32ec1222ae8632c30698ecbcccee` |
| `validators/sdd/validate.py` | `94f152e14dbe1dbb60fcd3d0ef40ba896fd9a71234d28d44ac8ba1d172d329bb` |

## Current contract baseline

Inspected 2026-11-14 at the merged source above. New remote observations establish PR #39 merge and source state; the underlying exposure/control observations below are dated predecessor evidence, not a fresh operational audit.

| Contract | Observed evidence and consequence |
|---|---|
| Delivery | Predecessor Proposal/Requirements, Design and Tasks R1 have recorded approvals; eight tasks and ten preparation checks are recorded complete. The archived dossier and PR #39 merge are distinct evidence. No historical approval transfers to this successor. |
| Outstanding exposure | The [handoff](../../../docs/handoffs/harness-publication-readiness/README.md) records a 16-category assessment, six inaccessible package-type listings, two uninspected cache payloads, external attachment/integration gaps and internal-reference history. These are starting gaps, not fresh absence/sensitivity findings. |
| Evidence boundary | [Review inputs](../../../docs/handoffs/harness-publication-readiness/review-inputs.json) bind opaque HPR-PRIVATE-01 and its restricted assessment. Public-safe metadata is available; the underlying private record and current reviewer access were not re-audited in this planning. Old collection/access approval is historical. |
| Terms/candidate | [Apache R1 approval](../../../docs/licensing/candidates/apache-2.0/APPROVAL.md) binds the exact 16-file text package; [adoption metadata](../../../docs/handoffs/harness-publication-readiness/adoption.json) binds the nine-file patch, preimages and intended 0.4.0 candidate. Root remains 0.3.0, without applied root LICENSE/NOTICE; no new adoption is inferred from merge. |
| Controls | Local CODEOWNERS and CI require review and run complete validation with the archive guard. That source configuration does not establish effective remote enforcement, bypass restrictions or public fork behavior. Prior gaps remain unverified until refreshed. |
| Reporting | The maintained security guide uses intended public PVR and a safe fallback; the handoff records unverified public Harness reporting. Prior organization pilot/internal receipt do not prove this audience. No synthetic message is sent at Gate 1. |
| Package/use | Canonical root and exact references remain; the predecessor records private 0.4.0 rehearsal, first-use Gate 1, failure/migration/recovery cases and unchanged real consumers. No public access or current-runtime claim follows. |
| Enforcement | `scripts/validate/run.sh` runs plugin/SDD validation and maintained validator/execution suites. Existing tests cover v3 planning/impact/evidence freshness, CI baseline/archive gates, execution and consumer recovery. They do not inspect live rights, remote payloads, control enforcement or confidential receipt. Design must add meaningful reviewed evidence procedures for those gaps, without weakening suites. |

The impact ledger classifies every one of the predecessor's 38 scenarios exactly once, retaining current invariants and extending unresolved work. Its H01/H02/root-package/user-documentation origins were inspected in the prior assessment and remain preserved through this delivered successor; this change introduces no independent alteration to those historical dossiers. Historical stage events are provenance, not instructions to repeat already delivered work. Two additional current obligations bind the operational handoff and complete validation entry point. No intentional supersession or exemption is proposed.

## Impact and risks

- Confidentiality/history may make the existing-repository publication infeasible without a new owner decision. Do not assume that references are harmless or authorize disclosure; do not promise clearance before evidence.
- Missing service access or ineffective plan-dependent controls may prevent acceptance. An exact least-privilege request and observable alternative must be reviewed; unavailable capability is not a passed test.
- Reporting depends on audience and visibility. Keep genuinely post-publication tests explicit while completing every feasible private prerequisite; do not create circular pre-merge tasks.
- Rights and release scope can drift after text approval. Preserve immutable candidate approvals; review changed source/patch identities and actual capacity separately.
- New evidence may itself be sensitive. Restricted originals and access checks stay outside prospective public trees/history; safe summaries use minimal opaque references.
- Full package diagnostics verify mechanical regressions, not specialist review or public usability. New acceptance evidence must be attributable to the actual inputs and authorized action.

## Ownership and Design decisions

Accountable coordinator: existing owner `@elviszoz`; retain existing CODEOWNER assignments. This is not a new legal/security qualification claim. Reuse prior contacts and decisions while verifying current evidence access and actual reviewer capacities.

Gate 1 has no unresolved choice of target repository, license direction or current planning scope. Before Design approval, resolve the exact restricted-evidence access/collection boundary, feasible classification/treatment decision path, control capabilities and proposed corrections, reporting audience/dependencies, current candidate/runtime assessment and reproducible checks. Missing access may block Design readiness; a material treatment choice reopens the earliest affected gate. These questions do not authorize collection, remediation, configuration or messages now.

## Proposal acceptance criterion

The paired Requirements establish observable resolution, failure and boundary outcomes, retained impact and a clear distinction between pre-publication closure and later operational verification. Gate 1 approval permits Design only. Implementation cannot be reported complete while an in-scope pre-publication prerequisite remains unresolved; public-dependent checks remain mandatory external follow-up with no false pass.

## Planning review

Stage: Proposal/Requirements R1. Review: awaiting approval; approval null; no Gate 1 scope blocker. Operational blockers remain open as described above. The user's request authorizes preparation, not approval of these unseen files. No Design, Tasks, implementation ledger, license adoption or publication is performed.

Observed preparation checks on 2026-11-14, using Python 3.11.4, PyYAML 6.0.2 and jsonschema 4.23.0 with the five verified source anchors above:

- `PYTHONDONTWRITEBYTECODE=1 /private/tmp/versat-pr36-validation-venv/bin/python validators/sdd/validate.py --root . --change harness-publication-blockers --phase planning --json`: exit 0, pass, no findings or warnings; 31 local scenarios and 40 retained obligations (38 predecessor scenarios plus two current contracts).
- `PYTHONDONTWRITEBYTECODE=1 PYTHON=/private/tmp/versat-pr36-validation-venv/bin/python ./scripts/validate/run.sh`: final exit 0; Plugin and SDD validation pass, 131 validator tests and 48 execution tests pass. Historical legacy/v2 inventory warnings remain; no exemption or test was changed. The full command was repeated after clarifying that adoption/publication execution is outside scope while separately authorized control verification can belong to later implementation.
- Full review of both new files, 15 valid local Markdown links, explicit untracked whitespace checks and `git diff --check`: pass. All 1,551 pre-existing tracked files remain byte-identical. The only new repository files are Proposal and Requirements; all 38 predecessor acceptance positions are classified exactly once.
- Canonical combined Proposal/Requirements R1 digest: `d3552c1655c58d08d56c9c0178c75c50e804c171087b6d62a2f8be1e6147e5eb`. Obtain it with the same provider's `--change harness-publication-blockers --digest proposal`. This identifies the presented revision; it is not approval.

These are local planning diagnostics and maintained regression tests, not execution of the proposed resolution work or fresh operational clearance. No new implementation acceptance ledger, sensitive collection, remote CI run, control change, message, publication or consumer migration occurred. Gate 1 remains awaiting the user's review; approval is null.

### Gate 1 approval — 2026-11-14

The user explicitly approved the presented pair: “Sim, aprovo a Proposal e os Requirements R1 de harness-publication-blockers. Avance somente ao Design, sem iniciar a implementação ou publicar.” The combined digest was reverified unchanged before recording approval. This authorizes Design only. Earlier pending statements preserve the presentation history; current structured review is approved. Tasks, implementation and publication remain unauthorized.
