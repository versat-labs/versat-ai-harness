# Licensing review decision record

Initial packet status: pending. The recorded decision below supersedes the pending review fields. Reviewed PR head for this packet: `aba801b98363bd796a2b3f16056561d0c3732c96`. The draft PR exposes the bundled copies in a public repository. The intended operational use is internal to Versat.

Review the [source and legal basis](README.md), the [per-file evidence](item-review.csv) and the [exact proposed notice](attribution-notice-draft.md). [Packet checksums](SHA256SUMS) identify the submitted evidence and notice text.

Record the following when the review takes place:

| Field | Reviewer entry |
| --- | --- |
| Decision (approve, approve with conditions, or defer) | Pending |
| Reviewer name and licensing review capacity | Pending |
| Accountable owner and distribution boundary accepted | Pending |
| Date and durable approval reference | Pending |
| Notice SHA-256 and reviewed packet revision | Pending |
| Files covered and exceptions, by inventory path | Pending |
| Conditions and implementation owner | Pending |

The review should decide whether article 38 and Annex II apply to the 33 originals and their 40 derivatives, including archive members and any embedded material with separate rights. Record any excluded files or conditions explicitly by inventory path, and account for both the public PR exposure and internal use. Confirm the proposed wording, preservation of original notices, and how per-source last-update dates will accompany the distributed copies where known.

After approval, record the decision against the exact notice and scope, apply the accepted notice and date records in the package, and reassess CHECK-002 before closing FIND-001. Record approval of the review and implementation of its conditions separately.

## Recorded decision

On 2026-11-18, the requesting developer, acting as the scope approver in this change conversation, stated: “Aprovo o escopo de redistribuição e a minuta de atribuição.” The same message authorized recording the decision, applying the notice, revalidating, resolving FIND-001 on success and publishing the update to the draft branch.

- Decision: approve the exact reviewed corpus and draft notice in packet commit `e4d9e7ba1a4ad43b055968bd714cb86c87bffbc7`. No separate DNIT or outside counsel sign-off was represented.
- Boundary: the identified 33 originals and 40 derivatives in the public PR #42 branch, with Versat internal operational use. The local checksum manifest and Apache-licensed authored materials retain their separate classifications. The decision does not extend to new documents, independent third-party rights, or downstream release.
- Reviewed draft SHA-256: `ff42ee5c4e37b87f7aa177d2a0001be3b3f3594c331bb6fee24c9c16c69d9952`. [Original packet checksums](reviewed-packet-e4d9e7b.sha256) refer to the snapshot before recording this decision.
- Applied notice SHA-256: `519eb40e21e7808bff790f4b3ce0dd303ff14edf959b72af2b92c2b2df632ac5`. The installed notice is the exact text below the draft separator, excluding the review-only header.
- Implementation: the skill carries the accepted notice and a per-file attribution table. All 33 original URLs supplied HTTP Last-Modified timestamps. Derivatives cite their parent's timestamp and official link. These timestamps describe downloads as published by DNIT, not the regulatory effective dates. Existing official file bytes and source notices are preserved.
