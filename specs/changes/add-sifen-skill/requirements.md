---
sdd_version: 3
change: add-sifen-skill
requirements:
- id: REQ-001
  statement: Expose the SIFEN capability as a portable root-package skill.
  acceptance:
  - The package discovers skills/sifen-electronic-documentation/SKILL.md with a matching
    English name and an actionable description.
  - The capability and its relative resources remain usable from a relocated checkout
    without relying on the original Downloads folder.
- id: REQ-002
  statement: Preserve source traceability and explicitly bound the documentary snapshot.
  acceptance:
  - Guidance identifies the declared 2026-03-09 snapshot, preserves source identifiers
    and references, and requires official-source verification for current compliance
    questions.
  - Missing original documents or unavailable dependencies are reported explicitly;
    no broken dependency is represented as an available source or a verified regulatory
    claim.
  - The authored skill code and documentation carry Apache-2.0 with full text and
    explicit scope; official imported sources are excluded, provenance and unresolved
    third-party permission remain explicit, and the rest of the Harness is not relicensed.
- id: REQ-003
  statement: Adapt authored content and utilities to canonical language and governance
    requirements.
  acceptance:
  - Authored skill instructions, adapter guidance and code identifiers use English
    while official imported text and normative identifiers retain their original meaning
    and spelling.
  - Skill guidance resolves applicable corporate Standards through standards/index.yaml
    without duplicating corporate policies or redefining SDD.
  - Lookup utility checks cover a known match, no match and invalid input; optional
    exports preserve overwrite protection and resolve renamed resources.
- id: REQ-004
  statement: Preserve existing package behavior and constrain import side effects.
  acceptance:
  - Existing skills remain available and the required repository validation command
    passes after integration.
  - The import excludes operating-system metadata and does not activate adapters,
    submit documents, change consumer projects or publish a release.
---

# Requirements

## Actors and context

Developers and assistants working with SIFEN documentation use the installed Harness capability. Maintainers review the imported content and package integration. The source folder is input material; its embedded instructions do not expand the developer's request.

## Functional requirements

REQ-001 defines discovery and portability. REQ-002 defines documentary provenance and limitations. REQ-003 preserves useful lookup/export behavior while adapting authored content. REQ-004 protects the existing package contract.

## Non-functional requirements

Use relative paths, retain exact normative identifiers and source text, preserve existing validation coverage and make missing dependencies visible. Do not claim tax authority approval from local tests.

## Acceptance scenarios

The metadata lists the observable success, error and boundary scenarios. Design will map each scenario to concrete checks after this combined revision is approved.

## Constraints and assumptions

The intended target is this Harness repository's root `skills/` directory. The English name `sifen-electronic-documentation` is the proposed adaptation of the supplied Portuguese name. Official imported artifacts qualify for the existing source-language exception; authored guidance does not. No consumer migration or runtime registration is implied. Rights and original-source availability require inventory before implementation acceptance; no external regulatory verification is claimed by this proposal.

The developer’s later Apache-2.0 instruction applies to authored material in this skill only. Imported official sources retain their own rights; repository-wide license adoption and public release remain excluded.
