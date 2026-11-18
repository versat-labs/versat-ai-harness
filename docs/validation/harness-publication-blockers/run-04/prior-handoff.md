# Harness publication blockers — current operational handoff

Observed 2026-11-14. Accountable coordinator: @elviszoz. Implementation of the approved successor is authorized; **pre-publication resolution is incomplete and publication remains deferred**. This technical handoff preserves the [delivered predecessor](../harness-publication-readiness/README.md) and its dated evidence. It does not claim completed H03, a public release, adopted terms or migrated consumers.

## Current evidence and scope

The [input manifest](review-inputs.json) records six open blocker IDs, all 16 exposure categories, exact historical evidence hashes and actual observed reviewer capacities. [Run 01](../../validation/harness-publication-blockers/run-01/) retains the initial technical checks; [Run 02](../../validation/harness-publication-blockers/run-02/) records the newly authorized restricted inventory and its limits. Source baseline is `4a56181d3597c5d345a7639f013547e1700420cb`; new local changes are reviewed separately. Historical results are not current acceptance.

The 16 [approved candidate texts](../../licensing/candidates/apache-2.0/APPROVAL.md), including seven preserved dependency-license texts, match their approved hashes. The exact [nine-file patch and preimages](../harness-publication-readiness/adoption.json) match the current root. This establishes integrity, not rights or confidentiality clearance of the final distribution. Canonical root remains 0.3.0; 0.4.0 is a private rehearsal candidate. No root LICENSE/NOTICE, release, visibility or consumer change is applied.

| Blocker | Current evidence | Owner action and observable exit |
|---|---|---|
| HPB-001 — restricted originals/access | Both original hashes and all 96 manifest entries still match. The authorized inventory preserved 97 exact copies and bound 320 files locally with owner-only access. Earlier remote-path 404 remains historical; no remote delivery or actual human review is established. | Preserve the exact originals in the existing restricted system under scoped write/delivery authority, verify an immutable revision and have the actual reviewers inspect it. Preserve existing originals byte-for-byte. |
| HPB-002 — exposure completeness | The authorized inventory covered 1,616 current files, 1,244 remote blobs, 19 PR heads and 58 CI log archives/115 entries. Package listing still lacks scopes; two cache payloads and two external integration link occurrences remain unreviewed. | Obtain inspectable repository-specific package/cache/integration evidence from an authorized custodian using existing access. Complete attributable review; inaccessible results remain open, not absent. |
| HPB-003 — confidentiality/history | A frozen private queue identifies 82 location/type entries, including repeated indicators across snapshots. These are review candidates, not confirmed disclosures. No accountable classification or verified treatment is inferred. | Review exact findings privately. Close only with attributable benign disposition or verified, authorized treatment. A history rewrite, destructive cleanup, changed destination or lost provenance requires replanning. |
| HPB-004 — current rights | Text/patch integrity is verified; 202 committed path changes from the predecessor's source base and this successor's additions require a current scope review. | Review actual grants, notices, generated/copied material and final candidate scope in the declared capacity. Missing evidence stays unverified; no specialist qualification is inferred. |
| HPB-005 — effective private controls | `main` is unprotected; protection and ruleset reads return HTTP 403 with a capability limitation. Both existing CODEOWNERS have observed admin permission; neither has supplied a new eligible review. | Owner arranges supported private protection capability, then authorizes the concrete correction/test below. No spending, public conversion or bypass is authorized. |
| HPB-006 — reporting prerequisites | Intended destination remains this repository's PVR; its private-state read returned 404. Maintainer fallback and existing owner remain. Public receipt/exclusion are unverified. | Confirm actual responder/recipient arrangements and complete feasible private prerequisites. Bind public-only activation/receipt/exclusion to the later separately authorized operation. |

Only HPB-001–HPB-006 are blocker identifiers. This table is a safe index, not the restricted finding register or a substitute for reviewing originals. A closed local test cannot close any of these operational blockers automatically.

## Authorized inventory scope and remaining review

The user explicitly authorized this bounded inventory on 2026-11-14: “Sim, autorizo o inventário restrito no escopo do handoff, sem ampliar permissões, apagar histórico ou publicar. Prossiga.” Collection and exact local preservation were executed as recorded in run-02. The following scope continues to govern remaining review; no remote publication, access expansion, deletion or remediation was performed. Local hashes/custody do not imply durable remote delivery or actual human acceptance:

1. **Preserve existing evidence:** use the existing restricted evidence system selected by ADR-0016. Verify every file against the existing integrity manifest before any write. Preserve HPR-PRIVATE-01 without modifying its bytes; create a new attributable preservation/access record in a new `docs/validation/harness-publication-blockers/<run>/` area there. Confirm the target remains private and actual reviewers can inspect the immutable revision. Remote commit/push/PR of restricted records requires its own explicit scope and that repository's governance; no new destination or sharing is proposed.
2. **Collect only the Harness exposure:** current source plus reachable/deleted objects and refs; releases/assets and LFS; fixtures/SDD/evaluation records; issue/PR/comment/review bodies and their directly linked attachments; enabled wiki/discussions/Pages; repository-related package listings/payloads; CI logs/artifacts/caches; relevant repository metadata/integration payloads. Include new planning and handoff files. Enumerate each collection completely with page counts and stable object/ref IDs before asserting coverage.
3. **Minimize and retain privately:** collect only within that repository and directly relevant payload boundaries. Stop at unrelated repositories, inaccessible package scopes, unsupported cache extraction, third-party attachment hosts requiring new access, or external integration boundaries. Use inspectable authorized-custodian evidence where direct access is unavailable. Request no token dump, blanket permission expansion, deletion, sharing or retention change. Record failed reads as unavailable, never absent.
4. **Review actual findings:** existing owner coordinates identified technical/rights/security reviewers in their actual capacities. Record source, sensitivity, evidence revision/access, proposed treatment, authority, preconditions, exit test and result. Agent scans are aids, not human classification or rights grants. Changes to history/destination/licensing reopen the affected gate before action.
5. **Publish only safe evidence locally:** bind the new restricted ID/revision/digest into the safe manifest after preservation and access verification. No private URLs, payloads, internal addresses, report bodies or raw findings enter Harness. Re-freeze inputs and rerun affected checks after any source/evidence drift.

Exit evidence includes exact immutable originals and manifests, reviewer access and capacity, all category observations, actual classification/treatment review and verification. Until available, TASK-001–TASK-003 cannot be completed. No assumption about another reviewer's consent or access closes this dependency.

## Private control correction and test envelope

**Target:** `versat-labs/versat-ai-harness`, default branch `main`, still private. **Before-state:** observed unprotected with capability HTTP 403. Capability must be actually available before mutation. Preserve CODEOWNERS and use an eligible non-author reviewer; current admin permissions do not constitute that review.

**Proposed minimal delta, requiring scoped operational authority:** PR integration; at least one eligible non-author approval and applicable CODEOWNER approval; dismiss stale approvals; require the actually observed `structural-validation` check from GitHub Actions; enforce against ordinary admin/role bypass; disallow force pushes and branch deletion. Preserve existing stricter rules and read-only workflow tokens. Do not add signing, unrelated restrictions or release automation. Reobserve current configuration and check application identity before deriving the final service payload; do not apply a speculative payload while the API is unavailable.

**Bounded test:** one disposable non-sensitive test branch/PR targeting main, only after explicit test-PR authority. Use a reversible invalid manifest to produce a real failing required check, observe blocked mergeability/missing-review state, then correct it and obtain an eligible real review to observe the permitted state. Capture configuration readback, actual check/review identities, actor permissions and service mergeability. Do not merge or attempt force push/deletion against main. No agent-generated review impersonates a person. Test-PR creation and later cleanup are separately scoped; preserve evidence before cleanup.

**Failure/containment:** stop if capability, check application, actor eligibility or enforcement differs. Preserve the prior configuration and operation evidence privately. Any rollback is separately reviewed against that exact before-state; do not disable working protection automatically. No purchase or subscription change is proposed by this operation. Public-fork behavior must be rechecked after separately authorized visibility.

GitHub documents plan-dependent private protection in [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), consulted 2026-11-14. The actual service response above is the current capability observation; it is not a recommendation to expose the repository.

## Reporting procedure and public-only follow-up

The intended destination is the Harness repository's native PVR, accountable coordinator @elviszoz. Existing CODEOWNERS coordinate triage; actual authorized recipients and an intended external reporter must be recorded before a test. Observed admin permission alone does not establish receipt or user consent. Preserve the [safe fallback](../../user-docs/guides/security-reporting.md): request private instructions through an existing maintainer contact without vulnerability details.

[GitHub documents PVR for public repositories](https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories), consulted 2026-11-14. The current private-state 404 is not proof of enabled/disabled public routing. No private PVR pass, marker submission or channel activation is recorded.

After separate visibility authority and a verified public destination, the later operator must:

1. Obtain exact authority for PVR activation and one synthetic non-sensitive report, identify an intended external reporter, the actual permitted recipient set and an independent unauthorized-viewer account. Do not use real vulnerability data.
2. Reobserve the repository identity/visibility and reporting configuration. Activate only the agreed route; inspect intended-reporter access. A wrong repository, changed destination, inaccessible route or unconfirmed actor stops the test.
3. Submit a uniquely labelled synthetic verification marker, retain its actual private identifier in restricted storage and confirm actual private receipt by the authorized responder. Record submission and receipt separately. Do not publish an advisory or request a CVE.
4. Verify that an unauthorized account cannot access the private report; an authenticated administrator view is insufficient. Missing receipt, unauthorized visibility or an inaccessible observation leaves the check incomplete and withdraws active-route claims.
5. Preserve evidence and the fallback. Any cleanup, configuration reversal or further message requires its applicable scope. Reverify after audience, recipient or configuration drift. Invent no mailbox, SLA or retention period.

Prior pilot/internal H02 receipt retains its original audience and repository. It cannot replace any step above. No test message is sent under the present implementation request.

## Later adoption, publication and consumer sequence

All steps below are outside this successor's execution authority. Owner: @elviszoz, coordinating the actual responsible reviewers/operators.

| Step/trigger | Required input and observation | Stop/containment |
|---|---|---|
| Reconcile immediately before adoption | Closed pre-publication blockers; current source/refs, reviewed rights, exact approved text/patch/preimages, current controls, current check results, intended version availability. | Any drift or missing review stops; re-review affected evidence. |
| Apply separately approved root adoption | Exact nine-file patch on the reviewed source; inspect resulting license/notices/manifests and run complete suites. | Patch mismatch or altered wording requires renewed review; no silent regeneration. |
| Execute separately authorized visibility and exact release | Actual intended tree/tag identity, current protection and explicit visibility/tag/release scope. | Do not overwrite tags; no release/public claim without actual observation. |
| Verify intended external use | Anonymous acquisition, installation/resource resolution, first planning contribution, exact update and failed-update recovery under an account without private membership. | Missing/failed external case keeps availability unverified; preserve evidence. Private rehearsal is insufficient. |
| Verify public reporting and controls | Execute the reporting protocol above and actual post-visibility fork/check/review enforcement. | Keep fallback and withdraw unsupported claims; containment needs a concrete authorized scope. |
| Migrate consumers independently | Each target's reviewed exact old/new provider/lock pair, compatibility and observed recovery. | Preserve last compatible pair on failure. No `latest`, automatic migration or changes to other products' terms. |

Changing visibility or reverting metadata cannot retract public copies or previously granted rights. A final merge/release is never a prerequisite to completing pre-merge tasks. Current source review, implementation acceptance, documentary archival, PR review/CI, merge, adoption and publication remain distinct states.

## Resume and verification

Use the approved `harness-publication-blockers` dossier and current task statuses. Recompute all stage digests and provider anchors, resolve actual external prerequisites, then continue only authorized dependent work. The safe manifest is an included review input; changing it invalidates affected results. Reports under the excluded run directory do not hash themselves or grant approval. Failed/partial attempts remain preserved.

Local package/unit success proves only the executed technical scope. Full resolution requires all ten Design checks and individual assessment of 31 local plus 40 retained obligations. No historical pass, future procedure or defer memo substitutes for those outcomes.

## Inventory checkpoint — 2026-11-14

All 16 categories have dated observations. Current release/artifact listings are empty; wiki/discussions/Pages are disabled; no LFS pointers or binary blobs were found in the inspected reachable sets. These are bounded observations, not claims about inaccessible deleted objects or every external copy. Branch/tag observations remained stable and the forensic refs match the enumerated source. The private copies are investigation evidence, not a new distribution destination.

The repository-scoped package query returned insufficient scopes; no organization-wide package collection or privilege change followed. The documented cache API was reviewed, but no supported payload-read route was established; caches were not executed, extracted through a workaround or deleted. All acquired issue/PR/comment/review bodies were checked for plain URLs, Markdown targets and HTML src/href; two external integration links remain at the authorized boundary. Raw locations and values remain exclusively in the restricted record.

This changes included review inputs. The previous private client and suite results remain preserved historical executions; they are not relabelled as passes for the updated final candidate. Final candidate revalidation belongs after the unresolved reviews and source inputs are stabilized. No native scenario was repeated for this inventory.
