---
sdd_version: 3
change: add-sifen-skill
tasks:
- id: TASK-001
  description: Inventory the supplied package and record provenance, integrity and
    permission disposition.
  requirements:
  - REQ-002
  - REQ-004
  status: completed
- id: TASK-002
  description: Import and adapt the portable English skill, references and optional
    adapter guidance.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  status: completed
- id: TASK-003
  description: Adapt lookup and export utilities and add maintained behavior tests.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  status: completed
- id: TASK-004
  description: Integrate package discovery, the full validation runner and aligned
    usage documentation.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  status: completed
- id: TASK-005
  description: Execute the approved checks and assess every acceptance and regression
    obligation.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  status: blocked
- id: TASK-006
  description: Prepare the validated dossier for documentary delivery in the same
    branch.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  status: blocked
review:
  revision: 2
  state: approved
  blockers: []
  upstream:
    proposal: 063fe58b812b25111c3d7737dd29a645f0a93e653f0a1c69da4806701b41c35a
    design: 285fd45ef6cbaafdbd7fdb0028051b0a4400f5062df0e0e3dfc9703d1051dfb1
  approval:
    source: Developer reply after Tasks revision 2 presentation in this chat
    quote: Aprovado
    revision: 2
    digest: c5beeeccd35539e7950ea4b2c165ad0f2e2d0d73426a797512b9835bb6c0b424
validation:
  plan_digest: c5beeeccd35539e7950ea4b2c165ad0f2e2d0d73426a797512b9835bb6c0b424
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    revision: Approved Tasks R2 working-tree snapshot, 2026-11-18; bound input hashes
    input_digest_before: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    input_digest_after: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    context:
      execution: local
      environment: macOS; Python validation venv; standard-library utilities; no live
        tax services
      observed: true
  - check: CHECK-002
    result: unverified
    evidence: docs/validation/add-sifen-skill/r2/review.md
    revision: Approved Tasks R2 working-tree snapshot, 2026-11-18; bound input hashes
    input_digest_before: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    input_digest_after: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    context:
      execution: local
      environment: macOS; Python validation venv; standard-library utilities; no live
        tax services
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    revision: Approved Tasks R2 working-tree snapshot, 2026-11-18; bound input hashes
    input_digest_before: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    input_digest_after: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    context:
      execution: local
      environment: macOS; Python validation venv; standard-library utilities; no live
        tax services
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/add-sifen-skill/r2/snapshot-lookup/observed-response.md
    revision: Approved Tasks R2 working-tree snapshot, 2026-11-18; bound input hashes
    input_digest_before: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    input_digest_after: 41fc5daa6756699284a13de3251d6e21e3309c2a4c0249c04e0476f290880df6
    context:
      execution: local
      environment: macOS; Python validation venv; standard-library utilities; no live
        tax services
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: Current technical/source-boundary observations satisfy the mapped
      behavior.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: Current technical/source-boundary observations satisfy the mapped
      behavior.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: unverified
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/add-sifen-skill/r2/review.md
    explanation: Technical observations recorded; the required source-permission review
      remains unverified under CHECK-002.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: unverified
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/add-sifen-skill/r2/review.md
    explanation: Technical observations recorded; the required source-permission review
      remains unverified under CHECK-002.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: unverified
    checks:
    - CHECK-002
    evidence: docs/validation/add-sifen-skill/r2/review.md
    explanation: Technical observations recorded; the required source-permission review
      remains unverified under CHECK-002.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: unverified
    checks:
    - CHECK-002
    evidence: docs/validation/add-sifen-skill/r2/review.md
    explanation: Technical observations recorded; the required source-permission review
      remains unverified under CHECK-002.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: unverified
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/add-sifen-skill/r2/review.md
    explanation: Technical observations recorded; the required source-permission review
      remains unverified under CHECK-002.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: Current technical/source-boundary observations satisfy the mapped
      behavior.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: Current technical/source-boundary observations satisfy the mapped
      behavior.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: Current technical/source-boundary observations satisfy the mapped
      behavior.
  - obligation:
      regression:
        impact: 1
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/add-sifen-skill/r2/full-validation.txt
    explanation: All existing entry points and full maintained suites plus 15 SIFEN
      tests pass.
  findings:
  - id: FIND-001
    source:
      local:
        requirement: REQ-002
        scenario: 3
    category: missing
    state: open
    evidence: docs/validation/add-sifen-skill/r2/official-source-verification.md
    description: Official DNIT publication and unauthenticated access verified. Express
      permission/equivalent reviewed basis for repackaging the official corpus remains
      unverified; inspected page reserves rights. Apache authorization covers authored
      material only. Maintainer follow-up before distribution.
    tasks:
    - TASK-005
    - TASK-006
    checks:
    - CHECK-002
closure: active
---

# Tasks

- [x] TASK-001 — Inventory the supplied package and record provenance, integrity and permission disposition.
- [x] TASK-002 — Import and adapt the portable English skill, references and optional adapter guidance.
- [x] TASK-003 — Adapt lookup and export utilities and add maintained behavior tests.
- [x] TASK-004 — Integrate package discovery, the full validation runner and aligned usage documentation.
- [ ] TASK-005 — Execute the approved checks and assess every acceptance and regression obligation.
- [ ] TASK-006 — Prepare the validated dossier for documentary delivery in the same branch.

## Dependencies and completion conditions

### TASK-001: Inventory and provenance

Dependencies: current Tasks approval and explicit implementation authorization.

Record every supplied file's source path, hash, disposition and intended target path; exclude OS metadata and identify authored versus official imported material. Recheck the 35 original-manifest entries and preserve the original manifest. Inspect source content for sensitive material. Create the in-skill provenance record and target-path integrity inventory without exposing personal absolute paths. Record inspectable authorship/permission evidence or the concrete missing evidence and its maintainer follow-up. Retain the developer’s declared authorship and explicit Apache-2.0 instruction as observed authorization for authored material. Do not infer third-party rights or apply that grant to official sources.

Completion: the inventory is complete, source dependencies and transformations are explicit, and rights status is accurately recorded. An unresolved rights disposition may be documented as deferred; that completes inventory work only and continues to block CHECK-002 and delivery. No source-folder changes are permitted. Supports CHECK-001 and CHECK-002.

### TASK-002: Skill and resources

Dependencies: TASK-001 inventory and file classification; local reviewable preparation may proceed with deferred distribution status.

Create `skills/sifen-electronic-documentation/` with the approved English entry point, translated authored references and optional adapter guidance. Retain official source bytes, exact identifiers and the declared snapshot date. Apply the approved path mapping and update all relative links, manifests and examples. Replace machine-specific paths with explicit `SIFEN_SKILL_ROOT` or a verified repository-relative location. Resolve corporate context through the canonical Standards index. Clearly distinguish exported guidance, installed corpus and native agent registration. Include the full verbatim Apache-2.0 LICENSE, NOTICE attribution, LICENSE-SCOPE.md and Python SPDX markers. Verify authored material is covered while official originals, extracts, XML examples and the original manifest are excluded. Preserve the rest of the Harness licensing state and update provenance and target-integrity records.

Completion: each included source has a disposition, links resolve, authored content is English, official-source hashes remain attributable, missing-resource/current-compliance limitations are documented and no adapter has been activated in this or another project. The licensing records must match the developer’s actual authorization, identify exact text hashes and preserve official-source exclusions. Supports CHECK-001, CHECK-002 and CHECK-004.

### TASK-003: Utilities and deterministic tests

Dependencies: TASK-002 paths and resource layout.

Implement standard-library `query_rules.py` and `export_agent.py` with the English interfaces in Design. Preserve literal lookup, bounded results/context and explicit regex handling; make invalid options and missing corpus fail clearly while treating no-match as an ordinary result. Preflight all export output collisions before creating any files; preserve existing content unless explicit force replacement is requested. Keep all five platform targets and make generated instructions point to usable installed resources.

Add `tests/skills/test_sifen_documentation.py` covering known/no matches, invalid regex/options, absent corpus, discovery and relative references, a relocated package, all platform exports, an existing later output in a multi-file export, preservation on collision and explicit replacement. Use temporary directories and synthetic data for writes. Assert observable results and file preservation rather than implementation wording.

Completion: CHECK-001 passes with actual test counts and intact original fixtures; relocation does not depend on Downloads. Supports CHECK-001 and CHECK-003.

### TASK-004: Package and usage integration

Dependencies: TASK-002 and TASK-003.

Add the capability to `validators/plugin/validate.py`'s expected skill set without removing existing entries or changing manifest discovery paths. Integrate the focused test suite into `scripts/validate/run.sh` without narrowing any required suite. Create the approved aligned English, Portuguese and Spanish usage guide and maintained community entry links. Document setup, the snapshot, command arguments, no-match/error behavior, export collision handling and the separate resource-location requirement. Align all three guides and entry points on the authored Apache-2.0 scope, excluded official sources and unresolved redistribution evidence. Include all translated README files in current check snapshots, as specified by Design revision 2.

Completion: package validation recognizes the added skill and retains the five existing skills; executable guide examples agree with the utility tests; language variants describe the same behavior and limits. VERSION, release references and installed consumer configurations remain unchanged. Supports CHECK-001, CHECK-002 and CHECK-003.

### TASK-005: Acceptance and regression evidence

Dependencies: TASK-001 through TASK-004; unresolved rights or unavailable supervised observations prevent successful completion.

Run CHECK-001 through CHECK-004 using the approved methods, input scopes and limits. Prepare versioned synthetic prompts/fixtures for the two supervised attempts and follow the existing supervised evaluation guide. Run one fresh revision 2 attempt per scenario sequentially (two invocations total), bounded to ten minutes each; preserve the revision 1 attempts, failures and missing observations. Capture the current provider identity and input digests rather than relabeling historical results. Review lookup citations and independently compare fixture state to establish read-only behavior; structural tests do not substitute for observed assistant behavior. Do not call production tax services or use production credentials.

Record actual commands, environment, before/after input digests and results under `docs/validation/add-sifen-skill/`. Record a separate assessment for each of the ten acceptance scenarios and the baseline regression obligation. Use stable finding IDs for open gaps. Resolve ordinary defects within approved scope and rerun affected checks; material scope or check-plan changes reopen the appropriate gate. For CHECK-002, compare the LICENSE text with the retained canonical Apache-2.0 text, record its SHA-256 and observed developer authorization, inspect NOTICE and scope exclusions, and verify no repository-wide adoption. Record CHECK-002 as unverified or failed if official-source permission evidence or required acceptance review is absent rather than treating the recorded limitation as permission.

Completion: every required check and mapped obligation has current passing evidence, no unresolved findings remain, the full repository runner passes and the final diff remains within approved scope. Local results do not establish remote CI, publication or regulatory certification.

### TASK-006: Documentary closure

Dependencies: TASK-005 complete and all current approvals/evidence valid.

Read and follow the archive workflow at that phase. Check delivery eligibility, then move the unique dossier to `specs/archive/add-sifen-skill/` in the same branch and prepare its closure metadata. Recheck links and run selected delivery with `--require-archive`, plus the required final repository checks. Preserve truthful distinctions between local preparation and external review/merge.

Completion: the archive guard and required checks pass with current evidence, all task states match their checklist and the dossier is ready for a separately authorized PR action. Do not create a PR, merge, publish, install into consumers or change visibility under this task plan. No task depends on a future merge to finish.

## Risks and recovery

Renamed paths and translation may corrupt utility references or normative meaning; the inventory, source hashes, relocation tests and semantic review address these risks. An exporter collision must not leave partial files. Deferred rights evidence and unavailable supervised observations remain delivery blockers. Revert the new capability, focused integration and related guide links together if needed; preserve the supplied source and existing capabilities. No new architecture or policy exception is introduced.

## Planning review

Proposal/Requirements revision 2 and Design revision 2 are approved. Tasks revision 2 is awaiting approval. It adds scoped Apache-2.0 verification, aligned documentation and the two bounded current-provider supervised attempts. Existing implementation authorization is retained for the unchanged work; execution of the revised task scope follows current Tasks approval. The revision 1 approval below remains historical.

Historical revision 1 approval:

```json
{
  "source": "Developer reply after Tasks revision 1 in this chat",
  "quote": "Aprovado. Pode implementar e validar.",
  "revision": 1,
  "digest": "dc0c03d67f7606d98d6fd923e741ba0085d711af65ce8433006869d72682e991"
}
```

## Progress

TASK-001 through TASK-004 were implemented locally under revision 1. TASK-001 and TASK-003 retain completed progress. TASK-002 and TASK-004 are reopened as pending for their revised licensing and documentation acceptance, although the requested files are already present. The original 15 focused tests and full 131-validator/48-execution/15-SIFEN suites passed. Two supervised attempts completed with unchanged fixtures and observed source-grounded answers. The later Apache-2.0 instruction changes the reviewed scope; current acceptance and archival await Tasks revision 2 approval and third-party source permission evidence. The scoped license is present as the developer-requested reviewable change. No commit, PR or release was created.

## Validation evidence

Historical execution is retained under docs/validation/add-sifen-skill/. Input snapshots for the four original checks matched at execution time. Subsequent scoped licensing edits make those runs historical; they are not rebound to current inputs. Tasks revision 2 is approved. Current results and all ten local assessments plus retained regression are recorded in metadata. All technical checks passed; CHECK-002 remains unverified for third-party source permission. TASK-005 and TASK-006 remain blocked; closure stays active. Final post-license automated results are recorded separately; see implementation-report.md for observed results and unresolved obligations.

## Delivery

Closure remains active. No documentary archival, PR publication, remote CI, merge or release is claimed.

Tasks revision 2 approved in this chat with “Aprovado”; existing implementation/validation authorization resumes for the approved revised scope.

Revision 2 validation completed on 2026-11-18. The complete runner passes (131 validator, 48 execution, 15 SIFEN tests). Two fresh sequential supervised attempts passed observable criteria with unchanged fixtures and matching check input hashes. Evidence: docs/validation/add-sifen-skill/r2/. FIND-001 remains open; no archival or publication readiness is claimed.

Official-source follow-up: the developer supplied the DNIT technical-documentation URL. Public access and Manual/NT 27 download links were verified; the inspected page reserves rights and supplies no express repackaging grant. See r2/official-source-verification.md. FIND-001 remains open for distribution acceptance; no new planning revision is required for this evidence update.
