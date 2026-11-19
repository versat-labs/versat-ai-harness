# Source provenance and disposition

## Identity and authority

Input: the developer-supplied `sifen-documentacao-eletronica` folder. Declared documentary snapshot: 2026-03-09. Imported in change `add-sifen-skill` on 2026-11-17. The package contains authored skill instructions, utilities and summaries, plus official SIFEN/DNIT documents, extracted text and historical XML examples.

The developer stated in this change's conversation: “Use a msm licença das outras skills do projeto, origem desenvolvida por mim msm”. This records declared authorship of the skill's authored material and authorization to include/adapt it under the same regime as the other Harness skills. It does not assert ownership of official third-party documents. The technical review is recorded under `docs/validation/add-sifen-skill/` in the Harness repository; normal governed review remains with the repository CODEOWNERS.

## Terms and distribution status

The developer directed Apache-2.0 for this skill's authored material on 2026-11-17. The [license scope](../LICENSE-SCOPE.md) identifies those files and the official materials excluded from the grant.

The developer approved redistribution of the reviewed SIFEN corpus and the attribution wording on 2026-11-18. See the [official-material notice](attribution-notice.md) and [per-file attribution inventory](official-source-attribution.csv) for the DNIT source URLs, parent publications, and DNIT-reported HTTP Last-Modified timestamps when available. These timestamps describe the published files and are distinct from substantive document dates and effective dates. The review identified Decree 4064/2015, article 38 and Annex II, as the basis for redistribution of these identified materials. The approval covers the reviewed corpus in the public draft PR and Versat's internal operational use.

## Inventory and transformations

[import-inventory.json](import-inventory.json) records every supplied file, its source SHA-256, target path and disposition. Original source bytes, extracted official text, XML examples and the supplied [source-manifest.csv](source-manifest.csv) are preserved. The manifest retains its original Portuguese column names and original paths as historical evidence; resolve them through the import inventory, not relative to the renamed directories. [target-integrity.json](target-integrity.json) records target paths and hashes of imported/adapted files, excluding itself to avoid self-reference.

Authored instructions, summaries, adapter guidance, script identifiers and command-line interfaces were adapted to English. Manual-section and authored directory names were translated; official titles and source filenames remain in the import inventory. Three accented target filenames use ASCII names to preserve identical paths across macOS and Linux. Official extracted text was not translated. OS metadata was excluded. The source folder was not modified.

The original manifest's 35 entries were checked against their source files before import. This establishes local consistency only. The historical checksum list and the local Manual PDF disagree on MD5; do not claim binary identity with the historical published Manual. Dates in authored summaries are snapshot assertions to check against their originals for each question; no current-law or production conformity determination was performed during this import.
