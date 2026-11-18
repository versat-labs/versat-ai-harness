# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Versat’s source of truth for AI-assisted development: a portable Plugin containing Standards, Spec Driven Development (SDD), reusable Skills, composable project templates and deterministic validation.

For developers, reviewers and maintainers, including external contributors when access and applicable terms are available. Maintained by Versat; governed-component review contacts are @elviszoz and @evertonspohrversat in .github/CODEOWNERS.

## Start here

[Quickstart: obtain a first SDD plan](docs/user-docs/quickstart.md) · [Product context](docs/product/overview.md)

- [Workspace setup](docs/user-docs/guides/workspace-setup.md)
- [SDD with Codex](docs/user-docs/guides/sdd-with-codex.md)
- [GitHub delivery](docs/user-docs/guides/github-delivery.md)
- [Bootstrap a project](docs/user-docs/guides/project-bootstrap.md)
- [Maintain an existing project](docs/user-docs/guides/project-maintenance.md)
- [Audit a project](docs/user-docs/guides/project-audit.md)
- [Review architecture](docs/user-docs/guides/architecture-review.md)
- [Validation and evaluations](docs/user-docs/guides/validation-and-evaluations.md)
- [SIFEN electronic documentation](docs/user-docs/guides/sifen-electronic-documentation.md)

## Publication preparation in progress

The public Apache-2.0 direction is approved. The [concrete candidate](docs/licensing/candidates/apache-2.0/APPROVAL.md) has text approval and has not been adopted. The existing repository remains private; 0.4.0 is a future candidate, not an available release. See [licensing](docs/user-docs/guides/licensing.md), [contribution](docs/user-docs/guides/contributing.md), [security reporting](docs/user-docs/guides/security-reporting.md) and the [preparation status](docs/handoffs/harness-publication-readiness/README.md).

## Current state and adoption

VERSION declares 0.3.0. The marketplace selects the exact tag v0.3.0; verify that tag and its contents before distribution. Consumer execution and supervised evaluations in the current source are explicitly unreleased. A source change or merge does not update installed Plugins or consumer pins. Adopt another exact release through a reviewed change.

Workspace administrators manage marketplace import and member installation policy. Use this repository as the source, authenticate with read access, review the imported exact release and confirm member availability. Follow the current workspace administration interface; the repository marketplace policy is AVAILABLE and does not prove automatic installation. Members can use [workspace setup](docs/user-docs/guides/workspace-setup.md).

## Repository and consumer layout

The repository root is the Plugin package. Policies live in standards/; capabilities in skills/; process in sdd/; enforcement in validators/ and CI; composition in project-templates/; contracts in schemas/; reusable role guidance in agents/; non-normative knowledge in resources/. Plugin manifests and the marketplace select version-matched resources.

Consumer agent projects instead use .agents/skills/, .codex/agents/ and workflows/. A workflow needs an explicit executor; root agents/*.md is not native Codex registration. See [architecture (English)](docs/architecture/overview.md) · [artifact contract (English)](standards/core/agent-artifacts.md).

## Local validation

Use Python 3.11+ in a virtual environment from this repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
./scripts/validate/run.sh
```

An existing interpreter can be selected with PYTHON=/absolute/path/to/python. This entry point checks the package, SDD records and validator/execution regressions. It does not prove human approval, remote CI, merge or another application’s behavior. Historical compatibility exceptions are explicit.

## Contribute and maintain

Use $versat-sdd for material changes. Read repository instructions, review the three planning stages and explicitly authorize implementation after Tasks. Prepare living documentation and the documentary archive in the same delivery PR. Actual PR review, final checks and merge remain separate checkpoints.

[SDD (English)](sdd/README.md) · [Repository instructions (English)](AGENTS.md) · [ADRs (English)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
