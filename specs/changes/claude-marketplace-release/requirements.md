---
sdd_version: 3
change: claude-marketplace-release
requirements:
  - id: REQ-001
    statement: The repository root is installable as a Claude Code plugin without duplicating the package.
    acceptance:
      - A Claude plugin manifest at .claude-plugin/plugin.json declares name versat-ai-harness and the same semantic version as VERSION, plugin.json and .codex-plugin/plugin.json.
      - After installation, Claude discovers every packaged Skill under root skills/ and each Skill resolves canonical Standards, SDD, templates, schemas and validators from the installed plugin root; no copied tree exists.
      - Root agents/ role guidance, which has no Claude agent frontmatter, does not produce load errors or unintended Claude subagents; the chosen handling is recorded in Design.
  - id: REQ-002
    statement: A Claude marketplace catalog in this repository distributes the plugin by exact release reference.
    acceptance:
      - .claude-plugin/marketplace.json declares marketplace name versat with an owner and exactly one versat-ai-harness entry whose source is this GitHub repository at the exact v<VERSION> tag.
      - A catalog with a wrong marketplace name, missing or duplicated plugin entry, wrong repository, or a ref other than v<VERSION> (including a branch or latest) fails Plugin validation.
      - The Codex catalog .agents/plugins/marketplace.json keeps its name, display label, policy and source type, and selects the same exact v<VERSION> tag as the Claude catalog.
  - id: REQ-003
    statement: Users have truthful EN/PT/ES instructions to add the Claude marketplace, install, update and recover the plugin.
    acceptance:
      - Active setup guidance documents adding the marketplace from versat-labs/versat-ai-harness, installing versat-ai-harness@versat, explicit or automatic update, and verifying the installed version and Skill location, in English with aligned Portuguese and Spanish translations.
      - Native Claude commands or behaviors not actually observed are labelled unverified; no historical record, approval or release note is rewritten.
  - id: REQ-004
    statement: A new semantic release exposes the current main content to both catalogs.
    acceptance:
      - The release version is 0.5.0 (a minor bump over the published v0.4.0); VERSION, all three manifests, both catalogs and CHANGELOG agree, and the CHANGELOG moves Unreleased entries into a dated 0.5.0 section.
      - The existing v0.4.0 tag and release are not moved, retagged or edited.
      - The v0.5.0 tag is created on the reviewed merge commit only after merge to main and only with scoped tag/release authority; the GitHub release references that tag. Until it exists, guidance does not claim v0.5.0 is installable.
      - After the release, a ChatGPT installation that follows the main-tracking Codex catalog can resolve v0.5.0; the actual refresh and update of the existing installation are recorded as observed or as unverified, never assumed.
  - id: REQ-005
    statement: Existing package, governance and consumer boundaries are preserved.
    acceptance:
      - The complete repository validation (./scripts/validate/run.sh) and quality checks pass on the final source, including the existing Codex marketplace regression tests.
      - No consumer lockfile, Standards snapshot or project template is silently updated to 0.5.0 or latest; Skills keep resolving Standards through standards/index.yaml.
      - Merge requires the existing protected PR, required CI and review; planning approval does not authorize tag, release or merge.
  - id: REQ-006
    statement: Claude reads the canonical AGENTS.md instructions in this repository and in consumer projects through a CLAUDE.md that only imports it.
    acceptance:
      - The repository root contains CLAUDE.md whose only instruction is the import @AGENTS.md; a Claude Code session opened in the repository loads the AGENTS.md rules.
      - The base project template provides the same import-only CLAUDE.md, composed by every profile through base without per-profile copies; bootstrap of a new project produces it next to AGENTS.md.
      - Validation fails when a repository or base-template CLAUDE.md is missing, does not import AGENTS.md, or contains rules beyond the import, so no parallel instruction set is maintained.
      - Existing consumers receive CLAUDE.md only through a reviewed migration; an existing project-specific CLAUDE.md is surfaced as a conflict, not overwritten.
---

# Requirements

## Actors and context

Elvis and Everton (reported current users) install the Harness in ChatGPT/Codex and will add it to Claude (Claude Code and Claude surfaces that consume Claude plugin marketplaces). Maintainers prepare the source; a repository administrator holds tag/release authority.

## Functional requirements

REQ-001 to REQ-004 and REQ-006 above.

## Non-functional requirements

REQ-005: no duplication, exact-version selection, governed release.

## Acceptance scenarios

Positions are listed in the frontmatter under each requirement.

## Constraints and assumptions

- Claude Code reads `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` at the repository root and auto-discovers `skills/` and `agents/`. This is based on public Claude Code documentation and is re-verified in Design.
- CLAUDE.md is Claude's standard instruction file. Some Claude Code versions also read AGENTS.md, but that is not guaranteed on every Claude surface; the @AGENTS.md import is version-independent.
- Automatic updates of third-party Claude marketplaces depend on the user's client settings; the Harness cannot force them.
- The Codex catalog is reported to track main in the managed ChatGPT workspace; updating its ref is what lets existing installations receive v0.5.0.
