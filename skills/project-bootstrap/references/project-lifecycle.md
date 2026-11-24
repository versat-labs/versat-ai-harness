# Project Lifecycle

## 1. Intake

Capture sponsor, objective, expected users, data sensitivity, operational criticality, profile and technologies. Use [guided product discovery](product-discovery.md) to develop the product context with the developer, reusing supplied information and recording unknowns explicitly.

## 2. Bootstrap

Create the repository from the composed template, populate `specs/product/overview.md` and supporting files when needed, add the project identity and lockfile, initialize the first SDD change with references to the product context, and run baseline validation. Present the product draft and evidence gaps for review separately from structural readiness.

Use the version-matched [composition guide](../../../project-templates/README.md) to distinguish consumer artifacts from the installed Plugin package. Record artifact purpose, executor and dependencies in the generated architecture documentation. Keep authoring placeholders and examples separate from active project capabilities.

Apply the resolved [Documentation Standard](../../../standards/core/documentation.md) to actual usable behavior when populating the base README's first-use entry point. Follow the composition guide's conditional authoring instructions; product ambitions alone do not supply runnable usage content.

## 3. Repository readiness

Verify ownership, default branch protection, required checks, secret scanning, dependency update policy and access boundaries before normal delivery begins.

For public GitHub projects, follow the index-resolved public-security contract and [verification procedure](../../../docs/guides/public-repository-security.md). The complete fresh live result, including its mode and `public_ready` value, is required before declaring public readiness. A composed skeleton, rendered settings or an offline assessment remains preparation. Use only actual operational authorization, preserve stronger controls, and re-observe authorized configuration changes.

Verify any emitted README guide link and affected documented steps against actual behavior under the resolved Standards. Report unavailable verification separately from a successful structural check.

For projects with operational workflows, verify their bindings and executor support under the resolved Standards. A successful Plugin validation does not establish that external integrations or consumer agents work.

## 4. Delivery

Use the SDD lifecycle for material changes. Keep proposal, requirements, design, tasks, implementation and validation consistent throughout review.

## 5. Operations

Operate according to the resolved profile and criticality requirements. Preserve observability, recovery, security and ownership evidence.

## 6. Evolution

Adopt Harness and Standards updates only through explicit versioned migrations. Review diffs, update the lockfile, run validation and merge through the governed workflow.

## 7. Retirement

Document owners, data disposition, dependency removal, access revocation and retained records. Retirement is a governed change, not an untracked deletion.
