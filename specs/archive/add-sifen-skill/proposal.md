---
sdd_version: 3
change: add-sifen-skill
status: accepted
owner: Versat
summary: Add the supplied SIFEN documentation capability to the Harness skills package.
risk: medium
impact:
  state: assessed
  summary: Extend the existing root skill collection while preserving package discovery,
    governance boundaries and existing capabilities.
  items:
  - current_contract:
      change: add-sifen-skill
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-001
    - REQ-004
    reason: Add one domain capability without replacing existing skills or changing
      consumer installation contracts.
review:
  revision: 2
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply after presentation of Proposal/Requirements revision 2
      in this chat
    quote: aprovado
    revision: 2
    digest: 063fe58b812b25111c3d7737dd29a645f0a93e653f0a1c69da4806701b41c35a
---

# Proposal

## Context and problem

The developer supplied the local `sifen-documentacao-eletronica` folder and requested its addition to this project's skills through Versat SDD. The supplied package includes SKILL.md, references, two Python utilities and optional platform adapters. Its entry point describes a documentary snapshot dated 2026-03-09. That date is a source declaration, not verification of current regulatory completeness.

The target is the Harness source repository, version 0.3.0, whose installable capabilities live under root `skills/`. This is not a consumer project and has no consumer Standards lockfile; applicable core Standards resolve through this checkout's `standards/index.yaml`.

## Expected outcome

Provide a portable, discoverable SIFEN documentation skill with useful local references and utilities, adapted to the repository's English authoring policy and canonical governance. Preserve official Spanish source material and exact technical identifiers where required for fidelity.

## Scope

- Import and adapt the supplied capability under `skills/sifen-electronic-documentation/`, using an English directory and skill name.
- Include the supporting references and utilities needed by the capability, with working relative links and explicit provenance and snapshot limitations.
- Adapt authored instructions, identifiers, utility interfaces and optional adapter guidance to English; retain imported official material in its source language.
- Preserve the optional exporters' useful behavior without installing their instructions into unrelated project configuration.
- Exclude operating-system metadata such as `.DS_Store` and verify that documented original-source dependencies actually exist.
- Update applicable skill inventory/discovery documentation and validate the integration through existing checks and focused behavior checks.
- Apply Apache-2.0 to this skill’s authored code and documentation, as explicitly requested by the contributing developer after implementation authorization. Include the full license text and an explicit scope/attribution record; exclude imported official sources and do not relicense the rest of the Harness.

## Out of scope

Live SIFEN integration, tax submissions, certificates, production credentials, regulatory certification, public release, repository-wide license adoption, remote PR publication, consumer updates and automatic installation of platform adapters. No architectural boundary or corporate policy change is proposed.

## Work tracking

No Shortcut Story or issue was supplied. Change ID: `add-sifen-skill`. Local branch: `codex/add-sifen-skill`.

## Impact and risks

The source contains Portuguese authored guidance and utilities, official-language extracts and a manifest referring to original documents. Renaming can break paths or commands; translation can distort official identifiers. Verify portability and preserve exact identifiers and source quotations. Record missing originals explicitly rather than claiming the snapshot is complete. Supplied document instructions are material being reviewed, not authority to run exports, change other projects or contact tax services.

The contributing developer declared authorship of the supplied skill and subsequently instructed “use a licenca apache 2.0”. This authorizes a scoped Apache-2.0 grant for authored material; it does not establish third-party rights in official documents. Inventory and disposition of those sources must be resolved before accepting the combined package for distribution; unknown rights remain an explicit delivery limitation, not an inferred grant. This does not block review of the proposed scope. No current-law determination is made in this planning stage.

## Current contract baseline

The current root skill collection contains architecture-review, project-audit, project-bootstrap, project-maintenance and versat-sdd; there is no SIFEN skill or matching active/archive dossier. Root package discovery and existing skill behavior must remain usable. The package retains canonical Standards in `standards/`, process in `sdd/` and deterministic enforcement in `validators/`. Existing plugin and validation checks remain required. The integration extends this collection without changing those responsibilities or installing consumer artifacts.

## Proposal acceptance criterion

All requirements below have observable evidence, the existing required validation suite passes, and no unresolved source dependency or provenance issue is represented as verified availability or permission.

## Planning review

Revision 1 was approved in this chat with “Aprovado”; its historical approval is retained below. Tasks revision 1 was subsequently approved with implementation/validation authority. During execution the developer declared authorship and then explicitly requested “use a licenca apache 2.0”. This changes the previous license-adoption exclusion and creates revision 2. The scoped license files and completed local implementation are reviewable; the new combined scope awaits Gate 1 approval. Design and Tasks approvals are superseded, not silently rebound. No release or public export occurred.

Historical Proposal/Requirements revision 1 approval:

```json
{
  "source": "Developer reply in this chat after presentation of Proposal/Requirements revision 1: Aprovado",
  "quote": "Aprovado",
  "revision": 1,
  "digest": "ffcf1644640a50b3e6702471a2b0c2d72c71dd00e97186b885355a51bfc8b75f"
}
```

Proposal/Requirements revision 2 was approved in this chat with “aprovado”. Design revision 2 may now be reviewed.
