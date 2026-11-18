---
sdd_version: 3
change: payment-validation-tests
status: proposed
owner: Synthetic evaluator
summary: Strengthen payment validation and duplicate-prevention tests against the existing product contract.
risk: medium
impact:
  state: assessed
  summary: Preserve the existing payment contract while closing meaningful error, boundary and state-invariant coverage gaps in the maintained unit suite.
  items:
    - current_contract:
        path: specs/product/payment.md
        locator: Payment requires a nonempty key and positive amount.
        digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
      effect: preserve
      targets: [REQ-001, REQ-002, REQ-003]
      reason: The current living specification remains authoritative; tests must retain valid-charge, invalid-input and at-most-once behavior.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Proposal

## Context and problem

The synthetic `payment-fixture` project uses Harness 0.4.0 and the exact development snapshot selected in `.versat/standards.lock`. Applicable Standards were resolved from that provider's `standards/index.yaml` for software, finance, Python and medium criticality.

The existing [product specification](../../product/payment.md) requires a nonempty key, a positive amount and at most one charge per key. `src/payment.py` rejects an empty key or a nonpositive amount with `ValueError`, returns `False` for an already-seen valid key, and adds a valid new key before returning `True`.

Inspection of `tests/test_payment.py` finds coverage for a new charge, one duplicate, zero amount and an empty string key. It does not explicitly assert negative-amount rejection or preservation of the recorded key set after rejected input and duplicates. No active or archived change dossiers exist, so no historical requirement origin is claimed.

## Expected outcome

The maintained payment unit suite expresses observable success, error, boundary and duplicate-prevention behavior from the existing contract, with assertions that invalid attempts do not consume a key and duplicate attempts do not modify recorded charges.

## Scope

- Reuse adequate existing tests and add only missing assertions or scenarios for empty keys, zero and negative amounts, valid positive amounts and duplicate prevention.
- Preserve the existing payment behavior and required unit suite declared in `.versat/validation.yaml`.
- Keep this stage limited to Proposal and Requirements. Test implementation and execution evidence belong to later authorized phases.

## Out of scope

Changes to payment behavior, new payment integrations, persistent or distributed idempotency, concurrency guarantees, key normalization, additional input types, currency arithmetic and remote publication are outside this change.

## Work tracking

No Story or issue is associated with this synthetic scenario. The consumer has no `.git` directory; no branch or remote review state is claimed. The stable SDD ID is `payment-validation-tests`.

## Impact and risks

The impact item preserves the living contract and binds its current file digest. Existing success and duplicate tests must remain in the maintained unit suite. This is a test-coverage change with financial-domain relevance; avoiding duplicate charges and accidental state mutation are the main invariants. Synthetic keys and numeric amounts are sufficient; production data and real transactions are unnecessary.

The current implementation supplies the rejection exception and in-memory set behavior, while the product specification supplies the validity and at-most-once contract. The requirements make these existing observations explicit for review. This scope does not claim production payment-system assurance.

## Current contract baseline

The living specification is authoritative and remains unchanged. The inspected implementation validates input before looking up a key, never adds a rejected key, and leaves the set unchanged on duplicate submissions. For this change, an empty key means the empty string, and nonpositive boundaries are represented by zero and a negative integer; other input types and whitespace normalization are unspecified and outside scope.

## Proposal acceptance criterion

Proposal and Requirements describe a bounded preservation of the existing contract, identify observable scenarios and current gaps, resolve impact, and are presented together for Gate 1 review. No human approval or test success is inferred from structural validation.

## Planning review

Gate 1: Proposal/Requirements revision 1 is awaiting approval. No approval has been received. Approval of this revision unlocks Design only.
