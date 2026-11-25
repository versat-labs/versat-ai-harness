# SIFEN compliance checklist

Use for an authorized audit. Mark an inapplicable layer with a reason; do not silently omit it. This is a translated snapshot aid, not a current-law determination. Verify conditions against the sources before applying them.

## Context and effective dates

- [ ] Identify Test/Production, target date, DE/DTE type, actor, operation, currency, taxes and event.
- [ ] Apply Manual v150 and every Note effective for that environment/date.
- [ ] Verify official material after 2026-03-09 when a current conclusion is required; report unavailable verification.

## XML and schema

- [ ] Check XML 1.0 well-formedness, encoding, namespace and schema, without inappropriate DE tag prefixes.
- [ ] Preserve exact element case; apply rules on comments, `annotation`, `documentation`, inter-tag tabs/newlines/spaces and value-boundary spaces.
- [ ] Do not emit empty optional tags or blank/zero padding unless expressly allowed.
- [ ] Check sequence, parent, type, length, decimal places and occurrence against the official XSD; packaged examples do not replace it.

## Identification and CDC

- [ ] Generate a 44-digit CDC consistent with the DE; recalculate check digit and security code.
- [ ] Validate timbrado, effective period, establishment, issuance point, numbering and series.
- [ ] Enforce CDC uniqueness and avoid resubmission before a definitive response.

## Issuer, recipient and operation

- [ ] Validate RUC/check digit, nature, taxpayer type and issuer registration data.
- [ ] Cross-check `D201`, `D202`, `D208`, `D210`, country, operation and document.
- [ ] Apply the active Gs. 7.000.000 threshold in `D208c/1321` and `D011=13` exception.
- [ ] Apply NT 20 B2G/OEE and NT 26 DNCP relaxations.
- [ ] Validate affected obligations `D030-D032`, catalog and uniqueness.
- [ ] Require PYG for Autofactura under `D022/1213`.

## Items, taxes and totals

- [ ] Check item code/description, unit, quantity, price and sector groups.
- [ ] Apply `E701`/`E708` under NT 9 and `E711` quantity under NT 23.
- [ ] Recalculate item totals and all subtotals; apply NT 1 discounts/advances (`EA004`, `F009`, `F011-F014`, `F033-F035`).
- [ ] Apply NT 13 partial taxable/exempt base and subtotals (`E735`, `E737`, `F002`, `F004`, `F005`).
- [ ] Validate rate, tax treatment, IVA, ISC, rounding/tolerance and currency conversion; apply NT 8 `F023` by document/currency.

## Associated documents and sectors

- [ ] Validate associated-document type, CDC, issuer/recipient and timbrado.
- [ ] Apply `H004g/H004h/H004i`, `H018/H018a` and merged RUC where relevant.
- [ ] Require associated documents for `C002=4,5,6,8` under NT 23.
- [ ] Apply insurance, energy, traceability/SENAVE, transport, public procurement and DNCP rules only where applicable.

## Signature and certificate

- [ ] Sign the complete document using an enveloped XML signature and match `Reference URI` to `Id`.
- [ ] Use canonicalization, RSA-SHA-256/384/512 and SHA-256/384/512 digest accepted by NT 16.
- [ ] Include qualified X509.v3 certificate and validate the chain to PCSC/MIC.
- [ ] Validate validity, revocation, CRL, `KeyUsage`, `ExtendedKeyUsage clientAuth` and certificate RUC; detect post-signature modifications.

## Web Services and batches

- [ ] Use SOAP 1.2, TLS 1.2, mutual authentication and the environment/service endpoint and namespace.
- [ ] Limit batches to 50 DE, same RUC/type, all signed, input at most 1000 KB.
- [ ] Compress `rLoteDE`, Base64-encode and handle `0300/0301`.
- [ ] Poll after approximately ten minutes, intervals >=10 minutes; handle `0360/0361/0362/0364`.
- [ ] Do not resend a processing CDC; handle 10–60-minute blocks and query individual CDC after 48 hours.
- [ ] Handle `0420/0422` and validate returned XML in `xContenDE`.

## Events

- [ ] Validate actor, signature, CDC, state, period and specific cancellation, invalidation, transport and recipient formats/validations.
- [ ] Do not apply `GEC002c/4004` after NT 25.
- [ ] For recipients, count from issuance (DE) or approval (DTE); apply 45-day and corrective 15-day windows under NT 19.
- [ ] For Nomination, apply NT 14, NT 15 and NT 27's `GENFE010/GENFE011` list.

## KuDE and QR

- [ ] Represent required fields legibly for the DTE type; generate QR with the applicable order, values, hash/CSC and environment URL.
- [ ] Set `dTotIVA=0` in QR when the DE has no IVA.
- [ ] Validate CSC at issuance; consider error `2501` when not valid.
- [ ] Visually inspect PDF/receipt, scannable QR and corresponding query.

## Final report

- [ ] Separate structural, signature, business and operational errors from recommendations.
- [ ] Give ID, code, severity, condition and source for each finding; identify rules superseded or eliminated by later Notes.
- [ ] Declare environment, schema, missing-source and official-update verification limitations.
