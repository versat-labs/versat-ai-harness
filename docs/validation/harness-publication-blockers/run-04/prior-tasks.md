---
sdd_version: 3
change: harness-publication-blockers
tasks:
- id: TASK-001
  description: Reconcile current authority, source identity and restricted evidence access.
  requirements:
  - REQ-001
  - REQ-009
  - REQ-010
  status: blocked
- id: TASK-002
  description: Complete the exact exposure inventory and inaccessible-surface review.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-009
  status: blocked
- id: TASK-003
  description: Resolve confidentiality findings through verified, attributable treatment.
  requirements:
  - REQ-003
  - REQ-009
  - REQ-010
  status: blocked
- id: TASK-004
  description: Refresh rights evidence and verify the exact approved candidate and patch.
  requirements:
  - REQ-004
  - REQ-008
  - REQ-009
  status: blocked
- id: TASK-005
  description: Establish and verify effective controls while the repository remains private.
  requirements:
  - REQ-005
  - REQ-007
  - REQ-010
  status: blocked
- id: TASK-006
  description: Verify feasible reporting prerequisites and prepare public-audience verification.
  requirements:
  - REQ-006
  - REQ-007
  - REQ-010
  status: blocked
- id: TASK-007
  description: Prepare safe current guidance, the review-input manifest and operational handoff.
  requirements:
  - REQ-001
  - REQ-007
  - REQ-008
  - REQ-009
  status: in-progress
- id: TASK-008
  description: Exercise the exact private candidate, client behavior and recovery.
  requirements:
  - REQ-004
  - REQ-008
  - REQ-009
  status: blocked
- id: TASK-009
  description: Execute all required checks and assess every local and retained obligation.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  - REQ-009
  - REQ-010
  status: blocked
- id: TASK-010
  description: Reconcile final blocker closure, acceptance evidence and delivery prerequisites.
  requirements:
  - REQ-007
  - REQ-009
  - REQ-010
  status: blocked
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: d3552c1655c58d08d56c9c0178c75c50e804c171087b6d62a2f8be1e6147e5eb
    design: 67d7645746e0cd955cffc3e0a110a708b8bb99e25859bead72fcc2400fb93ea7
  approval:
    source: User reply in this chat on 2026-11-14 answering the explicit Gate 3 approval question for Tasks R1 while
      keeping implementation and publication suspended
    quote: sim
    revision: 1
    digest: 1aeb424124652464b6bf115fd7900f068e8e9c0af7eba0d95035e8229616dfa7
validation:
  plan_digest: 1aeb424124652464b6bf115fd7900f068e8e9c0af7eba0d95035e8229616dfa7
  results:
  - check: CHECK-001
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-001.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-002
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-002.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-004
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-004.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-005
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-005.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-007
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-007.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-008
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-008.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-009
    result: fail
    evidence: docs/validation/harness-publication-blockers/run-02/check-009.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  - check: CHECK-010
    result: unverified
    evidence: docs/validation/harness-publication-blockers/run-02/check-010.json
    revision: 4a56181d3597c5d345a7639f013547e1700420cb plus inventory-01 and included handoff revision 2
    input_digest_before: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    input_digest_after: 5a68467166a20d9c4057713632fe9548bb08492cd4d9b71965b011663886e027
    context:
      execution: local
      environment: Python 3.11.4; macOS arm64; read-only GitHub inventory; locally preserved restricted evidence;
        no remote writes
      observed: true
  assessments: []
  findings:
  - id: FIND-001
    source:
      plan: HPB-001 evidence-access
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: Both predecessor hashes and all 96 old manifest entries are intact; 97 exact copies and a new 320-file-bound
      inventory are locally preserved with owner-only access. Actual human review and durable remote custody remain
      unverified.
    tasks:
    - TASK-001
    - TASK-002
    - TASK-003
    checks:
    - CHECK-001
  - id: FIND-002
    source:
      plan: HPB-002 surface-review
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: 'Authorized inventory executed: 1616 current files, 1244 remote reachable blobs, 19 PR heads, 58
      log archives/115 entries. Package query has insufficient scopes; two cache payloads and two external integration
      link occurrences remain unreviewed.'
    tasks:
    - TASK-002
    - TASK-003
    checks:
    - CHECK-002
  - id: FIND-003
    source:
      plan: HPB-003 confidentiality
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: The private queue contains 82 location/type entries for accountable review, including duplicates
      across current/local/remote history. They are literal indicators, not 82 confirmed sensitive findings or an
      approved treatment.
    tasks:
    - TASK-003
    checks:
    - CHECK-002
    - CHECK-007
  - id: FIND-004
    source:
      plan: HPB-004 rights
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: Sixteen approved texts, including seven dependency texts, and nine preimages match; current final-scope
      rights review remains open.
    tasks:
    - TASK-004
    checks:
    - CHECK-003
  - id: FIND-005
    source:
      plan: HPB-005 private-controls
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: Current main is unprotected; protection and ruleset reads return capability HTTP 403.
    tasks:
    - TASK-005
    checks:
    - CHECK-004
  - id: FIND-006
    source:
      plan: HPB-006 reporting
    category: missing
    state: open
    evidence: docs/handoffs/harness-publication-blockers/review-inputs.json
    description: Private repository PVR read returns 404; actual public receipt/access remains unverified.
    tasks:
    - TASK-006
    checks:
    - CHECK-005
closure: active
---

# Tasks

## Scope and authority

This plan implements the approved [Proposal](proposal.md), [Requirements](requirements.md) and [Design](design.md) only after Gate 3 approval and a later explicit execution request. The current instruction authorizes Tasks preparation only. No task is completed by writing this plan or running planning diagnostics.

The selected scope resolves pre-publication prerequisites for the existing Harness. Effective license adoption, visibility, release/tag publication and real consumer migration remain outside this successor. Preserve the exact candidate, prior approvals and archived dossiers. Destructive remediation, changed publication destination, material licensing changes or a different control-timing approach require renewed planning; no task silently grants those powers.

Current source is `4a56181d3597c5d345a7639f013547e1700420cb`, branch `codex/harness-publication-blockers`. Keep the Proposal's exact provider anchors, the source SDD v3 contract and index-resolved Standards. No Story or new issue is associated; do not fabricate one or reopen predecessor issues. No commit, push, PR or remote update is authorized in this phase.

## Ordered implementation tasks

### Baseline and evidence access

- [ ] TASK-001 — Reconcile current authority, source identity and restricted evidence access.

**Requirements/checks:** REQ-001, REQ-009, REQ-010; CHECK-001 and CHECK-010.

**Dependencies:** approved Tasks plus explicit implementation authority. New sensitive collection, restricted-system writes or access expansion must have their own applicable bounded authority; predecessor permissions do not transfer.

**Work:** Reverify current stage digests, the five provider anchors, actual Python dependencies, Git state and source/remote drift. Preserve unrelated work. Verify the existing restricted system remains private, actual reviewers can inspect the exact HPR-PRIVATE-01 originals, and their durable restricted preservation and two bound hashes are supported by evidence. Record real reviewer capacities without asserting specialist qualification. Establish the new restricted run area and complete blocker register under the Design's data contract only when authorized. Preserve the predecessor area. Record each actual baseline, required missing input, next owner and exit condition; retain unknowns.

**Completion:** exact source/candidate identities and access/provenance are reconciled; authorized reviewers can inspect the required evidence; CHECK-001's missing-record, changed-hash and unconfirmed-capacity cases behave correctly. An opaque identifier, local readability or owner/admin assignment alone is insufficient. No implementation pass is inferred from current planning checks.

### Complete exposure inventory

- [ ] TASK-002 — Complete the exact exposure inventory and inaccessible-surface review.

**Requirements/checks:** REQ-001, REQ-002, REQ-009; CHECK-001, CHECK-002, CHECK-007 and CHECK-008 as mapped in Design.

**Dependencies:** TASK-001 and the specific read/collection/custodian authority for the proposed scope. This task can identify confidentiality findings for TASK-003; it cannot clear them itself through a clean scan.

**Work:** Reconcile all 16 predecessor categories and the new source/remote delta. Include new planning and handoff material, current tree, reachable/deleted history and refs, releases/assets, LFS, fixtures, governance/evaluation records, issue/PR/comment/attachment surfaces, optional site/discussion features, packages and CI logs/artifacts/caches. Investigate the recorded inaccessible package types, cache payloads, alternate attachments and integration payloads through scoped reads or an inspectable authorized custodian record. Record exact scope, pagination, actual content review or demonstrated absence, date, method and limits. Keep raw payloads and private references in restricted storage. Exercise incomplete-listing, inaccessible-payload and new-ref/drift cases.

**Completion:** every required category has an attributable complete observation, and unavailable inputs have actually been resolved rather than relabelled optional. Identified treatment findings are explicitly handed to TASK-003; complete inventory is not confidentiality clearance. Missing access leaves this task incomplete and the corresponding requirement unverified. Sensitive downloads or unrelated collection are not a fallback for missing authority.

### Confidentiality and history disposition

- [ ] TASK-003 — Resolve confidentiality findings through verified, attributable treatment.

**Requirements/checks:** REQ-003, REQ-009, REQ-010; CHECK-002, CHECK-007, CHECK-008 and CHECK-010.

**Dependencies:** TASK-001 and relevant TASK-002 observations. Any treatment must fit the approved Design and have the concrete authority needed for its actual operation.

**Work:** Have authorized reviewers classify every actual internal-reference/sensitive-history finding against its exact exposure. Record benign findings with evidence; for sensitive findings, preserve authentic restricted originals and review a feasible non-destructive treatment, affected copies/surfaces, provenance correspondence, exit test and recovery. Execute only a treatment within the approved scope and specific authority, then reinspect every affected surface. A current-file move cannot clear past blobs or remote copies. Preserve historical approvals and their actual meaning.

**Completion:** every in-scope confidentiality blocker has actual review and verified treatment or an evidence-backed non-sensitive disposition. Rejected treatment, incomplete reinspection or inaccessible affected copies prevent completion. If resolution requires destructive cleanup, rewriting history, losing provenance, changing destination or changing license direction, stop and reopen the relevant gate with the concrete decision; do not complete this task with another defer memo.

### Rights and candidate applicability

- [ ] TASK-004 — Refresh rights evidence and verify the exact approved candidate and patch.

**Requirements/checks:** REQ-004, REQ-008, REQ-009; CHECK-003, CHECK-006, CHECK-007 and CHECK-010 where applicable.

**Dependencies:** TASK-001; complete relevant surface findings from TASK-002 and treatment deltas from TASK-003 before final acceptance. Preliminary delta inspection may proceed earlier, but changes invalidate affected results.

**Work:** Refresh the proposed distribution inventory and inspect original/copied/generated material, actual grants, dependencies and notices. Reuse bounded predecessor evidence without widening its scope. Verify the 16 approved Apache candidate texts, seven preserved dependency-license texts, exact nine-file patch and preimages. Use `git apply --check` in a disposable private copy before an authorized private rehearsal application. Record actual rights reviewer/capacity, concrete terms, source/patch/test-tree identity and limits. Preserve root 0.3.0, the candidate 0.4.0 intent, marketplace/Plugin identities and all old approvals. Test missing grants, incompatible terms, changed wording and preimage mismatches.

**Completion:** rights for the reviewed proposed scope are supported, the exact approved candidate is applicable, and blocking cases stop rather than silently rebase or adopt. Missing rights/review, altered text or patch mismatch stays unresolved. Any candidate regeneration or substantive text change needs the relevant renewed review before acceptance. No effective root license, tag or release is applied.

### Private repository controls

- [ ] TASK-005 — Establish and verify effective controls while the repository remains private.

**Requirements/checks:** REQ-005, REQ-007, REQ-010; CHECK-004, CHECK-008 and CHECK-010.

**Current status: blocked.** The Design's 2026-11-14 observation reports `main` unprotected and protection/ruleset reads returning HTTP 403 with a plan-capability limitation. No resolution is recorded. This is an execution prerequisite, not an ambiguity in the task plan. Do not represent the current state as ready to execute or infer a purchase authorization.

**Unblock condition/owner:** the accountable owner arranges supported private-repository protection capability and it is actually reobserved available. Spending/subscription changes require their own authority. Recheck before execution; only actual evidence can change this task from blocked. Public conversion to unlock controls is outside the approved approach.

**Dependencies:** TASK-001, the capability above, an eligible existing author/reviewer arrangement and specific authorization for the exact control correction and bounded test branch/PR. No automatic CODEOWNER changes or bypass grants.

**Work:** Prepare the concrete operation envelope and apply/read back only the Design's minimal correction: PR integration, eligible non-author approval and applicable CODEOWNER review, stale-review dismissal, actual `structural-validation` check from the observed GitHub Actions source, ordinary bypass disabled, force pushes and branch deletion disabled. Verify read-only workflow tokens and no secret/privileged execution of untrusted contribution code. Under explicit test-PR authority, observe blocked mergeability with an actual failing required check/missing review, then correct the reversible invalid manifest and obtain a real eligible review to observe the permitted state. Do not merge. Do not attempt destructive or unauthorized main operations to prove denial. Scope cleanup separately and preserve evidence.

**Completion:** actual private-main enforcement, actor permissions, configuration readbacks and permitted/denied states agree under CHECK-004. An unsupported/inaccessible capability or unenforced rule does not pass. Public-fork and post-visibility rechecks remain explicit later obligations, not substitutes for feasible private enforcement. The task cannot finish while the recorded capability blocker persists.

### Reporting prerequisites

- [ ] TASK-006 — Verify feasible reporting prerequisites and prepare public-audience verification.

**Requirements/checks:** REQ-006, REQ-007, REQ-010; CHECK-005, CHECK-007, CHECK-008 and CHECK-010.

**Dependencies:** TASK-001. Any feasible private route configuration or non-sensitive message test needs its exact operation envelope and explicit scope; no message is authorized by planning approval.

**Work:** Reconfirm the intended repository-native PVR destination, current platform/visibility boundary, accountable triage, actual recipient permissions, intended reporter roles and safe fallback. Reuse the prior H02 observations only for their original repository/audience. Verify all feasible private prerequisites. If an authorized private test is necessary, record actual private receipt and unauthorized-viewer exclusion with a non-sensitive marker. Prepare an exact later public PVR activation/submission/receipt/exclusion procedure with authorization, actor, expected evidence and containment. Preserve the existing request-for-private-instructions fallback; invent no endpoint, mailbox, SLA or retention period.

**Completion:** CHECK-005 supports the private prerequisites and executable public-only follow-up, including wrong-repository, unavailable route, missing-receipt and changed-audience cases. Actual public activation/receipt remains unverified until a separately authorized post-visibility operation. This task does not require public exposure to finish, but cannot waive feasible private gaps or relabel the old pilot as a Harness public pass.

### Safe documentation and handoff inputs

- [ ] TASK-007 — Prepare safe current guidance, the review-input manifest and operational handoff.

**Requirements/checks:** REQ-001, REQ-007, REQ-008, REQ-009; CHECK-001, CHECK-007 and CHECK-008, with actual usage covered by CHECK-006.

**Dependencies:** reconciled observations from TASK-001–TASK-006. Drafts may accurately show open blockers; final closure statements depend on their verified resolution. No final pass is written in anticipation of tests.

**Work:** Prepare the Design's minimal scrubbed `docs/handoffs/harness-publication-blockers/review-inputs.json` and maintained handoff README. Bind exact restricted revisions and source/candidate identities without sensitive payloads, private URLs or self-hashes. State each disposition, owner, exit condition and actual reviewer capacity. Describe separate later adoption, visibility/release, anonymous acquisition/install/update/contribution, reporting/control rechecks and independent consumer migration, with immediate drift checks and bounded containment. Update only affected EN/PT/ES guides and navigation, retaining canonical sources and pending-state accuracy. Review each prospective public file independently and preserve other products/organization routes.

**Completion:** all changed guidance has equivalent meaning and working local links/anchors; the handoff clearly distinguishes verified private outcomes from mandatory public-only observations and actual publication authority. CHECK-007's history and privacy review passes. The manifest binds review inputs but does not prove review by itself. Final handoff acceptance is reconciled in TASK-009–TASK-010; a document cannot close real blockers.

### Private candidate and client behavior

- [ ] TASK-008 — Exercise the exact private candidate, client behavior and recovery.

**Requirements/checks:** REQ-004, REQ-008, REQ-009; CHECK-003, CHECK-006, CHECK-007 and CHECK-009.

**Dependencies:** TASK-004's valid candidate and the reviewed current guide/input set from TASK-007; applicable explicit implementation/rehearsal authority and an independently usable private client context. Preserve real workspace settings and consumers.

**Work:** Reverify the Design's selected Codex desktop 26.915.31945/build 9922, macOS 26.5.2 arm64 target and pinned Python environment before use. Use a separately namespaced private test installation and disposable copy of the canonical root; record exact source, patch, resulting tree, installed resources and synthetic provider/lock pairs. Exercise the six-case protocol: first-use Gate 1, missing provider, missing resources, unavailable exact version, explicit synthetic migration and failed-update recovery, with installation/resource verification as setup. Use the maintained fixtures and independent artifact verification. Respect one fresh native new-intent invocation, no automatic retry, at most 600 seconds for it, 300 seconds for each remaining case and 2,400 seconds for the suite. Preserve every attempt and unavailable telemetry/shared-permission limits.

**Completion:** actual client and package observations support all six cases; first-use creates only Proposal/Requirements with null approval and unchanged application/tests; failures preserve the last verified compatible pair. Run the complete maintained suites in preparation and candidate roots and retain separate identities. No public access or real migration is claimed. Missing test context is unverified; a material runtime/method change reopens Design instead of silently substituting a target.

### Final checks and individual acceptance

- [ ] TASK-009 — Execute all required checks and assess every local and retained obligation.

**Requirements/checks:** REQ-001–REQ-010; CHECK-001–CHECK-010 exactly as approved in Design.

**Dependencies:** actual work and evidence from TASK-001–TASK-008; unresolved pre-publication blockers prevent complete acceptance. Adequate current checks from earlier tasks may be retained only for unchanged inputs and execution context; do not rerun blindly or transfer results between roots.

**Work:** Freeze the final reviewed source/candidate artifacts and scrubbed input manifest after actual observations. For each required check capture the canonical before/after input snapshots, exact runtime/actor/environment, result, method and limitations. Keep restricted raw evidence outside Harness and scrubbed reports under new `docs/validation/harness-publication-blockers/<run>/` directories. Record one result per Design check and one assessment for each of 31 local scenarios and 40 retained obligations; preserve original sources and historical scope. Run the full required `./scripts/validate/run.sh` suites with the pinned environment in both preparation and patched roots, retaining actual nonzero counts and failures. Reconcile semantic adequacy and real authority under CHECK-010.

**Completion:** ten actual current required checks pass, all 71 obligations have adequate individual assessments, and there are no open findings or stale results. Synthetic stop cases do not close actual unresolved rights/history/control findings. Missing execution remains unverified, not not-applicable. A changed source/manifest or known remote drift invalidates affected results and requires current re-execution; never rewrite an old hash to keep a pass. The execution ledger is populated only during actual implementation, not now.

### Final resolution and acceptance record

- [ ] TASK-010 — Reconcile final blocker closure, acceptance evidence and delivery prerequisites.

**Requirements/checks:** REQ-007, REQ-009, REQ-010; CHECK-008 and CHECK-010, retaining all other required passing evidence.

**Dependencies:** TASK-001–TASK-009 completed with actual in-scope blocker resolution, current reviews and valid evidence. No future merge/publication event is a completion prerequisite for this private work.

**Work:** Reconcile the actual rights/surface/confidentiality/control/reporting-prerequisite decisions with the final ledger and safe handoff. Verify every pre-publication exit condition and the distinction between ready for separately authorized operations and public availability. Write a scrubbed acceptance record in the excluded current run output, preserve outstanding public-only follow-up as unverified, and align task status/checklists only with real completion. If final status changes any included handoff or guide, freeze again and rerun the affected checks before completing this task; do not publish future pass claims to avoid that work.

**Completion:** the final acceptance record matches the actual reviewed inputs, all tasks are truthfully complete, and every required pre-publication blocker is closed with inspectable evidence. No new rights grant, release, public-reporting result or consumer adoption is inferred. Ordinary selected delivery validation follows the completed ledger, not a circular prerequisite to recording it. Documentary archive preparation and later PR/merge controls are separate lifecycle actions with their actual authority, as described below.

## Dependencies and execution checkpoints

TASK-001 establishes the evidence/authority baseline. TASK-002 supplies surface findings to TASK-003; both feed the final rights/candidate review in TASK-004. TASK-005 and TASK-006 may be planned independently after TASK-001 but execute only when their respective capabilities and scoped authority exist. TASK-007 consolidates truthful guide/handoff inputs, TASK-008 verifies actual private usage, TASK-009 reconciles all checks, and TASK-010 records final acceptance. Partial independent progress never makes a blocked workstream complete.

The known TASK-005 capability blocker is explicit; the remaining tasks are pending rather than assumed ready to execute. Required payload access, inspectable rights evidence, actual reviewers and private client context must be checked when relevant. No stage approval replaces these prerequisites. Reuse existing owner decisions; ask only for a genuinely missing scope, capability or review decision, with the concrete action prepared for review.

There is no unresolved task-plan choice for Gate 3. The review `blockers` list concerns approval of this plan; it does not erase the blocked task or certify implementation readiness. Tasks approval completes planning only. The user's prohibition on implementation/publication continues until an explicit later instruction changes it.

## Evidence and freshness rules

Follow the [Design validation contract](design.md#validation-plan), [SDD metadata](../../../sdd/metadata.md) and resolved Standards. The source input scopes, output exclusions, check methods and local execution contexts remain exactly those approved in Design. The current dossier is bound by canonical stage/plan digests rather than raw mutable bookkeeping. The included safe review-input manifest is not an excluded report.

Once Tasks is approved and execution is authorized, compute the actual Tasks digest before recording results. Use `--input-digest CHECK-NNN` immediately before/after actual checks, separately for each root where applicable. Passing checks require unchanged before/after inputs and fresh external observations. Do not copy the preparation hash to the patched root. Outputs belong only in the excluded run directory; the final ledger, its guard result and a report's own hash are not prerequisites to themselves.

Maintain real attempts and stable findings, with actual check/task references and current resolution evidence. Failed/unavailable checks prevent readiness. All 31 local and 40 retained mappings are required; no new exclusion or waiver is introduced. Public-dependent scenarios are assessed for the approved handoff contract, never relabelled as executed public outcomes. No report is created now to simulate that future evidence.

## Documentary closure and operational follow-up

After actual task completion, run the selected ordinary delivery validator against the final ledger. It may expose stale or missing evidence; resolve it through authorized corrections and actual reruns before claiming readiness. When documentary closure is authorized, follow the archive workflow: unique dossier, same branch, `closure: prepared`, final selected `--phase delivery --require-archive` and the complete suite with the trusted baseline. Archive preparation, private PR publication, final remote review/CI and merge remain distinct. These future procedural checks do not imply authority in this Tasks-only request.

Adoption of root license/metadata, visibility/tag/release operations, anonymous installation/update/contribution, public PVR activation/receipt/exclusion, post-visibility control checks and real consumer migration remain separately authorized operational follow-up. Preserve their exact owners, triggers, inputs, expected evidence and failure response in the handoff. Do not add a pre-merge task that requires its own merge or public exposure to finish.

## Stop conditions and recovery

Stop dependent work for absent execution authority, mismatched stage/provider identities, substantive scope drift, unavailable required evidence/reviewer access, unsupported private protection, invalid candidate applicability, failed required tests or an unresolved confidentiality conflict. Preserve the evidence and current safe state. Controls and reporting tests never imply permission to send messages, merge, publish or spend.

Routine authorized fixes within Design rerun affected checks. New task content reopens Gate 3; broader design/requirements changes reopen the earliest affected gate. Destructive history remedies, destination changes and a public-first control sequence remain outside scope. Recovery preserves historical approvals and the last verified private installation; no revert promises to withdraw public copies or grants.

## Planning review

Tasks R1 is presented after the actual Design approval: “Sim, aprovo o Design R1 de harness-publication-blockers. Prepare somente as Tasks, sem iniciar a implementação ou publicar.” Both approved upstream digests remain unchanged.

Review is awaiting approval, approval null. Nine tasks are pending; TASK-005 is blocked by the recorded private-protection capability limitation. All ten checkboxes remain unchecked. Validation plan digest is null, results/assessments/findings are empty and closure is active. No implementation or publication is authorized or performed. The preparation diagnostics below do not resolve TASK-005 or execute the future acceptance checks.

### Actual preparation diagnostics — 2026-11-14

- Selected planning validation with the pinned Python environment: exit 1, one finding `APPROVAL_REQUIRED` for Tasks, no warnings. It recognizes 31 local scenarios and 40 retained obligations; all ten requirements remain unverified with zero implementation results or assessments.
- The new-change workflow expressly permits `blocked` for an actual unavailable prerequisite during Tasks preparation. The current validator's `executing` predicate treats every non-`pending` task status, including `blocked`, as execution and therefore requires Tasks approval even in planning phase. TASK-005 is truthfully blocked and remains so. No task status, approval, exemption or validator is changed to conceal this diagnostic. Actual Gate 3 approval is still pending; after it is received, record the real approval and rerun validation. A future clean approval diagnostic would not resolve the private-protection prerequisite or authorize execution.
- Full required command `PYTHONDONTWRITEBYTECODE=1 PYTHON=/private/tmp/versat-pr36-validation-venv/bin/python ./scripts/validate/run.sh`: exit 1 from the same SDD approval finding. Plugin validation passed; all 131 validator tests and 48 execution tests passed. Existing legacy/v2 inventory warnings remain. The aggregate command did not pass, despite the 179 passing tests. No provider, implementation or test code was changed.
- Proposal and Requirements bytes match their pre-Tasks copies. Design changed only in review bookkeeping to record the user's actual Gate 2 approval. Both approved upstream digests and all five provider anchors match the approved values. All 1,551 pre-existing tracked files remain byte-identical.
- Task coverage includes all ten requirements, with one unchecked checkbox per task and correct status/metadata correspondence. All 24 local Markdown links and anchors across the dossier resolve. Explicit new-file whitespace checks and `git diff --check` pass. No implementation ledger or prospective output was created.
- Canonical Tasks R1 digest: `1aeb424124652464b6bf115fd7900f068e8e9c0af7eba0d95035e8229616dfa7`. This identifies the presented revision; it is not approval or execution evidence.

Gate 3 remains pending. The only next requested action is review of Tasks R1. Approval would conclude the human planning gates while implementation, publication and the unresolved operational prerequisite remain separately constrained.

### Gate 3 approval — 2026-11-14

The user replied “sim” to the explicit question: “Você aprova as Tasks R1 no Gate 3, mantendo implementação e publicação suspensas?” This approves the presented Tasks R1 only. All three canonical stage digests were reverified unchanged before recording the approval above. Earlier pending statements and diagnostics preserve the presentation history.

The three human planning gates are now approved. Nine tasks remain pending and TASK-005 remains blocked by the private-protection capability prerequisite. All checkboxes remain unchecked, the implementation ledger remains empty and closure remains active. Approval does not resolve that prerequisite, authorize implementation or publication, or grant any remote operation or spending authority. A later explicit execution instruction is required before implementation can begin.

Post-approval diagnostics: selected planning validation passed (exit 0, no findings or warnings). The full required `./scripts/validate/run.sh` command with the same pinned Python environment passed (exit 0): Plugin/SDD checks, 131 validator tests and 48 execution tests. Historical legacy/v2 inventory warnings remain unchanged. The earlier `APPROVAL_REQUIRED` finding is no longer present after the actual approval was recorded; the validator/workflow status interpretation was not changed. Tasks content digest remains `1aeb424124652464b6bf115fd7900f068e8e9c0af7eba0d95035e8229616dfa7`; only review bookkeeping changed, and whitespace checks passed. These are planning diagnostics, not execution evidence or operational readiness.

## Progress

### Authorized implementation — 2026-11-14

The user explicitly requested: “Implemente as tasks.” All three R1 approvals and provider identities were verified before work. Entry implementation validation passed. This supersedes the earlier phase-only suspension for in-scope implementation; separately scoped collection, remote configuration/messages, delivery and publication retain their approved boundaries.

TASK-008 is completed for the approved private technical scope: exact disposable candidate and personal test installation, all six client cases, independent first-use artifact review, complete preparation/candidate suites and unchanged workspace installation. TASK-004's exact candidate applicability prerequisite is verified; its separate rights review is not complete. The test catalog and last verified private candidate remain available; real workspace 0.3.0 is unchanged. The one native attempt stayed within its bound; no automatic retry occurred. An initial coordinator assertion omitted the native agent's empty stderr evidence file; inspection corrected that checker expectation, and the failed coordinator attempt remains recorded.

TASK-007 has a concrete safe handoff/input manifest and aligned EN/PT/ES navigation, but final history/privacy acceptance depends on unresolved restricted findings. It remains in progress. TASK-001–TASK-006, TASK-009 and TASK-010 are blocked by the actual prerequisites recorded in FIND-001–FIND-006 and the handoff. No remaining task is marked complete by a defer memo or a synthetic pass.

Bounded existing-evidence verification found both predecessor hashes and all 96 manifest entries intact locally. The remote exact record read returned 404 and the local area is untracked; current reviewer access and durable preservation are unverified. Private main still lacks protection and the APIs report a capability limitation. No expanded raw collection, restricted-system write, remote correction, test PR or report message ran. Current rights/security review and reporting recipient confirmation remain outstanding.

The 16 approved texts, nine preimages and postimages match. Root remains 0.3.0 without effective license adoption. Seven tracked documentation files changed only to point to the new current status; every other pre-existing tracked file is unchanged. Current source delta, exact check results, tests and preservation evidence are in run-01. All historical approvals/candidate material remain intact.

### Authorized restricted inventory — 2026-11-14

The user approved the concrete handoff scope: “Sim, autorizo o inventário restrito no escopo do handoff, sem ampliar permissões, apagar histórico ou publicar. Prossiga.” The bounded inventory was executed into the existing restricted system under new local record HPB-PRIVATE-01, inventory revision 1. Its raw payloads, forensic Git copy, exact preserved originals, body/link records and reviewer queue remain outside Harness. No remote write, permission expansion, deletion, history change or publication occurred.

The 320-file integrity manifest was verified; the old 96 manifest entries and 97 exact preserved copies remain unchanged. Owner-only local read access is observed, but actual human acceptance and remote durability remain unverified. The collection covered 1,616 current files, 1,244 remote and 1,246 local reachable blobs, 19 PR heads, 58 log archives/115 entries and all acquired issue/PR/comment/review bodies. Current refs match and branch/tag observations remained stable. Package scopes, two cache payloads and two external integration link occurrences remain gaps; no boundary was bypassed. The 82 private location/type queue entries require actual classification and include duplicates; they are not 82 confirmed sensitive findings.

The new safe handoff/input revision invalidates broad-input results for the final candidate. Run-01 and its former ledger are preserved in run-02/prior-ledger.json. TASK-008's earlier completion remains true for its tested snapshot, but its current status is blocked pending final-source revalidation; no old hash or pass was transferred, and no second native attempt ran. TASK-007 remains in progress. The other eight tasks retain their operational blockers. This inventory advances TASK-001–TASK-003 without claiming full closure.

### Authorized decision preparation — 2026-11-14

The user replied “Ok. Prossiga.” to preparation of concrete review decisions. Restricted packet HPB-REVIEW-01 R1 now preserves all 82 queue entries as 85 occurrences across seven distinct values: one scanner false positive, two synthetic test identities and four actual context/classification decisions. The 320-file source inventory remains unchanged. A 283-row rights delta, three unsent custodian requests, empty attributable decision fields and operational prerequisite actions are prepared. No human classification, rights approval, custodian receipt or control capability was inferred.

A local disposable-copy fixture passed plugin validation before mutation, failed on the intentional template version mismatch and passed after exact restoration. The existing applicable CODEOWNER scope supports a future eligible non-author review without changing owners; actual participation and remote enforcement remain unverified. All task statuses and six findings remain unchanged. [Run 03](../../../docs/validation/harness-publication-blockers/run-03/) contains only safe preparation metadata and actual diagnostics; raw values and evidence stay restricted. No remote operation, message, native rerun or publication occurred.

## Validation evidence

[Run 02](../../../docs/validation/harness-publication-blockers/run-02/) records the current restricted inventory, safe hashes, reference reconciliation and limits. [Run 01](../../../docs/validation/harness-publication-blockers/run-01/) remains historical: one native first-use invocation and five other client cases passed, and both roots ran the full 179-test suites before the final aggregate failed on recorded operational gaps. Those results are not current passes for the changed review inputs. The prior ledger is preserved; no old result was rehashed.

Six stable findings remain open. Final individual assessment of 31 local and 40 retained obligations remains incomplete. Current checks record only actually executed review/validation, with fresh input snapshots. Run-02 executed the complete preparation suite: 131 validator and 48 execution tests passed; the aggregate failed on the six true operational acceptance gaps. The strategy consumer validator separately passed with 9 Standards and 13 verified snapshots. Incomplete/unavailable work cannot be waived by successful integrity or unit checks.

## Delivery

Active, incomplete implementation. No archive preparation, repository commit/push/PR/merge, effective license adoption, visibility change, release, test report message or real consumer migration. Synthetic local provider commits are test fixtures only. Resume after the handoff's actual evidence/access, review and private-capability prerequisites are supplied; remote actions retain their concrete scoped authority.
