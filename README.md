# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Versat’s source of truth for AI-assisted development: a portable Plugin containing Standards, Spec Driven Development (SDD), reusable Skills, composable project templates and deterministic validation.

For developers, reviewers and maintainers, including external contributors. Maintained by Versat. @elviszoz and @evertonspohrversat are the general CODEOWNERS and shared security-triage maintainers; Elvis coordinates. Main requires one eligible nonauthor CODEOWNER approval and passing CI. The internal approval/dismissal/renewed-approval test is complete. External security-report receipt remains unverified.

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

- [Marketplace transition: new and legacy identities](docs/user-docs/guides/marketplace-transition.md)

## Repository published; 0.4.0 candidate unreleased

The repository is public and the reviewed Apache-2.0 license and notices are integrated on main. Version 0.4.0 remains an unreleased candidate: no v0.4.0 tag or release is available. Existing text approvals and historical evidence retain their original scope.

Main protection and the internal PR control test have been verified. Private Vulnerability Reporting is enabled; external fork/CI behavior, security-report receipt/confidentiality and native Plugin installation/update/recovery remain pending. The opening write pause has ended; ordinary work follows protected PRs.

[0.4.0 candidate notes and remaining checks](docs/releases/0.4.0-candidate.md)

[License](LICENSE) · [Contribution](docs/user-docs/guides/contributing.md) · [Security reporting](docs/user-docs/guides/security-reporting.md)

## Current state and adoption

VERSION and manifests now declare the local 0.4.0 candidate. Its repository catalog selects v0.4.0, which must not be imported as an available release before that exact tag is created and verified under separate authority. This local preparation changes no installation or consumer pin; the previous released reference is v0.3.0. The two current users plan later manual reinstallation; main synchronization may interrupt their existing setup. See the transition guide for the accepted scope and pending native checks.

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
./scripts/validate/run.sh --quality-base origin/main
```

An existing interpreter can be selected with PYTHON=/absolute/path/to/python. This entry point checks the package, SDD records and validator/execution regressions. It does not prove human approval, remote CI, merge or another application’s behavior. Historical compatibility exceptions are explicit.

## Contribute and maintain

Use $versat-sdd for material changes. Read repository instructions, review the three planning stages and explicitly authorize implementation after Tasks. Prepare living documentation and the documentary archive in the same delivery PR. Actual PR review, final checks and merge remain separate checkpoints.

[SDD (English)](sdd/README.md) · [Repository instructions (English)](AGENTS.md) · [ADRs (English)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
