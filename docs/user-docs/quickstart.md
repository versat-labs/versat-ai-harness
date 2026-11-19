# Quickstart

[English](quickstart.md) | [Português](quickstart.pt.md) | [Español](quickstart.es.md)

For a developer with authorized repository access planning a first change, including an external contributor once access and applicable terms are available. You need repository access, a prepared local project and the exact Harness provider with versat-sdd available. Complete [workspace setup](guides/workspace-setup.md).

## Plan one small change

Use a disposable prepared project for this example. In a real project, describe the actual user story and link its real issue. Send:

```text
Use $versat-sdd to plan change welcome-message: add a short, accessible welcome message to the existing home page. Show it on page load, using the project’s existing language convention. Create Proposal and Requirements only; do not implement. Stop for Gate 1 review.
```

## Recognize the result

Expect specs/changes/welcome-message/proposal.md and requirements.md, written in English, with the need, scope and observable acceptance scenarios. Codex presents their shared revision for approval. Read both files and ask for corrections or approve the presented revision. Design and Tasks come later, after their respective review gates; implementation requires an explicit request after Tasks review.

## If preparation is missing

If the provider or repository cannot be read, return to setup and resolve access/version before continuing. If the example project has no home page, supply an existing screen or choose an equivalent small behavior; do not invent implemented behavior. Missing context should become a focused question, not an invented approval.

## Continue

[SDD + Codex](guides/sdd-with-codex.md) · [GitHub](guides/github-delivery.md) · [Validation](guides/validation-and-evaluations.md) · [Publish user documentation and feature pages](guides/publish-product-documentation.md)

[Full SDD developer reference (English)](../../sdd/README.md)
