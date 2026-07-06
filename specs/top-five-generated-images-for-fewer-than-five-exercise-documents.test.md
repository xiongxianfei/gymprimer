# Test Spec: Top-Five Generated Images for Fewer-Than-Five Exercise Documents

## Status

active

## Related spec and plan

- Spec: `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Plan: `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- Architecture: `docs/architecture/system/architecture.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
|---|---|---|---|
| Proposal | `docs/proposals/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | accepted | Proposal-review R2 approved the direction. |
| Spec | `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md` | approved | Spec-review R1 approved the contract. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Architecture-review R1 approved the scoped architecture amendment. |
| Plan | `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md` | reviewed | Plan-review R1 approved the three-milestone execution plan. |

## Testing strategy

Unit tests cover deterministic validation for the named population, five-total-image counting, older sequence image counting, sixth-image rejection, duplicate muscle-attention rejection, prompt-record and provenance requirements, and the repository reviewer exception.

Integration checks run real exercise pages, prompt records, `media/PROVENANCE.md`, and change-local evidence through Markdown and privacy checks.

Manual proof covers page-local candidate scoring, source-support judgment, beginner-comprehension outcomes, and rollback proof where automation cannot prove image usefulness.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1-R2 | T1, CMD1 | unit | Named included and excluded population. |
| R3-R6 | T2, MP1 | unit, manual | Fewer-than-five generation trigger and accepted existing image counting. |
| R7-R14 | T3, T4, MP1 | unit, manual | Page-local audit, candidate scoring, target count, coverage limit, and sixth-image failure. |
| R15-R19 | T5, CMD1, CMD2 | unit, integration | Purpose, media path, prompt-record, and provenance requirements. |
| R20-R22A | T6, CMD1 | unit | Repository reviewer exception and remaining required provenance fields. |
| R23-R26 | T7, MP2 | integration, manual | Markdown source-of-truth, prohibited claims, and replacement reasons. |
| R27-R30 | T8, CMD2, CMD3 | integration | Milestone grouping and excluded runtime behavior. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | T2 | Existing images count toward five total images. |
| E2 | T2 | Accepted older sequence image counts. |
| E3 | T3 | Named population uses generation trigger after audit. |
| E4 | T4, MP1 | Coverage limit prevents filler images. |
| E5 | T4 | Sixth image is deferred by default. |
| E6 | T6 | Blank `human_reviewer` and absent repository-local review evidence do not fail this initiative. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1-EC3 | T2 | unit | Accepted image counts produce correct new image need. |
| EC4 | T4, MP1 | unit, manual | Coverage-limit outcome below five. |
| EC5 | T4 | unit | Candidate rank 6 deferred. |
| EC6-EC7 | T7, MP2 | integration, manual | Rejected existing image and preserved image cleanup. |
| EC8-EC9A | T6 | unit | Reviewer exception and missing prompt-record boundary. |
| EC10 | T1 | unit | Baduanjin cannot enter milestone batch. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `python3 -m unittest tests.test_exercise_image_standard tests.test_exercise_document_image_prioritization` | existing/configured | implementation agent | M1 | M1 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest only; no network, generation, or publication. |
| CMD2 | `python3 tools/checks/check_markdown_first.py exercises media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` | existing/configured | implementation agent | M2-M3 | M2 code-review | Nonzero exit blocks milestone closeout. | Not applicable. | Change validation notes | Local Markdown checker only. |
| CMD3 | `python3 tools/checks/check_privacy.py exercises media media/PROVENANCE.md docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents` | existing/configured | implementation agent | M2-M3 | M2 code-review | Privacy finding blocks milestone closeout. | Not applicable. | Change validation notes | Local privacy scan only. |
| CMD4 | `python3 -m unittest discover -s tests` | existing/configured | implementation agent | M3 | M3 code-review | Nonzero exit blocks milestone closeout. | Zero tests discovered blocks milestone closeout. | Change validation notes | Local unittest discovery only. |
| CMD5 | `git diff --check` | existing/configured | implementation agent | M1-M3 | M1 code-review | Whitespace errors block milestone closeout. | Not applicable. | Change validation notes | Local diff check only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
|---|---|---|---|---|---|---|
| M1 | T1-T7 | MP1 | CMD1, CMD5 | Test fixtures and audit framework evidence | M1 code-review | Establishes validator and audit behavior before media work. |
| M2 | T2-T8 | MP1, MP2, MP3 | CMD1, CMD2, CMD3, CMD5 | First batch pages, assets, prompts, provenance, and evidence | M2 code-review | First page batch reaches five total images or records coverage-limit outcomes. |
| M3 | T1-T8 | MP1-MP4 | CMD1-CMD5 | Remaining page batch and final rollback evidence | M3 code-review | Full named population complete or explicitly coverage-limited. |

## Test cases

### T1. Named Population Boundary

- Covers: R1, R2, EC10
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Candidate exercise paths including all included documents and `exercises/baduanjin-basics.md`.
- Steps: Validate included documents pass the population check and Baduanjin fails.
- Expected result: Only R1 paths are accepted.
- Failure proves: The named exception leaked to the wrong document set.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### T2. Five Total Image Counting

- Covers: R3-R6, E1, E2, EC1-EC3
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Pages with one, two, and three accepted existing images, including older sequence image fixtures.
- Steps: Compute accepted existing count and new generated image need.
- Expected result: Existing accepted images count toward five total images.
- Failure proves: Implementation treats five as five new images or ignores older accepted sequence images.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_document_image_prioritization.py`.
- Required by milestone: M1

### T3. Page-Local Audit Contract

- Covers: R7-R11, E3
- Level: unit, manual
- Command IDs: CMD1
- Fixture/setup: Audit-table fixtures.
- Steps: Validate required audit fields, top-10 table fields, scoring criteria, and dispositions.
- Expected result: Missing fields fail; valid audit passes.
- Failure proves: Implementation can promote images without page-local justification.
- Evidence artifact: M1 audit evidence.
- Automation location: checker tests and change-local audit.
- Required by milestone: M1

### T4. Coverage Limit and Sixth-Image Rejection

- Covers: R12-R14, E4, E5, EC4, EC5
- Level: unit, manual
- Command IDs: CMD1
- Fixture/setup: Four-purpose audit fixture and six-image page fixture.
- Steps: Validate coverage-limit outcome and sixth-image rejection.
- Expected result: Fewer than five passes with rationale; sixth image fails without later approval.
- Failure proves: The implementation can force filler images or exceed the approved count.
- Evidence artifact: M1 validation notes and MP1.
- Automation location: `tests/test_exercise_image_standard.py`.
- Required by milestone: M1

### T5. Media Purpose, Prompt, and Provenance

- Covers: R15-R19
- Level: unit, integration
- Command IDs: CMD1, CMD2
- Fixture/setup: Generated raster image references, prompt records, and provenance rows.
- Steps: Validate accepted purposes, local paths, prompt-record reverse asset match, and provenance rows.
- Expected result: Valid media records pass; missing or mismatched records fail.
- Failure proves: Generated images can be promoted without traceable media records.
- Evidence artifact: M2-M3 validation notes.
- Automation location: `tests/test_exercise_image_standard.py`.
- Required by milestone: M2

### T6. Repository Reviewer Exception

- Covers: R20-R22A, E6, EC8-EC9A
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Named-initiative provenance rows with blank `human_reviewer`, no repository-local review evidence, and separate missing prompt-record fixture.
- Steps: Validate blank reviewer and absent review evidence pass only for the named initiative; missing prompt record still fails.
- Expected result: Reviewer exception is accepted only in scope and does not weaken other provenance fields.
- Failure proves: The exception is either too broad or not implemented.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_exercise_image_standard.py`.
- Required by milestone: M1

### T7. Markdown Source-of-Truth and Replacement Reasons

- Covers: R23-R26, EC6, EC7
- Level: integration, manual
- Command IDs: CMD2, CMD3
- Fixture/setup: Real exercise pages and page-local audit evidence.
- Steps: Check nearby Markdown supports image teaching purpose and replacement reasons are concrete.
- Expected result: Unsupported claims, unsafe prompt text, or style-only replacements fail audit. [Source][local-top-five-generated-images-for-fewer-than-five-exercise-documents.test-exercise-image-standard]
- Failure proves: Images can override Markdown or replace useful media without justification.
- Evidence artifact: M2-M3 source-support evidence.
- Automation location: Markdown checker and manual audit.
- Required by milestone: M2

### T8. Milestone Grouping and Runtime Non-Goals

- Covers: R27-R30
- Level: integration
- Command IDs: CMD2, CMD3, CMD4, CMD5
- Fixture/setup: Change-local milestone evidence and repository scan.
- Steps: Confirm two or three milestone batches, no hosted/runtime artifacts, and no PR-rule changes.
- Expected result: Scope remains repository-local and milestone-based.
- Failure proves: Implementation drifted outside the approved workflow or product surface.
- Evidence artifact: M3 validation notes.
- Automation location: Markdown/privacy scans and review evidence.
- Required by milestone: M3

## Fixtures and data

Fixtures should use small Markdown snippets and provenance rows under existing test fixtures.
Real-page checks should use the actual `exercises/` documents only after each milestone adds or edits them.
No private data or identifying imagery is allowed in fixtures.

## Mocking/stubbing policy

Do not mock filesystem validation for path, prompt-record, provenance, or page-reference checks.
Image generation itself is not mocked in tests; generated assets are reviewed by repository files after creation.

## Migration or compatibility tests

Compatibility tests must prove the reviewer exception is scoped to this named initiative and does not globally remove existing exercise-image requirements.
Existing accepted images remain compatible.

## Observability verification

Validation failures should name the affected page, asset path, provenance field, prompt-record path, or audit field.
Milestone reports should distinguish accepted existing images from newly generated images.

## Security/privacy verification

Run privacy scans over exercise pages, media provenance, prompt records, and change evidence.
Prompt records and audit evidence must not include secrets, private data, private health information, identifying private-person imagery, or private machine paths.

## Performance checks

No runtime performance checks are required.
Local validation should remain suitable for pre-commit-style execution.

## Manual QA checklist

| Manual proof ID | Required check | Evidence artifact | Required milestone |
|---|---|---|---|
| MP1 | Page-local audit confirms candidate scores, distinct purposes, accepted existing images, and coverage-limit outcomes. | Change-local audit evidence | M1-M3 |
| MP2 | Source-support audit confirms nearby Markdown carries the teaching claims. | Source-support evidence | M2-M3 |
| MP3 | Beginner-comprehension proof confirms images help purpose, setup/body position, movement, what to notice, and stop condition. [Source][local-top-five-generated-images-for-fewer-than-five-exercise-documents.test-exercise-image-standard] | Beginner-comprehension evidence | M2-M3 |
| MP4 | Rollback proof shows each page remains readable when a generated image reference is removed. | Rollback evidence | M3 |

## What not to test

- Do not test a hosted app, database, account system, API, video, animation, or user-input flow because none is approved.
- Do not test `exercises/baduanjin-basics.md` as part of this initiative because it is excluded.
- Do not require repository-local human-reviewer or visual-safety-review evidence for this named initiative.

## Uncovered gaps

None.

## Next artifacts

- Implementation M1 after test-spec-review approval.

## Follow-on artifacts

None yet

## Readiness

Ready for test-spec-review.

## Sources

- `specs/top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/plans/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents.md`
- `docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/reviews/plan-review-r1.md`

[local-top-five-generated-images-for-fewer-than-five-exercise-documents.test-exercise-image-standard]: exercise-image-standard.md
