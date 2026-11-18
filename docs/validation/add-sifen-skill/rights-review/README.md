# DNIT item-by-item rights review

Reviewed 2026-11-18 against PR #42 head `aba801b98363bd796a2b3f16056561d0c3732c96`. Intended consumption is internal to Versat. The branch carrying the copies is publicly accessible, so the actual hosting surface is public. Technical evidence review by Codex. Maintainer disposition remains **defer**, pending an observed licensing acceptance review and implementation of the notice on the distributed surface.

## Review packet

Start with the [decision record](review-decision.md) and [draft attribution notice](attribution-notice-draft.md). The [per-file inventory](item-review.csv) links each official item to its publication and the supporting verification records below. [Packet checksums](SHA256SUMS) identify the submitted versions.

## Primary basis

- [Law 5282/2014, art. 2 and 4](https://www.bacn.gov.py/leyes-paraguayas/3013/libre-acceso-ciudadano-a-la-) defines public information broadly, across formats, with a statutory secrecy or reservation exception, and provides free access.
- [Decree 4064/2015, art. 38 and Annex II](https://mitic.gov.py/eoj0cad9uplo/2023/11/DECRETO_4064_15_Reglamento_Ley_de_Acceso_a_la_Informacion_5282-2014.pdf) extends the Public Information Use License to public information without statutory reservation. The Annex addresses public information and open data owned by the Paraguayan State. Its permitted acts include copying, reproduction, distribution, public communication, adaptation and transformation. Conditions are attribution of the supplying public source and this license, stating last update when known, and avoiding presentation as an official or State-sponsored use. It disclaims liability of the supplying public source. Identify extracts as derived and preserve official originals.
- [Law 1328/98, arts. 8, 26, 32 and 44](https://www.bacn.gov.py/leyes-paraguayas/908/derecho-de-autor-y-derechos-conexos) separately excludes official legislative, administrative and judicial texts (with source attribution and fidelity) and mere facts from copyright protection. The official-text exclusion can support qualifying texts, but was not assumed for every guide, illustration, archive or schema. The personal-copy exception does not establish a general company-wide copying or distribution entitlement.
- The [e-Kuatia Technical Documentation portal](https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica) directly serves all 33 exact originals publicly. Its generic rights-reserved footer is not itself a demonstrated statutory confidentiality reservation. No e-Kuatia-specific permissive license or document-specific reservation was found in the inspected index. The [government open-data directory](https://www.datos.gov.py/portales-de-datos-abiertos) lists a DNIT Customs portal, which is separate from the basis relied on here.

## Inventory results

[item-review.csv](item-review.csv) accounts for all 88 source inventory entries. The exact DNIT URLs and digests are retained in [official-downloads.json](official-downloads.json). The [derivation checks](derivation-checks.json) record parent URLs, local hashes and page ranges for each extract and exact archive-member comparisons for each XML.

| Packaged material | Count | Evidence and applicability |
| --- | ---: | --- |
| Manual v150 and Technical Notes 1–27 | 28 | All match DNIT downloads byte for byte. DNIT presents these as the official electronic invoicing Manual and amendments. Strong evidence of state-published public information under art. 38. The archived historical MD5 for the Manual remains a different comparison and is not used to discredit the current exact DNIT match. |
| Testing guide, submission best practices and historical MD5 list | 3 | Each matches its distinct DNIT download byte for byte. Art. 38 is the candidate basis for the official copies, independent of whether the guides qualify as administrative texts under Law 1328/98. |
| XML and XSD archives | 2 | Both match the distinct DNIT RAR downloads byte for byte. Their software-oriented format does not itself exclude public information under Law 5282 Art. 2. State ownership and any independently protected embedded material remain part of the reviewed scope. |
| Archived XML/XSD payloads | 2 | Each local XML is byte-identical to its corresponding member extracted using bsdtar from the verified official RAR. Same candidate provenance and license as the parent payload. This review does not authorize reuse of any underlying marks or separately owned material. |
| Text extracts | 38 | Each is mapped to its exact verified parent PDF, including the 8 Manual extracts, 27 note extracts, 2 guide extracts and historical checksum extract. The comparison tested page markers/count and normalized token overlap for each page. Five Manual pages fell below 95% because of text segmentation in headings and diagrams. Unmatched examples were split or concatenated words. The result substantiates source mapping and is not a certification of extraction fidelity or of every embedded graphic. Annex II allows transformation of covered material. |
| Supplied checksum manifest | 1 | Local import metadata, distinct from the official checksum-list PDF. Separately classified in the CSV. Factual hashes and sizes are distinguishable from a redistribution license for the official PDFs. |

The tenet behind the candidate disposition is that these exact originals are official DNIT/SET e-Kuatia materials intentionally distributed by the government for software development, including documented public indexes and technical examples. This is persuasive provenance and coverage evidence. A public download match alone cannot establish State ownership of every independently sourced illustration, symbol or embedded input. An accountable licensing reviewer should accept the scope explicitly or identify exceptions before the packet is treated as cleared.

## Draft third-party notice for review

The [standalone draft](attribution-notice-draft.md) contains the candidate text for placement with the distributed corpus. Record accepted scope, conditions and the exact notice hash in the [decision record](review-decision.md).

## FIND-001 disposition

The statutory basis and item source evidence materially narrow FIND-001. The approved Design, Tasks and Licensing and Publication Standard also require an observed licensing acceptance review. None was supplied, and the draft notice has not been adopted in the distributed package. Keep CHECK-002 unverified and FIND-001 open. Maintainer follow-up: obtain a component-specific review of this evidence and notice, record reviewer capacity and decision, apply the accepted notice and dates, then reassess CHECK-002. The public branch exposure must be included in that review even though business use is internal.
