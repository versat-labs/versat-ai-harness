# Public repository security

The canonical [Git](../../standards/core/git.md#public-github-repository-security) and [Security](../../standards/core/security.md) Standards resolve the typed baseline through `standards/index.yaml`. It applies to public GitHub repositories in every profile and criticality. Policy values live in the indexed YAML; Skills and templates do not select weaker alternatives.

## Prepare the provider and target

Use the exact selected provider and a Python environment with `requirements-validation.txt`. Commands below run from that provider root. Installed consumer use adds `--project-root /absolute/consumer`; its manifest, complete Standards lock, provider commit/version and file digests must match a clean provider. Direct source commands report their version, commit and dirty state explicitly and do not claim that any installed consumer was upgraded.

Choose the actual `owner/repository` explicitly. The verifier observes its numeric identity, visibility and default branch. A declared public project cannot skip controls by pointing to a private repository. An inaccessible repository, missing main or unsupported host is not a readiness pass.

## Stage configuration

```sh
python scripts/bootstrap/public_security.py --output /tmp/public-security-staging
```

The output contains `.github/CODEOWNERS`, `.github/security/main-protection.json`, `branch-administration.json`, `tag-administration.json`, `secret-settings.json` and a digest manifest. Use a fresh staging directory; conflicting files or user-created symlink destinations are refused. The standard macOS `/tmp` and `/var` system aliases are normalized before path safety checks. Identical content is unchanged on a repeated render.

Review existing settings and ownership before applying anything. Keep custom required check contexts and stronger compatible review settings. Main protection is independent of the administrator exception used for reference management. A repository with sufficient classic main protection can retain it while using the broad branch/tag rulesets. The renderer does not create repositories, modify visibility or call GitHub.

Within the user's existing operational authorization, an administrator can enable the repository secret features in **Settings → Advanced Security** and configure active branch/tag rulesets in **Settings → Rules → Rulesets**, or use the staged payloads in scoped GitHub API operations. Preserve before/after observations and reconcile existing rules rather than PUT a generated default over the current configuration. In an empty repository, establishing main precedes protection; neither that initial reference nor rendering permits a public-ready claim before all settings are verified.

## Verify current settings

Authenticate GitHub CLI in a trusted operator session with sufficient repository metadata, contents, collaborator-permission and administrative read access. The verifier uses the credentials already available to that process; it does not log in, switch accounts, grant roles or print tokens. A connected app may expose repository metadata while lacking the administration scope needed for protection details. An ambiguous 404 or empty listing from such a session is not proof that protection is absent.

```sh
python validators/security/validate.py --check-policy
python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json
```

Live mode uses bounded GET requests only. It observes classic main protection, effective branch rules, all inherited/repository ruleset details, CODEOWNERS and syntax errors at the main commit, owner permissions, repository secret controls and participation settings. Two complete normalized samples must agree before readiness. A change during collection, unavailable observation or reached resource limit remains unverified. No force push, real secret, test PR or destructive branch operation is performed.

The supported ownership proof has a global CODEOWNERS row containing the policy's designated owners and any later path rows retaining those same owners. Both need write access or stronger. GitHub can request reviews from both, while one eligible owner's approval satisfies the baseline. The most recent reviewable push still needs approval by someone other than its pusher; new reviewable commits invalidate prior approvals as configured.

The universal reference proof uses active `~ALL` branch/tag rules with no exclusions and the policy's repository administrator role as the only bypass actor. This covers future names and slash-containing names. Main controls require independently sufficient no-bypass sources, including administrator enforcement for classic protection. Complex pattern unions, unknown custom roles, hidden bypass lists or unsupported ownership overrides are unverified, not guessed compliant. Normalize them only through reviewed changes that preserve stronger controls.

## Interpret and recover

| Result | Exit | Meaning |
| --- | --- | --- |
| `pass` | 0 | Requested assessment passed; inspect mode and `public_ready`. |
| `fail` | 1 | A demonstrated violation exists; other unknown controls remain listed. |
| `unable-to-verify` | 2 | Required observation, input, permission or supported interpretation is unavailable. |
| `not-applicable` | 3 | The observed target is outside this baseline and does not contradict a declared public target. |

Only a complete passing **live** assessment can return `public_ready: true`. Local policy checks and supplied snapshots always return false even if their own assessment succeeds. Reports identify their repository, provider, policy digest, observation interval, pinned main, controls and evidence. They are observations, not signed attestations or perpetual proof; rerun before a new readiness decision and after any relevant change.

For offline diagnosis, extract the `evidence` snapshot from a prior report or use a clearly synthetic fixture:

```sh
python validators/security/validate.py --repository owner/repository --snapshot /tmp/settings-snapshot.json --output /tmp/offline-report.json
```

Do not treat offline success as current enforcement. Restore missing read access or fix the explicitly identified setting within actual authorization, then run live verification again. Missing CODEOWNERS eligibility requires a reviewed access/ownership correction. A renderer conflict requires reconciliation, not deletion of consumer content. Preserve old failed attempts. Rolling back a client/provider integration does not authorize disabling correct GitHub protections.

## Lifecycle, CI and adoption

Bootstrap stages assets and withholds public readiness while any live control is failed or unknown. Audit reports evidence and remediation without unauthorized edits. Maintenance compares the exact target baseline, preserves stronger settings/content, and verifies authorized changes. Existing product, SDD and profile checks still apply.

Ordinary PR CI runs the policy and offline tests with read-only checkout permissions. Never expose administrative credentials to fork code or add privileged PR checkout execution for this check. External contributors work in their forks and submit PRs; upstream reference changes and merge remain subject to administrative and main protections.

The implementation is source functionality until a separately reviewed exact release is published and adopted. Existing provider pins, releases and marketplace entries are not updated implicitly. Preserve valid consumer wrappers and lock/configuration as a reviewed rollback unit. The [validator README](../../validators/security/README.md) documents the executable boundary.
