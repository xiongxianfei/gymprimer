# Spec: Markdown-First Gym Primer

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-06-27-markdown-first-gym-primer.md`
- Proposal review: `docs/changes/markdown-first-gym-primer/reviews/proposal-review-r2.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for GymPrimer's Markdown-first v0.1 content slice. The product source of truth is self-contained Markdown pages in the repository, with citation-based authority, conservative beginner scope, visible disclaimers, page-local sources, and optional derived mdBook HTML.

The spec replaces the prior structured content-schema direction for this slice. It does not define an app, database, generated public JSON package, formal expert-review lifecycle, CMS workflow, AI assistant, or hosted website.

## Glossary

- Markdown page: A `.md` file that is readable directly in GitHub or a cloned repository.
- Exercise page: A Markdown page that teaches one exercise or equipment pattern.
- Principle page: A Markdown page that teaches a general beginner training concept.
- v0.1 first slice: The five selected English-first pages used to prove the format.
- Claim-level citation: A source link placed next to, or in the same paragraph as, the claim it supports.
- Page-local sources: A `Sources` section in the same Markdown page as the claims.
- Global source index: `SOURCES.md`, used to list sources reused across pages.
- Disclaimer: A prominent statement that the content is educational, not medical advice or personalized coaching.
- Non-canonical spike: Draft content used to test the format before promotion to active source of truth.
- Derived HTML: Static HTML generated from Markdown, such as mdBook output, that does not replace Markdown as source.
- AI-generated raster illustration: A bitmap image generated with an AI image
  tool and reviewed by a human maintainer before use as supporting educational
  media.
- Media provenance record: A repository-tracked record that identifies an
  image's generator or source, prompt or creation notes, date, author or
  maintainer, license assertion, and human review status.
- First-slice media purpose: The reason an image is included in v0.1. Allowed
  values are `equipment_identification` and `key_movement_illustration`.
- Media provenance index: The single repository-tracked file
  `media/PROVENANCE.md`, containing one row per AI-generated raster
  illustration.

## Examples first

Example E1: a beginner opens a machine page directly
Given `02-machines/lat-pulldown.md` exists as a Markdown page
When a reader opens the file on GitHub
Then the reader can see the disclaimer, purpose, setup, muscles, movement breakdown, feel cues, common mistakes, easier and harder versions, safety notes, and sources without using a separate app.

Example E2: a safety warning is source-backed
Given an exercise page warns the reader to stop for sharp or worsening symptoms
When a reviewer checks the warning
Then the warning has a claim-level citation to a public source and the source also appears in the page's `Sources` section.

Example E3: a global-only source is insufficient
Given a page makes a safety claim
And the source appears only in `SOURCES.md`
When source coverage is checked
Then the page fails the source check because the reader cannot verify the claim from the page alone.

Example E4: an out-of-scope page is rejected
Given a contributor adds `02-machines/barbell-deadlift.md` or content that claims to treat knee pain
When scope checks or maintainer review run
Then the page is rejected for v0.1 scope.

Example E5: mdBook stays derived
Given five Markdown pages render directly on GitHub
When minimal mdBook configuration is added
Then `mdbook build` may generate derived HTML, but the Markdown files remain the canonical product.

Example E6: an AI-generated illustration is added to a page
Given a maintainer adds an AI-generated raster illustration under `media/`
When the page and media are reviewed
Then the image uses a relative path, has alt or adjacent explanatory text, has
a media provenance record, is licensed for project use, and does not replace
the Markdown explanation.

Example E7: a page stays text-only
Given `01-getting-started/beginner-training-principles.md` is understandable
without images
When the page is reviewed
Then it remains valid without any media reference or provenance row.

Example E8: a missing provenance row fails validation
Given `02-machines/lat-pulldown.md` references
`../media/equipment/lat-pulldown-machine.png`
And the normalized asset path is `media/equipment/lat-pulldown-machine.png`
When media validation checks `media/PROVENANCE.md`
Then validation fails if no row has exactly that `asset_path`.

## Requirements

R1. The repository MUST treat Markdown files as the source of truth for v0.1 beginner education.

R2. The first slice MUST include exactly these five Markdown pages before broader content expansion: `01-getting-started/beginner-training-principles.md`, `02-machines/lat-pulldown.md`, `02-machines/seated-row.md`, `02-machines/chest-press.md`, and `03-bodyweight/incline-push-up.md`.

R3. Each v0.1 Markdown page MUST be readable directly in GitHub without requiring generated HTML, JavaScript, a database, search index, account, app shell, or local server.

R4. The root `README.md` MUST provide repository navigation to the v0.1 pages once those pages are promoted from spike to active source content.

R5. Each exercise page MUST include these headings or equivalent page-local sections: purpose, equipment setup, muscles involved, movement breakdown, feel cues, common mistakes, easier version, harder version, safety notes, and sources.

R6. Each principle page MUST include a disclaimer, beginner-readable explanation, scope boundaries, safety notes when applicable, and sources.

R7. Every safety-relevant page MUST include a prominent disclaimer near the top of the page.

R8. The disclaimer MUST state that GymPrimer is educational content, not medical advice and not personalized coaching.

R9. Safety warnings MUST have claim-level citations to public, named sources.

R10. Weekly activity guidance MUST cite a public-health or professional guidance source.

R11. Exercise technique claims SHOULD cite an authoritative instructional source because technique claims affect reader safety.

R12. Feel cues MUST be framed as practical beginner orientation unless they are anatomy or safety claims; anatomy or safety feel cues MUST have claim-level citations.

R13. Every Markdown page MUST include a `Sources` section listing the sources used on that page.

R14. A source reused across more than one page MUST appear in `SOURCES.md`.

R15. `SOURCES.md` MUST NOT be the only citation surface for a safety claim.

R16. Reference-style Markdown links SHOULD be used for v0.1 citations because they are portable across GitHub-rendered Markdown and mdBook.

R17. v0.1 content MUST be English-first.

R18. v0.1 pages MAY include Chinese aliases for exercise recognition.

R19. v0.1 pages MUST NOT include full-card Chinese translation.

R20. Future full Chinese translation MUST use a separate reviewed locale path before it becomes active source content.

R21. v0.1 content MUST stay within beginner training principles, common machine exercises, low-risk bodyweight progressions, simple dumbbell patterns, and basic cardio equipment.

R22. v0.1 content MUST NOT include barbell lifts, Olympic lifting, kettlebell ballistic lifts, plyometrics, sprint programming, sport-specific programming, injury-specific advice, posture-correction protocols, pain treatment, diagnosis, or rehabilitation pathways.

R23. v0.1 media MUST be either original educational diagrams,
human-reviewed AI-generated raster illustrations, or no media.

R23a. v0.1 images are optional and MUST be used only when they are necessary
supporting visuals for equipment identification or key movement illustration.

R23b. v0.1 media SHOULD follow this preference order: no image, then simple
original SVG, then AI-generated raster illustration only when the page needs a
picture and a simple original SVG is not enough.

R24. v0.1 content MUST NOT use third-party screenshots, stock photos, borrowed public web images, or commercial machine screenshots.

R25. Every media reference MUST use a relative repository path and have enough surrounding text or alt text for a reader to understand its educational purpose.

R26. Code and tooling contributions MUST be documented as Apache-2.0.

R27. Written content and original educational diagrams MUST be documented as CC BY 4.0.

R28. Contributor guidance MUST state that contributors have the right to submit their content and are not submitting undocumented third-party media.

R29. A non-canonical first-card spike MUST be clearly labeled as non-canonical until governance, architecture/ADR, and required checks allow promotion.

R30. Spike pages MUST NOT be described as published, approved, expert-reviewed, or active source of truth before promotion.

R31. mdBook configuration MAY be added only after the five Markdown pages exist and render directly as Markdown.

R32. mdBook output MUST be treated as derived HTML and MUST NOT become the source of truth.

R33. If mdBook requires custom plugins, custom themes, layout churn, or non-trivial styling for v0.1, mdBook MUST be deferred.

R34. The old structured content-schema spec and repository-native reviewed-content ADR MUST NOT be used as active implementation guidance for Markdown-first v0.1 when they conflict with this spec.

R35. Superseded old-platform artifacts MUST remain traceable as historical context until a later archive decision moves them.

R36. Local validation SHOULD include checks for Markdown rendering, source sections, claim-level safety citations, disclaimers, excluded-scope terms, relative media paths, link health, privacy, and optional mdBook build.

R37. Privacy scans MUST pass only when forbidden patterns are absent; raw positive-match `rg` output alone is not an acceptable passing privacy check.

R38. The first slice MUST include a beginner read test with at least one beginner reader before the spike is promoted.

R39. Beginner read-test evidence MUST record whether the reader could explain each exercise page's purpose, setup, steps, and stop condition after reading.

R40. The project MUST NOT claim CI passed unless a real CI run was observed.

R41. Every AI-generated raster illustration MUST have a media provenance record
before the page that references it is promoted.

R42. AI-generated raster illustration provenance MUST be recorded in
`media/PROVENANCE.md`, using one Markdown table row per AI-generated raster
asset.

R43. AI-generated raster illustrations MUST be supporting visual aids only; the
Markdown text remains the source of instructional guidance.

R44. AI-generated raster illustrations MUST NOT depict unsafe setup, excluded
v0.1 exercise scope, medical treatment, diagnosis, identifiable private people,
or misleading equipment-specific branding.

R45. Contributor guidance MUST explain how AI-generated raster illustrations
are licensed, how provenance is recorded, and when such images are rejected.

R46. Each `media/PROVENANCE.md` row for an AI-generated raster illustration
MUST include these fields: `asset_path`, `asset_type`, `media_purpose`,
`generator`, `prompt_or_creation_notes`, `created_date`, `human_reviewer`,
`license_assertion`, `source_inputs`, `review_status`, `page_refs`, and
`notes`.

R47. The `asset_path` field MUST be the exact repository-relative normalized
path to the image, without a leading `./` or `/`.

R48. A provenance row matches a Markdown image reference only when `asset_path`
exactly equals the repository-relative path produced by resolving the image
reference from the Markdown page.

R49. `asset_type` MUST be `ai_generated_raster` for AI-generated raster
illustrations.

R50. `media_purpose` MUST be `equipment_identification` or
`key_movement_illustration` for v0.1.

R51. `review_status` MUST be one of `approved`, `needs_revision`, or
`rejected`; a promoted page may reference the image only when `review_status`
is `approved`.

R52. `page_refs` MUST include every promoted Markdown page that references the
asset, using repository-relative Markdown paths.

R53. A promoted Markdown page MUST fail media validation when it references an
AI-generated raster illustration whose provenance row is missing, whose
required fields are blank, whose `review_status` is not `approved`, whose
`media_purpose` is outside v0.1 scope, or whose `page_refs` does not include
the page.

## Inputs and outputs

Inputs:

- Markdown source pages under numbered beginner content directories.
- Root navigation in `README.md`.
- Source index in `SOURCES.md`.
- Contributor guidance in `CONTRIBUTING.md`.
- Optional original diagrams under `media/`.
- Optional AI-generated raster illustrations under `media/`.
- `media/PROVENANCE.md` for AI-generated raster illustration provenance.
- Optional mdBook config in `book.toml` and `SUMMARY.md`.
- Public source links used by content pages.

Outputs:

- GitHub-readable Markdown pages.
- Page-local `Sources` sections.
- Global reusable source index.
- Optional derived HTML under the mdBook output directory.
- Validation evidence from local commands or manual checks.
- Beginner read-test notes for the first slice.
- `media/PROVENANCE.md` rows for referenced AI-generated raster images.

## State and invariants

- Markdown pages are canonical source content after promotion.
- Non-canonical spike pages are not active source content until explicitly promoted.
- Derived HTML never outranks Markdown.
- Safety claims are not valid without page-local claim-level citations.
- v0.1 remains English-first.
- Old platform artifacts remain historical when they conflict with current governance.
- A page that enters excluded medical, rehab, or advanced lifting scope is not eligible for v0.1.
- Images support Markdown explanations; they do not become the instructional
  source of truth.
- AI-generated raster illustrations are not eligible for promotion without
  human review and provenance.
- Text-only pages remain valid when no image is necessary.
- AI-generated raster provenance is centralized in `media/PROVENANCE.md`.

## Error and boundary behavior

- Missing disclaimer on a safety-relevant page blocks promotion.
- Missing page-local sources block promotion.
- Global-only citation for a safety claim blocks promotion.
- Broken source links block promotion unless the source is replaced or the broken link is explicitly recorded as deferred with risk.
- Third-party, unclear-license, or unprovenanced media blocks promotion.
- AI-generated media without a provenance record blocks promotion.
- AI-generated media that conflicts with the written instructions blocks
  promotion until the media is replaced or the page is revised.
- AI-generated media outside `equipment_identification` or
  `key_movement_illustration` blocks promotion.
- AI-generated media with missing, blank, or non-approved provenance blocks
  promotion.
- AI-generated media whose provenance `page_refs` omit the referencing page
  blocks promotion.
- Content that diagnoses, treats pain, prescribes rehab, or teaches excluded advanced lifts blocks promotion.
- mdBook failure blocks only derived HTML, not GitHub-readable Markdown, unless Markdown itself no longer renders or navigates.
- Missing `mdbook`, `markdownlint`, `lychee`, or local check scripts must be reported as validation gaps rather than silently treated as pass.

## Compatibility and migration

- Compatibility note: Responsible Breadth expansion.
  This spec remains the governing contract for the original Markdown-first v0.1
  slice and for shared Markdown source-of-truth, citation, media, privacy,
  mdBook-derived-output, and promotion requirements.
- If `specs/responsible-breadth.md` is approved, it governs expanded pattern,
  condition, programming-principle, static program-example, and expanded
  visual-standard pages. For those expanded page types only,
  `specs/responsible-breadth.md` supersedes this spec's original v0.1
  content-scope exclusions.
- This spec's prohibitions on diagnosis, personalized treatment, personalized
  programming, rehabilitation protocols, unsafe media, private data, and
  AI-generated source-of-truth content remain active unless a later
  higher-ranked artifact explicitly changes them.
- Existing structured-platform artifacts remain in the repository as historical context until a superseding ADR or archive decision changes their status.
- Existing generated output and validator artifacts are not v0.1 product surfaces for the Markdown-first primer.
- Stable Markdown paths and headings become compatibility surfaces once linked from `README.md` or `SUMMARY.md`.
- AI-generated raster illustration `asset_path` values in
  `media/PROVENANCE.md` become compatibility surfaces once referenced by a
  promoted page.
- Future locale migration must preserve existing English Markdown URLs unless an accepted proposal and migration plan approve a path change.
- Rollback from mdBook must leave Markdown pages usable and linked from `README.md`.

## Observability

- Local validation output must identify which page, source, disclaimer, scope term, media path, or link failed when a check fails.
- Media validation output must identify the page path, normalized `asset_path`,
  and stable failure code when media provenance fails. Stable media failure
  codes are `media_provenance_missing`,
  `media_provenance_incomplete`, `media_provenance_not_approved`,
  `media_usage_out_of_scope`, and `media_page_refs_mismatch`.
- Manual validation records must list the exact files inspected and the observed pass/fail result.
- Beginner read-test records must identify the page tested, the reader type at a non-identifying level, the questions asked, and the comprehension result.
- Completion reports must include exact commands run, skipped commands, and residual risks.

## Security and privacy

- Markdown pages, examples, validation output, and read-test notes MUST NOT include private health information, real user health profiles, private contact details, secrets, credentials, or local machine paths.
- Safety content MUST NOT diagnose conditions, prescribe treatment, or imply medical authority.
- AI-generated exercise wording MUST NOT become source content unless a human author verifies scope, sources, and safety claims.
- External media MUST NOT be added without documented license compatibility.
- AI-generated raster illustrations MUST NOT include private people,
  identifying marks, third-party source images, or branding unless provenance
  and license compatibility are documented.
- Reader-test notes MUST avoid personally identifying participants.

## Accessibility and UX

- Pages must use plain headings and lists that render clearly in GitHub Markdown.
- Images, when present, must include alt text or adjacent explanatory text.
- AI-generated raster illustrations must be visually simple enough that a
  beginner can understand their purpose without relying on hidden context.
- The README navigation must be usable without a site renderer.
- Page titles must clearly name the exercise or principle.
- Link text should name the source or destination rather than using bare "click here" wording.

## Performance expectations

- The five-page first slice must be small enough to browse in GitHub without generated indexes.
- Optional local checks should complete on the v0.1 slice in under 30 seconds on a typical developer laptop, excluding network-dependent link checking.
- mdBook build, when used for v0.1, should run with default behavior and no custom plugin requirement.

## Edge cases

EC1. A page has sources but no claim-level citation on a stop rule.
Expected behavior: fail source coverage.

EC2. A page cites a source in text but omits the `Sources` section.
Expected behavior: fail page-local source structure.

EC3. A page includes a Chinese exercise alias.
Expected behavior: allowed when the full page remains English-first.

EC4. A page includes a full Chinese translation section.
Expected behavior: fail v0.1 language scope.

EC5. A contributor adds a licensed third-party image with attribution.
Expected behavior: reject for v0.1 unless a later media policy explicitly
allows external third-party media.

EC6. A maintainer adds an AI-generated raster illustration without provenance.
Expected behavior: fail media validation or manual review until a provenance
record is added.

EC7. A page references an AI-generated raster image whose provenance row has
blank required fields.
Expected behavior: fail with `media_provenance_incomplete`.

EC8. A page references an AI-generated raster image whose provenance row has
`review_status` set to `needs_revision` or `rejected`.
Expected behavior: fail with `media_provenance_not_approved`.

EC9. A page references an AI-generated raster image whose provenance row uses
`media_purpose` outside `equipment_identification` and
`key_movement_illustration`.
Expected behavior: fail with `media_usage_out_of_scope`.

EC10. A page references an AI-generated raster image, but the provenance row's
`page_refs` field does not include that page.
Expected behavior: fail with `media_page_refs_mismatch`.

EC11. An AI-generated raster illustration shows an excluded advanced lift or a
setup that conflicts with the Markdown instructions.
Expected behavior: reject or replace the image before promotion.

EC12. mdBook builds but changes navigation expectations away from GitHub-readable Markdown.
Expected behavior: reject the navigation change or defer mdBook.

EC13. A beginner read test shows confusion about stop conditions.
Expected behavior: revise the page before promotion.

EC14. A source link breaks after a page is otherwise ready.
Expected behavior: replace the source, archive an acceptable citation, or record the page as not ready.

EC15. An old generated JSON file contradicts a Markdown page.
Expected behavior: Markdown-first governance wins for v0.1; generated output is historical or derived.

EC16. A page uses "soreness vs pain" language.
Expected behavior: allowed only when it avoids diagnosis/treatment and uses conservative safety citations.

## Non-goals

- No hosted web app, CMS, database, account system, analytics, or deployment target.
- No formal expert-review lifecycle for v0.1.
- No generated public JSON package as the product.
- No broad exercise library beyond the first five pages in this spec.
- No full Chinese translation in v0.1.
- No external photos, screenshots, stock assets, borrowed web images, or
  commercial machine screenshots in v0.1.
- No unreviewed or unprovenanced AI-generated media in v0.1.
- No AI assistant, chatbot, personalized programming, progress tracking, trainer dashboard, or camera form analysis.
- No diagnosis, rehab, pain treatment, posture-correction protocol, or medical advice.
- No barbell, Olympic lifting, kettlebell ballistic, plyometric, sprint, sport-specific, or advanced programming content in v0.1.

## Acceptance criteria

AC1. The first slice contains the five required Markdown pages listed in R2.

AC2. Each first-slice page renders as readable Markdown in GitHub or by direct file inspection.

AC3. Each first-slice page includes a prominent disclaimer.

AC4. Each exercise page includes the required exercise-page sections from R5.

AC5. Every safety-relevant claim has a claim-level citation and page-local source entry.

AC6. Reused sources appear in `SOURCES.md`.

AC7. No first-slice page contains excluded scope content from R22.

AC8. No first-slice page uses prohibited third-party media from R24, and every
AI-generated raster illustration referenced by a first-slice page has
exactly one matching row in `media/PROVENANCE.md` using exact `asset_path`
matching.

AC9. Contributor guidance documents Apache-2.0 for code/tooling and CC BY 4.0
for written content, original educational diagrams, and accepted AI-generated
raster illustrations to the extent contributors have rights to license them.

AC10. If mdBook is included, `mdbook build` succeeds with minimal/default configuration; otherwise the decision to defer mdBook is recorded.

AC11. A privacy scan or manual privacy check reports no secrets, private health information, private contacts, or local machine paths in the first-slice content and validation outputs.

AC12. At least one beginner reader can explain purpose, setup, steps, and stop condition after reading each exercise page, or the page remains unpromoted.

AC13. Completion evidence reports exact commands run, commands unavailable, and residual risks.

AC14. Media validation or manual proof confirms that any AI-generated raster
illustration is a supporting visual aid, has relative-path usage and alt or
adjacent explanatory text, has provenance, and does not contradict the page's
Markdown instructions.

AC15. First-slice pages may include images only when they are necessary
supporting visuals for equipment identification or key movement illustration.

AC16. A page with no image remains valid when it otherwise satisfies the spec.

AC17. Required provenance fields in `media/PROVENANCE.md` are present and
non-blank for every referenced AI-generated raster illustration.

AC18. Referenced AI-generated raster illustrations have
`review_status = approved`.

AC19. Media validation fails with stable failure codes when provenance is
missing, incomplete, not approved, outside v0.1 media scope, or missing the
referencing page in `page_refs`.

## Open questions

- Who is the named maintainer empowered to accept citation quality and scope decisions for the first slice?
- Who is the named maintainer empowered to accept AI-generated media
  provenance and visual-safety decisions?
- What exact archive path or supersession format will be used for old structured-platform artifacts if moving them creates excessive diff churn?
- Which local tools will be installed for link checking and Markdown linting?

## Next artifacts

- `spec-review` for this spec.
- If approved, update architecture, test spec, plan, contributor guidance,
  content license notes, and Markdown-first media checks for AI-generated
  raster illustration provenance.
- Superseding ADR for Markdown-first citation-based authority and old artifact disposition.
- Architecture update if repository layout, mdBook, validation tooling, or archive movement crosses component boundaries.
- Test specification mapping these requirements to automated and manual checks.
- Card template and contributor guidance after spec review.

## Follow-on artifacts

None yet

## Readiness

This spec is ready for spec-review. It is not architecture-ready, plan-ready, implementation-ready, verification-ready, branch-ready, or PR-ready.
