# SIFEN source index and precedence

## Snapshot scope

The supplied collection comprises 31 PDFs and two RARs: Technical Manual v150, Notes 1–27, Guia de Pruebas (February 2026), Guia de Mejores Prácticas (October 2024), a historical checksum list and two XMLs extracted from the archives. The declared cutoff is NT 27, available in Test and Production on 2026-03-09. This index translates the supplied summary; verify each applicable rule in its original source.

## Decision order

1. Identify environment and target date.
2. Locate the Manual v150 baseline and every Note mentioning the same ID, group, field, code or section.
3. Order changes by effective date for that environment, falling back to the document date only when none is specified.
4. Apply additions and amendments cumulatively; deactivate eliminated/excluded validations.
5. Use operational guidance after consolidating format and validation rules.

Note number is not a substitute for chronology: NT 8 and 9 predate NT 7. NT 25's header says `23/04/2024`, while Test/Production availability is 28/04/2025 and preparation/revision history is April 2025; the supplied index uses 28/04/2025 as the effective date. Verify newer official documentation when current compliance is requested.

## Technical Manual v150 map

| Subject | Extract | Physical PDF pages |
|---|---|---|
| Index and version control | [00](extracted-text/manual/00-index-and-version-history.txt) | 1–15 |
| Model, XML, certificates, signature | [01](extracted-text/manual/01-operating-model-and-technology.txt) | 16–42 |
| Web Services | [02](extracted-text/manual/02-web-services.txt) | 43–56 |
| CDC, timbrado and DE format | [03](extracted-text/manual/03-electronic-document-format.txt) | 57–112 |
| Events | [04](extracted-text/manual/04-event-management.txt) | 113–145 |
| Validations | [05](extracted-text/manual/05-validations.txt) | 146–193 |
| KuDE, QR, catalogs and glossary | [06](extracted-text/manual/06-kude-qr-codes-glossary.txt) | 194–217 |

`PAGE` markers identify physical PDF pages; printed Manual numbering is usually one lower. Preserve that distinction in citations.

## Technical Notes catalog

Dates below reproduce the supplied index's document/effective dates. Test/Prod qualifiers distinguish environment availability. Consult [Notes](extracted-text/notes/) and [original PDFs](original-sources/) for exact conditions.

| NT | Declared date/effectivity | Main changes |
|---|---|---|
| 1 | 14/10/2019 | Global discount per item; discount/advance totals; `F009`, `F033-F035`, `F011`, `F012`, `F014` formulas and validations. |
| 2 | 16/07/2020 | `D208`, `D210`; eliminates `D208d/1322`, `D210a/1323`. |
| 3 | 18/11/2020 | `D219`, `D223` conditioned on `D213`/`D202`; eliminates `D219/1324`, `D223/1327`. |
| 4 | 29/12/2020 | Eliminates `D101a/1251` (disabled issuer RUC). |
| 5 | 09/02/2021 | `D204` becomes 1-1; registration `E965` length 6–7, required when `E967=2`. |
| 6 | 25/03/2021 | Adds `D011a/1216`: transaction type must not be supplied when `C002` is neither 1 nor 4. |
| 7 | 01/02/2022 | Extends `B006` with tax information and export/remission-note requirements. |
| 8 | 21/09/2021 | Changes `EA797` and `F023` formula/conditions. |
| 9 | 09/09/2021 | `E701` uniqueness/repetition; `E708` length 1–2000. |
| 10 | 04/02/2022 | Removes `A005`; changes D/E/H fields, invalidation event, schemas, recipient, associated document, QR/URL, tax-affectation code and namespace. |
| 11 | 20/10/2022 | Bulk RUC lookup, schemas, fields and responses `0520-0523`. |
| 12 | 21/02/2023 | `D022/1213`: Autofactura (`C002=4`) must use PYG. |
| 13 | Test 21/04/2023; Prod 17/06/2023 | Partial IVA: `E735`, new `E737`, `F002/F004/F005` subtotals, validations `1921`, `1910`, `1911`, `2353`, `2357`, `2359`. |
| 14 | Test 31/05/2023; Prod 08/08/2023 | FE Nomination event `GENFE001-027`, validations `4451-4478`. |
| 15 | Test 21/08/2023; Prod 21/09/2023 | Adds `H004i/2442` for associated-CDC recipient and nomination. |
| 16 | Test 25/08/2023; Prod 22/09/2023 | Signature/certificates under Law 6822: RSA-SHA-2, SHA-2 digest, canonicalization, enveloped signature, X509, CRL/PCSC, TLS/signature validations. |
| 17 | Test 24/08/2023; Prod 25/08/2023 | Changes `D222/1326`, `D224/1329` messages. |
| 18 | Test 01/12/2023; Prod 08/01/2024 | Affected obligations `D030-D032`, table 12, `1220/1221`; transport `4325-4335`, new `GET002/4336`. |
| 19 | Test 15/12/2023; Prod 31/01/2024 | Recipient events, 45/15-day periods, CDC count/state, signature `AD04/0143`; eliminates old sequence matrix. |
| 20 | Test 15/12/2023; Prod 31/01/2024 | Adds `E827 dCodConDncp`; requires B2G for OEE recipient in `D202b/1332`. |
| 21 | Test/Prod 01/01/2024 | `D208c/1321`: unnamed-recipient threshold Gs. 35.000.000, except medical samples. |
| 22 | Test/Prod 09/02/2024 | Prevents duplicate affected obligation `D031a/1222`. |
| 23 | Test 30/08/2024; Prod 27/09/2024 | Recipient, item quantity, energy, merged RUC/associated documents; units of measure 111–140. |
| 24 | Test/Prod 01/01/2025 | Replaces `D208c/1321` threshold with Gs. 7.000.000. |
| 25 | Test/Prod 28/04/2025 | Excludes cancellation validation `GEC002c/4004`. |
| 26 | Test 09/06/2025; Prod 16/06/2025 | Public procurement/DNCP optional for B2G; excludes `E020/1400`, `E020a/1401`, `E704/1800`, `E705/1801`. |
| 27 | Test/Prod 09/03/2026 | Removes value 5 from `GENFE010/GENFE011` document types/descriptions in FE Nomination. |

## Critical replacements in this snapshot

Use NT 24's Gs. 7.000.000 threshold instead of NT 21's Gs. 35.000.000. Apply NT 26 optionality for `E020`, `E704`, `E705` and remove its four excluded validations. Do not apply `GEC002c/4004` after 28/04/2025. Use NT 27's nomination list, NT 16 for signatures, NT 19 for recipient events without the eliminated matrix, and NT 13's `E737` and partial-taxation formulas. These reminders require source/date checks before application.

## Guides and integrity

The October 2024 best-practices guide covers XML hygiene, batches, polling, retries, blocking, endpoints and SOAP examples. The February 2026 testing guide describes suggested Test data and coverage; Test documents have no legal value.

The preserved [source manifest](source-manifest.csv) contains original sizes/hashes and pre-import paths. Resolve them through [import inventory](import-inventory.json); use [target integrity](target-integrity.json) for current paths. The historical list declares MD5 `25EB165A8506EFA3A255B863ABCCAE95` for `MT_E_Kuatia_V150_10_09_2019.pdf`; the local PDF has a different MD5. This may reflect another copy/package but prevents a binary-identity claim. See [provenance](provenance.md) for distribution limitations.
