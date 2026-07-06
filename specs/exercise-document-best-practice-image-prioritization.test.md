# Test Spec: Exercise Document Best-Practice Image Prioritization

## Status

active

## Related spec and plan

- Spec: `specs/exercise-document-best-practice-image-prioritization.md`
- Spec review: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/spec-review-r1.md`
- Architecture assessment: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/architecture-assessment.md`
- Plan: `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- Plan review: `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/plan-review-r1.md`
- Governing exercise-image test spec: `specs/exercise-image-standard.test.md`

## Input artifact identities

| Kind | Path | Status or review state | Identity |
|---|---|---|---|
| Feature spec | `specs/exercise-document-best-practice-image-prioritization.md` | approved | Per-exercise image-prioritization contract. |
| Spec review | `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/spec-review-r1.md` | approved | No material findings. |
| Architecture assessment | `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/architecture-assessment.md` | architecture-not-required | Existing media architecture covers this slice. |
| Plan | `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md` | active | M1-M3 implementation sequence. |
| Plan review | `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/plan-review-r1.md` | approved | No material findings. |

## Testing strategy

The proof strategy uses focused Python `unittest` coverage for audit artifacts and image-count selection, existing exercise-image validation for generated media behavior, Markdown-first checks for reviewable evidence, privacy checks for prompt/evidence safety, and manual proof where visual semantics cannot be automated.

- Unit: add `tests/test_exercise_document_image_prioritization.py` for image-count inventory, audit schema, candidate-table fields, scoring, top-five backlog semantics, replacement rationale, and exception detection.
- Integration: run `tools/checks/check_markdown_first.py` against change-local audit evidence, changed exercise pages, `media/PROVENANCE.md`, and prompt records when generated images exist.
- End-to-end: for the first selected page or small batch, prove the audit can select a minimum-needed generated subset or no generated image without treating five images as mandatory.
- Smoke: prove no hosted app, video-first path, runtime service, new exercise inventory, or PR-rule behavior appears.
- Manual: visual-safety review, source-support audit, beginner-comprehension proof, and rollback proof are required for generated image promotion.
- Contract: every requirement, example, edge case, and acceptance criterion maps to a test or manual proof.
- Migration: prove existing acceptable images and older sequence images are preserved unless a concrete page-local replacement reason exists.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1 | EDIP-T1 | unit | Inventory includes all current exercise pages with fewer than five images. |
| R2 | EDIP-T2 | unit, integration | Fewer-than-five status does not require generation. |
| R3 | EDIP-T3 | unit | Audit records are page-specific. |
| R4 | EDIP-T3, EDIP-T8 | integration | Page-local audit exists before page/media promotion. |
| R5 | EDIP-T3 | unit, contract | Required audit fields are enforced. |
| R6 | EDIP-T4 | unit | Top-10 table or fewer-than-ten rationale is required. |
| R7 | EDIP-T4 | unit | Candidate row fields are enforced. |
| R8 | EDIP-T4 | unit | Five scoring dimensions and 1-5 range are checked. |
| R9 | EDIP-T2, EDIP-T5 | unit | Top five are backlog, not target. |
| R10 | EDIP-T5, EDIP-MP3 | manual, integration | Generated subset must be minimum-needed. |
| R11 | EDIP-T5 | unit | Sixth candidate generation needs downstream justification. |
| R12 | EDIP-T6, EIS-T4 | unit, integration | Existing three-image normal limit remains authoritative. |
| R13 | EDIP-T6 | unit, contract | Fourth/fifth image needs page-specific approval. |
| R14 | EDIP-T7, EIS-T5 | unit, integration | Second muscle-attention image fails. |
| R15 | EDIP-T7, EIS-T2 | unit, integration | Candidate/generated purposes use accepted exercise-image purpose values. |
| R16 | EIS-T3, EIS-T19, EIS-T20, EDIP-MP1, EDIP-MP2 | integration, manual | Generated image provenance, prompt, review, alt, and comprehension proof reuse exercise-image coverage. |
| R17 | EDIP-T8, EDIP-MP2 | integration, manual | Markdown retains setup, movement, muscles, safety, and citations. |
| R18 | EDIP-T9, EDIP-MP1 | unit, manual | Clinical/coaching/unsupported image-adjacent claims fail or block review. |
| R19 | EDIP-T10 | unit, migration | Existing acceptable images are preserved. |
| R20 | EDIP-T10 | unit, migration | Style-only replacement rationale fails. |
| R21 | EDIP-T10 | unit | Concrete replacement reasons are accepted. |
| R22 | EDIP-T11 | integration | Change-local proof exists before template update. |
| R23 | EDIP-T12 | contract | First implementation slice is one page or deliberately small batch. |
| R24 | EDIP-T13, EDIP-MP4 | integration, manual | Rollback removes failed image artifacts and keeps page readable. |
| R25 | EDIP-T14 | smoke | No new PR-review rule is introduced. |
| R26 | EDIP-T14 | smoke | No hosted app, CMS, database, API, video-first, or coaching behavior is introduced. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | EDIP-T1, EDIP-T2 | Fewer-than-five pages enter evaluation without mandatory generation. |
| E2 | EDIP-T3, EDIP-T4 | Selected page audit includes a top-10 table. |
| E3 | EDIP-T5 | Top five are backlog; generated subset is separate. |
| E4 | EDIP-T6 | Fourth image requires page-specific downstream justification. |
| E5 | EDIP-T10 | Older sequence image preservation and replacement reasons. |
| E6 | EDIP-T11 | Change-local audit proof precedes template updates. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1 | EDIP-T2 | unit | Text-only page can record no generation needed. |
| EC2 | EDIP-T10 | migration | Older sequence image is preserved. |
| EC3 | EDIP-T6 | unit | Three-image page does not add a fourth without exception. |
| EC4 | EDIP-T3, EDIP-T10 | unit | Four-existing-image page can audit duplicate or unsafe image. [Source][local-exercise-document-best-practice-image-prioritization.test-exercise-image-standard] |
| EC5 | EDIP-T4 | unit | Fewer-than-ten candidate rationale is accepted. |
| EC6 | EDIP-T5 | unit | Candidate 6 requires downstream churn rationale. |
| EC7 | EDIP-T7 | unit | Second muscle-attention candidate/image is rejected. |
| EC8 | EIS-T20, EDIP-MP1 | unit, manual | Prompt redaction is explicit and reasoned. |
| EC9 | EDIP-T13, EDIP-MP4 | integration, manual | Rollback leaves Markdown page usable. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe-mode or side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `python3 -m unittest tests.test_exercise_document_image_prioritization` | planned-for-implementation | tooling maintainer | M1 | M1 | Any nonzero exit fails the active milestone. | Zero collected tests fail M1 because this is the focused proof suite. | M1 validation notes. | Local test process only; no network or media generation. |
| CMD2 | `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | planned-for-implementation | tooling/content maintainer | M2 | M2 | Any nonzero exit fails page-slice closeout. | Zero collected focused tests fail M2. | M2 validation notes. | Local test process only. |
| CMD3 | `python3 -m unittest discover -s tests` | existing/configured | repository maintainer | M3 | M3 | Any nonzero exit fails final implementation closeout. | Zero collected tests fail M3. | M3 validation notes and verify report. | Local test process only. |
| CMD4 | `python3 tools/checks/check_markdown_first.py docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization` | existing/configured | content/check maintainer | M1 | M1 | Any nonzero exit fails audit-evidence closeout. | Not a test collector; missing target path fails. | M1 validation notes. | Local Markdown scan only. |
| CMD5 | `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization` | existing/configured | content/check maintainer | M2 | M2 | Any nonzero exit fails page/media closeout. | Not a test collector; missing target path fails. | M2 validation notes. | Local Markdown/media scan only. |
| CMD6 | `python3 tools/checks/check_privacy.py -- docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization tests` | existing/configured | privacy/check maintainer | M1 | M1 | Forbidden findings or setup errors fail M1. | Not a test collector; missing target path fails. | M1 validation notes. | Local privacy scan only. |
| CMD7 | `python3 tools/checks/check_privacy.py -- exercises media docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization` | existing/configured | privacy/check maintainer | M2 | M2 | Forbidden findings or setup errors fail M2. | Not a test collector; missing target path fails. | M2 validation notes. | Local privacy scan only. |
| CMD8 | `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests` | existing/configured | privacy/check maintainer | M3 | M3 | Forbidden findings or setup errors fail final local closeout. | Not a test collector; missing target path fails. | Verify report. | Local privacy scan only. |
| CMD9 | `git diff --check` | existing/configured | repository maintainer | M1-M3 | M1 | Whitespace errors fail the active milestone. | Not a test collector. | Milestone validation notes. | Local git metadata only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required-before gate | Notes |
|---|---|---|---|---|---|---|
| M1 | EDIP-T1, EDIP-T2, EDIP-T3, EDIP-T4, EDIP-T5, EDIP-T10, EDIP-T11 | none | CMD1, CMD4, CMD6, CMD9 | M1 validation notes and audit-criteria evidence. | M1 code-review | No exercise pages or media assets are changed. |
| M2 | EDIP-T5, EDIP-T6, EDIP-T7, EDIP-T8, EDIP-T9, EDIP-T12 | EDIP-MP1, EDIP-MP2, EDIP-MP3 | CMD2, CMD5, CMD7, CMD9 | Page-local audit, source audit, visual review if images exist. | M2 code-review | Generated images are optional and minimum-needed only. |
| M3 | EDIP-T13, EDIP-T14 | EDIP-MP1, EDIP-MP2, EDIP-MP3, EDIP-MP4 | CMD3, CMD5, CMD8, CMD9 | Beginner-comprehension, rollback, final validation notes. | final code-review and verify | Final closeout proof before explain-change/verify/PR. |

## Test cases

### EDIP-T1. Evaluation population uses fewer-than-five trigger

- Covers: R1, E1
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Temporary exercise directory with pages containing zero, one, four, five, and six image references.
- Steps: Run the audit inventory helper or test fixture.
- Expected result: Pages with zero, one, and four images are included; pages with five or more images are excluded unless explicitly selected by later scope.
- Failure proves: The first evaluation population cannot be built deterministically.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T2. Evaluation trigger does not mandate generation

- Covers: R2, R9, E1, E3, EC1
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Page-local audit fixture for a text-only exercise page with disposition `no generation needed`.
- Steps: Validate the audit fixture.
- Expected result: The audit passes when it records sufficient Markdown/current-image rationale and no generated images.
- Failure proves: Fewer-than-five was converted into an automatic generation target.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T3. Page-local audit required fields

- Covers: R3, R4, R5, E2, EC4
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Valid and invalid audit records with required fields present or missing.
- Steps: Validate each record.
- Expected result: Complete records pass; missing path, image count, section coverage, source issues, replacement issues, candidate table, generation decision, validation expectations, or rollback path fails.
- Failure proves: Page edits or generated images can proceed without reviewable page-local proof.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T4. Top-10 candidate table contract

- Covers: R6, R7, R8, E2, EC5
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Candidate tables with ten candidates, fewer candidates plus rationale, missing fields, and out-of-range scoring.
- Steps: Validate candidate table fixtures.
- Expected result: Valid tables pass; missing required columns, missing fewer-than-ten rationale, and scores outside 1-5 fail.
- Failure proves: Candidate ranking is not comparable across exercise documents.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T5. Top-five backlog and sixth-candidate boundary

- Covers: R9, R10, R11, E3, EC6
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Audit fixtures with top-five backlog, generated subset, and candidate-six generation decisions.
- Steps: Validate fixtures.
- Expected result: Top-five backlog without generation passes; generated subset must be separately justified; sixth candidate generation fails without downstream churn rationale.
- Failure proves: Candidate ranking can become automatic generation.
- Evidence artifact: M1/M2 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T6. Image-count exception proof

- Covers: R12, R13, E4, EC3
- Level: unit
- Command IDs: CMD1, CMD2
- Fixture/setup: Page/audit fixtures ending with three, four, and five images with and without approved exception references.
- Steps: Validate fixtures and run existing exercise-image count checks where page media exists.
- Expected result: Three images pass; four or five images fail unless a page-specific approved exception is recorded.
- Failure proves: The approved exercise-image count policy was weakened.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`; existing exercise-image tests.
- Required by milestone: M2

### EDIP-T7. Purpose and muscle-attention boundaries

- Covers: R14, R15, EC7
- Level: unit
- Command IDs: CMD2
- Fixture/setup: Candidate and page fixtures with accepted purposes, disallowed purposes, and one or two muscle-attention images.
- Steps: Validate fixtures and existing exercise-image checks.
- Expected result: Accepted purposes pass; disallowed purposes and second muscle-attention image fail.
- Failure proves: Page-specific ranking can bypass exercise-image purpose rules.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`; `tests/test_exercise_image_standard.py`.
- Required by milestone: M2

### EDIP-T8. Markdown remains source of truth

- Covers: R4, R17
- Level: integration
- Command IDs: CMD2, CMD5
- Fixture/setup: Selected page or fixture with generated image references and nearby Markdown.
- Steps: Run real-page tests and Markdown-first checks.
- Expected result: Setup, movement, muscle, safety, and citation claims remain in Markdown and sources, not only in images or prompt records.
- Failure proves: Images became the source of truth.
- Evidence artifact: M2 validation notes and source audit.
- Automation location: `tests/test_markdown_first_real_pages.py`; change-local source audit.
- Required by milestone: M2

### EDIP-T9. Forbidden image-adjacent claims

- Covers: R18, EC8
- Level: unit
- Command IDs: CMD2
- Fixture/setup: Candidate, prompt, alt, or nearby Markdown fixtures with treatment, cure, individualized coaching, clinical assessment, exact-anatomy authority, or workout-planner claims.
- Steps: Run focused tests and existing image-standard guardrails.
- Expected result: Forbidden claims fail or require manual review failure.
- Failure proves: Image workflow can introduce unapproved health/coaching behavior.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`; existing image-standard tests.
- Required by milestone: M2

### EDIP-T10. Existing image preservation and replacement reasons

- Covers: R19, R20, R21, E5, EC2
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Audit fixtures with preserve decisions, style-only replacement, and concrete replacement reasons.
- Steps: Validate replacement decision fixtures.
- Expected result: Preserve decisions pass; style-only replacement fails; listed concrete reasons pass.
- Failure proves: Existing acceptable images can be replaced without page-local justification.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### EDIP-T11. Template update deferral

- Covers: R22, E6
- Level: integration
- Command IDs: CMD4
- Fixture/setup: Change-local audit criteria evidence and unchanged or changed template path state.
- Steps: Inspect or validate that first-slice criteria are recorded change-locally before any template update is made.
- Expected result: M1 passes without template changes; any template update must cite later approved proof.
- Failure proves: Reusable template policy was changed before first-slice learning.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py` or change-local evidence check.
- Required by milestone: M1

### EDIP-T12. Small first slice

- Covers: R23
- Level: contract
- Command IDs: CMD2
- Fixture/setup: Plan or audit evidence naming selected exercise document paths.
- Steps: Validate selected page count against one page or deliberately small batch rationale.
- Expected result: One page passes; small batch passes only with rationale; broad all-pages implementation fails M2 review.
- Failure proves: First slice hides all-document implementation scope.
- Evidence artifact: M2 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py` or code-review evidence.
- Required by milestone: M2

### EDIP-T13. Rollback proof

- Covers: R24, EC9
- Level: integration
- Command IDs: CMD3, CMD5, CMD8
- Fixture/setup: Change-local rollback proof for removing generated image references, unused assets, prompt records, and provenance rows.
- Steps: Run recorded rollback commands or verify concrete rollback evidence.
- Expected result: Page remains readable in text form and local checks pass.
- Failure proves: Failed images cannot be removed safely.
- Evidence artifact: M3 rollback proof.
- Automation location: `tests/test_exercise_document_image_prioritization.py`; change-local rollback evidence.
- Required by milestone: M3

### EDIP-T14. Non-goal smoke

- Covers: R25, R26
- Level: smoke
- Command IDs: CMD3, CMD8, CMD9
- Fixture/setup: Final diff and repository tree.
- Steps: Inspect diff and run broad checks.
- Expected result: No PR-rule, hosted app, CMS, database, API, video-first, or coaching behavior is introduced.
- Failure proves: Implementation exceeded the approved proposal and spec.
- Evidence artifact: final validation notes and verify report.
- Automation location: broad tests, privacy checks, code review, verify.
- Required by milestone: M3

## Fixtures and data

Fixtures should be temporary Markdown audit records, temporary exercise pages, and generated-media stubs.
Fixtures must avoid network calls, real image generation, private data, and private health information.
Real page tests may be added only for selected implementation pages.

## Mocking/stubbing policy

Generated raster image behavior should be represented by local stub files and provenance rows in tests.
Do not call image-generation services or external network resources in automated tests.
Manual visual proof uses final generated assets only after implementation creates them.

## Migration or compatibility tests

EDIP-T10 covers older-image preservation.
Existing exercise-image migration compatibility remains covered by `specs/exercise-image-standard.test.md`.
No existing generated raster assets are migration targets for M1.

## Observability verification

Test failures should identify the exercise page, audit artifact, candidate rank, score field, image count, replacement rationale, purpose, prompt/provenance path, or rollback artifact that failed.

## Security/privacy verification

CMD6, CMD7, and CMD8 run local privacy checks over evidence, tests, exercises, media, prompt records, and docs.
Manual proof must avoid private reader data, private health data, secrets, and identifying private-person imagery.

## Performance checks

No runtime performance checks are required.
Local checks should remain scoped in M1 and M2, then broaden in M3.

## Manual QA checklist

| Manual proof ID | Automation rationale | Exact steps | Required environment | Evidence artifact | Pass condition | Failure condition | Owning stage |
|---|---|---|---|---|---|---|---|
| EDIP-MP1 | Static checks cannot prove visual-safety semantics. | Inspect each generated image, alt text, prompt record, provenance row, and nearby Markdown for one teaching concept, no labels, no clinical framing, no private/identifiable people, no unsupported claims, and color-accessible support. | Local checkout with final generated assets. | M2 or M3 visual-safety evidence. | Every generated image passes or is removed. | Any generated image fails or lacks evidence. | code-review |
| EDIP-MP2 | Static checks cannot prove source-support adequacy for image-adjacent text. | Sample setup, movement, muscle, feel-cue, common-mistake, safety, and image-adjacent claims; confirm page-local source support or remove/reword the claim. | Local checkout with reviewed Markdown and public sources available. | Source-support audit. | Sampled claims are supported or removed. | Unsupported claims remain. | code-review |
| EDIP-MP3 | Static checks cannot prove the generated subset is minimum-needed for beginners. | Record non-identifying beginner-comprehension prompts and outcomes for image purpose, setup/body position, movement, what to notice, stop condition, and source verification. | Local checkout and non-identifying reader-test process. | Beginner-comprehension evidence. | Evidence supports the minimum-needed generated subset or removes excess images. [Source][local-exercise-document-best-practice-image-prioritization.test-exercise-image-standard] | Evidence is absent, global only, private, or shows unresolved confusion. | code-review |
| EDIP-MP4 | Static checks cannot fully prove rollback usability. | Remove proposed generated image references and unused generated artifacts in a temporary copy; run recorded Markdown-first and privacy commands; record concrete temp path and command output summary. | Local checkout and temporary working copy. | Rollback proof. | Page remains readable and checks pass. | Rollback commands fail or are not reproducible. | code-review |

## What not to test

- Do not test actual image generation services.
- Do not test a repository-wide top-10 image list.
- Do not test that every selected page reaches five images.
- Do not test hosted runtime, CMS, database, public API, video, or user-account behavior because those are non-goals.
- Do not retest all exercise-image standard behavior except where this workflow depends on it.

## Uncovered gaps

None for pre-implementation proof planning.
If implementation requires shared validation architecture changes, return to architecture before continuing.

## Next artifacts

- Test-spec review for this proof map.
- Implementation of M1 only after approved test-spec review.

## Follow-on artifacts

- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/reviews/test-spec-review-r1.md`

## Readiness

Active proof map ready for test-spec review.
Implementation must not start until test-spec review is approved.

## Sources

- `specs/exercise-document-best-practice-image-prioritization.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-image-standard.test.md`

[local-exercise-document-best-practice-image-prioritization.test-exercise-image-standard]: exercise-image-standard.md
