# Project validation

Validate `.versat/project.yaml`, required directories for the resolved profile, ownership, README, instructions, SDD initialization and validation entry points.

## Claude instruction entry point

`instructions.py` implements the CLAUDE.md rule of the [Agent Artifact Standard](../../standards/core/agent-artifacts.md#claude-instruction-entry-point). It is read-only and needs only the Python standard library:

```sh
python validators/project/instructions.py --root /path/to/project
python validators/project/instructions.py --root /path/to/project --json
```

Exit status 0 means compliant or not applicable (no `AGENTS.md`); 1 means at least one finding, each naming the affected Standard and a remediation; 2 means a usage error. Symlinked `AGENTS.md` or `CLAUDE.md` files are reported, not followed. Run it from the project's selected Harness release during audits; fix findings through a reviewed migration.

## Agent artifact coverage

The [Agent Artifact Standard](../../standards/core/agent-artifacts.md) defines consumer paths, format requirements and workflow readiness. Future project validation must resolve this contract through the index, distinguish Plugin exports from project artifacts and report missing dependencies without implying successful execution.

Apart from the instruction entry-point check above, no executable consumer artifact validator is implemented here yet. The repository entry point validates the Harness Plugin package, not generated project discovery, Codex agent TOML semantics, workflow completeness or external integrations. During adoption, review these contracts manually and run the target project's executor and integration checks. A passing Harness check does not prove consumer readiness.
