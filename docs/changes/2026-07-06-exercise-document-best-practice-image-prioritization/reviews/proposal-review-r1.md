## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-EDIP-001, PR-EDIP-002
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`
- Review resolution: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- Open blockers: PR-EDIP-001 and PR-EDIP-002 must be resolved before owner acceptance or downstream spec reliance.
- Immediate next stage: no automatic downstream handoff

## Material Findings

## Finding PR-EDIP-001

- Finding ID: PR-EDIP-001
- Severity: high
- Location: `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`, Recommended Direction and Expected Behavior Changes.
- Evidence: The proposal selects "every exercise document with fewer than five images" and says it will "generate up to the top five image candidates" for each document. It also says the first slice uses "five images as the default cap" and only treats a sixth image as an exception. The approved exercise-image spec says exercise documents use the minimum number of images needed for comprehension, must not include more than three exercise images unless a downstream approved spec or plan records explicit justification, and acceptance criteria preserve zero-through-three as the normal image range.
- Required outcome: Clarify whether "five" means five total images on a page, up to five new generated images, or only a candidate-ranking cap. If the proposal intends to normalize five images per exercise page, it must explicitly propose a spec amendment to replace or narrow the current three-image normal limit. If it does not intend to change the approved image-count policy, it must state that pages still default to the minimum needed and the existing three-image limit, with page-specific justification for any fourth or fifth image.
- Safe resolution path: Revise the proposal's Goals, Recommended Direction, Expected Behavior Changes, Rollout and Rollback, Risks, Scope Budget, and Next Artifacts so "documents with fewer than five images" is an evaluation trigger rather than an automatic generation target, unless the owner explicitly chooses to revise the exercise-image spec's image-count policy.
- needs-decision rationale: Owner decision is needed on whether this proposal changes the normal exercise-image count from three to five, or keeps the current three-image normal limit and treats four or five as justified exceptions.

## Finding PR-EDIP-002

- Finding ID: PR-EDIP-002
- Severity: medium
- Location: `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`, Slice decisions, Testing and Verification Strategy, and Risks and Mitigations.
- Evidence: The proposal says "The PR author will review the PR after submission" and that review should include human visual-safety and provenance approval. The approved exercise-image spec requires generated raster provenance to name an accountable human maintainer or GitHub handle, forbids an AI tool as reviewer, requires approved review status before promotion, and requires visual-safety evidence that identifies reviewed image path, referencing page, review criteria, pass/fail result, reviewer role or handle, and residual risk.
- Required outcome: Define the eligible reviewer and timing. The proposal should state that PR author review is acceptable only when the author is a named accountable human maintainer or reviewer handle; AI agents and image-generation tools cannot satisfy this role; and visual-safety, provenance, and reviewer-handle evidence must be recorded before any generated image is promoted.
- Safe resolution path: Revise the review language to separate PR review from promotability: PR author review may be the human review path after submission, but the downstream spec or plan must record reviewer eligibility, evidence fields, and promotion gate timing.
- needs-decision rationale: Owner decision is needed on whether the PR author can self-approve generated media, or whether a second named human reviewer is required for generated image promotion.

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal identifies per-exercise image evaluation and explains why direct image generation from chat is not acceptable. |
| User value | pass | The user value is concrete: better beginner comprehension for setup, movement, and broad muscle attention. |
| Option diversity | pass | The options include direct generation, repository-wide ranking, per-document ranking, and text-only cleanup. |
| Decision rationale | concern | Per-document ranking follows the user's clarified direction, but the rationale around a five-image page target is not yet aligned with the approved image-count policy. |
| Scope control | concern | Scope budget exists, but "all documents with fewer than five images" plus "top five" can be read as broad generation across most exercise pages. |
| Architecture awareness | pass | The proposal names media paths, prompt records, provenance, validation, and change-local evidence. |
| Testability | pass | Automated and manual proof obligations are named. |
| Risk honesty | concern | The proposal names image-count and AI self-approval risks, but the mitigations need stronger owner decisions before spec. |
| Rollout realism | concern | Small slices are stated, but the proposal's evaluation population and five-image language can still overrun the accepted media policy. |
| Readiness for spec | block | The spec stage would not know whether to preserve the current three-image limit or design a new five-image policy. |

## Scope Preservation Review

- Scope-preservation result: pass with findings.
- Initial user goals checked: list top 10 images for each exercise document; generate at least the top five images; improve all exercise documents; follow best practices; evaluate each document instead of the repository; select all documents without five images; preserve older sequence images unless justified; use change-local audit proof first; use PR author review after submission.
- Result: The proposal visibly classifies all initial goals and routes deferred generation through downstream artifacts. PR-EDIP-001 and PR-EDIP-002 are not scope-preservation omissions; they are policy and review-gate clarity issues.

## Recommended Proposal Edits

- For PR-EDIP-001, replace ambiguous "generate up to the top five image candidates" wording with one of two explicit directions: either "evaluate up to ten and normally generate only the minimum needed, with three images as the default maximum unless a page-specific exception justifies four or five" or "revise the exercise-image standard so five images becomes the new page-specific cap."
- For PR-EDIP-001, define whether existing images count toward the five-image cap. The current wording does not say whether a page with two existing images may receive five more images or only enough additional images to reach five total.
- For PR-EDIP-002, replace "The PR author will review the PR after submission" with reviewer eligibility and evidence language that satisfies the existing `human_reviewer`, `review_status`, and visual-safety evidence contract.
- For PR-EDIP-002, decide whether PR author self-review is acceptable for generated media, or whether a second named human reviewer is required.

## Recommendation

- Recommendation: changes-requested.
- Reason: The proposal direction is viable and fits the project vision, but it is not ready for owner acceptance or spec because it is ambiguous about whether it changes the approved three-image normal limit and because the human-review gate is underspecified.
- Next step: revise the proposal to resolve PR-EDIP-001 and PR-EDIP-002, then rerun proposal review.
- Immediate next stage: no automatic downstream handoff. This review does not automatically hand off to `spec`.

## Sources

- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `AGENTS.md`
- `CONSTITUTION.md`
- `VISION.md`
- `docs/workflows.md`
- `specs/exercise-image-standard.md`
- `media/PROVENANCE.md`
