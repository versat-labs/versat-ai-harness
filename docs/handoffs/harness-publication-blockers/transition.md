# GitHub Free transition operation

Status: prepared procedure; **not authorized or executed**. Source: approved [Design R4](../../../specs/archive/harness-publication-blockers/design.md#ownership-and-protected-opening). Repository: `versat-labs/versat-ai-harness`, ID `1350076941`; branch `main`. Coordinator: @elviszoz. Preparation evidence and open prerequisites are in the [current handoff](README.md).

## Bounded deviation and actual participants

`HPB-FREE-TRANSITION-R2` permits only the reviewed sequence for this repository/main, named preparation/adoption PRs and a named attended session. It narrows timing under [Git](../../../standards/core/git.md) and [Licensing and Publication](../../../standards/core/licensing-publication.md), without changing either Standard or waiving actual rights, confidentiality, reviews or checks. Each private integration authorization expires at its named session end. The public transition allowance expires at successful protection readback or `t0 + 900 seconds`, whichever comes first; failure does not renew it.

Before any operation, record the actual operator, named PR author, eligible non-author CODEOWNER, external test author/reporter, both security-triage maintainers and unauthorized viewer, with actual consent, access and exact session authority. Owner selection is settled; availability and participation are not inferred from administrator roles. No invitation, role expansion, credential substitution or message is authorized by this procedure.

## General ownership and base-branch transition

Existing private implementation already changed only the first line of `.github/CODEOWNERS` from `* @elviszoz` to `* @elviszoz @evertonspohrversat`, as the approved one-line patch specifies. The 12 specific entries already name both; preserve their patterns, order and contents. Inspect the complete effective mapping, including root READMEs, docs/specs, `.github/CODEOWNERS` and the existing test fixture. Do not replace the file wholesale, grant access, change organization teams/defaults or add a different owner through this work. Verify the actual account identities and existing repository access without exposing credentials.

| PR author after the new fallback is effective | Required owner review | Other conditions |
|---|---|---|
| @elviszoz | @evertonspohrversat | One eligible approval, actual successful required checks and no blocking/stale review. |
| @evertonspohrversat | @elviszoz | The same conditions; author self-approval is never a substitute. |
| Another actual contributor | Either eligible named owner | One meets the selected count; stronger existing policy or blocking reviews still apply. |

Required count remains one, not two; the protection JSON below is unchanged. Require a PR and an eligible non-author owner review, dismiss stale approvals after new commits, keep the actual check/app, administrator enforcement, empty bypass and force-push/deletion denial. Do not use `require_last_push_approval` as a substitute for the requested non-author rule or silently add a second reviewer requirement.

The applicable base branch supplies CODEOWNERS for review. Before integration, the current fallback still names Elvis alone. The current complete change touches default-covered docs/specs, so a valid existing-access arrangement is Everton actually authoring/submitting the PR and Elvis substantively reviewing it. Merely adding Everton in that PR's head does not solve eligibility for an Elvis-authored PR against the old base. Do not swap nominal authors, impersonate a maintainer or bypass. If that real arrangement is unavailable, stop for a separately reviewed integration plan; do not claim this Design changed the base. After separately authorized integration, re-read the base file and exact commit before allowing reciprocal use. Private Free reviews/checks remain manually verified, not platform-enforced.

The current private implementation updates the current handoff/manifest and affected EN/PT/ES root/reporting guidance to name both general owners and shared triage while retaining the accountable coordinator and truthful unverified route. Preserve approved frozen contribution texts and all historical approvals. Source work and local mapping checks are pre-merge preparation; base adoption, public enforcement and actual reporting receipt are later distinct observations. No new ADR is required: repository/package/evidence boundaries, canonical policy and ownership roles remain, with an owner-approved assignment change only.

## Private prerequisites and final freeze

1. Reconcile evidence preservation under the approved R4 criterion and resolve actual remaining candidate/exposure gaps; reuse the recorded owner decisions and independent approval. Privately integrate/adopt the exact reviewed nine-file patch through separately authorized named PRs with actual eligible review and successful checks. Those checks/reviews are manually verified while protection is unavailable, not platform-enforced.
2. After the last private CI run, reconcile the final main SHA, all relevant refs and full exposed surfaces, including new logs, artifacts and caches. Reconfirm approved terms/preimages, source rights, sensitivity decisions, intended version availability and real reviewer access. A dated empty listing or old source scan does not satisfy this refresh.
3. Confirm the operator can read/write the intended controls using existing access. Preserve all accessible current protection/rules reads and capability errors. Reverify the `structural-validation` GitHub Actions app ID `15368`; compare the current workflow and CODEOWNERS to the reviewed content.
4. Review all human/agent/bot writers, pending pushes/merges, running and queued automation, privileged contribution processing and release paths. Record how each writer will remain idle from final clearance until protection and enforcement verification. Empty run queues alone do not establish this agreement. If infeasible, stop for a concrete separately authorized remedy; do not disable workflows, revoke credentials or alter organization settings.
5. Verify read-only workflow tokens, no Actions PR approvals, no secret/write-token forwarding and no privileged contributor-code path. The private fork policy is evidence only for its private context; actual public fork behavior must later be observed. Unsolicited public PRs are possible immediately on opening. A procedural freeze cannot prevent copying, reading or forking.
6. Bind the exact source SHA/refs, candidate, review-input manifest and proposed rule SHA-256 in the restricted operation record. Identify the named session and authority covering visibility **and** the immediate rule correction together. Any unknown or changed prerequisite stops before exposure.

## Attended visibility and protection readback

The [proposed JSON body](main-protection.proposed.json) is a preparation asset, not an executable action. Future request: `PUT /repos/versat-labs/versat-ai-harness/branches/main/protection`, API version `2026-03-10`. Do not apply it before the conditions below are met.

1. Immediately before the final authorized visibility confirmation, record UTC `t0` and a monotonic clock; the 900-second deadline includes confirmation/request delay. No timestamp is filled in ahead of execution.
2. After that one visibility action, read repository identity and visibility. An unknown outcome triggers read-only reconciliation, not a duplicate visibility action. Read main SHA, classic protection, all paginated repository/inherited rulesets and active main rules. Include this time in the same deadline.
3. A successful explicit unprotected observation may support the proposed body. A 403 is unknown configuration. If existing stronger effective rules already meet the target, preserve them and verify without writing. If a different/stronger configuration needs a different correction, stop for review of that exact delta; never overwrite it blindly.
4. Allow **one** reviewed protection application attempt. Require service success plus independent readback: `protected`, check/context and app ID, at least one eligible approval, required CODEOWNER, stale-review dismissal, administrator enforcement, empty bypass allowances and force-push/deletion denial. Inspect inherited effective rules and confirm no weaker or unintended change. `strict: false` adds no up-to-date-branch requirement; `restrictions: null` adds no new push allowlist.
5. Confirm the main SHA is unchanged and all readback observations completed before the deadline. GETs may be repeated at no more than one poll per five seconds, with a ten-second request timeout and bounded by the remaining allowance. Failed/unknown mutation is followed only by reads, not a duplicate write. CI completion is outside this activation window and follows verified protection.
6. On failure, contradictory state, timeout, lost connectivity or SHA drift, stop rollout and retain the coordinated freeze and every observation. No normal merge or release. The owner chooses a separately authorized repair/containment; there is no automatic visibility reversal, rule weakening/deletion, history rewrite, spending or permission change. Public exposure may persist. Returning to private cannot retract public copies or enable Free private protection. A new session cannot silently reset the deadline.

Record actual attempt timestamps, elapsed monotonic time, request/body hash, service outcomes, branch/rule/check identities, actor permissions, before/after source and observed unknowns. Raw payloads belong in the existing restricted system; only scrubbed references enter Harness.

## OP-CTRL-01: real public enforcement

Status: **unverified / not executed**. Trigger: successful timely protection readback and separate authority for one external fork PR, three commits, workflow/run approval and actual human reviews. No merge or cleanup is included.

The only functional fixture is `project-templates/base/.versat/standards.lock`, accompanied by its genuine operational-test dossier/evidence below; recheck its valid published base and eligible CODEOWNERS first. The external author must act through their own account/fork.

| Step | Change/observation | Required outcome |
|---|---|---|
| A | Change `harness.version` to `0.0.0`, mismatching the actual package version. | Real `structural-validation` failure, missing review and blocked mergeability. |
| B, before review | Restore exact base version and retain a harmless YAML fixture comment so the PR has a real diff. | Real passing check, missing approval and blocked mergeability. |
| B, after review | Obtain a genuine eligible non-author CODEOWNER approval. | Passing check and allowed mergeability; do not merge. |
| C, before renewed review | Change only the harmless comment. | Prior approval dismissed as stale, renewed check execution, blocked mergeability until renewed eligible approval. |
| C, after review | Obtain the second genuine eligible approval. | Passing check and allowed mergeability; do not merge. |

Observe actual fork-run token permissions from available setup metadata/logs, exact workflow revision and service policies; verify no secret forwarding or privileged contributor-code path. Do not dump environment variables, inject/access real secrets, force-push or delete main. An internal PR cannot replace the external audience. Missing transitions, unknown mergeability, inaccessible token evidence or unrelated failing checks remain unverified/failed; do not weaken checks. Confirm fresh service state before any success claim. Fixture cleanup needs its own authorization and prior evidence preservation.

## Operational test delivery prerequisite

The current workflow runs the archive-required branch for non-draft PRs. `validators/sdd/validate.py` rejects `--require-archive` when no affected dossier is selected. A fixture-only PR therefore cannot demonstrate a passing required check and allowed mergeability merely by restoring its version. This is a real prerequisite, not a reason to disable the guard or use a draft PR as a passing-merge test.

Before the later test-PR operation, prepare a bounded operational-test SDD dossier for each actual PR, only when no suitable governed contribution can be reused, with genuine stage approvals and the exact synthetic changes, expected negative/positive observations, actual local evidence and documentary delivery state appropriate to the positive revision. The operational test cases are already specified here; those later records bind actual participants/base/source and actual execution, not fabricated or backdated approvals. Keep output evidence outside check inputs where the approved contract requires; include the functional fixture in affected local validation inputs. Refresh actual results after each valid B/C input change. The real service enforcement outcome under observation remains separately recorded follow-up, so a positive fixture's pre-merge ledger does not claim its own future merge or successful public test. Negative commit A must keep its real failed state, never a forged green record. Archive selection and passing delivery on the positive non-draft head must be confirmed with the trusted base and actual required CI run. Missing genuine delivery evidence stops the test before a success claim. Do not alter existing archived history or synthetic-patch an approval to satisfy CI.

Allow these exact test dossier/evidence files plus the specified functional fixture inside the separately authorized test-PR envelope; no helper PR, additional code change or unbounded retry is implied. Reuse a real independently governed contribution only if its exact scope, authors, base and observations meet the same contract; otherwise keep the defined fixture procedure. This prerequisite does not create or approve any new dossier in this private implementation phase.

## OP-CTRL-02 — shared-rule mapping


R4 supersedes the two additional reciprocal-author test PRs. Review both named accounts' existing applicable access, complete effective CODEOWNERS mapping (general fallback and specific patterns), one-approval setting, code-owner/stale-review enforcement and empty bypass. Combine this with the actual OP-CTRL-01 sequence to verify the common rule's applicability to the owner matrix. Do not claim two account-specific service experiments occurred.

Any different rule, missing general fallback, ineligible owner or contradictory observed behavior defeats that inference and requires a targeted follow-up under its own authority. Configuration alone never substitutes for OP-CTRL-01's real denied/allowed sequence. The 15-minute limit covers initial protection readback, not later CI/test duration. This Design does not execute either procedure.

## Public reporting, external use and later release

After actual representative enforcement and shared-rule mapping succeed, execute only separately authorized PVR activation and one labelled non-sensitive marker from an intended reporter. Verify applicable report access for both Elvis and Everton through service configuration/access evidence; one accountable handler must actually receive the report, and an unauthorized viewer must be denied. Do not demand duplicate notifications, duplicate replies or a simulated handover. A real access or receipt failure still stops verification. Record an actual handover only when needed; never substitute credentials or publish a real vulnerability payload.

Keep identifiers/payloads restricted and retain the [safe fallback](../../user-docs/guides/security-reporting.md) until verification. Current private-state observations do not prove public receipt. Confirm destination/audience again at the operation; no message is sent by this procedure document.

Verify anonymous access and basic obtain/install/use against the exact reviewed public commit during opening. Release/tag-specific behavior, marketplace repinning and real consumer migrations are later separately authorized work with their own version/update/recovery checks. Do not require that later release merely to change visibility or claim a commit rehearsal proves release availability.

## Evidence fields and stop review

Keep the operation unexecuted until the actual record contains: session/authority; participant consent/capacity; private clearance and immutable evidence-preservation identities; source SHA/refs/candidate/manifest/body hashes; writer agreements and queue observations; accessible rules and check identity; UTC and monotonic `t0`/deadline; visibility outcome; each rule attempt/readback; OP-CTRL-01 commit/check/review/mergeability observations; fork token limits; public report receipt/exclusion; exact-commit external-use outcomes; owner containment decision for each failure. A blank or simulated field is not an observed pass.

The [local walkthrough record](../../validation/harness-publication-blockers/run-r2-01/walkthroughs.json) checks procedure stop decisions only. It does not supply actor consent, platform enforcement, receipt or publication authority.

API field meanings and the public PVR boundary were checked on 2026-11-16 against [GitHub branch protection](https://docs.github.com/en/rest/branches/branch-protection) and [repository PVR configuration](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository). Reobserve service behavior in the actual operation.
