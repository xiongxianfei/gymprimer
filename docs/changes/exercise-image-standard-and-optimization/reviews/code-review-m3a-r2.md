# Code Review M3A R2: Prompt Record Compatibility Scope

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r2.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EIS-M3A-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r2.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Reviewed milestone: M3A
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3A resolution, M3 re-review/resolution, M4, lifecycle closeout
- Required review-resolution: yes
- Finding IDs: CR-EIS-M3A-2
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `b217f88` (`Resolve M3A prompt compatibility scope`), especially `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plan.md`, and `docs/plans/2026-07-03-exercise-image-standard.md`.
- Tracked governing branch state: approved prompt-record spec amendment, approved architecture/ADR, approved M3A plan and proof map, code-review M3A R1, and review-resolution state for `CR-EIS-M3A-1` are present in tracked branch state.
- Governing artifacts: `specs/exercise-image-standard.md` R20-R20H, `specs/exercise-image-standard.test.md` EIS-T19 through EIS-T21, and `docs/plans/2026-07-03-exercise-image-standard.md` M3A.
- Validation evidence inspected: CR-EIS-M3A-1 resolution validation notes in the active plan and change metadata; reviewer-rerun command output listed below.

## Diff summary

The resolution adds `PROMPT_RECORD_COMPATIBILITY_ASSETS` with the ten recorded M3 compatibility assets, requires the compatibility note and asset allowlist before bypassing prompt-record validation, and adds a regression proving a non-M3 generated exercise image with the compatibility note and blank `prompt_record` fails. It also updates review-resolution and lifecycle state for M3A re-review.

The checker and regression resolve `CR-EIS-M3A-1`. The lifecycle artifact updates, however, contain inconsistent milestone state.

## Findings

## Finding CR-EIS-M3A-2

- Finding ID: CR-EIS-M3A-2
- Severity: major
- Location: `docs/plans/2026-07-03-exercise-image-standard.md:274`, `docs/plans/2026-07-03-exercise-image-standard.md:322`
- Evidence: The plan still states `CR-EIS-M3-2 remains open` in the current handoff summary, and `review-resolution.md` still lists `CR-EIS-M3-2` as open. Despite that, the resolution diff changes the M3 milestone line to `Milestone state: review-requested` at `docs/plans/2026-07-03-exercise-image-standard.md:274`. Separately, the current handoff summary and `change.yaml` route M3A to code-review re-review, but the M3A milestone body still says `Milestone state: resolution-needed` at `docs/plans/2026-07-03-exercise-image-standard.md:322`. These states contradict each other and can misroute downstream workflow.
- Required outcome: The plan and compact metadata must consistently show M3A as the milestone under review or resolution, and must keep M3 in `resolution-needed` until `CR-EIS-M3-2` is actually resolved or superseded by reviewed upstream artifacts.
- Safe resolution path: Update the M3 milestone state back to `resolution-needed`; update the M3A milestone state, current handoff summary, `docs/plan.md`, and `change.yaml` to the correct post-resolution/pre-rereview state; keep `CR-EIS-M3-2` open; rerun scoped privacy and `git diff --check`; return M3A to `review-requested`.
- needs-decision rationale: none
- auto_fix_class: none

## Checklist coverage

- Spec alignment: pass for checker behavior, concern for lifecycle routing. The code change now preserves R20/R20A for non-M3 assets while allowing the recorded M3 compatibility path, but the plan state drift conflicts with the milestone-aware workflow contract.
- Test coverage: pass. `tests/test_exercise_image_standard.py` now proves a non-M3 compatibility-note asset fails and the recorded M3 compatibility rows remain present.
- Edge cases: pass for `CR-EIS-M3A-1`; concern for workflow state. The copied-note bypass is covered, but the M3/M3A state edge case needs artifact correction.
- Error handling: pass. Missing prompt-record handling now falls through to `media_prompt_record_missing` unless both the compatibility note and allowlisted asset match.
- Architecture boundaries: pass. The resolution stays inside checker, tests, and change-local workflow artifacts; it adds no runtime, CMS, hosted media, API, or generated JSON path.
- Compatibility: pass for media compatibility. Legacy image purposes remain valid, and the M3 pre-amendment compatibility path is now bounded to the recorded asset set.
- Security/privacy: pass. The reviewed diff does not expose secrets or private data, and scoped privacy validation passed in the implementation evidence.
- Derived artifact currency: concern. The lifecycle artifacts are not internally consistent because the M3 and M3A milestone states disagree with open findings and handoff text.
- Unrelated changes: concern. Changing M3 to `review-requested` is unrelated to resolving `CR-EIS-M3A-1` and conflicts with the still-open M3 finding.
- Validation evidence: pass for code behavior, concern for lifecycle artifact state. Reviewer-rerun focused tests and the checker passed, but static checks do not catch milestone-state drift.

## No-finding rationale

Not applicable; this review has one material finding.

## Prior finding reconciliation

- `CR-EIS-M3A-1`: resolved. The checker now requires both the compatibility note and membership in `PROMPT_RECORD_COMPATIBILITY_ASSETS` before accepting a blank `prompt_record`, and the new regression proves non-M3 copied-note rows fail.

## Direct-proof gaps

- No direct-proof gap remains for `CR-EIS-M3A-1`; the targeted regression and reviewer-rerun focused test cover it.
- `CR-EIS-M3A-2` is a direct artifact-state inconsistency visible in the plan and review-resolution table.

## Validation run during review

- `python3 -m unittest tests.test_exercise_image_standard` passed with 12 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` passed, checking 25 Markdown files.
- `git diff --check HEAD` passed.

## Milestone handoff state

- Reviewed milestone: M3A
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M3A resolution, M3 re-review/resolution, M4, lifecycle closeout
- Next stage: review-resolution for CR-EIS-M3A-2
- Final closeout readiness: not ready because M3A has an unresolved lifecycle artifact finding, M3 still has unresolved reader-prompt evidence, and M4, explain-change, final verification, and PR handoff remain open.
