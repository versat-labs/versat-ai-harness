---
sdd_version: 3
change: payment-validation-tests
requirements:
  - id: REQ-001
    statement: Maintained tests verify rejection of empty keys and nonpositive amounts without recording a charge.
    acceptance:
      - Given a set containing an unrelated key, charging the empty string with amount 1 raises ValueError and leaves that set unchanged.
      - Given an unseen nonempty key, charging amount 0 raises ValueError and leaves the recorded key set unchanged.
      - Given an unseen nonempty key, charging amount -1 raises ValueError and leaves the recorded key set unchanged.
      - After rejecting amount 0 or -1 for an unseen key, a subsequent charge for the same key with amount 1 returns True and records the key exactly once.
  - id: REQ-002
    statement: Maintained tests preserve successful positive charges for previously unseen nonempty keys.
    acceptance:
      - Given an empty recorded key set, charging a nonempty key with amount 1 returns True and adds that key.
      - Given an existing recorded key, charging a different nonempty key with amount 1 returns True and retains both keys.
  - id: REQ-003
    statement: Maintained tests preserve at-most-once charging for each valid key without changing recorded state on duplicates.
    acceptance:
      - After a successful charge for a key, a repeated charge for that same key with a positive amount returns False and leaves the recorded key set unchanged.
      - Further repeated positive charges for the same recorded key return False, including a changed positive amount, while an unrelated recorded key remains present.
---

# Requirements

## Actors and context

A developer maintains the synthetic payment unit suite; the caller invokes `charge(seen, key, amount)` with an in-memory set. The source contract is [the existing payment specification](../../product/payment.md), supported by inspection of `src/payment.py` and the maintained tests. These documents do not authorize a real payment.

## Functional requirements

REQ-001 covers invalid input and state preservation. REQ-002 preserves successful charges. REQ-003 preserves duplicate prevention by key, independent of the positive amount supplied on a repeat.

## Non-functional requirements

Scenarios must be deterministic, use synthetic data, assert observable results and state, and remain part of the maintained required unit suite. Existing adequate coverage should be reused. A passing structural planning check is not evidence that these behavioral scenarios executed successfully.

## Acceptance scenarios

The ordered acceptance arrays above are the reviewable scenarios for this revision. Their positions will be used for Design coverage after Gate 1 approval. Current test inspection identifies existing success, duplicate, zero-amount and empty-key tests; negative amounts, retry after rejection and explicit state-preservation assertions remain coverage work.

## Constraints and assumptions

This is a test-coverage change preserving existing behavior. Empty means an empty string. Representative amounts are integer 0, -1 and positive values. Exception type and set-state observations reflect existing implementation; exact exception wording is not part of the contract. Persistent storage, concurrency, invalid Python types, whitespace normalization and numerical precision are outside scope. There are no material unresolved decisions for this bounded stage.
