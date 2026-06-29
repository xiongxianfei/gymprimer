# Test Spec: Markdown-First Gym Primer

## Status

active

## Related spec and plan

- Spec: `specs/markdown-first-primer.md`
- Spec review:
  - `docs/changes/markdown-first-gym-primer/reviews/spec-review-r1.md`
  - `docs/changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
- Plan: `docs/plans/2026-06-27-markdown-first-gym-primer.md`
- Plan review:
  - `docs/changes/markdown-first-gym-primer/reviews/plan-review-r1.md`
  - `docs/changes/markdown-first-gym-primer/reviews/plan-review-r3.md`
- Architecture: `docs/architecture/system/architecture.md`
- Architecture review:
  - `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`
- ADRs:
  - `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `docs/adr/2026-06-26-repository-native-reviewed-content.md` (superseded)

## Testing strategy

The proof strategy combines automated file-contract checks, integration checks over the real first-slice pages, and manual evidence where automation cannot prove meaning.

- Unit: exercise small checker functions for disclaimer presence, required sections, page-local sources, claim-level safety citations, excluded scope, language scope, deterministic media classification, media provenance table parsing, and privacy scan exit semantics.
- Integration: run the Markdown-first checker against real repository surfaces: `README.md`, `SOURCES.md`, `CONTRIBUTING.md`, `CONTENT_LICENSE.md`, numbered content directories, optional `media/`, `media/PROVENANCE.md`, and change-local proof records.
- End-to-end: validate that a reader can start from `README.md`, reach the five pages by relative links, inspect page-local sources, and use the pages without a generated site.
- Smoke: assert required files exist, required headings are present, old structured-platform surfaces are marked superseded, and optional mdBook either builds or has a durable deferral record.
- Manual: perform direct Markdown render/readability inspection, semantic citation review, beginner read-test proof, and visual-safety review for any optional AI-generated raster illustration.
- Contract: prove the v0.1 Markdown contract, license/contribution contract, source-of-truth boundary, and old-platform supersession boundary.
- Migration: prove old structured-platform artifacts remain traceable but inactive, and that mdBook rollback leaves Markdown navigation intact.

Existing old structured-platform tests under `tests/test_*.py` are historical unless they are explicitly reworked for Markdown-first checks. New automated tests should use Python standard-library `unittest`, temporary directories, and subprocess-style CLI checks consistent with the current repository test style.

## Milestone and proof ownership

This test spec is milestone-gated. A test, command, or manual proof record is not required to pass before its owning milestone unless explicitly marked as pre-milestone required.

Proof classifications:

| Classification | Meaning |
| --- | --- |
| existing | Command, fixture, or proof already exists and must pass now. |
| planned-for-milestone | Command, fixture, or proof is part of this test contract but may be absent before its owning milestone. |
| manual-only | Proof is collected by a bounded manual procedure rather than automation. |
| conditional/external | Proof depends on an optional external tool or explicitly documented deferral path. |

Before a proof's owning milestone, absence is not a failure unless the proof is marked pre-milestone required. At and after the owning milestone, absence, configuration failure, unexpected nonzero exit, missing fixture, or missing evidence artifact is a test-spec failure.

## Test ownership map

| Test ID | Proof area | Owner | Owning milestone | First meaningful execution | Classification | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Active repository guidance and contribution contract | project maintainer | M1 | M1 | planned-for-milestone | `tests/test_markdown_first_contract.py` result or documented structural check transcript |
| T2 | Card and principle template shape | content maintainer | M1 | M1 | planned-for-milestone | template fixture test output and template files |
| T3 | Page-local disclaimer and source-section checker | tooling maintainer | M2 | M2 | planned-for-milestone | unit test output for valid and invalid page-structure fixtures |
| T4 | Claim-level citation and source quality minimum gate | tooling maintainer | M2 | M2 | planned-for-milestone | citation fixture test output plus manual citation-review record when real pages exist |
| T5 | Scope, language, and media guardrails | tooling maintainer | M2 | M2 | planned-for-milestone | guardrail fixture test output |
| T6 | Negative-match privacy scan | tooling maintainer | M2 | M2 | planned-for-milestone | privacy fixture test output and generated privacy report |
| T7 | Old platform supersession boundary | project maintainer | M1 | M1 | planned-for-milestone | legacy-boundary test output or structural supersession scan transcript |
| T8 | Real first-slice page integration | content maintainer | M3 | M3 | planned-for-milestone | integration test output over the five real Markdown pages |
| T9 | README navigation and direct Markdown browsing smoke test | content maintainer | M3 | M3 | planned-for-milestone | README link/path test output and `MP1-direct-markdown-render.md` |
| T10 | Beginner read-test and manual citation review | content maintainer / reader-test facilitator | M3 | M3 | manual-only | `MP2-citation-semantic-review.md` and `MP3-beginner-read-test.md` |
| T11 | Optional mdBook build or durable deferral | release/check maintainer | M4 | M4 | conditional/external | `mdbook build` transcript or `MP4-mdbook-build-or-deferral.md` |
| T12 | Validation observability, command reporting, and performance | release/check maintainer | M4 | M4 | planned-for-milestone | final validation ledger with command output, skipped tools, and timing notes |
| T13 | Compatibility and migration boundary | release/check maintainer | M4 | M4 | planned-for-milestone | compatibility test output and `MP5-source-of-truth-drift.md` |
| T14 | Deterministic media classification and provenance validation | tooling maintainer | M3A | M3A | planned-for-milestone | media fixture test output and checker transcript |
| T15 | Optional AI raster visual-safety and provenance review | content maintainer / media reviewer | M3A | M3A when raster media is referenced | manual-only | `MP6-ai-raster-media-review.md` or explicit no-raster note |

## Planned validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | Required starting | Allowed before owning milestone? | Expected failure behavior | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | planned-for-milestone | tooling maintainer | M2 | M2 | yes | Before M2, no matching tests or missing check scripts are not failure. From M2, zero discovered tests, unexpected nonzero exit, or missing required fixtures fail the milestone. | test runner transcript |
| CMD2 | `python3 tools/checks/check_markdown_first.py --help` | planned-for-milestone | tooling maintainer | M2 | M2 | yes | Before M2, missing command is not failure. From M2, missing command or nonzero help exit fails. | command transcript |
| CMD3 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | Before M3, missing real content directories are not failure. From M3, nonzero exit means the first-slice pages are not promotable unless the page is explicitly kept non-canonical. | command transcript or generated report |
| CMD4 | `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | Before M3, missing real content directories are not failure. From M3, forbidden findings or execution errors fail promotion. | privacy report transcript |
| CMD5 | `if rg -n "barbell\|deadlift\|bench press\|Olympic\|kettlebell\|plyometric\|sprint\|diagnos\|rehab\|treat pain\|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | Before M3, missing real content directories are not failure. From M3, any positive match fails unless reviewed as an allowed out-of-scope explanation and covered by a safer checker rule. | negative-scan transcript |
| CMD6 | `markdownlint "**/*.md"` | conditional/external | tooling maintainer | M2 | M2 if selected | yes | If selected and installed, lint failures block M2 and later. If unavailable or not selected, record deferral. | lint transcript or deferral note |
| CMD7 | `command -v mdbook \|\| true` | conditional/external | release/check maintainer | M4 | M4 | yes | The command itself never proves readiness; it only determines whether `mdbook build` can be attempted or deferral is required. | command transcript |
| CMD8 | `mdbook build` | conditional/external | release/check maintainer | M4 | M4 | yes | From M4, either build succeeds with minimal config or explicit mdBook deferral proof is recorded. | `book/` output transcript or `MP4-mdbook-build-or-deferral.md` |
| CMD9 | Final local quality gate checklist | manual-only | release/check maintainer | M4 | M4 | yes | From M4, missing current evidence for required M1-M4 checks blocks final local quality gate completion. | `MP5-validation-command-ledger.md` or equivalent validation ledger |
| CMD10 | `python3 -m unittest tests.test_markdown_first_guardrails` | planned-for-milestone | tooling maintainer | M3A | M3A | yes | Before M3A, missing media-classification fixtures are not failure. From M3A, unexpected nonzero exit or missing required media fixtures fails the milestone. | test runner transcript |
| CMD11 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight` | planned-for-milestone | tooling maintainer | M3A | M3A | yes | Before M3A, missing M3A media behavior is not failure. From M3A, any referenced raster media without approved provenance fails promotion. | checker transcript or generated report |
| CMD12 | `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md media docs/changes/markdown-first-gym-primer` | planned-for-milestone | tooling maintainer | M3A | M3A | yes | Before M3A, missing `media/PROVENANCE.md` is not failure. From M3A, forbidden findings in media/provenance evidence or execution errors fail the milestone. | privacy report transcript |

## Manual proof ownership

| Proof ID | Proof name | Classification | Owner | Owning milestone | Required starting | Evidence artifact | Pass condition | Failure condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP1 | Direct Markdown render inspection | manual-only | content maintainer | M3 | M3 | `docs/changes/markdown-first-gym-primer/manual-proof/MP1-direct-markdown-render.md` | README and all five pages are readable as Markdown without generated HTML. | Any page cannot be reached or understood by direct Markdown inspection. |
| MP2 | Semantic citation review | manual-only | content maintainer | M3 | M3 | `docs/changes/markdown-first-gym-primer/manual-proof/MP2-citation-semantic-review.md` | Safety and technique claims have local citations that semantically support the claim. | A safety or technique claim is unsupported, global-only, broken, or misleading. |
| MP3 | Beginner read test | manual-only | reader-test facilitator | M3 | M3 | `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md` | At least one beginner can identify purpose, setup, steps, and stop condition for each exercise page. | A beginner cannot explain core setup, execution, or stop condition for any first-slice exercise page. |
| MP4 | mdBook build-or-deferral proof | conditional/external | release/check maintainer | M4 | M4 | `docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md` | `mdbook build` succeeds with minimal config, or deferral explains unavailable/non-trivial mdBook. | mdBook is claimed without build evidence or deferral, or derived HTML is treated as source. |
| MP5 | Validation command ledger and source-of-truth drift inspection | manual-only | release/check maintainer | M4 | M4 | `docs/changes/markdown-first-gym-primer/manual-proof/MP5-validation-command-ledger.md` | Required M1-M4 checks are current and no old/generated surface outranks Markdown. | Required evidence is missing, stale, or shows source-of-truth drift. |
| MP6 | AI raster media visual-safety and provenance review | manual-only | content maintainer / media reviewer | M3A | M3A when raster media is referenced | `docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md` | Every referenced AI-generated raster image is necessary, visually safe, non-decorative, within allowed purpose, and consistent with page text, or the record states no raster media was added. | A raster image is referenced without human visual-safety review, provenance approval, or explicit no-raster note. |

Manual proof records must include owner, owning milestone, automation rationale, required environment, exact steps, evidence artifact, pass condition, failure condition, and re-run trigger.

## Milestone closeout proof

| Milestone | Automated proof required | Manual proof required | Closeout rule |
| --- | --- | --- | --- |
| M1 | T1, T2, and T7 pass or are structurally satisfied. | None unless direct documentation inspection is used instead of automation. | M1 closes when active route, templates, contributor/license contract, and old-platform supersession are explicit. |
| M2 | T3, T4, T5, and T6 fixture tests pass; CMD1, CMD2, and CMD6 pass or have documented conditional deferral where applicable. | None unless a fixture requires bounded manual inspection. | M2 closes when checker tooling and deterministic fixture tests prove source, disclaimer, citation, scope, media, language, and privacy rules. |
| M3A | T14 passes; CMD10, CMD11, and CMD12 pass. | MP6 only when raster media is referenced, or an explicit no-raster note. | M3A closes when media classification and provenance validation are executable, `media/PROVENANCE.md` exists with the required table schema, text-only pages remain valid, SVG pages pass without AI-raster provenance, and raster pages require approved provenance. |
| M3 | T8 and T9 pass on real first-slice pages; CMD3, CMD4, and CMD5 pass; any referenced media passes M3A. | MP1, MP2, and MP3. | M3 closes when five real pages pass automated checks and human render, citation, beginner comprehension, and media-gate proof exists. |
| M4 | T11, T12, and T13 pass; CMD7, CMD8 or mdBook deferral, and CMD9 are recorded. | MP4 and MP5. | M4 closes when optional HTML is proven or deferred, source-of-truth drift is checked, and final local evidence is current. |

## TSR1 resolution acceptance criteria

| ID | Criterion |
| --- | --- |
| TSR1-AC1 | Every T1-T15 test has an owning milestone. |
| TSR1-AC2 | Every T1-T15 test names an owner role. |
| TSR1-AC3 | Every T1-T15 test states first meaningful execution. |
| TSR1-AC4 | Every planned command has a classification: existing, planned-for-milestone, manual-only, or conditional/external. |
| TSR1-AC5 | Every planned command has an owning milestone. |
| TSR1-AC6 | Every planned command states whether absence or failure is allowed before its milestone. |
| TSR1-AC7 | Every command states closeout evidence. |
| TSR1-AC8 | Every manual proof record has an owner, milestone, evidence artifact, pass condition, and failure condition. |
| TSR1-AC9 | mdBook proof is assigned to M4 and is allowed to be either successful build evidence or explicit deferral evidence. |
| TSR1-AC10 | Implementation handoff remains blocked until test-spec-review R2 records approval. |

## M3A proof-map acceptance criteria

| ID | Criterion |
| --- | --- |
| M3A-AC1 | M3A has an owning milestone entry before M3 closeout and after M2. |
| M3A-AC2 | R41-R53 and AC15-AC19 map to T14 and, where human visual judgment is required, T15/MP6. |
| M3A-AC3 | Planned commands identify when media classification/provenance checks become required. |
| M3A-AC4 | Text-only pages remain valid and are tested. |
| M3A-AC5 | SVG files under `media/` pass without AI-raster provenance and are tested. |
| M3A-AC6 | `.png`, `.jpg`, `.jpeg`, and `.webp` under `media/` are classified as AI-generated raster illustrations and require provenance. |
| M3A-AC7 | Remote images, media outside `media/`, unsupported extensions, and missing local media files fail with stable codes. |
| M3A-AC8 | Missing, incomplete, non-approved, out-of-scope, and page-reference-mismatched provenance rows fail with stable codes. |
| M3A-AC9 | `media/PROVENANCE.md` creation with the required table schema is part of M3A even when no raster assets exist. |
| M3A-AC10 | M3 closeout remains blocked on MP3 beginner read-test evidence and any referenced media passing M3A validation. |

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1, T8, T9 | contract, integration, smoke | Confirms Markdown is described and wired as source of truth. |
| R2 | T8 | integration | Asserts exactly the five required first-slice page paths exist before expansion. |
| R3 | T8, T9 | integration, smoke | Direct file inspection and README navigation prove no app or generated HTML requirement. |
| R4 | T1, T9 | contract, smoke | README links to promoted first-slice pages. |
| R5 | T2, T3, T8 | unit, integration | Exercise template and real exercise pages expose required sections. |
| R6 | T2, T3, T8 | unit, integration | Principle template and `beginner-training-principles.md` expose required sections. |
| R7 | T3, T8 | unit, integration | Safety-relevant pages require prominent top disclaimer. |
| R8 | T3, T8 | unit, integration | Disclaimer text must include educational, not medical advice, and not personalized coaching meaning. |
| R9 | T4, T8, T10 | unit, integration, manual | Automated adjacency checks plus manual citation review cover safety warnings. |
| R10 | T4, T8, T10 | unit, integration, manual | Weekly guidance needs public-health/professional source. |
| R11 | T4, T10 | unit, manual | Technique citation is checked as a minimum gate and manually reviewed semantically. |
| R12 | T4, T8, T10 | unit, integration, manual | Feel cues are checked for safety/anatomy citation where needed and manually reviewed. |
| R13 | T3, T4, T8 | unit, integration | Every page must contain a `Sources` section. |
| R14 | T4, T8 | unit, integration | Reused sources are cross-checked against `SOURCES.md`. |
| R15 | T4 | unit | Fixture with global-only safety citation must fail. |
| R16 | T4, T8 | unit, integration | Citation checks prefer reference-style definitions and links. |
| R17 | T5, T8 | unit, integration | Pages remain English-first. |
| R18 | T5, T8 | unit, integration | Chinese aliases are allowed when bounded. |
| R19 | T5 | unit | Full-card Chinese translation fixture fails. |
| R20 | T13 | migration | Future separate-locale structure is documented as not active in v0.1. |
| R21 | T5, T8 | unit, integration | Allowed beginner scope is checked against real pages and fixtures. |
| R22 | T5, T8 | unit, integration | Excluded lifting, rehab, diagnosis, pain treatment, and programming terms block promotion. |
| R23 | T5, T14, T15 | unit, manual | Media is absent, original SVG, or human-reviewed AI-generated raster. |
| R23a | T14, T15 | unit, manual | Images are optional and limited to necessary equipment identification or key movement illustration. |
| R23b | T14, T15 | unit, manual | Fixtures and manual review preserve the preference order: no image, SVG, then AI raster only when needed. |
| R24 | T5, T14 | unit | Third-party screenshots/photos/web-image fixtures fail as external or unsupported media. |
| R25 | T5, T14, T8 | unit, integration | Media references must be relative and understandable through alt or adjacent text. |
| R26 | T1 | contract | Contributor/license docs document Apache-2.0 for code/tooling. |
| R27 | T1 | contract | Contributor/license docs document CC BY 4.0 for written content and original diagrams. |
| R28 | T1 | contract | Contributor guidance includes right-to-submit and third-party media terms. |
| R29 | T1, T8, T10 | contract, integration, manual | Spike labeling and promotion evidence are checked before active links. |
| R30 | T1, T8 | contract, integration | Unpromoted pages must not be described as published, approved, expert-reviewed, or active source of truth. |
| R31 | T11 | smoke, migration | mdBook config is allowed only after the five Markdown pages exist and render directly. |
| R32 | T11, T13 | smoke, migration | mdBook output is treated as derived and disposable. |
| R33 | T11 | smoke | Missing/non-trivial mdBook produces deferral record instead of forced setup. |
| R34 | T7, T13 | contract, migration | Old content-schema spec/ADR are not active when conflicting. |
| R35 | T7, T13 | contract, migration | Old artifacts remain traceable. |
| R36 | T3, T4, T5, T6, T8, T11, T12 | unit, integration, smoke | Local validation covers Markdown shape, sources, citations, disclaimers, scope, media, privacy, and optional mdBook. |
| R37 | T6 | unit | Privacy check passes only when forbidden patterns are absent. |
| R38 | T10 | manual | At least one beginner read test is required before promotion. |
| R39 | T10 | manual | Read-test evidence records purpose, setup, steps, and stop condition comprehension. |
| R40 | T12 | smoke, manual | Reports exact commands run, unavailable commands, and residual risks; CI is not claimed without observation. |
| R41 | T14, T15 | unit, manual | Raster fixtures prove provenance is required before promotion; manual review covers human approval. |
| R42 | T14 | unit | Provenance must be parsed from `media/PROVENANCE.md`. |
| R43 | T14, T15 | unit, manual | Raster media is tested as supporting visual aid only; manual review checks it does not replace Markdown guidance. |
| R44 | T15 | manual | Unsafe, excluded-scope, medical, identifiable-person, or branding problems require human visual-safety review. |
| R45 | T1, T14 | contract, unit | Contributor guidance and validation failures explain media provenance and rejection behavior. |
| R46 | T14 | unit | Provenance rows must include all required fields. |
| R47 | T14 | unit | `asset_path` normalization rejects leading `./`, `/`, or mismatched path values. |
| R48 | T14 | unit | Provenance row matching is exact by normalized repository-relative `asset_path`. |
| R49 | T14 | unit | `asset_type` must be `ai_generated_raster`. |
| R50 | T14 | unit | `media_purpose` must be `equipment_identification` or `key_movement_illustration`. |
| R51 | T14 | unit | Only `review_status = approved` allows a promoted page to reference the raster image. |
| R52 | T14 | unit | `page_refs` must include every referencing promoted Markdown page. |
| R53 | T14 | unit | Missing, incomplete, non-approved, out-of-scope, and page-ref-mismatched provenance fail with stable codes. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T8, T9, T10 | Real page integration, README navigation, and beginner read test cover direct machine-page use. |
| E2 | T4, T8, T10 | Safety-warning citations are checked by tooling and manual source review. |
| E3 | T4 | Fixture with only `SOURCES.md` backing a safety claim must fail. |
| E4 | T5, T8 | Excluded-scope fixtures and real-page scans reject advanced lifting and pain-treatment content. |
| E5 | T11, T13 | mdBook build-or-defer proof keeps Markdown canonical. |
| E6 | T14, T15 | AI raster fixture and optional manual review prove relative path, provenance, license assertion, human review, and text-support boundaries. |
| E7 | T14 | Text-only fixture proves pages remain valid without media or provenance rows. |
| E8 | T14 | Missing provenance fixture fails by exact normalized `asset_path`. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | T4 | unit | Stop rule without claim-level citation fails. |
| EC2 | T3, T4 | unit | Source link without page-local `Sources` section fails. |
| EC3 | T5 | unit | Chinese alias fixture passes when the page remains English-first. |
| EC4 | T5 | unit | Full Chinese translation fixture fails. |
| EC5 | T5, T14 | unit | Licensed third-party image fixture is rejected for v0.1 unless later policy changes. |
| EC6 | T14 | unit | AI raster without provenance fails with `media_provenance_missing`. |
| EC7 | T14 | unit | Blank required provenance fields fail with `media_provenance_incomplete`. |
| EC8 | T14 | unit | `needs_revision` or `rejected` provenance fails with `media_provenance_not_approved`. |
| EC9 | T14 | unit | Out-of-scope `media_purpose` fails with `media_usage_out_of_scope`. |
| EC10 | T14 | unit | Missing referencing page in `page_refs` fails with `media_page_refs_mismatch`. |
| EC11 | T15 | manual | Unsafe or contradictory AI raster illustration is rejected or replaced before promotion. |
| EC12 | T11, T13 | smoke, migration | mdBook cannot replace GitHub-readable Markdown navigation. |
| EC13 | T10 | manual | Reader confusion keeps page unpromoted until revised. |
| EC14 | T4, T10 | unit, manual | Broken source is replaced, archived acceptably, or recorded as not ready. |
| EC15 | T7, T13 | contract, migration | Markdown-first governance outranks old generated JSON. |
| EC16 | T4, T5, T10 | unit, manual | "Soreness vs pain" wording must avoid diagnosis/treatment and use conservative safety citation. |

## Test cases

### T1. Active repository guidance and contribution contract

- Covers: R1, R4, R7-R16, R23-R30, AC3, AC6, AC8, AC9, AC13
- Level: contract
- Fixture/setup: Real files `README.md`, `CONTRIBUTING.md`, `SOURCES.md`, `CONTENT_LICENSE.md`, `docs/templates/exercise-card.md`, and `docs/templates/principle-page.md`.
- Steps: Check that README describes Markdown as source of truth and links active pages only after promotion; check contributor and license docs for Apache-2.0, CC BY 4.0, right-to-submit, no undocumented third-party media, citation, disclaimer, scope, and privacy language; check templates for required sections and source guidance.
- Expected result: Active guidance matches the Markdown-first contract and does not advertise generated public JSON, expert-reviewed pages, or old platform workflow as v0.1 product behavior.
- Failure proves: Contributors could follow stale or incomplete product, licensing, citation, media, or safety guidance.
- Automation location: `tests/test_markdown_first_contract.py`; command `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`.

### T2. Card and principle template shape

- Covers: R5, R6, R7, R8, R13, AC3, AC4
- Level: unit
- Fixture/setup: `docs/templates/exercise-card.md`, `docs/templates/principle-page.md`, and invalid template fixtures in `tests/fixtures/markdown-first/templates/`.
- Steps: Parse headings and top text; assert exercise template includes purpose, equipment setup, muscles involved, movement breakdown, feel cues, common mistakes, easier version, harder version, safety notes, and sources; assert principle template includes disclaimer, beginner explanation, scope boundaries, safety notes when applicable, and sources.
- Expected result: Valid templates pass; missing-section, missing-disclaimer, and missing-sources fixtures fail with file and rule identifiers.
- Failure proves: First-slice pages may be drafted from incomplete templates.
- Automation location: `tests/test_markdown_first_templates.py`.

### T3. Page-local disclaimer and source-section checker

- Covers: R7, R8, R13, R36, AC3, AC5
- Level: unit
- Fixture/setup: Valid and invalid Markdown fixtures in `tests/fixtures/markdown-first/pages/`.
- Steps: Run checker fixtures for missing disclaimer, disclaimer too low on the page, missing `Sources`, malformed heading, and valid page-local source structure.
- Expected result: The checker returns nonzero for invalid fixtures and reports the failing file plus rule code.
- Failure proves: Pages can be promoted without prominent safety framing or page-local sources.
- Automation location: `tests/test_markdown_first_page_structure.py` and `tools/checks/check_markdown_first.py`.

### T4. Claim-level citation and source quality minimum gate

- Covers: R9-R16, R36, AC5, AC6, EC1, EC2, EC14, EC16
- Level: unit
- Fixture/setup: Markdown fixtures with safety warnings, weekly activity guidance, technique claims, feel cues, reference-style links, global-only sources, and broken placeholder links.
- Steps: Run citation checker; assert safety stop rules require adjacent/reference-style citation and page-local source entry; assert reused source IDs must appear in `SOURCES.md`; assert global-only safety citation fails; assert broken or placeholder source URLs fail or are recorded as deferred/not ready.
- Expected result: Valid source-backed claims pass; unsupported safety claims, global-only citations, and missing page-local sources fail.
- Failure proves: Citation-based authority is not replacing unavailable expert review.
- Automation location: `tests/test_markdown_first_citations.py`; manual semantic citation review in `docs/changes/markdown-first-gym-primer/manual-proof/`.

### T5. Scope, language, and basic media guardrails

- Covers: R17-R25, R36, AC7, AC8, EC3, EC4, EC5, EC16
- Level: unit
- Fixture/setup: Fixtures for allowed Chinese alias, full Chinese translation, excluded scope terms, allowed no-media page, relative original SVG, external image URL, absolute local media path, and missing alt/adjacent media explanation.
- Steps: Run guardrail checks; assert allowed aliases pass; full translation fails; excluded advanced lifting, rehab, diagnosis, pain-treatment, and posture-correction terms fail; third-party or absolute media references fail; relative original SVG with alt or adjacent explanation passes.
- Expected result: v0.1 scope, language, and media boundaries are enforceable before content promotion.
- Failure proves: Higher-risk or unclear-license content can enter the first slice.
- Automation location: `tests/test_markdown_first_guardrails.py`.

### T6. Negative-match privacy scan

- Covers: R36, R37, AC11
- Level: unit
- Fixture/setup: Clean and forbidden-pattern fixtures under `tests/fixtures/markdown-first/privacy/`.
- Steps: Run `tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md` and unit tests for clean files, forbidden matches, missing target, and invalid pattern.
- Expected result: Clean scan exits `0`; forbidden match exits nonzero and redacts sensitive match details; setup errors are distinct from pass/fail content results.
- Failure proves: Privacy scanning can falsely pass or leak sensitive details.
- Automation location: `tests/test_markdown_first_privacy.py`; command `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md`.

### T7. Old platform supersession boundary

- Covers: R34, R35, EC15
- Level: contract
- Fixture/setup: Real files `docs/plans/2026-06-26-content-schema-foundation.md`, `docs/adr/2026-06-26-repository-native-reviewed-content.md`, `content/README.md`, `schemas/README.md`, `generated/README.md`, and `tools/validation/README.md`.
- Steps: Check that old plan and old ADR are marked superseded; check old implementation directories identify themselves as historical/superseded; check README/workflow no longer routes readers to generated JSON as v0.1 product.
- Expected result: Old artifacts remain traceable but cannot be mistaken for active v0.1 implementation guidance.
- Failure proves: Contributors may follow conflicting structured-platform instructions.
- Automation location: `tests/test_markdown_first_legacy_boundary.py`.

### T8. Real first-slice page integration

- Covers: R1-R25, R29-R30, R36, AC1-AC8, AC11, AC13, E1, E2, E4
- Level: integration
- Fixture/setup: Real files under `01-getting-started/`, `02-machines/`, `03-bodyweight/`, plus `README.md`, `SOURCES.md`, optional `media/`, and check scripts.
- Steps: Assert exactly the five required page paths exist; run `tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`; run privacy checks over content and proof records; run excluded-scope negative scan.
- Expected result: The real first slice satisfies the page contract, citation/source contract, scope/media guardrails, and privacy contract.
- Failure proves: The first slice is not promotable as active source content.
- Automation location: `tests/test_markdown_first_real_pages.py` and integration command in the plan.

### T9. README navigation and direct Markdown browsing smoke test

- Covers: R1-R4, AC2, E1
- Level: smoke
- Fixture/setup: `README.md` and the five first-slice page paths.
- Steps: Check README relative links resolve to the five pages; directly inspect pages as plain Markdown; confirm no generated HTML, JavaScript, database, account, app shell, or server is required to read them.
- Expected result: A reader can browse from README to every first-slice page in the repository.
- Failure proves: Markdown is not yet a usable primary product surface.
- Automation location: Link/path assertions in `tests/test_markdown_first_navigation.py`; direct inspection record in `docs/changes/markdown-first-gym-primer/manual-proof/`.

### T10. Beginner read-test and manual citation review

- Covers: R9-R12, R29, R38, R39, AC5, AC12, E1, E2, EC13, EC14, EC16
- Level: manual
- Fixture/setup: Non-identifying read-test template and completed records under `docs/changes/markdown-first-gym-primer/manual-proof/`.
- Steps: Ask at least one beginner reader the required questions for each exercise page: purpose, setup, steps, stop condition, and source they would click for a safety claim; record result without personally identifying details; manually inspect safety and technique citations for semantic support.
- Expected result: Each exercise page is either understood by the reader and citation-reviewed, or remains unpromoted with revision notes.
- Failure proves: Automated checks did not prove beginner comprehension or semantic citation support.
- Automation location: Manual proof files; optional presence checks in `tests/test_markdown_first_manual_evidence.py`.

### T11. Optional mdBook build or durable deferral

- Covers: R31-R33, R36, AC10, E5, EC12
- Level: smoke
- Fixture/setup: Five first-slice pages exist; optional `book.toml`, `SUMMARY.md`, `.gitignore`, and deferral note.
- Steps: Run `command -v mdbook || true`; if mdBook is installed and minimal config is adopted, run `mdbook build`; if missing or non-trivial, assert a deferral record explains the blocker and no generated HTML is treated as source.
- Expected result: mdBook either builds with minimal/default configuration or is explicitly deferred; Markdown remains canonical.
- Failure proves: Derived HTML is blocking Markdown proof or drifting into product source authority.
- Automation location: `tests/test_markdown_first_mdbook.py` plus manual command record.

### T12. Validation observability, command reporting, and performance

- Covers: R36, R40, AC11, AC13
- Level: smoke
- Fixture/setup: Check script output, test command output, manual proof records, and change-local validation notes.
- Steps: Verify checker failures identify file and rule; record exact commands run and skipped/unavailable commands; ensure local checks for the v0.1 slice complete under 30 seconds excluding network link checks; verify no CI pass is claimed without observed CI evidence.
- Expected result: Completion evidence is reproducible and honest about gaps.
- Failure proves: Reviewers cannot trust the validation record.
- Automation location: `tests/test_markdown_first_observability.py`; manual validation notes in `docs/changes/markdown-first-gym-primer/`.

### T13. Compatibility and migration boundary

- Covers: R20, R31-R35, EC12, EC15
- Level: migration
- Fixture/setup: README links, optional `SUMMARY.md`, old structured-platform files, old generated artifacts, and mdBook rollback or deferral evidence.
- Steps: Confirm future full Chinese translation is not active and no mixed-language full-card sections exist; confirm old generated JSON does not outrank Markdown; if mdBook is removed or deferred, README-linked Markdown remains usable; if `SUMMARY.md` exists, it points to the same Markdown source pages without replacing README navigation.
- Expected result: Compatibility surfaces are clear and rollback leaves Markdown usable.
- Failure proves: v0.1 can regress into the old platform or a generated-site source-of-truth model.
- Automation location: `tests/test_markdown_first_compatibility.py` and manual migration notes.

### T14. Deterministic media classification and provenance validation

- Covers: R23-R25, R36, R41-R43, R45-R53, AC8, AC14-AC19, E6-E8, EC5-EC10
- Level: unit
- Fixture/setup: Media fixtures under `tests/fixtures/markdown-first/media/` with temporary Markdown pages, local SVG files, raster files, and `media/PROVENANCE.md` variants.
- Steps: Run checker fixtures for text-only pages, `.svg` under `media/`, `.png`, `.jpg`, `.jpeg`, and `.webp` under `media/`, remote images, media outside `media/`, unsupported extensions, missing local media files, missing provenance, incomplete provenance, wrong `asset_type`, out-of-scope `media_purpose`, non-approved `review_status`, exact `asset_path` mismatch, leading `./` or `/` asset paths, and `page_refs` mismatch.
- Expected result: Text-only pages pass; SVG assets under `media/` pass without AI-raster provenance; raster assets under `media/` require one approved matching provenance row; invalid media fails with stable codes including `external_media_reference`, `media_outside_allowed_directory`, `unsupported_media_type`, `media_asset_missing`, `media_provenance_missing`, `media_provenance_incomplete`, `media_provenance_not_approved`, `media_usage_out_of_scope`, and `media_page_refs_mismatch`.
- Failure proves: The checker cannot enforce the approved v0.1 media boundary before first-slice pages reference images.
- Automation location: `tests/test_markdown_first_guardrails.py` or a focused `tests/test_markdown_first_media.py`; checker behavior in `tools/checks/check_markdown_first.py`.

### T15. Optional AI raster visual-safety and provenance review

- Covers: R23a, R23b, R41, R43, R44, AC14, AC15, EC11
- Level: manual
- Fixture/setup: Any optional AI-generated raster assets referenced by first-slice pages, their Markdown page references, and matching `media/PROVENANCE.md` rows. If no raster assets are added, use an explicit no-raster note.
- Steps: Inspect each referenced raster image and provenance row; confirm the image is necessary, limited to equipment identification or key movement illustration, visually simple, not decorative, not medical or rehab content, not an excluded lift, not identifying a private person, not branded in a misleading way, and not contradictory to the Markdown instructions; record reviewer role and pass/fail result without private data.
- Expected result: Every referenced AI raster image has human review evidence and approved provenance, or the proof record states that no raster images were added in M3A.
- Failure proves: Generated raster media can be promoted without the human visual-safety judgment required by the spec.
- Automation location: `docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md`; optional presence check in `tests/test_markdown_first_manual_evidence.py`.

## Fixtures and data

Planned automated fixtures:

- `tests/fixtures/markdown-first/pages/valid-exercise.md`
- `tests/fixtures/markdown-first/pages/valid-principle.md`
- `tests/fixtures/markdown-first/pages/invalid-missing-disclaimer.md`
- `tests/fixtures/markdown-first/pages/invalid-missing-sources.md`
- `tests/fixtures/markdown-first/pages/invalid-global-only-safety-source.md`
- `tests/fixtures/markdown-first/pages/invalid-stop-rule-no-citation.md`
- `tests/fixtures/markdown-first/pages/valid-chinese-alias.md`
- `tests/fixtures/markdown-first/pages/invalid-full-chinese-translation.md`
- `tests/fixtures/markdown-first/pages/invalid-excluded-scope.md`
- `tests/fixtures/markdown-first/media/text-only-page.md`
- `tests/fixtures/markdown-first/media/svg-under-media.md`
- `tests/fixtures/markdown-first/media/png-missing-provenance.md`
- `tests/fixtures/markdown-first/media/jpg-missing-provenance.md`
- `tests/fixtures/markdown-first/media/jpeg-missing-provenance.md`
- `tests/fixtures/markdown-first/media/webp-missing-provenance.md`
- `tests/fixtures/markdown-first/media/png-approved-provenance.md`
- `tests/fixtures/markdown-first/media/png-unapproved-provenance.md`
- `tests/fixtures/markdown-first/media/png-incomplete-provenance.md`
- `tests/fixtures/markdown-first/media/png-out-of-scope-purpose.md`
- `tests/fixtures/markdown-first/media/png-page-ref-mismatch.md`
- `tests/fixtures/markdown-first/media/png-asset-path-mismatch.md`
- `tests/fixtures/markdown-first/media/remote-image.md`
- `tests/fixtures/markdown-first/media/image-outside-media.md`
- `tests/fixtures/markdown-first/media/unsupported-gif.md`
- `tests/fixtures/markdown-first/media/missing-local-asset.md`
- `tests/fixtures/markdown-first/privacy/clean/`
- `tests/fixtures/markdown-first/privacy/forbidden-pattern/`
- `tests/fixtures/markdown-first/mdbook/valid-minimal/`
- `tests/fixtures/markdown-first/mdbook/deferred/`

Manual proof records:

- `docs/changes/markdown-first-gym-primer/manual-proof/README.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP1-direct-markdown-render.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP2-citation-semantic-review.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP5-validation-command-ledger.md`
- `docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md`

Reader-test records must avoid names, contact details, private health details, and local machine paths. Use a non-identifying reader description such as "beginner reader, first 90 days of gym training."

## Mocking/stubbing policy

- Do not mock file parsing for integration tests over the real first-slice pages.
- Unit tests may use temporary directories and fixture files to isolate individual checker rules.
- Do not call external websites in unit tests. Link health can be manual or optional tool evidence because network behavior is unstable.
- Do not mock mdBook success. If `mdbook build` is claimed, run the real command locally and record the result. If mdBook is unavailable, record deferral.
- Do not use AI-generated exercise wording as test oracle. Content checks prove structure, source linkage, and boundaries; human review proves meaning.

## Migration or compatibility tests

- T7 proves old structured-platform artifacts are superseded in place and traceable.
- T11 proves mdBook output is derived or deferred.
- T13 proves README-linked Markdown remains usable if mdBook is removed or never added.
- Future locale migration is not implemented in v0.1; tests only assert that full Chinese translation is absent and any future separate-locale structure is not active source content without a reviewed follow-up.

## Observability verification

Checker output must identify:

- file path relative to repository root;
- rule ID or check name;
- failing section, source ID, media reference, normalized `asset_path`, media
  classification, provenance field, scope term, or privacy category when
  applicable;
- pass/fail/error status with distinct exit behavior.

Media validation output must identify:

- Markdown page path;
- referenced media path;
- normalized repository-relative `asset_path`;
- extension-based classification;
- provenance path when relevant;
- stable failure code.

Manual records must identify:

- inspected files;
- questions asked;
- pass/fail result;
- exact commands run;
- skipped tools and residual risk.

Do not include secrets, private health details, local absolute paths, or personally identifying reader details in validation output.

## Security/privacy verification

- T5 rejects undocumented third-party media and absolute local media paths.
- T6 verifies negative-match privacy semantics and redacted findings.
- T14 rejects remote images, media outside `media/`, unsupported image
  extensions, missing local assets, unprovenanced raster media, incomplete
  provenance, non-approved provenance, out-of-scope purpose, and mismatched
  page references.
- T15 verifies that optional AI-generated raster illustrations do not include
  private people, misleading branding, medical/rehab content, or unsafe
  contradictory movement details.
- T8 runs privacy checks over first-slice content and manual proof records.
- T10 requires non-identifying reader-test records.
- T12 prevents unobserved CI claims and requires skipped-tool disclosure.

## Performance checks

- Local Markdown-first unit and integration checks should complete in under 30 seconds on the v0.1 slice, excluding network-dependent link checking.
- Record command duration when practical with `time` or the test runner output.
- Performance failure does not block Markdown readability, but it blocks claiming the local quality gate is ergonomic.

## Manual QA checklist

- Open `README.md` and confirm navigation reaches the five required pages by relative links.
- Open each page as Markdown and confirm it is readable without generated HTML.
- Confirm each page has a near-top disclaimer.
- Confirm each exercise page has purpose, setup, muscles, movement breakdown, feel cues, common mistakes, easier version, harder version, safety notes, and sources.
- Confirm the principle page has beginner explanation, scope boundaries, safety notes where applicable, and sources.
- Inspect every safety warning for claim-level citation and page-local source entry.
- Inspect weekly activity guidance for a public-health or professional guidance source.
- Confirm reused sources appear in `SOURCES.md`.
- Confirm no page teaches excluded advanced lifts, rehab, diagnosis, posture correction, pain treatment, or sport-specific programming.
- Confirm media is absent, an original SVG under `media/`, or an approved
  AI-generated raster illustration under `media/` with relative path and alt or
  adjacent explanation.
- Confirm `media/PROVENANCE.md` exists with the required table schema once M3A
  is implemented, even if it has no raster asset rows.
- If raster media is referenced, confirm its provenance row has exact
  `asset_path`, `asset_type = ai_generated_raster`, allowed `media_purpose`,
  `review_status = approved`, non-blank required fields, and matching
  `page_refs`.
- Complete the beginner read test and record non-identifying evidence.
- Record mdBook build success or durable deferral.

## What not to test and why

- Do not test hosted website routing, analytics, CMS, accounts, frontend search, or deployment because they are out of v0.1 scope.
- Do not test formal expert-review lifecycle or reviewer tiers because citation-based authority replaces that model for v0.1.
- Do not test generated public JSON as a product surface because the approved spec rejects it for v0.1.
- Do not test full Chinese translation behavior beyond rejection of mixed full-card translation because active locale work is deferred.
- Do not test a broad external media licensing workflow because v0.1 rejects
  third-party assets and allows only original SVGs or approved AI-generated
  raster illustrations with centralized provenance.
- Do not test original raster drawings or photos as separate allowed media
  categories because v0.1 treats raster images under `media/` as AI-generated
  raster illustrations requiring provenance.
- Do not test clinical rehab, diagnosis, pain-treatment, or personalized coaching flows because they are forbidden.
- Do not require CI evidence unless CI is actually configured and observed.

## Uncovered gaps

None that require returning to spec or architecture before test-spec-review.

Known validation limitations to preserve in review:

- Automated citation checks can only prove presence and locality of citations, not semantic authority. Manual citation review remains required.
- Link checking may be manual or optional-tool evidence until the project chooses and installs a link checker.
- mdBook is conditional. The required proof is either a real `mdbook build` from minimal config or a durable deferral record.
- Named maintainer authority for citation/scope acceptance remains an open spec question, but it does not block proof design because manual review evidence can record the reviewer role used for the first slice.

## Next artifacts

- `test-spec-review` for this M3A media proof-map update.
- After clean test-spec-review, implement M3A from
  `docs/plans/2026-06-27-markdown-first-gym-primer.md`.

## Follow-on artifacts

None yet

## Readiness

This test spec is ready for test-spec-review. It is not implementation-ready,
code-review-ready, verification-ready, branch-ready, or PR-ready until
test-spec-review approves the M3A media proof-map update and the workflow
advances.
