# Code Review M3A R3: Prompt Record Compatibility and Lifecycle State

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r3.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: code-review M3 re-review
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r3.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Reviewed milestone: M3A
- Milestone closeout: closed
- Remaining implementation milestones: M3 re-review/resolution, M4, lifecycle closeout
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commits after `2681df7`, especially `d15147e` and `818f832`, covering `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, `media/PROVENANCE.md`, `media/prompts/exercises/`, M3/M3A evidence, and lifecycle artifacts.
- Tracked governing branch state: approved prompt-record spec amendment, approved architecture/ADR, approved M3A plan and proof map, code-review M3A R1/R2, and review-resolution state for `CR-EIS-M3A-1` and `CR-EIS-M3A-2`.
- Governing artifacts: `specs/exercise-image-standard.md` R20-R20H, `specs/exercise-image-standard.test.md` EIS-T19 through EIS-T21, and `docs/plans/2026-07-03-exercise-image-standard.md` M3A.
- Validation evidence inspected: implementation validation notes in the active plan and change metadata; reviewer-rerun command output listed below.

## Diff summary

The resolution keeps the prompt-record compatibility bypass deterministic and scoped. Five assets remain on the explicit pre-amendment compatibility path because exact prompts are unavailable:

- `media/exercises/chin-nod/muscle-attention.png`
- `media/exercises/thoracic-extension/muscle-attention.png`
- `media/exercises/wall-slide/movement.png`
- `media/exercises/wall-slide/muscle-attention.png`
- `media/exercises/prone-y-t/muscle-attention.png`

Five CR-EIS-M3-2 replacement assets now leave the compatibility path and use normal prompt-record validation:

- `media/exercises/chin-nod/movement.png`
- `media/exercises/thoracic-extension/movement.png`
- `media/exercises/prone-y-t/movement.png`
- `media/exercises/band-pull-apart/movement.png`
- `media/exercises/band-pull-apart/muscle-attention.png`

The lifecycle artifacts now keep M3A in `review-requested` until this review, keep M3 out of final closeout, and record CR-EIS-M3-2 as addressed pending M3 re-review after owner clarity confirmation.

## Findings

None.

## Checklist coverage

- Spec alignment: pass. Non-blank `prompt_record` remains required for governed generated raster exercise images, while the compatibility path is restricted to explicitly recorded pre-amendment M3 assets.
- Test coverage: pass. `tests/test_exercise_image_standard.py` proves non-M3 blank prompt-record rows with the compatibility note fail, verifies the remaining compatibility rows, and verifies replacement rows have prompt-record paths.
- Edge cases: pass. Copied compatibility notes, blank prompt records, replacement assets, and prompt-backed replacements are covered directly.
- Error handling: pass. Missing prompt records fall through to `media_prompt_record_missing` unless both the compatibility note and allowlisted asset match.
- Architecture boundaries: pass. The change stays within static validation, provenance, prompt-record artifacts, and change-local lifecycle records; it adds no runtime, CMS, hosted media path, API, or coaching behavior.
- Compatibility: pass. The pre-amendment compatibility exception remains available only for the five recorded unreplaced assets; replacement assets now use the normal prompt-record contract.
- Security/privacy: pass. Prompt records are repository-local audit artifacts, not reader-facing exercise Markdown. Scoped privacy validation passed.
- Derived artifact currency: pass. `media/PROVENANCE.md`, prompt records, checker allowlist, tests, M3A backfill evidence, review-resolution, change metadata, plan, and plan index agree on the five compatibility assets and five prompt-backed replacements.
- Unrelated changes: pass. The reviewed diff is limited to M3A prompt-record compatibility, M3 clarity evidence, replacement assets, prompt records, and lifecycle routing for the same active change.
- Validation evidence: pass. Reviewer-rerun focused tests, Markdown checker, scoped privacy scan, and whitespace check passed.

## No-finding rationale

`CR-EIS-M3A-2` is resolved because the plan, plan index, change metadata, and review-resolution table no longer contradict the M3/M3A handoff. M3A can close, and M3 can return to code-review re-review next.

## Prior finding reconciliation

- `CR-EIS-M3A-1`: remains resolved. The compatibility bypass is scoped to recorded assets, and the test suite proves copied compatibility notes do not bypass prompt-record validation for other generated raster exercise images.
- `CR-EIS-M3A-2`: resolved. M3A lifecycle state is review-requested through this review, M3 is not marked closed or final, and the current handoff routes to M3 re-review after M3A closeout.

## Direct-proof gaps

None for M3A. M3 visual clarity and comprehension evidence is reviewed in the M3 re-review, not closed by this M3A review.

## Validation run during review

- `python3 -m unittest tests.test_exercise_image_standard` passed with 12 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` passed, checking 25 Markdown files.
- `python3 tools/checks/check_privacy.py -- docs/plan.md docs/plans/2026-07-03-exercise-image-standard.md docs/changes/exercise-image-standard-and-optimization media/PROVENANCE.md media/prompts tools/checks/check_markdown_first.py tests/test_exercise_image_standard.py exercises` passed, checking 54 files.
- `git diff --check HEAD` passed.

## Milestone handoff state

- Reviewed milestone: M3A
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M3 re-review/resolution, M4, lifecycle closeout
- Next stage: code-review M3 re-review
- Final closeout readiness: not ready because M3 still needs code-review re-review, and M4, explain-change, final verification, and PR handoff remain open.
