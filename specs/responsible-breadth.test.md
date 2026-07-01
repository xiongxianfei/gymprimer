# Test Spec: Responsible Breadth Content Expansion

## Status

draft

## Related spec and plan

- Spec: `specs/responsible-breadth.md`
- Spec review:
  - `docs/changes/responsible-breadth/reviews/spec-review-r2.md`
  - `docs/changes/apt-pattern-architecture/reviews/spec-review-r2.md`
- Compatibility spec: `specs/markdown-first-primer.md`
- Plan: `docs/plans/2026-06-29-responsible-breadth.md`
- Follow-up change metadata:
  - `docs/changes/apt-pattern-architecture/change.yaml`
- Plan review:
  - `docs/changes/responsible-breadth/reviews/plan-review-r1.md`
- Architecture/ADRs:
  - `docs/architecture/system/architecture.md`
  - `docs/changes/responsible-breadth/reviews/architecture-review-r1.md`
  - `docs/changes/apt-pattern-architecture/reviews/architecture-review-r2.md`
  - `docs/adr/2026-06-29-responsible-breadth-static-content-boundaries.md`
  - `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`
  - `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
  - `docs/adr/2026-06-29-expanded-raster-media-purposes.md`

## Testing strategy

The proof strategy combines path-scoped automated checks, real-page integration
tests, and bounded audit records for semantic safety and source-quality
judgments.

- Unit: checker tests for Responsible Breadth page-class classification,
  required sections, red-flag order, metadata/review cadence, source-count
  minimums, excluded-scope language, pattern-page exercise preview contracts,
  and inherited plus expanded media/provenance behavior.
- Integration: run the Markdown-first checker against real Responsible Breadth
  surfaces: `SOURCES.md`, `about/`, `patterns/`, `conditions/`, `principles/`,
  `programs/`, optional `media/`, and change-local validation records.
- End-to-end: validate that README or other active navigation links expanded
  pages only after evidence exists, and that every linked expanded page remains
  readable as Markdown without generated HTML or runtime services.
- Smoke: assert the first expanded proof slice exists, paths map to exactly one
  page class, required metadata is present, and final evidence is current.
- Audit: perform semantic source-quality review, safety/scope-boundary review,
  visual-necessity and purpose-specific media review when media exists, and
  beginner comprehension review.
- Contract: prove the same-rank compatibility boundary between
  `specs/responsible-breadth.md` and `specs/markdown-first-primer.md`.
- Migration: prove original numbered v0.1 pages remain governed by the
  Markdown-first spec and are not forced into expanded page classes.

Existing `test_markdown_first_*.py` tests remain regression coverage for shared
Markdown, citation, media, privacy, and mdBook behavior. Responsible Breadth
tests should use Python standard-library `unittest`, temporary directories, and
subprocess-style checker calls consistent with the current repository style.

## Milestone and proof ownership

Proof classifications:

| Classification | Meaning |
| --- | --- |
| existing | Command, fixture, or proof already exists and must pass now. |
| planned-for-milestone | Proof is required by the owning milestone and may be absent before then. |
| audit-record | Proof is collected by bounded audit evidence rather than automation. |
| conditional/external | Proof depends on an optional external tool or documented deferral path. |

Before a proof's owning milestone, absence is not failure unless the proof is
marked pre-milestone required. At and after the owning milestone, absence,
unexpected nonzero exit, missing fixture, missing audit evidence, or missing
closeout record fails the milestone.

## Test ownership map

| Test ID | Proof area | Owner | Owning milestone | First meaningful execution | Classification | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RB-T1 | Page-class classification | tooling maintainer | M1 | M1 | planned-for-milestone | `tests/test_responsible_breadth_classification.py` |
| RB-T2 | Required expanded page sections | tooling maintainer | M1 | M1 | planned-for-milestone | `tests/test_responsible_breadth_page_contract.py` |
| RB-T3 | Red-flag routing and order | tooling maintainer | M1 | M1 | planned-for-milestone | red-flag fixture tests |
| RB-T4 | Metadata and review cadence | tooling maintainer | M1 | M1 | planned-for-milestone | metadata/review-cadence fixture tests |
| RB-T5 | Source count, source-index validity, and citation locality | tooling maintainer | M1 | M1 | planned-for-milestone | source fixture tests |
| RB-T6 | Excluded scope and non-prescription guardrails | tooling maintainer | M1 | M1 | planned-for-milestone | diagnosis/treatment/rehab/personalization fixture tests |
| RB-T7 | Evidence-record contract | release/check maintainer | M1 | M1 | planned-for-milestone | test-spec audit-record checks |
| RB-T8 | Red-flags reference contract | content maintainer | M2 | M2 | planned-for-milestone | `about/red-flags.md` tests and non-triage audit evidence |
| RB-T9 | Expanded templates contract | content maintainer | M2 | M2 | planned-for-milestone | `docs/templates/*` tests |
| RB-T10 | Source seed and contributor guidance | content maintainer | M2 | M2 | planned-for-milestone | `SOURCES.md` and `CONTRIBUTING.md` tests |
| RB-T11 | First expanded proof slice integration | content maintainer | M3 | M3 | planned-for-milestone | real-page integration test output |
| RB-T12 | Pattern/condition semantic safety proof | content maintainer | M3 | M3 | audit-record | bounded source/scope audit evidence |
| RB-T13 | Programming and program-example boundary proof | content maintainer | M3 | M3 | audit-record | bounded source/scope audit evidence |
| RB-T14 | Reader comprehension proof | reader-test facilitator | M3 | M3 | audit-record | non-identifying comprehension evidence |
| RB-T15 | Visual necessity and media provenance | media reviewer | M3 when media exists; otherwise M4 no-media note | conditional/external | media validation evidence or explicit no-media note |
| RB-T16 | Navigation promotion gate | release/check maintainer | M4 | M4 | planned-for-milestone | README/SUMMARY navigation tests |
| RB-T17 | Final validation ledger and lifecycle sync | release/check maintainer | M4 | M4 | audit-record | final validation ledger |
| RB-T18 | mdBook build or deferral | release/check maintainer | M4 | M4 | conditional/external | deferral record or build transcript |
| RB-T19 | Compatibility with original v0.1 slice | release/check maintainer | M4 | M4 | planned-for-milestone | compatibility regression test output |
| RB-T20 | Privacy scan over expanded content and proof | tooling maintainer | M2-M4 | M2 | planned-for-milestone | privacy command transcript |
| RB-T21 | Pattern-page architecture and exercise previews | content/check maintainer | APT amendment | APT amendment | planned-for-milestone | real APT page and fixture integration tests |
| RB-T22 | Expanded raster media-purpose validation | media/check maintainer | APT amendment | APT amendment | planned-for-milestone | media-purpose fixture tests and visual-media proof |

## Planned validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | Required starting | Allowed before owning milestone? | Expected failure behavior | Closeout evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RB-CMD1 | `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` | planned-for-milestone | tooling maintainer | M1 | M1 | yes | From M1, zero discovered tests or unexpected nonzero exit fails the milestone. | test runner transcript |
| RB-CMD2 | `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | existing | tooling maintainer | M1 | now | yes | Any unexpected nonzero exit fails because shared Markdown-first behavior must not regress. | test runner transcript |
| RB-CMD3 | `python3 tools/checks/check_markdown_first.py --help` | existing | tooling maintainer | M1 | now | yes | Missing command or nonzero help exit fails M1. | command transcript |
| RB-CMD4 | `python3 tools/checks/check_markdown_first.py SOURCES.md about` | planned-for-milestone | tooling maintainer | M2 | M2 | yes | From M2, nonzero exit blocks project-level references. | checker transcript |
| RB-CMD5 | `python3 tools/checks/check_markdown_first.py SOURCES.md about patterns conditions principles programs` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | From M3, nonzero exit blocks the expanded proof slice. | checker transcript |
| RB-CMD6 | `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs` | planned-for-milestone | release/check maintainer | M4 | M4 | yes | From M4, nonzero exit blocks promotion. | checker transcript |
| RB-CMD7 | `python3 tools/checks/check_privacy.py docs/changes/responsible-breadth specs/responsible-breadth.md specs/markdown-first-primer.md` | existing | tooling maintainer | M1 | now | yes | Forbidden findings or setup errors fail. | privacy transcript |
| RB-CMD8 | `python3 tools/checks/check_privacy.py SOURCES.md CONTRIBUTING.md about docs/templates docs/changes/responsible-breadth` | planned-for-milestone | tooling maintainer | M2 | M2 | yes | From M2, forbidden findings or setup errors fail. | privacy transcript |
| RB-CMD9 | `python3 tools/checks/check_privacy.py SOURCES.md about patterns conditions principles programs docs/changes/responsible-breadth` | planned-for-milestone | tooling maintainer | M3 | M3 | yes | From M3, forbidden findings or setup errors fail. | privacy transcript |
| RB-CMD10 | `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media` | planned-for-milestone | release/check maintainer | M4 | M4 | yes | From M4, forbidden findings or setup errors fail. | privacy transcript |
| RB-CMD11 | `command -v mdbook \|\| true` | conditional/external | release/check maintainer | M4 | M4 | yes | Never proves readiness; determines build or deferral path. | command transcript |
| RB-CMD12 | `mdbook build` | conditional/external | release/check maintainer | M4 | M4 if configured and available | yes | From M4, either build succeeds or a deferral record explains why mdBook is unavailable. | build transcript or deferral record |

## Bounded audit evidence ownership

Separate proof artifact trees are not required by this test spec. Where automation cannot
fully prove semantic source support, scope boundaries, comprehension, visual
necessity, lifecycle synchronization, or mdBook deferral, the owning change MUST
record bounded audit or validation evidence.

Bounded audit records must include owner role, owning milestone or change,
automation rationale, files inspected, exact criteria or steps, pass/fail
result, re-run trigger, and a privacy statement that no identifying reader
details or private health profiles are included.

## Milestone closeout proof

| Milestone | Automated proof required | Additional evidence required | Closeout rule |
| --- | --- | --- | --- |
| M1 | RB-T1 through RB-T7; RB-CMD1, RB-CMD2, RB-CMD3, RB-CMD7 | None beyond evidence-contract coverage | M1 closes when expanded path classification, structural checks, guardrails, and evidence contracts exist without regressing Markdown-first checks. |
| M2 | RB-T8 through RB-T10, RB-T20; RB-CMD4, RB-CMD8 | Red-flags non-triage audit evidence where automation cannot prove semantics | M2 closes when red flags, templates, sources, contributor guidance, and non-triage evidence exist. |
| M3 | RB-T11 through RB-T15, RB-T20; RB-CMD5, RB-CMD9 | Source/scope, comprehension, and media evidence as applicable | M3 closes when the four dependent expanded pages pass checks, remain draft-only, and have source/scope/comprehension evidence. |
| M4 | RB-T16 through RB-T20; RB-CMD6, RB-CMD10, RB-CMD11, RB-CMD12 or deferral | Final validation ledger and mdBook build/deferral evidence | M4 closes when navigation promotes only fully proven pages and final evidence is current. |

Follow-up APT amendment proof closes when RB-T21 and RB-T22 pass against the
real APT pattern page, linked exercise pages, generated raster media
provenance, and change-local validation evidence. This amendment does not
reopen the original M1-M4 milestone scope.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | RB-T11, RB-T16, RB-T19 | integration, smoke, migration | Expanded pages must be repository-readable Markdown and remain compatible with the original slice. |
| R2 | RB-T1, RB-T11 | unit, integration | Path classification and real-page tests prove allowed top-level directories. |
| R3 | RB-T11, RB-T17 | integration, audit | Real-page and ledger checks prove the exact five-category proof slice before scaling. |
| R4 | RB-T11 | integration | Confirms expected first-slice paths or records reviewed architecture alternative. |
| R5 | RB-T2, RB-T11 | unit, integration | Pattern/condition required sections are fixture-tested and checked on real pages. |
| R5a | RB-T2, RB-T11 | unit, integration | Condition pages are fixture-tested against the additional required condition sections. |
| R6 | RB-T2, RB-T6, RB-T11 | unit, integration | Forbidden diagnosis/treatment/corrective-routine headings fail. |
| R7 | RB-T3, RB-T11 | unit, integration | Red-flags link must appear before self-management discussion. |
| R8 | RB-T2, RB-T12, RB-T14 | unit, audit | Non-diagnostic/no-treatment statement is checked structurally and through bounded audit evidence. |
| R9 | RB-T6, RB-T11, RB-T12 | unit, integration, audit | Condition page scope is checked against path and content boundaries. |
| R10 | RB-T6, RB-T12 | unit, audit | Pattern page must not frame posture as diagnosis or guaranteed problem. |
| R11 | RB-T6, RB-T13 | unit, audit | Principle page must use general concepts and no individual adaptation. |
| R12 | RB-T6, RB-T13 | unit, audit | Program-example page must remain static for general healthy beginners. |
| R13 | RB-T6, RB-T13 | unit, audit | User-input, routing, personal load, symptom adaptation, and injury progression fail. |
| R14 | RB-T2, RB-T13 | unit, audit | Scope note must make non-prescription framing visible. |
| R15 | RB-T5, RB-T11, RB-T17 | unit, integration, audit | Minimum three named authoritative sources checked for each content page. |
| R16 | RB-T5, RB-T12 | unit, audit | Pattern source-quality mix is reviewed. |
| R17 | RB-T5, RB-T12 | unit, audit | Condition source-quality mix is reviewed. |
| R18 | RB-T5, RB-T13 | unit, audit | Public-health and resistance-training source mix checked for relevant principles. |
| R19 | RB-T5, RB-T13 | unit, audit | Program-example source mix includes public-health, resistance-training, and illustration source. |
| R20 | RB-T5, RB-T11 | unit, integration | Source-index and page-local source presence are checked. |
| R21 | RB-T5, RB-T12, RB-T13 | unit, audit | Safety warnings need claim-level citations and semantic support evidence. |
| R22 | RB-T2, RB-T12, RB-T13 | unit, audit | Uncertainty/mixed-evidence section and audit evidence cover source disagreement. |
| R23 | RB-T4, RB-T11 | unit, integration | Metadata fields required on every expanded page. |
| R24 | RB-T4, RB-T17 | unit, audit | Safety-relevant first review date no later than 90 days. |
| R25 | RB-T4, RB-T17 | unit, audit | Pattern review cadence verified. |
| R26 | RB-T4, RB-T17 | unit, audit | Condition, program-example, and red-flags cadence verified. |
| R27 | RB-T4, RB-T17 | unit, audit | Exercise/principle cadence rules are checked when those page classes exist. |
| R28 | RB-T4, RB-T17 | unit, audit | Triggered review events are represented in validation ledger checks. |
| R29 | RB-T15, RB-T22 | audit, unit | Visual necessity is audit evidence; media path/provenance/purpose behavior is fixture-tested. |
| R29a | RB-T15, RB-T22 | audit, unit | Expanded pages prefer high-quality reviewed raster images when realistic beginner-readable detail is needed. |
| R29b | RB-T15, RB-T22 | audit, unit | SVG remains allowed only when simple enough and passing visual-necessity review. |
| R30 | RB-T15 | audit | Machine setup visuals are conditional and reviewed when present. |
| R31 | RB-T15 | audit | Movement visuals are conditional and reviewed when present. |
| R32 | RB-T15 | audit | Overlays/wrong frames/alignment diagrams require material-comprehension rationale. |
| R33 | RB-T15 | audit | Regression visual change rule is checked when such visuals exist. |
| R34 | RB-T15, Markdown-first media regression tests | audit, unit | Relative path and alt/adjacent explanation use inherited Markdown-first media checks. |
| R35 | RB-T15, RB-T22, Markdown-first media regression tests | audit, unit | Raster media inherits `media/PROVENANCE.md` contract. |
| R35a | RB-T15, RB-T22 | audit, unit | Human-reviewed AI-generated raster images are allowed only as support assets with provenance. |
| R35b | RB-T15, RB-T22 | audit, unit | Generated raster images cannot become source of truth for anatomy, technique, safety, diagnosis, treatment, or programming. |
| R35c | RB-T22 | unit | Expanded `media_purpose` enum values are accepted only for expanded Responsible Breadth pages. |
| R35d | RB-T15, RB-T22 | audit, unit | Pattern alignment images use `pattern_alignment_illustration` only for non-diagnostic visual comparison. |
| R35e | RB-T15, RB-T22 | audit, unit | Condition anatomy images use `anatomical_region_illustration` only for plain region context. |
| R35f | RB-T15, RB-T21, RB-T22 | audit, unit, integration | Exercise preview images support pattern/condition pages without replacing exercise instructions. |
| R36 | RB-T7, RB-T12, RB-T13, RB-T17 | audit, integration | Higher-bar review evidence is required for expanded pages. |
| R37 | RB-T7, RB-T12, RB-T13 | audit | Source traceability, red flags, non-diagnosis, no treatment, no personalization, and scope fit are evidence fields. |
| R38 | RB-T6, RB-T11 | unit, integration | Excluded populations/categories fail automated and real-page checks. |
| R39 | RB-T6, RB-T12, RB-T13 | unit, audit | Diagnosis, treatment, rehab, posture promise, and injury protocol fail. |
| R40 | RB-T6, RB-T16, RB-T19 | unit, smoke, migration | No symptom checker, runtime API, hosted app, CMS, or AI source-of-truth surfaces. |
| R41 | RB-T16, RB-T17 | smoke, audit | Promotion requires completed lifecycle evidence. |
| R42 | RB-T14 | audit | Comprehension evidence covers purpose, boundary, red flags/stop condition, and source verification. |
| R43 | RB-T14 | audit | Pattern/condition reader must understand no diagnosis. |
| R44 | RB-T14 | audit | Program-example reader must understand no personal prescription. |
| R45 | RB-T1 through RB-T6, RB-T11 | unit, integration | Validation tooling should fail missing sections, metadata, sources, red flags, media, and scope guardrails. |
| R46 | RB-T12, RB-T13, RB-T14, RB-T15 | audit | Semantic source quality and scope-boundary evidence are required. |
| R47 | RB-T8 | integration, audit | Red-flags reference distinguishes emergency, prompt, and professional care. |
| R48 | RB-T8 | integration, audit | Red-flags reference must not diagnose or choose the reader's condition. |
| R49 | RB-T10, RB-T11 | unit, integration | Reused Responsible Breadth sources appear in `SOURCES.md`. |
| R50 | RB-T16 | smoke | Active navigation cannot promote expanded pages until evidence exists. |
| R51 | RB-T1, RB-T11 | unit, integration | Page has exactly one Responsible Breadth page class before validation. |
| R52 | RB-T1 | unit | First-slice path classification table is enforced. |
| R53 | RB-T1 | unit | Ambiguous paths require an equivalent page-local type before promotion. |
| R54 | RB-T19 | migration | Responsible Breadth supersedes Markdown-first scope limits only for expanded classes. |
| R55 | RB-T19, RB-CMD2 | migration, unit | Shared Markdown-first rules continue unless stricter here. |
| R56 | RB-T19 | migration | Original five-page v0.1 slice remains governed by Markdown-first spec. |
| R57 | RB-T21 | integration | Pattern pages follow pain point to pattern to core contributors to exercise options. |
| R58 | RB-T21 | integration | `Why beginners come to this page` includes three to five reader-facing entry points. |
| R59 | RB-T21 | integration | `The core reason` includes three to five named contributors with citations. |
| R60 | RB-T6, RB-T12, RB-T21 | unit, audit, integration | `What commonly helps` remains an educational menu, not routine/prescription/guaranteed fix. |
| R61 | RB-T21 | integration | Each linked exercise preview includes fix reason, used muscles, and one important note. |
| R62 | RB-T21 | integration | Exercise previews link only to existing exercise pages unless the page is draft-only and marked unavailable. |
| R63 | RB-T15, RB-T21, RB-T22 | audit, integration, unit | Optional preview images require existing media, alt/adjacent text, and passing provenance. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | RB-T2, RB-T3, RB-T12, RB-T14 | Pattern page non-diagnostic framing and comprehension proof. |
| E2 | RB-T3, RB-T8, RB-T12, RB-T14 | Condition page red-flag routing and urgent/individual boundary. |
| E3 | RB-T6, RB-T13, RB-T14 | Static program example and non-prescription comprehension. |
| E4 | RB-T5, RB-T12 | Three weak sources fail source-quality review. |
| E5 | RB-T15, Markdown-first media regression tests | Necessary visuals pass without mandatory overlay. |
| E6 | RB-T11, RB-T17 | First expanded proof slice remains narrow. |
| E7 | RB-T19 | Original five-page slice remains governed by Markdown-first. |
| E8 | RB-T1, RB-T2, RB-T3, RB-T12 | Responsible Breadth pattern page allowed only under full contract. |
| E9 | RB-T6, RB-T12 | Condition page that becomes treatment fails. |
| E10 | RB-T6, RB-T13 | Static program example allowed only without personalization. |
| E11 | RB-T21 | APT-style pattern page routes reader pain point to pattern explanation, core contributors, and bounded exercise previews. |
| E12 | RB-T22 | Generated pattern alignment image passes only with `pattern_alignment_illustration` purpose and support-only framing. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | RB-T6, RB-T12 | unit, audit | Pattern page says reader "has" the pattern. |
| EC2 | RB-T2, RB-T6, RB-T12 | unit, audit | Condition page uses treatment-plan framing. |
| EC3 | RB-T6, RB-T13 | unit, audit | Program says "follow this program" as prescription. |
| EC4 | RB-T3, RB-T11 | unit, integration | Red-flags link appears only at bottom. |
| EC5 | RB-T5, RB-T12 | unit, audit | Three sources are present but all weak. |
| EC6 | RB-T15 | audit | Visual introduces anatomy claims absent from Markdown/citations. |
| EC7 | RB-T20, RB-T14 | unit, audit | Reader-test note includes a private health profile. |
| EC8 | RB-T17 | audit | Source link rot triggers review before page remains current. |
| EC9 | RB-T6, RB-T11 | unit, integration | Condition page targets pregnancy, post-surgical, pediatric, or other excluded scope. |
| EC10 | RB-T6, RB-T13 | unit, audit | Program example includes injury-specific substitution. |
| EC11 | RB-T21 | integration | Pattern page links an exercise preview to a missing exercise page. |
| EC12 | RB-T21 | integration | Exercise preview omits fix reason, used muscles, or important note. |
| EC13 | RB-T22 | unit | Generated expanded-page image lacks an approved provenance row. |
| EC14 | RB-T22 | unit | Pattern alignment image uses `key_movement_illustration` instead of `pattern_alignment_illustration`. |
| EC15 | RB-T15, RB-T22 | audit, unit | Condition anatomy image implies diagnosis, pathology, or treatment despite provenance. |

## Test cases

### RB-T1. Responsible Breadth page-class classification

- Covers: R1, R2, R51, R52, R53, E8
- Level: unit
- Fixture/setup: Temporary fixture tree with files under `patterns/`,
  `conditions/`, `principles/`, `programs/`, `exercises/`, `about/`, and an
  ambiguous unsupported path.
- Steps: Run the checker or classification helper; assert each allowed path
  maps to exactly one class and unsupported paths require a page-local type
  before promotion.
- Expected result: Allowed first-slice paths classify deterministically;
  ambiguous/unclassified paths fail with a stable page-class message.
- Failure proves: Downstream validation cannot route pages to the right
  contract.
- Automation location: `tests/test_responsible_breadth_classification.py`.

### RB-T2. Required expanded page sections

- Covers: R5, R6, R8, R14, R22, R45, E1, E8, EC2
- Level: unit
- Fixture/setup: Valid and invalid pattern, condition, principle, and program
  fixtures under `tests/fixtures/responsible-breadth/page-contracts/`.
- Steps: Run checker fixtures for required sections and forbidden headings.
- Expected result: Valid fixtures pass; missing required sections and forbidden
  diagnosis/treatment/fix/corrective-routine sections fail.
- Failure proves: Expanded pages can be structurally promoted without the
  visible reader contract.
- Automation location: `tests/test_responsible_breadth_page_contract.py`.

### RB-T3. Red-flag routing order

- Covers: R7, R47, R48, E2, EC4
- Level: unit
- Fixture/setup: Fixtures with red-flags links before self-management, missing
  red-flags links, and red-flags links after self-management.
- Steps: Run checker fixtures and inspect failure codes.
- Expected result: Safety-relevant pages pass only when red-flag routing
  precedes self-management discussion.
- Failure proves: Readers can reach self-management language before safety
  routing.
- Automation location: `tests/test_responsible_breadth_red_flags.py`.

### RB-T4. Metadata and review cadence

- Covers: R23, R24, R25, R26, R27, R28
- Level: unit
- Fixture/setup: Fixtures with valid metadata, missing metadata, stale review
  dates, and invalid next-review cadence by page class.
- Steps: Run checker fixtures.
- Expected result: Every page has author, created date, last reviewed, next
  review due, and review scope; cadence rules fail when invalid.
- Failure proves: Expanded content can become current without review ownership
  or maintenance timing.
- Automation location: `tests/test_responsible_breadth_metadata.py`.

### RB-T5. Source count and source-index validity

- Covers: R15, R16, R17, R18, R19, R20, R21, R49, E4, EC5
- Level: unit
- Fixture/setup: Expanded-page fixtures with sufficient sources, too few
  sources, reused source IDs missing from `SOURCES.md`, and global-only safety
  citations.
- Steps: Run checker fixtures.
- Expected result: Source-count and source-index failures produce stable
  messages; safety warnings need page-local claim-level citations.
- Failure proves: Expanded pages can pass on citation count alone or with
  unverifiable safety claims.
- Automation location: `tests/test_responsible_breadth_sources.py`.

### RB-T6. Scope and personalization guardrails

- Covers: R6, R9, R10, R11, R12, R13, R38, R39, R40, E3, E9, E10, EC1, EC2,
  EC3, EC9, EC10
- Level: unit
- Fixture/setup: Fixtures containing diagnosis language, treatment-plan
  language, rehab progressions, posture-correction promises, acute/specialized
  population terms, symptom-collection prompts, and adaptive programming.
- Steps: Run checker fixtures.
- Expected result: Excluded clinical, rehab, treatment, diagnosis,
  personalization, and runtime-product language fails.
- Failure proves: Expanded pages can cross the core safety/product boundary.
- Automation location: `tests/test_responsible_breadth_guardrails.py`.

### RB-T7. Evidence-record contract

- Covers: R36, R37, R42, R43, R44, R46
- Level: smoke
- Fixture/setup: `specs/responsible-breadth.test.md`.
- Steps: Check that bounded audit evidence requirements name owner roles, files
  inspected, pass/fail result, rerun triggers, privacy rule, and milestone or
  change ownership without requiring a separate proof artifact tree.
- Expected result: Audit records have a stable shape before content pages rely
  on them.
- Failure proves: Semantic review obligations can be skipped or recorded
  inconsistently.
- Automation location: `tests/test_responsible_breadth_m1.py`.

### RB-T8. Red-flags reference contract

- Covers: R47, R48, E2
- Level: integration
- Fixture/setup: Real `about/red-flags.md`.
- Steps: Run checker and audit evidence review; assert emergency, prompt
  medical care, and professional assessment concepts are present without
  diagnosis or condition-selection language.
- Expected result: The red-flags reference routes past project content without
  triage.
- Failure proves: The project-level safety artifact is unsafe for expanded
  content.
- Automation location: `tests/test_responsible_breadth_references.py`.

### RB-T9. Expanded templates contract

- Covers: R5, R6, R8, R14, R23
- Level: contract
- Fixture/setup: `docs/templates/pattern-page.md`,
  `docs/templates/condition-page.md`, `docs/templates/programming-principle-page.md`,
  and `docs/templates/program-example-page.md`.
- Steps: Check templates contain required headings, metadata fields, source
  sections, and non-diagnostic/non-prescription boundary prompts.
- Expected result: Templates guide contributors into compliant pages.
- Failure proves: Future pages can start from a non-compliant scaffold.
- Automation location: `tests/test_responsible_breadth_templates.py`.

### RB-T10. Source seed and contributor guidance

- Covers: R15-R21, R36, R37, R49
- Level: contract
- Fixture/setup: `SOURCES.md` and `CONTRIBUTING.md`.
- Steps: Check reusable sources used by more than one expanded page are in
  `SOURCES.md`; contributor guidance names higher-bar review for patterns,
  conditions, and program examples.
- Expected result: Source reuse and contribution workflow support expanded
  review standards.
- Failure proves: Contributors cannot discover the evidence and review bar.
- Automation location: `tests/test_responsible_breadth_contract.py`.

### RB-T11. First expanded proof-slice integration

- Covers: R1-R5, R7, R15-R28, R38, R41, R45, R49, R51-R53, E6, E8
- Level: integration
- Fixture/setup: Real files under `about/`, `patterns/`, `conditions/`,
  `principles/`, and `programs/`.
- Steps: Assert exact first-slice paths exist; run the checker over
  `SOURCES.md about patterns conditions principles programs`; verify pages are
  not promoted before M4 evidence.
- Expected result: First expanded pages satisfy structural/source/metadata
  contracts and remain draft-only until promotion.
- Failure proves: The slice is incomplete or prematurely promoted.
- Automation location: `tests/test_responsible_breadth_real_pages.py`.

### RB-T12. Pattern and condition semantic safety proof

- Covers: R8-R10, R16-R17, R21-R22, R36-R37, R39, R43, R46, E1, E2, E4, E8,
  E9, EC1, EC2, EC5
- Level: audit
- Fixture/setup: Pattern and condition pages plus bounded source/scope evidence.
- Steps: Review source quality, claim support, red-flag routing, uncertainty,
  non-diagnostic framing, no treatment plan, and professional routing.
- Expected result: Pattern/condition pages are consumer education, not
  diagnosis, treatment, rehab, or corrective prescription.
- Failure proves: Automated checks missed a semantic safety violation.
- Automation location: Change-local validation records and structural tests.

### RB-T13. Programming and program-example semantic boundary proof

- Covers: R11-R14, R18-R19, R36-R37, R39, R44, R46, E3, E10, EC3, EC10
- Level: audit
- Fixture/setup: Principle/program pages plus bounded source/scope evidence.
- Steps: Review source mix, general-range language, non-prescription scope
  note, static worked-example framing, and absence of symptom/goal/equipment
  adaptation.
- Expected result: Programming content is literacy and illustration only.
- Failure proves: The program surface has become individualized prescription.
- Automation location: Change-local validation records and structural tests.

### RB-T14. Reader comprehension proof

- Covers: R42, R43, R44, AC9
- Level: audit
- Fixture/setup: Non-identifying reader-test prompts and comprehension evidence.
- Steps: Ask a beginner reader to state each page's purpose, boundary,
  stop/red-flag condition, and source they would inspect; record non-identifying
  results.
- Expected result: Reader understands no diagnosis and no personal
  prescription.
- Failure proves: Pages are not comprehensible or safety boundaries are unclear.
- Automation location: Change-local comprehension evidence or equivalent
  structural validation.

### RB-T15. Visual necessity and media provenance

- Covers: R29-R35, EC6
- Level: audit
- Fixture/setup: Any media referenced by expanded pages, `media/PROVENANCE.md`,
  and media validation evidence. If no media is used, record a no-media note.
- Steps: Inspect each media reference for necessity, non-decorative purpose,
  alt/adjacent explanation, source-of-truth alignment, and inherited provenance
  where raster media exists.
- Expected result: Text-only pages pass when images are unnecessary; media is
  safe and compliant when used.
- Failure proves: Visual layer can introduce unsupported or unsafe claims.
- Automation location: Media validation evidence plus inherited Markdown-first media
  tests.

### RB-T16. Navigation promotion gate

- Covers: R41, R50, AC10
- Level: smoke
- Fixture/setup: `README.md`, optional `SUMMARY.md`, and final validation records.
- Steps: Before M4, assert expanded pages are not promoted. In M4, assert
  navigation links only pages with complete evidence.
- Expected result: Active navigation cannot expose unproven expanded pages.
- Failure proves: Draft health-adjacent content can become public project
  surface prematurely.
- Automation location: `tests/test_responsible_breadth_navigation.py`.

### RB-T17. Final validation ledger and lifecycle sync

- Covers: R24-R28, R36-R37, R41-R46, AC1-AC10
- Level: audit
- Fixture/setup: Final validation ledger, review log, change metadata, plan,
  spec, architecture, ADR, and validation records.
- Steps: Confirm required commands and bounded audit evidence are current; confirm
  proposal accepted, spec approved, architecture approved, ADR accepted, plan
  active, review-resolution closed, and no unobserved CI pass is claimed.
- Expected result: Final evidence is coherent before code review and verify.
- Failure proves: Lifecycle state or validation evidence is stale.
- Automation location: Final validation ledger and optional structural checks.

### RB-T18. mdBook build or deferral

- Covers: R40, R55, AC-COMP-4
- Level: smoke
- Fixture/setup: `command -v mdbook || true`, optional `book.toml`,
  `SUMMARY.md`, and deferral record.
- Steps: If mdBook is configured and available, run `mdbook build`; otherwise
  record deferral and confirm Markdown remains canonical.
- Expected result: Derived HTML remains optional and non-authoritative.
- Failure proves: Generated output is blocking or replacing Markdown authority.
- Automation location: `tests/test_responsible_breadth_mdbook.py` and deferral record.

### RB-T19. Markdown-first compatibility regression

- Covers: R54, R55, R56, E7, AC-COMP-1 through AC-COMP-10
- Level: migration
- Fixture/setup: Original five-page v0.1 paths, expanded paths, and
  compatibility notes in both specs.
- Steps: Run Markdown-first regression tests; assert original numbered pages
  are not required to adopt Responsible Breadth page classes; assert expanded
  pages inherit shared Markdown-first rules.
- Expected result: Same-rank compatibility remains deterministic.
- Failure proves: Responsible Breadth breaks or silently supersedes the original
  v0.1 slice.
- Automation location: `tests/test_responsible_breadth_compatibility.py` plus
  `test_markdown_first_*.py`.

### RB-T20. Privacy scan over expanded content and proof

- Covers: R40, security/privacy section, EC7
- Level: unit
- Fixture/setup: Clean/forbidden privacy fixtures and real expanded content and
  proof directories when present.
- Steps: Run privacy checker over relevant paths for each milestone.
- Expected result: Forbidden private data patterns fail; setup errors are not
  treated as pass.
- Failure proves: Content or proof evidence may expose private data.
- Automation location: `tests/test_responsible_breadth_privacy.py` and
  `tools/checks/check_privacy.py`.

### RB-T21. Pattern-page architecture and exercise previews

- Covers: R35f, R57-R63, AC11, E11, EC11, EC12
- Level: integration
- Fixture/setup: Real `patterns/anterior-pelvic-tilt.md`, linked files under
  `exercises/`, and optional fixture pages under
  `tests/fixtures/responsible-breadth/pattern-architecture/`.
- Steps: Assert the pattern page contains the required reader journey:
  `Why beginners come to this page`, `Working definition`, `How to notice this
  in yourself`, `The core reason`, `What is uncertain or mixed`, and
  `What commonly helps`. Assert `Why beginners come to this page` has three to
  five bullets. Assert `The core reason` has three to five named contributors
  and each contributor has a citation. Assert every linked exercise preview in
  `What commonly helps` has `Fix reason`, `Used muscles`, and `Important note`.
  Resolve each exercise link and fail broken links unless the page is explicitly
  draft-only and marks the exercise unavailable.
- Expected result: The pattern page maps user pain point to observable pattern,
  contributor mechanisms, and bounded exercise options without duplicating full
  exercise instructions or creating broken links.
- Failure proves: Pattern pages can be structurally compliant but operationally
  unhelpful, or can route readers to missing exercise content.
- Automation location: `tests/test_responsible_breadth_pattern_architecture.py`
  or the equivalent Responsible Breadth real-page integration test.

### RB-T22. Expanded raster media-purpose validation

- Covers: R29, R29a, R29b, R35, R35a-R35f, AC12, AC13, E12, EC13, EC14,
  EC15
- Level: unit plus audit review
- Fixture/setup: Expanded-page fixtures and `media/PROVENANCE.md` fixtures
  under `tests/fixtures/responsible-breadth/media-purpose/`, including valid
  and invalid rows for `pattern_alignment_illustration`,
  `anatomical_region_illustration`, and `exercise_preview_illustration`.
- Steps: Run media/provenance checks against fixtures. Assert original v0.1
  pages still accept only original media purposes. Assert expanded pattern,
  condition, and exercise-support pages accept the expanded purpose values only
  in their permitted page contexts. Assert generated raster images require
  approved provenance and cannot be the source of truth for anatomy, technique,
  safety, diagnosis, treatment, programming, or exercise instruction. Pair the
  automated result with change-local visual-media audit evidence for
  visual meaning that cannot be mechanically inferred.
- Expected result: Expanded generated raster images are support assets with
  deterministic purpose labels and review evidence, while SVG remains allowed only
  when the visual-necessity review accepts it.
- Failure proves: The media layer can misclassify pattern/condition/exercise
  support images, silently weaken the original v0.1 media contract, or let
  generated images carry clinical or instructional authority.
- Automation location: `tests/test_responsible_breadth_media_purpose.py` or
  the equivalent media/provenance checker test.

## Fixtures and data

Planned automated fixtures:

- `tests/fixtures/responsible-breadth/classification/`
- `tests/fixtures/responsible-breadth/page-contracts/`
- `tests/fixtures/responsible-breadth/red-flags/`
- `tests/fixtures/responsible-breadth/metadata/`
- `tests/fixtures/responsible-breadth/sources/`
- `tests/fixtures/responsible-breadth/guardrails/`
- `tests/fixtures/responsible-breadth/pattern-architecture/`
- `tests/fixtures/responsible-breadth/media-purpose/`
- `tests/fixtures/responsible-breadth/navigation/`
- `tests/fixtures/responsible-breadth/privacy/`

Planned real pages:

- `about/red-flags.md`
- `patterns/anterior-pelvic-tilt.md`
- `conditions/non-specific-chronic-low-back-pain.md`
- `principles/how-many-days-a-week.md`
- `programs/generic-3-day-full-body-example.md`
- `exercises/*.md` pages referenced by expanded pattern exercise previews
- `media/PROVENANCE.md` rows for generated raster media when media exists

Historical evidence records from completed changes may remain archived, but
this test spec does not require a separate proof artifact tree for new work.

Reader-test records must avoid names, contact details, private health details,
symptom histories, and local machine paths. Use a non-identifying reader
description such as "beginner reader, first 90 days of gym training."

## Mocking/stubbing policy

- Do not mock file parsing for real expanded-page integration tests.
- Unit tests may use temporary directories and fixture files to isolate checker
  behavior.
- Do not call external websites in unit tests. Link health can be audit evidence or an
  optional tool because network behavior is unstable.
- Do not mock mdBook success. If `mdbook build` is claimed, run the real
  command and record the result. If unavailable, record deferral.
- Do not use AI-generated exercise or health guidance as a test oracle.
- Do not use generated raster images as an oracle for anatomy, technique,
  diagnosis, treatment, programming, or safety.
- Do not use reader symptom histories as fixtures.

## Migration or compatibility tests

- RB-T19 proves original numbered v0.1 pages remain governed by
  `specs/markdown-first-primer.md`.
- RB-T19 proves Responsible Breadth supersedes Markdown-first R21/R22 only for
  accepted expanded page classes.
- RB-T18 proves mdBook remains derived or deferred.
- RB-T16 proves expanded paths become active compatibility surfaces only after
  promotion evidence exists.
- Inherited Markdown-first media tests prove `media/PROVENANCE.md` semantics
  continue to apply.
- RB-T22 proves original v0.1 media-purpose values remain valid for original
  pages while expanded Responsible Breadth pages use the expanded purpose enum
  only in the permitted page contexts.

## Observability verification

Checker output should identify:

- page path relative to repository root;
- page class;
- rule ID or stable check name;
- missing section, missing metadata field, source ID, red-flag link,
  exercise preview annotation, broken exercise link, normalized media path,
  provenance field, `media_purpose`, scope term, or privacy category when
  applicable;
- pass/fail/setup-error status with distinct exit behavior.

Audit or validation records must identify:

- inspected files;
- requirement IDs or acceptance criteria checked;
- owner/reviewer role;
- questions asked where reader comprehension is tested;
- pass/fail result;
- commands run;
- skipped tools and residual risk.

Do not include secrets, private health details, local absolute paths, or
personally identifying reader details in validation output.

## Security/privacy verification

- RB-T6 rejects diagnosis, treatment, rehab, personalized programming, symptom
  collection, acute/specialized population content, and runtime-product
  language.
- RB-T12 and RB-T13 verify that semantic wording does not cross into
  diagnosis, treatment, rehab, correction promises, or prescription.
- RB-T14 requires non-identifying comprehension evidence.
- RB-T15 and RB-T22 verify that media does not introduce unsupported anatomy,
  unsafe setup, diagnosis/pathology/treatment implications, medical/rehab
  imagery, wrong purpose labels, or unprovenanced raster assets.
- RB-T20 runs negative-match privacy checks over content and validation records.

## Performance checks

- Responsible Breadth unit and integration checks should complete in under 30
  seconds on the first expanded proof slice, excluding network-dependent link
  checking.
- Record command duration when practical with test runner output or a validation
  ledger.
- Performance failure blocks claiming the local quality gate is ergonomic, but
  does not make Markdown unreadable.

## Audit Checklist

- Open every expanded page directly as Markdown.
- Confirm no expanded page requires JavaScript, generated HTML, accounts, CMS,
  API, local server, or user input.
- Confirm path classification is unambiguous.
- Confirm pattern and condition pages link red flags before self-management.
- Confirm pattern and condition pages say what the page is not and avoid
  diagnosis or individualized treatment.
- Confirm program example says it is not the reader's prescription.
- Confirm every expanded page has required metadata and review cadence.
- Confirm every safety warning has claim-level citation and page-local source.
- Confirm source-quality mix is documented in audit evidence.
- Confirm uncertainty/mixed-evidence language is present where sources do not
  fully agree.
- Confirm pattern pages state reader pain points, a working pattern definition,
  named core contributors, and bounded exercise previews.
- Confirm every exercise preview has fix reason, used muscles, and one
  important note, and links to an existing exercise page.
- Confirm generated raster media has an approved provenance row, deterministic
  `media_purpose`, alt/adjacent explanation, and support-only framing.
- Confirm no page asks for symptoms, personal goals, equipment constraints,
  injury status, age, pregnancy status, medical history, or training response to
  choose content.
- Confirm README/SUMMARY do not promote expanded pages before evidence exists.
- Confirm validation records are non-identifying.
- Confirm mdBook is built or explicitly deferred if generated output surfaces
  are touched.

## What not to test and why

- Do not test symptom-checker flows, diagnosis routing, individualized
  programming, treatment planning, rehab progressions, or return-to-training
  protocols because they are forbidden.
- Do not test hosted website behavior, analytics, CMS, accounts, search index,
  API, or deployment because Responsible Breadth does not introduce them.
- Do not test broad content scaling beyond the five-page expanded proof slice.
- Do not test formal clinician review-board mechanics because the accepted
  trust model is citation discipline, red-flag routing, honest authorship, and
  bounded audit evidence.
- Do not require network link checks as unit proof; link-health can be optional
  or audit evidence.
- Do not test generated AI content as source of truth because it remains
  prohibited.
- Do not test whether generated images are medically or biomechanically
  authoritative; they are support assets and must be checked against Markdown
  and cited sources instead.

## Uncovered gaps

None that require returning to spec or architecture before test-spec-review.

Known validation limits to preserve in review:

- Automated checks can prove structure, source counts, source-index validity,
  and known forbidden terms, but they cannot prove semantic source authority.
- Audit review remains required for source quality, non-diagnostic language,
  non-prescription boundaries, visual necessity, and reader comprehension.
- Link health remains optional audit evidence until a network-capable link checker is
  selected.
- mdBook remains conditional and derived.

## Next artifacts

- `test-spec-review` for `specs/responsible-breadth.test.md`.
- After clean test-spec-review, the APT follow-up can implement or reconcile
  RB-T21/RB-T22 proof without reopening the original M1-M4 milestone scope.

## Follow-on artifacts

None yet.

## Readiness

This test spec is ready for test-spec-review. It is not implementation-ready,
code-review-ready, verification-ready, branch-ready, PR-ready, or Done until
test-spec-review approves it and downstream implementation/review gates
complete.
