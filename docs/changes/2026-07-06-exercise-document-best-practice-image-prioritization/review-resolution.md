# Review Resolution: Exercise Document Best-Practice Image Prioritization

## Status

Closed.
Code-review M2 R2 confirmed CR-EDIP-M2-1 is resolved.
M2 is closed.
Code-review M1 R2 confirmed CR-EDIP-M1-1 is resolved.
Proposal-review findings PR-EDIP-001 and PR-EDIP-002 remain resolved by proposal revision and proposal-review R2.

## Findings

| Finding | Status | Required resolution |
|---|---|---|
| PR-EDIP-001 | resolved | The proposal now treats fewer than five images as an evaluation trigger and the top five as a candidate backlog, while preserving the approved three-image normal limit unless downstream approved artifacts justify a fourth or fifth image. |
| PR-EDIP-002 | resolved | The proposal now removes proposal-specific PR-review rule language and states that generated image promotion remains governed by the existing exercise-image standard, provenance contract, and visual-safety review requirements. |
| CR-EDIP-M1-1 | resolved | Code-review M1 R2 confirmed M1 validation now rejects top-five candidate dispositions that select generation directly and focused tests cover `generate_now` and `first_generation_candidate`. |
| CR-EDIP-M2-1 | resolved | Code-review M2 R2 confirmed the Bird Dog page-local candidate table now has an adjacent scoring matrix with the required five per-candidate scoring fields, total score, and disposition traceability for ranks 1-10. |

Proposal-review R2 approved the revised proposal with no material findings.

## CR-EDIP-M2-1

Source review: `reviews/code-review-m2-r1.md`

Required outcome:

The Bird Dog page-local candidate table must record the five per-candidate scoring fields required by M1, while retaining the total score and disposition for each rank.

Resolution:

Resolved.
The M2 audit evidence now has an adjacent scoring matrix with beginner comprehension, setup value, muscle-attention value, page value, readiness, and total score for ranks 1-10.
Markdown/privacy validation passed after the evidence update.
Code-review M2 R2 confirmed the finding is resolved.

## CR-EDIP-M1-1

Source review: `reviews/code-review-m1-r1.md`

Required outcome:

M1 validation must reject or require explicit separate generation-decision justification for top-five `generate_now` and `first_generation_candidate` dispositions.
The focused M1 tests must include direct proof for those rank 1-5 cases, or equivalent coverage showing top-five backlog status cannot become an automatic generated-image batch.

Resolution:

Addressed by extending EDIP-T5 focused tests with top-five `generate_now` and `first_generation_candidate` fixtures.
The audit validator now rejects rank 1-5 generation dispositions with `top_five_candidate_must_not_select_generation_directly`.
Focused M1 validation passed after the fix.
Code-review M1 R2 confirmed the finding is resolved.

## PR-EDIP-001

Source review: `reviews/proposal-review-r1.md`

Required outcome:

The proposal must clarify whether "five" means five total images on a page, up to five new generated images, or only a candidate-ranking cap.
If the proposal intends to normalize five images per exercise page, it must explicitly propose a spec amendment to replace or narrow the current three-image normal limit.
If it does not intend to change the approved image-count policy, it must state that pages still default to the minimum needed and the existing three-image limit, with page-specific justification for any fourth or fifth image.

Resolution:

The proposal was revised so "fewer than five existing images" is an evaluation trigger, not a requirement to bring every page to five images.
The top five ranked images are now a candidate backlog.
Generation selects the minimum needed subset from that backlog and preserves the approved exercise-image count policy: the normal zero-to-three image range remains in effect, and any fourth or fifth image requires downstream approved page-specific justification.

## PR-EDIP-002

Source review: `reviews/proposal-review-r1.md`

Required outcome:

The proposal must define the eligible reviewer and timing.
PR author review is acceptable only when the author is a named accountable human maintainer or reviewer handle.
AI agents and image-generation tools cannot satisfy this role.
Visual-safety, provenance, and reviewer-handle evidence must be recorded before any generated image is promoted.

Resolution:

The proposal was revised to remove proposal-specific PR-review rule language.
It now records the user's statement that pull requests merge only after author review and agreement, while generated image promotion remains governed by the existing exercise-image standard, provenance contract, and visual-safety review requirements.

## Sources

- `reviews/proposal-review-r1.md`
- `reviews/proposal-review-r2.md`
- `reviews/code-review-m1-r1.md`
- `reviews/code-review-m1-r2.md`
- `reviews/code-review-m2-r1.md`
- `reviews/code-review-m2-r2.md`
- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.md`
