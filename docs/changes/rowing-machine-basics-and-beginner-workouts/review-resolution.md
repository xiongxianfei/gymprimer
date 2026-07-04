# Review Resolution: Rowing Machine Basics and Beginner Workout Guidance

## Status

pending code-review

## Open findings

| Finding ID | Review | Status | Required owner action |
| --- | --- | --- | --- |
| PR-RMB-1 | `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/plan-review-r1.md` | resolved by `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/plan-review-r2.md` | Plan references were revised from the incorrect prompt-record directory to the approved `media/prompts/exercises/rowing-machine/<asset-stem>.md` path shape, and plan-review R2 approved the resolution. |
| TSR-RMB-1 | `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/test-spec-review-r1.md` | resolved by `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/test-spec-review-r2.md` | `RMB-M1` through `RMB-M5` now include explicit automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger; test-spec-review R2 approved the resolution. |
| CR-RMB-M2-1 | `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r1.md` | resolved pending M2 code-review | Safety notes were split into source-supported groups in `exercises/rowing-machine.md`; real-page tests now require the page-local safety source IDs, and M2 validation passed. |

## Resolution notes

- 2026-07-04: Opened for plan-review R1. The plan is paused at plan revision
  until PR-RMB-1 is resolved.
- 2026-07-04: Addressed PR-RMB-1 by updating the plan context, M3 file list,
  and M3 privacy command to use `media/prompts/exercises/rowing-machine/<asset-stem>.md`
  or the existing `media` scan surface. Rerun plan-stage checks and request
  plan-review R2.
- 2026-07-04: Plan-stage privacy, whitespace, and stale prompt-record path
  scans passed after the PR-RMB-1 revision.
- 2026-07-04: Plan-review R2 approved the PR-RMB-1 resolution and closed the
  plan-review finding.
- 2026-07-04: Opened TSR-RMB-1 from test-spec-review R1. Implementation is
  blocked until manual-proof metadata is added and re-reviewed.
- 2026-07-04: Addressed TSR-RMB-1 by adding required manual-proof metadata to
  `RMB-M1` through `RMB-M5`; test-spec-review R2 approved the resolution.
- 2026-07-04: Test-spec-review R2 approved the TSR-RMB-1 resolution and closed
  the test-spec-review finding.
- 2026-07-04: Opened CR-RMB-M2-1 from code-review M2 R1. M2 is paused for
  review-resolution until safety stop-condition source support is corrected
  and M2 is returned to code-review.
- 2026-07-04: Addressed CR-RMB-M2-1 by splitting `## Safety notes` into
  cardiopulmonary, pain/worsening/numbness, and painful/uncontrolled technique
  groups with nearby page-local citations. Added test coverage for the safety
  source IDs and reran M2 validation. M2 is ready for code-review rerun.
