# Code Review R3: M2 First Top-Five Image Batch

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r3.md`, `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-log.md`, `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`, `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/change.yaml`, `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-T5IMG-M2-1, CR-T5IMG-M2-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/code-review-r3.md`
- Review log: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-log.md`
- Review resolution: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2, M3
- Required review-resolution: yes
- Finding IDs: CR-T5IMG-M2-1, CR-T5IMG-M2-2
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `610bb6c` (`M2: implement first top-five image batch`)
- Governing spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Test spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- Plan: `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- M2 audit evidence: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md`
- Tests inspected: `tests/test_exercise_image_standard.py`, `tests/test_exercise_document_image_prioritization.py`
- Validator inspected: `tools/checks/exercise_document_image_prioritization.py`
- Visual evidence inspected: six promoted M2 PNG assets under `media/exercises/band-pull-apart/` and `media/exercises/bird-dog/`
- Validation evidence inspected: M2 validation notes in the plan and reviewer rerun of the broader CMD3 privacy command

## Diff Summary

M2 adds generated-image support for `exercises/band-pull-apart.md` and `exercises/bird-dog.md`.
The diff adds six generated PNG assets, six prompt records, six `media/PROVENANCE.md` rows with blank `human_reviewer`, page image references, an M2 audit artifact, and a real-page regression test for the first batch.
The plan and change metadata route M2 to code review.

## Findings

## Finding CR-T5IMG-M2-1

- Finding ID: CR-T5IMG-M2-1
- Severity: major
- Location: `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md:19`
- Evidence: Spec R10 requires candidate scoring fields to be scored from 1 to 5. The M2 audit instead says scores use 0-3 values, and the candidate rows include multiple `0` values at lines 26-30 and 41-45. The validator and M1 fixture still enforce the 1-5 range, so the M2 manual evidence no longer matches the approved scoring contract.
- Required outcome: Revise the M2 candidate scoring matrix to use 1-5 scores for every required score field, or revise the approved spec before relying on a different scale.
- Safe resolution path: Update the audit scale text and every M2 candidate score to the approved 1-5 range, then extend or adjust `test_top_five_m2_first_batch_has_page_images_prompt_records_and_audit_evidence` so it fails if M2 evidence reintroduces `0` scores or non-1-5 scale text. Rerun the M2 validation commands.
- needs-decision rationale: none

## Finding CR-T5IMG-M2-2

- Finding ID: CR-T5IMG-M2-2
- Severity: major
- Location: `media/exercises/bird-dog/short-reach.png`, referenced by `exercises/bird-dog.md:42` and justified by `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md:44`
- Evidence: The page and audit claim `short-reach.png` is a shorter-reach or smaller controlled reach image. Direct visual inspection shows a full arm and leg extension that is materially similar to `level-pelvis-reach.png`, not a shorter/easier range. This weakens the claim that bird dog has five distinct accepted images and conflicts with the R13/R23 requirement that images remain distinct support for the Markdown rather than carrying unsupported or duplicate page value.
- Required outcome: Replace `short-reach.png` with an image that visibly shows a smaller bird-dog range, or remove/downgrade the image and record a coverage-limit outcome below five for bird dog.
- Safe resolution path: Generate or select a new `short-reach.png` with visibly smaller arm and leg reach, update the prompt record selected-output notes and audit row if needed, visually inspect it, rerun M2 page/provenance tests and Markdown/privacy validation. If no distinct shorter-reach image is promoted, remove its page reference, provenance row, prompt record, and asset, then update the audit outcome and tests to reflect a four-image bird-dog coverage limit.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | block | CR-T5IMG-M2-1 violates R10's 1-5 score scale; CR-T5IMG-M2-2 undermines R13 distinct page value and R23 Markdown-support behavior. |
| Test coverage | concern | The new real-page test checks presence of score-field names but does not check the required 1-5 score range or catch the M2 evidence's `0` values. |
| Edge cases | concern | Coverage-limit behavior is present for band pull-apart, but bird dog's fifth image is accepted despite visual duplication of the full-reach movement purpose. |
| Error handling | pass | Prompt-record, provenance, image-path, and page-reference checks remain deterministic for missing or mismatched files. |
| Architecture boundaries | pass | Changes stay within Markdown pages, media assets, prompt records, provenance, tests, and change-local evidence. No hosted app, database, API, or runtime surface is added. |
| Compatibility | pass | Existing accepted images are preserved, and the reviewer exception remains scoped to blank `human_reviewer` rows for this named initiative. |
| Security/privacy | pass | Prompt records and provenance rows contain no secrets or private data in the inspected diff; reviewer reran the broader CMD3 command and it passed. |
| Derived artifact currency | concern | Plan and metadata reflect M2 review-requested, but the M2 audit evidence is stale against R10 and must be corrected before M2 can close. |
| Unrelated changes | pass | Commit `610bb6c` is scoped to M2 artifacts. Unrelated working-tree files `SOURCES.md` and `docs/proposals/2026-07-06-safer-running-basics-and-running-images.md` are outside the reviewed commit. |
| Validation evidence | concern | The implementation validation commands passed, and reviewer reran the broader CMD3 privacy command successfully, but tests did not cover the scoring-scale mismatch or image-purpose mismatch. |

## Validation Evidence

Implementation-reported validation from the plan:

- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed with 68 tests.
- `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- `python3 tools/checks/check_privacy.py exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed.
- `git diff --check` passed.

Reviewer rerun:

- `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed, checking 107 files.
- `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` passed, checking 32 Markdown files.
- `git diff --check` passed.

## Direct-Proof Gaps

- No test currently proves that M2 audit score values are in the approved 1-5 range.
- Automated checks cannot prove the visual claim that a generated image depicts a shorter reach; this review used direct visual inspection and the finding should be resolved with updated visual evidence.

## Milestone Handoff State

- Reviewed milestone: M2
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M2, M3
- Next stage: review-resolution for CR-T5IMG-M2-1 and CR-T5IMG-M2-2
- Final closeout readiness: not ready because M2 has unresolved findings and M3 remains pending.

## Recommendation

Route to review-resolution for M2.
Do not start M3 until these M2 findings are resolved and M2 passes rereview.

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.test.md`
- `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md`
- `tools/checks/exercise_document_image_prioritization.py`
- `tests/test_exercise_image_standard.py`
- `tests/test_exercise_document_image_prioritization.py`
