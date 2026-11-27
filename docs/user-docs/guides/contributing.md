# Contribute with clear provenance

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

This is the maintained contribution route for the Harness candidate and for contributors selecting a destination project. Harness public availability and Apache adoption are pending. Until actually available, use only repositories and terms for which you have authorization; no public fork or installation is promised by this guide.

## Prepare and contribute

1. Choose the actual target repository and read its README, AGENTS and contribution instructions. Its own guidance takes precedence over organization defaults. Other products retain their independent terms and routes.
2. Select an existing issue or an available bug, feature or maintenance form. When opening or substantively revising an issue, write its title and description in English, including form responses, the expected result and any reproduction steps. Teammates may discuss the work in Spanish in comments. If the discussion changes the scope or acceptance criteria, update the English description. Use the actual issue or Story number. See the [Language Standard](../../../standards/core/language.md#github-issues).
3. Identify original/third-party material, sources, versions, applicable grants and notices. Missing rights prevents acceptance. Read [candidate licensing](licensing.md); a tool's license does not determine unrelated destination-project terms.
4. Follow [setup](workspace-setup.md). For a Harness checkout, use Python 3.11+, install `requirements-validation.txt` in a virtual environment and run `./scripts/validate/run.sh --quality-base origin/main` from the root. Use the target project's own checks elsewhere.
5. When the repository and applicable permissions permit it, use an authorized fork or work branch and the [Git convention](../../../standards/core/git.md). Public read/fork access does not grant upstream write, merge or release authority.
6. For material changes, follow the [three SDD planning gates](sdd-with-codex.md); explicitly request implementation after Tasks approval. Include living documentation and meaningful checks. Follow [delivery](github-delivery.md) for archival, PR review and final checks, with actual remote-operation authority.

Expected result: a reviewable contribution with genuine issue/provenance links and observed checks. Describe unavailable verification; a local pass does not prove effective branch protections or acceptance.

## Candidate contribution terms

If and when this Apache candidate is adopted, section 5 of the exact [Apache text](../../licensing/candidates/apache-2.0/LICENSE.txt) governs contributions intentionally submitted for inclusion unless explicitly stated otherwise, subject to the license's definitions and any separate agreement. This guide introduces no additional CLA, DCO or IP assignment. Until adoption, use the actual terms applicable to the repository/version and obtain clarification when unavailable. Do not treat the earlier proprietary text approval or these draft instructions as an effective grant.

## Review and recovery

The actual maintainer must review scope, provenance and required checks. CODEOWNERS identifies technical contacts, not proof of legal qualification or enforced protection. Missing rights or required review prevents acceptance. Failed checks need correction and fresh evidence; changed scope reopens the affected SDD gate. If access is unavailable, use the target's existing public participation route without the Harness when appropriate, or ask its visible maintainer for access instructions without sharing confidential information.

Keep vulnerability details out of public issues; use [security reporting](security-reporting.md). Canonical policy: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
