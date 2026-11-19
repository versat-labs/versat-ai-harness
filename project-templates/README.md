# Project Templates

Templates are composable modules. The bootstrap starts with `base` and adds one or more profile modules.

```text
software       = base + software
agent          = base + agent
hybrid         = base + software + agent
library        = base + library
infrastructure = base + infrastructure
```

The base includes [the product overview template](base/specs/product/overview.md) for all profiles. During bootstrap, populate it through the project-bootstrap Skill's guided discovery. Supporting product documents are created only when the collected content warrants them; profile modules do not copy or redefine the shared overview. Follow the resolved [Documentation Standard](../standards/core/documentation.md) for the reader overview, first-use guidance and ADR references. Create reader material when there is suitable content, and link from the README to existing targets. During maintenance, preserve working equivalent paths and review links and pinned references before adopting a new layout.

The base README's Getting started prompt is conditional. Apply the resolved [Documentation Standard](../standards/core/documentation.md#first-use-guides) to actual usable behavior: populate the link to existing first-use content or omit the section. Do not copy the authoring prompt into a finished README, generate an empty guide or add guide directories to every profile. Create useful content and its README link together when behavior is available; preserve existing documentation conventions during adoption.

## Composition

Structure manifests describe directories to create. Copy the base files, then overlay the selected modules' content at project-relative paths, including hidden directories. `structure.yaml` and `composition.yaml` are composition metadata, not generated project files. Identical shared directories are allowed; conflicting file destinations must fail rather than overwrite content. Preserve project-specific content during upgrades.

The agent module contributes its directory manifest and `docs/architecture/agent-project.md`. The software and agent modules continue to share `base`; hybrid does not copy or redefine it. Deterministic bootstrap automation is not implemented yet; the bootstrap Skill follows this composition contract.

## Agent artifacts

The [Agent Artifact Standard](../standards/core/agent-artifacts.md), resolved through the index, defines the canonical paths and responsibilities. A composed agent project includes:

```text
AGENTS.md
.versat/project.yaml
.versat/standards.lock
.agents/skills/<skill-name>/SKILL.md
.codex/agents/<agent-name>.toml
workflows/<workflow-name>/workflow.md
docs/architecture/agent-project.md
evals/
tests/
specs/product/
specs/changes/
```

Named files above illustrate destinations; bootstrap creates the artifact directories without installing placeholder Skills, agents or workflows. Use the [authoring templates](artifacts/README.md) to add concrete artifacts. The [supplier-payment workflow](examples/supplier-payment/workflow.md) is a technical example of Gmail intake, Versat ERP registration and Google Drive archival, with dependencies that must be supplied before execution. `artifacts/` and `examples/` are reference material, not profile modules.

For hybrid projects, the software module also supplies `src/` and `infra/`. These application directories retain their runtime responsibilities. Local Skills and workflows may serve business operations or development; their role must be explicit in project architecture.

## Consumer migration

Adopt a reviewed exact Harness release and record the target version. Do not blindly move every root `skills/` or `agents/` directory:

1. Classify each artifact as local capability, Plugin export, role guidance, application code or operational workflow.
2. Move local Skills to the consumer destination with uppercase `SKILL.md`; update references and verify discovery. Keep installed Plugin dependencies referenced rather than duplicated.
3. Convert applicable role guidance into valid Codex agent TOML and verify loading in the supported Codex release. A Markdown rename is insufficient. Preserve application source and intentional Plugin exports.
4. Organize operational workflows into one directory per workflow and bind their actual Skill dependencies. Document executor, permissions, outputs and recovery before marking them ready.
5. Preserve project-specific content, surface destination conflicts, review the diff and run consumer tests/evals and integration checks. Retain a reviewed rollback path and update the exact lockfile only with the migration.

The Harness package keeps root `skills/` and `agents/`, and its SDD lifecycle procedures stay under `sdd/workflows/`. Those package paths are not consumer migration targets.

## Optional project validation

After composing base and the selected profile, adopt [validation assets](artifacts/validation/README.md) only for a usable project execution integration. Follow [project validation](../docs/guides/project-validation.md) to select an exact provider, resolve identity/Standards, preserve custom commands, configure complete required suites and execute them. Include hidden files; a copied CI placeholder or empty tests directory is not readiness. Bootstrap reports these gaps. Maintenance reviews destination conflicts and keeps the prior wrapper/configuration/CI/lockfile together for rollback. Neither flow silently selects a newer Harness release.
