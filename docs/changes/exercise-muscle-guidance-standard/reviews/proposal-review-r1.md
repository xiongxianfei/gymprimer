# Proposal Review R1: Exercise Muscle Guidance Standard

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-muscle-guidance-standard/reviews/proposal-review-r1.md`
- Review log: `docs/changes/exercise-muscle-guidance-standard/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: isolated stop; `spec` is the next lifecycle stage only after proposal status normalization and an explicit workflow or user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Problem clarity | pass | The proposal states a real content-quality problem: current exercise muscle sections vary in heading and usefulness, and beginner readers need movement-role guidance rather than isolated anatomy lists. |
| User value | pass | The benefit is concrete: beginners can understand which broad regions matter, what each region helps do, what they may feel, what not to overuse, and when not to overinterpret muscle cues. |
| Option diversity | pass | The proposal compares doing nothing, a simple muscle list, role-based muscle guidance, and a separate anatomy atlas. |
| Decision rationale | pass | The recommended role-based approach follows from the rowing-machine evidence, the exercise-page contract, and the need to preserve source-backed Markdown over precise or unsupported activation claims. |
| Scope control | pass | Non-goals exclude exact activation percentages, EMG-as-instruction, individualized cueing, diagnosis, treatment, posture-correction promises, required images, anatomy-as-source-of-truth, broad one-PR migration, new exercise inventory, and personalized coaching. |
| Architecture awareness | pass | The proposal names the likely touched surfaces: focused spec, exercise template, image-standard alignment, later checker support, exercise pages, source index discipline, and manual proof records. It also rules out runtime, database, hosted app, AI coach, and generated JSON impacts. |
| Testability | pass | Automated structure checks, forbidden wording checks, image-purpose/provenance checks, alt-text checks, page-local source sections, manual source audits, and beginner comprehension proof are specific enough for downstream test-spec authoring. |
| Risk honesty | pass | The proposal identifies the major risks: anatomical overreach, overprecise claims, readers feeling wrong, excessive internal focus, review burden, migration inconsistency, misleading muscle images, premature checker enforcement, and unsupported claims. |
| Rollout realism | pass | Rollout uses a spec/template loop, a representative proof slice, touched-page legacy normalization, batched audits, and delayed checker support. Rollback is additive and preserves text-only guidance when images or role tables fail. |
| Readiness for spec | pass | Open questions are appropriately spec-level details: exact role labels, table versus bullet defaults, proof-slice list, checker codes, and legacy `## Used muscles` warning behavior. |

## Scope Preservation Review

- Scope-preservation result: pass
- Scope-budget result: pass
- Vision-fit result: pass
- Standing-gate result: pass

The user's initial goals are preserved and classified in `Initial intent preservation`: improving all exercise documents, adding clear muscle engagement guidance, using best practices, avoiding unsafe overclaiming, staying beginner-friendly, using muscle-attention visuals where helpful, and avoiding one massive implementation batch are all marked `in scope`.

The scope budget is appropriate for a multi-workstream proposal. It separates core standard decisions, same-slice dependencies, first-slice exercise updates, separate implementation slices, deferable image follow-up, separate anatomy-atlas proposal work, and out-of-scope personalized cueing.

The proposal's `Vision fit` section uses the exact allowed value `fits the current vision`, and the rationale matches `VISION.md` and `CONSTITUTION.md`: Markdown remains the product, exercise pages teach beginner literacy, and the proposal avoids diagnosis, treatment, adaptive coaching, and media-as-source-of-truth drift.

## Recommended Proposal Edits

- Recommended edits: none required before acceptance.
- Optional follow-up: when normalizing the proposal to `accepted`, update `Status` and add this review record under `Follow-on artifacts`.

## Recommendation

- Recommendation: approve the proposal direction for owner acceptance and downstream spec authoring.

The proposal is strategically coherent, source-order compatible, scoped tightly enough for a broad exercise-muscle-guidance standard, and explicit that downstream spec, architecture assessment, planning, test-spec, implementation, review, and verification are still required before changing templates, checkers, images, or exercise pages.

The next lifecycle artifact should be a focused exercise-muscle-guidance spec or spec amendment after the proposal is accepted. This direct proposal-review request remains isolated and does not automatically hand off to spec authoring.
