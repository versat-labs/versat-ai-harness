# Documentation Standard

- Every repository MUST explain its purpose, owner, lifecycle and validation entry point.
- Architecture documentation MUST describe current reality, not only intended design.
- Significant structural decisions MUST be recorded as ADRs.
- Product changes MUST keep living specifications synchronized with implementation.
- Examples MUST be clearly distinguishable from normative requirements.
- Sensitive data, credentials and customer information MUST NOT be copied into documentation.

## Consumer documentation layout

Apply these defaults to new material where it is useful. The root README links to the actual entry points. During a reviewed adoption, an equivalent existing location MAY remain in use with working navigation. Do not create empty guides, placeholder directories or links to work that is not usable. Keep living documentation outside SDD dossiers.

| Path | Purpose |
| --- | --- |
| `README.md` | Repository orientation and links to maintained documentation. |
| `docs/user-docs/quickstart.md` | One representative first-use result when usable behavior needs explanation. An equivalent existing guide or README section can serve the same purpose. |
| `docs/user-docs/guides/` | Detailed feature or workflow guidance when the quickstart needs supporting material. Link to guides and reuse common setup. |
| `docs/architecture/overview.md` | Current system boundaries, dependencies and architecture. |
| `docs/architecture/decisions/` | New consumer ADRs. Reference these decisions in SDD by explicit repository-relative path. Existing ADR references and equivalent decision directories remain supported. |
| `docs/runbooks/` | Operation, deployment, incident and support procedures. |
| `docs/integrations/` | Details specific to integrations. |
| `docs/api/` | API conventions, contracts and references. |
| `docs/product/overview.md` | Product context for readers, linking to approved material they can access. Use `specs/product/overview.md` for the shared bootstrap discovery record. |

## Feature documentation

- When a change affects readers, planning MUST identify the audience, goal, purpose of the feature and living material to create or update. Internal changes without documentation impact require no dedicated guide or documentation task. Record why the guidance does not apply.
- A first-use guide MUST explain why and when to use the feature, prerequisites and preparation, one representative action and its observable result. Include relevant limits or recovery. Technical documentation MUST explain the rationale, contracts and operational effects that matter to its readers.
- Changes affecting documented usage MUST update the instructions and examples alongside implementation. Compare affected steps with observed results. Reuse adequate functional checks and report unavailable verification through the existing SDD evidence contract.
- Apply the [Language Standard](language.md). User guides and first-use documents use canonical English and aligned `.pt.md` and `.es.md` siblings. Update the three versions together, make language variants discoverable and preserve the meaning and observable results of examples.
- Apply the [Security](security.md) and [Licensing and Publication](licensing-publication.md) Standards. For publication planning and review, see the [user documentation and feature pages guide](../../docs/user-docs/guides/publish-product-documentation.md).
