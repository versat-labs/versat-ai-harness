---
sdd_version: 3
change: retire-branch-administration-ruleset
tasks:
  - id: TASK-001
    description: Retire the universal branch target in the policy, schema and affected guidance.
    requirements: [REQ-001]
    status: completed
  - id: TASK-002
    description: Review bootstrap output and trace the revised baseline through audit and maintenance.
    requirements: [REQ-001]
    status: completed
  - id: TASK-003
    description: Identify matching repository rules and capture independent main and tag protections.
    requirements: [REQ-002]
    status: completed
  - id: TASK-004
    description: Remove each confirmed rule and record the verified outcome per repository.
    requirements: [REQ-002]
    status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 31f9e0df4f220d67d1c44395b3c2d37d36797d40db58418802b229f7339c0307
    design: c1213a62ef87a6888872a0f4bf4be4b1895ecfb5016c818e34cb8e2134135220
  approval:
    source: Developer reply in this Codex chat approving Tasks R1 and authorizing implementation.
    quote: "Aprovo as Tasks R1 e autorizo a implementação. Retire a regra de todos os repositórios onde ela foi confirmada, mantendo o PR obrigatório na main e sem executar testes."
    revision: 1
    digest: 5f7345f415c2940e4f156e915821f1c59e474f65d8dfccbc69c0df469a98cd89
validation:
  plan_digest: 5f7345f415c2940e4f156e915821f1c59e474f65d8dfccbc69c0df469a98cd89
  results:
    - check: CHECK-001
      result: pass
      revision: "Working tree based on 577512598afe2f9a296f3b7a92acff9f40b961f2 with policy 2.0.0"
      evidence: docs/validation/retire-branch-administration-ruleset/source-review.md
      input_digest_before: 2bb02edb8cfefe36925d7b6203243bc57f90de60712046e9a48bcbf3cda8cc0e
      input_digest_after: 2bb02edb8cfefe36925d7b6203243bc57f90de60712046e9a48bcbf3cda8cc0e
      context: {execution: local, environment: Local provider renderer and source inspection, observed: true}
    - check: CHECK-002
      result: pass
      revision: "Working tree based on 577512598afe2f9a296f3b7a92acff9f40b961f2 with policy 2.0.0"
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      input_digest_before: 1967237e150699617b6583d62523ac9e674dcc127a7ecf2823c2f1fb34d263e2
      input_digest_after: 1967237e150699617b6583d62523ac9e674dcc127a7ecf2823c2f1fb34d263e2
      context: {execution: local, environment: Authenticated GitHub CLI and REST settings readback, observed: true}
  assessments:
    - obligation: {local: {requirement: REQ-001, scenario: 1}}
      result: pass
      checks: [CHECK-001]
      evidence: docs/validation/retire-branch-administration-ruleset/source-review.md
      explanation: Fresh staging contained main and tag payloads and omitted branch administration.
    - obligation: {local: {requirement: REQ-001, scenario: 2}}
      result: pass
      checks: [CHECK-001]
      evidence: docs/validation/retire-branch-administration-ruleset/source-review.md
      explanation: The schema accepted the tag-only policy and the evaluator iterates only the configured targets.
    - obligation: {local: {requirement: REQ-001, scenario: 3}}
      result: pass
      checks: [CHECK-001]
      evidence: docs/validation/retire-branch-administration-ruleset/source-review.md
      explanation: The shared guides and Git Standard describe the revised scope and all three Skills use that procedure.
    - obligation: {local: {requirement: REQ-002, scenario: 1}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: The two exact repository-owned rules and independent main controls were identified before deletion. Inaccessible inventory was recorded.
    - obligation: {local: {requirement: REQ-002, scenario: 2}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: Each post-delete inventory and settings comparison confirmed main and tag protection and preserved existing checks.
    - obligation: {local: {requirement: REQ-002, scenario: 3}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: A second list on each repository confirmed absence without another write.
    - obligation: {regression: {impact: 2, scenario: 1}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: Independent main settings retained PRs and all required approval flags.
    - obligation: {regression: {impact: 2, scenario: 2}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: Administrator enforcement or an empty bypass list covered main and its deletion and force-push protections.
    - obligation: {regression: {impact: 2, scenario: 3}}
      result: pass
      checks: [CHECK-002]
      evidence: docs/validation/retire-branch-administration-ruleset/github-readback.md
      explanation: Main was present on both targets and the required check configuration matched its pre-delete state.
  findings: []
closure: active
---

# Retire the administrator-only branch rule

The work follows the [approved design](design.md), [PR #48](https://github.com/versat-labs/versat-ai-harness/pull/48) and [issue #17](https://github.com/versat-labs/versat-ai-harness/issues/17).

- [x] TASK-001 — Set the public security policy to version 2.0.0 with `references.targets: [tag]` and constrain the schema to that value. Update the Git standard, architecture overview, security guide, template README and ADR index. Reconcile any explicit branch-rule instructions in bootstrap and the EN/PT/ES user guides. Complete when the source diff removes the branch mandate and still specifies reviewed PRs on main and administrator-only tag management.
- [x] TASK-002 — After TASK-001, stage output in a fresh directory with the ordinary bootstrap renderer. Inspect its manifest and files for CODEOWNERS, main protection, tag administration and secret settings. Confirm that the retired branch payload is absent. Trace the three retired branch controls through the evaluator and the lifecycle instructions. Complete CHECK-001 with the source review recorded at the path specified in Design.
- [x] TASK-003 — Refresh the paginated Versat inventory. Start with Harness rule `28023884` and organization metadata repository rule `27159054`. For each match, record its repository, ID and recoverable settings, and identify the independent protection enforcing reviewed PRs on main for all writers including administrators. Capture the review flags, force-push and deletion protections, required check settings and tag rules. Complete the inventory with a per-repository disposition, including inaccessible results or ambiguous matches. This read-only work can proceed alongside TASK-001.
- [x] TASK-004 — For each eligible target identified by TASK-003, refresh its settings immediately before deleting the matched rule ID. Re-read the inventory and compare the surviving protections before proceeding to the next target. On an uncertain response, inventory again before retrying. If a required protection disappears, follow the recovery procedure in Design and record the outcome. Complete CHECK-002 with a dated per-repository record showing the confirmed removals, the independent PR requirement on main, preserved tag rules and checks, and any unresolved inventory. A repeat read showing prior removal requires no write.

## Evidence and delivery

Use CHECK-001 and CHECK-002 to assess the six acceptance scenarios and three retained main-protection obligations in Design. Record the observed results, scoped input digests and outstanding gaps. The requester excluded test execution. Two existing suites refer to the retired asset or control IDs. Required CI still governs merge. Report its actual status separately from the source review and administrative readback.
