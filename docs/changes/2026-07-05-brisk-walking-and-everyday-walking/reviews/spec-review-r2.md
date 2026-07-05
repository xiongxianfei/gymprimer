# Spec Review R2: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-WALK-IMG-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Open blockers: SR-WALK-IMG-1
- Immediate next stage: review-resolution
- Eventual test-spec readiness: not-ready
- Stop condition: amended spec conflicts with the accepted proposal's image-scope decision

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

## Finding SR-WALK-IMG-1

- Finding ID: SR-WALK-IMG-1
- Severity: blocking
- Location: `specs/brisk-walking-and-everyday-walking.md` BWG-R24, BWG-R25A, E5, AC7; accepted proposal `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md` Image guidance.
- Evidence: The accepted proposal says walking pages do not require images by default, recommends optional one `exercise_movement_illustration` for `exercises/brisk-walking.md`, says `principles/everyday-walking.md` needs no image, and says not to add multiple walking images unless a beginner read test shows text alone is unclear. The amended spec now requires exactly two generated raster support images for `exercises/brisk-walking.md`: one movement image and one muscle-attention image. It also says the media-bearing slice requires both images. Under the repository source-order rule, accepted proposals outrank specs unless the higher-ranked source is explicitly updated.
- Required outcome: Bring the source-of-truth chain back into agreement before architecture, plan, test-spec, or implementation relies on the amended image contract.
- Safe resolution path: Either revise the accepted proposal or add a new accepted proposal/proposal amendment that explicitly changes the walking media decision to require both images, then re-review the spec; or revise the spec back to the proposal-compatible contract of text-only validity with at most one optional movement image unless beginner proof records a concrete text-only comprehension gap.
- needs-decision rationale: Owner decision is required because the maintainer has expressed a desire for all necessary images, but the currently accepted proposal still limits first-slice walking media. The decision is whether to amend the higher-ranked proposal direction or narrow the spec to match it.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | block | Required image behavior is clear in the spec but conflicts with the accepted proposal. |
| normative language | pass | The amended image requirements use testable MUST language. |
| completeness | block | The source-of-truth update is incomplete because the proposal remains unchanged. |
| testability | concern | The amended test spec is directionally testable, but it should not proceed until SR-WALK-IMG-1 is resolved. |
| examples | pass | E5 matches the amended spec's two-image behavior. |
| compatibility | block | The amendment breaks compatibility with the accepted proposal's first-slice image limit. |
| observability | pass | Image path, purpose, prompt, provenance, page-reference, and visual-safety failures are observable. |
| security/privacy | pass | The spec preserves non-identifying, no-private-data media constraints. |
| non-goals | pass | The spec keeps images support-only and excludes everyday-walking media. |
| acceptance criteria | block | AC7 is testable but cannot be accepted while the higher-ranked proposal says images are optional and multiple images require proof. |

## Exact Resolution Options

Option A: proposal amendment path.

- Add a proposal revision or follow-on accepted proposal stating that `exercises/brisk-walking.md` now requires both `exercise_movement_illustration` and `exercise_muscle_attention_illustration`.
- Record why this supersedes the earlier "optional one movement image" decision.
- Keep the amended spec's BWG-R24, BWG-R25A, BWG-R25B, E5, EC7A, and EC7B shape.
- Re-run spec-review after the proposal-level decision is accepted.

Option B: spec narrowing path.

- Restore BWG-R24/BWG-R25 to allow text-only validity and at most one optional `exercise_movement_illustration`.
- Remove the required `exercise_muscle_attention_illustration` from this walking spec.
- Keep muscle-attention media as a future follow-up requiring beginner-proof evidence or a proposal amendment.
- Re-run spec-review.

## Scope Notes

This review did not inspect implementation assets or generated images because the spec is not approved for implementation.

The related `specs/exercise-image-standard.md` permits movement and muscle-attention images generally, but it does not override the accepted walking proposal's narrower first-slice media decision.

## Routing

No automatic downstream handoff.

The immediate next stage is `review-resolution` because the material finding needs an owner decision about whether to amend the higher-ranked proposal direction or narrow the spec.
