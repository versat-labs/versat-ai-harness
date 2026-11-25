# Security validation

`validate.py` assesses the index-resolved public GitHub security contract. `policy.py` evaluates normalized observations; `scripts/security/github.py` collects bounded GET-only data through GitHub CLI. Neither modifies GitHub. This check complements threat modeling and human security review; it does not scan source for secrets or inspect secret alerts.

Use `--check-policy` for local policy/schema validation, `--snapshot FILE --repository OWNER/REPO` for explicitly offline evidence, or `--live --repository OWNER/REPO` for current settings. `--project-root PATH` additionally verifies the consumer's exact provider/Standards lock. `--output FILE` writes a JSON report. Only a complete, stable live pass sets `public_ready: true`; exit 0 alone is insufficient.

Exit codes: 0 successful requested assessment; 1 non-compliance; 2 missing/invalid/unverifiable evidence; 3 genuinely non-applicable target. Each control supplies its result, diagnostic, evidence and remediation. An aggregate failure retains all unknown controls. A missing ruleset bypass list is never assumed empty. Reports do not authenticate themselves or provide lasting assurance against later drift.

Normal package/PR CI checks the policy and offline regression suites without production credentials. The trusted operator runs live assessment separately. See the [setup and verification guide](../../docs/guides/public-repository-security.md) for supported proof shapes, permissions, rendering, recovery and evidence limits.
