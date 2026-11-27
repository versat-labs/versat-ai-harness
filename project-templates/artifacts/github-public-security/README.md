# Public GitHub security assets

This conditional extension composes over the shared base for public GitHub projects in every profile. It is not an additional copied profile or automatic configuration of GitHub.

From the exact selected provider, run `python scripts/bootstrap/public_security.py --output /absolute/empty-staging-directory`. The renderer locates the typed policy through `standards/index.yaml`, emits CODEOWNERS, separate payloads for main protection and tag administration, the secret-settings payload and a digest manifest. It refuses conflicting files and unsafe paths; identical content is idempotent.

Review staged assets before adoption. Preserve custom content and stronger compatible rules, particularly required check names and existing effective classic main protection. Rendered payloads are examples for reviewed administrative operations, not instructions to replace existing settings wholesale. A rendered directory never establishes public readiness. Private projects retain their applicable existing policy.

Follow the [public-security procedure](../../../docs/guides/public-repository-security.md) for authorized application and fresh live verification. Keep the exact provider and policy digest in the consumer's lock through a reviewed versioned migration; never silently adopt `latest`.
