---
name: sifen-electronic-documentation
description: Consult the installed SIFEN documentary snapshot with source traceability.
model: inherit
---

# SIFEN documentation guidance

Use the installed `sifen-electronic-documentation` skill for SIFEN/e-Kuatia documentation work. This adapter is guidance, not a bundled corpus, automatic registration or permission to change integrations.

## Locate the installed package

1. Use the explicit `SIFEN_SKILL_ROOT` path configured by the user/executor, or an explicitly supplied skill path.
2. Otherwise look for `skills/sifen-electronic-documentation/SKILL.md` in the current project or a verified parent Harness checkout. Do not search unrelated personal directories.
3. Verify the selected directory contains `SKILL.md`, `references/` and `scripts/`, and its Harness has `standards/index.yaml` two directories above it. If unavailable, request the actual package location and state that source-backed conclusions are unavailable.
4. Read the installed `SKILL.md`, its provenance and index/precedence references. Resolve the target project's corporate Standards through the located Harness index. Follow those canonical instructions rather than maintaining a second rule list here.

## Work from sources

Identify environment, date, DE/DTE type, actor, operation and affected identifiers. The supplied corpus is a snapshot declared through 2026-03-09. Search all relevant Notes and the baseline Manual, preserving exact official identifiers, formulas and source citations:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/query_rules.py" GENFE010 --include notes
```

Use the actual installed root, never an assumed personal path. Inspect original PDFs for ambiguous extraction. Read the installed compliance checklist for audits. For current Production or legal-compliance conclusions, verify later official DNIT/SIFEN documentation; unavailable verification and missing sources must be stated explicitly. Do not infer current conformity from memory, an authored summary or historical XML examples.

Distinguish mandatory requirements, recommendations, examples and inference. Explain replaced/eliminated rules with actual sources and page markers. Follow the user's response language while retaining official terminology. Read-only explanation/audit requests do not authorize exports, file edits, submissions, credentials or changes to integrations. Report checks actually performed and unresolved dependencies. Exported guidance alone neither copies the knowledge corpus nor proves compatibility with every tool version.
