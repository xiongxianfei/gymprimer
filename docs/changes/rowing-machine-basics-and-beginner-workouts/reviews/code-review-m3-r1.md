# Code Review M3 R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m3-r1.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M3
- Milestone closeout: closed
- Remaining implementation milestones: M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `4f3daa5`, especially
  `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/source-audit.md`,
  `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/beginner-comprehension.md`,
  `docs/changes/rowing-machine-basics-and-beginner-workouts/manual-proof/media-decision.md`,
  `exercises/rowing-machine.md`, `tools/checks/check_markdown_first.py`,
  `tests/test_exercise_image_standard.py`, and the exercise-image M4 audit row.
- Tracked governing branch state: commit `4f3daa5` includes the accepted
  proposal, approved spec, approved architecture update, active plan, active
  test spec, M1/M2 clean code-reviews, and M3 validation notes.
- Governing artifacts:
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `specs/exercise-image-standard.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/architecture/system/architecture.md`
- Validation evidence:
  - plan validation notes for M3;
  - independent reviewer rerun of
    `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises media`;
  - independent reviewer rerun of
    `python3 tools/checks/check_privacy.py exercises media docs/changes/rowing-machine-basics-and-beginner-workouts`;
  - independent reviewer rerun of
    `python3 -m unittest discover -s tests -p 'test_*image*.py'`;
  - independent reviewer rerun of
    `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`;
  - independent reviewer rerun of `git diff --check`;
  - direct external source check for the Concept2 muscles-used source added in
    M3.

## Diff Summary

M3 records the required manual source audit, beginner-comprehension proof, and
text-only media decision for `exercises/rowing-machine.md`. It adds a nearby
page-local Concept2 muscles-used citation to support the muscles section,
records that no unresolved visual comprehension gap requires rowing media, and
adds a text-only inventory row for the rowing page in the exercise-image M4
audit.

The implementation also narrows Markdown-first page scanning so
`media/prompts/` Markdown prompt records are not treated as reader-facing
content pages. `tests/test_exercise_image_standard.py` adds a regression where a
prompt record containing exercise-image prompt language is ignored by the page
checker while prompt-record contract tests remain in the image-standard suite.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M3 plan requirements R28-R36 and AC5-AC7 require source audit, comprehension evidence, media decision, and optional media only when needed. The three manual proof files record those decisions, and no media is added. |
| Test coverage | pass | The new prompt-record skip regression in `tests/test_exercise_image_standard.py` covers the M3 validator boundary. Existing prompt-record contract tests still cover generated raster prompt records through provenance validation. |
| Edge cases | pass | `media-decision.md` handles the no-image path by linking source-audit and beginner-comprehension evidence. `RMB-M4` visual-safety evidence remains explicitly conditional because no rowing media was added. |
| Error handling | pass | The checker still reports missing paths and page-validation errors; the new skip is limited to repository-relative `media/prompts/` Markdown records. |
| Architecture boundaries | pass | The change remains Markdown-first content, manual proof, local tests, and a checker boundary; it adds no hosted app, tracker, calculator, user-input flow, or generated image asset. |
| Compatibility | pass | The prompt-record path shape stays aligned with `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`. Prompt records remain validated by the exercise-image contract instead of reader-facing page checks. |
| Security/privacy | pass | Manual proof records state that no private reader, health, contact, or training-log data is recorded. The reviewer reran the privacy scan successfully. |
| Derived artifact currency | pass | The exercise-image audit now includes `exercises/rowing-machine.md` as text-only accepted, matching the current no-media state. No provenance row or prompt record is required. |
| Unrelated changes | pass | The diff is limited to M3 proof, the rowing muscles citation, prompt-record page-scan handling, image-standard regression coverage, and required lifecycle records. |
| Validation evidence | pass | Reviewer reran the M3 Markdown-first check, privacy scan, image-standard tests, Markdown-first tests, and whitespace check; all passed. |

## No-Finding Rationale

The manual source audit covers the M3 claim categories named by the test spec,
including setup, stroke sequence, damper, beginner method, weekly activity,
stop conditions, muscle wording, and static examples. The added Concept2
muscles-used source directly supports rowing as a coordinated full-body action
using legs, glutes, trunk/core, back, shoulders, and arms; the page frames
`upper back, lats, and arms` as broad exercise literacy rather than a precise
muscle-activation claim.

The comprehension record answers every required beginner-read question without
recording private data, and the media decision is traceable to that evidence.
Because the decision is text-only, the absence of `media/exercises/rowing-machine/`,
`media/PROVENANCE.md` changes, prompt records, and visual-safety review is
consistent with the approved test spec.

The checker change is also scoped: it prevents support prompt records from
failing reader-facing content checks while leaving generated raster prompt
records under the exercise-image provenance tests. The regression proves the
named failure mode that appeared during M3 validation.

## Residual Risks

M4 still needs the full integration validation ledger and lifecycle evidence.
This review does not claim final verification, branch readiness, PR readiness,
hosted CI success, or completion of M4.
