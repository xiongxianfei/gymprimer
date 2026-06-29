# Plan: Markdown-First Gym Primer

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the approved Markdown-first v0.1 direction without reviving the superseded structured content platform. The work should make the repository itself usable as the product: a small English-first Markdown primer with five pages, page-local citations, disclaimers, contribution and license guidance, lightweight validation, manual beginner read-test evidence, and optional mdBook output only if it stays minimal.

This plan sequences implementation only. It does not reopen product direction, expert-review policy, hosted website scope, AI features, rehab content, or broad exercise-library expansion.

## Source artifacts

- Proposal: `../proposals/2026-06-27-markdown-first-gym-primer.md`
- Proposal review: `../changes/markdown-first-gym-primer/reviews/proposal-review-r2.md`
- Spec: `../../specs/markdown-first-primer.md`
- Spec reviews:
  - `../changes/markdown-first-gym-primer/reviews/spec-review-r1.md`
  - `../changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review:
  `../changes/markdown-first-gym-primer/reviews/architecture-review-r1.md`
  `../changes/markdown-first-gym-primer/reviews/architecture-review-r2.md`,
  and `../changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`
  with AR-MEDIA-1 resolved.
- ADR: `../adr/2026-06-27-markdown-first-citation-based-authority.md`
- Media ADR: `../adr/2026-06-28-ai-generated-raster-media-provenance.md`
- Superseded ADR: `../adr/2026-06-26-repository-native-reviewed-content.md`
- Test spec: `../../specs/markdown-first-primer.test.md`

## Context and orientation

The repository is on the Markdown-first branch, but it still contains active-looking artifacts from the superseded structured-platform track: schema files, `content/`, `generated/`, `tools/validation/`, old tests, and the old content-schema plan. The approved v0.1 source surfaces are different:

- `README.md` as product entry and navigation.
- `SOURCES.md` as reusable source index.
- `CONTRIBUTING.md` as contributor contract.
- `CONTENT_LICENSE.md` as content and diagram license clarification.
- `01-getting-started/`, `02-machines/`, and `03-bodyweight/` for the five first-slice Markdown pages.
- `media/` for optional original SVGs and approved AI-generated raster
  illustrations with centralized provenance.
- `media/PROVENANCE.md` for AI-generated raster illustration provenance.
- `tools/checks/` for lightweight Markdown-first checks.
- `docs/changes/markdown-first-gym-primer/` for review, validation, and manual proof evidence.

Planning choice for old artifacts: mark the structured-platform implementation and plan as superseded in place during v0.1 instead of moving many files under `docs/archive/`. This avoids large path churn while preventing the old validator, generated JSON, schemas, and review lifecycle from being mistaken for active implementation guidance. A later archive-only change can move those artifacts if maintainers want a cleaner tree.

Implementation must wait for plan-review and test-spec/test-spec-review. This plan intentionally does not authorize coding from chat alone.

The media provenance amendment is now approved at the spec, architecture, and
ADR levels. The next implementation-facing work is not image generation yet:
the plan and test spec must first make the media classification and provenance
checks executable.

## Non-goals

- Do not build a hosted app, CMS, database, account system, analytics, or deployment target.
- Do not create generated public JSON as the v0.1 product.
- Do not implement a formal expert-review lifecycle.
- Do not add broad exercise content beyond the five pages in `specs/markdown-first-primer.md`.
- Do not add barbell, Olympic lifting, kettlebell ballistic, plyometric, sprint, sport-specific, rehab, posture-correction, pain-treatment, diagnosis, or injury-specific content.
- Do not add full-card Chinese translation in v0.1.
- Do not add third-party screenshots, stock photos, borrowed public web images,
  commercial machine screenshots, decorative images, anatomy posters, medical
  illustrations, rehab illustrations, or images with identifying people.
- Do not add AI-generated raster images outside equipment identification or key
  movement illustration.
- Do not treat mdBook HTML, generated validation reports, or old generated artifacts as source of truth.
- Do not claim CI passed unless an actual CI run is observed.

## Requirements covered

- R1-R4: M1 and M3 establish Markdown source, README navigation, and direct repository browsing.
- R5-R6: M1 defines templates; M3 applies required exercise and principle sections.
- R7-R16: M1-M3 cover disclaimers, claim-level citations, page-local `Sources`, `SOURCES.md`, and reference-style links.
- R17-R20: M1-M3 keep v0.1 English-first and allow only Chinese aliases.
- R21-R22: M2 and M3 cover scope allowlist and excluded-scope blocking.
- R23-R25: M1-M3A cover optional media policy, relative paths, and
  alt/adjacent explanatory text.
- R41-R53: M3A covers deterministic media classification, centralized
  provenance, provenance row validation, and stable media failure codes before
  generated pictures are added to documents.
- R26-R28: M1 covers Apache-2.0, CC BY 4.0, and inbound contribution terms.
- R29-R30: M1 and M3 cover non-canonical spike labeling and promotion language.
- R31-R33: M4 covers mdBook add-or-defer behavior.
- R34-R35: M1 covers old platform supersession and traceability.
- R36-R37: M2 covers local validation checks, including negative-match privacy scanning.
- R38-R39: M3 covers beginner read-test evidence.
- R40: M2-M4 ensure completion reports list exact commands, unavailable commands, and residual risks.
- AC1-AC19: M1-M4 collectively cover the accepted first-slice acceptance
  criteria after test-spec and implementation are updated for media
  provenance.

## Current Handoff Summary

- Current plan state: branch-ready for PR handoff after local final verification.
- Current milestone: M4. Optional mdBook and Final Local Quality Gate.
- Current milestone state: closed.
- Last reviewed milestone: M4
- Review status: code-review-m4-r1 clean-with-notes; no review-resolution required
- Remaining in-scope implementation milestones: none
- Next stage: pr.
- Final closeout readiness: branch-ready
- Reason final closeout is or is not ready: M1-M2 are closed and the M3 draft
  pages pass local checks, and the media provenance architecture/ADR are
  normalized after clean architecture-review R3. M3A is closed after clean
  code-review. CR-M3-1 has been resolved by code-review M3 R3, and M3 is
  closed. M4 deferred mdBook because the binary is unavailable, recorded the
  final local quality gate, and passed clean code-review R1. The implementation
  milestones are closed. Explain-change and verify are recorded; PR handoff
  remains.

Implementation sequence:

1. PR handoff - prepare the branch for human review after verification.

## Milestones

### M1. Active Route, Contributor Contract, and Legacy Supersession

- Milestone state: closed
- Goal: Make the active repository surfaces point at the Markdown-first product and mark old structured-platform work as superseded without deleting traceability evidence.
- Requirements: R1-R4, R7-R16, R23-R30, R34-R35, AC3, AC6, AC8, AC9, AC13
- Files/components likely touched:
  - `README.md`
  - `CONTRIBUTING.md`
  - `SOURCES.md`
  - `CONTENT_LICENSE.md`
  - `docs/templates/exercise-card.md`
  - `docs/templates/principle-page.md`
  - `docs/plan.md`
  - `docs/plans/2026-06-26-content-schema-foundation.md`
  - `content/README.md`
  - `schemas/README.md`
  - `generated/README.md`
  - `tools/validation/README.md`
  - `docs/changes/markdown-first-gym-primer/`
- Dependencies:
  - Plan-review approval.
  - Test-spec/test-spec-review defining proof obligations before implementation.
- Tests to add/update:
  - Plan/test-spec should define documentation checks for README navigation, contributor license terms, source index presence, template required sections, and old-platform supersession markers.
- Implementation steps:
  - Update `README.md` so its body matches the Markdown-first vision and no longer advertises generated public JSON as the product.
  - Add `SOURCES.md` with reusable source-index conventions and initial public sources expected by the first five pages.
  - Add `CONTENT_LICENSE.md` documenting Apache-2.0 for code/tooling and CC BY 4.0 for written content and original diagrams.
  - Update `CONTRIBUTING.md` with citation, disclaimer, scope, media, privacy, and inbound licensing terms.
  - Add exercise and principle page templates with disclaimer, section, citation, source, media, and scope reminders.
  - Mark old structured-platform implementation directories and the old plan as superseded in place.
  - Record the old-artifact disposition decision in this plan and change-local evidence.
- Validation commands:
  - `rg -n "Markdown-first|source of truth|01-getting-started|02-machines|03-bodyweight|SOURCES.md" README.md`
  - `rg -n "Apache-2.0|CC BY 4.0|right to submit|third-party media|claim-level|not medical advice" CONTRIBUTING.md CONTENT_LICENSE.md`
  - `test -f SOURCES.md && test -f CONTENT_LICENSE.md && test -f docs/templates/exercise-card.md && test -f docs/templates/principle-page.md`
  - `rg -n "superseded|Markdown-first" docs/plans/2026-06-26-content-schema-foundation.md content/README.md schemas/README.md generated/README.md tools/validation/README.md`
- Expected observable result: A contributor landing in the repository sees Markdown-first guidance, license terms, templates, and clear supersession of old structured-platform implementation surfaces.
- Commit message: `M1: align active repository guidance with Markdown-first`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated; no new product decision was needed
  - validation notes updated
  - milestone handoff commit not created because the branch already contains uncommitted upstream workflow artifacts; code-review should review the working tree state for M1
- Risks:
  - Superseded old files may still be mistaken for active tests or tooling if notices are too subtle.
  - License wording may overstate legal certainty.
- Rollback/recovery:
  - Revert M1 if guidance conflicts with the spec; preserve the accepted proposal, spec, architecture, and ADR.

### M2. Markdown-First Check Tooling and Test Fixtures

- Milestone state: closed
- Goal: Add lightweight local checks and tests that prove the Markdown-first content contract before promoting the five pages.
- Requirements: R7-R16, R21-R25, R29-R30, R36-R37, R40, AC3, AC5, AC7, AC8, AC11, AC13
- Files/components likely touched:
  - `tools/checks/`
  - `tests/`
  - `tests/fixtures/markdown-first/`
  - `docs/changes/markdown-first-gym-primer/`
- Dependencies:
  - M1 contributor/template surfaces, or equivalent test-spec fixtures that can be used before M1 closes.
- Tests to add/update:
  - Unit tests for disclaimer detection.
  - Unit tests for page-local `Sources` section detection.
  - Unit tests for claim-level safety-citation detection using explicit safety terms and adjacent reference-style links.
  - Unit tests for excluded-scope terms.
  - Unit tests for full-card Chinese translation detection versus allowed Chinese aliases.
  - Unit tests for media references, relative paths, and external media rejection.
  - Unit tests for privacy scan semantics: exit success only when forbidden patterns are absent.
- Implementation steps:
  - Add a single check entry point or small focused scripts under `tools/checks/`.
  - Keep checks standard-library Python unless a later reviewed artifact allows dependencies.
  - Make failures name the file and rule that failed.
  - Include valid and invalid fixtures for each check.
  - Do not reuse old structured-platform schema validators as active v0.1 gates.
- Validation commands:
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py --help`
  - `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md`
- Expected observable result: The repository has runnable local checks for the v0.1 Markdown contract, and negative fixtures prove important failures are caught.
- Commit message: `M2: add Markdown-first content checks`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated; no new product decision was needed
  - validation notes updated
  - milestone handoff commit not created because the branch already contains uncommitted upstream workflow artifacts; code-review should review the working tree state for M2
- Risks:
  - Citation checks may become too heuristic and miss unsupported claims.
  - Scope-term checks may create false positives for pages that explain what is out of scope.
- Rollback/recovery:
  - Revert the faulty check or narrow it to a warning while retaining test fixtures that demonstrate the gap.

### M3A. AI Raster Media Provenance Validation and Optional Page Images

- Milestone state: closed
- Goal: Make the approved media-provenance contract executable before adding
  AI-generated raster illustrations to first-slice pages.
- Sequencing: M3A was the next executable implementation milestone after
  test-spec review approval. It has been implemented before MP3 beginner
  read-test evidence is collected.
- M3 relationship: M3A does not close M3 and does not replace MP3. It supplies
  the media validation gate required before M3 pages with media can be
  promoted.
- Requirements: R23-R25, R36-R40, R41-R53, AC7, AC11, AC15-AC19
- Files/components likely touched:
  - `tools/checks/check_markdown_first.py`
  - `tests/test_markdown_first_guardrails.py`
  - `tests/fixtures/markdown-first/media/`
  - `media/PROVENANCE.md`
  - `media/equipment/`
  - `media/movements/`
  - first-slice Markdown pages only if optional images are added after
    validation exists
  - `docs/changes/markdown-first-gym-primer/manual-proof/`
- Dependencies:
  - Plan-review approval for this amended plan is complete.
  - Test-spec and test-spec-review updates covering R41-R53 and AC15-AC19 are
    complete.
  - Architecture-review R3 approval and normalized architecture/ADR status are
    complete.
  - MP3 beginner read-test evidence is not required before M3A code-review.
  - Image generation, if used later, must happen only after the
    validator/provenance contract passes code-review or as non-promoted fixture
    work covered by tests.
- Tests to add/update:
  - `text_only_page_passes`
  - `svg_under_media_passes_without_provenance`
  - `png_under_media_requires_provenance`
  - `jpg_under_media_requires_provenance`
  - `jpeg_under_media_requires_provenance`
  - `webp_under_media_requires_provenance`
  - `png_with_approved_provenance_passes`
  - `png_with_unapproved_provenance_fails`
  - `remote_image_fails`
  - `image_outside_media_fails`
  - `unsupported_extension_fails`
  - provenance row field, `review_status`, `media_purpose`, and `page_refs`
    mismatch fixtures
- Implementation steps:
  - Extend Markdown image-reference parsing so media validation classifies image
    references by resolved repository path and lowercase extension before
    provenance lookup.
  - Treat `.svg` under `media/` as original educational diagrams.
  - Treat `.png`, `.jpg`, `.jpeg`, and `.webp` under `media/` as
    AI-generated raster illustrations.
  - Fail remote image URLs, media paths outside `media/`, unsupported
    extensions, and missing local media files with stable error codes.
  - Create `media/PROVENANCE.md` with the required header and Markdown table
    schema even if no AI-generated raster assets are added in M3A.
  - If no raster assets exist, leave the provenance table with no asset rows.
  - Validate required provenance fields, `asset_type = ai_generated_raster`,
    allowed `media_purpose`, `review_status = approved`, exact `asset_path`,
    and `page_refs` consistency.
  - If optional first-slice images are added, include only necessary equipment
    identification or key movement illustrations and record approved
    provenance before page promotion.
  - Do not add decorative, stock, third-party, screenshot, medical, rehab,
    identifying-person, or non-AI raster media.
- Media scope:
  - M3A does not require adding generated images.
  - Pages without images remain valid.
  - First-slice images, when used, are limited to equipment identification and
    key movement illustration.
- M3A closeout commands:
  - `python3 -m unittest tests.test_markdown_first_guardrails`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md media docs/changes/markdown-first-gym-primer`
- Inspection-only evidence:
  - `rg` commands may inspect media reports or provenance contents, but
    `rg ... || true` commands are not closeout gates.
- PR-MEDIA-1 acceptance criteria:
  - M3A is named as the next executable implementation target after test-spec
    review approval.
  - M3 remains promotion-blocked until MP3 evidence is collected and any
    referenced media passes M3A.
  - M3A is explicitly independent of MP3 beginner read-test collection.
  - M3A does not require adding images; pages without images remain valid.
  - First-slice images are limited to equipment identification and key movement
    illustration.
  - `media/PROVENANCE.md` is created in M3A with the required table schema even
    if there are no raster asset rows.
  - Inspection-only `rg ... || true` commands are not closeout gates.
  - `change.yaml` moves to `current_milestone: M3A` only when the workflow
    advances to implementation after test-spec review.
- Expected observable result: Raster images under `media/` cannot be promoted
  without approved provenance, SVG diagrams remain allowed without AI-raster
  provenance, and media validation findings identify classification and
  provenance failures.
- Commit message: `M3A: add AI raster media provenance checks`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if optional first-slice images are added
  - validation notes updated
  - clean code-review recorded in `docs/changes/markdown-first-gym-primer/reviews/code-review-m3a-r1.md`
  - milestone handoff commit not created because the branch already contains
    uncommitted upstream workflow artifacts; code-review reviewed the working
    tree state for M3A
- Risks:
  - Media parsing may miss Markdown image syntaxes or produce false positives.
  - Provenance table parsing may become brittle if contributors format tables
    inconsistently.
  - Generated images may contain unsafe or misleading setup details.
- Rollback/recovery:
  - Remove optional raster references from first-slice pages and keep
    text/SVG-only content while retaining failing fixtures to document the gap.
  - Defer generated images if provenance validation or human image review is
    not ready.

### M3. Five-Page First Slice and Beginner Read-Test Evidence

- Milestone state: closed
- Goal: Draft and validate the exact five v0.1 Markdown pages, with page-local sources, disclaimers, conservative scope, and manual beginner comprehension evidence.
- Requirements: R1-R25, R29-R30, R36-R40, AC1-AC8, AC11-AC13
- Files/components likely touched:
  - `01-getting-started/beginner-training-principles.md`
  - `02-machines/lat-pulldown.md`
  - `02-machines/seated-row.md`
  - `02-machines/chest-press.md`
  - `03-bodyweight/incline-push-up.md`
  - `README.md`
  - `SOURCES.md`
  - `media/`
  - `docs/changes/markdown-first-gym-primer/manual-proof/`
- Dependencies:
  - M1 active route and templates closed.
  - M2 local checks closed or an explicit reviewed exception if check tooling is blocked.
  - M3A media provenance validation closed for any page that references media.
  - At least one beginner reader is available for non-identifying read-test feedback before promotion.
- Tests to add/update:
  - Add fixtures or real-page coverage for all five pages in Markdown-first check tests.
  - Add manual read-test evidence template and completed record.
- Implementation steps:
  - Create the required directories and five Markdown pages.
  - Keep pages English-first; include Chinese aliases only where useful.
  - Use reference-style links and page-local `Sources`.
  - Add reused sources to `SOURCES.md`.
  - Use no media unless original simple SVG diagrams are added with relative
    paths and explanatory text.
  - Do not add AI-generated raster illustrations in M3 until M3A media
    provenance validation exists and has passed review.
  - Update README navigation after pages are ready to be treated as active source content.
  - Record beginner read-test notes without personal identifying information.
- Validation commands:
  - `test -f 01-getting-started/beginner-training-principles.md && test -f 02-machines/lat-pulldown.md && test -f 02-machines/seated-row.md && test -f 02-machines/chest-press.md && test -f 03-bodyweight/incline-push-up.md`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer/manual-proof`
  - `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi`
- Expected observable result: The five first-slice pages are directly readable Markdown, pass local checks, and have recorded beginner read-test evidence or remain clearly unpromoted.
- Commit message: `M3: add first Markdown primer slice`
- Milestone closeout:
  - local automated validation passed for the five draft pages
  - MP1 and MP2 manual proof records exist
  - MP3 beginner read-test evidence is recorded with readability revisions,
    beginner-reader approval, and required per-page comprehension outcomes
  - any referenced media passes M3A validation
  - pages without media remain valid and do not require generated images
  - clean code-review recorded in `docs/changes/markdown-first-gym-primer/reviews/code-review-m3-r3.md`
- Risks:
  - Beginner read-test feedback may show confusion about setup or stop conditions.
  - Source links may be unstable or insufficient for a safety claim.
- Rollback/recovery:
  - Keep failing pages labeled non-canonical and do not link them from active README navigation until revised and rechecked.

### M4. Optional mdBook and Final Local Quality Gate

- Milestone state: closed
- Goal: Add minimal mdBook only if it stays trivial after the Markdown pages work directly; otherwise record a deferral and complete the local quality gate without generated HTML.
- Requirements: R31-R33, R36-R40, AC10-AC13
- Files/components likely touched:
  - `book.toml`
  - `SUMMARY.md`
  - `.gitignore`
  - `README.md`
  - `docs/changes/markdown-first-gym-primer/manual-proof/`
- Dependencies:
  - M3 pages and README navigation closed.
  - M3A media provenance validation closed if any raster media is referenced
    by promoted pages.
- Tests to add/update:
  - If mdBook is added, add a minimal command check or documented manual proof for `mdbook build`.
  - If mdBook is deferred, add a durable deferral note explaining the blocker or unavailable tool.
- Implementation steps:
  - Check whether `mdbook` is installed.
  - If installed and default configuration works, add minimal `book.toml` and `SUMMARY.md`; ensure generated `book/` is ignored.
  - If `mdbook` is missing or requires plugins, custom themes, layout churn, or non-trivial styling, record deferral instead of adding derived output.
  - Run the final local quality gate and update validation notes.
- Validation commands:
  - `command -v mdbook || true`
  - `mdbook build`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer`
- Expected observable result: mdBook either builds from minimal configuration or is explicitly deferred; Markdown remains the source of truth either way.
- Commit message: `M4: finalize optional Markdown primer output`
- Milestone closeout:
  - validation passed
  - `MP4-mdbook-build-or-deferral.md` records mdBook deferral because the
    binary is unavailable
  - `MP5-validation-command-ledger.md` records the final local quality gate and
    source-of-truth drift inspection
  - progress updated
  - decision log updated for mdBook deferral
  - validation notes updated
  - milestone handoff commit not created because the branch already contains
    uncommitted upstream workflow artifacts; code-review should review the
    working tree state for M4
  - clean code-review recorded in `docs/changes/markdown-first-gym-primer/reviews/code-review-m4-r1.md`
- Risks:
  - mdBook availability could vary across contributors.
  - Derived HTML may distract from Markdown quality if custom styling starts here.
- Rollback/recovery:
  - Remove `book.toml` and `SUMMARY.md` and keep the Markdown pages and README navigation as the complete product.

## Validation plan

- `rg -n "^- Status:|^- Plan lifecycle state:|^- Terminal disposition:" docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plans/2026-06-26-content-schema-foundation.md`: confirms plan lifecycle markers exist.
- `rg -n "Current milestone: M2|Next stage: review-resolution|resolution-needed|superseded by:" docs/plan.md`: confirms plan index routing during M2 finding resolution.
- `rg -n "^- approved$|architecture-review-r1|Next stage: plan" docs/architecture/system/architecture.md docs/changes/markdown-first-gym-primer/reviews/architecture-review-r1.md`: confirms upstream architecture status settlement.
- `rg -n "^- approved$|architecture-review-r3|ready for downstream test-spec" docs/architecture/system/architecture.md`: confirms media architecture status settlement.
- `rg -n "^accepted$|AI-Generated Raster Media Provenance" docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`: confirms media ADR status settlement.
- `rg -n "\\.svg|\\.png|\\.jpg|\\.jpeg|\\.webp|before provenance lookup|media_asset_missing" docs/architecture/system/architecture.md docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`: confirms deterministic media classification remains documented.
- `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`: validates Markdown-first check tests after M2.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`: validates page shape, source, disclaimer, scope, media, and citation rules after M2/M3.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer`: validates negative-match privacy behavior after M2/M3.
- `python3 -m unittest tests.test_markdown_first_guardrails`: validates media
  classification and provenance fixtures after M3A.
- `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md media docs/changes/markdown-first-gym-primer`: validates media and provenance artifacts after M3A.
- `mdbook build`: validates optional derived HTML only when mdBook is installed and accepted for M4.
- Manual GitHub-render inspection or direct Markdown inspection: validates readable pages when local GitHub rendering is unavailable.
- Manual beginner read-test record: validates AC12 and R38-R39.

## Risks and recovery

- Risk: Old structured-platform files keep confusing contributors.
  - Recovery: Add stronger supersession notices or run a later archive-only change moving old artifacts under `docs/archive/structured-platform-2026-06/`.
- Risk: Citation checks are too weak to prove claim support.
  - Recovery: Treat tooling as a minimum gate and require manual citation review in code-review and verify.
- Risk: Reader testing finds the pages unclear.
  - Recovery: Keep affected pages non-canonical, revise them, and rerun the read test before promotion.
- Risk: mdBook creates layout churn or dependency friction.
  - Recovery: Defer mdBook and rely on GitHub-readable Markdown.
- Risk: AI-generated raster images bypass provenance because classification is
  ambiguous.
  - Recovery: Keep the strict v0.1 extension classifier and fail all raster
    images under `media/` without approved provenance.
- Risk: generated raster illustrations are misleading or unsafe.
  - Recovery: Reject or revise the asset in `media/PROVENANCE.md`; remove the
    Markdown image reference until human review approves it.
- Risk: Existing old tests conflict with new workflow.
  - Recovery: Keep old tests as historical or move them with old-platform artifacts in a later archive decision; do not use them as v0.1 readiness gates.

## Dependencies

- Plan-review must approve this plan before implementation.
- Test-spec and test-spec-review must map the spec requirements, media
  provenance architecture, and this plan to concrete automated and manual
  checks before implementation.
- At least one beginner reader must be available for M3 read-test evidence before first-slice promotion.
- Public sources used by cards must remain reachable or be replaced before promotion.
- `mdbook`, `markdownlint`, and link-checking tools are optional unless installed and adopted by a reviewed downstream artifact; missing tools are reported as gaps.

## Progress

- 2026-06-27: Created execution plan after accepted proposal, approved spec, approved architecture review, and architecture status normalization.
- 2026-06-27: `test-spec-review-r2` approved implementation handoff after TSR1 was resolved; next stage is implement M1.
- 2026-06-27: Implemented M1 active route, contributor/license contract, source index, templates, legacy supersession notices, and M1 contract tests.
- 2026-06-27: M1 validation passed and the milestone moved to `review-requested` for code-review.
- 2026-06-27: `code-review-m1-r1` reviewed M1 as clean-with-notes, recorded no material findings, closed M1, and routed to implement M2.
- 2026-06-27: Implemented M2 Markdown-first checker CLI, privacy checker CLI, deterministic fixtures, and unit tests for page structure, citations, scope/language/media guardrails, and privacy scan semantics.
- 2026-06-27: M2 validation passed and the milestone moved to `review-requested` for code-review.
- 2026-06-27: `code-review-m2-r1` requested changes for CR-M2-1 because the checker does not enforce `SOURCES.md` coverage for reused source IDs required by T4.
- 2026-06-27: Addressed CR-M2-1 by making `SOURCES.md` a real global source-index input, adding source-index regression fixtures, and rerunning M2 validation. M2 returned to `review-requested` for code-review M2 R2.
- 2026-06-27: `code-review-m2-r2` reviewed CR-M2-1 as resolved, recorded no material findings, closed M2, and routed to implement M3.
- 2026-06-27: Implemented the local M3 draft slice: five Markdown pages,
  README draft links, real-page tests, MP1 direct Markdown inspection, and MP2
  citation review. M3 remains blocked because MP3 beginner comprehension
  evidence has not been collected.
- 2026-06-28: Updated the plan for the approved AI-generated raster media
  provenance contract after spec-review R3, architecture-review R3, and
  architecture/ADR status normalization. Added M3A for media classification,
  provenance validation, and optional first-slice images.
- 2026-06-28: Resolved PR-MEDIA-1 by choosing Option A: M3A is the next
  executable implementation target after test-spec review approval, while M3
  remains promotion-blocked until MP3 evidence is collected and any referenced
  media passes M3A validation.
- 2026-06-28: Implemented M3A media validation. The Markdown-first checker now
  classifies image references before provenance lookup, allows SVG diagrams
  under `media/`, requires approved provenance for `.png`, `.jpg`, `.jpeg`,
  and `.webp` raster assets, rejects external/out-of-directory/unsupported or
  missing media, and creates the empty `media/PROVENANCE.md` contract. M3A
  validation passed and the milestone moved to `review-requested` for
  code-review.
- 2026-06-28: `code-review-m3a-r1` reviewed M3A as clean-with-notes, recorded
  no material findings, closed M3A, and returned the workflow to the existing
  M3 closeout blocker: missing MP3 beginner read-test evidence.
- 2026-06-28: Recorded MP3 beginner read-test evidence after a non-identifying
  beginner reader reviewed `01-*`, `02-*`, and `03-*` documents, reported
  readability problems, approved the implementation after example pictures were
  added, and moved M3 to `review-requested` for code-review R2.
- 2026-06-28: `code-review-m3-r2` requested changes for CR-M3-1 because MP3
  records reader approval after readability revisions but does not record the
  required per-page comprehension outcomes for purpose, setup, steps, and stop
  condition.
- 2026-06-29: Addressed CR-M3-1 by updating MP3 with non-identifying
  principle-page and exercise-page comprehension outcomes, confusion/revision
  records, and final MP3 pass conclusion; M3 returned to `review-requested`
  for code-review R3.
- 2026-06-29: `code-review-m3-r3` reviewed the CR-M3-1 resolution as
  clean-with-notes, closed CR-M3-1, closed M3, and routed the change to
  implement M4.
- 2026-06-29: Implemented M4 by adding mdBook deferral proof, final validation
  command ledger, source-of-truth drift inspection, and M4 tests for mdBook
  deferral, validation observability, and compatibility. M4 validation passed
  and the milestone moved to `review-requested` for code-review R1.
- 2026-06-29: `code-review-m4-r1` reviewed M4 as clean-with-notes, closed M4,
  and routed the change to explain-change.
- 2026-06-29: Recorded `docs/changes/markdown-first-gym-primer/explain-change.md`
  with the final reviewed diff rationale and routed the change to verify.
- 2026-06-29: Recorded final local verification in
  `docs/changes/markdown-first-gym-primer/verify-report.md`, marked the change
  branch-ready for PR handoff, and routed the change to pr.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-27 | Mark old structured-platform implementation and plan as superseded in place for v0.1. | Preserves traceability and avoids broad path churn while the Markdown-first slice is still being proven. | Delete old files; immediately move all old files under `docs/archive/`; leave old plan active. |
| 2026-06-27 | Sequence check tooling before first-slice promotion. | The spec requires disclaimers, citations, scope, media, and privacy proof before promotion claims. | Write content first and validate only manually. |
| 2026-06-27 | Treat mdBook as the final optional milestone. | The spec allows mdBook only after the five Markdown pages work directly. | Add mdBook before content; defer without checking whether minimal setup is trivial. |
| 2026-06-28 | Add M3A before any generated raster images are promoted. | The approved media architecture requires deterministic classification and approved provenance before raster assets can appear in promoted pages. | Generate images first and document provenance later; fold media validation into M4; allow raster assets without provenance. |
| 2026-06-28 | Make M3A the next executable target while M3 remains promotion-blocked. | M3A is validation infrastructure and can proceed before MP3, but M3 cannot close until MP3 and media validation gates pass. | Make M3A depend on MP3; allow M3 code-review before media validation; keep both M3 and M3A as ambiguous next targets. |
| 2026-06-29 | Defer mdBook in M4. | `mdbook` is not installed in the local validation environment, and v0.1 Markdown remains usable directly without generated HTML. | Add unchecked mdBook config; require contributors to install mdBook before proving Markdown content; treat generated HTML as source of truth. |

## Surprises and discoveries

- `docs/project-map.md` is stale and still describes the pre-implementation/pre-pivot repository. It should not be used as active Markdown-first architecture evidence.
- `docs/plan.md` still listed the old content-schema plan as active before this plan-stage update.
- The active README still advertised generated public JSON and old validator commands before M1; M1 replaced those with Markdown-first navigation and validation guidance.
- The first privacy pattern treated the word `secrets` in policy guidance as a finding; M2 narrowed the privacy scan to concrete private paths, secret assignments/keys, PHI assignments, and personal health profiles so repository guidance can be scanned without false positives.
- The M3A privacy scan found an existing review phrase, `local private paths`,
  that matched the broad `private[-_ ]?path` pattern even though it was policy
  language rather than a leaked path. The scan was narrowed to concrete private
  path forms while preserving `/home/...` and secret/PHI detection.

## Validation notes

- 2026-06-27 M1 pre-change proof: `python3 -m unittest tests.test_markdown_first_contract tests.test_markdown_first_templates tests.test_markdown_first_legacy_boundary` failed as expected because `SOURCES.md`, `CONTENT_LICENSE.md`, and templates were missing; README still routed to generated JSON; and old implementation directories lacked supersession notices.
- 2026-06-27 M1 targeted tests: `python3 -m unittest tests.test_markdown_first_contract tests.test_markdown_first_templates tests.test_markdown_first_legacy_boundary` passed with 7 tests.
- 2026-06-27 M1 structural check: `rg -n "Markdown-first|source of truth|01-getting-started|02-machines|03-bodyweight|SOURCES.md" README.md` passed.
- 2026-06-27 M1 structural check: `rg -n "Apache-2.0|CC BY 4.0|right to submit|third-party media|claim-level|not medical advice" CONTRIBUTING.md CONTENT_LICENSE.md` passed.
- 2026-06-27 M1 structural check: `test -f SOURCES.md && test -f CONTENT_LICENSE.md && test -f docs/templates/exercise-card.md && test -f docs/templates/principle-page.md` passed.
- 2026-06-27 M1 structural check: `rg -n "superseded|Markdown-first" docs/plans/2026-06-26-content-schema-foundation.md content/README.md schemas/README.md generated/README.md tools/validation/README.md` passed.
- 2026-06-27 M1 code review: `code-review-m1-r1` reran the M1 targeted tests and structural checks, found no material issues, and did not require review-resolution.
- 2026-06-27 M2 pre-change proof: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` failed as expected because `tools/checks/check_markdown_first.py` and `tools/checks/check_privacy.py` did not exist.
- 2026-06-27 M2 targeted tests: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 23 tests.
- 2026-06-27 M2 command check: `python3 tools/checks/check_markdown_first.py --help` passed.
- 2026-06-27 M2 privacy check: `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md` passed.
- 2026-06-27 M2 conditional lint check: `if command -v markdownlint >/dev/null 2>&1; then markdownlint "**/*.md"; else printf 'markdownlint not installed\n'; fi` reported `markdownlint not installed`; CMD6 is deferred because the external tool is unavailable.
- 2026-06-27 M2 code review: `code-review-m2-r1` reran `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`, which passed with 23 tests, but an adversarial temporary-page check showed that a safety-cited source ID absent from `SOURCES.md` still passed. CR-M2-1 was opened for resolution.
- 2026-06-27 CR-M2-1 pre-fix proof: `python3 -m unittest tests.test_markdown_first_citations` failed because missing global source IDs, reused local IDs, reused missing global IDs, and URL mismatches were not detected.
- 2026-06-27 CR-M2-1 targeted citation tests: `python3 -m unittest tests.test_markdown_first_citations` passed with 10 tests.
- 2026-06-27 CR-M2-1 M2 suite: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 29 tests.
- 2026-06-27 CR-M2-1 command check: `python3 tools/checks/check_markdown_first.py --help` passed.
- 2026-06-27 CR-M2-1 privacy check: `python3 tools/checks/check_privacy.py -- README.md CONTRIBUTING.md SOURCES.md CONTENT_LICENSE.md` passed.
- 2026-06-27 CR-M2-1 adversarial check: `python3 tools/checks/check_markdown_first.py tests/fixtures/markdown-first/citations/missing-global-source-id.md; test $? -eq 1` passed and reported `source_id_missing_from_sources_md` for `unknown-source`.
- 2026-06-27 CR-M2-1 conditional lint check: `if command -v markdownlint >/dev/null 2>&1; then markdownlint "**/*.md"; else printf 'markdownlint not installed\n'; fi` reported `markdownlint not installed`; CMD6 remains deferred.
- 2026-06-27 M2 R2 code review: `code-review-m2-r2` reran the M2 citation tests, full Markdown-first suite, source-index adversarial checks, checker help, privacy scan, conditional markdownlint check, and `git diff --check`; CR-M2-1 is resolved and M2 is closed.
- 2026-06-27 M3 pre-change proof: `python3 -m unittest tests.test_markdown_first_real_pages` failed as expected because the five first-slice pages and README draft links did not exist.
- 2026-06-27 M3 targeted tests: `python3 -m unittest tests.test_markdown_first_real_pages` passed with 3 tests.
- 2026-06-27 M3 full Markdown-first suite: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 32 tests.
- 2026-06-27 M3 Markdown-first check: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight` passed.
- 2026-06-27 M3 privacy check: `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer/manual-proof` passed.
- 2026-06-27 M3 excluded-scope scan: `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi` printed `no excluded-scope terms found`.
- 2026-06-27 M3 scoped lint check: `markdownlint 01-getting-started 02-machines 03-bodyweight docs/changes/markdown-first-gym-primer/manual-proof` passed after formatting the new M3 files.
- 2026-06-27 M3 repository-wide lint check: `markdownlint "**/*.md"` failed with broad pre-existing MD013/table/reference issues across legacy and workflow documents; it is not a current M3 gate.
- 2026-06-27 M3 diff whitespace check: `git diff --check` passed.
- 2026-06-28 media architecture status check: `rg -n "^- approved$|architecture-review-r3|ready for downstream test-spec" docs/architecture/system/architecture.md` passed.
- 2026-06-28 media ADR status check: `rg -n "^accepted$|AI-Generated Raster Media Provenance" docs/adr/2026-06-28-ai-generated-raster-media-provenance.md` passed.
- 2026-06-28 media classifier architecture check: `rg -n "\\.svg|\\.png|\\.jpg|\\.jpeg|\\.webp|before provenance lookup|media_asset_missing" docs/architecture/system/architecture.md docs/adr/2026-06-28-ai-generated-raster-media-provenance.md` passed.
- 2026-06-28 M3A pre-change proof: `python3 -m unittest tests.test_markdown_first_guardrails` failed as expected because raster media classification and provenance validation were not implemented.
- 2026-06-28 M3A targeted tests: `python3 -m unittest tests.test_markdown_first_guardrails` passed with 17 tests.
- 2026-06-28 M3A full Markdown-first suite: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 44 tests.
- 2026-06-28 M3A Markdown-first check: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight` passed.
- 2026-06-28 M3A privacy regression test: `python3 -m unittest tests.test_markdown_first_privacy` passed with 3 tests after narrowing a false-positive privacy pattern.
- 2026-06-28 M3A privacy check: `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md media docs/changes/markdown-first-gym-primer` passed.
- 2026-06-28 M3A scoped lint check: `markdownlint --disable MD013 -- media/PROVENANCE.md docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md docs/changes/markdown-first-gym-primer/explain-change.md docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plan.md docs/workflows.md specs/markdown-first-primer.test.md` passed.
- 2026-06-28 M3A diff whitespace check: `git diff --check` passed.
- 2026-06-28 M3 MP3 evidence update: recorded non-identifying beginner-reader
  review evidence in `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md`.
- 2026-06-28 M3 rerun after MP3 evidence update: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 44 tests.
- 2026-06-28 M3 rerun after MP3 evidence update: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight` passed.
- 2026-06-28 M3 rerun after MP3 evidence update: `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer/manual-proof` passed.
- 2026-06-28 M3 rerun after MP3 evidence update: `markdownlint --disable MD013 -- docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plan.md docs/workflows.md` passed.
- 2026-06-28 M3 rerun after MP3 evidence update: `git diff --check` passed.
- 2026-06-29 CR-M3-1 resolution validation: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 44 tests.
- 2026-06-29 CR-M3-1 resolution validation: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight` passed.
- 2026-06-29 CR-M3-1 resolution validation: `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer/manual-proof` passed.
- 2026-06-29 CR-M3-1 resolution validation: `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi` printed `no excluded-scope terms found`.
- 2026-06-29 M4 pre-change proof: `python3 -m unittest tests.test_markdown_first_mdbook tests.test_markdown_first_observability tests.test_markdown_first_compatibility` failed as expected because MP4 and MP5 did not exist.
- 2026-06-29 M4 focused tests: `python3 -m unittest tests.test_markdown_first_mdbook tests.test_markdown_first_observability tests.test_markdown_first_compatibility` passed with 7 tests.
- 2026-06-29 M4 mdBook availability check: `command -v mdbook || true` produced no path.
- 2026-06-29 M4 mdBook deferral command: `if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf 'mdbook not installed; mdBook deferred\n'; fi` printed `mdbook not installed; mdBook deferred`.
- 2026-06-29 M4 full Markdown-first suite: `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` passed with 51 tests.
- 2026-06-29 M4 Markdown-first check: `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight` passed.
- 2026-06-29 M4 privacy scan: `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer` passed.
- 2026-06-29 M4 excluded-scope scan: `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi` printed `no excluded-scope terms found`.

## Outcome and retrospective

- Pending until all implementation milestones and downstream review/verification gates complete.

## Readiness

- See `Current Handoff Summary`.
- M3A is closed.
- All implementation milestones are closed. Ready for explain-change. Not ready
  for final verification, branch handoff, or PR until explain-change and
  downstream verification complete.
