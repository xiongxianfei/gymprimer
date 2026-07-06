# Test Spec: Necessary Images and Tai Chi Exercise

## Status

active

## Related spec and plan

- Spec: `specs/necessary-images-and-tai-chi-exercise.md`
- Plan: `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`
- Architecture: `docs/architecture/system/architecture.md`
- Related ADRs:
  - `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `docs/adr/2026-07-03-exercise-document-image-purposes.md`
  - `docs/adr/2026-07-03-generated-raster-prompt-records.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Proposal | `docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md` | accepted | Proposal-review R2 approved the Tai Chi direction with no material findings. |
| Spec | `specs/necessary-images-and-tai-chi-exercise.md` | approved | Spec-review R1 approved the spec with no material findings. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Architecture-review R1 approved the Tai Chi canonical architecture amendment. |
| Plan | `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md` | reviewed | Plan-review R1 approved the four-milestone execution plan. |
| Change metadata | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml` | active | Workflow-managed change routed to test-spec-review after this test spec. |

## Testing strategy

Unit tests cover deterministic checker behavior for page shape, method label, forbidden scope wording, image count, media purpose, prompt-record, provenance, page-reference, and alt-text failures.

Integration checks run the real Tai Chi page, `SOURCES.md`, `RED-FLAGS.md`, `media/PROVENANCE.md`, prompt records, and change-local evidence through existing Markdown and privacy checks.

Manual proof covers visual-safety review, source-support sampling, and beginner comprehension because static tools cannot prove generated-image semantics or reader understanding.

No browser, hosted-app, video, animation, API, database, account, tracker, or generated public JSON test is required because the product surface remains GitHub-readable Markdown.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | TC-T1, CMD2 | integration | Page path exists. |
| R2 | TC-T1, CMD2 | integration | Page title is exact. |
| R3 | TC-T2, TC-T8, CMD2 | integration | Static beginner page and excluded scope. |
| R4 | TC-T1, CMD2 | integration | Required Markdown sections. |
| R5 | TC-T2, CMD2 | integration | Movement breakdown limited to beginner basics. |
| R6 | TC-T2, CMD2 | integration | No named long form, lineage form, or martial application. |
| R7 | TC-T2, MP1 | integration, manual | Approved Tai Chi framing and source support. |
| R8 | TC-T2, TC-T8, CMD2 | integration | No treatment, cure, fall-prevention, posture-fix, or medical replacement claim. |
| R9 | TC-T3, CMD2 | integration | Setup includes area, footwear/contact, small movement, and support. |
| R10 | TC-T3, CMD2 | integration | Safety notes include required stop-or-pause categories. |
| R11 | TC-T3, MP1 | integration, manual | Safety and setup claims have page-local source support. |
| R12 | TC-T4, CMD1, CMD2 | unit, integration | Method type is `low_load_control_drill`. |
| R13 | TC-T4, CMD1, CMD2 | unit, integration | Required visible method labels. |
| R14 | TC-T4, CMD1, CMD2 | unit, integration | Static general education, not adaptive programming. |
| R15 | TC-T4, MP1 | integration, manual | Short low-effort duration receives source and review support. |
| R16 | TC-T4, CMD2 | integration | Progression prioritizes smoother control before bigger/deeper/faster movement. |
| R17 | TC-T5, CMD2 | integration | Broad role-based muscle language. |
| R18 | TC-T5, CMD2 | integration | Required muscle regions and roles. |
| R19 | TC-T5, MP1 | integration, manual | No exact activation claims; Markdown owns muscle names and cues. |
| R20 | TC-T6, CMD4 | contract | Top-10 candidate pool exists before image generation. |
| R21 | TC-T7, CMD4 | unit, integration | First image batch selects exactly three generated rasters. |
| R22 | TC-T7, TC-T9, CMD4 | integration | Required first-batch filenames and directory. |
| R23 | TC-T7, TC-T9, CMD4 | integration | Setup image purpose. |
| R24 | TC-T7, TC-T9, CMD4 | integration | Weight-shift image purpose. |
| R25 | TC-T7, TC-T9, CMD4 | integration | Muscle-attention image purpose. |
| R26 | TC-T6, TC-T7, CMD4 | contract | Candidates 4-10 do not authorize more than three images. |
| R27 | TC-T7, CMD4 | integration | Replacement candidate allowed only within three-image limit. |
| R28 | TC-T7, CMD4 | unit, integration | More than three images requires approved exception. |
| R29 | TC-T7, CMD4 | unit, integration | At most one muscle-attention image. |
| R30 | TC-T9, CMD4 | integration | Approved provenance row before promotion. |
| R31 | TC-T9, CMD4 | integration | Prompt record exists under approved path. |
| R32 | TC-T9, CMD4 | integration | Prompt record preserves exact prompt or approved redaction note. |
| R33 | TC-T9, CMD4 | integration | Provenance required fields. |
| R34 | TC-T9, CMD4 | integration | Asset type and approved review status. |
| R35 | TC-T9, CMD4 | integration | `page_refs` includes Tai Chi page. |
| R36 | TC-T10, CMD4 | unit, integration | Meaningful alt text exists. |
| R37 | TC-T10, CMD4 | unit, integration | Generic alt text fails. |
| R38 | TC-T8, TC-T10, MP2 | unit, manual | Image visual exclusions. |
| R39 | TC-T10, MP2 | unit, manual | Muscle-attention image uses broad regions only. |
| R40 | MP2 | manual | Visual-safety evidence for each generated image. |
| R41 | MP3 | manual | Beginner comprehension proof. |
| R42 | TC-T11, MP4 | integration, manual | Text-only rollback remains valid. |
| R43 | TC-T8, CMD2, CMD3 | unit, integration | No runtime app, clinical, adaptive, or generated-guidance source-of-truth behavior. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | TC-T7, TC-T9 | Exactly three first-batch image purposes. |
| E2 | TC-T6, TC-T7 | Deferred candidate is not a fourth image. |
| E3 | TC-T7 | Replacement remains valid when image count stays at three. |
| E4 | TC-T7 | Fourth image fails without approved exception. |
| E5 | TC-T4 | Method section uses approved low-load control labels. |
| E6 | TC-T9 | Image reference maps to approved provenance and prompt record. |
| E7 | TC-T11, MP4 | Text-only rollback remains valid after image removal. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | TC-T11 | integration | Text-only page before generated images. |
| EC2 | TC-T7, TC-T9 | integration | Exactly three first-batch images. |
| EC3 | TC-T7 | integration | Deferred candidate replaces one image without exceeding three. |
| EC4 | TC-T7 | unit | Fourth image fails without exception. |
| EC5 | TC-T9 | unit | Approved provenance without prompt record fails. |
| EC6 | TC-T9 | unit | Prompt record points to a different asset path. |
| EC7 | TC-T10, MP2 | unit, manual | Exact anatomy labels fail. |
| EC8 | TC-T8, MP2 | unit, manual | Therapy or fall-prevention framing fails. |
| EC9 | TC-T8, MP2 | unit, manual | Combat framing or correctness badges fail. |
| EC10 | MP3 | manual | Residual confusion about weight shift is recorded and blocks promotion until resolved or accepted as residual risk. |
| EC11 | TC-T4 | unit | Non-approved method type or missing labels fail. |
| EC12 | TC-T3 | integration | Reused source IDs missing from `SOURCES.md` fail when required. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python3 -m unittest tests.test_exercise_method_guidance` | existing/configured | implementation agent | M1 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest only; no network, image generation, or publication. |
| CMD2 | `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md` | planned-for-implementation | implementation agent | M2-M4 | M2 code-review | Nonzero exit blocks milestone closeout once the referenced page exists. | Not applicable. | Change validation notes | Local checker only; no network, image generation, or publication. |
| CMD3 | `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/` | existing/configured | implementation agent | M2-M4 | M2 code-review with existing paths only; full target by M4 | Forbidden finding or setup error blocks milestone closeout. | Not applicable. | Change validation notes | Local privacy scan only; no network or publication. |
| CMD4 | `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | existing/configured | implementation agent | M1-M4 | M1 code-review for planned fixture coverage; M3 code-review for real image references | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest only; no image generation or publication. |
| CMD5 | `python3 -m unittest discover -s tests` | existing/configured | implementation agent | M1-M4 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest discovery only; no network or publication. |
| CMD6 | `git diff --check` | existing/configured | implementation agent | M1-M4 | M1 code-review | Whitespace errors block milestone closeout. | Not applicable. | Change validation notes | Local diff check only. |

## Manual proof procedures

| Manual proof ID | Automation rationale | Exact steps | Required environment | Evidence artifact | Pass condition | Failure condition | Owning stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP1 | Static checks can find sources, but cannot prove claim-level support. | Sample setup, safety, method, movement, muscle, feel, and stop-condition claims; verify each sampled claim has page-local source support or remove/reword the claim. | Local checkout with final Markdown and public source links available. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/source-audit.md` or validation notes | Sampled claims are supported by page-local sources or removed. | Unsupported sampled claims remain or evidence omits claim categories. | M2 code-review and M4 code-review |
| MP2 | Static checks cannot prove generated-image visual semantics. | Inspect each selected image with nearby Markdown; record one-concept teaching purpose, no in-image text, no identifiable person, no brand mark, no clinical or combat framing, no unsupported claim, broad muscle highlighting, and color-accessibility. | Local checkout with final images renderable from `media/exercises/tai-chi-basics/`. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/visual-safety-review.md` | Every selected image passes all criteria or is removed/replaced before promotion. | Any selected image fails criteria, lacks evidence, or introduces unsupported visual meaning. | M3 code-review and M4 code-review |
| MP3 | Static checks cannot prove beginner understanding. | Record non-identifying beginner responses for Tai Chi purpose, ready stance, weight shift, body feel, pause/stop conditions, and whether images helped more than text alone. | Local checkout with final page and images; no private health information collected. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/beginner-comprehension-proof.md` | Evidence records each prompt outcome and residual confusion without private health data. | Evidence is absent, global-only, omits required prompts, or stores private health information. | M4 code-review |
| MP4 | Static checks cannot prove rollback procedure was exercised. | Remove image references in a temporary or documented review state; confirm unused Tai Chi assets, prompt records, and provenance rows can be removed while the text-only page still passes focused checks. | Local checkout; no destructive command against unrelated work. | `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/rollback-proof.md` or validation notes | Text-only Tai Chi page remains valid and cleanup steps are documented. | Page depends on images, prompt records, or provenance rows to remain valid. | M4 code-review |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | TC-T4, TC-T6, TC-T7, TC-T8, TC-T9, TC-T10 | none | CMD1, CMD4, CMD5, CMD6 | `specs/necessary-images-and-tai-chi-exercise.test.md`; test fixtures; validation notes | M1 code-review | Establishes proof obligations and negative fixtures before content/media implementation. |
| M2 | TC-T1, TC-T2, TC-T3, TC-T4, TC-T5, TC-T8, TC-T11 | MP1 | CMD1, CMD2, CMD3, CMD5, CMD6 | `exercises/tai-chi-basics.md`; `SOURCES.md`; source-audit evidence; validation notes | M2 code-review | Text-only page must pass before image generation. |
| M3 | TC-T6, TC-T7, TC-T9, TC-T10 | MP2 | CMD2, CMD3, CMD4, CMD5, CMD6 | Image assets; prompt records; `media/PROVENANCE.md`; visual-safety evidence; validation notes | M3 code-review | Exactly three governed generated images must pass media checks and visual review. |
| M4 | TC-T1-TC-T11 | MP1, MP2, MP3, MP4 | CMD1-CMD6 | Beginner comprehension proof; rollback proof; validation notes | M4 code-review | Final implementation evidence before downstream code-review and verification. |

## Test cases

### TC-T1. Tai Chi Page Structure

- Covers: R1-R4, AC1
- Level: integration
- Command IDs: CMD2, CMD5
- Fixture/setup: Real page `exercises/tai-chi-basics.md`.
- Steps: Assert path, `# Tai Chi Basics`, and required headings.
- Expected result: The real page has all required sections and no extra source-of-truth media structure.
- Failure proves: The page cannot serve as the stable Markdown exercise contract.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_markdown_first_real_pages.py` or checker tests.
- Required by milestone: M2

### TC-T2. Beginner Tai Chi Scope

- Covers: R3, R5-R8, AC1, EC8, EC9
- Level: integration
- Command IDs: CMD2, CMD3
- Fixture/setup: Real page and forbidden-wording fixtures.
- Steps: Check movement breakdown remains ready stance, weight shift, opening movement, and return to standing; check forbidden martial, clinical, treatment, fall-prevention, cure, and guarantee wording.
- Expected result: Approved beginner scope passes; forbidden scope fixtures fail.
- Failure proves: The page can drift into martial curriculum, clinical protocol, or unsupported safety claims.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_markdown_first_real_pages.py`, `tools/checks/check_markdown_first.py`.
- Required by milestone: M2

### TC-T3. Setup, Safety, and Sources

- Covers: R9-R11, EC12, AC2
- Level: integration
- Command IDs: CMD2
- Fixture/setup: `exercises/tai-chi-basics.md`, `SOURCES.md`, and page-local source references.
- Steps: Assert setup guidance includes clear flat area, foot stability, small slow movements, and support when balance is uncertain; assert safety notes and reused source IDs are traceable.
- Expected result: Page-local sources support safety/setup claims and shared source IDs are indexed when required.
- Failure proves: Safety or setup guidance is not traceable.
- Evidence artifact: M2 validation notes and MP1 source-audit evidence.
- Automation location: checker tests and real-page tests.
- Required by milestone: M2

### TC-T4. Low-Load Control Drill Method

- Covers: R12-R16, E5, EC11, AC2
- Level: unit, integration
- Command IDs: CMD1, CMD2
- Fixture/setup: Method fixtures and real page.
- Steps: Assert `Method type: low_load_control_drill` and visible beginner starting point, effort, rest, progression, and stop guidance; assert adaptive programming wording fails.
- Expected result: Static general education method guidance passes; missing labels or adaptive wording fails.
- Failure proves: Tai Chi method guidance is either absent, unsupported by the approved method taxonomy, or personalized.
- Evidence artifact: M1 and M2 validation notes.
- Automation location: `tests/test_exercise_method_guidance.py`, real-page tests.
- Required by milestone: M1 and M2

### TC-T5. Broad Muscle Guidance

- Covers: R17-R19, AC2
- Level: integration, manual
- Command IDs: CMD2
- Fixture/setup: Real page `## Muscles involved` and `## What you should feel`.
- Steps: Assert broad role-based regions include legs/glutes, trunk, shoulders/upper back, and feet/ankles; check no exact activation claims.
- Expected result: Muscle guidance stays broad, role-based, and Markdown-owned.
- Failure proves: The page violates the muscle-guidance standard or lets images carry anatomy truth.
- Evidence artifact: M2 validation notes and MP1 source-audit evidence.
- Automation location: real-page tests and manual source audit.
- Required by milestone: M2

### TC-T6. Tai Chi Candidate Pool Record

- Covers: R20, R26-R28, E2, AC3
- Level: contract
- Command IDs: CMD4
- Fixture/setup: Spec, plan, or change-local evidence containing the ranked top-10 Tai Chi candidate pool.
- Steps: Assert the candidate pool exists before image generation and candidates 4-10 are classified as deferred alternatives or replacement candidates.
- Expected result: Candidate-pool evidence exists and does not authorize more than three page images.
- Failure proves: Image generation could proceed without recorded prioritization or could misread the backlog as an asset list.
- Evidence artifact: M1 validation notes.
- Automation location: test-spec review and optional artifact-presence test.
- Required by milestone: M1

### TC-T7. First-Batch Image Count and Purpose

- Covers: R21-R29, E1-E4, EC2-EC4, AC3
- Level: unit, integration
- Command IDs: CMD4, CMD2
- Fixture/setup: Fixtures and real page variants with zero, three, replacement-three, four, and two muscle-attention image references.
- Steps: Assert first-batch page references exactly setup, weight-shift, and muscle-attention images; assert fourth image and second muscle-attention image fail without approved exception.
- Expected result: Exactly three valid images pass after M3; invalid count or purpose combinations fail.
- Failure proves: The image limit or purpose selection can be bypassed.
- Evidence artifact: M1 and M3 validation notes.
- Automation location: `tests/test_exercise_image_standard.py`, checker tests.
- Required by milestone: M1 and M3

### TC-T8. Forbidden Product and Visual Semantics

- Covers: R38, R43, EC8, EC9, AC7
- Level: unit, manual
- Command IDs: CMD2, CMD3
- Fixture/setup: Forbidden wording fixtures, real page, prompt records, and visual review checklist.
- Steps: Check no hosted app, CMS, database, user input, coaching, clinical framing, combat framing, in-image text, correctness badges, red pain marks, brand marks, or identifiable people.
- Expected result: Deterministic forbidden text fails and manual visual review rejects unsafe image semantics.
- Failure proves: The implementation crossed GymPrimer's product or media safety boundary.
- Evidence artifact: M2-M4 validation notes and MP2 visual-safety review.
- Automation location: checker tests plus manual review.
- Required by milestone: M1-M4

### TC-T9. Prompt Records and Provenance

- Covers: R30-R35, E6, EC5, EC6, AC4
- Level: unit, integration
- Command IDs: CMD4, CMD2
- Fixture/setup: Real or fixture image references, prompt records, and `media/PROVENANCE.md` rows.
- Steps: Assert each selected asset has one approved provenance row, valid fields, `asset_type = ai_generated_raster`, approved review status, valid media purpose, `page_refs`, and matching prompt record with reverse asset path.
- Expected result: Valid rows and prompt records pass; missing, mismatched, or incomplete rows fail.
- Failure proves: Generated media can be promoted without deterministic provenance or prompt traceability.
- Evidence artifact: M3 validation notes.
- Automation location: `tests/test_exercise_image_standard.py`, checker tests.
- Required by milestone: M1 and M3

### TC-T10. Alt Text and Muscle-Attention Visual Contract

- Covers: R36-R40, EC7, AC5
- Level: unit, manual
- Command IDs: CMD4, CMD2
- Fixture/setup: Real image references and alt-text fixtures.
- Steps: Assert alt text is meaningful and non-generic; verify muscle-attention image highlights broad regions only and avoids exact labels or pain marks.
- Expected result: Meaningful alt text and broad visual highlights pass; generic alt text, exact anatomy labels, or pain marks fail.
- Failure proves: Images are not accessible or are making unsupported visual claims.
- Evidence artifact: M3 visual-safety evidence.
- Automation location: image-standard tests and manual review.
- Required by milestone: M1 and M3

### TC-T11. Text-Only Rollback

- Covers: R42, E7, EC1, AC6
- Level: integration, manual
- Command IDs: CMD2, CMD3
- Fixture/setup: Real page with image references removed and no unused Tai Chi prompt/provenance rows.
- Steps: Run focused Markdown and privacy checks on the text-only page and record rollback proof.
- Expected result: Text-only page remains valid when failed images are removed.
- Failure proves: The implementation made generated images a source-of-truth dependency.
- Evidence artifact: M4 rollback proof.
- Automation location: real-page checks and manual rollback evidence.
- Required by milestone: M2 and M4

## Fixtures and data

- Fixture pages for valid text-only Tai Chi, valid three-image Tai Chi, fourth-image failure, second muscle-attention failure, generic-alt failure, missing prompt record, prompt-record asset mismatch, invalid media purpose, and forbidden clinical/combat wording.
- Real implementation artifacts after M2-M4: `exercises/tai-chi-basics.md`, generated image assets, prompt records, `media/PROVENANCE.md`, `SOURCES.md`, and change-local evidence.

## Mocking/stubbing policy

Checker tests may use temporary repositories and small placeholder raster files.
They must not call image generation, network sources, hosted services, or external review systems.
Manual proof uses final repository artifacts, not mocked image semantics.

## Migration or compatibility tests

No existing page migration is required.
Compatibility checks cover the new stable Markdown path, the three first-batch media paths, prompt-record paths, provenance `asset_path` values, and text-only rollback.

## Observability verification

Validation output should identify affected page paths, asset paths, prompt-record paths, provenance fields, image-count failures, and source-index failures where tooling supports stable categories.
Manual evidence must identify reviewed image paths, review result, checked criteria, residual risk, and beginner comprehension outcome without private health information.

## Security/privacy verification

Run privacy checks on the Tai Chi page, prompt records, provenance rows, and change-local review evidence.
Manual review must reject identifiable people, private environments, private reviewer data, private reader data, private health information, secrets, or local machine paths.

## Performance checks

No runtime performance check is required.
Review generated asset dimensions and repository weight during M3 if generated files are unusually large.

## Manual QA checklist

- MP1 source audit: setup, safety, method, movement, muscle, feel, and stop-condition claims have page-local support.
- MP2 visual-safety review: each image teaches one concept, has no in-image text, no identifiable person, no brand mark, no clinical or combat framing, no unsupported claim, and remains color-accessible.
- MP3 beginner comprehension proof: reader can explain Tai Chi purpose, ready stance, weight shift, body feel, pause/stop conditions, and whether images helped more than text alone.
- MP4 rollback proof: failed images can be removed with prompt/provenance cleanup while leaving a valid text-only page.

## What not to test and why

- Do not test a full Tai Chi form, combat application, lineage/style correctness, therapy outcome, fall-prevention effect, or clinical recovery plan because those are out of scope.
- Do not test video, animation, camera analysis, app behavior, account behavior, database behavior, generated public JSON, or hosted deployment because the approved change does not introduce those surfaces.
- Do not test medical efficacy or disease outcomes because GymPrimer is static general education.

## Uncovered gaps

None blocking test-spec review.
Generated image semantic quality remains manual by design and is covered by MP2 and MP3.

## Next artifacts

1. Test-spec review.
2. Implementation M1 after clean test-spec review.

## Follow-on artifacts

None yet.

## Readiness

This test spec is ready for test-spec review.
It does not authorize implementation until test-spec-review is recorded cleanly.
