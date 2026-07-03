# Code Review M3 R1: Exercise Image Standard

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3-r1.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EIS-M3-1, CR-EIS-M3-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3 resolution, M4, lifecycle closeout
- Required review-resolution: yes
- Finding IDs: CR-EIS-M3-1, CR-EIS-M3-2
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M3 commit `4b3b36d`, with focus on the five target exercise pages, five new PNG assets under `media/exercises/`, `media/PROVENANCE.md`, M3 visual-safety and beginner-comprehension evidence, and `tests/test_exercise_image_standard.py`.
- Tracked governing branch state: accepted proposal, approved spec, approved architecture/ADR, active plan, approved test spec, M1 and M2 code-review closeout, and M3 review-requested state are present in tracked branch state.
- Governing artifacts: `specs/exercise-image-standard.md`, `specs/exercise-image-standard.test.md`, and `docs/plans/2026-07-03-exercise-image-standard.md`.
- Validation evidence inspected: M3 validation notes in the active plan and reviewer-rerun command output listed below.

## Diff summary

M3 adds one generated movement image each to `exercises/chin-nod.md`, `exercises/thoracic-extension.md`, `exercises/wall-slide.md`, `exercises/prone-y-t.md`, and `exercises/band-pull-apart.md`. It adds the corresponding PNG assets, five approved `exercise_movement_illustration` provenance rows, M3 visual-safety and beginner-comprehension evidence files, focused test coverage, and lifecycle handoff updates.

Automated tests and static checks pass, but two manual-review obligations are not satisfied.

## Findings

## Finding CR-EIS-M3-1

- Finding ID: CR-EIS-M3-1
- Severity: major
- Location: `media/exercises/wall-slide/movement.png`, `exercises/wall-slide.md`, `docs/changes/exercise-image-standard-and-optimization/evidence/m3-visual-safety-review.md`
- Evidence: `exercises/wall-slide.md` describes the forearms-on-wall variation: "Place the forearms against the wall with the elbows bent" and "Slide the forearms upward on the wall." The new image primarily shows hands/palms contacting the wall, not forearms flat against the wall, while the visual-safety evidence records `Matches nearby Markdown` as `pass` and the alt text says "forearms sliding upward on a clear wall."
- Required outcome: The wall-slide image and evidence must truthfully match the forearms-on-wall variation, or the image must be removed from the page until a matching asset exists.
- Safe resolution path: Regenerate or replace `media/exercises/wall-slide/movement.png` with a visual where the forearms are clearly the wall contact point in both positions, then update provenance prompt notes if needed, re-inspect visual-safety evidence, rerun M3 validation, and return M3 to `review-requested`.
- needs-decision rationale: none.
- auto_fix_class: none.

## Finding CR-EIS-M3-2

- Finding ID: CR-EIS-M3-2
- Severity: major
- Location: `docs/changes/exercise-image-standard-and-optimization/evidence/m3-beginner-comprehension.md`
- Evidence: The approved test spec says M3 is a material exercise-image batch and EIS-T11 requires EIS-RO3 with "non-identifying reader prompts" and per-page outcomes for purpose, setup/body position, movement steps, what to notice or feel, stop condition, and source verification. The M3 evidence states its method was a "non-identifying maintainer checklist against each page, image, alt text, and nearby Markdown," which proves an internal artifact review, not a reader-prompt comprehension check.
- Required outcome: M3 must include beginner-comprehension evidence that satisfies EIS-T11/EIS-RO3 for this material batch, or the governing test spec/plan must be revised and reviewed before accepting a maintainer-only checklist.
- Safe resolution path: Run and record a non-identifying reader-prompt check for the five-page batch using the approved prompts, preserve per-page outcomes and residual confusion without private health information, rerun scoped privacy validation, and return M3 to `review-requested`.
- needs-decision rationale: none if the reader-prompt check is performed; owner/spec decision is needed only if the project wants maintainer-only checklist evidence to count for material image batches.
- auto_fix_class: none.

## Checklist coverage

- Spec alignment: concern. R2/R3/R28 are preserved in nearby Markdown, and provenance/path/purpose requirements are mostly satisfied, but CR-EIS-M3-1 blocks R30 visual evidence fidelity for the wall-slide image and CR-EIS-M3-2 blocks R31 beginner-comprehension evidence for the material batch.
- Test coverage: concern. `tests/test_exercise_image_standard.py` proves expected page references, asset existence, provenance shape, and evidence-file existence, but it cannot prove visual match or reader-prompt evidence quality.
- Edge cases: concern. The material batch edge case for beginner-comprehension evidence is not satisfied because the evidence is a maintainer checklist rather than reader-prompt outcomes. The wall-slide variation-specific visual edge case is not satisfied.
- Error handling: pass. No new runtime or parser error path is introduced; invalid media/provenance states remain covered by the checker tests.
- Architecture boundaries: pass. The diff stays within Markdown pages, repository-local media, central provenance, tests, and change-local evidence; no hosted app, CMS, database, user input, JSON API, video path, or coaching behavior is introduced.
- Compatibility: pass. Existing exercise images and legacy media-purpose rows are not migrated or changed.
- Security/privacy: pass. The scoped privacy check passed, and the evidence files avoid private health details and identifying private reader information.
- Derived artifact currency: concern. The visual-safety evidence marks wall-slide `Matches nearby Markdown` as `pass`, but the inspected image does not match the page variation closely enough.
- Unrelated changes: pass. The M3 diff is scoped to the first image batch, its evidence, tests, and lifecycle state.
- Validation evidence: pass for automated checks, concern for manual proof. Reviewer-rerun automated validation passed; the findings are from visual and requirement-fidelity review that static checks cannot prove.

## Direct-proof gaps

- CR-EIS-M3-1 is a direct visual-inspection failure against `exercises/wall-slide.md` and R30.
- CR-EIS-M3-2 is a direct proof-gap against EIS-T11/EIS-RO3 because the recorded method names a maintainer checklist rather than a non-identifying reader-prompt process.

## Validation run during review

- `python3 -m unittest tests.test_exercise_image_standard` passed with 8 tests.
- `python3 -m unittest discover tests` passed with 97 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` passed, checking 25 Markdown files.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md docs/changes/exercise-image-standard-and-optimization exercises media/PROVENANCE.md` passed, checking 39 files.
- `git diff --check` passed.

## Milestone handoff state

- Reviewed milestone: M3
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M3 resolution, M4, lifecycle closeout
- Next stage: review-resolution for CR-EIS-M3-1 and CR-EIS-M3-2
- Final closeout readiness: not ready because M3 has unresolved findings, and M4, final explain-change, final verification, and PR handoff remain open.
