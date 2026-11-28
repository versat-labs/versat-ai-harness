# Release scripts

Release automation must validate semantic versions, changelog state, Plugin manifests, marketplace references and release provenance.

The repository root is the Plugin artifact; release automation does not build or maintain a copied distribution tree. Before creating a tag, it must confirm that:

- `VERSION`, `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json` and `project-templates/base/.versat/standards.lock` (`harness.version`) contain the same semantic version;
- `.agents/plugins/marketplace.json` (Codex) and `.claude-plugin/marketplace.json` (Claude) select the same exact `v<VERSION>` Git reference;
- repository and Plugin validation pass;
- the release commit contains the canonical Standards, SDD, templates, schemas and validators used by its Skills.

## Release order

Catalogs on main reference the release tag before it exists, because the tag is created on the reviewed merge commit:

1. Prepare the version, catalogs and a dated CHANGELOG section in the release PR; pass required CI and review.
2. Merge the PR.
3. Immediately create the annotated tag `v<VERSION>` on the merge commit and the GitHub release whose notes are the CHANGELOG section. Tag administration is reserved to administrators by the public GitHub policy.
4. Record what was actually observed: tag target, Claude marketplace add/install of the new version, and whether existing ChatGPT/Codex and Claude installations offer or apply it. Record anything not observed as unverified.

Between steps 2 and 3, main-tracking catalogs point to a missing tag and existing installations keep their previous version. If the tag cannot be created promptly, revert the catalog references in a follow-up PR. Never move or recreate a published tag; fix a defective release with a new patch version.

Release automation must never rewrite consumer repositories directly. It proposes exact version updates through reviewable changes.

## Commit parsing

Before adding changelog generation or version inference from commits, implement the compatibility contract in the canonical [Git Standard](../../standards/core/git.md). A stock Conventional Commits parser cannot be assumed to recognize Versat's leading Shortcut marker. Parser support must preserve Story traceability and breaking-change information. No commit-driven release automation is implemented by this change.
