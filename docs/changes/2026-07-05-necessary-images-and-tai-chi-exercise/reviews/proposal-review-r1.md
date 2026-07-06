## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-TC-1, PR-TC-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`
- Review resolution: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-resolution.md`
- Open blockers: PR-TC-1 and PR-TC-2 block accepting this proposal for downstream spec.
- Immediate next stage: isolated stop

## Material Findings

## Finding PR-TC-1

- Finding ID: PR-TC-1
- Severity: high
- Location: `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md:200`
- Evidence: The proposal ranks ten image candidates for the same `exercises/tai-chi-basics.md` page, records seven as "Later candidate", and says the remaining candidates are a deferable follow-up at `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md:365`. The approved exercise-image spec says exercise documents must not include more than three exercise images unless a downstream approved spec or plan records explicit justification for the exception (`specs/exercise-image-standard.md:97`). The current proposal does not say whether candidates 4-10 are alternatives, replacements, or future additions requiring a separate exception.
- Required outcome: The proposal must clarify that the top-10 list is a prioritization pool for one exercise, not a commitment to eventually place ten images on one page. It must state that the first implementation is capped at the selected three images, and any later attempt to exceed three images on `exercises/tai-chi-basics.md` needs explicit downstream approved spec or plan justification.
- Safe resolution path: Revise the `Recommended Direction`, `Scope budget`, `Expected Behavior Changes`, `Rollout and Rollback`, and `Decision Log` wording so candidates 4-10 are clearly treated as deferred alternatives or future candidates subject to the existing three-image limit. If the product owner wants more than three images on the page, route that as a deliberate downstream exception with justification under the approved exercise-image spec.
- needs-decision rationale: none

## Finding PR-TC-2

- Finding ID: PR-TC-2
- Severity: medium
- Location: `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md:320`
- Evidence: The proposed `## How much to do` example uses `Method type: low_load_control_drill`, then includes only `Beginner starting point:` and `Progression:` labels. The approved exercise-method spec requires the `How much to do` section to include visible labels or equivalent plain-language lines for `Beginner starting point:`, `Effort:`, `Rest:`, `Progression:`, and `Stop if:` (`specs/exercise-method-guidance.md:141`). It also says `low_load_control_drill` must use low effort, rest as needed, and smoother-control progression (`specs/exercise-method-guidance.md:191`).
- Required outcome: The proposal's sample Tai Chi method guidance must align with the approved exercise-method contract or explicitly defer exact method wording to the downstream spec without showing a non-conforming example.
- Safe resolution path: Add `Effort:`, `Rest:`, and `Stop if:` lines to the sample, or replace the sample with a note that downstream spec must use the approved `low_load_control_drill` labels and editorial range. Keep the wording static and non-prescriptive.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal distinguishes image prioritization for Tai Chi Basics from immediate image generation. |
| User value | pass | It targets beginner comprehension of stance, weight shift, and broad muscle attention. |
| Option diversity | pass | It includes immediate generation, text-only, combined prioritization, and split-proposal options. |
| Decision rationale | concern | Option C is plausible, but PR-TC-1 must clarify that the top-10 list does not bypass the three-image cap. |
| Scope control | concern | Non-goals are strong, but later image candidates need clearer exception routing under PR-TC-1. |
| Architecture awareness | pass | The proposal identifies exercise page, media directory, prompt records, provenance, source index, and checker surfaces. |
| Testability | concern | Image and comprehension checks are plausible, but PR-TC-2 currently gives a method example that would not satisfy the approved method spec. |
| Risk honesty | pass | The proposal names clinical, martial-curriculum, unsupported-balance, provenance, and cultural-simplification risks. |
| Rollout realism | concern | Rollout is realistic for the first three images but must state how later candidates interact with the three-image limit. |
| Readiness for spec | block | PR-TC-1 and PR-TC-2 must be resolved before the proposal is ready to normalize to accepted and feed a spec. |

## Scope Preservation Review

- Scope-preservation result: concern
- Initial user goals checked: images are important for understanding; evaluate top 10 necessary images for one exercise; choose at least the top three images; use imagegen later; add Tai Chi next; follow best practices; keep the project safe and non-clinical.
- Result: All initial goals are visible in `Initial intent preservation`, but PR-TC-1 blocks acceptance because "top 10 for one exercise" is not yet reconciled with the approved three-image normal limit.

## Recommended Proposal Edits

- Recommended edits:
  - Add a sentence after the top-10 table: "Candidates 4-10 are alternatives or future candidates, not approval to place more than three images on this page; any page version with more than three images requires explicit downstream approved spec or plan justification."
  - Update the scope-budget row for remaining Tai Chi image candidates to say they are deferred alternatives subject to the exercise-image spec's three-image limit.
  - Update rollout or rollback to say future candidates may replace one of the first three or require an explicit more-than-three-image exception.
  - Revise the `How much to do` example to include `Effort:`, `Rest:`, and `Stop if:` lines, or remove the concrete example and defer exact wording to the downstream spec.
  - Optionally add the four Tai Chi source IDs to `SOURCES.md` only when downstream content implementation reuses them beyond the proposal; this is not a proposal-review blocker.

## Recommendation

- Recommendation: changes-requested. The direction fits GymPrimer's vision and is worth pursuing, but it is not ready for spec until PR-TC-1 and PR-TC-2 are resolved. This review is isolated and does not automatically hand off to `spec`.
