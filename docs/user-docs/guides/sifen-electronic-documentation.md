# SIFEN electronic documentation

[English](sifen-electronic-documentation.md) | [Português](sifen-electronic-documentation.pt.md) | [Español](sifen-electronic-documentation.es.md)

Use the [SIFEN skill](../../../skills/sifen-electronic-documentation/SKILL.md) to consult the supplied Manual v150, Notes 1–27 and testing/submission guides. This source addition is unreleased; installing a published older Harness does not include it. The declared snapshot ends on **2026-03-09**. Current production conclusions require later official-source verification. Local lookup does not certify fiscal compliance.

From the root of the actual installed Harness checkout, with Python 3.11+:

```sh
export SIFEN_SKILL_ROOT="$PWD/skills/sifen-electronic-documentation"
python3 "$SIFEN_SKILL_ROOT/scripts/query_rules.py" GENFE010 --include notes --context 2 --max 50
```

The utilities use the Python standard library. Queries are literal and case-insensitive by default; `--regex` and `--case-sensitive` opt into those modes. `--include` filters relative paths. No match returns success with an empty-result message. Invalid arguments, unreadable/missing corpus or a selection with no source files return an error. A result-limit message means more sources may need inspection. Search Notes and Manual separately, read source context and cite actual pages; missing documents and ambiguous extracts must be reported.

Example request:

> Use $sifen-electronic-documentation to explain GENFE010 in Production on 2026-03-09, using the local sources. Cite the applicable Note and do not modify files or submit documents.

## Optional exports

Export only when you want to add guidance to a chosen project:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/export_agent.py" generic --destination /path/to/project
```

Platforms: `claude`, `gemini`, `copilot`, `cursor`, `generic`. All output collisions are checked before writing; existing files cause an error without partial output. `--force` explicitly replaces existing regular output files. Export does not copy the corpus or install a native Codex agent. Configure `SIFEN_SKILL_ROOT` for the target executor or provide the verified installed path; it must still access the skill and its Harness Standards. Generated files are artifact-tested; live compatibility with every IDE version is not claimed.

The original official files and extracts retain their language and hashes. This skill’s authored material uses [Apache-2.0](../../../skills/sifen-electronic-documentation/LICENSE-SCOPE.md). For official materials, see the [DNIT attribution and applicable terms](../../../skills/sifen-electronic-documentation/references/attribution-notice.md) and the [source provenance](../../../skills/sifen-electronic-documentation/references/provenance.md).

Run the repository's full validation with `./scripts/validate/run.sh` after installing `requirements-validation.txt` in the documented Python environment. The focused suite can be run with `python -m unittest discover -s tests/skills -p test_sifen_documentation.py`; it does not replace the full suite or supervised evidence.
