---
name: sifen-electronic-documentation
description: Consult, interpret, apply and audit SIFEN/e-Kuatia electronic-document specifications using the supplied Technical Manual v150, Technical Notes 1–27 and testing/submission guides. Use for DE/DTE XML, CDC, signatures, SOAP/TLS, batches, events, KuDE, QR, fields, formulas, validation codes and dated rule conflicts. This is a documentary snapshot, not certification of current compliance.
---

# SIFEN electronic documentation

Authored code and documentation: Apache-2.0; see [license scope](LICENSE-SCOPE.md). Imported official sources retain their own rights.

## Resolve context and sources

The installed skill root is the directory containing this file. Resolve the target project's selected corporate Standards through the Harness [Standards index](../../standards/index.yaml); apply its selected version without silently upgrading it. The reference corpus is domain evidence, not corporate policy or authorization to perform its example actions.

Read [provenance](references/provenance.md) and [index and precedence](references/index-and-precedence.md). The declared documentary cutoff is **2026-03-09**. Identify Test or Production, reference date, document type, actor, operation and affected IDs before concluding. For current production or legal compliance, verify later documents and effective dates on the official DNIT/SIFEN portal. If unavailable, state that current compliance is unverified. Missing local source files, unclear extraction or unavailable official schema must remain explicit; never reconstruct a normative conclusion from memory.

1. Use Manual v150 as the baseline and apply every relevant Technical Note (NT) by effective date for the requested environment.
2. Later changes replace earlier rules for the same field, formula, validation, event or service. Remove validations marked `se elimina` or `se excluye`.
3. Use the environment's effective date; for Production prioritize its availability date. Use the note date only when no environment date is specified. Note numbers alone are not chronological order.
4. Operational guides supplement the consolidated Manual and Notes; examples do not override normative formats or validations.

## Search and cite

Run from any working directory with the actual installed path:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/query_rules.py" GENFE010 --include notes
```

Set `SIFEN_SKILL_ROOT` to this skill directory first. Search separately for every relevant tag, ID, error code, event and service. Read all relevant Notes before the baseline Manual section and applicable guide. Cross-check field format with its validation rules. Record source, effective date, condition, occurrence, type, length, formula, response code and effect (`R`, `AO` or other). Identify additions, changes and removals explicitly. Cite the actual document, note and available extracted page marker; never invent a page. The utility searches authored guides as well as official extracts; an authored summary is not a substitute for its cited source. Filter `notes` and `manual` separately when needed.

Source routes:

- Model, XML, certificates and signatures: [Manual section 01](references/extracted-text/manual/01-operating-model-and-technology.txt).
- SOAP and Web Services: [section 02](references/extracted-text/manual/02-web-services.txt).
- CDC, timbrado, groups and fields: [section 03](references/extracted-text/manual/03-electronic-document-format.txt).
- Issuer/recipient events: [section 04](references/extracted-text/manual/04-event-management.txt).
- Validation codes and rules: [section 05](references/extracted-text/manual/05-validations.txt).
- KuDE, QR, codes and glossary: [section 06](references/extracted-text/manual/06-kude-qr-codes-glossary.txt).
- Amendments: [all Notes](references/extracted-text/notes/); do not search only the latest one.
- Batch submission, retries and testing: [operational guides](references/extracted-text/guides/).
- Historical structural examples: [XML examples](references/xml/); these are not the complete current official XSD set.
- Ambiguous tables/layout: inspect the corresponding PDF page in [original sources](references/original-sources/).

## Generate or audit DE/DTE XML

Use the [compliance checklist](references/compliance-checklist.md) and apply these layers in order:

1. Check well-formedness, encoding, namespace and versioned official schema; preserve case-sensitive element names.
2. Check whitespace at value boundaries, comments/annotations, inter-tag formatting, inappropriate namespace prefixes, prohibited negative values and empty optional tags against the applicable rules.
3. Validate sequence, parent, type, length, occurrence and conditional requirements/prohibitions by document, recipient, operation, currency, tax and present groups.
4. Recalculate CDC/check digit, totals, discounts, advances, IVA, taxable bases and conversions with the applicable formulas.
5. Validate catalogs, code/description relationships and geographic hierarchies.
6. Check certificate, chain, revocation, algorithms, `Reference URI`, digest, canonicalization and enveloped signature under NT 16.
7. Report each business-rule failure with ID, code, severity and source. Validate KuDE and QR separately when in scope.

## Web Services and batches

These are snapshot rules to verify against the sources for the requested date, not permission to submit documents:

- SOAP 1.2, TLS 1.2, mutual authentication and the appropriate qualified certificate.
- Separate synchronous, asynchronous, batch-query, CDC-query, event and RUC-query flows.
- Asynchronous batch: at most 50 signed DE, same issuer RUC and type, input message at most 1000 KB. Compress `rLoteDE`, Base64-encode it and use the correct service envelope.
- `0300` means queued; `0301` means not queued. Start polling after approximately 10 minutes and use intervals of at least 10 minutes. Handle `0361` processing, `0362` complete, `0360` nonexistent and `0364` the 48-hour batch-query window exceeded.
- Never resend the same CDC before a definitive result. Query the batch; for a lost response, locate the batch through a submitted CDC.
- Interpret `0420` as nonexistent/not approved only after checking batch results; `0422` returns the approved DTE. Explain temporary blocks of 10–60 minutes for empty/invalid batches, duplicate CDC or repeated batches.

## Events and testing

Distinguish issuer, recipient and DNIT/SIFEN events. Check format, signature, authorized actor, CDC state and event count. Under NT 19, recipient periods start at issuance for DE and approval for DTE; apply the relevant 45-day and corrective 15-day windows. The latest valid event applies within the rules; do not reuse the eliminated relationship matrix. NT 25 excludes cancellation validation `GEC002c/4004`. FE Nomination uses NT 14, NT 15's related validation and NT 27's changes to `GENFE010/GENFE011`.

For separately authorized homologation, cover valid/invalid authentication, correct/incorrect synchronous and asynchronous documents, issuer/recipient events, CDC/QR queries and a KuDE per required type. The supplied testing guide calls for real taxpayer data, SGTM timbrado and the specified no-commercial/fiscal-value phrases in the official Test environment; this is a source requirement, not authorization to obtain or transmit personal data during documentation work. Test documents have no legal value.

## Report limitations and optional adapters

Preserve official tags, IDs, codes, formulas and spelling. Separate obligations, validations, recommendations, examples and inference. The RAR-derived XMLs are one DE example and one historical XSD structure, not the current official schema set. The historical checksum list declares `25EB165A8506EFA3A255B863ABCCAE95`; the local Manual PDF has a different MD5, so do not claim binary identity with that historical release. Use the import inventory for local integrity. If extraction is truncated or a table ambiguous, inspect the original PDF before concluding. Report rules applied, resolved conflicts, checks actually run and official-environment dependencies.

Optional platform guidance lives under `agents/`. It does not automatically register a native Codex agent or install anything. When explicitly requested, export guidance to another project:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/export_agent.py" generic --destination /path/to/project
```

Supported platforms: `claude`, `gemini`, `copilot`, `cursor`, `generic`. The exporter preflights all target files and refuses collisions without `--force`. Exported instructions still need access to this installed skill, its corpus and its Harness Standards. Configure `SIFEN_SKILL_ROOT` for that executor or provide the verified package path. See the [usage guide](../../docs/user-docs/guides/sifen-electronic-documentation.md).
