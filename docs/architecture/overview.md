# Architecture overview

## Purpose

Versat AI Harness is the governance runtime that connects agents, Enterprise Standards, Versat SDD, local projects and GitHub. The repository root is both the product's source of truth and the portable installable Plugin boundary.

## Components

```text
                    VERSAT AI HARNESS
                         source of truth
                                |
          +---------------------+---------------------+
          |                     |                     |
      Standards                SDD               Validators
        (rules)              (process)           (enforcement)
          |                     |                     |
          +---------------------+---------------------+
                                |
                        execution adapters
                                |
                +---------------+---------------+
                |               |               |
          Codex Plugin        CI/CD          future tools
                |
         project-bootstrap
                |
         standards resolver
                |
        project repository
```

## Context model

Each project declares only its identity:

```yaml
project:
  profile: agent
  domain: finance
  criticality: high
technologies:
  - python
```

The resolver uses `standards/index.yaml` to compose:

```text
core + profile + domain + technologies + criticality
```

The exact resolved versions are recorded in `.versat/standards.lock`. Consumers do not manually select standards packages and do not silently follow `latest`.

## Package boundary

```text
versat-ai-harness/
├── plugin.json                 portable package manifest
├── .codex-plugin/plugin.json   Codex compatibility overlay
├── skills/                     capabilities and procedures
├── agents/                     reusable execution roles
├── standards/                  canonical policies
├── sdd/                        canonical change process
├── project-templates/          composable project structures
├── schemas/                    metadata contracts
└── validators/                 deterministic enforcement
```

Keeping the canonical core and its execution capabilities inside one package boundary prevents an installed Skill from losing access to its version-matched Standards, process or templates. Directory responsibilities remain separate even though they share the portable package root.

## Consumer artifacts and execution

The consumer contract is defined in the [Agent Artifact Standard](../../standards/core/agent-artifacts.md) and resolved through `standards/index.yaml`. It separates capabilities, execution roles and operational composition:

```text
consumer-project/
├── AGENTS.md
├── .agents/skills/<skill-name>/SKILL.md
├── .codex/agents/<agent-name>.toml
├── workflows/<workflow-name>/workflow.md
├── evals/
└── tests/
```

A workflow explicitly calls Skills and passes their results between steps. The chosen executor loads the workflow document and provides the tool access and execution state. Codex agents use the TOML adapter; the workflow convention does not itself register agents, schedule runs or implement integrations. These artifacts may implement business operations or development assistance. Separately deployed application agents retain the architecture of their application runtime.

The agent template extends `base`; hybrid composition adds the software module and its application source directories. Authoring templates and illustrative examples are supplied separately and are not automatically installed as active capabilities. See [template composition](../../project-templates/README.md) and [ADR-0012](../decisions/0012-consumer-agent-artifacts.md).

The Harness root `agents/*.md` files remain reusable role guidance requiring explicit loading or conversion; they are not native Codex custom-agent registrations. `sdd/workflows/` contains development lifecycle procedures, while consumer `workflows/` describes operational flows. GitHub Actions retain their separate `.github/workflows/` contract.

## Unified lifecycle

```text
Intent -> Proposal/Requirements -> human approval
       -> Design -> human approval -> Tasks -> human approval
       -> Implementation + Living Specifications -> Validation
       -> Documentary Archive Preparation -> PR Review / Required Checks
       -> Merge -> Read-only Delivery Confirmation
```

The same lifecycle applies to software, agent, library, automation, infrastructure and hybrid projects. The profile changes the applicable modules and criteria, not the corporate process.

The public `versat-sdd` Skill explicitly routes developer intent to one of four canonical procedures in `sdd/workflows/`. Shared gates and state transitions live in [the SDD process](../../sdd/process.md); the [developer guide](../../sdd/README.md) describes invocation and deliverables. Skills are adapters, not alternate policy sources.

As recorded in [ADR-0013](../decisions/0013-consolidated-sdd-workflow.md), documentary closure is prepared in the implementation branch so code, living specifications and historical artifacts enter the default branch together. PR state remains the authority for merge; an archive path alone conveys no delivery claim. Local SDD checks validate recorded metadata, revision binding and traceability, not human identity, semantic correctness or remote CI. Legacy exceptions are explicit and immutable until governed migration.

## Knowledge governance

| Level | Example | Allowed change |
|---|---|---|
| Operational memory | contextual customer preference | automatic learning within retention boundaries |
| Skill | how to prepare a recurring analysis | proposal and human approval |
| Corporate policy | security, language, Git, `AGENTS.md` | branch, PR, review and required checks |

## Distribution and enforcement

- The Plugin distributes capabilities and instructions on demand.
- The repository marketplace selects an exact semantic Plugin release from GitHub.
- Versioned snapshots and lockfiles make Standards application reproducible.
- Pull Requests propagate new releases to consumer repositories.
- GitHub Rulesets and reusable workflows enforce policies that cannot rely on agents alone.
- The Marketplace is a distribution channel, not the normative authority.

## Version 0.2.0 boundaries

This version makes the source repository a self-contained portable Plugin package and defines workspace distribution metadata. Remote repository creation, automated workspace import, consumer release resolution, GitHub organization configuration and technology-specific semantic validators are not yet part of the executable implementation.

## Version 0.3.0 boundaries

The SDD consolidation adds local contract validation and executable regression tests. It does not add a workflow engine, GitHub approval integration or automatic release publication. Installed consumers are not changed by edits to this source checkout.

The consumer artifact revision changes templates and guidance. Automated project composition, operational workflow execution and semantic validation of consumer agent artifacts are not implemented by it. Local validation checks Plugin structure and recorded SDD consistency; consumer loading and workflow behavior require separate verification.

## Acceptance and regression validation in the current source

[ADR-0014](../decisions/0014-sdd-acceptance-and-regression.md) adds v3 scenario mappings, qualified impact origins, retained regression obligations and semantic assessment records within the existing four-file lifecycle and three human gates. Policies remain in Standards; SDD defines records/workflows; the existing validator entry point delegates bounded checks to internal assurance and input-snapshot helpers. Skills continue routing through the canonical procedures.

Execution evidence binds reviewed source/test/configuration scopes with before/after snapshots. Maintained regression suites remain outside archived dossiers and run against the effective current contract. The validator checks declared consistency and freshness; agents/reviewers assess assertion adequacy and behavior. Historical inventory preserves older snapshots, while selected delivery and trusted CI-baseline candidates require live checks. Full required suites continue to run.

Compatibility is explicit: immutable historical v2 bytes and bounded approved in-flight v2 plans coexist with unchanged pre-v2 exceptions. New work uses v3. This source revision does not authenticate execution, add automatic check execution, publish a release or migrate installed consumers.

The existing pre-PR archival rule is mechanically checked with `--require-archive`: local selected preflight checks location, prepared closure and live delivery; trusted CI baseline selection covers affected active and archived dossiers for non-draft PRs and main pushes. Planning drafts retain inventory behavior. Ordinary delivery remains a pre-move eligibility check. This refines ADR-0013/0014 enforcement within the existing validator/CI boundaries, without a new planning gate or remote-publication capability.

## Explicit execution in the unreleased source

[ADR-0015](../decisions/0015-explicit-test-execution-and-skill-evaluations.md) keeps bounded explicit test execution under `scripts/testing/` and adds supervised Skill scenario/verification helpers under `tests/skills/`. Pure configuration/report enforcement lives in `validators/testing/` and versioned `schemas/`; policy remains in index-resolved Standards and lifecycle records remain in SDD. Consumer `.versat/validation.yaml` supplies explicit suites. The runner executes complete required suites or labeled targeted subsets and exports observed fragments without editing approvals, assessments or the dossier. Version-matched consumer wrappers verify exact provider identity; development fixtures identify a source snapshot explicitly.

Native scenario agents exercise versioned synthetic consumers under coordinator supervision. Available observations, original runner results, artifact differences and independent replay support local review evidence; fresh directories and context do not isolate permissions. Helpers do not invoke models or declare semantic acceptance. Required automated suites continue in deterministic CI; required supervised evidence is assessed before archival/submission and never becomes an automated CI pass. The unshipped credentialed CLI evaluator and protected model workflow are removed from this delivery. Final required remote CI remains separately observed before merge. See [project execution](../guides/project-validation.md) and [supervised evaluation](../guides/skill-evaluations.md).

## Public Harness preparation in the current source

[ADR-0016](../decisions/0016-public-harness-preparation-boundary.md) retains the same root Plugin and marketplace identities while separating preparation, effective license adoption and publication/consumer migration. Concrete Apache candidate terms and notices live under `docs/licensing/candidates/apache-2.0/`; their actual text approval is recorded separately from SDD gates. Maintained community guides describe intended access and truthful pending operations in EN/PT/ES.

The exact reviewed nine-file 0.4.0 patch from `docs/handoffs/harness-publication-readiness/` is now applied in the local delivery branch, with matching license/notice postimages. Main integration, release and catalog activation remain pending. Earlier disposable rehearsals retain their original scope. They do not create a maintained mirror, copied Standards distribution, release engine or automatic consumer migration. The original handoff retains its dated preparation evidence. Current unresolved prerequisites and separately authorized operational steps are recorded in the [publication-blocker handoff](../handoffs/harness-publication-blockers/README.md); required runtime/evidence gaps remain explicit.

Sensitive surface/control evidence stays in the selected restricted system with verified reviewer access. New public-facing preparation records contain only scrubbed summaries and opaque evidence identities; retained historical exposure still requires its separately reviewed disposition. Historical approvals and frozen records remain unchanged; exposure conflicts defer publication and require separate remediation decisions. Tests, local preparation and text approval cannot establish anonymous access, public reporting or configured remote protections.

The approved R2 operational handoff selects GitHub Free: private clearance/adoption, separately authorized visibility with immediate main protection/readback within 15 minutes, then actual public enforcement/reporting/external-use checks before later release. This is a bounded operation sequence, not configured protection or a new architectural boundary. The [transition procedure](../handoffs/harness-publication-blockers/transition.md) records scope, failure handling and unverified outcomes; canonical Standards and ADR-0016 remain unchanged.

## Revision-based quality validation

[ADR-0017](../decisions/0017-revision-based-code-quality-checks.md) places coding and changelog policy in index-resolved Standards. A read-only Git comparator and pinned Ruff checks run from local validation and CI through `scripts/validate/quality.sh`. The comparator selects changed tracked Python files and checks new Unreleased notes against the event or developer-selected base. Required suites and the structural SDD archive selector keep their existing responsibilities. The Python reference wrapper verifies its exact provider before running quality and suites. Reviewers assess semantic design and release-note accuracy. See [project validation](../guides/project-validation.md) for adoption and rollback.

## Consumer documentation and PR reporting

[ADR-0018](../decisions/0018-consumer-documentation-and-pr-reporting.md) keeps consumer layout and documentation obligations in the index-resolved Documentation Standard. Bootstrap provides its shared discovery record and adds reader material when applicable. SDD stages guide documentation planning and verify affected usage with existing evidence. New consumer ADRs can use explicit paths while historical identifier references continue to resolve.

The advisory documentation validator reads two Git commits without reading working-tree document contents. The GitHub PR job publishes mechanical results in its check summary using read access. Content quality, semantic alignment and publication access remain human review items. Product teams own publication. Consumer CI adoption is optional at the exact provider commit, and the required validation jobs keep their existing responsibilities.
