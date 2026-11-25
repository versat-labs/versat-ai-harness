# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog, and the project follows Semantic Versioning.

## [Unreleased]

### Fixed

- Validate the resources of every packaged Skill after relocation, including SIFEN.

### Added

- index-resolved public GitHub security policy, read-only live/offline verification, safe configuration rendering and mandatory readiness guidance for bootstrap, audit and maintenance; exact release publication and consumer adoption remain separate.
- index-resolved coding and changelog standards, with pinned Python lint and formatting checks and Git-based changelog validation in the Harness and Python reference integration.

### Changed

- rename the candidate marketplace to `versat` while keeping plugin `versat-ai-harness`; document later manual reinstallation for the two current users and retain explicit pending native/external checks.

## [0.4.0] - Unreleased candidate

### Prepared

- integrated Apache-2.0 license/notices on public main and shared CODEOWNERS; main protection and the internal review-control test were verified operationally;
- changed the local candidate catalog identity to `versat` / `Versat Plugins`, retaining plugin `versat-ai-harness`, policy and exact `v0.4.0` selection; existing `versat-internal` installations are not migrated;
- added marketplace identity/label regression checks and EN/PT/ES transition guidance; the approved two-user handoff accepts main synchronization and later manual reinstallation, while native/external observations remain pending and v0.4.0 is not yet available;
- public Apache-2.0 candidate for eligible first-party Harness material, with retained third-party notices and independent destination-project terms;
- multilingual contribution, reporting, setup and recovery guidance with explicit pending external-user verification;
- separate preparation, adoption and operational handoff with private evidence and no automatic consumer migration.

The reviewed license/notices are integrated on public main. This candidate entry does not assert a versioned release date or completion of pending external checks. The following previously unreleased source capabilities are included in the candidate review.


### Added

- explicit configured project suite execution, structured test counts, bounded attempt logs and current SDD evidence fragments;
- optional consumer validation assets and first-use guides with exact provider verification and migration/rollback guidance;
- supervised native-subagent Skill evaluation procedure, synthetic cases and independent verification helpers alongside complete deterministic CI;
- offline regression tests for execution, evidence, consumer adoption, evaluation and CI eligibility.

### Changed

- integrated coverage creation/reuse and full regression execution into canonical testing and SDD guidance;
- extended package validation with execution/adapter tests while preserving existing SDD regression and archive checks.

## [0.3.0] - 2026-09-29

### Added

- central SDD developer guide, structured review/evidence contracts and a stage-aware JSON Schema validator;
- regression cases for approval freshness, traceability, delivery readiness and explicit legacy migration;
- ADR-0013 governing single-Skill routing and documentary closure in the implementation PR;
- product discovery guidance and an overview template for project bootstrap;
- a first-use quickstart in consumer project templates and explicit scenario coverage guidance for SDD validation.

### Changed

- consolidated SDD access in `versat-sdd`, with explicit routing to canonical workflows and three human planning gates;
- prepared documentary archival alongside code and living specifications before merge, with read-only delivery confirmation;
- included SDD validation and regression tests in the local and CI entry points, and corrected Skill review ownership;
- separated consumer Skills, Codex custom agents and Versat operational workflows through a canonical artifact Standard and updated agent/hybrid template guidance;
- added explicit authoring templates, a supplier-payment workflow example and reviewed migration guidance while preserving the Harness Plugin package layout;
- clarified Plugin role guidance, SDD procedures and validation limits; recorded ADR-0012 for consumer artifacts and the `agent-project-layout` SDD change.
- replaced the obsolete nested Plugin CODEOWNERS path with current Skills, role guidance and project-template ownership.
- defined Shortcut-linked branch names and typed commit messages in the canonical Git Standard, preserving English technical descriptions and gradual adoption;
- added Story traceability prompts to SDD and PR review, with explicit squash, parser compatibility and validation guidance;
- clarified merged-branch and worktree cleanup without treating a documentary archive path as proof of delivery.

### Removed

- the standalone `new-change` Skill; its planning behavior and developer guidance now belong to the canonical SDD process.

## [0.2.0] - 2026-09-08

### Added

- portable Agent Plugins manifest at the repository root;
- private GitHub marketplace metadata for ChatGPT workspace distribution;
- deterministic validation for portable and compatibility manifests, marketplace pinning and version agreement;
- ADR-0011 and SDD artifacts governing the package-boundary migration.

### Changed

- made the repository root the installable Plugin package boundary;
- moved Skills and reusable agent roles to root-level directories;
- updated Skills to resolve canonical artifacts from the installed Plugin root;
- aligned legacy technical documentation, ADRs, SDD templates and Plugin metadata with the canonical language standard;
- superseded ADR-0008 with ADR-0010 to record the refined language policy;
- superseded ADR-0001 and ADR-0002 with ADR-0011.

## [0.1.0] - 2026-08-28

### Added

- initial Versat AI Harness architecture;
- Plugin manifest and five foundational Skills;
- declarative Standards catalog;
- initial SDD process, schemas, templates and workflows;
- composable templates for project profiles;
- validation contracts and minimum CI pipeline;
- architecture documentation and foundational ADRs.
