# Source provenance and disposition

## Identity and authority

Input: the developer-supplied `sifen-documentacao-eletronica` folder. Declared documentary snapshot: 2026-03-09. Imported in change `add-sifen-skill` on 2026-11-17. The package contains authored skill instructions, utilities and summaries, plus official SIFEN/DNIT documents, extracted text and historical XML examples.

The developer stated in this change's conversation: “Use a msm licença das outras skills do projeto, origem desenvolvida por mim msm”. This records declared authorship of the skill's authored material and authorization to include/adapt it under the same regime as the other Harness skills. It does not assert ownership of official third-party documents. The technical review is recorded under `docs/validation/add-sifen-skill/` in the Harness repository; normal governed review remains with the repository CODEOWNERS.

## Terms and distribution status

The current Harness has no adopted root public license; its repository-wide Apache-2.0 candidate remains inactive. After the initial same-regime instruction, the developer explicitly directed “use a licenca apache 2.0” on 2026-11-17. Apache-2.0 is applied to this skill’s authored code and documentation under [LICENSE-SCOPE.md](../LICENSE-SCOPE.md), with the full text in [LICENSE](../LICENSE) and attribution in [NOTICE](../NOTICE). Official imported material is excluded from that grant. The authorization and declared authorship are available in the change conversation; no separate ownership assignment or third-party permission is inferred.

Official documents and their extracts retain their origin. No third-party redistribution permission was supplied in the source folder. Public distribution clearance remains **deferred**, with the repository maintainer responsible for identifying and reviewing applicable source terms before distribution. Neither an official-looking filename, public availability, source hashes nor planning approval establishes those rights. No new license is assigned to those files. Local import and validation do not constitute release or publication clearance.

## Inventory and transformations

[import-inventory.json](import-inventory.json) records every supplied file, its source SHA-256, target path and disposition. Original source bytes, extracted official text, XML examples and the supplied [source-manifest.csv](source-manifest.csv) are preserved. The manifest retains its original Portuguese column names and original paths as historical evidence; resolve them through the import inventory, not relative to the renamed directories. [target-integrity.json](target-integrity.json) records target paths and hashes of imported/adapted files, excluding itself to avoid self-reference.

Authored instructions, summaries, adapter guidance, script identifiers and command-line interfaces were adapted to English. Manual-section and authored directory names were translated; official titles and source filenames remain in the import inventory. Three accented target filenames use ASCII names to preserve identical paths across macOS and Linux. Official extracted text was not translated. OS metadata was excluded. The source folder was not modified.

The original manifest's 35 entries were checked against their source files before import. This establishes local consistency only. The historical checksum list and the local Manual PDF disagree on MD5; do not claim binary identity with the historical published Manual. Dates in authored summaries are snapshot assertions to check against their originals for each question; no current-law or production conformity determination was performed during this import.
