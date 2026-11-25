# Supervised public-security scenarios

The approved `public-repository-security` Design defines these three cases. Follow
[the supervised evaluation procedure](../../../docs/guides/skill-evaluations.md):
one fresh native agent per case, sequentially, 600 seconds per case and 1800 seconds
for the suite including independent replay. No automatic retries. This is local
behavioral evidence, separate from CI and authenticated GitHub observation.

`fixtures.py --case <case> --output <fresh-directory> --source-digest <CHECK-input-digest>`
prepares a public library identity, index-resolved development lock, product context,
passing local tests and supplied settings. It does not invoke agents or authenticate.
Use the versioned prompt for the case, actual Skill/provider paths, prepared Python
and a separate allowed output directory. Preserve original inputs and outputs.

Record available native actions and original reports; never accept only a final
narrative. `manifest` detects file mutation and `replay` uses independent copies to
execute the actual snapshot verifier, renderer and fixture tests. Review semantic
outcomes separately: unavailable live readiness; both injected drift findings;
preserved ownership conflict, stronger checks and provider identity. Unknown runtime
telemetry stays unknown. Agent scope restrictions are not a security sandbox.
