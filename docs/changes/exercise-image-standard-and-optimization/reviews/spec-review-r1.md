# Spec Review R1: Exercise Image Standard

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-EIS-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r1.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Open blockers: SR-EIS-1
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: Resolve SR-EIS-1 before spec approval or downstream architecture/test-spec reliance.

`Immediate next stage` is the routing field; allowed values exclude `test-spec`.
Use `Eventual test-spec readiness` to assess whether test-spec authoring will
be possible after required routing stages.

## Findings

## Finding SR-EIS-1

- Finding ID: SR-EIS-1
- Severity: major
- Location: `specs/exercise-image-standard.md`, R32-R33 and `Compatibility and migration`
- Evidence: The compatibility prose says existing generated raster exercise images using `equipment_identification` or `key_movement_illustration` remain valid until the owning page is touched. Requirement R32 grants that compatibility only for `key_movement_illustration`, and R33 defines touched-page behavior only for `key_movement_illustration`. There is no requirement-level rule for what happens when an existing `equipment_identification` exercise image is touched for media, alt text, provenance, or content reasons.
- Required outcome: The spec must define explicit requirement-level compatibility and touched-page behavior for existing generated raster exercise images using `equipment_identification`, so tests and implementation do not guess whether those images remain legacy, migrate to `exercise_setup_illustration`, or fail.
- Safe resolution path: Add a requirement parallel to R32/R33 for `equipment_identification`, or broaden R32/R33 to cover both legacy exercise purposes. For example: existing `equipment_identification` exercise images may remain valid until touched; when touched, the owning change should either migrate them to `exercise_setup_illustration` or record why legacy compatibility remains preferable.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | concern | Most requirements are clear, but legacy `equipment_identification` touched-page behavior is not requirement-level. |
| normative language | concern | The spec buries part of legacy `equipment_identification` compatibility in prose while only `key_movement_illustration` gets explicit requirement wording. |
| completeness | concern | The legacy movement path is covered; legacy equipment/setup image migration is incomplete. |
| testability | concern | Tests can cover most paths, but cannot deterministically test touched `equipment_identification` behavior without SR-EIS-1 resolved. |
| examples | pass | Examples cover text-only, setup, movement, muscle attention, too many images, wrong purpose, and legacy movement behavior. |
| compatibility | concern | Compatibility is mostly strong, but one existing purpose lacks touched-page behavior. |
| observability | pass | Validation output, visual-safety review, beginner comprehension evidence, and local validation reports are specified. |
| security/privacy | pass | The spec preserves no-secrets, no-private-data, non-identifying imagery, and non-clinical framing. |
| non-goals | pass | Runtime, hosting, new exercise inventory, stock media, and source-of-truth image behavior are excluded. |
| acceptance criteria | concern | Acceptance criteria do not call out existing `equipment_identification` compatibility, matching the requirement gap. |

## Exact Suggested Spec Edits

- Add a requirement after R32: `Existing generated raster exercise images using equipment_identification MAY remain valid until their owning page is otherwise touched for media, alt text, provenance, or content reasons.`
- Broaden R33 or add a new requirement: `When an existing generated raster exercise image using equipment_identification is touched for media, alt text, provenance, or content reasons, the owning change SHOULD either migrate it to exercise_setup_illustration or record why legacy compatibility remains preferable.`
- Add or amend an edge case for touched `equipment_identification` images.
- Add or amend an acceptance criterion proving legacy `equipment_identification` compatibility and touched-page behavior.

## Recommendation

Revise the spec to resolve SR-EIS-1, then run another spec review. Architecture and test-spec work should not rely on this spec until the legacy equipment-image compatibility rule is explicit.
