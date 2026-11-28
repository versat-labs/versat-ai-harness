# Plugin validation

`validate.py` enforces the portable root package contract:

- portable and Codex compatibility manifests are valid and agree;
- Plugin identity matches the semantic repository version;
- the Codex marketplace (`.agents/plugins/marketplace.json`) selects the exact release tag;
- the Claude manifest (`.claude-plugin/plugin.json`) mirrors the portable identity and declares `agents: []`, so root role guidance is not registered as Claude subagents;
- the Claude marketplace (`.claude-plugin/marketplace.json`) is named `versat`, has an owner and one `versat-ai-harness` GitHub entry at the exact release tag, and both catalogs select the same tag;
- `CLAUDE.md` at the root and in `project-templates/base/` only imports `AGENTS.md`, using the [consumer instruction check](../project/README.md#claude-instruction-entry-point);
- required Skills and canonical runtime directories exist;
- former nested Plugin entry points are absent.

The repository validation entry point invokes this validator.

Root `skills/` and `agents/` are package-level checks. They do not impose that layout on consumer projects or register Markdown role guidance as native Codex custom agents. Consumer checks are described separately in [project validation](../project/README.md).
