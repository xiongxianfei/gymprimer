# Test Spec: Forward Head Posture Pattern Architecture

## Status

active

## Related spec and plan

- Spec: `specs/forward-head-posture-pattern-architecture.md`
- Spec review: `docs/changes/forward-head-posture-pattern-architecture/reviews/spec-review-r1.md`
- Plan: `docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md`
- Plan review: `docs/changes/forward-head-posture-pattern-architecture/reviews/plan-review-r1.md`
- Architecture/ADRs:
  - `docs/architecture/system/architecture.md`
  - `docs/changes/forward-head-posture-pattern-architecture/reviews/architecture-review-r1.md`
  - `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `docs/adr/2026-06-29-expanded-raster-media-purposes.md`
  - `docs/adr/2026-06-29-responsible-breadth-static-content-boundaries.md`

## Testing strategy

The proof strategy uses existing Python `unittest` conventions, fixture-driven checker failures, real-page integration checks, and review-only semantic checks where source-support quality cannot be reliably inferred by static parsing. Review-only semantic evidence is recorded in normal code-review records, not in a separate proof file.

- Unit: extend `tests/test_responsible_breadth_m1.py` and related fixtures to cover forward-head required sections, detailed exercise links, same-slice exercise page existence, one-image limits, image asset existence, provenance purpose, forbidden language, and deterministic no-in-image-text contract checks.
- Integration: run `tools/checks/check_markdown_first.py` against real `patterns/`, `exercises/`, `media/PROVENANCE.md`, `SOURCES.md`, `RED-FLAGS.md`, and README surfaces after each owning milestone.
- End-to-end: prove the six-page slice can be read as repository Markdown, with red-flag routing first, same-slice exercise links resolving, optional media resolving, and README still not promoting the single pattern page.
- Smoke: assert the exact six expected Markdown paths exist by M3, the optional media contract is either absent or valid, and lifecycle validation evidence names exact local commands.
- Manual: code review must inspect semantic source support for claim families, exercise instruction and safety claims, and generated image safety if the checker cannot prove those semantics.
- Contract: map all R1-R32 and AC1-AC17 to checker tests, real-page checks, privacy checks, or review-only source-support inspection.
- Migration: prove no new page class, routing change, generated output path, hosted runtime, CI workflow, or README promotion is introduced.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | FHP-T1, FHP-T12 | integration, smoke | Real-page check requires `patterns/forward-head-posture.md` and exact title. |
| R2 | FHP-T1 | unit, integration | Required pattern-page sections are fixture-tested and checked on the real page. |
| R3 | FHP-T2 | unit, integration | Red flags must precede exercise options and link `../RED-FLAGS.md`. |
| R4 | FHP-T3 | unit, integration | Non-diagnosis, no individualized care, no correction promise, and no all-pain explanation are checked. |
| R5 | FHP-T1, FHP-T3 | integration | The definition must frame forward head posture as observable position, not condition. |
| R6 | FHP-T1 | integration | The page must include three to five beginner observations or search phrases. |
| R7 | FHP-T1 | integration | Self-observation methods must be labeled observation, not diagnosis. |
| R8 | FHP-T4, FHP-RO1 | integration, manual | Contributor names are structurally checked; source support is code-review evidence. |
| R9 | FHP-T4, FHP-RO1 | integration, manual | Contributor claims need page-local sources or removal; semantic support is review-only. |
| R10 | FHP-T3, FHP-T4 | unit, integration | Uncertainty section and forbidden-language tests prevent posture-correction or pain-relief promises. |
| R11 | FHP-T4, FHP-RO1 | integration, manual | Four source families are checked by headings/source labels and reviewed for claim support. |
| R12 | FHP-T5 | integration | Five required detailed exercise options are checked by name and link. |
| R13 | FHP-T5 | unit, integration | Each detailed option must include fix reason, used muscles, and important cue/caveat. |
| R14 | FHP-T5 | unit, integration | Each detailed option must link to the exact same-slice exercise path. |
| R15 | FHP-T7 | integration | All five exercise pages must exist. |
| R16 | FHP-T7 | unit, integration | Exercise pages must satisfy the exercise-card contract. |
| R17 | FHP-T8, FHP-RO2 | integration, manual | Page-local source presence is automated; semantic instruction and safety support is code-review evidence. |
| R18 | FHP-T6 | integration | Secondary exercise list must remain clearly secondary unless fully annotated and linked. |
| R19 | FHP-T3, FHP-T5 | unit, integration | Routine, frequency, prescription, treatment-plan, and guaranteed-fix framing must fail. |
| R20 | FHP-T9 | unit, integration | Pattern page may reference no more than one pattern comparison image. |
| R21 | FHP-T9 | unit, integration | Referenced image must live under the allowed path with approved provenance and permitted purpose. |
| R22 | FHP-T9, FHP-RO3 | unit, integration, manual | Tests reject deterministic text evidence of unsafe image framing; code review checks semantic image safety if optional media is used. |
| R23 | FHP-T9 | integration | Labels, explanations, safety claims, and exercise instructions must remain in Markdown text and citations. |
| R24 | FHP-T5 | unit, integration | Detailed exercise-link existence is checked from pattern page to all five pages. |
| R25 | FHP-T9 | unit, integration | Any referenced pattern image asset must exist. |
| R26 | FHP-T1, FHP-T3, FHP-T7, FHP-T8, FHP-T9, FHP-T11 | unit, integration | Page sources, source-index reuse, provenance, privacy, and forbidden language are checked. |
| R27 | FHP-T10 | smoke | README must not promote this page as active pattern-set content. |
| R28 | FHP-T11 | smoke, migration | Tests and review check no new page class, runtime, output path, CI, hosted app, CMS, symptom checker, decision tree, or user input flow. |
| R29 | FHP-T1, FHP-T11 | contract | Checks preserve spec, architecture, and template responsibilities without moving normative policy into templates only. |
| R30 | FHP-T12 | smoke | Final evidence must report exact commands and avoid unobserved CI claims. |
| R31 | FHP-T7, FHP-T9 | integration | Exercise pages remain text-first unless optional media also passes existing provenance checks. |
| R32 | FHP-T1, FHP-T5, FHP-T9 | unit | Focused assertions must be added for deterministic constraints not already covered. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | FHP-T5, FHP-T7 | Valid chin-nod detailed option links to `../exercises/chin-nod.md` and includes required annotation fields. |
| E2 | FHP-T9 | Valid image support requires existing asset, approved provenance, no in-image-text contract indicators, and Markdown source-of-truth text. |
| E3 | FHP-T5 | Missing `../exercises/wall-slide.md` fails validation. |
| E4 | FHP-T3 | Corrective routine language fails forbidden-language checks. |
| E5 | FHP-T10 | README does not promote this single page as active pattern-set content. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | FHP-T3 | unit | "You have forward head posture" fails reader-diagnosis guardrails. |
| EC2 | FHP-T3 | unit | "These exercises will fix posture" fails correction-promise guardrails. |
| EC3 | FHP-T5 | unit | Missing wall-slide link fails the complete-loop rule. |
| EC4 | FHP-T7, FHP-T8 | integration | Existing exercise page without sources fails exercise-page source contract. |
| EC5 | FHP-T3, FHP-T8 | unit, integration | Neck-pain treatment progression fails treatment/rehab boundary. |
| EC6 | FHP-T9 | unit | Two pattern comparison images fail one-image first-slice constraint. |
| EC7 | FHP-T9 | unit | Provenance row with wrong `page_refs` fails media provenance. |
| EC8 | FHP-T9 | unit | Alt/provenance/page contract evidence of red pain marks, bad-posture text, or labels fails deterministic media safety checks. |
| EC9 | FHP-T10 | smoke | README promotion before the full pattern set is approved fails. |
| EC10 | FHP-T6 | integration | Clearly secondary broader exercise item passes without a detailed annotation. |

## Planned validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | Required starting | Expected failure behavior | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FHP-CMD1 | `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` | planned for implementation | tooling maintainer | M1 | M1 | From M1, zero discovered tests or unexpected nonzero exit fails the milestone. | Test runner transcript in milestone validation notes. |
| FHP-CMD2 | `python3 -m unittest tests.test_markdown_first_templates` | existing and configured | tooling maintainer | M1 | now | Any unexpected nonzero exit fails because template regressions can break page authoring. | Test runner transcript in milestone validation notes. |
| FHP-CMD3 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing and configured | tooling maintainer | M2 | now | Any unexpected nonzero exit fails because shared Markdown-first behavior must not regress. | Test runner transcript in milestone validation notes. |
| FHP-CMD4 | `python3 -m unittest discover -s tests` | existing and configured | release/check maintainer | M4 | M4 | Any unexpected nonzero exit fails final local verification. | Final validation ledger and verify report. |
| FHP-CMD5 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` | existing and extended by M1 | tooling maintainer | M1 and M4 | M1 | From M1, unexpected nonzero exit fails validation-contract closeout; from M4, unexpected nonzero exit fails final local verification. | Checker transcript in milestone validation notes and final validation ledger. |
| FHP-CMD6 | `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises` | existing and extended by M1 | content/check maintainer | M2 | M2 | From M2, unexpected nonzero exit fails exercise-page closeout. | Checker transcript in M2 validation notes. |
| FHP-CMD7 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns exercises media/PROVENANCE.md` | existing and extended by M1 | content/check maintainer | M3 | M3 | From M3, unexpected nonzero exit fails pattern-page/media closeout. | Checker transcript in M3 validation notes. |
| FHP-CMD8 | `python3 tools/checks/check_privacy.py tools tests docs/templates docs/changes/forward-head-posture-pattern-architecture` | existing and configured | tooling maintainer | M1 | M1 | Forbidden findings or setup errors fail the milestone. | Privacy checker transcript in M1 validation notes. |
| FHP-CMD9 | `python3 tools/checks/check_privacy.py exercises docs/changes/forward-head-posture-pattern-architecture SOURCES.md` | existing and configured | content/check maintainer | M2 | M2 | Forbidden findings or setup errors fail the milestone. | Privacy checker transcript in M2 validation notes. |
| FHP-CMD10 | `python3 tools/checks/check_privacy.py patterns exercises media docs/changes/forward-head-posture-pattern-architecture SOURCES.md` | existing and configured | content/check maintainer | M3 | M3 | Forbidden findings or setup errors fail the milestone. | Privacy checker transcript in M3 validation notes. |
| FHP-CMD11 | `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/forward-head-posture-pattern-architecture` | existing and configured | release/check maintainer | M4 | M4 | Forbidden findings or setup errors fail final local verification. | Final validation ledger and verify report. |
| FHP-CMD12 | `rg -n "patterns/forward-head-posture.md" README.md` | existing and configured | release/check maintainer | M4 | M4 | A no-match exit is expected and passes; any match must be reviewed as forbidden promotion or explicitly non-promotional evidence. | README promotion-gate transcript or reviewed match disposition. |
| FHP-CMD13 | `git diff --check` | existing and configured | release/check maintainer | M1-M4 | now | Any whitespace error fails the active milestone. | Command transcript in milestone validation notes. |

## Review-only semantic evidence

Review-only semantic checks do not create separate proof files. They are recorded in the normal code-review record for the milestone that first introduces the reviewed content or media.

| Review ID | Automation rationale | Exact steps | Required environment | Evidence artifact | Pass condition | Failure condition | Owning stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FHP-RO1 | Static parsing can verify citations and source sections, but not whether each source actually supports the contributor and uncertainty claims. | Inspect `patterns/forward-head-posture.md`; list the four source families; sample each contributor and uncertainty claim; compare each sampled claim to the page-local source cited near it; require unsupported claims to be removed or recited. | Local repository checkout with the reviewed diff and public source links available. | M3 code-review record, with explicit mention of FHP-RO1 result and residual risk. | All four source families are present, and sampled contributor/uncertainty claims are supported by page-local sources or removed. | A source family is missing, a sampled claim is unsupported, or a source is used for a claim it does not address. | code-review |
| FHP-RO2 | Static parsing can verify page-local source definitions, but not whether exercise instruction and safety claims are supported by suitable exercise sources. | Inspect the five same-slice exercise pages; for each page, sample setup, technique, muscle, feel-cue, common-mistake, and safety claims; compare each sampled claim to page-local sources; require unsupported claims to be removed or recited. | Local repository checkout with the reviewed diff and public source links available. | M2 code-review record, with explicit mention of FHP-RO2 result and residual risk. | Each exercise page has suitable page-local support for sampled instruction and safety claims, independent of the pattern page's four-source set. | A page lacks suitable sources, uses pattern-only sources for exercise instruction, or keeps unsupported technique or safety claims. | code-review |
| FHP-RO3 | Static checks can verify image path, provenance, alt text, and deterministic text indicators, but cannot fully prove the visual does not imply cure, injury, diagnosis, or exercise routine. | If optional media is used, inspect the final generated raster image and adjacent Markdown; confirm it is one comparison image, contains no exercise thumbnails or embedded labels, and does not visually imply pain, cure, diagnosis, or before/after treatment. | Local repository checkout with the final image asset renderable from `media/patterns/forward-head-posture/`. | M3 code-review record, with explicit mention of FHP-RO3 result and residual risk. | The image is support-only, visually bounded to neutral versus forward-head comparison, and all explanatory claims remain in Markdown text. | The image contains embedded instructional labels, red injury marks, cure implication, diagnostic symbols, exercise thumbnails, or unsupported source-of-truth claims. | code-review |

## Test cases

### FHP-T1. Forward-head pattern page required contract

- Covers: R1, R2, R5, R6, R7, R26, R29, R32, AC2, AC3
- Level: integration
- Fixture/setup: Add valid and invalid forward-head pattern fixtures under `tests/fixtures/responsible-breadth/` or extend the existing temporary-root fixture style in `tests/test_responsible_breadth_m1.py`.
- Steps: Run `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` and `python3 tools/checks/check_markdown_first.py patterns`.
- Expected result: The valid page has title `Forward Head Posture` and all required pattern architecture sections; missing or renamed required sections fail with stable findings.
- Failure proves: The pattern page can drift from the approved architecture before content promotion.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tools/checks/check_markdown_first.py`.

### FHP-T2. Red flags route before exercise options

- Covers: R3, AC4
- Level: unit
- Fixture/setup: Create one fixture where red flags precede `## What commonly helps` and one where red flags appear after exercise options.
- Steps: Run the Responsible Breadth unittest target.
- Expected result: The valid fixture passes; the invalid fixture fails and reports red-flag ordering or missing `../RED-FLAGS.md`.
- Failure proves: A reader could reach exercise/self-management content before safety routing.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tools/checks/check_markdown_first.py`.

### FHP-T3. Scope and forbidden-language guardrails

- Covers: R4, R10, R19, R26, EC1, EC2, EC5, AC14
- Level: unit
- Fixture/setup: Add fixtures containing diagnosis, treatment, rehab, posture-correction, routine-prescription, guaranteed-fix, and personalized-programming phrases.
- Steps: Run the Responsible Breadth unittest target and Markdown-first checker over fixture roots.
- Expected result: Forbidden phrases fail with stable findings; uncertainty and non-diagnostic language remain required on the valid page.
- Failure proves: The page can become medical advice, a rehab protocol, or a corrective routine.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tools/checks/check_markdown_first.py`.

### FHP-T4. Source families and contributor support

- Covers: R8, R9, R10, R11, FHP-RO1, AC5
- Level: manual
- Fixture/setup: Use the real `patterns/forward-head-posture.md` after M3 and page-local sources selected during implementation.
- Steps: During M3 code review, perform FHP-RO1.
- Expected result: FHP-RO1 passes and the code-review record names the result.
- Failure proves: The page can appear citation-backed while unsupported claims remain.
- Automation location: M3 code-review record.

### FHP-T5. Detailed exercise complete loop

- Covers: R12, R13, R14, R19, R24, R32, E1, E3, EC3, AC6, AC7, AC13
- Level: integration
- Fixture/setup: Add fixtures for a valid pattern page, a missing detailed exercise link, a wrong exercise path, a missing same-slice page, and an annotation missing fix reason, used muscles, or important note.
- Steps: Run the Responsible Breadth unittest target and checker over `patterns exercises`.
- Expected result: The five required options are present, each exact link resolves, each annotation has the three required fields, and missing or wrong links fail.
- Failure proves: The pattern page can stop before the promised complete loop.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tools/checks/check_markdown_first.py`.

### FHP-T6. Broader collected exercise list remains secondary

- Covers: R18, EC10, AC10
- Level: integration
- Fixture/setup: Add a valid fixture with a clearly secondary broader list and an invalid fixture where a secondary item is formatted like a detailed option without a linked page and full annotation.
- Steps: Run the Responsible Breadth unittest target.
- Expected result: Secondary examples pass only when not presented as detailed complete-loop options.
- Failure proves: The page can silently expand scope beyond the five selected exercises.
- Automation location: `tests/test_responsible_breadth_m1.py`.

### FHP-T7. Same-slice exercise pages exist and follow the exercise contract

- Covers: R15, R16, R26, R31, EC4, AC8
- Level: integration
- Fixture/setup: Use real pages `exercises/chin-nod.md`, `exercises/thoracic-extension.md`, `exercises/wall-slide.md`, `exercises/prone-y-t.md`, and `exercises/band-pull-apart.md` after M2; add missing-section fixtures if existing tests do not cover expanded exercise pages.
- Steps: Run `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises` and `python3 -m unittest tests.test_markdown_first_templates`.
- Expected result: All five pages exist and include disclaimer, purpose, setup, muscles involved, movement breakdown, feel cues, mistakes, easier/harder versions, safety notes, and sources.
- Failure proves: The pattern page can link to pages that do not carry complete exercise instruction.
- Automation location: `tests/test_markdown_first_templates.py`; `tools/checks/check_markdown_first.py`; possible focused Responsible Breadth test.

### FHP-T8. Exercise instruction and safety source support

- Covers: R17, R26, FHP-RO2, AC9
- Level: manual
- Fixture/setup: Use the five real exercise pages and their page-local source definitions after M2.
- Steps: During M2 code review, perform FHP-RO2.
- Expected result: FHP-RO2 passes and the code-review record names the result.
- Failure proves: Pattern evidence can be misused to justify exercise technique or safety claims.
- Automation location: M2 code-review record plus `check_markdown_first.py` page-local source-section checks.

### FHP-T9. Optional pattern image contract

- Covers: R20, R21, R22, R23, R25, R26, R31, R32, FHP-RO3, E2, EC6, EC7, EC8, AC11, AC12, AC13
- Level: integration
- Fixture/setup: Add image fixtures for valid one-image use, missing asset, wrong media directory, wrong `media_purpose`, wrong `page_refs`, two images, exercise thumbnails or thumbnail wording, and deterministic no-in-image-text contract violations in alt text, adjacent text, or provenance notes.
- Steps: Run Responsible Breadth media tests and `python3 tools/checks/check_markdown_first.py patterns media/PROVENANCE.md`.
- Expected result: Text-only pages pass; one valid image passes; missing assets, invalid provenance, wrong purpose, multiple images, exercise-thumbnail framing, red pain mark/cure implication text, or in-image-text indicators fail. If optional media is used, FHP-RO3 also passes in M3 code review.
- Failure proves: Optional generated media can become unsupported, unsafe, or source-of-truth content.
- Automation location: `tests/test_responsible_breadth_m1.py`; `tests/test_markdown_first_guardrails.py`; `tools/checks/check_markdown_first.py`.

### FHP-T10. README pattern-set promotion gate

- Covers: R27, E5, EC9, AC16
- Level: smoke
- Fixture/setup: Use real `README.md` after M4.
- Steps: Run `rg -n "patterns/forward-head-posture.md" README.md` and review any match as forbidden promotion unless explicitly non-promotional evidence is present.
- Expected result: README does not promote the forward-head page as active pattern-set content.
- Failure proves: A single proof page can be exposed as a completed pattern set.
- Automation location: M4 validation command and optional focused README unittest.

### FHP-T11. Scope, privacy, and repository-boundary regression

- Covers: R26, R28, R29, AC15
- Level: smoke
- Fixture/setup: Use the full changed tree after each milestone.
- Steps: Run `python3 tools/checks/check_privacy.py` over the milestone paths, inspect `git status --short` and changed paths, and run Markdown-first checks over active content.
- Expected result: No secrets, private data, private health profiles, new runtime surfaces, new page classes, generated output path, CI workflow, hosted app, CMS, symptom checker, decision tree, or user-input flow appear.
- Failure proves: The slice exceeded the approved static Markdown boundary.
- Automation location: `tools/checks/check_privacy.py`; `git status --short`; code-review path audit.

### FHP-T12. Final validation ledger

- Covers: R30, AC1, AC17
- Level: smoke
- Fixture/setup: Use `docs/changes/forward-head-posture-pattern-architecture/change.yaml`, explain-change, and verify report after implementation and review.
- Steps: Confirm exact local commands are recorded and no hosted CI pass is claimed unless observed.
- Expected result: Final evidence includes exact commands and outcomes for tests, Markdown checker, privacy checker, README gate, and `git diff --check`.
- Failure proves: Completion can be claimed without reproducible validation evidence.
- Automation location: M4 closeout review; verify stage.

## Fixtures and data

- Valid forward-head pattern fixture with all required sections and five detailed exercise annotations.
- Invalid pattern fixtures for missing title, missing section, red flags after exercise options, missing `../RED-FLAGS.md`, diagnosis language, correction promise, routine prescription, and missing uncertainty.
- Exercise-link fixtures for each required path:
  - `../exercises/chin-nod.md`
  - `../exercises/thoracic-extension.md`
  - `../exercises/wall-slide.md`
  - `../exercises/prone-y-t.md`
  - `../exercises/band-pull-apart.md`
- Exercise-page fixtures for missing source section, missing safety notes, missing movement breakdown, and forbidden rehab/treatment framing.
- Media fixtures for one valid pattern alignment image, missing asset, wrong directory, wrong purpose, wrong `page_refs`, two image references, exercise-thumbnail framing, and in-image-text contract indicators.
- README fixture or real-page assertion for non-promotion.
- Privacy fixtures are not needed beyond the existing privacy checker unless implementation introduces new evidence surfaces.

## Mocking/stubbing policy

Use temporary directories and fixture Markdown files consistent with existing `tests/test_responsible_breadth_m1.py` patterns. Do not mock `tools/checks/check_markdown_first.py`; invoke the real checker so path resolution, source parsing, media provenance, and cross-page link behavior are exercised together. Do not mock `check_privacy.py` for milestone validation.

## Migration or compatibility tests

FHP-T11 covers compatibility by checking the change does not introduce a new page class, generated output path, hosted runtime, CMS, CI workflow, symptom checker, decision tree, or user-input flow. Existing Markdown-first and Responsible Breadth tests remain regression coverage for shared citation, media, privacy, and page-structure behavior.

## Observability verification

Checker failures should name the file path and stable finding category for missing sections, red-flag order, broken exercise links, missing image assets, bad media provenance, forbidden language, missing source sections, and privacy findings. The final validation ledger must record exact local commands and outcomes.

## Security/privacy verification

Run privacy checks over `patterns`, `exercises`, `media`, `SOURCES.md`, `RED-FLAGS.md`, and `docs/changes/forward-head-posture-pattern-architecture` according to the owning milestone. The pages must not include secrets, credentials, private local paths, private reviewer details, sensitive health information, real user health profiles, symptom intake, medical history intake, or user-specific routing.

## Performance checks

No runtime performance checks apply. If new checker behavior materially slows validation, implementation should record command duration in the milestone validation notes.

## Manual QA checklist

- M3 code review records FHP-RO1 for semantic source support across the four pattern claim families.
- M2 code review records FHP-RO2 for semantic source support across exercise setup, technique, muscle, feel-cue, common-mistake, and safety claims.
- M3 code review records FHP-RO3 for optional generated image safety if a pattern image is used.
- Code review checks README matches the pattern-set promotion gate.

## What not to test and why

- Do not test medical effectiveness, posture correction, pain relief, diagnosis, or individualized programming; the product must not make those claims.
- Do not test a rounded-shoulders page or any other future pattern; this slice covers only forward head posture.
- Do not test hosted deployment, CMS behavior, runtime APIs, user accounts, generated output, or CI workflows because the approved architecture forbids adding them.
- Do not require exercise thumbnails on the pattern page; the first slice explicitly excludes them.
- Do not require OCR or external image-analysis services; deterministic repository checks should cover the approved media contract without adding external tooling.

## Uncovered gaps

None. Semantic source quality and pixel-level image semantics cannot be fully proven by the existing static checker; this test spec assigns those checks to normal code-review records through FHP-RO1, FHP-RO2, and FHP-RO3.

## Next artifacts

- `test-spec-review` for this active proof map.
- After approval, M1 implementation of focused checker and fixture coverage.

## Follow-on artifacts

Test-spec-review R1 requested changes for review-only semantic evidence and validation command ownership. This revision addresses TSR-FHP-1 and TSR-FHP-2 and requires same-stage re-review before implementation relies on it.

## Readiness

Ready for test-spec-review. The proof map covers R1-R32, E1-E5, EC1-EC10, AC1-AC17, FHP-RO1 through FHP-RO3, FHP-CMD1 through FHP-CMD13, the approved plan milestones, and the existing Markdown-first checker/test conventions.
