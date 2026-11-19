# Optional validation assets

The `python/` directory contains project-relative files, including hidden `.versat/` and `.github/` directories. Compose it over `base` and the selected profile only when adopting the explicit Python executor. It is an optional artifact, not a profile copy or an automatically installed capability.

Read the [first-use guide](../../../docs/guides/project-validation.md) before applying the files. Supply real project tests and dependencies, resolve identity and Standards from the canonical index, and select a clean provider at an exact version/full commit. No test scaffold is supplied that can falsely pass empty discovery.

Review each destination first. Preserve existing test commands, custom framework wrappers, configuration and CI; merge/adapt the reference only after reviewing differences. The example workflow intentionally contains an unresolved commit placeholder. Replace it with the selected provider commit and use the project's existing private-checkout authorization if required. Do not treat copying it as configured or observed CI.

The thin project wrapper verifies its provider and runs quality checks and all required suites. It can be called with `bash scripts/validate/run.sh --quality-base origin/main`; executable mode is optional. Keep a reviewed rollback of the wrapper, configuration, CI and lockfile together. [Composition and migration](../../README.md) remain the shared contract.

The `documentation/` directory contains an independent, optional GitHub Actions example. Adopt it through a reviewed change using the exact Harness commit selected in the consumer lockfile. It reports mechanical results from the PR check details with read-only access and leaves the required suites in place. See [documentation reporting](../../../docs/guides/project-validation.md#documentation-reporting).
