---
sdd_version: 3
change: retire-branch-administration-ruleset
requirements: [REQ-001, REQ-002]
adrs: [ADR-0018, docs/decisions/0020-retire-universal-branch-administration.md]
validation:
  - id: CHECK-001
    description: Review the indexed policy, generated asset contract, readiness controls and living guidance.
    requirements: [REQ-001]
    required: true
    method:
      kind: review
      reason: The requested scope permits source and documentation review without executing tests.
      procedure: Trace references.targets from the index and schema through assets() and the evaluator. In a fresh staging directory inspect the ordinary bootstrap output and its manifest. Expect tag administration, independent main protection, CODEOWNERS and secret settings. Check that the branch administration payload and its three readiness obligations are omitted. Cross-read the affected instructions and verify the required PR rule on main.
    inputs:
      include: [standards, schemas/public-repository-security.schema.yaml, scripts/bootstrap/public_security.py, validators/security, skills/project-bootstrap, skills/project-audit, skills/project-maintenance, project-templates/artifacts/github-public-security, docs/guides/public-repository-security.md, docs/user-docs/guides, docs/architecture/overview.md, docs/decisions/0020-retire-universal-branch-administration.md]
      exclude: []
    outputs: [docs/validation/retire-branch-administration-ruleset/source-review.md]
    execution: local
  - id: CHECK-002
    description: Compare repository settings before and after each authorized removal.
    requirements: [REQ-002]
    required: true
    method:
      kind: manual
      reason: Authenticated administrative readback establishes the actual GitHub state for each repository.
      procedure: Follow the per-repository migration below. Record inventory, the exact rule and independent protections before removal. Read the list and surviving settings again afterward. Confirm that only the matched rule disappeared and that a subsequent inventory requires no write. Record inaccessible targets separately.
    inputs:
      include: [standards/core/public-repository-security.yaml, standards/core/git.md, docs/guides/public-repository-security.md]
      exclude: []
    outputs: [docs/validation/retire-branch-administration-ruleset/github-readback.md]
    execution: local
coverage:
  - {scenario: {requirement: REQ-001, scenario: 1}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-001, scenario: 2}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-001, scenario: 3}, applicability: required, checks: [CHECK-001]}
  - {scenario: {requirement: REQ-002, scenario: 1}, applicability: required, checks: [CHECK-002]}
  - {scenario: {requirement: REQ-002, scenario: 2}, applicability: required, checks: [CHECK-002]}
  - {scenario: {requirement: REQ-002, scenario: 3}, applicability: required, checks: [CHECK-002]}
regression:
  - {obligation: {impact: 2, scenario: 1}, checks: [CHECK-002], rationale: Compare the independent PR requirement and all mandatory review settings.}
  - {obligation: {impact: 2, scenario: 2}, checks: [CHECK-002], rationale: Confirm administrator enforcement or empty bypass lists and effective force-push and deletion protection on main.}
  - {obligation: {impact: 2, scenario: 3}, checks: [CHECK-002], rationale: Confirm main exists and compare each repository's actual required checks and their bindings.}
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 31f9e0df4f220d67d1c44395b3c2d37d36797d40db58418802b229f7339c0307
  approval:
    source: Developer reply in this Codex chat approving Design R1 and ADR-0020 and requesting Tasks.
    quote: "Aprovo o Design R1 e o ADR-0020. Avance para as Tasks, mantendo o PR obrigatório na main e sem executar testes."
    revision: 1
    digest: c1213a62ef87a6888872a0f4bf4be4b1895ecfb5016c818e34cb8e2134135220
---

# Retire the all-branches ruleset

## Source change

In Harness source 0.4.0, `standards/index.yaml` resolves the typed policy. Set `references.targets` to `[tag]` and constrain that array to the same value in `schemas/public-repository-security.schema.yaml`. Use policy version 2.0.0 because the reported public control set loses three previously mandatory controls. Package release and consumer pin adoption follow their existing processes.

Both the renderer and evaluator iterate over the configured targets. The renderer still builds the main protection payload independently. The collector must continue reading branch rulesets, including inherited rules, to establish effective main protection. The current bootstrap Skill delegates to the shared guide. Audit and maintenance use the same provider. These components can consume the revised policy without a new code path.

Update the Git Standard, architecture overview, security guide and security-template README where they describe universal branch administration. Add the successor ADR to the decision index on implementation. Review the affected EN/PT/ES guides for instructions that explicitly require the retired rule. Use a fresh staging directory for the new provider so a stale generated file from an older run cannot be mistakenly applied. Preserve historical evidence and consumer-owned staging files.

## Per-repository migration

| Repository | Candidate | Independent source requiring a PR on main |
| --- | --- | --- |
| `versat-labs/versat-ai-harness` | `28023884` | Classic main protection, including administrator enforcement and the required `structural-validation` check |
| `versat-labs/.github` | `27159054` | Active main ruleset `27159053`. Inspect its full rules and bypass list and any additional effective protections. |

1. Refresh the visible Versat inventory with authenticated, paginated reads. For each candidate, capture repository identity, default branch, rule ID, source, enforcement, conditions, bypass actors and rules. Match the repository-owned active branch target covering `~ALL` without exclusions, restricting only creation, update and deletion, with only repository administrators granted bypass. Treat names as descriptive. Preserve the writable fields of each matching rule for recovery. Record unavailable access or ambiguous matches.
2. Before deleting, inspect main's classic protection, effective rules and applicable ruleset details. Independently of the candidate, confirm that main requires a PR and at least one CODEOWNER approval, dismisses stale approvals and requires approval of the latest reviewable push. Verify that these settings cover administrators, force push and deletion are blocked, and record the existing required check contexts, producer identities and strictness where present. Capture the separate tag settings. A missing independent protection or incomplete observation defers only that target.
3. Re-read the candidate and surviving controls immediately before the write. If they still match, delete only that repository's exact rule ID. Re-list the rules and re-read the independent controls. Compare settings and report the repository, time, ID and outcome. A successful fresh inventory showing absence is sufficient on retry. A lone 404 or a timeout after deletion requires another read before considering a retry.
4. If the comparison shows a lost required protection, pause further removals. Use the captured configuration to restore the previous branch restriction if its restoration is needed and no equivalent now exists. GitHub assigns the recreated rule a new ID. Re-read its settings and independently verify main again. A restored branch restriction alone cannot establish mandatory PRs. Record any remaining drift for its repository administrator. Keep credentials outside evidence.

The planning inventory found two matching rules, four empty lists and 21 plan-related access failures. Report confirmed removals and unresolved targets separately. Settings readback establishes configuration only. The prior fork review observation and the scope of native approvals are recorded in the [approved proposal](proposal.md).

## Alternatives and delivery

Excluding main from the all-branches rule would retain the administrator-only restriction on ordinary branches, contrary to REQ-001. Removing only the live rules would leave bootstrap generating a replacement and readiness checking for it. Reusing the existing policy-driven paths addresses both.

The two planned checks are a source review with ordinary staging output and live administrative readback. Test execution is outside the request. Existing assertions in `tests/validators/test_security_contract.py` open the retired file, and `tests/validators/test_security_policy.py` looks up retired control IDs. Those assertions conflict with the new contract by inspection. Required CI remains a delivery dependency. A failing required check blocks merge and must be reported before delivery. The design introduces no CI bypass.
