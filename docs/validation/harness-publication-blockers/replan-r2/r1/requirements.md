---
sdd_version: 3
change: harness-publication-blockers
requirements:
- id: REQ-001
  statement: Establish an exact, current and privately reviewable baseline for each unresolved publication prerequisite.
  acceptance:
  - Given the merged preparation and HPR-PRIVATE-01, reconcile the exact source commit, candidate text/patch identities,
    remote surfaces and dated observations into a blocker register with scope, evidence revision/access, accountable
    reviewer and capacity, status, next action and observable exit condition; reuse existing ownership decisions without
    treating them as specialist clearance.
  - Given an inaccessible or changed restricted record, retain the last observation as historical and the current
    result as unverified; obtain scoped access or a review by an authorized custodian rather than copying sensitive
    evidence into the prospective public repository or treating an opaque reference as proof.
  - Given a claimed resolution, an authorized reviewer can inspect the underlying evidence and its limits; a scan,
    owner declaration, old approval or structural pass alone cannot close the blocker. New collection and permission
    expansion require a bounded reviewed scope and the applicable authority.
- id: REQ-002
  statement: Complete the previously inaccessible publication-surface review and verify that the review still covers
    the exact intended exposure.
  acceptance:
  - Given the prior 16-category assessment, refresh all categories and investigate the recorded package listings,
    cache payloads, external attachment bodies and integration payload gaps. Record actual reviewed content or demonstrated
    absence with method, date and limits; HTTP errors, empty partial listings and unavailable payloads are not proof
    of absence.
  - Given current files, reachable/deleted history, branches/tags, releases/assets, LFS, fixtures, SDD/evaluation
    records, issues/PRs/comments/attachments, wiki/discussions/Pages, packages and CI logs/artifacts/caches, bind
    the reviewed inventory to the actual prospective exposure, including new planning and review artifacts; a clean
    release ZIP or default-branch tree does not clear other surfaces.
  - Given new refs, artifacts, attachments, permissions or source changes after review, identify affected categories,
    invalidate their clearance and repeat the affected review. If required access cannot be obtained, retain an open
    blocker with its owner and stop dependent publication; do not close this work by relabelling the gap as optional.
- id: REQ-003
  statement: Resolve the confidentiality and immutable-history conflict through an attributable decision before any
    exposure.
  acceptance:
  - Given an internal-reference indicator or sensitive-history finding, an authorized reviewer determines its actual
    sensitivity and exposure scope in restricted storage. A non-sensitive finding can close only with review evidence;
    a sensitive finding requires an approved, feasible treatment and verification, not a blanket acceptance of confidential
    disclosure.
  - Given a proposed treatment, compare its effect on the existing-repository direction, original approvals, evidence
    retention, reachable copies and recovery. Preserve authentic restricted originals and an attributable correspondence
    for any proposed changed public surface; deleting or moving a current file does not resolve historical exposure.
  - Given a treatment that fits the approved scope and is specifically authorized, verify the exact affected surfaces
    after execution before closing the finding. If it requires destructive cleanup, history rewriting, a different
    destination, lost provenance or a material licensing change, keep publication deferred and reopen the relevant
    planning gate with the concrete decision; this plan does not select or authorize those operations.
  - Given an unresolved treatment, rejected review or failed reinspection, leave the associated requirement incomplete
    and publication deferred. Producing a decision memo or an additional defer assessment alone does not satisfy resolution
    of the confidentiality blocker.
- id: REQ-004
  statement: Refresh rights, third-party and exact candidate applicability evidence without adopting a license.
  acceptance:
  - Given the approved Apache R1 wording, seven preserved dependency-license texts and the nine-file adoption patch,
    review source and distribution changes since their bounded baseline, record actual grants/notices and reviewer
    capacity, and distinguish unchanged text approval from rights to the final proposed tree; preserve the original
    approval and package identities.
  - Given missing rights, incompatible terms, unconfirmed review capacity, changed candidate wording or a patch/preimage
    mismatch, stop dependent adoption and resolve the specific evidence or renewed review requirement; do not silently
    rebase the approved candidate, overwrite its approval, invent an effective date or rely on old passes.
  - Given a consistent reviewed candidate, record its source, patch, preimages, resulting test-tree identity and intended
    exact version separately from the unchanged canonical root. Any authorized rehearsal uses a disposable private
    copy, verifies matching package resources and preserves third-party notices; no root license, tag, release or
    consumer migration is implied.
- id: REQ-005
  statement: Establish evidence of effective contribution and repository controls for the intended publication sequence.
  acceptance:
  - Given the actual repository and audience, inspect effective branch/ruleset protection, required reviews/CODEOWNERS,
    required checks, bypass and force-push permissions, and fork workflow token/secret boundaries. Distinguish configured,
    enforced and inaccessible states; local YAML or administrator access is insufficient.
  - Given a missing or ineffective control, prepare the exact least-privilege correction, affected actors, expected
    enforcement, test and rollback for review. Apply a correction only after its scoped operational authorization,
    then observe allowed and denied behavior without exposing secrets; unavailable platform capability or authority
    remains a blocker.
  - Given controls whose behavior changes with visibility or fork audience, establish all verifiable pre-publication
    prerequisites and a mandatory post-visibility enforcement test with accountable owner and stop conditions. Pending
    post-visibility observations remain unverified and cannot be reported as public control assurance or replace feasible
    private checks.
- id: REQ-006
  statement: Resolve confidential-reporting prerequisites while preserving audience-specific verification and explicit
    message authority.
  acceptance:
  - Given the intended public Harness reporting route, confirm its actual destination, accountable responder, allowed
    recipients, intended reporter, access prerequisites and platform/visibility dependencies. Reuse the existing maintainer
    decision and prior limited H02 evidence without treating another repository or internal email receipt as public
    Harness verification.
  - Given a separately authorized route configuration or synthetic test, use a non-sensitive marker and the intended
    available audience, observe private receipt by authorized recipients and denial to unauthorized viewers, and retain
    minimal restricted evidence. No message, endpoint activation or permission change follows merely from planning
    approval or a general diagnostic request.
  - Given a route that cannot be exercised for the public audience until visibility changes, verify the available
    private prerequisites and bind the remaining public test to the later authorized operation. Missing/failed receipt
    or access keeps that claim unverified; retain the existing safe request-for-private-instructions fallback, with
    no invented endpoint, internal address, SLA or retention period.
- id: REQ-007
  statement: Produce an evidence-based pre-publication decision that cannot conceal unresolved blockers or premature
    public claims.
  acceptance:
  - Given all required pre-publication evidence, reconcile exact rights/surface dispositions, confidentiality treatment,
    effective controls and reporting prerequisites with actual reviewers, current source identities and required checks.
    Close each blocker only against its observable exit condition; unresolved pre-publication items leave this successor
    incomplete and the publication decision deferred.
  - Given prerequisites that inherently require public visibility, identify them individually as mandatory post-publication
    verification, with owner, trigger, audience, expected evidence and failure/containment response. The pre-publication
    decision may state ready for separately authorized operations, but must not claim public reporting, anonymous
    installation, completed H03 or migration until those outcomes are observed.
  - Given a later adoption/publication request, provide the exact reviewed action boundaries, immediate drift checks,
    sequencing and stop conditions for adoption, visibility, exact release, external acquisition/install/update/contribution,
    reporting and controls. Preserve evidence on failure; reverting metadata or visibility cannot promise to revoke
    distributed copies or granted rights. Adoption, visibility, release and real consumer-migration execution remain outside this successor.
- id: REQ-008
  statement: Preserve package behavior, usable guides and independent product boundaries during blocker resolution.
  acceptance:
  - Given any later authorized change to current guidance or a rehearsal candidate, preserve the canonical root, marketplace
    and Plugin identities, explicit exact-version installation/update/recovery and matching Skills/Standards/SDD/templates/validators.
    Retest affected behavior including missing resources/version and failed-update recovery; historical client passes
    do not establish current or anonymous use.
  - Given changed community instructions or status, keep English, Portuguese and Spanish semantically aligned, verify
    local links/anchors and representative affected steps, and preserve a self-contained contribution/reporting route
    without private links or payloads; unobserved behavior stays labelled pending. Technical planning artifacts remain
    English only.
  - Given other products, organization defaults or destination projects, preserve their independent terms, delivery,
    access and review contracts; do not absorb Platform/Workspace/Discover/CRM, organization rollout, hiring or commercial
    work, add a mirror/SDK, repin installed consumers or weaken maintained validation suites.
- id: REQ-009
  statement: Retain immutable predecessor evidence and validate new resolution claims with fresh, non-circular evidence.
  acceptance:
  - Given the archived predecessor and approved candidate, preserve their bytes and genuine review records; record
    this successor under its own ID. New safe status records identify which dated observations they supersede without
    rewriting historical approvals, results or source hashes; sensitive evidence stays in the approved restricted
    system.
  - Given a new resolution claim, record actual method, inputs, environment/audience, before/after identities, result
    and reviewer limits; retain failed attempts and rerun affected checks after drift. Missing execution is unverified
    and not not-applicable; no old result or edited label becomes acceptance of this successor.
  - Given delivery validation, use meaningful current evidence for every local and retained scenario and the complete
    required package suites. Keep pre-merge work independent of its own final merge/publication; assess post-publication
    obligations as handoff completeness only and never as executed public outcomes.
- id: REQ-010
  statement: Stop current work at Gate 1 and preserve separate authority for every later phase and operation.
  acceptance:
  - Given this request, create only Proposal and Requirements R1 for harness-publication-blockers, with assessed impact,
    awaiting-approval and null approval. Run bounded local planning diagnostics while leaving implementation, living
    guides, candidate text, licenses/manifests and remote state unchanged; no Design, Tasks or ADR draft is created.
  - Given approval of this exact paired revision, prepare only Design; Tasks requires Design approval, and implementation
    requires approved Tasks plus an explicit execution request. Material scope or remedy changes reopen the earliest
    affected gate rather than silently extending authority.
  - Given historical authorizations, reviewer assignments or successful checks, infer no new permission for sensitive
    collection, permission/control changes, report messages, commit/push/PR/merge, license adoption, visibility, tag/release,
    consumer migration or destructive remediation. Present concrete operations for their applicable scoped authorization;
    unknown evidence never grants authority.
---

# Requirements

## Actors and context

The accountable owner reviews scope and gates; authorized technical, rights and security reviewers inspect the relevant evidence in their actual capacities. An administrator executes only separately authorized operations. The intended external reporter/contributor and current internal consumer have different access boundaries. No contact, credential or sensitive payload is reproduced here.

## Functional requirements

REQ-001 establishes the current blocker/evidence baseline. REQ-002 and REQ-003 resolve inaccessible surfaces and confidentiality/history disposition. REQ-004 refreshes rights and candidate applicability. REQ-005 and REQ-006 establish effective controls and reporting prerequisites. REQ-007 defines the resulting pre-publication decision and separately authorized operational handoff.

## Non-functional requirements

REQ-008 retains usable package/guidance and independent products. REQ-009 preserves attribution and current evidence; REQ-010 enforces the current Gate 1 boundary and later authority. Resolve policy through canonical Standards rather than copying it into a new Skill or distribution mechanism.

## Acceptance scenarios

The frontmatter arrays are normative one-based scenarios. Design must map every local scenario and retained impact obligation to meaningful checks, with justified exclusions only where applicable. Reuse existing mechanical tests; missing live evidence cannot be replaced by file-presence checks. Preserve missing access, uncertain rights, confidential history, denied permissions, route failure, source drift and failed-update recovery cases.

Current authorization permits no acceptance execution beyond bounded planning diagnostics. Later implementation must distinguish actual blocker resolution from an assessment that simply restates defer. Public visibility, anonymous install/update/contribution, public-audience reporting and post-visibility controls remain unverified until the separately authorized operations actually occur. The pre-publication handoff is testable before merge; it is not evidence those future operations succeeded.

## Constraints and assumptions

- Only Proposal and Requirements are created now, in English. Gate 1 acceptance unlocks Design, not implementation, adoption or publication.
- Existing repository, canonical root, Apache direction, third-party terms, marketplace/Plugin identities and reviewed 0.4.0 candidate intent remain; root and installed consumers are not repinned.
- Historical approvals and evidence remain byte-identical. No waiver of confidentiality or silent destructive cleanup is permitted; an infeasible treatment requires explicit replanning.
- The approved restricted evidence system is reused subject to actual access verification. Raw payload review/collection is future bounded work, not a side effect of this planning request.
- Actual control corrections, channel setup and synthetic messages need concrete scope and authority even after the SDD plan is approved. Public release and effective adoption are outside this successor.
- Documentation and preparation can be reviewed privately while publication remains deferred. Completion of this successor requires the defined pre-publication exit conditions, not merely another defer report.
- Other repositories, product licenses, organization defaults and commercial/hiring initiatives remain independent.
