# Proposal Review R2: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Open blockers: none
- Immediate next stage: isolated stop; `spec` is the next lifecycle stage only after proposal status normalization and an explicit workflow or user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Problem clarity | pass | The proposal states the beginner-content gap clearly: walking is a low-barrier activity, but GymPrimer lacks a clear distinction between everyday walking and deliberate brisk walking. |
| User value | pass | The value is concrete: readers get intensity checks, time/effort guidance, progression framing, muscle roles, technique cues, strength-training context, and stop rules. |
| Option diversity | pass | The proposal compares doing nothing, one broad principle page, two complementary pages, and a walking program. |
| Decision rationale | pass | Option C now remains the stable recommendation, and the decision log consistently keeps the two-page split and `basic_cardio_activity`. |
| Scope control | pass | Non-goals and scope budget keep out personalized plans, weight-loss targets, step mandates, medical programs, return-to-walking protocols, tracking apps, running, hiking, and treadmill-specific scope. |
| Architecture awareness | pass | The proposal names expected content pages, source index, exercise-method spec surface, template/checker surfaces, and optional media provenance without inventing runtime architecture. |
| Testability | pass | Automated checks, manual source review, and beginner comprehension proof are specific enough for downstream test-spec authoring. |
| Risk honesty | pass | The risks cover weight-loss drift, casual-walking equivalence, medical drift, prescription feel, step-count overconfidence, weak image value, broad source support, and motivational fluff. |
| Rollout realism | pass | Rollout now adds `basic_cardio_activity` to the exercise-method contract and keeps implementation blocked until downstream artifacts define contracts, validation timing, sources, optional image handling, and reader proof. |
| Readiness for spec | pass | Remaining questions are limited to spec-level contract details and implementation choices, not core proposal direction. |

## Scope Preservation Review

- Scope-preservation result: pass.
- Scope-budget result: pass.
- Vision-fit result: pass.
- Standing-gate result: pass.
- Prior finding resolution: PR-WALK-1 resolved.

The user's initial goals are visibly classified in `Initial intent preservation`: brisk walking best practices, everyday walking best practices, proposal generation, project fit, and medical/personalized-guidance boundaries are all `in scope`.

The scope budget is appropriate for a multi-workstream proposal. It separates core walking pages, the same-slice method-type dependency, technique and intensity guidance, muscle guidance, optional image work, deferred step-count/program work, separate treadmill work, and out-of-scope medical/running work.

The proposal's `Vision fit` section uses the exact allowed value `fits the current vision`, and the direction matches `VISION.md` and `CONSTITUTION.md`: Markdown remains the product, walking guidance is static and citation-backed, and the proposal avoids diagnosis, treatment, adaptive coaching, generated guidance as source of truth, and hosted app behavior.

## Recommended Proposal Edits

- Recommended edits: none required before owner acceptance.
- Optional follow-up: when normalizing the proposal to `accepted`, update `Status` and add this R2 review record under `Follow-on artifacts`.

## Recommendation

- Recommendation: approve the proposal direction for owner acceptance and downstream spec authoring.
- Reason: The proposal is now internally consistent, vision-aligned, scoped tightly enough for the two-page walking slice, and explicit that implementation remains blocked until downstream contracts, validation, source review, and beginner proof exist.
- Next step: owner may normalize the proposal to `accepted`; after that, the next lifecycle artifact is a focused spec or spec amendment covering `basic_cardio_activity`, `exercises/brisk-walking.md`, and `principles/everyday-walking.md`.
- Immediate next stage: isolated stop. This review does not automatically start spec authoring.
