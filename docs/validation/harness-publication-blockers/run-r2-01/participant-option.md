# Participant option for owner review

Status: proposed only, not applied. During implementation the user asked whether Elvis and Everton could both participate in all PRs, review them and share security triage, with one approval sufficient even from the author. This is a question/proposed arrangement, not confirmation of Everton's consent or authorization to bypass review.

The supported arrangement is one **eligible non-author** approval. Elvis authors and Everton reviews, or Everton authors and Elvis reviews. For an external author's PR, either eligible owner can provide the required approval. Other required checks, stale-review dismissal and any blocking review remain effective. A repository owner/admin cannot substitute self-approval for that required independent review.

The [proposed patch](codeowners-option.patch) changes only the fallback line to `* @elviszoz @evertonspohrversat`; existing specific entries already name both and remain unchanged. It has not modified `.github/CODEOWNERS`. Current Design R2 explicitly preserves that file; the concrete adjustment needs its own reviewed scope before applying it. The current approved path remains an actual Everton-authored PR reviewed by Elvis, subject to real participation and later PR authority.

Shared security triage would separately record both accountable recipients, actual access and participation, notification/receipt verification and the safe fallback. CODEOWNERS does not configure vulnerability-report delivery. No current PVR receipt, notification subscription, recipient consent or permission change is inferred from this proposal.

GitHub's [required-review guidance](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews) states that authors cannot approve their own PRs. Its [code-owner guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) permits an approval from any eligible listed owner when owner review is required. Consulted 2026-11-16. Proposed owner selection does not waive the existing review/check contract or start a remote operation.
