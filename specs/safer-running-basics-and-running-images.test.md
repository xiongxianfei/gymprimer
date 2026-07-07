# Test Spec: Safer Running Basics and High-Quality Running Images

Status: active

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Feature spec: `specs/safer-running-basics-and-running-images.md`

Plan: `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`

## Purpose

This proof map defines the automated and manual evidence required before `exercises/safer-running-basics.md` and its first governed image batch can be accepted.

## Requirement Coverage

| Requirement | Proof IDs |
|---|---|
| R1 Page identity | T1, T2, CMD3 |
| R2 Required sections | T1, CMD3 |
| R3 Method and progression | T3, CMD1, CMD3 |
| R4 Warm-up and form guidance | T4, CMD3, MP1 |
| R5 Muscle and feel guidance | T5, CMD3, MP1 |
| R6 Common mistakes and variants | T6, CMD3, MP1 |
| R7 Image-count exception | T7, CMD2, CMD3 |
| R8 Required first-batch image assets | T8, CMD2, CMD3, CMD4 |
| R9 Image prioritization evidence | T9, MP2 |
| R10 Image safety and provenance | T10, CMD2, CMD3, CMD4, MP2 |
| R11 Source and safety boundaries | T11, CMD3, CMD4, MP1 |
| R12 Verification evidence | T12, MP2, MP3, CMD5, CMD6 |

## Automated Proof IDs

### T1. Page heading and section contract

Type: automated

Milestone: M1, M2

The test MUST fail until `exercises/safer-running-basics.md` exists with:

- H1 `# Safer Running Basics`;
- the required alias line;
- all required headings from R2.1;
- a page-local `## Sources` section.

### T2. Injury-free alias boundary

Type: automated

Milestone: M1, M2

The test MUST confirm that `injury-free running` appears only as alias/search language and that `# Injury-Free Running` is not used as the page title.

### T3. Method and beginner progression

Type: automated

Milestone: M1, M2

The test MUST confirm that the page uses `Method type: basic_cardio_activity` and includes run/walk, easy effort, rest days, gradual progression, and the rule against adding distance, speed, hills, and running days all at once.

### T4. Warm-up and form cues

Type: automated

Milestone: M2

The test MUST confirm that the page includes a short warm-up recommendation and non-dogmatic form cues for tall posture, relaxed shoulders, natural arm swing, shorter steps, quiet landing, easy effort, and avoiding a forced foot strike.

### T5. Muscles and feel

Type: automated

Milestone: M2

The test MUST confirm that the page includes a `Muscles involved` table covering the role groups in R5.2 and a `What you should feel` section covering warm effort, leg work, relaxed upper-body areas, and safety routing. [Mayo Clinic][mayo-exercise-chronic-disease]

### T6. Common mistakes and variants

Type: automated

Milestone: M2

The test MUST confirm that common mistakes, easier version, and harder version sections satisfy R6 without adding race programming or hard performance intervals.

### T7. Six-image exception

Type: automated

Milestone: M1, M3

The test MUST confirm that this page is the only page using this specific six-image exception and that the first implementation references no more than the six approved image paths.

### T8. Media records and exact asset paths

Type: automated

Milestone: M1, M3

The test MUST confirm exact correspondence among:

- page image references;
- `media/exercises/safer-running-basics/*.png` assets;
- `media/prompts/exercises/safer-running-basics/*.md` prompt records;
- approved `media/PROVENANCE.md` rows.

### T9. Top-10 ranking preservation

Type: automated or structured manual check

Milestone: M3

The proof MUST confirm that implementation evidence preserves the approved top-10 image ranking and does not promote candidates 7 through 10 into the first batch.

### T10. Image purpose and safety metadata

Type: automated plus manual support

Milestone: M3

The test MUST confirm that the six image purposes match R8.1, that exactly one image is `exercise_muscle_attention_illustration`, and that prompt records include review criteria for no in-image text, labels, badges, brand marks, identifiable people, medical framing, pain marks, or correct/wrong framing.

### T11. Sources and shared registry

Type: automated

Milestone: M2, M3

The test MUST confirm page-local citations, required shared source registration, and no unsupported safety or progression claims.

### T12. Workflow handoff evidence

Type: automated or checklist

Milestone: M4

The final implementation handoff MUST include exact local validation commands, results, manual review paths, and a statement that CI was not claimed unless observed.

## Manual Proof IDs

### MP1. Source support audit

Milestone: M2, M4

Reviewer MUST confirm that warm-up, frequency, progression, form, safety routing, adult activity guidance, and evidence-limit claims are supported by page-local citations and `SOURCES.md` entries where required.

### MP2. Visual-safety review

Milestone: M3, M4

Reviewer MUST inspect all six images and record whether each one:

- teaches one distinct concept;
- avoids in-image text, labels, badges, red pain marks, medical framing, brand marks, and identifiable people;
- keeps the overstride comparison neutral;
- keeps muscle highlighting broad and subtle;
- matches its alt text and prompt record.

### MP3. Beginner comprehension proof

Milestone: M4

Reviewer MUST record whether a beginner can answer:

- what the page can help them do;
- whether the page can guarantee injury-free running;
- how to start a first running session;
- what run/walk means;
- what effort should feel like;
- what the posture image teaches;
- what the landing image teaches;
- what would make them stop or seek help. [Mayo Clinic][mayo-exercise-chronic-disease]

### MP4. Rollback proof

Milestone: M4

Reviewer MUST confirm that failed images can be removed cleanly by deleting page references and corresponding prompt/provenance records, and that the page remains useful as a text-backed primer.

## Validation Commands

CMD1:

```bash
python3 -m unittest tests.test_exercise_method_guidance
```

CMD2:

```bash
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
```

CMD3:

```bash
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
```

CMD4:

```bash
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images
```

CMD5:

```bash
python3 -m unittest discover -s tests
```

CMD6:

```bash
git diff --check
```

Workflow-artifact-only validation before implementation:

```bash
python3 tools/checks/check_markdown_first.py SOURCES.md docs/proposals/2026-07-06-safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.test.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images
python3 tools/checks/check_privacy.py SOURCES.md docs/proposals/2026-07-06-safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.md specs/safer-running-basics-and-running-images.test.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images
git diff --check
```

## Milestone Mapping

| Milestone | Required proof before handoff |
|---|---|
| M1 Validation and Contract Fixtures | T1, T2, T3, T7, T8 tests fail for missing production artifacts or pass against fixtures as appropriate |
| M2 Markdown Page and Source Contract | T1 through T6, T11, CMD1, CMD3, CMD4, MP1 |
| M3 Governed Image Batch | T7 through T10, CMD2, CMD3, CMD4, MP2 |
| M4 Comprehension Proof and Final Readiness | T12, MP3, MP4, CMD5, CMD6 |

## Fixtures and Evidence Paths

Expected evidence paths:

- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/visual-safety-review.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/beginner-comprehension-proof.md`
- `media/prompts/exercises/safer-running-basics/posture.md`
- `media/prompts/exercises/safer-running-basics/landing.md`
- `media/prompts/exercises/safer-running-basics/run-walk.md`
- `media/prompts/exercises/safer-running-basics/warm-up.md`
- `media/prompts/exercises/safer-running-basics/muscle-attention.md`
- `media/prompts/exercises/safer-running-basics/overstride-comparison.md`

Temporary fixtures MAY be added under the existing test fixture structure when they make M1 checks clearer. Fixtures MUST NOT be treated as production content.

## Exit Criteria

The implementation is ready for code-review only when:

- all automated checks required for the completed milestone pass;
- visual-safety review and beginner comprehension proof are recorded;
- every generated raster image has a prompt record and approved provenance row;
- the page remains within the accepted beginner education scope;
- the implementation handoff reports exact command results.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- [Mayo Clinic exercise and chronic disease guidance][mayo-exercise-chronic-disease]

[mayo-exercise-chronic-disease]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-and-chronic-disease/art-20046049
