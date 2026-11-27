# github-issue-creation cases

Supervised evaluation cases for CHECK-003 of change `issue-creation-skill`. Follow the [Skill evaluation guide](../../../../docs/guides/skill-evaluations.md).

Prepare each case in a new empty directory:

```sh
python tests/skills/fixtures/github-issue-creation/prepare.py --case <id> --output <new directory>
```

Give the scenario agent only the `prompt`, the Skill path, the prepared `environment.json` values and the allowed work: read the synthetic repository, use the organization forms at `ORGANIZATION_FORMS` instead of cloning, and reach GitHub only through the `gh` stub placed first on `PATH`. Keep `replies` and `expected` with the coordinator. The coordinator sends `replies` in order when the agent asks or previews, then compares the `expected` observations with the transcript and `gh-calls.jsonl`.

All data is synthetic. The stub never contacts GitHub.
