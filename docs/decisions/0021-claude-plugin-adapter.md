# ADR-0021 — Distribute the root package to Claude through a second exact-ref catalog

- Status: Proposed with Design R2 of `claude-marketplace-release`
- Extends: [ADR-0011](0011-root-portable-plugin-package.md)
- Related decision: [ADR-0009](0009-execution-adapters.md)
- Scope: Plugin manifests, repository marketplace catalogs and agent instruction entry points

## Context

ADR-0011 makes the repository root the portable Plugin package and distributes it through one repository catalog (`.agents/plugins/marketplace.json`, Codex) that selects an exact release tag. Claude reads its own manifest (`.claude-plugin/plugin.json`) and catalog (`.claude-plugin/marketplace.json`), auto-discovers root `skills/` and `agents/`, and reads `CLAUDE.md` as project instructions. Claude Code reads `AGENTS.md` only in some versions and only when no `CLAUDE.md` exists.

Root `agents/` holds role guidance for explicit reading, without native agent frontmatter. Claude would register those files, including `README.md`, as plugin subagents.

## Decision

1. Add `.claude-plugin/plugin.json` as a second compatibility overlay over the same root package, with identity and version mirrored from `plugin.json`, and `agents: []` so root role guidance is not registered as Claude subagents. Skills are discovered from root `skills/`.
2. Add `.claude-plugin/marketplace.json` as a second repository catalog named `versat`, with one `versat-ai-harness` entry whose `github` source selects this repository at the exact `v<VERSION>` tag. Both catalogs always select the same tag.
3. Provide an import-only `CLAUDE.md` (`@AGENTS.md`) at the root and in the `base` project template. `AGENTS.md` stays the single canonical instruction file.
4. Require the import-only `CLAUDE.md` in the Agent Artifact Standard for every project that has `AGENTS.md`, and provide a read-only consumer check (`validators/project/instructions.py`) that `project-audit` runs.
5. Enforce the package items mechanically in the Plugin validator, reusing the consumer check for the root and the `base` template.

## Consequences

- One package, two client adapters; no copied Skills, Standards or instructions.
- Every release updates five version locations (VERSION, three manifests, two catalog refs); the validator rejects drift.
- Merging a release PR exposes catalogs that reference a tag created right after the merge; release procedure keeps that window short.
- Claude auto-update of third-party catalogs is off by default; users enable it in their client.
- Role guidance in `agents/` remains unregistered on both clients; registering native Claude subagents is a separate future decision.
- Consumers adopt `CLAUDE.md` only through a reviewed migration; until then, audits report it as non-compliant with a remediation path.
