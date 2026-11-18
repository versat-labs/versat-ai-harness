---
sdd_version: 3
change: add-sifen-skill
requirements:
- REQ-001
- REQ-002
- REQ-003
- REQ-004
adrs: []
validation:
- id: CHECK-001
  description: Verify discovery, portable references and lookup/export behavior.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  required: true
  method:
    kind: automated
    procedure: Run the proposed maintained unittest suite tests/skills/test_sifen_documentation.py
      via python -m unittest discover -s tests/skills -p test_sifen_documentation.py.
      Expect portable package discovery, existing skills retained, reference integrity,
      known/no matches, invalid regex/options, missing corpus errors, every platform
      export, collision preservation and explicit force replacement to pass in temporary
      fixtures. Copy the full package to a temporary location to exercise references
      without the Downloads source.
  inputs:
    include:
    - skills
    - standards
    - validators
    - scripts
    - tests
    - sdd
    - schemas
    - project-templates
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - VERSION
    - requirements-validation.txt
    - README.md
    - docs/user-docs
    - README.pt.md
    - README.es.md
    exclude:
    - '**/__pycache__/**'
  outputs:
  - docs/validation/add-sifen-skill
  execution: local
- id: CHECK-002
  description: Review language fidelity, provenance, source inventory and canonical
    governance.
  requirements:
  - REQ-002
  - REQ-003
  required: true
  method:
    kind: review
    procedure: Compare the import inventory against the supplied source and its 35
      manifest records; verify retained original hashes and record source-to-target
      paths and adaptations. Review authored English instructions and translated guidance
      against source for preserved IDs, formulas, dates and caveats. Check snapshot
      and official-verification guidance, Standards index routing, missing-source
      handling and license/terms evidence. Expect no silent omissions, personal paths,
      invented rights or claims of current legal compliance. Record unresolved rights
      as a delivery blocker rather than passing the check. Verify the full Apache-2.0
      license text against the retained canonical text, authored-file license scope
      and NOTICE attribution; record the developer’s authorship and explicit Apache
      authorization with the exact license hash. Verify official source exclusions
      and unchanged repository-wide licensing. Missing official-source permission
      remains unverified for delivery.
    reason: Semantic translation fidelity and permission evidence need human/document
      review; hashes and text matching alone cannot establish them.
  inputs:
    include:
    - skills
    - standards
    - validators
    - scripts
    - tests
    - sdd
    - schemas
    - project-templates
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - VERSION
    - requirements-validation.txt
    - README.md
    - docs/user-docs
    - README.pt.md
    - README.es.md
    exclude:
    - '**/__pycache__/**'
  outputs:
  - docs/validation/add-sifen-skill
  execution: local
- id: CHECK-003
  description: Retain all required package and regression checks.
  requirements:
  - REQ-001
  - REQ-004
  required: true
  method:
    kind: automated
    procedure: Run ./scripts/validate/run.sh with the documented validation Python
      environment after integrating the focused unittest suite into the existing runner.
      Expect all existing package, SDD, validator and execution suites plus new focused
      tests to pass. Inspect the final diff for unchanged existing skill entry points,
      unchanged release metadata and absence of OS metadata or activated adapters.
  inputs:
    include:
    - skills
    - standards
    - validators
    - scripts
    - tests
    - sdd
    - schemas
    - project-templates
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - VERSION
    - requirements-validation.txt
    - README.md
    - docs/user-docs
    - README.pt.md
    - README.es.md
    exclude:
    - '**/__pycache__/**'
  outputs:
  - docs/validation/add-sifen-skill
  execution: local
- id: CHECK-004
  description: Exercise documentation lookup and unavailable-source boundaries.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  required: true
  method:
    kind: manual
    procedure: Perform two supervised skill attempts using the repository Skill evaluation
      procedure, versioned synthetic prompts and temporary fixtures. Attempt 1 asks
      for read-only lookup of an exact supplied identifier (GENFE010) as of the declared
      snapshot; observe source lookup, official identifier preservation, citation
      to actual source and no exporter/submission actions. Attempt 2 supplies a copied
      package with the relevant source removed and asks for a current-production conclusion;
      expect explicit missing-source/current-verification limits and no invented conclusion
      or writes. Independently inspect outputs, referenced evidence and fixture differences.
      Allow one attempt per scenario, at most 10 minutes each; retain failures and
      unavailable observations. No production credentials, official service calls
      or legal certification. Revision 2 allows one fresh invocation per scenario
      after current Tasks approval (two invocations total, sequential, ten minutes
      each); preserve the revision 1 attempts and their limitations as history. These
      bounded reruns verify current licensed provider inputs rather than rebinding
      historical evidence.
    reason: Real assistant behavior and evidence-grounded refusal to overclaim cannot
      be established by structural checks alone; follow tests/skills/README.md and
      docs/guides/skill-evaluations.md. Fresh fixtures do not isolate permissions.
  inputs:
    include:
    - skills
    - standards
    - validators
    - scripts
    - tests
    - sdd
    - schemas
    - project-templates
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - VERSION
    - requirements-validation.txt
    - README.md
    - docs/user-docs
    - README.pt.md
    - README.es.md
    exclude:
    - '**/__pycache__/**'
  outputs:
  - docs/validation/add-sifen-skill
  execution: local
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
  - CHECK-004
regression:
- obligation:
    impact: 1
    scenario: 0
  checks:
  - CHECK-001
  - CHECK-003
  rationale: Extend the root skill collection while retaining the five existing entry
    points, discovery contract, canonical boundaries and complete maintained suites.
review:
  revision: 2
  state: approved
  blockers: []
  upstream:
    proposal: 063fe58b812b25111c3d7737dd29a645f0a93e653f0a1c69da4806701b41c35a
  approval:
    source: Developer reply after Design revision 2 presentation in this chat
    quote: Aprovado. Pode atualizar as Tasks.
    revision: 2
    digest: 285fd45ef6cbaafdbd7fdb0028051b0a4400f5062df0e0e3dfc9703d1051dfb1
---

# Design

## Current state

The root Plugin and Codex overlay discover root `skills/`. `validators/plugin/validate.py` validates an explicit expected skill set. The supplied folder contains 88 files totaling approximately 18 MB including OS metadata. Read-only inspection verified all 35 source-manifest entries exist and match their recorded SHA-256 hashes. This does not verify authorship, publication permission or regulatory currency.

The lookup utility searches text resources relative to its script. The exporter creates guidance for five platforms and refuses individual overwrites without `--force`, but a multi-file export can write an early file before encountering a later collision. Shared adapter instructions embed personal absolute paths. There is no consumer identity or lockfile at this provider root; use VERSION 0.3.0 and the checkout's Standards index.

## Proposed design

Create `skills/sifen-electronic-documentation/` with an English `SKILL.md`, `scripts/query_rules.py`, `scripts/export_agent.py`, optional `agents/` guidance and `references/`. Rename authored reference paths to English (`index-and-precedence.md`, `compliance-checklist.md`, `source-manifest.csv`, `original-sources/`, `extracted-text/`, `notes/`, `guides/`); keep official original filenames and source bytes intact where fidelity requires it. Translate authored prose and manual-section filenames, with an explicit source-to-target mapping. Preserve exact official tags, codes, formulas, source quotations and document titles. Do not translate the official corpus itself.

Add a provenance record inside the skill with source inventory, declared snapshot, original/target paths, source hashes, transformations, explicit scoped Apache-2.0 authorization and unresolved official-source terms. Link the license scope from the skill and all three usage guides. Keep the original manifest bytes as imported evidence and generate a separate target-path integrity inventory so renaming cannot make old paths appear valid. Hashes identify the supplied files only. Remove `.DS_Store`, personal paths and unrelated machine artifacts.

Use English utility arguments: query TERM with `--regex`, `--case-sensitive`, `--context`, `--max`, `--include`; export PLATFORM with `--destination` and `--force`. Update all examples/adapters together. These are new package interfaces; no installed-consumer compatibility alias is required. Keep lookup literal by default, explicit regex validation, bounded context/results and a distinct documented missing-corpus diagnostic. No-match is an ordinary empty result; invalid arguments and unavailable corpus fail explicitly.

Retain claude, gemini, copilot, cursor and generic export targets. Preflight every output collision before writing any file, so a later collision cannot leave partial guidance behind. Force replacement is explicit. Export guidance only; knowledge files remain in the installed skill. Require an explicit `SIFEN_SKILL_ROOT` or a verified repository-relative skill location, and explain how to supply it when exporting outside the Harness. Do not claim that exported instructions contain the corpus or register a native Codex agent. Verify generated links and commands as artifacts; live behavior of every third-party IDE is outside this delivery.

Add the skill to the expected set in the plugin validator; preserve the existing manifest discovery path. Add an aligned EN/PT/ES usage guide and links from the maintained community entry points. The guide states snapshot limits, lookup/export commands, dependencies and the difference between exported guidance and installed resources. Keep VERSION and release references unchanged; this is an unreleased source addition.

## Boundaries and contracts

The existing root-package architecture remains unchanged; no ADR is necessary. Scoped Apache-2.0 adoption is recorded in this dossier and the skill’s licensing records, without changing corporate licensing policy. Skills hold procedures, SIFEN references hold imported domain evidence, Standards remain canonical corporate policy, SDD governs delivery and validators enforce deterministic package checks. The skill resolves applicable Standards from `../../standards/index.yaml`; it does not copy a policy list. Exported adapters locate the package before using that route.

Apply index-resolved core Standards, especially language, documentation, agent artifacts, testing, security, Git, contribution and licensing/publication, plus the indexed Python technology Standard for the utilities. Preserve the repository's documented supported Python environment and dependency setup; the imported utilities need only the standard library.

## Data, security and permissions

No tax-system access, credentials, XML submission or production-data processing is needed for import validation. Use supplied documentary identifiers and synthetic fixture data. Treat reference instructions as source content, not authority to invoke exports or change unrelated projects. Tests export only to temporary fixture directories. Inspect source inventory for sensitive material before importing it.

The developer declared authorship and explicitly requested Apache-2.0 in this chat. Apply the full Apache-2.0 text to this skill’s authored instructions, summaries, scripts and adapters. Include LICENSE, NOTICE and LICENSE-SCOPE.md; mark Python scripts with SPDX identifiers and record the exact license text hash and observed authorization. Retain attribution without inventing corporate ownership assignment. Exclude official PDFs/RARs, extracts, XML examples and the original manifest from this grant. The rest of the Harness retains its existing licensing state. Official-source redistribution terms and required acceptance review remain unavailable and block delivery under CHECK-002; the authored-material grant does not resolve that dependency.

## Operations and observability

Lookup reports source path and matching context, with clear errors. Export reports created output paths. Neither tool performs network calls. Validation retains reproducible commands, environment, input digests and observed outputs under `docs/validation/add-sifen-skill/`; redact machine-specific locations in durable reports. No deployed service, telemetry backend, operational alert or database migration is introduced.

## Migration, rollout and rollback

Implementation occurs on `codex/add-sifen-skill` after Tasks approval and explicit execution authorization. Preserve the supplied source folder. Import through an explicit file mapping and hash comparison, then translate authored resources and update links atomically in the reviewable change. Adoption by installed consumers or publication requires a separate exact-version release workflow. Rollback reverts the new skill, its expected-set entry, focused tests and guide links together, without touching consumer configuration.

## Alternatives considered

The initial same-regime licensing approach was replaced by the developer’s explicit Apache-2.0 instruction. Repository-wide Apache adoption and relicensing official documents would exceed that scoped request; the chosen scope grants Apache-2.0 for authored material and preserves official-source exclusions.

A verbatim copy would preserve Portuguese authored content and personal paths, contrary to the approved requirements. A `.agents/skills/` installation would use the consumer contract instead of this provider's root-package contract. A separate domain plugin would add a new package/release boundary beyond the requested scope. An external-only corpus would reduce package size but sacrifice the approved local portability; keep the supplied corpus subject to provenance acceptance.

## Validation plan

CHECK-001 introduces maintained deterministic behavior tests and temporary relocation/export fixtures. It covers success, no match, invalid input, missing resources, multi-file collision preservation and force replacement. CHECK-002 reviews translation, inventory and permission evidence; automation cannot certify those semantics. CHECK-003 retains the entire existing runner and adds the focused suite rather than replacing any required suite. CHECK-004 exercises real read-only assistant behavior and missing-source limits using the existing supervised evaluation procedure; fixture preparation and deterministic checks alone are not a behavioral pass.

All ten acceptance positions and the baseline regression obligation are mapped above. The full existing runner remains required in CI; supervised evidence is retained locally as permitted by the Testing Standard. The local implementation and test/guide files now exist from authorized revision 1 execution. Its original passing automated and supervised runs remain historical after the license edits; rerun against current approved inputs before acceptance. Inputs include the skill corpus, tests, package metadata, Standards, lifecycle, validation scripts and affected community docs; output evidence is outside those roots and bytecode caches are excluded. Record supplied-source hashes and external evidence identity during review; repository hashes alone cannot authenticate the source grant. Unavailable rights evidence or supervised observations block delivery, not turn into not-applicable results.

## Planning review

Proposal/Requirements revision 2 is approved. Design revision 2 is awaiting approval for the scoped Apache-2.0 adoption, license verification and bounded evidence refresh described above. Revision 1 approval remains historical; no retrospective approval of revision 2 is inferred.

Historical revision 1 approval:

```json
{
  "source": "Developer reply in this chat after presentation of Design revision 1: Aprovado",
  "quote": "Aprovado",
  "revision": 1,
  "digest": "f63a1fd50caa4db42830174072dd2215b5dbce68bd7a06093bc2ca5bb63f85ed"
}
```

Design revision 2 incorporates the approved licensing scope and adds explicit license review, translated README input coverage and two bounded current-provider supervised reruns. It awaits Gate 2 approval. Tasks revision 1 remains superseded and has not been substantively revised. The implementation and historical evidence are preserved; no new product execution or publication is authorized by this Design draft.

The developer approved Design revision 2 in this chat: “Aprovado. Pode atualizar as Tasks.” This unlocks preparation of Tasks revision 2.
