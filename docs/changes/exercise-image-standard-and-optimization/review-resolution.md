# Review Resolution: Exercise Image Standard and Optimization

| Finding | Source | Status | Disposition |
|---|---|---|---|
| SR-EIS-1 | `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r1.md` | resolved | `specs/exercise-image-standard.md` now states at requirement level that existing `equipment_identification` and `key_movement_illustration` exercise images remain valid without media-purpose migration. |
| TSR-EIS-1 | `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r1.md` | resolved | `specs/exercise-image-standard.test.md` now classifies EIS-CMD5 as planned M1/M2 support, adds EIS-T18 for template-aware checker validation, and `docs/plans/2026-07-03-exercise-image-standard.md` mirrors that obligation in M1/M2. |
| CR-EIS-M1-1 | `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m1-r1.md` | pending test-spec-review | Owner directed broad privacy validation to happen during verify before PR rather than blocking M1. `specs/exercise-image-standard.test.md` and `docs/plans/2026-07-03-exercise-image-standard.md` now defer EIS-CMD4 to lifecycle closeout / verify; test-spec-review must approve the validation-path amendment before M1 code-review re-review. |
| TSR-EIS-2 | `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r3.md` | open | The validation-path amendment is internally inconsistent because the plan's general validation section still lists the broad EIS-CMD4 privacy command as expected after implementation begins. |
