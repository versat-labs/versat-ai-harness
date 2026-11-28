---
sdd_version: 3
change: claude-marketplace-release
status: proposed
owner: Versat / Elvis
summary: Make the root Harness package installable from a Claude plugin marketplace and publish v0.5.0 so both the Claude and ChatGPT catalogs select it.
risk: medium
impact:
  state: assessed
  summary: Extend the exact-ref repository catalog contract to a second client catalog and preserve the Codex marketplace identity, root package and canonical resources.
  items:
    - source:
        change: root-plugin-package
        requirement: REQ-003
        scenarios: [1, 2]
        requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
      current_contract:
        change: claude-marketplace-release
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-002, REQ-004]
      reason: Add a Claude catalog with the same exact-tag selection and move both catalogs to v0.5.0.
    - source:
        change: root-plugin-package
        requirement: REQ-002
        scenarios: [1, 2, 3]
        requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
      current_contract:
        change: claude-marketplace-release
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001, REQ-005, REQ-006]
      reason: The Claude package reuses the root tree and CLAUDE.md only imports AGENTS.md; no copied Skills, Standards or instructions.
    - source:
        change: harness-marketplace-transition
        requirement: REQ-001
        scenarios: [1]
        requirements_digest: 040f03e69d9af35567a293d97248c1c1222ed054117e1c675b4e41a8ed7f6af7
      current_contract:
        change: claude-marketplace-release
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-002]
      reason: Keep Codex catalog versat / Versat Plugins, plugin versat-ai-harness, URL and policy; only its ref advances.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Current conversation reply to the Gate 1 request for Proposal/Requirements R1 including REQ-006
    quote: Sim
    revision: 1
    digest: 9c4c65f9751a6e3accfa59f68b1f3b2f03bcae1def5abf3d9c2c69da0ff54af4
---

# Proposal

## Context and problem

The repository root is a portable plugin with a Codex manifest and a Codex catalog (`.agents/plugins/marketplace.json`, `versat`, ref `v0.4.0`). v0.4.0 is published (GitHub release 2026-11-24). Claude has no manifest or catalog, so the Harness cannot be installed there. Main also has unreleased work since v0.4.0 (SIFEN Skill, public security policy, issue language, `github-issue-creation` Skill), which the ChatGPT installation does not receive because its catalog pins v0.4.0.

## Expected outcome

1. Claude users add the marketplace from `versat-labs/versat-ai-harness` and install `versat-ai-harness@versat`, getting the same Skills and canonical resources.
2. Claude sessions in this repository and in consumer projects read the canonical AGENTS.md through an import-only CLAUDE.md.
3. Release v0.5.0; both catalogs select `v0.5.0`, so the main-tracking ChatGPT catalog offers the new version to the existing installation.

## Scope

- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` at the root.
- Plugin validator and tests extended to the Claude manifest/catalog and cross-catalog version agreement.
- Decide handling of `agents/` role guidance for Claude (Design).
- EN/PT/ES setup guidance for Claude; README pointers.
- Import-only CLAUDE.md (`@AGENTS.md`) at the root and in the `base` project template, with a validator check that it adds no rules.
- Version bump to 0.5.0, CHANGELOG, release notes; after merge and with authority, tag `v0.5.0` and GitHub release.
- An ADR if Design concludes the multi-client catalog is a significant structural decision (extends ADR-0011).

## Out of scope

- Changing the Codex catalog identity, policy or plugin name.
- Publishing to Anthropic's official marketplace or any third-party directory.
- Updating consumer projects or lockfiles to 0.5.0, or adding CLAUDE.md to existing consumers outside a reviewed migration.
- Forcing auto-update on users' clients; agent-driven install/uninstall in users' workspaces.
- Moving or editing v0.4.0.

## Work tracking

No Shortcut Story or GitHub issue is associated; none is invented. Branch `claude/fervent-lamport-lu2vf3` (session branch; no Story-linked name applies). Change ID `claude-marketplace-release`.

## Impact and risks

See `impact` metadata. Risks:

- Claude auto-discovers root `agents/*.md`; those files lack agent frontmatter and could load as malformed subagents or warnings.
- Release ordering: catalogs must reference `v0.5.0` before the tag exists (the PR merges first, the tag is created on the merge commit). Between merge and tag, the main-tracking Codex catalog points at a missing ref; keep this window short.
- Tag/release creation requires administrator authority under the public GitHub policy; this agent may be unable to perform it.
- Native Claude and ChatGPT update behavior can only be observed by the users.

## Current contract baseline

Observed at `b6b0a2a` (main): VERSION `0.4.0`; `plugin.json` and `.codex-plugin/plugin.json` at 0.4.0; `.agents/plugins/marketplace.json` = `versat` / `Versat Plugins`, one `versat-ai-harness` entry, `source: url` to the repository `.git`, `ref: v0.4.0`, AVAILABLE/ON_INSTALL. No `.claude-plugin/` and no CLAUDE.md at the root or in `project-templates/base/` (which provides AGENTS.md). `validators/plugin/validate.py` enforces manifest/version agreement and Codex catalog identity/ref. Remote tags v0.2.0, v0.3.0, v0.4.0; release v0.4.0 published. CHANGELOG still labels 0.4.0 "Unreleased candidate" and has an Unreleased section.

## Proposal acceptance criterion

Approve Proposal/Requirements R1: Claude manifest and catalog at the root with exact-tag selection, validator coverage, trilingual guidance, import-only CLAUDE.md at the root and in the base template, and release v0.5.0 with both catalogs at `v0.5.0`, tag created only after merge with scoped authority.

## Planning review

Proposal/Requirements R1 (with REQ-006) was presented for Gate 1 and approved by the owner with “Sim” under digest `9c4c65f9751a6e3accfa59f68b1f3b2f03bcae1def5abf3d9c2c69da0ff54af4`. This unlocks Design only.
