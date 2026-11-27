# Source review of public GitHub policy 2.0.0

CHECK-001 was performed in the Harness working tree based on `5775125` using the provider's ordinary bootstrap renderer and a fresh local staging directory. The renderer loaded the indexed policy through its schema. The manifest identified policy 2.0.0, SHA-256 `babd93d88981ea3b92fb88f53575e46038f4871cd9a874620fc506e6835affc6`, and these four assets.

| Staged asset | Observed contents |
| --- | --- |
| `.github/CODEOWNERS` | The global rule names both designated owners. |
| `.github/security/main-protection.json` | Active protection on main, empty bypass list, one required approval, CODEOWNER review, stale dismissal, last-push approval and blocks on deletion and force pushes. |
| `.github/security/tag-administration.json` | Creation, update and deletion of all tags restricted to repository administrators. |
| `.github/security/secret-settings.json` | Secret settings payload included in the manifest. |

The manifest and directory omitted `branch-administration.json`. The evaluator iterates over `references.targets` to emit reference controls. The revised singleton tag target therefore removes the three `refs.branch.*` obligations while retaining main evaluation and tag controls. The bootstrap, audit and maintenance Skills and their EN/PT/ES guides already refer to the shared procedure. The updated Git Standard, security guide, template and architecture overview describe the same permissions.

The source review and rendering used no test suite. Two existing suites reference the retired asset or control IDs. Required CI status was not observed for this local change.
