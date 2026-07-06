# Code Review M4 R1: Necessary Images and Baduanjin Exercise

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r1.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M4-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`
- Review resolution: required
- Reviewed milestone: M4
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M4 resolution
- Required review-resolution: yes
- Finding IDs: CR-M4-001
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `787ae04` (`M4: add Baduanjin review proof`).
- Tracked governing branch state: `proposal/baduanjin-exercise-images` at `787ae04`.
- Governing artifacts: `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`.
- Validation evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`.
- Relevant implementation files: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/beginner-comprehension-proof.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md`, `tests/test_markdown_first_real_pages.py`.

## Diff Summary

M4 adds the Baduanjin beginner-comprehension proof, text-only rollback proof, and real-page tests that require those proof records to exist and name the expected prompts, paths, cleanup surfaces, commands, and pass result.
The milestone also updates validation notes, explain-change rationale, the active plan, change metadata, and the plan index to route M4 to code review.

## Findings

## Finding CR-M4-001

- Finding ID: CR-M4-001
- Severity: major
- Location: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md:46`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md:123`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md:252`
- Evidence: The rollback proof and validation records state that `GYMPRIMER_ROOT=/tmp/gymprimer-baduanjin-rollback.* python3 tools/checks/check_markdown_first.py ...` passed. Re-running that recorded command literally fails because the wildcard in the environment assignment is not expanded by the shell, and the checker exits with `AttributeError: 'NoneType' object has no attribute 'startswith'`.
- Required outcome: M4 rollback evidence must record a reproducible temporary-root command sequence that matches the command actually exercised, and the focused rollback Markdown-first and privacy checks must pass from that recorded sequence.
- Safe resolution path: Replace the wildcard environment assignment record with a concrete temporary-root variable setup or concrete temp path, rerun the focused rollback Markdown-first and privacy checks, update rollback proof, validation notes, plan evidence, and change metadata consistently, then return M4 to code review.
- needs-decision rationale: none

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | R41 beginner-comprehension proof is recorded with the required prompts. R42 rollback proof exists, but the recorded rollback command is not reproducible as written. |
| Test coverage | concern | The new M4 tests require proof files and key tokens, but they do not catch the invalid shell form in the rollback command record. |
| Edge cases | block | The named E4/MP4 rollback edge case depends on credible proof that the text-only page remains valid after image rollback; the recorded command fails when run literally. |
| Error handling | pass | The static page has no runtime error path; rollback remains the relevant recovery path. |
| Architecture boundaries | pass | M4 does not introduce runtime, hosted app, CMS, database, user-input flow, video-first path, or generated exercise guidance as source of truth. |
| Compatibility | concern | The rollback proof is meant to be repeatable by future maintainers, but the current recorded command shape is incompatible with shell wildcard behavior in environment assignments. |
| Security/privacy | pass | The proof records are non-identifying and do not add private reader, health, contact, location, or training-log data. |
| Derived artifact currency | concern | Rollback proof, validation notes, plan evidence, and change metadata consistently repeat the same invalid rollback command record. |
| Unrelated changes | pass | The diff is limited to M4 proof records, proof-record tests, and lifecycle evidence. |
| Validation evidence | block | The exact recorded rollback Markdown-first command fails when rerun literally, so the recorded M4 rollback pass evidence needs correction. |

## No-Finding Rationale

Not applicable. This review has one material finding.

## Direct-Proof Gaps

- MP4 lacks a reproducible recorded rollback command sequence for the temporary text-only state.

## Milestone Handoff State

- Reviewed milestone: M4
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M4 resolution
- Next stage: review-resolution
- Final closeout readiness: not ready because M4 has an unresolved review finding and final holistic review, final verification, and PR handoff have not happened.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [Baduanjin Text-Only Rollback Proof](../rollback-proof.md)
