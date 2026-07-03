# Test Spec: Exercise Image Standard

## Status

draft

## Related spec and plan

- Spec: `specs/exercise-image-standard.md`
- Spec reviews:
  - `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r1.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r2.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r3.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/spec-review-r4.md`
- Review resolution:
  - `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Plan: `docs/plans/2026-07-03-exercise-image-standard.md`
- Plan review:
  - `docs/changes/exercise-image-standard-and-optimization/reviews/plan-review-r1.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/plan-review-r2.md`
- Architecture/ADRs:
  - `docs/architecture/system/architecture.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r1.md`
  - `docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md`
  - `docs/adr/2026-07-03-exercise-document-image-purposes.md`
  - `docs/adr/2026-07-03-generated-raster-prompt-records.md`

## Testing strategy

The proof strategy uses existing Python `unittest` conventions, temporary-root
fixture repositories, real-repository integration checks, and manual review
evidence where image semantics cannot be proven mechanically.

- Unit: extend `tests/test_markdown_first_guardrails.py` or add
  `tests/test_exercise_image_standard.py` for generated raster provenance,
  media-purpose, alt-text, image-count, reviewer-field, template-context, and
  path failures. M3A extends this coverage for prompt-record path, file,
  reverse-match, exact-prompt, redaction, and compatibility failures.
- Integration: run `tools/checks/check_markdown_first.py` against fixture
  exercise pages, real `exercises/`, `media/PROVENANCE.md`, and the shared
  source/disclaimer surfaces.
- End-to-end: after an image batch, prove a reader can open exercise Markdown
  directly, see zero to three support images, and trace every generated raster
  image to exact approved provenance and review evidence.
- Smoke: assert text-only exercise pages still pass, existing legacy-compatible
  exercise images still pass, and no runtime, CMS, generated JSON, user-input
  flow, or README promotion appears.
- Manual: visual-safety review, broad-region muscle-attention review,
  source-of-truth review, and beginner comprehension evidence are recorded in
  change-local evidence and checked during code review.
- Contract: map every R1-R38 requirement, E1-E7 example, EC1-EC20 edge case,
  and AC1-AC12 acceptance criterion to automated tests or manual review.
- Migration: prove existing `equipment_identification` and
  `key_movement_illustration` exercise images remain valid without changing
  their media purpose. M3A also proves older generated raster exercise images
  can remain under the pre-amendment compatibility path only when downstream
  scope explicitly treats them as pre-amendment assets.

The source spec contains an identical duplicate `R24` line. This test spec
treats it as one behavioral requirement because the repeated text is identical.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | EIS-T1 | unit, integration | Text-only exercise pages pass without image references or provenance. |
| R2 | EIS-T9, EIS-T10, EIS-T12 | integration, manual | Images are support-only; Markdown remains the authority. |
| R3 | EIS-T9, EIS-T12 | integration, manual | Setup, movement, muscles, cues, caveats, safety notes, and citations remain in Markdown. |
| R4 | EIS-T10, EIS-T13 | manual | Minimum necessary image count is reviewed per batch and audit record. |
| R5 | EIS-T4 | unit, integration | Four exercise images fail unless an approved exception is represented. |
| R6 | EIS-T2, EIS-T10 | unit, manual | Purpose enum and visual review enforce one primary concept. |
| R7 | EIS-T2 | unit, integration | New generated raster exercise images must use one of three new purposes. |
| R8 | EIS-T2, EIS-T10 | unit, manual | Setup purpose is fixture-tested and manually checked for setup-only use. |
| R9 | EIS-T2, EIS-T10 | unit, manual | Movement purpose is fixture-tested and manually checked for movement-only use. |
| R10 | EIS-T2, EIS-T5, EIS-T10 | unit, manual | Muscle-attention purpose is fixture-tested and manually checked for broad-region use. |
| R11 | EIS-T5 | unit, integration | More than one muscle-attention image on a page fails. |
| R12 | EIS-T10 | manual | Broad, not precise, highlight is visual-review evidence. |
| R13 | EIS-T8, EIS-T10 | unit, manual | Deterministic unsafe text indicators fail; final visual semantics are reviewed manually. |
| R14 | EIS-T8, EIS-T10 | unit, manual | Clinical, pain, cure, brand, and identifying-person risks are reviewed manually with deterministic text support. |
| R15 | EIS-T6 | unit, integration | Remote and non-local Markdown image references fail. |
| R16 | EIS-T6, EIS-T13 | integration, manual | Subject-co-located paths are checked for new generated rasters and audited for existing pages. |
| R17 | EIS-T6 | unit, integration | New generated raster exercise images outside `media/exercises/<slug>/` fail. |
| R18 | EIS-T10, EIS-T13 | manual | Filename descriptiveness is reviewed in batch and audit evidence. |
| R19 | EIS-T3 | unit, integration | Generated raster images require exact approved provenance. |
| R20 | EIS-T3, EIS-T19 | unit, integration | Required non-blank provenance fields are checked, including `prompt_record` for governed generated raster exercise images. |
| R20A | EIS-T19 | unit, integration | Provenance `prompt_record` must be repository-local and point to a prompt record preserving the exact prompt. |
| R20B | EIS-T19 | unit, integration | Prompt records must live under `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`. |
| R20C | EIS-T20 | unit, integration | Prompt records must identify generated asset path, generator, created date, reviewer or owner, review status, and exact prompt text. |
| R20D | EIS-T20, EIS-T21 | manual, migration | Selected-output, rejected-variant, and revision notes are checked when they materially explain M3 backfill or replacement choices. |
| R20E | EIS-T20 | unit, manual | Exact prompt text must be preserved verbatim except required redaction. |
| R20F | EIS-T20 | unit, manual | Redactions must be explicit and reasoned without exposing unsafe or private content. |
| R20G | EIS-T19 | integration | Prompt records are not embedded in reader-facing exercise Markdown. |
| R20H | EIS-T19, EIS-T20 | unit, integration | `prompt_or_creation_notes` remains a summary and cannot substitute for the prompt record. |
| R21 | EIS-T3 | unit, integration | Generated raster exercise rows must use `asset_type = ai_generated_raster`. |
| R22 | EIS-T3 | unit, integration | Non-approved review status fails. |
| R23 | EIS-T3 | unit, integration | `page_refs` must include the referencing exercise page. |
| R24 | EIS-T3 | unit, integration | AI-tool reviewer values fail where deterministic reviewer validation is implemented. |
| R25 | EIS-T7 | unit, integration | Alt text must be present and exercise-specific. |
| R26 | EIS-T7 | unit, integration | Generic alt text fails. |
| R27 | EIS-T7, EIS-T10 | unit, manual | Muscle-attention alt text must match broad supported Markdown wording. |
| R28 | EIS-T8, EIS-T10, EIS-T11 | unit, manual | Diagnosis, treatment, cure, individualized coaching, and unsupported safety wording fail or block manual review. |
| R29 | EIS-T10 | manual | Every promoted exercise image needs visual-safety review. |
| R30 | EIS-T10 | manual | Visual-safety evidence must include all required review criteria. |
| R31 | EIS-T11 | manual | Material image batches need beginner comprehension evidence. |
| R32 | EIS-T14 | migration | Existing legacy-compatible exercise images remain valid. |
| R33 | EIS-T14 | migration | Existing exercise image purposes are not migrated. |
| R34 | EIS-T2 | unit, integration | Pattern, condition, preview, vague, and unknown purposes fail on full exercise pages. |
| R35 | EIS-T3, EIS-T4, EIS-T6, EIS-T7, EIS-T8, EIS-T19, EIS-T20 | unit, integration | Required validation failure cases are fixture-tested, including prompt-record failures. |
| R36 | EIS-T15, EIS-T19, EIS-T20 | contract | Failure output includes stable categories for the expected failure classes, including prompt-record failures. |
| R37 | EIS-T16, EIS-T20 | smoke | Privacy checker covers Markdown, provenance, prompt records, prompts or creation notes, review evidence, and validation output. |
| R38 | EIS-T17 | smoke, migration | Repository diff and smoke checks prove no hosted app, CMS, database, input flow, JSON API, video-first path, or coaching behavior. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | EIS-T1 | Text-only exercise fixture passes without provenance. |
| E2 | EIS-T2, EIS-T3 | Setup image fixture uses `exercise_setup_illustration` and matching `page_refs`. |
| E3 | EIS-T2, EIS-T10 | Movement image fixture passes purpose validation; visual review checks movement-only semantics when assets exist. |
| E4 | EIS-T5, EIS-T7, EIS-T10 | Muscle-attention fixture covers one-image limit, broad-region alt text, and manual visual review. |
| E5 | EIS-T4 | Four image references fail unless an explicit approved exception is represented. |
| E6 | EIS-T2 | `pattern_alignment_illustration` fails as a full exercise-document purpose. |
| E7 | EIS-T14 | Existing `equipment_identification` and `key_movement_illustration` exercise images pass without migration. |
| E8 | EIS-T19, EIS-T20 | A generated raster exercise image with a valid `prompt_record` link and reverse `asset_path` match passes prompt-record validation. |
| E9 | EIS-T19 | A generated raster exercise image with no non-blank `prompt_record` value fails prompt-record validation. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | EIS-T1 | integration | Exercise page with no images passes. |
| EC2 | EIS-T2, EIS-T3 | integration | One setup image passes with correct path, purpose, provenance, and alt text. |
| EC3 | EIS-T2, EIS-T3 | integration | Setup plus movement images pass when each has valid purpose and provenance. |
| EC4 | EIS-T2, EIS-T5 | integration | Setup, movement, and one muscle-attention image pass. |
| EC5 | EIS-T4 | unit | Four images fail without approved exception. |
| EC6 | EIS-T5 | unit | Two muscle-attention images fail. |
| EC7 | EIS-T3 | unit | Missing provenance row fails. |
| EC8 | EIS-T3 | unit | Missing required provenance fields fail. |
| EC8A | EIS-T19 | unit | Provenance row with no non-blank `prompt_record` fails for governed generated raster exercise images. |
| EC8B | EIS-T19 | unit | `prompt_record` outside the repository or outside the required path shape fails. |
| EC8C | EIS-T20 | unit | Prompt record whose internal `asset_path` differs from the generated raster asset path fails. |
| EC8D | EIS-T20 | unit | Prompt record missing exact full prompt text and lacking an explicit redaction note fails. |
| EC8E | EIS-T21 | migration | Older generated raster exercise image with unavailable exact prompt is routed to explicit compatibility limitation or replacement. |
| EC9 | EIS-T3 | unit | `needs_revision` or `rejected` fails. |
| EC10 | EIS-T3 | unit | Missing referencing exercise in `page_refs` fails. |
| EC11 | EIS-T2 | unit | Pattern, condition, or preview purposes fail on full exercise documents. |
| EC12 | EIS-T2 | unit | Vague purpose values fail. |
| EC13 | EIS-T14 | migration | Existing legacy-compatible purpose values remain valid without migration. |
| EC14 | EIS-T10 | manual | Precise anatomy or muscle labels fail visual-safety review. |
| EC15 | EIS-T8, EIS-T10 | unit, manual | Correct/wrong labels, text arrows, citations, and safety warnings fail deterministic or manual checks. |
| EC16 | EIS-T8, EIS-T10 | unit, manual | Pain marks, injury symbols, diagnosis, treatment, and cure framing fail deterministic or manual checks. |
| EC17 | EIS-T10, EIS-T16 | manual, smoke | Brand marks, identifiable people, and private data fail visual-safety or privacy review. |
| EC18 | EIS-T7 | unit | Missing or generic alt text fails. |
| EC19 | EIS-T8, EIS-T12 | unit, manual | Unsupported diagnosis, treatment, cure, or coaching wording fails. |
| EC20 | EIS-T6 | unit | Remote URL, path outside `media/`, unsupported extension, and missing local file fail. |

## Planned validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | Required starting | Expected failure behavior | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EIS-CMD1 | `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1` | existing and extended | tooling maintainer | M1 | M1 | Any unexpected nonzero exit fails M1. | M1 validation notes and code-review record. |
| EIS-CMD2 | `python3 -m unittest discover tests` | existing and extended | tooling maintainer | M1-M4 and M3A | M1 | Any unexpected nonzero exit fails the active milestone. | Milestone validation notes. |
| EIS-CMD3 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` | existing and extended | tooling maintainer | M1-M4 and M3A | M1 | Any unexpected nonzero exit fails the active milestone. | Milestone validation notes and verify report. |
| EIS-CMD4 | `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/exercise-image-standard-and-optimization docs/plans media exercises tools tests` | existing and configured | content/check maintainer | lifecycle closeout / verify | verify | Forbidden findings or setup errors fail final verification before PR handoff. M1-M4 and M3A may run narrower current-change privacy scans for review hygiene, but the broad repository privacy sweep is not an implementation-milestone closeout gate. | Verify report and PR handoff notes. |
| EIS-CMD5 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md` | planned for implementation | documentation/check maintainer | M1-M2 | M2 | From M2, any unexpected nonzero exit fails authoring-guidance closeout. M1 must add tests proving template context is not treated as promoted product content. | M1 template-context test evidence and M2 validation notes. |
| EIS-CMD6 | `python3 tools/checks/check_privacy.py -- docs/templates docs/changes/exercise-image-standard-and-optimization` | existing and configured | documentation/check maintainer | M2 | M2 | Forbidden findings or setup errors fail M2. | M2 validation notes. |
| EIS-CMD7 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md` | existing and extended | content/check maintainer | M3-M4 and M3A | M3 | Unexpected nonzero exit fails image-batch, prompt-record, or audit closeout. | M3/M3A/M4 validation notes. |
| EIS-CMD8 | `git diff --check` | existing and configured | release/check maintainer | M1-M4 and M3A | now | Any whitespace error fails the active milestone. | Milestone validation notes. |
| EIS-CMD9 | `python3 -m unittest tests.test_exercise_image_standard` | existing and extended | tooling maintainer | M3A | M3A | Any unexpected nonzero exit fails prompt-record implementation closeout. | M3A validation notes and code-review record. |

## Review-only semantic evidence

| Review ID | Automation rationale | Exact steps | Required environment | Evidence artifact | Pass condition | Failure condition | Owning stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EIS-RO1 | Static checks cannot prove that an image teaches exactly one concept or stays visually non-clinical. | Inspect every new exercise image and nearby Markdown; confirm one teaching concept, no in-image text, no labels, no red pain marks, no injury symbols, no correction/cure framing, no identifying person, no misleading brand, no unsupported visual claim, and color-accessibility. | Local checkout with final image assets renderable from `media/exercises/<slug>/`. | M3 code-review record and change-local visual-safety evidence. | Every reviewed image passes all criteria or is removed. | Any reviewed image fails a criterion or lacks evidence. | code-review |
| EIS-RO2 | Static checks cannot prove that muscle highlighting is broad rather than overprecise anatomy. | For every muscle-attention image, compare the visual highlight, alt text, and nearby Markdown; confirm broad region wording and no unsupported exact anatomy. | Local checkout with the final image and Markdown. | M3 code-review record and visual-safety evidence. | Highlight is broad and supported by nearby Markdown. | Highlight is overprecise, labeled, or unsupported. | code-review |
| EIS-RO3 | Static checks cannot prove that images improve beginner comprehension. | For a material image batch, record non-identifying beginner comprehension prompts and outcomes for purpose, setup/body position, movement steps, what to notice/feel, stop condition, and source verification. | Local checkout and non-identifying reader-test process. | Change-local beginner comprehension evidence and M3 code-review record. | Evidence records per-page outcomes and residual confusion without private health data. | Evidence is absent, only global approval, or contains private health information. | code-review |
| EIS-RO4 | Static checks can find citations, but not whether nearby image-adjacent claims are source-supported. | Sample image-adjacent setup, technique, muscle, feel-cue, mistake, and safety claims; verify each is supported by page-local sources or remove/recite the claim. | Local checkout with reviewed Markdown and public source links available. | M3 code-review record. | Sampled claims are supported by page-local sources or removed. | Unsupported image-adjacent claims remain. | code-review |

## Test cases

### EIS-T1. Text-only exercise pages remain valid

- Covers: R1, E1, EC1, AC2
- Level: integration
- Fixture/setup: Temporary repository with `SOURCES.md`, an exercise page under `exercises/`, and no image references or `media/PROVENANCE.md` row for that page.
- Steps: Run `check_markdown_first.py` through `run_check_with_root` against the exercise page.
- Expected result: The page passes exercise-image-specific media validation.
- Failure proves: The checker made images mandatory or tied text-only pages to media provenance.
- Automation location: `tests/test_exercise_image_standard.py` or `tests/test_markdown_first_guardrails.py`; `tools/checks/check_markdown_first.py`.

### EIS-T2. Exercise media-purpose enum and page-context rules

- Covers: R6, R7, R8, R9, R10, R34, E2, E3, E6, EC2, EC3, EC4, EC11, EC12, AC1, AC7
- Level: unit
- Fixture/setup: Temporary exercise pages and generated raster assets under `media/exercises/<slug>/` with approved provenance rows using each allowed and disallowed purpose.
- Steps: Run `check_markdown_first.py` for allowed setup, movement, and muscle-attention rows; rerun for pattern, condition, preview, vague, and unknown purpose rows.
- Expected result: Allowed exercise-specific purposes pass; disallowed full exercise-document purposes fail with `media_usage_out_of_scope` or the final stable purpose failure category.
- Failure proves: The checker cannot distinguish exercise-document media purposes from pattern, condition, preview, or vague media purposes.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T3. Generated raster provenance contract

- Covers: R19, R20, R21, R22, R23, R24, R35, EC7, EC8, EC9, EC10, AC5
- Level: unit
- Fixture/setup: Temporary exercise page references a generated raster image; provenance variants cover missing row, duplicate row, blank required fields, wrong `asset_type`, non-approved `review_status`, missing `page_refs`, and AI-tool `human_reviewer`.
- Steps: Run `check_markdown_first.py` over each provenance variant.
- Expected result: The valid row passes; every invalid variant fails with a stable provenance, approval, page-reference, or reviewer failure category.
- Failure proves: Generated raster exercise images can be promoted without traceable approved provenance or accountable human review.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T4. Exercise image count limit

- Covers: R4, R5, R35, E5, EC5, AC3
- Level: unit
- Fixture/setup: Exercise page fixtures with zero, one, two, three, and four image references; four-image fixture has no approved downstream exception.
- Steps: Run `check_markdown_first.py` on each fixture.
- Expected result: Zero to three image references pass when other media rules pass; four image references fail with a stable image-count failure category unless an approved exception fixture is explicitly represented.
- Failure proves: Image bloat can enter exercise pages without a governed exception.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T5. Muscle-attention image limit

- Covers: R10, R11, R35, E4, EC4, EC6, AC4
- Level: unit
- Fixture/setup: Exercise page fixtures with one and two generated raster images whose provenance rows use `exercise_muscle_attention_illustration`.
- Steps: Run `check_markdown_first.py` on both fixtures.
- Expected result: One muscle-attention image passes when other media rules pass; two muscle-attention images fail with a stable muscle-attention limit category.
- Failure proves: A page can accumulate multiple anatomy-style overlays despite the spec limit.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T6. Exercise image path and extension boundaries

- Covers: R15, R16, R17, R35, EC20
- Level: unit
- Fixture/setup: Exercise page fixtures reference a valid relative `../media/exercises/<slug>/setup.png`, a remote URL, a repository-local path outside `media/`, a generated raster outside `media/exercises/<slug>/`, an unsupported `.gif`, and a missing local file.
- Steps: Run `check_markdown_first.py` over each fixture.
- Expected result: Valid relative exercise media passes; remote, outside-media, wrong-bucket new generated raster, unsupported extension, and missing file fail with stable path, extension, or asset failure categories.
- Failure proves: Exercise images can bypass repository-local media and subject-co-located generated-raster boundaries.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T7. Exercise image alt-text contract

- Covers: R25, R26, R27, R35, E4, EC18, AC8
- Level: unit
- Fixture/setup: Exercise page fixtures with missing alt text, generic placeholders, exercise-specific setup/movement alt text, and muscle-attention alt text with broad supported region wording.
- Steps: Run `check_markdown_first.py` over each fixture.
- Expected result: Missing or generic alt text fails; exercise-specific alt text passes; muscle-attention alt text that overnames unsupported exact anatomy fails when deterministic wording can identify it or is routed to manual review.
- Failure proves: Images can be inaccessible or can smuggle unsupported anatomy through alt text.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`; EIS-RO2 for non-deterministic cases.

### EIS-T8. Unsafe image-adjacent wording guardrails

- Covers: R13, R14, R28, R35, EC15, EC16, EC19, AC9, AC11
- Level: unit
- Fixture/setup: Exercise image fixtures with alt text, captions, nearby Markdown, or provenance notes containing deterministic unsafe phrases such as diagnosis, treatment, cure, correct/wrong label framing, warning badges, pain marks, or personalized coaching.
- Steps: Run `check_markdown_first.py` over each fixture.
- Expected result: Deterministic unsafe wording fails with a stable visual-safety or purpose failure category.
- Failure proves: Image-adjacent text can carry clinical, corrective, or unsupported claims.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T9. Markdown remains source of truth near images

- Covers: R2, R3, R28, AC11
- Level: manual
- Fixture/setup: Use every exercise page modified in an image batch.
- Steps: During code review, inspect each image-adjacent section and verify setup, movement, muscles, feel cues, caveats, safety notes, and citations remain in Markdown rather than only in the image.
- Expected result: Markdown carries the explanatory and cited content needed without seeing the image.
- Failure proves: The image became source-of-truth evidence or replaced accessible text.
- Automation location: M3 code-review record; EIS-RO4.

### EIS-T10. Visual-safety review evidence

- Covers: R4, R6, R8, R9, R10, R12, R13, R14, R18, R29, R30, E3, E4, EC14, EC15, EC16, EC17, AC9, AC10
- Level: manual
- Fixture/setup: Final generated raster exercise images, nearby Markdown, provenance rows, and change-local visual-safety checklist.
- Steps: Perform EIS-RO1 and EIS-RO2 for each new image before promotion.
- Expected result: Evidence identifies image path, referencing page, review criteria, pass/fail result, reviewer role or handle, and residual risk; failing images are removed or revised before promotion.
- Failure proves: Generated images can imply unsupported anatomy, diagnosis, treatment, correction, brands, identity, or inaccessible color-only meaning.
- Automation location: `docs/changes/exercise-image-standard-and-optimization/` visual-safety evidence; M3 code-review record.

### EIS-T11. Beginner comprehension evidence for material image batches

- Covers: R31, AC10
- Level: manual
- Fixture/setup: A material exercise-image batch such as the five forward-head support exercises.
- Steps: Perform EIS-RO3 with non-identifying reader prompts for purpose, setup/body position, movement steps, what to notice or feel, stop condition, and source verification.
- Expected result: Evidence records per-page outcomes and residual confusion without private health information.
- Failure proves: Image batches can be accepted without showing the intended beginner comprehension benefit.
- Automation location: `docs/changes/exercise-image-standard-and-optimization/` beginner comprehension evidence; M3 code-review record.

### EIS-T12. Image-adjacent source-support review

- Covers: R2, R3, R28, AC11
- Level: manual
- Fixture/setup: Exercise pages modified in an image batch and their page-local source lists.
- Steps: Perform EIS-RO4 during code review.
- Expected result: Sampled setup, technique, muscle, feel-cue, mistake, and safety claims near images are supported by page-local sources or removed.
- Failure proves: Images created pressure to add unsupported exercise-specific claims.
- Automation location: M3 code-review record.

### EIS-T13. Remaining exercise audit evidence

- Covers: R4, R16, R18, R32, R33, E7, AC6
- Level: manual
- Fixture/setup: Inventory of all current `exercises/*.md` pages after M1 closes.
- Steps: Record each page as `no image needed`, `keep existing image`, `candidate setup image`, `candidate movement image`, `candidate muscle-attention image`, or `needs future batch`.
- Expected result: Existing images are not modified solely for media-purpose migration, and future image work is routed into small loops under the accepted proposal and plan.
- Failure proves: The audit can become a hidden migration or broad all-pages optimization.
- Automation location: M4 audit evidence under `docs/changes/exercise-image-standard-and-optimization/`.

### EIS-T14. Legacy-compatible exercise image migration guard

- Covers: R32, R33, E7, EC13, AC6
- Level: migration
- Fixture/setup: Temporary exercise fixtures and/or real existing exercise pages with generated raster provenance rows using `equipment_identification` and `key_movement_illustration`.
- Steps: Run `check_markdown_first.py` and inspect the diff during code review.
- Expected result: Legacy-compatible purposes pass when provenance is otherwise valid; no existing exercise image reference, asset, or provenance purpose is changed solely for migration.
- Failure proves: The implementation violates the approved compatibility decision.
- Automation location: `tests/test_exercise_image_standard.py`; M1/M4 code-review diff inspection.

### EIS-T15. Stable failure categories for exercise-image validation

- Covers: R36, AC10
- Level: contract
- Fixture/setup: Reuse invalid fixtures from EIS-T2 through EIS-T8.
- Steps: Assert failure output includes page path, normalized asset path when relevant, and stable categories for path, extension, alt-text, provenance, purpose, page-reference, image-count, and visual-safety-evidence failures.
- Expected result: Failure categories are stable enough for reviewers and future tests to identify the violated contract.
- Failure proves: Validation can fail opaquely or drift across implementations.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T16. Security and privacy checks for exercise-image work

- Covers: R37, EC17
- Level: smoke
- Fixture/setup: Exercise-image Markdown, provenance rows, prompts or creation notes, review evidence, tests, and validation output from the active milestone.
- Steps: Run `check_privacy.py` over current-change paths during implementation milestones as needed, then run the full EIS-CMD4 command during final verification before PR handoff. Inspect visual-safety evidence for private health details or identifiable private people when image batches exist.
- Expected result: Current-change evidence has no obvious secrets or private health data during milestone review, and the full EIS-CMD4 command passes before PR handoff.
- Failure proves: Exercise-image work can leak private or health-identifying information.
- Automation location: `tools/checks/check_privacy.py`; M2/M3 code-review records.

### EIS-T17. No runtime or product-surface expansion

- Covers: R38, AC12
- Level: smoke
- Fixture/setup: Final milestone diff.
- Steps: Inspect changed files and run the full validation command set; confirm no hosted app, CMS, database, user account, user-input flow, generated JSON API, video-first media path, personalized coaching behavior, or README promotion was introduced.
- Expected result: Changes remain in Markdown, media, provenance, tests, templates, and change-local evidence.
- Failure proves: The implementation expanded beyond the approved exercise-image standard.
- Automation location: M4 code-review record and final verify report.

### EIS-T18. Template-aware checker support

- Covers: TSR-EIS-1, EIS-CMD5, M1, M2
- Level: integration
- Fixture/setup: Real `docs/templates/` files and focused fixture copies with template placeholders, template source IDs, and excluded-scope words used as instructions rather than promoted product content.
- Steps: Add checker support or path classification for `docs/templates/`; run focused tests and then run EIS-CMD5.
- Expected result: The checker validates templates without requiring product-page source sections, source IDs, or promoted-page safety citations for placeholders, while still failing real template media-contract violations such as remote image references, unsupported image extensions, unsafe exercise-image guidance, or missing required optional-image guidance once M2 adds it.
- Failure proves: Template authoring guidance cannot be validated without false positives or without missing real media-guidance regressions.
- Automation location: `tests/test_exercise_image_standard.py` or `tests/test_markdown_first_guardrails.py`; `tools/checks/check_markdown_first.py`.

### EIS-T19. Prompt-record provenance link contract

- Covers: R20, R20A, R20B, R20G, R20H, R35, R36, E8, E9, EC8A, EC8B, AC5, AC5A, AC10
- Level: integration
- Fixture/setup: Temporary exercise page references a generated raster asset under `media/exercises/fixture-exercise/setup.png`; provenance variants include valid `prompt_record`, blank `prompt_record`, remote or absolute `prompt_record`, path traversal, wrong prompt-record directory, wrong extension, missing prompt-record file, and an exercise page that embeds the prompt record as reader-facing Markdown.
- Steps: Run `check_markdown_first.py` over each fixture through `run_check_with_root`.
- Expected result: The valid prompt-record link passes; blank, non-repository-local, wrong-shape, non-Markdown, missing-file, and embedded-prompt variants fail with stable prompt-record failure categories.
- Failure proves: Generated raster exercise images can be promoted without durable repository-local exact prompt evidence or can expose prompt records as reader-facing content.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`.

### EIS-T20. Prompt-record content and reverse asset-path match

- Covers: R20C, R20D, R20E, R20F, R20H, R28, R35, R36, R37, E8, EC8C, EC8D, AC5A, AC10
- Level: unit
- Fixture/setup: Prompt-record Markdown fixtures with required fields, exact full prompt text, explicit redaction notes, missing `asset_path`, mismatched `asset_path`, missing generator/date/reviewer/status fields, missing exact prompt text, summary-only `prompt_or_creation_notes`, and unsafe or private redaction examples.
- Steps: Run prompt-record validation through `check_markdown_first.py` using generated raster exercise provenance rows that reference each prompt record.
- Expected result: Prompt records pass only when they identify the same normalized `asset_path`, include required audit fields, preserve exact full prompt text or an explicit redaction reason, and do not rely on the provenance summary as a substitute.
- Failure proves: Prompt records can drift from assets, omit exact prompts, or hide unsafe/private prompt material without deterministic review evidence.
- Automation location: `tests/test_exercise_image_standard.py`; `tools/checks/check_markdown_first.py`; scoped privacy checks for prompt-record files.

### EIS-T21. Prompt-record migration and M3 backfill guard

- Covers: R20D, EC8E, compatibility and migration, M3A
- Level: migration
- Fixture/setup: Real M3 generated raster exercise images and provenance rows, plus legacy-compatible generated raster exercise fixtures that predate the prompt-record amendment.
- Steps: During M3A implementation and code review, inspect whether exact prompts are recoverable for each M3 image. Add prompt records and `prompt_record` links when recoverable. If unavailable, require either an explicit compatibility limitation for a pre-amendment asset or replacement with a newly generated asset that has a prompt record and fresh review evidence.
- Expected result: No governed M3 generated raster exercise image is accepted without a valid prompt record; older legacy-compatible images are not forced into prompt-record migration without an approved scope decision.
- Failure proves: The repository can invent prompt evidence, silently accept missing prompts, or accidentally migrate old images outside the approved compatibility boundary.
- Automation location: `tests/test_exercise_image_standard.py` for deterministic prompt-record fixtures; M3A code-review record for real M3 backfill decisions.

## Fixtures and data

- Temporary repositories should use the existing `run_check_with_root` pattern
  so tests can create isolated `exercises/`, `media/`, `SOURCES.md`, and
  `media/PROVENANCE.md` surfaces.
- Template-context fixtures should include placeholder source IDs and
  instruction-only scope words so the checker proves those files are templates,
  not promoted product pages.
- Valid generated raster fixture rows should include all required provenance
  fields: `asset_path`, `asset_type`, `media_purpose`, `generator`,
  `prompt_record` for governed generated raster exercise images,
  `prompt_or_creation_notes`, `created_date`, `human_reviewer`,
  `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and
  `notes`.
- Prompt-record fixtures should live under
  `media/prompts/exercises/<exercise-slug>/<asset-stem>.md`, include a
  repository-relative `asset_path`, and include exact full prompt text or an
  explicit redaction note.
- Fixture image files may contain placeholder bytes; tests do not inspect
  raster pixels.
- Manual visual review uses final generated assets, not placeholder fixture
  bytes.
- Review evidence fixtures must avoid private health data and private reader
  identifiers.

## Mocking/stubbing policy

No external services are required. Tests should use local temporary files and
fixture Markdown. Image generation is not mocked because deterministic tests
only validate repository contracts; final generated assets are reviewed
manually when M3 adds them.

## Migration or compatibility tests

EIS-T14 is mandatory for M1. It must prove existing
`equipment_identification` and `key_movement_illustration` exercise images
remain valid without migration, and code review must confirm no existing
exercise media reference, asset, or provenance purpose was changed solely for
migration.

EIS-T21 is mandatory for M3A. It must prove governed M3 generated raster
exercise images have prompt records or are replaced, while older
legacy-compatible generated raster exercise images are not silently forced into
prompt-record migration.

## Observability verification

EIS-T15 verifies automated failure observability for page path, normalized asset
path when applicable, failure category, and relevant provenance field.
EIS-T19 and EIS-T20 add prompt-record observability for affected asset path,
`prompt_record` path, missing or invalid prompt-record file, reverse
`asset_path` mismatch, missing exact prompt text, and redaction-note failures.
EIS-RO1 through EIS-RO4 verify manual observability for visual-safety,
beginner-comprehension, and source-support evidence.

## Security/privacy verification

EIS-T16 runs privacy checks over Markdown, provenance, prompts or creation
notes, review evidence, tests, and validation output. Manual review also checks
that generated images do not depict identifiable private people and that
beginner comprehension evidence contains no private health information.
M3A scoped privacy checks must include prompt-record files because they preserve
exact prompt text.

## Performance checks

Exercise-image validation must remain suitable for local repository checks.
EIS-CMD2 and EIS-CMD3 are the performance smoke: they should complete within
normal local unittest/checker expectations for this repository. No separate
benchmark is required unless implementation adds expensive image inspection or
new dependency scanning.

Template-aware validation in EIS-CMD5 should reuse existing Markdown parsing
and path classification. It should not add expensive rendering, source-fetching,
or image-inspection dependencies.

## Manual QA checklist

- Confirm each new exercise image teaches exactly one setup, movement, or
  muscle-attention concept.
- Confirm every new exercise image matches nearby Markdown and does not add an
  unsupported claim.
- Confirm muscle-attention images use broad-region highlighting, not precise
  anatomy or in-image muscle labels.
- Confirm no in-image text, correctness labels, citations, warning badges,
  safety warnings, red pain marks, injury symbols, cure framing, diagnosis
  framing, treatment framing, brand marks, identifying private people, or
  shame-based posture comparison appear.
- Confirm nearby Markdown carries setup, movement, muscles, feel cues, caveats,
  safety notes, and citations.
- Confirm visual-safety evidence records image path, referencing page, criteria,
  reviewer identity or role, result, and residual risk.
- Confirm material image batches have non-identifying beginner comprehension
  evidence with per-page outcomes.
- Confirm existing exercise images were not changed solely for media-purpose
  migration.
- Confirm every governed generated raster exercise image has a `prompt_record`
  provenance value, a repository-local prompt-record file, a reverse
  `asset_path` match, and exact full prompt text or an explicit redaction note.
- Confirm exact prompts were not invented for images whose prompts cannot be
  recovered.

## What not to test and why

- Do not test raster pixel anatomy with automation; the spec requires broad
  visual-safety review, not pixel-perfect anatomy validation.
- Do not test external image generation service behavior; generated assets are
  repository artifacts after human review.
- Do not add browser, hosted-site, CMS, database, or API tests; this change
  preserves the Markdown-first repository boundary.
- Do not require existing exercise images to use the new purpose values; the
  approved spec explicitly preserves legacy-compatible purposes.
- Do not treat template placeholder source IDs, placeholder URLs, or
  instruction-only excluded-scope examples as promoted product content.
- Do not test image-generation model behavior from prompt text; test only that
  exact prompts are preserved as repository evidence for accepted assets.
- Do not test medical effectiveness, diagnosis, treatment, rehabilitation, or
  programming outcomes; GymPrimer does not make those claims.

## Uncovered gaps

None blocking for prompt-record test-spec-review. The duplicate `R24` line in
the source spec is identical text and does not create a behavioral coverage
gap.

## Next artifacts

1. Test-spec-review for the M3A prompt-record proof-map amendment.
2. M3A implementation only after test-spec-review approves the amended proof
   map.
3. M3 code-review re-review only after M3A closes or an approved review path
   explicitly supersedes the M3A dependency.

## Follow-on artifacts

- Plan review R2: `docs/changes/exercise-image-standard-and-optimization/reviews/plan-review-r2.md`

## Readiness

This test spec is ready for test-spec-review of the M3A prompt-record proof-map
amendment. It does not authorize M3A implementation or M3 code-review re-review
until test-spec-review approves the amended proof map.
