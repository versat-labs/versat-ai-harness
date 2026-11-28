---
sdd_version: 3
change: claude-marketplace-release
status: proposed
owner: Versat / Elvis
summary: Make the root Harness package installable from a Claude plugin marketplace and publish v0.5.0 so both the Claude and ChatGPT catalogs select it.
risk: medium
impact:
  state: assessed
  summary: Extend the exact-ref repository catalog contract to a second client catalog, extend the Agent Artifact Standard with an import-only CLAUDE.md entry point, and preserve the Codex marketplace identity, root package and canonical resources.
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
    - current_contract:
        path: standards/core/agent-artifacts.md
        locator: "## Scope and responsibilities"
        digest: cb54e704af8d32f42b302eaaefe06fa289ca2eb8136960e3330af49614f4444e
      effect: extend
      targets: [REQ-006]
      reason: Keep AGENTS.md as shared project guidance and the existing artifact rules; add the import-only CLAUDE.md entry point for projects that have AGENTS.md.
review:
  revision: 3
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
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
- Agent Artifact Standard rule: a project with `AGENTS.md` provides an import-only `CLAUDE.md`.
- A deterministic consumer instruction entry-point check used by `project-audit`; bootstrap and maintenance keep obtaining the file through the `base` template and reviewed migrations.
- Base template `.versat/standards.lock` `harness.version` set to 0.5.0, as in previous releases.
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

Observed at `b6b0a2a` (main): VERSION `0.4.0`; `plugin.json` and `.codex-plugin/plugin.json` at 0.4.0; `.agents/plugins/marketplace.json` = `versat` / `Versat Plugins`, one `versat-ai-harness` entry, `source: url` to the repository `.git`, `ref: v0.4.0`, AVAILABLE/ON_INSTALL. No `.claude-plugin/` and no CLAUDE.md at the root or in `project-templates/base/` (which provides AGENTS.md). No Standard requires AGENTS.md or CLAUDE.md: bootstrap obtains AGENTS.md only from the `base` template; `standards/core/agent-artifacts.md` lists AGENTS.md as shared project guidance for projects with agent artifacts; `project-audit` reads repository instructions without a deterministic check; `validators/project/` has no executable validator. `validators/plugin/validate.py` enforces manifest/version agreement and Codex catalog identity/ref. Remote tags v0.2.0, v0.3.0, v0.4.0; release v0.4.0 published. CHANGELOG still labels 0.4.0 "Unreleased candidate" and has an Unreleased section.

## Proposal acceptance criterion

Approve Proposal/Requirements R1: Claude manifest and catalog at the root with exact-tag selection, validator coverage, trilingual guidance, import-only CLAUDE.md at the root and in the base template, required by the Agent Artifact Standard and checked during project audit, and release v0.5.0 with both catalogs at `v0.5.0`, tag created only after merge with scoped authority.

## Planning review

Proposal/Requirements R1 (with REQ-006) was presented for Gate 1 and approved by the owner with “Sim” under digest `9c4c65f9751a6e3accfa59f68b1f3b2f03bcae1def5abf3d9c2c69da0ff54af4`. This unlocks Design only.

After Design R1 was presented, the owner asked to add the Standard rule and audit detection for CLAUDE.md (“Sim, inclua os itens 1 e 2 e reapresente a R2”). REQ-006 gained acceptance positions 5 and 6 and a fourth impact item, so Proposal/Requirements moved to R2 awaiting approval; the R1 approval above is historical. Design R1 is superseded; because Design files exist only after their upstream gate is approved, it was removed from the active dossier and remains in Git history at commit `7fc47b6`. It will be revised after R2 approval.

The owner approved Proposal/Requirements R2 with “Sim, aprovo a R2” under digest `84e1f18e758f8ff57deca1160bc5202ce8a40591f5875da659d0831ab026193e`. This unlocks Design R2 only.

Design R2 was then approved (“Sim, aprovo o Design R2”, digest `e6e9cca75e5d9d33eaeced674836e58cfe5eb59b2966400fbb48932602880efa`) and Tasks R1 presented. At Gate 3 the owner chose to update the base template lock (“Opção (b), reabra o Gate 1”): REQ-005 acceptance 2 now requires `harness.version: 0.5.0` in `project-templates/base/.versat/standards.lock`. Proposal/Requirements moved to R3 awaiting approval; R1 and R2 approvals are historical, and Design R2 and Tasks R1 are superseded.
