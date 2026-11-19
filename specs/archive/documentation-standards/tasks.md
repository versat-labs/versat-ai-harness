---
sdd_version: 3
change: documentation-standards
tasks:
  - id: TASK-001
    description: Define consumer documentation layout and preserve compatible bootstrap and ADR references
    requirements: [REQ-001]
    status: completed
  - id: TASK-002
    description: Guide documentation work through existing SDD stages
    requirements: [REQ-002, REQ-003]
    status: completed
  - id: TASK-003
    description: Write trilingual guidance and examples for publishing product documentation and feature pages
    requirements: [REQ-003, REQ-004]
    status: completed
  - id: TASK-004
    description: Build and test the deterministic advisory documentation report
    requirements: [REQ-005]
    status: completed
  - id: TASK-005
    description: Connect the optional report to Harness PR checks and document consumer adoption
    requirements: [REQ-005]
    status: completed
  - id: TASK-006
    description: Record current acceptance evidence and verify the integrated Harness change
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005]
    status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: "2fef179090a22f6c31db50ccf4fd99d7638fc559d5c176ecbb455b4f2493e2a4"
    design: "5643c1db95db9109e0f159a55a6083537fbecc33ab414a1626f1ff096e210a40"
  approval:
    source: "Developer approval and explicit execution request in this Codex conversation after the Portuguese reading translation of Issue #23 Tasks revision 1"
    quote: "Aprovo o plano de tarefas da revisão 1 da issue #23. Pode iniciar a implementação."
    revision: 1
    digest: "ff9b6805e77f8d7c211a09851ad9b313df4926bf9db1888aa9cd7a08873081f9"
validation:
  plan_digest: ff9b6805e77f8d7c211a09851ad9b313df4926bf9db1888aa9cd7a08873081f9
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/documentation-standards/check-001.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: e194cae45e50f8b88131b5dca5b30ec27f8ce78970a04c613ad8a8dee3e6f7b8
    input_digest_after: e194cae45e50f8b88131b5dca5b30ec27f8ce78970a04c613ad8a8dee3e6f7b8
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/documentation-standards/check-002.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: 2372bc84e1dff7d6917eaa350f4444db7d2747a23ff67a09d2e6576897730879
    input_digest_after: 2372bc84e1dff7d6917eaa350f4444db7d2747a23ff67a09d2e6576897730879
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/documentation-standards/check-003.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: 49a99331ad8f39b65fbf5e070797842bb02af5d6e960ad0cff94e47207f4ee6d
    input_digest_after: 49a99331ad8f39b65fbf5e070797842bb02af5d6e960ad0cff94e47207f4ee6d
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/documentation-standards/check-004.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: 3b506cc06528ff8d3cbc1dec4727fc9db15aa7c7bfd7154067072e680289e7ee
    input_digest_after: 3b506cc06528ff8d3cbc1dec4727fc9db15aa7c7bfd7154067072e680289e7ee
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/documentation-standards/check-005.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: 8078e04cec3ab08c46a78a248f7606b8710164ed296f9f50669c0920cfdeb685
    input_digest_after: 8078e04cec3ab08c46a78a248f7606b8710164ed296f9f50669c0920cfdeb685
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/documentation-standards/check-006.txt
    revision: Local implementation tree b561b69b1032137fb1f4f1f286506b9df380fc35 before final evidence
      bookkeeping
    input_digest_before: 6f4f08f7c279338beb987632c7119cb6f0523826739a56d689934ba393a07e26
    input_digest_after: 6f4f08f7c279338beb987632c7119cb6f0523826739a56d689934ba393a07e26
    context:
      execution: local
      environment: Darwin arm64, CPython 3.14.6, Git 2.54.0, local synthetic fixtures where applicable
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The usable fixture README resolved to the new quickstart. The standard assigns detailed
      guides to the user-docs guides directory.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The standard lists each applicable technical and reader path. The reader overview linked
      to the guide while shared bootstrap discovery remained in specs/product/overview.md. The explicit
      ADR reference resolved.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The empty fixture kept only inherited discovery, and the legacy fixture retained its
      working first-use link and identical lockfile bytes.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The scheduling fixture identified the operator, purpose, goal and existing guide. The
      revised guidance separates reader usage information from relevant technical rationale and contracts.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The CLI output matched the expected next run and supplied both product and guide evidence.
      The unavailable restricted UI was explicitly unverified.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The internal queue refactor had no user, contract or operations impact. The guidance
      required no guide or separate task.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/documentation-standards/check-003.txt
    explanation: English, Portuguese and Spanish siblings linked to each other and documented the same
      schedule outcome, access approval and recovery steps.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/documentation-standards/check-003.txt
    explanation: The localized guides labeled the English project-validation reference, and its reporting
      anchor resolved. The Documentation Standard refers to the current Language Standard.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/documentation-standards/check-004.txt
    explanation: The public preview tracked Reporting ownership, a chosen destination and approved revision,
      all locale links, a verified scheduled result and the prior revision for restoration.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/documentation-standards/check-004.txt
    explanation: The Support draft stayed outside the public preview. The pending record named its owner
      and the destination and access approval needed before exposure.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/documentation-standards/check-005.txt
    explanation: Synthetic Git snapshots produced actionable pass, fail and not-applicable rows, explicit
      unavailable results and human review items in the Markdown summary.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/documentation-standards/check-005.txt
    explanation: The workflow review and tests confirmed read access, GitHub summary output and unchanged
      structural and quality jobs. The mixed report showed satisfied and failed rules without presenting
      semantic compliance as automated.
  - obligation:
      regression:
        impact: 2
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The legacy fixture used its existing first-use guide without a duplicate or broken README
      link.
  - obligation:
      regression:
        impact: 2
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The empty fixture produced no quickstart or claim of usable behavior.
  - obligation:
      regression:
        impact: 4
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The usable fixture README pointed to the actual first-use guide.
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The revised standard calls for more detailed guides only when warranted. The empty base
      does not scaffold empty guides.
  - obligation:
      regression:
        impact: 4
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The guide and README navigation remained outside the SDD dossier. The ARCHIVE move navigation
      exercise is also documented in check-002.
  - obligation:
      regression:
        impact: 5
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The export fixture treated its guide update as part of the feature and validated the
      documented outcome.
  - obligation:
      regression:
        impact: 5
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The internal refactor did not add a separate documentation task.
  - obligation:
      regression:
        impact: 5
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The scheduling guidance was updated in its existing quickstart path.
  - obligation:
      regression:
        impact: 6
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The documented CLI action produced the stated next-run outcome.
  - obligation:
      regression:
        impact: 6
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The workflow still calls for verifying affected commands or UI steps against observable
      results. The restricted UI scenario exercised the explicit unavailable branch.
  - obligation:
      regression:
        impact: 6
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: Unavailable UI access was recorded as unverified without credit from the CLI check.
  - obligation:
      regression:
        impact: 6
        scenario: 4
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/documentation-standards/check-002.txt
    explanation: The fixture reused the observed functional action to verify the guide.
  - obligation:
      regression:
        impact: 7
        scenario: 1
    result: pass
    checks:
    - CHECK-006
    evidence: docs/validation/documentation-standards/check-006.txt
    explanation: Repository review confirmed the existing SDD process and three gates. Planning and validation
      still use the four dossier files and existing identifiers and evidence.
  - obligation:
      regression:
        impact: 7
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The base still owns discovery and leaves reader guidance out of an empty scaffold.
  - obligation:
      regression:
        impact: 7
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The legacy fixture preserved the first-use location and exact lockfile bytes. Adoption
      guidance requires a reviewed exact version.
  - obligation:
      regression:
        impact: 7
        scenario: 4
    result: pass
    checks:
    - CHECK-006
    evidence: docs/validation/documentation-standards/check-006.txt
    explanation: The revised Standard refers to Language and Security, and publication guidance sends
      disclosure review to the existing policy.
  - obligation:
      regression:
        impact: 8
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The base still contains the canonical discovery overview and composition guidance preserves
      inheritance.
  - obligation:
      regression:
        impact: 8
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/documentation-standards/check-001.txt
    explanation: The readable product overview links to maintained material while discovery remains in
      its shared source.
  - obligation:
      regression:
        impact: 9
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/documentation-standards/check-003.txt
    explanation: The three publication guides use the English canonical filename and .pt.md and .es.md
      siblings.
  - obligation:
      regression:
        impact: 9
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/documentation-standards/check-003.txt
    explanation: Language switches and the localized quickstart links resolved. The English-only reference
      is labeled and its anchor exists.
  - obligation:
      regression:
        impact: 9
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/documentation-standards/check-003.txt
    explanation: Operational review found equivalent prerequisites, access decisions, expected execution
      and rollback across the three languages.
  - obligation:
      regression:
        impact: 10
        scenario: 0
    result: pass
    checks:
    - CHECK-006
    evidence: docs/validation/documentation-standards/check-006.txt
    explanation: The implemented standard and guide use the existing policy ownership, and the advisory
      workflow adds read-only reporting independently of required validation and human decisions.
  findings: []
closure: prepared
---

# Tasks

- [x] TASK-001 — Update the canonical Documentation Standard, bootstrap and composition guidance. Define applicable default paths and working navigation. Preserve existing equivalent paths, exact version pins and the shared bootstrap discovery record. Explain use of explicit SDD paths for new consumer ADRs and compatibility with current short identifiers. Record the layout decision in ADR-0018 and update the decision index and architecture overview with the implemented behavior.

- [x] TASK-002 — Update the existing SDD templates and workflow guidance to identify readers, feature purpose, affected living material and applicable locales during planning. Carry that work through existing Design checks and Tasks. Update documentation with implementation and verify observed usage through the existing evidence contract. Cover a no-impact change and an unavailable usage check without adding a gate or dossier field.

- [x] TASK-003 — Add a discoverable publication guide under `docs/user-docs/guides/` with aligned English, Portuguese and Spanish versions. Include a publishable feature and a restricted case. A team following the examples can identify the owner, destination, audience, approved source revision, required locales, verification, maintenance and recovery steps or pending decision. The task delivers repository guidance and examples.

- [x] TASK-004 — Implement the report CLI under `validators/documentation/` and its local wrapper under `scripts/validate/`. Test a mixed comparison with satisfied and failed rows, including missing or empty counterparts and localized orphans. Also test complete removals, unrelated paths, moves, missing baseline or target inputs, safe rendering and bounded output. Completion requires actionable paths or reasons and clear human review items.

- [x] TASK-005 — Add the advisory PR job and opt-in consumer workflow example. Write an actionable job summary using read-only access. Document how to open it from the PR and adopt, troubleshoot or remove the integration with an exact provider pin. Verify the example against the adapter contract, preserve existing required jobs and finish the relevant ADR, architecture and Unreleased entries.

- [x] TASK-006 — Execute CHECK-001 through CHECK-006 against the completed change and capture the declared input snapshots before and after each check. Record outcomes and assess all 12 acceptance scenarios and 22 retained regression obligations on the current plan. Resolve in-scope findings and rerun affected checks after corrections. Completion requires the planned checks and full local Harness validation to pass, with actual evidence recorded.

## Dependencies and completion checks

| Task | Depends on | Completion check |
| --- | --- | --- |
| TASK-001 | None | CHECK-001 walks through new, empty and legacy consumers, including both ADR reference forms. |
| TASK-002 | TASK-001 | CHECK-002 traces the changed guide from planning to evidence and preserves navigation after dossier archival. |
| TASK-003 | TASK-001, TASK-002 | CHECK-003 compares language variants and technical links. CHECK-004 rehearses publication with public and restricted examples. |
| TASK-004 | TASK-001 | CHECK-005 exercises report decisions using representative repository snapshots and verifies the rendered output. |
| TASK-005 | TASK-004 | CHECK-005 verifies the adapter contract. CHECK-006 reviews permissions, presentation and preserved required checks. |
| TASK-006 | TASK-001, TASK-002, TASK-003, TASK-004, TASK-005 | The six checks, scenario assessments and local package validation cover the final implementation. |

A rendered report and workflow contract review are the local evidence for PR presentation. Record the report in a real PR only if observed after separately authorized publication of that PR. The pre-merge task plan does not depend on that external observation. Prepare documentary closure through the existing workflow after validation.

## Planning review

The developer approved revision 1 and explicitly requested implementation in the Codex conversation.

## Progress

All six approved tasks were implemented and verified locally.

## Validation evidence

All six checks passed on the declared inputs. The records in `docs/validation/documentation-standards/` include the layout and SDD walkthroughs, publication rehearsal, mechanical report tests, rendered samples and package validation. All 12 acceptance scenarios and 22 retained regression obligations were assessed. The restricted UI scenario verified unverified reporting. It did not verify the UI itself. GitHub's live PR rendering and public distribution were not exercised.

## Delivery

Documentary closure is prepared in the implementation branch. The selected delivery and archive preflights passed locally.
