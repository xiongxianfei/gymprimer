# Review Resolution: Exercise Method Guidance

## Status

- Open findings: none
- Current owner stage: implement
- Next review stage: code-review after M1 implementation

## Findings

### TSR-EMG-1 - Validation command ownership and classification

- Source review: `docs/changes/exercise-method-guidance/reviews/test-spec-review-r1.md`
- Status: resolved by `docs/changes/exercise-method-guidance/reviews/test-spec-review-r2.md`
- Required outcome: Add a command/validation ledger to `specs/exercise-method-guidance.test.md` that classifies every named command, assigns owner and milestone, names first required milestone, failure behavior, and evidence artifact.
- Resolution notes: Added `Validation commands` to `specs/exercise-method-guidance.test.md` with command IDs EMG-CMD1 through EMG-CMD14, classifications, owners, owning milestones, first required milestones, failure behavior, and evidence artifacts. Added a milestone proof map that ties M1, M2, M3, M4, and Lifecycle Closeout to command IDs and evidence artifacts. Updated EMG-T5 through EMG-T12 to reference command IDs instead of raw command strings where applicable.
- Review outcome: R2 confirmed the validation-command ledger, command ID references, and milestone proof map are adequate for implementation handoff.

### TSR-EMG-2 - Manual proof metadata completeness

- Source review: `docs/changes/exercise-method-guidance/reviews/test-spec-review-r1.md`
- Status: resolved by `docs/changes/exercise-method-guidance/reviews/test-spec-review-r2.md`
- Required outcome: Expand EMG-M1, EMG-M2, and EMG-M3 with automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger.
- Resolution notes: Expanded EMG-M1, EMG-M2, and EMG-M3 in `specs/exercise-method-guidance.test.md` with automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger while preserving the existing proof record paths.
- Review outcome: R2 confirmed the manual-proof metadata is adequate for implementation handoff.
