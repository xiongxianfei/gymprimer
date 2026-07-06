# M2 Bird Dog Page Audit

Audit date: 2026-07-06

Audited page: `exercises/bird-dog.md`

Slice scope: one selected exercise document from the fewer-than-five evaluation population.

## Decision

This M2 slice audits `exercises/bird-dog.md` and records its page-specific top-10 image candidate backlog.
It does not edit `exercises/bird-dog.md`, generate images, add prompt records, update `media/PROVENANCE.md`, or replace existing media.

Minimum-needed generated subset for this slice: zero images.

Reason: the current page already has one readable sequence image and the first page-specific audit did not identify a page-local issue that justifies generating media before M3 manual proof work.
The top-10 table remains backlog for future page-specific slices.

## Current Page State

| Field | Value |
|---|---|
| Current image count | 1 |
| Existing image | `media/exercises/bird-dog/bird-dog-sequence.png` |
| Existing image purpose | `key_movement_illustration` |
| Existing image decision | preserve |
| Replacement reason | none |
| Image-count exception needed | no |
| Muscle-attention images after this slice | 0 |
| Generated images selected in this slice | 0 |

## Section Coverage

| Section area | Audit result |
|---|---|
| Purpose | present |
| Setup | present |
| Movement | present |
| Muscle guidance | present |
| Easier and harder options | present |
| Safety notes | present |
| Sources | present |

## Source-Support Issues

No source-support issue is recorded in this M2 audit.
No image-adjacent Markdown is changed in this slice.

## Existing Image Decisions

| Image path | Decision | Reason |
|---|---|---|
| `media/exercises/bird-dog/bird-dog-sequence.png` | preserve | Existing sequence image remains readable and no concrete replacement reason is recorded. |

## Top-10 Candidate Table

| Rank | Candidate image | Page section supported | Purpose | Why it matters | Score | Disposition |
|---:|---|---|---|---|---:|---|
| 1 | Setup stance reference showing hands under shoulders and knees under hips | Setup | `exercise_setup_illustration` | Could clarify starting alignment for beginners. | 20 | candidate backlog |
| 2 | Broad trunk and hip muscle-attention reference | Muscles involved | `exercise_muscle_attention_illustration` | Could help readers notice broad trunk and hip effort without exact anatomy labels. | 18 | candidate backlog |
| 3 | Movement path reference showing opposite arm and leg reach | Movement breakdown | `exercise_movement_illustration` | Could supplement the existing sequence image with a cleaner single movement path. | 17 | candidate backlog |
| 4 | Easier version reference showing shorter reach | Make it easier | `exercise_movement_illustration` | Could show how to reduce range without changing the exercise goal. | 15 | candidate backlog |
| 5 | Stability cue reference showing level hips | Common mistakes | `exercise_movement_illustration` | Could clarify a common control cue if reader feedback shows confusion. | 14 | candidate backlog |
| 6 | Hand pressure setup reference | Setup | `exercise_setup_illustration` | Useful but lower priority than whole-position setup. | 12 | later candidate |
| 7 | Knee and hip spacing setup reference | Setup | `exercise_setup_illustration` | Useful only if future audit finds setup wording unclear. | 11 | later candidate |
| 8 | End-position side view reference | Movement breakdown | `exercise_movement_illustration` | Could show reach length but overlaps with existing sequence image. | 10 | later candidate |
| 9 | Common overreach comparison-free reference | Common mistakes | `exercise_movement_illustration` | Lower priority because the page can explain range with text. | 9 | later candidate |
| 10 | Breathing and pause cue reference | Movement breakdown | `exercise_movement_illustration` | Low visual value compared with text explanation. | 7 | later candidate |

## Scoring Notes

Scores use the approved five-field model: beginner comprehension, setup value, muscle-attention value, page value, and readiness.
Each field is scored from 1 to 5.
The top-10 candidate table records the total score.
The scoring matrix records the five required per-candidate scoring fields.

## Scoring Matrix

| Rank | Beginner comprehension | Setup value | Muscle-attention value | Page value | Readiness | Total score |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 2 | 4 | 4 | 20 |
| 2 | 4 | 1 | 5 | 4 | 4 | 18 |
| 3 | 4 | 2 | 2 | 5 | 4 | 17 |
| 4 | 3 | 3 | 1 | 4 | 4 | 15 |
| 5 | 3 | 1 | 2 | 4 | 4 | 14 |
| 6 | 3 | 4 | 1 | 2 | 2 | 12 |
| 7 | 2 | 4 | 1 | 2 | 2 | 11 |
| 8 | 2 | 1 | 1 | 4 | 2 | 10 |
| 9 | 2 | 1 | 1 | 3 | 2 | 9 |
| 10 | 2 | 1 | 1 | 2 | 1 | 7 |

## Generation Decision

| Field | Value |
|---|---|
| Decision | no generation needed in M2 |
| Selected count | 0 |
| Selected purposes | none |
| Rationale | Current Markdown plus the existing sequence image are sufficient for this first page-specific audit slice. |
| Top-five treatment | candidate backlog only |
| Candidate 6-10 treatment | deferred |

## Validation Expectations

- `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard tests.test_markdown_first_real_pages`
- `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
- `python3 tools/checks/check_privacy.py -- exercises media docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization`
- `git diff --check`

## Rollback Path

No page or media rollback is needed for this M2 slice because it does not change page content or media files.
If this audit evidence is rejected, remove this evidence file and keep `exercises/bird-dog.md` unchanged.

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `exercises/bird-dog.md`
