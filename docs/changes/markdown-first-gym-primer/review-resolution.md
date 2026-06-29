# Review Resolution: Markdown-First Gym Primer

## Status

closed

## Open findings

| Finding ID | Review | Status | Required owner action |
| --- | --- | --- | --- |
| TSR1 | `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r1.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r2.md`. |
| CR-M2-1 | `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r1.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/code-review-m2-r2.md`. |
| SR-MEDIA-1 | `docs/changes/markdown-first-gym-primer/reviews/spec-review-r2.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/spec-review-r3.md`. |
| AR-MEDIA-1 | `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r2.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`. |
| PR-MEDIA-1 | `docs/changes/markdown-first-gym-primer/reviews/plan-review-r2.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/plan-review-r3.md`. |
| TSR-M3A-1 | `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r3.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r4.md`. |
| CR-M3-1 | `docs/changes/markdown-first-gym-primer/reviews/code-review-m3-r2.md` | resolved | Resolved by `docs/changes/markdown-first-gym-primer/reviews/code-review-m3-r3.md`. |

## Resolution notes

- 2026-06-27: Opened for `test-spec-review-r1`.
- 2026-06-27: Addressed TSR1 by revising `specs/markdown-first-primer.test.md` to add milestone and proof ownership.
- 2026-06-27: `test-spec-review-r2` approved the revised proof map and closed TSR1.
- 2026-06-27: Opened CR-M2-1 from `code-review-m2-r1`; M2 remains in `resolution-needed`.
- 2026-06-27: Addressed CR-M2-1 by loading root `SOURCES.md` as the checker source index, adding source-index regression fixtures, and refreshing M2 validation evidence. M2 returned to `review-requested` for code-review M2 R2.
- 2026-06-27: `code-review-m2-r2` approved the CR-M2-1 resolution and closed M2.
- 2026-06-27: Opened SR-MEDIA-1 from `spec-review-r2`; the AI-generated media amendment requires spec revision before downstream artifacts can rely on it.
- 2026-06-27: Revised `specs/markdown-first-primer.md` for SR-MEDIA-1 with centralized `media/PROVENANCE.md`, required provenance fields, exact `asset_path` matching, media-purpose scope, status values, and stable media validation failure codes. Routed to spec-review R3.
- 2026-06-27: `spec-review-r3` approved the revised media provenance contract
  and closed SR-MEDIA-1.
- 2026-06-28: Opened AR-MEDIA-1 from `architecture-review-r2`; the media
  provenance architecture needs deterministic raster-media classification
  before downstream test-spec, plan, or implementation updates rely on it.
- 2026-06-28: Addressed AR-MEDIA-1 by adding the v0.1 extension-based media
  classifier to `docs/architecture/system/architecture.md` and
  `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`; routed to
  architecture-review R3.
- 2026-06-28: `architecture-review-r3` approved the deterministic
  media-classification boundary and closed AR-MEDIA-1.
- 2026-06-28: Opened PR-MEDIA-1 from `plan-review-r2`; the active plan must
  clarify whether implementation after test-spec targets M3A media validation
  while M3 remains blocked, or stays blocked on M3 beginner read-test evidence.
- 2026-06-28: Addressed PR-MEDIA-1 by choosing Option A. The plan now makes
  M3A the next executable implementation target after test-spec review approval,
  while M3 remains promotion-blocked until MP3 beginner read-test evidence is
  collected and any referenced media passes M3A validation.
- 2026-06-28: `plan-review-r3` approved the revised M3A sequencing and closed
  PR-MEDIA-1.
- 2026-06-28: Opened TSR-M3A-1 from `test-spec-review-r3`; the M3A proof map
  has stale edge-case IDs in several test-case `Covers:` lines.
- 2026-06-28: `test-spec-review-r4` approved the corrected M3A proof-map
  traceability and closed TSR-M3A-1.
- 2026-06-28: Opened CR-M3-1 from `code-review-m3-r2`; MP3 records beginner
  approval after image-based readability revisions, but it does not yet record
  the required per-page comprehension outcomes for purpose, setup, steps, and
  stop condition.
- 2026-06-29: Addressed CR-M3-1 by updating MP3 with non-identifying
  per-page beginner comprehension outcomes and routing M3 back to code-review
  R3.
- 2026-06-29: `code-review-m3-r3` approved the CR-M3-1 resolution and closed
  M3.

## Code-review M3 R2 resolution

### CR-M3-1 - MP3 does not record required comprehension outcomes

Resolution: ready for rereview.

Required owner action:

- Update `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md`
  with non-identifying per-page beginner comprehension outcomes.
- For each exercise page, record whether the beginner could explain purpose,
  setup or body position, movement steps, stop condition, and source
  verification.
- For the principle page, record the principle-page questions listed in MP3.
- Do not record reader names, contact details, health history, or private
  training data.
- Rerun the M3 validation commands and request code-review M3 R3.

Safe resolution path:

- Add a compact table to MP3 with one row per first-slice page and explicit
  pass/fail or short non-identifying notes for the required fields.
- Preserve the existing readability revision history and final reader approval.
- Route the change back to `code-review` after validation passes.

Changes:

- Added principle-page comprehension outcomes for
  `01-getting-started/beginner-training-principles.md`.
- Added exercise-page comprehension outcomes for:
  - `02-machines/lat-pulldown.md`
  - `02-machines/seated-row.md`
  - `02-machines/chest-press.md`
  - `03-bodyweight/incline-push-up.md`
- Recorded whether the reader could explain each exercise page's purpose,
  setup or body position, movement steps, stop condition, and source
  verification.
- Recorded confusion found, revisions made, recheck status, and final outcome.
- Confirmed no reader name, contact details, health history, private training
  data, or identifying information was recorded.

Validation:

- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  passed with 44 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight`
  passed.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer/manual-proof`
  passed.
- `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi`
  passed.

Status: resolved by `code-review-m3-r3`.

## Test-spec-review R3 resolution

### TSR-M3A-1 - Stale edge-case IDs in test-case traceability

Resolution: ready for rereview.

Changes:

- T4 now covers `EC1`, `EC2`, `EC14`, and `EC16`.
- T7 now covers `EC15`.
- T10 now covers `EC13`, `EC14`, and `EC16`.
- T11 now covers `EC12`.

Validation:

- Reran structural scans for T/CMD/MP ownership.
- Reran requirement coverage scan for R1-R53.
- Reran example coverage scan for E1-E8.
- Reran edge-case coverage scan for EC1-EC16.

Status: resolved by `test-spec-review-r4`.

## Test-spec-review R1 resolution

### TSR1 - Missing milestone/proof ownership map

Resolution: addressed by revising `specs/markdown-first-primer.test.md` to add explicit milestone and proof ownership.

Changes:

- Added proof classifications: existing, planned-for-milestone, manual-only, and conditional/external.
- Mapped T1-T13 to M1-M4.
- Added owner roles for each test group.
- Added first meaningful execution and closeout evidence for each test group.
- Added planned command ownership for Markdown-first checks, privacy checks, optional markdown linting, mdBook build, and final local quality gate.
- Added manual proof ownership records for direct Markdown render inspection, semantic citation review, beginner read test, mdBook build-or-deferral, and source-of-truth drift inspection.
- Clarified that pre-milestone absence is not failure unless marked pre-milestone required.

Status: resolved by `test-spec-review-r2`.

## Code-review M2 R1 resolution

### CR-M2-1 - Missing `SOURCES.md` coverage for reused source IDs

Resolution: resolved by `code-review-m2-r2`.

Changes:

- Added reference definitions to root `SOURCES.md` so it can act as a real global source index while pages still keep page-local reference definitions.
- Updated `tools/checks/check_markdown_first.py` to load root `SOURCES.md`, require every cited source ID to have a page-local definition, require non-local source IDs to appear in `SOURCES.md`, allow explicit `local-<page-slug>-...` IDs without global index entries, reject local IDs reused across pages, reject non-local reused IDs missing from `SOURCES.md`, and reject URL mismatches between page-local definitions and the global index.
- Added fixtures for missing global source ID, valid global source ID, valid page-local source ID, reused local source ID, reused non-local source ID missing from `SOURCES.md`, and source URL mismatch.
- Added citation tests:
  - `test_global_source_id_missing_from_sources_md_is_rejected`
  - `test_global_source_id_present_in_sources_md_passes`
  - `test_page_local_source_id_is_allowed_without_sources_md_entry`
  - `test_page_local_source_id_reused_across_pages_is_rejected`
  - `test_reused_source_id_missing_from_sources_md_is_rejected`
  - `test_page_source_url_must_match_sources_index`

Validation evidence refreshed:

- `python3 -m unittest tests.test_markdown_first_citations` passed with 10 tests.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 29 tests.
- `python3 tools/checks/check_markdown_first.py --help` passed.
- `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md` passed.
- `python3 tools/checks/check_markdown_first.py tests/fixtures/markdown-first/citations/missing-global-source-id.md; test $? -eq 1` passed and reported `source_id_missing_from_sources_md` for `unknown-source`.
- `if command -v markdownlint >/dev/null 2>&1; then markdownlint "**/*.md"; else printf 'markdownlint not installed\n'; fi` reported `markdownlint not installed`; CMD6 remains conditionally deferred.

Status: resolved by `code-review-m2-r2`.

## Spec-review R2 resolution

### SR-MEDIA-1 - Missing deterministic media provenance contract

Resolution: ready for rereview.

Required owner action:

- Revise `specs/markdown-first-primer.md` to define where AI-generated media
  provenance records live.
- Define the required field names or schema for each AI-generated raster
  illustration provenance record.
- Define how a Markdown image reference maps to its provenance record.
- Define the failure behavior when a referenced AI-generated image has no
  matching provenance record, blank required fields, or unapproved review
  status.

Changes:

- Added first-slice media purpose definitions with allowed values
  `equipment_identification` and `key_movement_illustration`.
- Added `media/PROVENANCE.md` as the single provenance index for
  AI-generated raster illustrations.
- Added one-row-per-asset provenance requirements with required fields:
  `asset_path`, `asset_type`, `media_purpose`, `generator`,
  `prompt_or_creation_notes`, `created_date`, `human_reviewer`,
  `license_assertion`, `source_inputs`, `review_status`, `page_refs`, and
  `notes`.
- Added exact `asset_path` matching between Markdown image references and
  provenance rows.
- Added required `review_status` values and promotion rule requiring
  `approved`.
- Added v0.1 media purpose limits and validation failure behavior for missing,
  incomplete, non-approved, out-of-scope, and page-reference-mismatched media
  provenance.

Status: resolved by `spec-review-r3`.

## Architecture-review R2 resolution

### AR-MEDIA-1 - Raster media classification is not deterministic

Resolution: ready for rereview.

Required owner action:

- Revise `docs/architecture/system/architecture.md` to define how v0.1
  validation classifies image references before checking
  `media/PROVENANCE.md`.
- Revise `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md` with
  the same durable classification rule.
- Preserve the approved spec boundary: text-only pages remain valid, original
  SVGs remain allowed, AI-generated raster images require provenance, and
  undocumented third-party raster media remains out of scope.

Safe resolution path:

- State that, for v0.1 promoted pages, original educational diagrams are SVG
  assets.
- State that referenced raster image files under `media/` are treated as
  AI-generated raster illustrations and require an approved matching
  `media/PROVENANCE.md` row.
- Name the allowed raster extensions or explicitly delegate them to a fixed
  checker allowlist.
- Route the revised architecture and ADR to architecture-review R3.

Changes:

- Added deterministic extension-based classification before provenance lookup.
- Classified `.svg` files under `media/` as original educational diagrams.
- Classified `.png`, `.jpg`, `.jpeg`, and `.webp` files under `media/` as
  AI-generated raster illustrations.
- Required AI-generated raster illustrations to have an approved matching row
  in `media/PROVENANCE.md`.
- Made remote image URLs, image paths outside `media/`, unsupported
  extensions, missing local assets, and raster images without approved
  provenance validation failures.

Status: resolved by `architecture-review-r3`.

## Plan-review R2 resolution

### PR-MEDIA-1 - M3A sequencing conflicts with the live blocked milestone

Resolution: ready for rereview.

Required owner action:

- Revise `docs/plans/2026-06-27-markdown-first-gym-primer.md` so the next
  executable implementation target after test-spec review is unambiguous.
- Update `docs/plan.md`, `docs/workflows.md`, and
  `docs/changes/markdown-first-gym-primer/change.yaml` to match the chosen
  sequence.

Safe resolution path:

- Option A: make M3A the next implementation milestone after test-spec review,
  while keeping M3 promotion/code-review blocked until MP3 beginner read-test
  evidence is collected and any referenced media passes M3A.
- Option B: keep M3 as the next implementation milestone and state that M3A
  cannot start until MP3 closes M3.

Changes:

- Updated Current Handoff Summary to name M3A as the next executable target
  after test-spec review approval.
- Reordered the plan so M3A appears before M3 closeout.
- Clarified that M3A can be implemented before MP3 beginner read-test evidence
  is collected.
- Clarified that M3A does not close M3 and does not satisfy MP3.
- Clarified that M3 closeout requires MP3 plus M3A validation for any
  referenced media.
- Clarified that `media/PROVENANCE.md` is created in M3A even if no raster rows
  exist.
- Marked `rg ... || true` commands as inspection-only evidence, not closeout
  gates.
- Noted that `change.yaml` moves to `current_milestone: M3A` only when the
  workflow advances to implementation after test-spec review.

Status: resolved by `plan-review-r3`.
