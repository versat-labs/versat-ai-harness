# GitHub settings after retiring the all-branches rule

The operator refreshed the paginated inventory for the two Versat organizations on November 27, 2026. Of 27 visible repositories, two had a matching repository-owned active rule, four returned an empty ruleset list and 21 returned HTTP 403 citing plan availability. The latter group remains unverified. The complete per-repository inventory and raw settings snapshots were retained locally outside this public source tree.

| Repository | Removed rule | Pre-delete and post-delete observation (UTC) | Surviving controls |
| --- | --- | --- | --- |
| `versat-labs/versat-ai-harness` (1350076941) | 28023884, Versat administrators manage branches | 17:28:05 / 17:28:09 | Classic main protection including administrator enforcement. Required check `structural-validation`, app 15368, strict mode off. Tag rule 28023891. |
| `versat-labs/.github` (1434917496) | 27159054, Administrators only - branches | 17:28:21 / 17:28:26 | Active main ruleset 27159053, with an empty bypass list. No required status check appeared in the effective rules or classic protection. Tag rule 27159055. |

Both targets were active branch rulesets owned by the named repository. They matched all branches with no exclusions, restricted creation, update and deletion, and granted bypass only to repository administrator role 5. For recovery, each rule's writable fields were captured before deletion. Both had conditions `{"ref_name":{"include":["~ALL"],"exclude":[]}}`, rules `creation`, `update`, `deletion` without extra parameters, and bypass actor `{"actor_type":"RepositoryRole","actor_id":5,"bypass_mode":"always"}`.

Immediately before each deletion, fresh repository settings matched the initial observation. Each DELETE addressed only the listed ID. A fresh read afterward compared repository identity, default branch, classic protection, effective rules and the source, target, name, conditions, bypass actors, enforcement and rules of every surviving ruleset. The sole observed difference on each target was removal of the specified rule and its entries among the effective rules for main.

In both repositories main requires a PR, one approval, CODEOWNER review, dismissal of stale approvals and last-push approval. The settings apply to administrators. Force pushes and deletion of main are blocked. The separate active all-tags rules retain their administrator-only controls. The check binding on the Harness was identical before and after.

A second paginated inventory returned only 28023891 on the Harness and only 27159055 and 27159053 on the organization metadata repository. No further write was needed. The readback establishes settings at the observation time. No test PR, push, branch deletion or merge was performed.
