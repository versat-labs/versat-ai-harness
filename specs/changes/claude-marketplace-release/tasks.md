---
sdd_version: 3
change: claude-marketplace-release
tasks:
  - id: TASK-001
    description: Add .claude-plugin/plugin.json mirroring plugin.json identity with agents [] and .claude-plugin/marketplace.json (versat, owner, one versat-ai-harness github entry at the exact v<VERSION> tag).
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-002
    description: Implement validators/project/instructions.py (read-only import-only CLAUDE.md check with findings, remediation and exit status), document it in validators/project/README.md, and add import-only CLAUDE.md files at the root and in project-templates/base.
    requirements: [REQ-006]
    status: completed
  - id: TASK-003
    description: Extend validators/plugin/validate.py with Claude manifest, Claude catalog, cross-catalog ref and CLAUDE.md checks (reusing TASK-002), add tests/validators/test_plugin_claude.py and tests/validators/test_project_instructions.py, register them in scripts/validate/run.sh and update validators/plugin/README.md.
    requirements: [REQ-001, REQ-002, REQ-004, REQ-005, REQ-006]
    status: completed
  - id: TASK-004
    description: Add the Claude instruction entry-point rule and Claude memory reference to standards/core/agent-artifacts.md and link the consumer check from skills/project-audit/SKILL.md without restating the rule.
    requirements: [REQ-006]
    status: completed
  - id: TASK-005
    description: Write docs/user-docs/guides/claude-setup.md with aligned .pt.md and .es.md, add install lines to the three READMEs, link from workspace setup, document CLAUDE.md adoption in project-templates/README.md and the two-catalog tag-after-merge order in scripts/release/README.md.
    requirements: [REQ-003, REQ-004, REQ-006]
    status: completed
  - id: TASK-006
    description: Prepare release 0.5.0 by updating VERSION, the three manifests, both catalog refs and the base template .versat/standards.lock harness.version to 0.5.0/v0.5.0, moving Unreleased into a dated 0.5.0 CHANGELOG section with this change, and correcting the 0.4.0 heading to 2026-11-24.
    requirements: [REQ-004, REQ-005]
    status: completed
  - id: TASK-007
    description: Execute CHECK-001 to CHECK-006 and CHECK-008 on the final source with input snapshots, record evidence under docs/validation/claude-marketplace-release and assess all 21 acceptance positions and 7 regression obligations.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
    status: pending
  - id: TASK-008
    description: Prepare the validated dossier under specs/archive/claude-marketplace-release with closure prepared in the same branch and pass delivery with --require-archive.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
    status: pending
review:
  revision: 3
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 6b3f2794954ddda85128da6d43f495adff3cc0f20a667854da4b13b346a15429
    design: 8c75656c935c80892399ac61a56b8633ee01f26d4b08108f95bc0d3edde82557
  approval: null
validation:
  plan_digest: dd5dac3144088ebeb3bf04388c04f0a17e5c98e5c107d66632592173f051dd31
  results:
    - check: CHECK-001
      result: pass
      evidence: docs/validation/claude-marketplace-release/check-001.txt
      revision: "Working tree of commit a57f29baae8a84a571fb1d805ae1cb8a34a07186 before evidence files"
      input_digest_before: "cb277b152d3b942c457321042d839903ec69d7b74ffa024f212e658a0903b009"
      input_digest_after: "cb277b152d3b942c457321042d839903ec69d7b74ffa024f212e658a0903b009"
      context:
        execution: local
        environment: "Linux container, Python 3.13, Ruff 0.14.14, Claude Code 2.1.332"
        observed: true
    - check: CHECK-003
      result: fail
      evidence: docs/validation/claude-marketplace-release/check-003.txt
      revision: "Working tree of commit 5d77d73a93ec4a2560ac91c213cf7d14f970e8ef (implementation) before evidence files"
      input_digest_before: "24335effa5391573e7591d815efa1449ef90de3b367045029718537fd8f0c7e4"
      input_digest_after: "24335effa5391573e7591d815efa1449ef90de3b367045029718537fd8f0c7e4"
      context:
        execution: local
        environment: "Linux container, Python 3.13, Ruff 0.14.14, Claude Code 2.1.332"
        observed: true
    - check: CHECK-004
      result: pass
      evidence: docs/validation/claude-marketplace-release/check-004.txt
      revision: "Working tree of commit 5d77d73a93ec4a2560ac91c213cf7d14f970e8ef (implementation) before evidence files"
      input_digest_before: "a54c0111decb472d6d9c559f31be22344b7845bbad3d18fb3a6dd21ae982ae11"
      input_digest_after: "a54c0111decb472d6d9c559f31be22344b7845bbad3d18fb3a6dd21ae982ae11"
      context:
        execution: local
        environment: "Linux container, Python 3.13, Ruff 0.14.14, Claude Code 2.1.332"
        observed: true
    - check: CHECK-005
      result: pass
      evidence: docs/validation/claude-marketplace-release/check-005.txt
      revision: "Working tree of commit 5d77d73a93ec4a2560ac91c213cf7d14f970e8ef (implementation) before evidence files"
      input_digest_before: "5bd9ea7666fb111c0c96d2ca0c84caa322334fd63c30f98be94bf0cca12a1f0f"
      input_digest_after: "5bd9ea7666fb111c0c96d2ca0c84caa322334fd63c30f98be94bf0cca12a1f0f"
      context:
        execution: local
        environment: "Linux container, Python 3.13, Ruff 0.14.14, Claude Code 2.1.332"
        observed: true
    - check: CHECK-008
      result: pass
      evidence: docs/validation/claude-marketplace-release/check-008.txt
      revision: "Working tree of commit a57f29baae8a84a571fb1d805ae1cb8a34a07186 before evidence files"
      input_digest_before: "638cf441c6f22be7c35c51ac4184991d160345bacdf94816fd95de543d71a7a3"
      input_digest_after: "638cf441c6f22be7c35c51ac4184991d160345bacdf94816fd95de543d71a7a3"
      context:
        execution: local
        environment: "Linux container, Python 3.13, Ruff 0.14.14, Claude Code 2.1.332"
        observed: true
  assessments: []
  findings:
    - id: FIND-001
      source: {plan: "CHECK-003 expected observations"}
      category: contradicts
      state: open
      evidence: docs/validation/claude-marketplace-release/check-003.txt
      description: claude plugin validate passes with an additional warning that root CLAUDE.md is not loaded as plugin context; Design R3 accepts only agent frontmatter and icon warnings. The root CLAUDE.md is required by REQ-006 for repository sessions, so the check expectation, not the implementation, needs review.
      tasks: [TASK-007]
      checks: [CHECK-003]
closure: active
---

# Tasks

- [x] TASK-001 — Claude manifest and catalog
- [x] TASK-002 — Consumer instruction check and import-only CLAUDE.md files
- [x] TASK-003 — Plugin validator extension, tests and runner registration
- [x] TASK-004 — Agent Artifact Standard rule and audit link
- [x] TASK-005 — EN/PT/ES Claude guidance, READMEs, template migration and release procedure
- [x] TASK-006 — Release 0.5.0 version and changelog preparation
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

Tasks R2 binds to Proposal/Requirements R3 and Design R3; TASK-006 now includes the base template lock version. Presented for Gate 3. The owner approved Tasks R2 and authorized implementation with “Sim, aprovo as Tasks R2 e pode implementar” under digest `dd5dac3144088ebeb3bf04388c04f0a17e5c98e5c107d66632592173f051dd31`. Planning is complete. This does not authorize marking the PR ready, merging, tagging or releasing.

Tasks R2 is superseded by Design R4 (CHECK-003 expectation revised for FIND-001); its approval above is historical. Implementation progress and evidence are preserved and will be rerun under the revised plan.

Tasks R3 binds to Design R4; task descriptions, dependencies and completion conditions are unchanged from R2. TASK-001 to TASK-006 remain completed; TASK-007 reruns every required check under this plan. Presented for Gate 3. No approval recorded yet. Tasks approval ends planning; implementation requires an explicit request.

## Progress

TASK-001 to TASK-006 implemented. The quality check requires a new note under `## [Unreleased]` in every PR that changes non-exempt paths, so the release keeps an Unreleased section with “No changes since 0.5.0.” and moves the prior entries into `## [0.5.0] - 2026-11-28`; adjust the date if the merge happens on a later day. Guides state that tags before v0.5.0 have no Claude catalog, so Claude recovery pins v0.5.0 or later.

## Validation evidence

CHECK-001, 002, 004, 005, 006 and 008 passed with identical before/after input digests. CHECK-003 failed its declared expectation: `claude plugin validate .` passed with warnings, but besides the accepted agent-frontmatter and icon warnings it reported `root: CLAUDE.md at the plugin root is not loaded as project context` (FIND-001). The root CLAUDE.md is intended for repository sessions (REQ-006.1, verified by CHECK-005), so resolving this needs a Design revision of CHECK-003's accepted warnings. CHECK-005 also showed that Claude Code loads no project instructions from directories inside the session scratchpad; the base-template copy was rerun outside it. Assessments are pending the FIND-001 decision.

The first full run also exposed that the Plugin validator, by importing `validators/project/instructions.py`, wrote `__pycache__` into validator inputs and made results look stale. Commit a57f29b stops bytecode writing during that import (routine implementation fix). CHECK-001 and CHECK-008 were rerun on that commit and passed. CHECK-002 and CHECK-006 results were withdrawn because their inputs changed (validator fix and the Unreleased note); CHECK-002 cannot pass while FIND-001 keeps a recorded failure in this dossier, so both rerun after FIND-001 is resolved.

## Delivery

Closure is active.
