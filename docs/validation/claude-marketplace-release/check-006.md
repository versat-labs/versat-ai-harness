# CHECK-006 review of guidance, release procedure and boundaries

Reviewer: implementing agent, on revision 5d77d73a93ec4a2560ac91c213cf7d14f970e8ef against origin/main b6b0a2abae51ec7724a2f6cb8f3c8325d0148df1. Human PR review remains required.

| Expectation | Observation | Result |
|---|---|---|
| EN/PT/ES Claude setup guides aligned and linked | `claude-setup{,.pt,.es}.md` have the same 7 sections and commands; linked from the three READMEs and the three workspace-setup guides | pass |
| Unobserved native steps labelled unverified | Each guide's "Verification status" marks GitHub install at v0.5.0, auto-update and explicit update unverified; local-catalog install is stated as exercised (CHECK-004) | pass |
| No history rewritten | 0 changed files under specs/archive, docs/handoffs, docs/releases/0.4.0-*, or other changes' docs/validation | pass |
| v0.4.0 unchanged | `git ls-remote`: v0.4.0 → c191f3b126c659fbabfd4ed3d40b474407cfd26a; no v0.5.0 tag yet | pass |
| Only allowed template changes | project-templates: base/CLAUDE.md added, base/.versat/standards.lock harness.version 0.4.0 → 0.5.0, README migration step; no other lockfile or snapshot changed | pass |
| CLAUDE.md migration documented | project-templates/README.md step 5: add import-only CLAUDE.md, surface an existing CLAUDE.md as a conflict, verify with the check | pass |
| Release procedure | scripts/release/README.md lists all version locations, both catalogs, tag-after-merge, observed-or-unverified recording and revert/patch rollback | pass |
| No premature availability claim | READMEs and guides state v0.5.0 is available only after its tag exists; latest released reference v0.4.0 | pass |
| Standard rule and unchanged rules | agent-artifacts.md adds the table row, scope sentence and "Claude instruction entry point" section; the only removed line is the scope sentence, re-added with the new clause appended; other rules unchanged | pass |
| Audit reference without restating | project-audit step 4 links validators/project/README.md; validators/project/README.md documents the check and links the Standard | pass |
| Protected PR | Draft PR versat-labs/versat-ai-harness#59; merge still requires required CI and nonauthor review | pass (pre-merge; final CI observed on the PR) |
