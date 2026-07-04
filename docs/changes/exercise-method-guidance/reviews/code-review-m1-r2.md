# Code Review M1 R2: Exercise Method Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-method-guidance/reviews/code-review-m1-r2.md`, `docs/changes/exercise-method-guidance/review-log.md`, `docs/changes/exercise-method-guidance/review-resolution.md`, `docs/changes/exercise-method-guidance/change.yaml`, `docs/plans/2026-07-04-exercise-method-guidance.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/code-review-m1-r2.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: `docs/changes/exercise-method-guidance/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3, M4, Lifecycle Closeout
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review status

clean-with-notes

## Review inputs

- Diff/review surface: commit `f388d09` (`M1: resolve exercise method validator findings`) against prior code-review findings CR-EMG-M1-1 and CR-EMG-M1-2.
- Tracked governing branch state: current branch contains the accepted proposal, approved focused spec, approved architecture update, approved plan, active test spec, M1 implementation, M1 R1 code-review, M1 review-resolution commit, and later learning-only commit `565609e`.
- Governing artifacts: `specs/exercise-method-guidance.md`, `specs/exercise-method-guidance.test.md`, `docs/architecture/system/architecture.md`, `docs/plans/2026-07-04-exercise-method-guidance.md`.
- Prior review and resolution artifacts: `docs/changes/exercise-method-guidance/reviews/code-review-m1-r1.md`, `docs/changes/exercise-method-guidance/review-resolution.md`.
- Validation evidence run during this review:
  - `python3 -m unittest tests.test_exercise_method_guidance` passed, 9 tests.
  - `python3 -m unittest discover -s tests -p 'test_markdown_first*.py'` passed, 52 tests.
  - Direct proof script returned `exercise_method_missing_section` for `## How much to do wrong`.
  - Direct proof script returned five `exercise_method_empty_label` findings for empty required labels including `Beginner starting point:`.

## Diff summary

The resolution commit adds method-specific exact-heading parsing in `tools/checks/check_markdown_first.py`, preserves visible Markdown as the source of truth, and distinguishes missing required method labels from labels with no text after the colon. It adds focused regression tests for a non-exact method heading and for empty required labels, including `Beginner starting point:`.

The commit also updates workflow state from review-resolution back to M1 review-requested before this re-review.

## Prior finding reconciliation

| Finding | Result | Evidence |
| --- | --- | --- |
| CR-EMG-M1-1 | resolved | `exact_method_section_text` matches only `^## How much to do$`, malformed heading `## How much to do wrong` returns stable category `exercise_method_missing_section`, and `test_method_section_heading_must_be_exact` covers the regression. |
| CR-EMG-M1-2 | resolved | `method_label_content` parses label lines and `validate_exercise_method_guidance` emits `exercise_method_empty_label` when label content is blank; `test_required_method_labels_must_have_content` covers empty `Beginner starting point:`, `Effort:`, `Rest:`, `Progression:`, and `Stop if:`. |

## Findings

No blocking or required-change findings.

## Checklist coverage

| Area | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R1 requires exact `## How much to do`; the checker now uses an exact-heading extractor and rejects prefixed non-exact headings. R6/R37/R38 require visible labels and stable categories; empty labels now fail with `exercise_method_empty_label`. |
| Test coverage | pass | Focused tests cover valid sections, unselected pages, missing fields, exact heading failure, empty labels, inactive method types, hidden metadata, forbidden adaptive/treatment language, and compatibility-note assertions. |
| Edge cases | pass | Named edge cases from R1 review have direct proof: malformed heading and empty `Beginner starting point:` both fail with stable method categories. |
| Error handling | pass | Invalid method-section shapes return existing `Finding` objects with file path and stable category; no exception-prone parsing path was introduced. |
| Architecture boundaries | pass | The change keeps method guidance in visible Markdown and does not introduce hidden metadata, generated data, taxonomy files, runtime behavior, or a second source of truth. |
| Compatibility | pass | Unselected pages without a method section still pass the method contract, preserving the additive migration behavior required by R41. |
| Security/privacy | pass | The implementation only parses Markdown content and adds no secrets, user input flow, logging, auth, network, or private-data surface. |
| Derived artifact currency | pass | No generated artifacts are introduced or required for M1. |
| Unrelated changes | pass | The reviewed implementation changes are limited to the checker, focused tests, and workflow state for M1 review-resolution. |
| Validation evidence | pass | Focused and Markdown-first unittest suites passed during review; direct proof outputs matched the required stable categories. |

## No-finding rationale

The two prior material issues are fixed at the validator boundary and covered by focused tests. The implementation now enforces the exact method heading expected by R1 and fails empty required label lines with a stable category, satisfying the requested checker behavior without changing the approved Markdown-first architecture or expanding M1 scope.

## Residual risks

M1 only proves the template and validation contract. Source semantics, real proof-slice exercise pages, pattern preview alignment, manual source audit, beginner comprehension evidence, and final validation remain assigned to M2, M3, M4, and Lifecycle Closeout.

## Milestone handoff

M1 is closed by this review. The next workflow stage is implementation of M2, the sets/reps/holds/rest/progression principle page. Final closeout is not ready because M2, M3, M4, explain-change, verification, and PR handoff remain.
