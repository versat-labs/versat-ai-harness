# Issue authoring review

Reviewed the maintained files at commit `ecaa6463550d032d9fb77cbc055df1d713a4575b` using the local examples in Design revision 1 for issue #50.

| Case | Observation and disposition |
|---|---|
| CSV feature request | The [issue rule](../../../standards/core/language.md#github-issues) covers the title, authored form answers, problem, outcome and applicable acceptance criteria. Write them in English. |
| Bug with the message `Archivo no encontrado` | The same section calls for English reproduction steps and outcomes and preserves verbatim diagnostics. Keep the quoted message as reported. |
| English title and Spanish description | The first sentence of the issue rule applies to both fields. A reviewer can request an English description. |
| A teammate asks where a fixture lives | The second paragraph permits discussion in Spanish and explicitly exempts routine comments from translation. |
| A discussion adds archived records to a CSV export | The maintainer must add that acceptance criterion to the English description. Reading the description reveals the decision. |
| Maintainer guidance | The [root language instructions](../../../AGENTS.md#languages) distinguish issue fields from team comments. Step 2 of the [English](../../user-docs/guides/contributing.md), [Portuguese](../../user-docs/guides/contributing.pt.md) and [Spanish](../../user-docs/guides/contributing.es.md) guides makes the same distinction. Each link resolves to the GitHub issues section. |
| Internal pull request | The [artifact table](../../../standards/core/language.md#required-language-by-artifact) specifies Spanish. The [PR template](../../../.github/pull_request_template.md) retains its Spanish headings and instructions, including the reference to the internal PR language rule. Its contents match the comparison revision. |

[ADR-0019](../../decisions/0019-github-issue-language.md) is indexed and links back to [ADR-0010](../../decisions/0010-refine-language-policy.md). The earlier decision adds a reciprocal reference and retains its historical text. The [changelog](../../../CHANGELOG.md) records the issue convention under Unreleased.

CHECK-001 passed for all seven local scenarios and both retained obligations it covers. The review was repeated on `a5860da` after the marketplace correction with the same outcomes and matching input snapshots. The [full suite rerun](suite.md#corrected-run) supplies the second required check for REQ-003 scenario 1.
