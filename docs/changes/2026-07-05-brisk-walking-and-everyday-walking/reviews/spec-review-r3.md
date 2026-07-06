# Spec Review R3: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r3.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Open blockers: none
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready; downstream architecture/plan/test-spec artifacts must be updated or confirmed current for the required media contract
- Stop condition: none

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

None.

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | pass | Required brisk-walking media is specified as exactly one movement image and one muscle-attention image. |
| normative language | pass | The amended image contract uses testable MUST language and delegates media mechanics to the approved exercise-image standard. |
| completeness | pass | The spec covers page contracts, method type, sources, safety, media, validation, rollback, and non-goals. |
| testability | pass | Image references, media purposes, alt text, prompt records, provenance rows, page references, and visual-safety evidence are observable. |
| examples | pass | E5 matches the amended proposal and required two-image behavior. |
| compatibility | pass | The amended proposal now authorizes the two-image first slice; everyday walking remains text-only. |
| observability | pass | Automated and manual validation surfaces are named, including required media failures. |
| security/privacy | pass | The spec excludes user input, private health data, private reviewer/reader details, trackers, accounts, analytics, and identifiable people. |
| non-goals | pass | The spec preserves no medical program, no personalization, no generated image as source of truth, and no everyday-walking image. |
| acceptance criteria | pass | AC7 now aligns with the accepted proposal's required movement and muscle-attention image decision. |

## SR-WALK-IMG-1 Recheck

SR-WALK-IMG-1 is resolved at the spec-review layer.

The accepted amended proposal now requires one `exercise_movement_illustration` and one `exercise_muscle_attention_illustration` for `exercises/brisk-walking.md`, keeps `principles/everyday-walking.md` text-only, and preserves support-only Markdown-first media boundaries.

The amended spec matches that direction through BWG-R24, BWG-R25, BWG-R25A, BWG-R25B, BWG-R26, E5, EC7A, EC7B, AC7, observability, and rollback language.

## Scope Notes

This review did not inspect generated image assets because implementation remains downstream.

The related `specs/exercise-image-standard.md` already permits one movement image and one muscle-attention image on an exercise document when each image has one purpose, stays support-only, has prompt/provenance records, passes visual-safety review, and remains subordinate to Markdown.

## Routing

No automatic downstream implementation handoff.

The immediate next stage is architecture assessment or architecture update because the accepted proposal/spec now require media assets, prompt records, provenance rows, validation proof, and visual-safety evidence where the prior implementation closed as text-only.
