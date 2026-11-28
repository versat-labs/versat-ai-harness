---
sdd_version: 3
change: claude-marketplace-release
tasks:
  - id: TASK-001
    description: Add .claude-plugin/plugin.json mirroring plugin.json identity with agents [] and .claude-plugin/marketplace.json (versat, owner, one versat-ai-harness github entry at the exact v<VERSION> tag).
    requirements: [REQ-001, REQ-002]
    status: pending
  - id: TASK-002
    description: Implement validators/project/instructions.py (read-only import-only CLAUDE.md check with findings, remediation and exit status), document it in validators/project/README.md, and add import-only CLAUDE.md files at the root and in project-templates/base.
    requirements: [REQ-006]
    status: pending
  - id: TASK-003
    description: Extend validators/plugin/validate.py with Claude manifest, Claude catalog, cross-catalog ref and CLAUDE.md checks (reusing TASK-002), add tests/validators/test_plugin_claude.py and tests/validators/test_project_instructions.py, register them in scripts/validate/run.sh and update validators/plugin/README.md.
    requirements: [REQ-001, REQ-002, REQ-004, REQ-005, REQ-006]
    status: pending
  - id: TASK-004
    description: Add the Claude instruction entry-point rule and Claude memory reference to standards/core/agent-artifacts.md and link the consumer check from skills/project-audit/SKILL.md without restating the rule.
    requirements: [REQ-006]
    status: pending
  - id: TASK-005
    description: Write docs/user-docs/guides/claude-setup.md with aligned .pt.md and .es.md, add install lines to the three READMEs, link from workspace setup, document CLAUDE.md adoption in project-templates/README.md and the two-catalog tag-after-merge order in scripts/release/README.md.
    requirements: [REQ-003, REQ-004, REQ-006]
    status: pending
  - id: TASK-006
    description: Prepare release 0.5.0 by updating VERSION, the three manifests, both catalog refs and the base template .versat/standards.lock harness.version to 0.5.0/v0.5.0, moving Unreleased into a dated 0.5.0 CHANGELOG section with this change, and correcting the 0.4.0 heading to 2026-11-24.
    requirements: [REQ-004, REQ-005]
    status: pending
  - id: TASK-007
    description: Execute CHECK-001 to CHECK-006 and CHECK-008 on the final source with input snapshots, record evidence under docs/validation/claude-marketplace-release and assess all 21 acceptance positions and 7 regression obligations.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
    status: pending
  - id: TASK-008
    description: Prepare the validated dossier under specs/archive/claude-marketplace-release with closure prepared in the same branch and pass delivery with --require-archive.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
    status: pending
review:
  revision: 2
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 6b3f2794954ddda85128da6d43f495adff3cc0f20a667854da4b13b346a15429
    design: 5a31b8cfacb94274d7ce44c9222f59a5dbcefe990daadc58c900d67df4cc9284
  approval: null
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks

- [ ] TASK-001 — Claude manifest and catalog
- [ ] TASK-002 — Consumer instruction check and import-only CLAUDE.md files
- [ ] TASK-003 — Plugin validator extension, tests and runner registration
- [ ] TASK-004 — Agent Artifact Standard rule and audit link
- [ ] TASK-005 — EN/PT/ES Claude guidance, READMEs, template migration and release procedure
- [ ] TASK-006 — Release 0.5.0 version and changelog preparation
- [ ] TASK-007 — Execute required checks and record evidence
- [ ] TASK-008 — Documentary archive preparation

## Dependencies

- TASK-003 depends on TASK-001 and TASK-002.
- TASK-005 depends on TASK-001 and TASK-004 (guides describe the final catalog and rule).
- TASK-006 depends on TASK-001 to TASK-005 (versions and changelog cover the final content).
- TASK-007 depends on TASK-006; CHECK-004 and CHECK-005 use an isolated scratch CLAUDE_CONFIG_DIR and a local test catalog, deleted afterwards.
- TASK-008 depends on TASK-007 passing.

Completion conditions: each implementation task is complete when its files exist and `./scripts/validate/run.sh --quality-base origin/main` passes; TASK-007 when every required check has a recorded pass; TASK-008 when delivery with `--require-archive` passes.

## Post-merge operational follow-up

Not part of the pre-merge completion gate: after merge and with scoped administrator authority, create the annotated tag `v0.5.0` on the merge commit and the GitHub release from the 0.5.0 CHANGELOG section, then record CHECK-007 observations (tag target, Claude marketplace add/install, ChatGPT refresh) as observed or unverified.

## Planning review

Tasks R1 (digest `88b5463ccc1ed9eb5a64f7d53e08e1e721293c396ecd5ecb6890450c8ce58081`) was presented for Gate 3 and not approved; it is superseded by Proposal/Requirements R3.

Tasks R2 binds to Proposal/Requirements R3 and Design R3; TASK-006 now includes the base template lock version. Presented for Gate 3. No approval recorded yet. Tasks approval ends planning; implementation requires an explicit request. Tasks approval ends planning; implementation requires an explicit request.

## Progress

No task has started.

## Validation evidence

No check has been executed for this plan.

## Delivery

Closure is active.
