---
sdd_version: 3
change: claude-marketplace-release
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
adrs: [ADR-0011, ADR-0021]
validation:
  - id: CHECK-001
    description: Verify Claude manifest, Claude catalog, cross-catalog version agreement and import-only CLAUDE.md through maintained validator tests.
    requirements: [REQ-001, REQ-002, REQ-004, REQ-006]
    required: true
    method:
      kind: automated
      procedure: >-
        Run python -m unittest tests.validators.test_plugin_marketplace tests.validators.test_plugin_claude.
        Expect the existing Codex catalog tests to pass unchanged in intent and new tests to assert:
        valid package passes; Claude manifest name, version, description or repository drift fails;
        Claude manifest without agents [] fails; Claude catalog with wrong name, missing owner, zero or
        two versat-ai-harness entries, non-github source, wrong repo, branch/latest ref or ref other than
        v<VERSION> fails; Codex and Claude refs that differ fail; root or base-template CLAUDE.md that is
        missing, lacks @AGENTS.md or contains extra instructions fails.
    inputs:
      include: [.claude-plugin, .codex-plugin, .agents/plugins, plugin.json, VERSION, CLAUDE.md, AGENTS.md, project-templates/base, validators/plugin, tests/validators/test_plugin_marketplace.py, tests/validators/test_plugin_claude.py, tests/fixtures/marketplace-transition]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-002
    description: Retain the complete repository and quality validation on the final source.
    requirements: [REQ-004, REQ-005]
    required: true
    method:
      kind: automated
      procedure: >-
        Install requirements-validation.txt (including Ruff 0.14.14) and run
        ./scripts/validate/run.sh --quality-base origin/main. Expect every suite to pass, the plugin
        validator to report version 0.5.0 in all manifests and v0.5.0 in both catalogs, and the changelog
        check to find a 0.5.0 section. CI on the PR revision must also pass.
    inputs:
      include: [skills, standards, validators, scripts, tests, sdd, schemas, project-templates, agents, plugin.json, .codex-plugin, .claude-plugin, .agents, VERSION, CLAUDE.md, AGENTS.md, requirements-validation.txt, CHANGELOG.md, README.md, README.pt.md, README.es.md, docs/user-docs, docs/decisions]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-003
    description: Validate the package and catalog with the native Claude Code validator.
    requirements: [REQ-001, REQ-002]
    required: true
    method:
      kind: automated
      procedure: >-
        Run claude plugin validate . (non-strict) from the repository root with Claude Code 2.1.332 or
        later. Expect a passing verdict whose Provides list contains the seven versat-ai-harness Skills and
        no agents; the only accepted warnings are missing agent frontmatter in agents/*.md (unregistered
        role guidance) and the plugin-directory icon advice, which applies only to official directory
        submission. Record the output.
    inputs:
      include: [.claude-plugin, skills, agents, plugin.json, README.md]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-004
    description: Install the candidate in an isolated Claude configuration and confirm Skills resolve canonical resources from the installed root.
    requirements: [REQ-001]
    required: true
    method:
      kind: manual
      reason: The installed layout and Skill resolution are only observable through a real Claude Code installation; the v0.5.0 tag does not exist before merge, so a local test catalog stands in for the github source.
      procedure: >-
        With CLAUDE_CONFIG_DIR set to a new empty scratch directory, copy a git archive snapshot of the
        candidate to scratch, replace only its catalog source with "./", run claude plugin marketplace add
        <snapshot> and claude plugin install versat-ai-harness@versat. Expect the installed version 0.5.0,
        claude plugin list showing it enabled, the seven Skills and no plugin agents. Then run a non-interactive
        session asking the versat-sdd Skill to report its resolved VERSION, sdd/process.md and
        standards/index.yaml paths; expect paths inside the installed plugin root and VERSION 0.5.0. Delete
        the scratch configuration afterwards. If Claude authentication is unavailable, record unverified.
    inputs:
      include: [.claude-plugin, skills, sdd, standards, plugin.json, VERSION]
      exclude: ['**/__pycache__/**']
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-005
    description: Confirm Claude Code loads AGENTS.md rules through CLAUDE.md at the root and in a project rendered from the base template.
    requirements: [REQ-006]
    required: true
    method:
      kind: manual
      reason: Instruction loading is client behavior observable only in a real Claude Code session.
      procedure: >-
        In the repository root and in a scratch copy of project-templates/base, run a non-interactive Claude
        Code session that asks which file it loaded project instructions from and to quote the first
        mandatory rule. Expect CLAUDE.md with the imported AGENTS.md content and the quoted rule matching
        AGENTS.md. If authentication is unavailable, record unverified.
    inputs:
      include: [CLAUDE.md, AGENTS.md, project-templates/base]
      exclude: []
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-006
    description: Review guidance, release procedure and boundaries against the requirements.
    requirements: [REQ-003, REQ-004, REQ-005, REQ-006]
    required: true
    method:
      kind: review
      reason: Truthfulness of multilingual guidance and preservation of history and boundaries need human-readable review.
      procedure: >-
        Review the PR diff against origin/main. Expect: EN/PT/ES Claude setup guides aligned and linked
        from READMEs and workspace setup; native steps not observed by CHECK-004 labelled unverified;
        no changes under specs/archive, docs/validation of other changes, docs/handoffs or
        docs/releases/0.4.0-*; git ls-remote shows v0.4.0 still at c191f3b; no consumer lockfile, Standards
        snapshot or profile template other than the base CLAUDE.md changed; project-templates README
        documents CLAUDE.md adoption as a reviewed migration that surfaces existing CLAUDE.md conflicts;
        scripts/release/README documents tag-after-merge, both catalogs and that refresh/update observations
        are recorded as observed or unverified; guidance does not claim v0.5.0 installable before the tag;
        PR stays protected with required CI and review.
    inputs:
      include: [docs/user-docs, README.md, README.pt.md, README.es.md, project-templates/README.md, scripts/release/README.md, CHANGELOG.md, docs/decisions]
      exclude: []
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
  - id: CHECK-007
    description: Post-merge release observation of tag, release and both catalogs.
    requirements: [REQ-004]
    required: false
    method:
      kind: manual
      reason: Tag, release and client refresh exist only after merge and require administrator authority and the users' clients; this is operational follow-up outside the pre-merge gate.
      procedure: >-
        After merge and with scoped authority, confirm v0.5.0 points to the merge commit and the GitHub release
        references it; in Claude run claude plugin marketplace add versat-labs/versat-ai-harness and
        claude plugin install versat-ai-harness@versat and record the version; in ChatGPT record whether the
        existing installation offers or applies 0.5.0. Record each observation or unverified.
    inputs:
      include: [.claude-plugin, .agents/plugins, VERSION]
      exclude: []
    outputs: [docs/validation/claude-marketplace-release]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-001, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-003, CHECK-004]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-002, scenario: 3}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-006]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-006]
  - scenario: {requirement: REQ-004, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-002]
  - scenario: {requirement: REQ-004, scenario: 2}
    applicability: required
    checks: [CHECK-006]
  - scenario: {requirement: REQ-004, scenario: 3}
    applicability: required
    checks: [CHECK-006, CHECK-007]
  - scenario: {requirement: REQ-004, scenario: 4}
    applicability: required
    checks: [CHECK-006, CHECK-007]
  - scenario: {requirement: REQ-005, scenario: 1}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-005, scenario: 2}
    applicability: required
    checks: [CHECK-006]
  - scenario: {requirement: REQ-005, scenario: 3}
    applicability: required
    checks: [CHECK-006]
  - scenario: {requirement: REQ-006, scenario: 1}
    applicability: required
    checks: [CHECK-005]
  - scenario: {requirement: REQ-006, scenario: 2}
    applicability: required
    checks: [CHECK-001, CHECK-005]
  - scenario: {requirement: REQ-006, scenario: 3}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-006, scenario: 4}
    applicability: required
    checks: [CHECK-006]
regression:
  - obligation: {impact: 1, scenario: 1}
    checks: [CHECK-001]
    rationale: Existing Codex catalog tests keep asserting the repository catalog contains the Plugin; new tests add the Claude catalog.
  - obligation: {impact: 1, scenario: 2}
    checks: [CHECK-001]
    rationale: Exact-tag selection is asserted for both catalogs, with branch/latest negatives.
  - obligation: {impact: 2, scenario: 1}
    checks: [CHECK-001]
    rationale: The plugin validator keeps requiring canonical root directories; the Claude manifest adds no package tree.
  - obligation: {impact: 2, scenario: 2}
    checks: [CHECK-001]
    rationale: Root skill resolution is unchanged; CHECK-001 keeps required Skills checks and CHECK-004 observes installed resolution.
  - obligation: {impact: 2, scenario: 3}
    checks: [CHECK-001]
    rationale: Existing checks reject copied or nested package trees; CLAUDE.md tests reject duplicated instructions.
  - obligation: {impact: 3, scenario: 1}
    checks: [CHECK-001]
    rationale: Existing marketplace identity tests keep versat / Versat Plugins, plugin name, URL and policy; only the expected ref follows VERSION.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 9c4c65f9751a6e3accfa59f68b1f3b2f03bcae1def5abf3d9c2c69da0ff54af4
  approval: null
---

# Design

## Current state

Root `plugin.json` (portable) and `.codex-plugin/plugin.json` (Codex) at 0.4.0; Codex catalog `.agents/plugins/marketplace.json` `versat` at `v0.4.0`; `validators/plugin/validate.py` enforces manifest/version agreement and Codex catalog identity/ref. No Claude files, no `CLAUDE.md`. `project-templates/base/AGENTS.md` is composed by every profile.

A disposable prototype (scratchpad copy, Claude Code 2.1.332, `claude plugin validate`) showed: without an `agents` key, Claude registers `agents/README.md`, `architect`, `orchestrator` and `reviewer` as plugin subagents and warns about missing frontmatter; with `"agents": []` the Provides list contains only the seven Skills (the frontmatter warnings remain because the directory is still scanned). Claude Code documentation states: only `name` is required in `plugin.json`; `skills` adds to the default directory while `agents` replaces it; catalogs require `name`, `owner`, `plugins`; `github` sources accept `repo` and `ref`; third-party catalog auto-update is off by default and enabled per marketplace in `/plugin` → Marketplaces; `AGENTS.md` is read only when no `CLAUDE.md` exists, and `CLAUDE.md` supports `@path` imports.

## Proposed design

See [ADR-0021](../../../docs/decisions/0021-claude-plugin-adapter.md) (proposed with this Design).

1. **`.claude-plugin/plugin.json`**: `name`, `version`, `description`, `author`, `repository`, `homepage`, `license: Apache-2.0`, `keywords` mirrored from `plugin.json`, plus `"agents": []`. No `skills` key (default `skills/` discovery).
2. **`.claude-plugin/marketplace.json`**: `name: versat`, `owner: {name: Versat}`, `description`, `plugins: [{name: versat-ai-harness, description, category: Developer Tools, source: {source: github, repo: versat-labs/versat-ai-harness, ref: v<VERSION>}}]`. A `github` source is used instead of `./` because a relative source follows whatever revision the catalog was added from and cannot pin a tag.
3. **`CLAUDE.md`** at the root and in `project-templates/base/`: a single line `@AGENTS.md`.
4. **Validator** (`validators/plugin/validate.py`): new functions for the Claude manifest (mirrors fields, `agents == []`), Claude catalog (identity, owner, single entry, github repo, exact ref), cross-catalog ref equality, and import-only `CLAUDE.md` for root and base template (content after stripping whitespace equals `@AGENTS.md`). New tests in `tests/validators/test_plugin_claude.py`; existing Codex tests stay. Update `validators/plugin/README.md`.
5. **Guidance**: `docs/user-docs/guides/claude-setup.md` with `.pt.md`/`.es.md` (add marketplace, install, enable auto-update or `claude plugin update versat-ai-harness@versat`, verify version/Skill paths, recover by reinstalling an exact earlier tag via `owner/repo#vX.Y.Z`); install line in the three READMEs; link from workspace setup; `project-templates/README.md` consumer migration step for `CLAUDE.md`; `scripts/release/README.md` release order.
6. **Release 0.5.0**: bump VERSION, three manifests, both catalog refs; CHANGELOG moves Unreleased into `## [0.5.0] - <merge date>` and adds this change. The existing `0.4.0` heading is corrected from "Unreleased candidate" to its published date 2026-11-24 without editing its entries. The GitHub release body is the 0.5.0 CHANGELOG section.

## Boundaries and contracts

Root package, canonical directories and Codex catalog identity are unchanged. `agents/` stays role guidance on both clients. Consumer lockfiles and Standards snapshots are not touched. `AGENTS.md` stays the only instruction source; `CLAUDE.md` adds nothing.

## Data, security and permissions

No secrets or credentials. The Claude catalog references a public repository. Tag/release creation is reserved to administrators by the public GitHub policy 2.0.0; the agent performs it only with explicit scoped authorization and if permitted, otherwise hands it to an administrator.

## Operations and observability

Release order: (1) PR reviewed with required CI; (2) merge; (3) immediately create annotated tag `v0.5.0` on the merge commit and the GitHub release. Between (2) and (3) the main-tracking Codex catalog references a missing tag; existing installations keep 0.4.0 until the tag exists. Observations of Claude install and ChatGPT refresh go into CHECK-007 evidence as observed or unverified.

## Migration, rollout and rollback

- Claude users: `/plugin marketplace add versat-labs/versat-ai-harness`, `/plugin install versat-ai-harness@versat`, optionally enable auto-update.
- ChatGPT users: no action expected; the catalog refresh offers 0.5.0 (unverified until observed).
- Consumers: optional reviewed migration adds `CLAUDE.md`; conflicts surfaced.
- Rollback: if the tag cannot be created promptly, revert the catalog refs to `v0.4.0` in a follow-up PR; if 0.5.0 is defective, publish 0.5.1 — never move tags. Claude users can pin `#v0.4.0` when adding the marketplace.

## Alternatives considered

- **Relative `./` source in the Claude catalog**: simplest, but tracks the default branch instead of an exact tag, violating exact-version consumption. Rejected.
- **Add frontmatter to `agents/*.md` to make them native Claude subagents**: changes their contract from read-on-demand guidance to auto-invocable agents, and would diverge from Codex. Deferred to a separate decision.
- **Symlink `CLAUDE.md` → `AGENTS.md`**: symlinks are rejected by validators and unreliable on Windows checkouts. Rejected.
- **Two PRs (content, then catalog refs after the tag)**: the tagged commit would carry catalogs at `v0.4.0`, failing the release contract. Rejected.

## Validation plan

CHECK-001 covers structural contracts and all six regression obligations with positive and negative cases. CHECK-002 retains the full suites and CI. CHECK-003 uses the native Claude validator. CHECK-004 and CHECK-005 observe real Claude installation, Skill resolution and instruction loading in isolated scratch configurations; unavailable authentication is recorded as unverified, which blocks delivery readiness until resolved. CHECK-006 reviews documentation truthfulness and preserved history/boundaries. CHECK-007 is non-required post-merge operational follow-up for tag, release and client refresh. All 19 acceptance positions are mapped.

## Planning review

Design R1 presented for Gate 2 with ADR-0021 (proposed). No approval recorded yet.
