---
sdd_version: 3
change: retire-branch-administration-ruleset
status: proposed
owner: elviszoz
summary: Retire the administrator-only all-branches rule while keeping pull requests mandatory on main.
risk: medium
impact:
  state: assessed
  summary: Remove the branch portion of the public reference policy from bootstrap and readiness. Keep the independent main and tag controls.
  items:
    - source: {change: public-repository-security, requirement: REQ-004, scenarios: [1, 2], requirements_digest: f114240b614b60a3a283b2d8e78da5ed7d78edefd1db5d98484d5d87d09ae085}
      current_contract: {path: standards/core/public-repository-security.yaml, locator: 'targets: [branch, tag]', digest: 508997f206f827868a515f4dc8f692229e9c500d8960bba98e2bfdd755a1c504}
      effect: supersede
      targets: [REQ-001, REQ-002]
      reason: Drop universal branch administration across the lifecycle while continuing to reserve tag administration for administrators.
    - source: {change: public-repository-security, requirement: REQ-002, scenarios: [1, 2, 3], requirements_digest: f114240b614b60a3a283b2d8e78da5ed7d78edefd1db5d98484d5d87d09ae085}
      current_contract: {path: standards/core/git.md, locator: Public GitHub repository security, digest: 08f5e989ab50e6341eb1ddeeb380eb151252fbc1ef44e291515e7beda027dc06}
      effect: preserve
      targets: [REQ-002]
      reason: Keep GitHub's independent main protection and its existing review and check settings on each target.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply in this Codex chat approving Proposal and Requirements R1 and requesting Design.
    quote: "Aprovo a Proposta e os Requisitos R1. Avance para o Design, mantendo o PR obrigatório na main e sem executar testes."
    revision: 1
    digest: 31f9e0df4f220d67d1c44395b3c2d37d36797d40db58418802b229f7339c0307
---

# Retire the administrator-only branch rule

The all-branches update restriction makes an ordinary merge into main require an administrator bypass even after the PR meets GitHub's review and check requirements. The requested policy lets collaborators with write access merge a qualifying PR and manage ordinary unprotected branches. Main keeps its independent PR requirement.

## Work tracking

[Harness PR #48](https://github.com/versat-labs/versat-ai-harness/pull/48) introduced the policy. [Issue #17](https://github.com/versat-labs/versat-ai-harness/issues/17) records the original concern about mandatory PR approval. GitHub lists no closing issue for PR #48. Reference #17 for context without closing it. No Shortcut Story was supplied.

## Current contract and scope

The provider is the Harness source at `5775125`, version 0.4.0. The bootstrap Skill delegates to the shared guide and index-resolved policy. The policy currently lists both branch and tag targets, and its schema requires both. The renderer in `scripts/bootstrap/public_security.py` and readiness evaluator in `validators/security/policy.py` already iterate over that list. The minimal source change therefore includes the typed policy, its schema and directly affected living guidance. Edit the Skill only if its own instructions would still direct an operator to create the rule. Historical PRs, evidence and archived specifications retain their original meaning.

Existing security tests include expectations for the retired control in `tests/validators/test_security_policy.py` and the generated asset in the contract suite. The requester limited this work to configuration and guidance and waived test execution. Record any impact on required CI separately. This change grants no exception to the repository's required merge checks.

## Operational inventory

On 2026-11-27, GitHub listed 27 visible repositories across the two Versat organizations. Two had matching repository-owned rules. Four returned empty ruleset lists. For 21 the ruleset endpoint returned HTTP 403 citing plan availability. Those repositories have no verified inventory. Match effective scope, operations, bypass role and source repository because the rules have different names.

| Repository | Rule to remove | Independent main protection |
| --- | --- | --- |
| `versat-labs/versat-ai-harness` | [28023884](https://github.com/versat-labs/versat-ai-harness/rules/28023884) | Classic protection enforces reviewed PRs for administrators and requires `structural-validation`. |
| `versat-labs/.github` | [27159054](https://github.com/versat-labs/.github/rules/27159054) | [27159053](https://github.com/versat-labs/.github/rules/27159053) independently requires a PR on main and blocks force pushes and deletion. |

The separate, interrupted `maintainer-main-merge` change considered restricting mergers to designated maintainers and qualifying independent owner reviews. The requested policy permits the repository's ordinary write roles to merge. Leave the interrupted work in its own worktree. Its [fork PR #6](https://github.com/versat-labs/.github/pull/6) recorded an enabled merge action after the pushing CODEOWNER and a different writer approved, with the other CODEOWNER still pending. This proposal keeps GitHub's native review configuration. It makes no stronger guarantee about who supplied the latest approval.

## Acceptance and review

Review the two requirements together. Operational evidence should identify each removed rule and confirm that the independent PR protection remains active. No new test, trial PR, release, grant of access or organization-level rule is requested.
