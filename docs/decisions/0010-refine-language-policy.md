# ADR-0010 — Refine the language policy

- Status: Accepted
- Date: 2026-09-01
- Supersedes: [ADR-0008](0008-hybrid-language-policy.md)
- Refined by [ADR-0019](0019-github-issue-language.md) for GitHub issue definitions and team discussion in issue comments.

## Context

ADR-0008 assigned Spanish to specifications, requirements and decisions. That split made technical artifacts harder to reuse across systems and conflicted with the need for one canonical technical language. The repository also retained Portuguese bootstrap documentation that did not belong to any language category in the policy.

## Decision

Use English for technical and structural artifacts, including architecture documentation, ADRs, Skills, agent instructions and SDD specifications. Use Spanish for internal business playbooks, issues, Pull Requests and corporate communication. Product interfaces and community-facing documentation use canonical English with aligned Portuguese and Spanish translations.

`standards/core/language.md` remains the canonical and detailed language policy.

## Consequences

- technical artifacts can be reused consistently across systems;
- internal business collaboration remains accessible in Spanish;
- product and community content requires maintained translations;
- legacy Portuguese and Spanish technical artifacts must be migrated to English;
- validators should classify artifacts before enforcing language requirements.
