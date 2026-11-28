# Claude setup

[English](claude-setup.md) | [Português](claude-setup.pt.md) | [Español](claude-setup.es.md)

Install the Versat AI Harness in Claude Code (terminal, desktop or web) from the repository marketplace, keep it at an exact release and verify which provider your session uses.

## Prerequisites

- Claude Code 2.1.277 or later; run `claude --version`.
- Read access to `github.com/versat-labs/versat-ai-harness` (public).
- The exact release you want exists as a Git tag. Both repository catalogs select `v<VERSION>`; Claude support starts with 0.5.0, which is installable only after the `v0.5.0` tag is created on its merge commit. Earlier tags have no Claude catalog.

## Install

In a Claude Code session:

```text
/plugin marketplace add versat-labs/versat-ai-harness
/plugin install versat-ai-harness@versat
```

From a shell, the equivalent commands are:

```sh
claude plugin marketplace add versat-labs/versat-ai-harness
claude plugin install versat-ai-harness@versat
```

The marketplace is named `versat`. Its single entry installs `versat-ai-harness` from this repository at the exact tag the catalog selects. Start a new session after installing.

## Update

Claude does not auto-update third-party marketplaces by default. Choose one:

- Turn auto-update on: run `/plugin`, open **Marketplaces**, select `versat` and enable auto-update.
- Update explicitly: `claude plugin marketplace update versat`, then `claude plugin update versat-ai-harness@versat`.

An update moves your installation to the tag the current catalog selects. It does not change any project lockfile; projects adopt a new Harness release through a reviewed migration.

## Verify

1. `claude plugin list` shows `versat-ai-harness@versat` enabled with the expected version.
2. In a new session, ask: “Using the versat-sdd Skill, report the Harness VERSION and the paths of sdd/process.md and standards/index.yaml you resolved.” The paths must be inside the installed plugin directory and VERSION must match the installed version.
3. The plugin provides seven Skills and no subagents. The Markdown files under the package `agents/` directory are role guidance for explicit reading, not Claude subagents.

If a Skill is missing or resolves files from another location, stop and fix the installation before running a workflow.

## Project instructions

Versat projects keep their rules in `AGENTS.md`. Claude reads `CLAUDE.md`; the Agent Artifact Standard requires a `CLAUDE.md` whose only content is `@AGENTS.md`, so Claude loads the same rules. New projects get it from the base template; existing projects adopt it through [project maintenance](project-maintenance.md), and [project audit](project-audit.md) reports a missing or divergent file. Do not put rules in `CLAUDE.md`.

## Recovery

- Pin an exact release: `claude plugin marketplace remove versat`, then `claude plugin marketplace add versat-labs/versat-ai-harness#v0.5.0` (or a later tag) and reinstall. Tags before v0.5.0 have no Claude catalog. Never select a branch or `latest`.
- A failed update leaves the last verified release in place only if you keep it pinned; record the failure and report it to the maintainers.
- A project with active SDD v3 records needs a v3-capable provider (0.3.0 or later).

## Verification status

The marketplace and plugin files pass `claude plugin validate` and the Harness package validator. Installation from a local test catalog was exercised in an isolated configuration during release preparation. Installation from GitHub at `v0.5.0`, auto-update and explicit update have not been observed yet; treat them as unverified until the release follow-up records them.
