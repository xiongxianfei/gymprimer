# Test Spec: Necessary Images and Baduanjin Exercise

## Status

active

## Related spec and plan

- Spec: `specs/necessary-images-and-baduanjin-exercise.md`
- Plan: `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`
- Architecture: `docs/architecture/system/architecture.md`
- Related ADRs:
  - `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `docs/adr/2026-07-03-exercise-document-image-purposes.md`
  - `docs/adr/2026-07-03-generated-raster-prompt-records.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
|---|---|---|---|
| Proposal | `docs/proposals/2026-07-06-necessary-images-and-baduanjin-exercise.md` | accepted | Proposal-review R1 approved the Baduanjin direction with no material findings. |
| Spec | `specs/necessary-images-and-baduanjin-exercise.md` | approved | Spec-review R1 approved the spec with no material findings. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Architecture-review R1 approved the Baduanjin canonical architecture amendment. |
| Plan | `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md` | reviewed | Plan-review R1 approved the four-milestone execution plan. |
| Change metadata | `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml` | active | Workflow-managed change routed to test-spec-review after this test spec. |

## Testing strategy

Unit tests cover deterministic checker behavior for page shape, method label, forbidden scope wording, image count, media purpose, prompt-record, provenance, page-reference, and alt-text failures.

Integration checks run the real Baduanjin page, `SOURCES.md`, `RED-FLAGS.md`, `media/PROVENANCE.md`, prompt records, and change-local evidence through existing Markdown and privacy checks.

Manual proof covers visual-safety review, source-support sampling, beginner comprehension, and rollback because static tools cannot prove generated-image semantics, source judgment, or reader understanding.

No browser, hosted-app, video, animation, API, database, account, tracker, or generated public JSON test is required because the product surface remains GitHub-readable Markdown.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1-R5 | BJ-T1, CMD2 | integration | Page path, title, alias, required sections, and static beginner page contract. |
| R6-R9 | BJ-T2, BJ-T8, CMD2 | integration | Beginner movement scope and excluded claims. |
| R10-R12 | BJ-T3, MP1, CMD2 | integration, manual | Setup, safety, and page-local source support. |
| R13-R17 | BJ-T4, CMD1, CMD2 | unit, integration | Low-load control method guidance. |
| R18-R20 | BJ-T5, MP1, CMD2 | integration, manual | Broad role-based muscle guidance. |
| R21-R29 | BJ-T6, BJ-T7, CMD4 | contract, integration | Candidate pool, exact first-five batch, five-image exception, and muscle-attention limit. |
| R30-R35 | BJ-T9, CMD4 | integration | Prompt records, provenance rows, review status, and page refs. |
| R36-R39 | BJ-T10, MP2, CMD4 | unit, integration, manual | Alt text and visual exclusions. |
| R40 | MP2 | manual | Visual-safety evidence for each generated image. |
| R41 | MP3 | manual | Beginner comprehension proof. |
| R42 | BJ-T11, MP4 | integration, manual | Text-only rollback remains valid. |
| R43 | BJ-T8, CMD2, CMD3 | unit, integration | No runtime app, clinical, adaptive, or generated-guidance source-of-truth behavior. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | BJ-T7, BJ-T9 | Exactly five first-batch image purposes and asset paths. |
| E2 | BJ-T6, BJ-T7 | Deferred candidates are not sixth through tenth images. |
| E3 | BJ-T9 | Image reference maps to approved provenance and prompt record. |
| E4 | BJ-T11, MP4 | Text-only rollback remains valid after image removal. |
| E5 | BJ-T4 | Method section uses approved low-load control labels. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1 | BJ-T11 | integration | Text-only page before generated images. |
| EC2 | BJ-T7, BJ-T9 | integration | Exactly five first-batch images. |
| EC3 | BJ-T7 | unit | Sixth image fails without later approved exception. |
| EC4 | BJ-T7 | unit | Second muscle-attention image fails. |
| EC5 | BJ-T10, MP2 | unit, manual | Drawing-bow image looks combat-focused. |
| EC6 | BJ-T8, MP2 | unit, manual | Forward-bend or other image implies recovery care. |
| EC7 | BJ-T9 | unit | Prompt record points to a different asset path. |
| EC8 | BJ-T9 | unit | Approved provenance without prompt record fails. |
| EC9 | BJ-T10, MP2 | unit, manual | Exact anatomy labels fail. |
| EC10 | MP3 | manual | Residual confusion about drawing bow or alternating reach is recorded and blocks promotion until resolved or accepted as residual risk. |
| EC11 | BJ-T4 | unit | Non-approved method type or missing labels fail. |
| EC12 | BJ-T3 | integration | Reused source IDs missing from `SOURCES.md` fail when required. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `python3 -m unittest tests.test_exercise_method_guidance` | existing/configured | implementation agent | M1 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest only; no network, image generation, or publication. |
| CMD2 | `python3 tools/checks/check_markdown_first.py exercises/baduanjin-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | planned-for-implementation | implementation agent | M2-M4 | M2 code-review with existing paths only; full target by M4 | Nonzero exit blocks milestone closeout once referenced paths exist. | Not applicable. | Change validation notes | Local checker only; no network, image generation, or publication. |
| CMD3 | `python3 tools/checks/check_privacy.py exercises/baduanjin-basics.md media/PROVENANCE.md media/prompts/exercises/baduanjin-basics/ docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/` | existing/configured | implementation agent | M2-M4 | M2 code-review with existing paths only; full target by M4 | Forbidden finding or setup error blocks milestone closeout. | Not applicable. | Change validation notes | Local privacy scan only; no network or publication. |
| CMD4 | `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | existing/configured | implementation agent | M1-M4 | M1 code-review for planned fixture coverage; M3 code-review for real image references | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest only; no image generation or publication. |
| CMD5 | `python3 -m unittest discover -s tests` | existing/configured | implementation agent | M1-M4 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest discovery only; no network or publication. |
| CMD6 | `git diff --check` | existing/configured | implementation agent | M1-M4 | M1 code-review | Whitespace errors block milestone closeout. | Not applicable. | Change validation notes | Local diff check only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
|---|---|---|---|---|---|---|
| M1 | BJ-T4, BJ-T6, BJ-T7, BJ-T8, BJ-T9, BJ-T10 | none | CMD1, CMD4, CMD5, CMD6 | Test fixtures; validation notes | M1 code-review | Establishes proof obligations and negative fixtures before content/media implementation. |
| M2 | BJ-T1, BJ-T2, BJ-T3, BJ-T4, BJ-T5, BJ-T8, BJ-T11 | MP1 | CMD1, CMD2, CMD3, CMD5, CMD6 | `exercises/baduanjin-basics.md`; `SOURCES.md`; source-audit evidence; validation notes | M2 code-review | Text-only page must pass before image generation. |
| M3 | BJ-T6, BJ-T7, BJ-T9, BJ-T10 | MP2 | CMD2, CMD3, CMD4, CMD5, CMD6 | Image assets; prompt records; `media/PROVENANCE.md`; visual-safety evidence; validation notes | M3 code-review | Exactly five governed generated images must pass media checks and visual review. |
| M4 | BJ-T1-BJ-T11 | MP1, MP2, MP3, MP4 | CMD1-CMD6 | Beginner comprehension proof; rollback proof; validation notes | M4 code-review | Final implementation evidence before downstream code-review and verification. |

## Test cases

### BJ-T1. Baduanjin Page Structure

- Covers: R1-R5, AC1
- Level: integration
- Command IDs: CMD2, CMD5
- Fixture/setup: Real page `exercises/baduanjin-basics.md`.
- Steps: Assert path, `# Baduanjin Basics`, alias line, and required headings.
- Expected result: The real page has all required sections and no extra source-of-truth media structure.
- Failure proves: The page cannot serve as the stable Markdown exercise contract.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_markdown_first_real_pages.py` or checker tests.
- Required by milestone: M2

### BJ-T2. Beginner Baduanjin Scope

- Covers: R4, R6-R9, AC1, EC5, EC6
- Level: integration
- Command IDs: CMD2, CMD3
- Fixture/setup: Real page and forbidden-wording fixtures.
- Steps: Check movement breakdown remains ready stance, two-hands lift, drawing bow, alternating reach, and return to standing; check forbidden martial, clinical, treatment, fall-prevention, cure, and guarantee wording.
- Expected result: Approved beginner scope passes; forbidden scope fixtures fail.
- Failure proves: The page can drift into martial curriculum, clinical protocol, full-form teaching, or unsupported safety claims.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_markdown_first_real_pages.py`, `tools/checks/check_markdown_first.py`.
- Required by milestone: M2

### BJ-T3. Setup, Safety, and Sources

- Covers: R10-R12, EC12, AC2
- Level: integration
- Command IDs: CMD2
- Fixture/setup: `exercises/baduanjin-basics.md`, `SOURCES.md`, and page-local source references.
- Steps: Assert setup guidance includes clear flat area, comfortable clothing, foot stability, small range, and support when balance is uncertain; assert safety notes and reused source IDs are traceable.
- Expected result: Page-local sources support safety/setup claims and shared source IDs are indexed when required.
- Failure proves: Safety or setup guidance is not traceable.
- Evidence artifact: M2 validation notes and MP1 source-audit evidence.
- Automation location: checker tests and real-page tests.
- Required by milestone: M2

### BJ-T4. Low-Load Control Drill Method

- Covers: R13-R17, E5, EC11, AC2
- Level: unit, integration
- Command IDs: CMD1, CMD2
- Fixture/setup: Method fixtures and real page.
- Steps: Assert `Method type: low_load_control_drill` and visible beginner starting point, effort, rest, progression, and pause guidance; assert adaptive programming wording fails. ([Veterans Affairs][va-tai-chi-qigong])
- Expected result: Static general education method guidance passes; missing labels or adaptive wording fails.
- Failure proves: Baduanjin method guidance is either absent, unsupported by the approved method taxonomy, or personalized.
- Evidence artifact: M1 and M2 validation notes.
- Automation location: `tests/test_exercise_method_guidance.py`, real-page tests.
- Required by milestone: M1 and M2

### BJ-T5. Broad Muscle Guidance

- Covers: R18-R20, AC2
- Level: integration, manual
- Command IDs: CMD2
- Fixture/setup: Real page `## Muscles involved` and `## What you should feel`.
- Steps: Assert broad role-based regions include legs/glutes, trunk, shoulders/upper back, and feet/ankles; check no exact activation claims.
- Expected result: Muscle guidance stays broad, role-based, and Markdown-owned.
- Failure proves: The page violates the muscle-guidance standard or lets images carry anatomy truth.
- Evidence artifact: M2 validation notes and MP1 source-audit evidence.
- Automation location: real-page tests and manual source audit.
- Required by milestone: M2

### BJ-T6. Baduanjin Candidate Pool Record

- Covers: R21, R27-R28, E2, AC3
- Level: contract
- Command IDs: CMD4
- Fixture/setup: Spec, plan, or change-local evidence containing the ranked top-10 Baduanjin candidate pool.
- Steps: Assert the candidate pool exists before image generation and candidates 6-10 are classified as deferred alternatives or replacement candidates.
- Expected result: Candidate-pool evidence exists and does not authorize more than five page images.
- Failure proves: Image generation could proceed without recorded prioritization or could misread the backlog as an asset list.
- Evidence artifact: M1 validation notes.
- Automation location: test-spec review and optional artifact-presence test.
- Required by milestone: M1

### BJ-T7. First Five Image Batch and Exception

- Covers: R22-R29, E1, E2, EC2, EC3, EC4, AC3
- Level: unit, integration
- Command IDs: CMD4
- Fixture/setup: Fixtures for valid five-image Baduanjin page, sixth-image failure, second-muscle-attention failure, and unrelated four-image exercise failure.
- Steps: Assert Baduanjin first batch can reference exactly five images; assert sixth image fails; assert other exercise pages still fail above the normal three-image default without an approved exception.
- Expected result: The exception is narrow to Baduanjin and does not alter the global limit.
- Failure proves: The five-image exception is either missing or over-broad.
- Evidence artifact: M1 and M3 validation notes.
- Automation location: `tests/test_exercise_image_standard.py` or checker fixtures.
- Required by milestone: M1 and M3

### BJ-T8. Forbidden Scope

- Covers: R4, R7-R9, R43, EC5, EC6
- Level: unit, integration
- Command IDs: CMD2, CMD3
- Fixture/setup: Real page plus negative fixtures for treatment, full-form, combat, fall-prevention, recovery-care, and adaptive coaching language.
- Steps: Assert approved wording passes and forbidden fixtures fail.
- Expected result: Content remains static, non-clinical, non-martial, and non-prescriptive.
- Failure proves: The page can cross GymPrimer boundaries.
- Evidence artifact: M1, M2, and M4 validation notes.
- Automation location: checker tests and real-page tests.
- Required by milestone: M1 and M2

### BJ-T9. Prompt Records and Provenance

- Covers: R30-R35, E3, EC7, EC8, AC4
- Level: integration
- Command IDs: CMD4
- Fixture/setup: Real Baduanjin image references, prompt records, and `media/PROVENANCE.md` rows.
- Steps: Assert every generated raster image has an approved provenance row, valid required fields, matching `page_refs`, non-blank prompt record, existing prompt file, and matching asset path.
- Expected result: All generated raster assets are traceable and approved before promotion.
- Failure proves: Media governance is incomplete.
- Evidence artifact: M3 validation notes.
- Automation location: `tests/test_exercise_image_standard.py`, `tests/test_markdown_first_real_pages.py`.
- Required by milestone: M3

### BJ-T10. Alt Text and Visual Exclusions

- Covers: R36-R40, EC5, EC9, AC4, AC5
- Level: unit, integration, manual
- Command IDs: CMD4
- Fixture/setup: Real image references and negative alt-text fixtures.
- Steps: Assert alt text names Baduanjin context and teaching purpose; assert generic alt text fails; use MP2 for visual semantics.
- Expected result: Images have meaningful alt text and pass visual-safety review.
- Failure proves: Media could be inaccessible, misleading, clinical, combat-framed, or over-anatomical.
- Evidence artifact: M3 validation notes and visual-safety review.
- Automation location: checker tests and MP2.
- Required by milestone: M3

### BJ-T11. Text-Only Rollback

- Covers: R42, E4, EC1, AC5
- Level: integration, manual
- Command IDs: CMD2
- Fixture/setup: Temporary or documented text-only Baduanjin page state.
- Steps: Remove image references and omit unused assets, prompt records, and Baduanjin provenance rows in a temporary state; rerun focused checks.
- Expected result: Text-only Baduanjin page remains valid.
- Failure proves: The page depends on generated images to remain a valid Markdown page.
- Evidence artifact: rollback proof.
- Automation location: rollback proof and optional checker test.
- Required by milestone: M4

## Fixtures and data

Use temporary Markdown fixtures for valid five-image Baduanjin, sixth-image failure, second muscle-attention failure, generic-alt failure, missing prompt record, prompt-record asset mismatch, invalid media purpose, and forbidden clinical/combat wording.

Manual proof records must avoid private health information and identifiable reader details.

## Mocking/stubbing policy

Use temporary repositories or fixture roots for checker unit tests.
Do not mock `media/PROVENANCE.md` parsing when the test is intended to prove real provenance behavior.
Do not call network services or image generation during automated tests.

## Migration or compatibility tests

Test that the Baduanjin five-image exception does not change the normal exercise-image default for unrelated exercise pages.
No existing page migration is required.

## Observability verification

Failure messages should identify the path, missing section, media asset, prompt record, provenance row, page ref, or forbidden scope term that failed.
Manual evidence should name the checked asset or page section.

## Security/privacy verification

Run privacy scans on the Baduanjin page, prompt records, provenance rows, and change-local review evidence.
Manual proof must be non-identifying.
Prompt records must not include secrets, private data, or private health information.

## Performance checks

No separate performance check is required.
Local validation should remain within the existing lightweight checker and unittest model.

## Manual QA checklist

- MP1 source audit: sampled setup, safety, method, movement, muscle, feel, and pause-condition claims have page-local source support. ([Veterans Affairs][va-tai-chi-qigong])
- MP2 visual-safety review: each of the five images teaches one concept and avoids text, labels, identifiable people, brand marks, clinical framing, combat framing, and exact anatomy claims.
- MP3 beginner comprehension proof: reader can explain Baduanjin purpose, ready stance, upward reach, drawing bow, alternating reach, body regions to notice, pause conditions, and whether images helped more than text alone.
- MP4 rollback proof: text-only page remains valid after image references, Baduanjin assets, prompt records, and provenance rows are removed in a temporary or documented state.

## What not to test

- Do not test full eight-brocade lineage correctness because the page is a beginner introduction.
- Do not test clinical efficacy, disease treatment, fall-prevention effect, recovery outcome, or posture-fix effects because those are out of scope.
- Do not test video, animation, hosted app, user accounts, or generated public JSON because the change is static Markdown and repository-local media.
- Do not test exact anatomy activation from images because images are broad support assets only.

## Uncovered gaps

None.

## Next artifacts

1. Test-spec review.
2. Implementation M1 only after test-spec-review approval.

## Follow-on artifacts

- Test-spec review R1: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/test-spec-review-r1.md`

## Readiness

This test spec is active and approved after test-spec-review R1.

Implementation may start at M1 only after this workflow run halts at the requested target and the user asks to continue.

## Sources

- `specs/necessary-images-and-baduanjin-exercise.md`
- `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`
- `docs/architecture/system/architecture.md`
- `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/plan-review-r1.md`

[va-tai-chi-qigong]: https://www.va.gov/WHOLEHEALTH/cih/Tai_Chi_and_Qigong.asp
