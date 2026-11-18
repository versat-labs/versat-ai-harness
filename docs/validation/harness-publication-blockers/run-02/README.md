# Authorized restricted inventory — run 02

The user explicitly authorized the inventory described in the current handoff: “Sim, autorizo o inventário restrito no escopo do handoff, sem ampliar permissões, apagar histórico ou publicar. Prossiga.” Collection finished on 2026-11-14. This run records actual collection and its limits, not permission to publish or a claim that the successor is complete.

## Observed inventory

| Surface | Observation |
|---|---|
| Current source | 1,616 local file records at collection time, including uncommitted planning and safe evidence. |
| Reachable history | 1,244 remote and 1,246 local blobs read; remote and local-only scope distinguished. Deleted-path history retained. |
| References | Current branches, tags and 19 PR heads match the restricted forensic copy; beginning/end branch/tag observations remained stable. |
| CI logs | All 58 enumerated run archives obtained; 115 entries read. No archive content was executed or extracted into the Harness. |
| Issues/PRs/reviews | All acquired paginated bodies retained privately, including submitted reviews for 19 PRs; 56 body fields and 42 link occurrences inspected. |
| Currently absent/disabled surfaces | Successful release and artifact listings were empty; wiki/discussions/Pages were disabled. No LFS pointers or binary blobs occurred in the inspected reachable sets. These observations do not cover inaccessible deleted content or unseen external copies. |
| Remaining payload gaps | Repository-scoped package query lacked required scopes; two listed cache payloads and two external integration link occurrences remain unreviewed. |
| Preserved originals | The 96 predecessor manifest entries remain intact; 97 files were copied byte-for-byte into new restricted local custody. |
| Integrity and access | The new manifest binds 320 files, verified after collection. New local files are owner-readable with no group/other access. Actual human acceptance and durable remote custody remain unverified. |

The private review queue has 82 location/type entries, including duplicated indicators across snapshots. They are candidates for actual classification, **not 82 confirmed sensitive findings**. No rights grant, confidentiality waiver, treatment or specialist review is inferred from a literal scan.

## Evidence and boundaries

[Sanitized inventory summary](inventory-summary.json) contains opaque record HPB-PRIVATE-01, revision 1, two hashes, counts, category observations and limits. Raw payloads, locations, URLs, logs, the forensic Git copy and reviewer queue remain exclusively in the selected restricted system. Collector sources were preserved there separately after execution; the frozen inventory was not rewritten.

The collection used read-only repository/API queries and forensic Git fetches. Package queries were repository-scoped; unrelated organization packages were not enumerated. No credential scope was expanded. No unsupported cache extraction, workflow execution, external integration traversal, deletion, sharing change, remote commit/push/PR or publication occurred.

Method references: [GitHub repository package connections](https://docs.github.com/en/graphql/reference/repos) and [GitHub cache REST endpoints](https://docs.github.com/en/rest/actions/cache), consulted 2026-11-14. Available API inventory/management operations did not establish a supported cache-payload read route. Failed reads remain unavailable, not absent.

## Validation and freshness

[Prior ledger](prior-ledger.json) and [prior input manifest](prior-review-inputs.json) preserve the previous state. Updating included review inputs invalidates the old broad-input passes for the final candidate. They were not rehashed or presented as current success. TASK-008's earlier private success remains recorded for its tested snapshot; its current status awaits final-source revalidation after remaining inputs stabilize. No native scenario was repeated by this inventory authorization.

The current check reports record bounded review only, plus the complete preparation suite under CHECK-009. Missing rights/access/enforcement/receipt and incomplete semantic acceptance remain open. Strategy consumer validation separately passed with its exact 0.3.0 context, nine Standards and 13 verified snapshots; it is not remote delivery or human review evidence.

## Next permitted work

Use the [current handoff](../../../handoffs/harness-publication-blockers/README.md) and the private review queue. Obtain inspectable package/cache/integration evidence from authorized custodians using existing access, accountable rights/security dispositions, actual reviewer access/custody evidence, and supported private protection capability. Remote control/reporting/delivery operations retain their separate scoped authority. No new approval of the unchanged SDD plan is requested by this inventory.
