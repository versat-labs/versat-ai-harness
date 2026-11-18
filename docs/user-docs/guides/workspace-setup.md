# Workspace setup

[English](workspace-setup.md) | [Português](workspace-setup.pt.md) | [Español](workspace-setup.es.md)

Prepare the repository you will work on and confirm which Harness version is available. Versat workspace distribution is managed by an administrator; installation policy and member access must be checked in your workspace.

## Prepare

1. Obtain access to the target repository and read its README and contribution guidance. Clone it with the real repository URL, or use an existing clean checkout.
2. In Codex, open that repository as the project folder. Confirm it is the primary folder before starting work.
3. Read AGENTS.md and identify the project’s Harness/provider version and Standards lock when present. Ask Codex to locate the required Skill and matching canonical resources before changing files.

OpenAI documents folder selection in [Projects and chats](https://learn.chatgpt.com/docs/projects). Project setup actions can be shared through [local environments](https://learn.chatgpt.com/docs/environments/local-environment); configure only commands required by your repository.

## Verify and recover

Ask Codex to report the working directory, selected provider version and where it found versat-sdd. The paths must belong to the intended project/provider. If access or a Skill is missing, stop that workflow and ask the repository or workspace owner to resolve it. Do not copy policy from another release or assume automatic installation. A repository without identity metadata needs an explicit classification before bootstrap or migration.

[Continue to quickstart](../quickstart.md)

## Candidate installation, exact updates and recovery

The approved license/notices are applied in the local delivery branch, but main integration and a public 0.4.0 release remain pending. Do not activate the local v0.4.0 catalog reference before the separately authorized exact release exists. Current source and installed v0.3.0 are different snapshots; match the selected provider's actual SDD version and resources. The selected local rehearsal target is Codex desktop 26.915.31945/build 9922 on macOS arm64, not a claimed support matrix.

The owner selected an individual installation under the same Versat user for the private rehearsal. On Codex desktop 26.915.31945/build 9922, its bundled CLI installed `versat-ai-harness@versat-internal` version 0.4.0 into a separate local cache; the existing workspace 0.3.0 files were unchanged. The installed copy matched every source file and resolved all five Skills and canonical resources. This verifies the private installation step, not anonymous access, a public release or the full behavioral suite.

For this selected macOS build, the observed commands were:

```sh
harness_test_catalog=/absolute/path/to/reviewed-private-catalog
/Applications/Codex.app/Contents/Resources/codex plugin marketplace add "$harness_test_catalog" --json
/Applications/Codex.app/Contents/Resources/codex plugin add versat-ai-harness@versat-internal --json
```

The reviewed local catalog names `versat-internal` and points `source.path` at the exact private candidate inside its root; it is a test adapter, not a replacement for the versioned repository marketplace. Before running these steps, verify that this personal entry/cache is absent or explicitly authorized for replacement, and preserve the workspace-managed installation. Inspect the returned plugin identity, version and installed path, compare actual files and start a fresh synthetic context with that exact installed provider. Do not confuse two installations with the same plugin name or use a different provider's Skill. A local installation may be private to your user while that user still belongs to a workspace.

[Official plugin guidance](https://developers.openai.com/plugins/build/plugins) describes local catalogs; the [preparation record](../../handoffs/harness-publication-readiness/README.md) identifies observed scope and remaining checks. A new local context shares the user's permissions and is not security isolation. First-use, failure, explicit-update and recovery cases each require their own actual observations. An external account is unnecessary for this private rehearsal; later public acceptance must still use an intended external user without private membership.

For an explicit update, record the previous exact provider and project lock/config pair; review the proposed exact replacement and resource compatibility before changing the consumer. Test the candidate in a disposable context first. After a failed update, keep or restore the last verified compatible pair and record the failure. Missing access, unavailable exact ref, incompatible runtime or missing canonical resources must stop the workflow, not select `latest`. A consumer with active SDD v3 records must retain a verified v3-capable provider; do not downgrade to an incapable old tag or remove version markers. Publication or marketplace refresh does not itself migrate consumers.

Expected result: the actual selected provider and resolved resource locations are known, or a specific prerequisite is reported unverified. Anonymous access, external installation and post-publication recovery remain separately authorized operational checks.
