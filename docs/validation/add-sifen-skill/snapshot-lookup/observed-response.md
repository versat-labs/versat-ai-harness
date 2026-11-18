# Native scenario response and coordinator verification

Native agent: `/root/sifen_snapshot_eval`; fresh context (`fork_turns: none`), one attempt. Exact model/reasoning, native start time, token usage and complete network/filesystem telemetry were not exposed to the coordinator. The conversation retains the native response and its tool activity; the coordinator did not request a rerun. Prepared fixtures share host permissions and are not isolation.

## Returned answer

The agent located NT 27's Production availability date 2026-03-09 and `PAGE 1 / 1`, and identified GENFE010 as iTipIDRec in the FE nomination event, with codes 1, 2, 3, 4, 6 and 9. It distinguished Manual D208/D209 from the nomination fields introduced by NT 14; described the change from NT 14's diplomatic-card value 5 to NT 27's value 6; and related GENFE011 and validations 4464/4465/4466 to their actual local extracts. It did not present this snapshot as current compliance.

The agent disclosed that PDF inspection failed: `pypdf` was absent from the supplied environment and `pdftotext` was unavailable. It therefore limited the conclusion to extracted text without claiming independent PDF-layout verification. Official portal, current schema, live Production behavior and post-cutoff changes were not verified. The source table was available in the extract; no PDF/layout acceptance assertion was planned.

## Reported actions

From the fixture provider, the native response lists reads of SKILL.md, the Standards index and resolved core Standards, provenance, index/precedence, query utility, NT 14, NT 27, Manual sections 03 and 04; searches for GENFE010/GENFE011/iTipIDRec/dDTipIDRec/4464/4465/4466; and the two failed PDF extraction attempts. An `rg --files` call also reported the absent `.harness` path. No write, export or submission was reported. This is an attributed native report, not complete syscall telemetry.

Reproducible principal queries (relative to the fixture's skill root):

```sh
python -B scripts/query_rules.py GENFE010 --include notes --context 6 --max 100
python -B scripts/query_rules.py 'GENFE010|GENFE011|iTipIDRec|dDTipIDRec|4464|4465|4466' --regex --include notes --context 1 --max 100
```

## Independent observations

The coordinator re-ran the principal lookup against the untouched fixture and retained the raw output. It read NT 27 directly: the extract contains the declared date, physical page marker, identity-document table, GENFE004 condition and codes 1/2/3/4/6/9. Source paths cited in the answer exist. Fixture hash comparison found no changed/added/deleted files. The raw query output and fixture comparison supplement the response; the response alone was not treated as test evidence. Global absence of network/system side effects is not independently attested.

Result: the observable source-lookup, date/source citation and read-only fixture requirements pass. Complete external-action telemetry remains unavailable; no certification beyond the local exercise is claimed.
