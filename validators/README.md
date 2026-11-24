# Validators

Validation is the deterministic enforcement layer. Validators must emit machine-readable results in addition to concise human output and must distinguish pass, fail and unable-to-verify.

The Harness entry point validates repository structure, the portable root Plugin package and the [SDD contract](sdd/README.md). It also runs SDD regression tests through `scripts/validate/run.sh`. Install `requirements-validation.txt` in a virtual environment first.

SDD checks validate local schemas, recorded approval freshness, traceability and documentary closure prerequisites. They do not authenticate approval records, run product acceptance tests automatically, or prove remote review, CI, merge or deployment. Exact legacy exceptions remain explicitly unverified for the new gates. Other domain and technology validators remain contracts for incremental implementation.

The current source also implements [v3 acceptance/regression validation](../sdd/metadata.md), declared-input freshness and trusted baseline selection of changed archives. Historical inventory remains separate from live delivery. This source change does not publish a release or update consumers.

The [quality validator](quality/validate.py) checks changed Python sources and Unreleased notes against a Git base. See [project validation](../docs/guides/project-validation.md) for the local command and CI comparison rules.

The [public security verifier](security/README.md) evaluates canonical policy against explicit live GitHub observations or labeled offline snapshots. Local validation includes its policy/schema and offline tests; public readiness additionally requires a complete live assessment from a trusted operator. The collector is read-only and no administrative credential is added to PR CI.
