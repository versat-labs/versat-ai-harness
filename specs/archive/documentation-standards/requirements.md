---
sdd_version: 3
change: documentation-standards
requirements:
  - id: REQ-001
    statement: The Documentation Standard MUST define a discoverable layout for applicable consumer documentation.
    acceptance:
      - Given a new consumer with usable behavior, the README identifies its purpose, owner, lifecycle and validation entry point, and links to the first-use guide at docs/user-docs/quickstart.md. Detailed guides belong under docs/user-docs/guides/ when a workflow warrants one.
      - Given a consumer's applicable technical and product surfaces, the standard places architecture in docs/architecture/overview.md and new ADRs in docs/architecture/decisions/, and identifies docs/runbooks/, docs/integrations/, docs/api/ and docs/product/overview.md. The product overview for readers links to maintained material as access allows. Bootstrap retains the canonical product discovery record at specs/product/overview.md and shared base composition.
      - Given an empty scaffold or a legacy consumer with working documentation, applicable content can be introduced or adopted without empty placeholders, broken entry points, automatic path moves, or changes to the consumer's pinned Harness version.
  - id: REQ-002
    statement: SDD MUST guide developers through documenting the purpose and use of changed behavior and verifying the result.
    acceptance:
      - Given a feature affecting readers, planning identifies the affected audiences, their goal, the reason for the feature and the living material to add or update. A guide explains when the feature is useful, prerequisites, a representative workflow, the expected result and relevant limits or recovery. Technical material explains relevant rationale, contracts and operational consequences.
      - Given approved work affecting documented usage, implementation updates the affected documents alongside the feature and validation compares the instructions and expected results with observed behavior. Existing checks may supply that evidence. Unavailable verification is reported explicitly.
      - Given an internal change with no effect on documented behavior and no new documentation obligation, planning records applicability without requiring a new guide or a separate documentation task.
  - id: REQ-003
    statement: Consumer user documentation MUST apply the existing Language Standard consistently.
    acceptance:
      - Given a new or changed user-facing guide or quickstart, English is canonical and the corresponding .pt.md and .es.md files are maintained in the same change. Readers can reach the language variants and examples retain the same meaning and results.
      - Given an internal technical reference or a localized guide linking to it, reviewers can identify which language rules apply and follow a working reference. Existing language policy governs exceptions.
  - id: REQ-004
    statement: The Harness MUST explain how a product team publishes maintained user docs and marketing pages for its features.
    acceptance:
      - Given a product with publishable features, the guidance explains how to select the publication destination and owner, map each feature to a discoverable marketing page and user guide where applicable, and review, publish, verify and update the content and its required language variants from maintained sources.
      - Given private content, a restricted product or an unavailable publishing destination, the guidance distinguishes audience and access decisions, requires appropriate review before exposure and describes how to record the pending or inapplicable publication state.
  - id: REQ-005
    statement: The design MUST evaluate a GitHub Actions report for documentation compliance visible from the PR.
    acceptance:
      - Given a PR that changes applicable documentation, the evaluation identifies a feasible reporting surface and shows which rules can report pass, fail or not applicable with actionable paths or reasons, and which rules require human review or unavailable evidence.
      - Given the evaluation, Design presents a recommendation, its rationale and its effect on permissions and existing required checks. An implemented report, if selected in Design, shows both satisfied and unmet mechanical rules for representative PR inputs and distinguishes human review from automated results.
---

# Requirements

The Versat SDD developer needs guidance for documenting a feature as it is planned and built. A product user should be able to understand why the feature exists, decide when to use it and complete a representative workflow without training or consulting the Product Owner. Maintainers own the structure, localization and publication process. Reviewers assess both observable behavior and the quality of the explanation.

The consumer layout is a default for new applicable material. Existing equivalent documents may be retained during governed adoption when navigation and required content are intact. A consumer product overview for readers and the bootstrap discovery record serve distinct audiences. Link maintained sources and avoid reproducing discovery content.

The publication requirement delivers a usable process for product teams. A hosting choice, production deployment, and product-by-product backfill are outside this change. The PR reporting evaluation concerns documentation. Cross-surface translation automation for product interfaces is tracked in [Issue #26](https://github.com/versat-labs/versat-ai-harness/issues/26).
