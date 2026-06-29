# Spec: Responsible Breadth Content Expansion

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-06-29-responsible-breadth.md`
- Proposal review: `docs/changes/responsible-breadth/reviews/proposal-review-r3.md`
- Constitution: `CONSTITUTION.md`
- Vision: `VISION.md`
- Existing v0.1 spec: `specs/markdown-first-primer.md`

## Goal and context

This spec defines the observable contract for expanding GymPrimer beyond narrow
exercise literacy into static, citation-based education for common patterns,
well-studied conditions, programming principles, and generic program examples.

The expansion keeps Markdown as the source of truth. It does not define a
personalized coach, symptom checker, diagnostic tool, rehab product, hosted app,
CMS, account system, or runtime recommendation engine.

The approved Markdown-first v0.1 spec remains active for the original five-page
slice. This spec governs the Responsible Breadth expansion after review,
architecture, planning, test-spec, validation, and required downstream updates.

## Compatibility with `specs/markdown-first-primer.md`

This spec is an expansion spec. It does not replace the approved Markdown-first
v0.1 spec.

`specs/markdown-first-primer.md` remains the governing spec for:

- the original five-page Markdown-first v0.1 slice;
- Markdown-as-source-of-truth behavior;
- GitHub-readable page structure;
- page-local citations and global `SOURCES.md` behavior;
- media path, media provenance, and AI-raster rules;
- privacy scanning and no-private-data rules;
- mdBook as derived output;
- promotion, read-test, and manual-proof behavior unless this spec gives a
  stricter rule.

For Responsible Breadth pages only, this spec supersedes the Markdown-first
v0.1 content-scope restrictions that limited promoted content to the original
beginner-principles, machines, low-risk bodyweight, dumbbell, and basic-cardio
surface.

The expanded Responsible Breadth surface is limited to:

- pattern education pages;
- condition education pages;
- programming-principle pages;
- static program-example pages;
- exercise pages updated to the Responsible Breadth visual and citation
  standards.

All other Markdown-first requirements continue to apply unless this spec gives a
stricter rule.

### Original v0.1 slice preservation

The original Markdown-first five-page slice remains governed by
`specs/markdown-first-primer.md`.

Responsible Breadth does not retroactively require the original five-page slice
to include pattern pages, condition pages, program examples, or expanded visual
standards before the original v0.1 slice can close.

The original five-page slice may later be revised to adopt stricter Responsible
Breadth standards, but that is a separate content update and is not a
prerequisite for recognizing the original v0.1 contract.

### Governing requirement matrix

| Surface | Governing spec | Compatibility rule |
| --- | --- | --- |
| Original five-page v0.1 slice | `specs/markdown-first-primer.md` | Responsible Breadth does not change the closeout contract for the original slice. |
| New beginner exercise pages within original narrow scope | `specs/markdown-first-primer.md`, plus stricter Responsible Breadth visual/source rules if adopted for that page | Markdown-first governs baseline page structure; Responsible Breadth may add stricter visual/citation obligations. |
| Pattern education pages | `specs/responsible-breadth.md` | Responsible Breadth supersedes old v0.1 scope exclusions only to allow non-diagnostic pattern education. |
| Condition education pages | `specs/responsible-breadth.md` | Responsible Breadth supersedes old v0.1 scope exclusions only to allow consumer education with red-flag routing. |
| Programming-principle pages | `specs/responsible-breadth.md` | Responsible Breadth allows general programming literacy, not individualized prescription. |
| Static program examples | `specs/responsible-breadth.md` | Responsible Breadth allows worked examples, not personalized plans. |
| Markdown source-of-truth | `specs/markdown-first-primer.md` | Continues to apply. |
| Citation and `SOURCES.md` behavior | `specs/markdown-first-primer.md`, plus Responsible Breadth source-quality rules | Stricter source-quality requirements apply for patterns, conditions, principles, and programs. |
| Media provenance and image validation | `specs/markdown-first-primer.md`, plus Responsible Breadth visual-purpose rules | Provenance and path rules continue to apply; Responsible Breadth may require page-type-specific visual proof. |
| Privacy and no user-data collection | `specs/markdown-first-primer.md`, plus Responsible Breadth condition-page privacy rules | Stricter privacy rule applies. No symptom collection, reader identification, or personal inference. |
| Red-flags reference | `specs/responsible-breadth.md` | Required for pattern, condition, and other safety-relevant expanded pages. |
| mdBook / generated HTML | `specs/markdown-first-primer.md` | Remains derived output only. |

### Treatment of prior v0.1 exclusions

Responsible Breadth narrows some old v0.1 exclusions only for accepted expanded
content types.

| Prior v0.1 exclusion | Responsible Breadth treatment |
| --- | --- |
| Injury-specific advice | Preserved. The project still must not give individualized injury advice. General consumer education about well-studied conditions is allowed when non-diagnostic, cited, and red-flag routed. |
| Posture-correction protocols | Preserved as a prohibition on corrective protocols. Pattern education pages may explain a pattern and mainstream self-management themes, but must not promise correction or prescribe a corrective routine. |
| Pain treatment | Preserved. Pages may describe common source-backed education and professional-routing guidance, but must not present a treatment plan. |
| Diagnosis | Fully preserved. No page may diagnose the reader or help the reader self-diagnose. |
| Rehabilitation pathways | Fully preserved. Rehab protocols, return-to-sport paths, post-surgical guidance, and condition-specific progression plans remain out of scope. |
| Workout prescription | Preserved for personalized plans. Static program examples are allowed only as educational illustrations. |

### Conflict resolution

If this spec and `specs/markdown-first-primer.md` conflict:

1. For content-type eligibility of Responsible Breadth pages, this spec controls.
2. For the original five-page v0.1 slice, `specs/markdown-first-primer.md`
   controls.
3. For Markdown source-of-truth, citation mechanics, media provenance, privacy,
   mdBook-derived-output behavior, and local validation mechanics,
   `specs/markdown-first-primer.md` continues to apply unless this spec gives a
   stricter rule.
4. For safety, privacy, red-flag routing, source quality, and program-boundary
   rules, the stricter rule controls.
5. No conflict rule may permit diagnosis, personalized treatment, personalized
   programming, acute injury guidance, post-surgical guidance,
   specialized-population guidance, AI-generated source-of-truth content, or
   clinical-authority claims.

## Glossary

- Pattern page: A Markdown page explaining a non-diagnostic posture, alignment,
  or movement pattern such as anterior pelvic tilt or forward head posture.
- Condition page: A Markdown page explaining a common, well-studied condition in
  general consumer-education terms.
- Programming-principle page: A Markdown page explaining a general training
  structure topic such as frequency, sets and reps, progression, or recovery.
- Program-example page: A Markdown page showing a static generic beginner
  program as an educational worked example.
- Red-flags reference: A project-level Markdown page that routes symptoms or
  situations past GymPrimer content to qualified professional or emergency care.
- Source-quality tier: The type of source required for a claim, such as public
  health guidance, clinical guideline, institutional patient education,
  professional organization guidance, or supporting source.
- Static education: General explanation that does not adapt to the reader's
  symptoms, history, goals, body, equipment, or training response.
- `pattern_page`: A Responsible Breadth page class for non-diagnostic education
  about common movement or posture patterns.
- `condition_page`: A Responsible Breadth page class for consumer education
  about well-studied conditions with red-flag routing.
- `programming_principle_page`: A Responsible Breadth page class for general
  training-literacy content.
- `program_example_page`: A Responsible Breadth page class for static worked
  examples showing how principles compose.
- `expanded_exercise_page`: A Responsible Breadth page class for exercise pages
  using Responsible Breadth visual or source standards.

## Expanded page classes

| Page class | Description | Allowed example |
| --- | --- | --- |
| `pattern_page` | Non-diagnostic education about common movement or posture patterns. | anterior pelvic tilt, forward head posture |
| `condition_page` | Consumer education about well-studied conditions with red-flag routing. | non-specific chronic low back pain, plantar fasciitis |
| `programming_principle_page` | General training-literacy content. | sets and reps, training frequency, progression |
| `program_example_page` | Static worked example showing how principles compose. | generic 3-day beginner full-body example |
| `expanded_exercise_page` | Exercise page using Responsible Breadth visual or source standards. | goblet squat with necessary visuals |

The first expanded slice should classify pages by path:

- `patterns/*.md` -> `pattern_page`
- `conditions/*.md` -> `condition_page`
- `principles/*.md` -> `programming_principle_page`
- `programs/*.md` -> `program_example_page`
- `exercises/*.md` -> `expanded_exercise_page`

## Examples first

Example E1: a pattern page remains non-diagnostic
Given `patterns/anterior-pelvic-tilt.md` exists
When a reader opens the page
Then the page explains the pattern in general terms, links to red flags, states
what the page does not do, avoids diagnosis language, and routes individual
assessment to a qualified professional.

Example E2: a condition page routes red flags
Given `conditions/non-specific-chronic-low-back-pain.md` exists
When a reader opens the page
Then the first safety section links to `about/red-flags.md` and makes clear that
urgent or individualized concerns are outside GymPrimer.

Example E3: a program example is static
Given `programs/generic-3-day-full-body-example.md` exists
When a reader opens the page
Then the page explains how principles compose into a week and does not ask for
reader inputs, select personal loads, adapt to pain, or say the reader should
follow that exact plan.

Example E4: citation count is not enough
Given a condition page cites three personal blogs
When source quality is reviewed
Then the page fails the spec because it lacks the required institutional,
clinical-guideline, or patient-education source coverage.

Example E5: necessary visuals pass
Given a machine exercise page needs equipment identification
When the page includes a relative image with alt text and approved provenance
where required
Then the page passes visual necessity review without needing a muscle overlay or
wrong-frame comparison.

Example E6: first expanded proof slice stays narrow
Given the Responsible Breadth expansion begins
When the first proof slice is selected
Then it contains the red-flags page, one pattern page, one condition page, one
programming-principle page, and one program-example page before broader scaling.

Example E7: original five-page slice remains governed by Markdown-first
Given a maintainer changes `02-machines/lat-pulldown.md`
When the change remains part of the original v0.1 slice
Then `specs/markdown-first-primer.md` governs the closeout contract, and
Responsible Breadth does not require the page to become a pattern page,
condition page, or program example.

Example E8: a Responsible Breadth pattern page is allowed
Given `patterns/anterior-pelvic-tilt.md` exists
When it is reviewed for promotion
Then it may be promoted only if it is non-diagnostic, cites required sources,
links to red flags, avoids individualized treatment language, and passes shared
Markdown-first citation, media, and privacy validation.

Example E9: a condition page that becomes treatment fails
Given `conditions/non-specific-chronic-low-back-pain.md` exists
When it tells the reader what treatment plan to follow, gives a rehab
progression, or claims to diagnose the reader
Then the page fails even if it includes citations and a red-flags link.

Example E10: a static program example is allowed
Given `programs/generic-3-day-full-body-example.md` exists
When the page shows a static worked example for general education
Then it may be promoted only if it does not accept symptoms, pain reports,
goals, constraints, or training response and output a personalized program.

## Requirements

R1. Responsible Breadth source content MUST be canonical Markdown readable
directly in the repository.

R2. Responsible Breadth MUST use these top-level content directories for new
published pages: `exercises/`, `patterns/`, `conditions/`, `principles/`,
`programs/`, and `about/`.

R3. The first expanded-scope proof slice MUST include exactly these page
categories before broader scaling: red-flags reference, one pattern page, one
condition page, one programming-principle page, and one program-example page.

R4. The first expanded-scope proof slice SHOULD use these paths unless
architecture review chooses different stable paths: `about/red-flags.md`,
`patterns/anterior-pelvic-tilt.md`,
`conditions/non-specific-chronic-low-back-pain.md`,
`principles/how-many-days-a-week.md`, and
`programs/generic-3-day-full-body-example.md`.

R5. Pattern and condition pages MUST include page-local sections equivalent to:
`What this page is`, `What this page is not`,
`Red flags: when to stop reading and seek care`, `Plain-language overview`,
`What mainstream sources generally agree on`, `What is uncertain or mixed`,
`Commonly recommended self-management themes`, `What to avoid`,
`When to see a professional`, `Sources`, and `Author and review date`.

R6. Pattern and condition pages MUST NOT include sections or framing equivalent
to `Diagnosis`, `Treatment plan`, `Fix this in 30 days`, or `Corrective routine
for you`.

R7. Pattern and condition pages MUST link to the red-flags reference before any
general self-management discussion.

R8. Pattern and condition pages MUST state that the page does not diagnose the
reader or provide individualized treatment.

R9. Condition pages MUST cover only common, well-studied conditions for general
fit adults unless a later accepted proposal expands the population or condition
scope.

R10. Pattern pages MUST frame posture or alignment topics as observable patterns,
not as diagnoses, moral judgments, or guaranteed problems to fix.

R11. Programming-principle pages MUST explain general training concepts using
cited ranges or principles and MUST NOT adapt recommendations to an individual
reader.

R12. Program-example pages MUST be static worked examples for general healthy
beginners.

R13. Program-example pages MUST NOT accept reader input, route readers into a
plan, prescribe personal load, adapt to symptoms, or provide injury-specific
progressions.

R14. Program-example pages MUST include a clear scope note that the example is
not the reader's prescription.

R15. Every Responsible Breadth content page MUST cite at least three named
authoritative sources unless a narrower spec section defines a higher minimum.

R16. Pattern pages MUST include at least two institutional, clinical, or
public-health sources plus one supporting source.

R17. Condition pages MUST include at least two institutional, clinical-guideline,
or patient-education sources plus one supporting source.

R18. Programming-principle pages MUST include public-health guidance plus
resistance-training guidance when the topic concerns training frequency, volume,
intensity, progression, or recovery.

R19. Program-example pages MUST include public-health guidance,
resistance-training guidance, and a cited beginner-program illustration source.

R20. Source checks MUST validate source-index references and page-local source
presence; citation count alone is not sufficient for promotion.

R21. Safety warnings MUST have claim-level citations to public, named sources.

R22. Pages MUST distinguish mainstream agreement from uncertainty or mixed
evidence when sources do not fully agree.

R23. Every Responsible Breadth content page MUST include author, created date,
last reviewed date, next review due date, and review scope metadata.

R24. Safety-relevant pages MUST receive a first review due date no later than 90
days after publication.

R25. Pattern pages MUST use a six-month review cadence for the first year and
MAY move to annual review only after stable review evidence exists.

R26. Condition pages, program-example pages, and the red-flags reference MUST use
a six-month review cadence.

R27. Exercise and programming-principle pages MAY use annual review after the
first 90-day review unless safety concerns or reader confusion trigger earlier
review.

R28. Any source change, safety concern, reader confusion, media provenance
change, or scope-boundary concern MUST trigger review before the affected page is
treated as current.

R29. Visuals MUST be necessary for beginner comprehension, not decorative.

R30. Machine exercise pages SHOULD include equipment setup visuals when text
alone is insufficient for identification or setup.

R31. Movement pages SHOULD include key position or phase visuals when text alone
is insufficient for comprehension.

R32. Muscle overlays, wrong-frame comparisons, and alignment diagrams MUST be
used only when they materially reduce confusion for the page.

R33. Regression visuals MUST be change-based: different equipment requires setup
visuals, different body position requires key-position visuals, different target
emphasis requires updated muscle explanation or overlay, and unchanged movement
patterns may reuse the main explanation.

R34. All media references MUST use relative repository paths and alt text or
nearby explanatory text.

R35. Raster media under `media/` MUST satisfy the existing provenance contract
before a page referencing it is promoted.

R36. Pattern, condition, and program-example PRs MUST receive higher-bar review
than ordinary exercise-page wording edits.

R37. Higher-bar review MUST verify source traceability, red-flag routing,
non-diagnostic language, no individualized treatment, no personalized
programming, and scope-boundary fit.

R38. Responsible Breadth content MUST NOT cover acute injury, post-surgical
care, pediatric training, pregnancy, oncology-related training, mental-health
treatment, sport-specific programming, or specialized populations.

R39. Responsible Breadth content MUST NOT include diagnosis, individualized
medical advice, treatment plans, return-to-training prescriptions, active
rehabilitation protocols, posture-correction promises, or injury-specific
protocols.

R40. Responsible Breadth MUST NOT introduce a symptom-checker UI, diagnostic
decision tree, user account, CMS dependency, runtime API, hosted app dependency,
or AI-generated source-of-truth content.

R41. Expanded-scope content MUST NOT be described as published, promoted, or
current until spec review, architecture review where required, plan review,
test-spec review, implementation review, and final verification are complete for
that slice.

R42. The first expanded-scope proof slice MUST include manual comprehension
proof for each page's purpose, boundaries, stop or red-flag condition, and source
verification.

R43. Pattern and condition comprehension proof MUST confirm the reader can state
that the page does not diagnose them.

R44. Program-example comprehension proof MUST confirm the reader can state that
the example is not a personal prescription.

R45. Validation tooling SHOULD fail promoted Responsible Breadth pages that miss
required page sections, red-flag links, metadata, source-count minimums,
source-index validity, media provenance, or excluded-scope guardrails.

R46. Where semantic source quality or scope-boundary judgment cannot be fully
automated, the change MUST record manual proof before promotion.

R47. The red-flags reference MUST distinguish emergency care, prompt medical
care, and professional assessment in plain language.

R48. The red-flags reference MUST NOT attempt to diagnose the reader or decide
which condition they have.

R49. The sources index MUST include reusable sources used by more than one
Responsible Breadth page.

R50. The root README or active navigation surface MUST NOT link expanded-scope
pages as promoted content until promotion evidence exists.

R51. A Responsible Breadth page MUST be classified into exactly one Responsible
Breadth page class before Responsible Breadth-specific validation applies.

R52. Responsible Breadth page classes SHOULD be path-classified for the first
expanded slice: `patterns/*.md` as `pattern_page`, `conditions/*.md` as
`condition_page`, `principles/*.md` as `programming_principle_page`,
`programs/*.md` as `program_example_page`, and `exercises/*.md` as
`expanded_exercise_page`.

R53. If a page cannot be path-classified into exactly one Responsible Breadth
page class, it MUST declare an equivalent page-local type before promotion.

R54. For Responsible Breadth page classes only, this spec MUST supersede
Markdown-first R21 and R22 content-scope restrictions only to the extent needed
to allow accepted pattern, condition, programming-principle, static
program-example, and expanded-exercise education.

R55. Markdown-first source-of-truth, citation mechanics, media provenance,
privacy, mdBook-derived-output, and local validation requirements MUST continue
to apply to Responsible Breadth pages unless this spec gives a stricter rule.

R56. The original Markdown-first five-page v0.1 slice MUST remain governed by
`specs/markdown-first-primer.md` and MUST NOT be required to adopt Responsible
Breadth page classes or expanded visual standards before v0.1 closeout.

## Inputs and outputs

Inputs:

- Markdown source pages in `exercises/`, `patterns/`, `conditions/`,
  `principles/`, `programs/`, and `about/`.
- `SOURCES.md` entries for reusable sources.
- Media assets under `media/` with provenance where required.
- Manual proof records for source quality, scope boundaries, visuals, and reader
  comprehension.
- Validation commands and reports.

Outputs:

- GitHub-readable Markdown pages.
- Page-local source lists and reusable source-index entries.
- Review metadata on each published page.
- Red-flags reference and professional-routing language.
- Optional derived mdBook output that does not outrank Markdown.
- Validation evidence and manual proof records.

## State and invariants

- Markdown remains the canonical source of truth.
- Responsible Breadth pages are not current until promoted through the reviewed
  workflow.
- Red-flag routing must precede self-management discussion on safety-relevant
  pages.
- Static education must never become personalized diagnosis, treatment, or
  programming.
- Derived HTML, generated outputs, and future websites never outrank Markdown.
- The existing Markdown-first v0.1 spec remains active until explicitly amended
  or superseded.

## Error and boundary behavior

- A page that lacks required red-flag routing fails promotion.
- A page that uses diagnosis, treatment-plan, or personalized-prescription
  language fails promotion.
- A page that meets source count but fails source quality fails promotion.
- A program example that adapts to reader symptoms, goals, equipment, or training
  response fails promotion.
- A media asset without required provenance fails promotion for every page that
  references it.
- A page with missing review metadata is draft-only.
- Broken or redirected sources trigger review before the page remains current.

## Compatibility and migration

The compatibility contract near the top of this spec controls same-rank
interaction with `specs/markdown-first-primer.md`.

Existing numbered first-slice directories remain valid for the current v0.1
proof. New expanded-scope paths become compatibility surfaces only after
architecture approval and promotion.

If a promoted expanded-scope page must be narrowed or removed, the project uses
content rollback: remove the page from active navigation, mark it draft or
withdrawn, and keep correction history in the normal review record.

## Observability

- Review records must show when a page passes higher-bar review.
- Manual proof records must show citation-quality review, scope-boundary review,
  visual-necessity review where media exists, and comprehension outcomes.
- Validation output should identify missing section, missing metadata, missing
  red-flag link, source-index, source-count, media-provenance, and excluded-scope
  failures with stable messages.
- Reports must state exact local commands run and whether CI was observed.

## Security and privacy

- Pages and proof records MUST NOT include secrets, private contact details,
  local machine paths, private health information, real user health profiles, or
  identifying reader-test notes.
- Reader-test evidence MUST be non-identifying.
- Pattern and condition pages MUST NOT ask the reader to disclose symptoms or
  health history.
- Program pages MUST NOT collect or infer personal goals, limitations, injuries,
  or training response.

## Accessibility and UX

- Pages MUST be readable as plain Markdown without JavaScript or generated HTML.
- Pages MUST use plain language suitable for beginners.
- Images MUST have alt text or adjacent explanatory text.
- Safety boundaries MUST be visible before general self-management content on
  safety-relevant pages.
- Page headings MUST make scope and non-scope easy to scan.

## Performance expectations

- Repository checks for Responsible Breadth pages SHOULD run as part of the
  existing local validation flow without requiring network access for normal
  structural validation.
- Link-health checks MAY require network access when selected, but absence of
  link-health tooling must be recorded as a validation gap.

## Edge cases

EC1. A pattern page says a reader "has" anterior pelvic tilt: fails
non-diagnostic framing.

EC2. A condition page lists exercises under "treatment plan": fails page
contract.

EC3. A program page says "follow this program": fails prescription boundary.

EC4. A page links red flags only at the bottom: fails safety-routing order.

EC5. A page cites three sources but none are institutional, clinical,
public-health, or professional guidance: fails source quality.

EC6. A page uses a muscle overlay that introduces anatomy claims absent from the
Markdown: fails source-of-truth boundary until text and citations are updated.

EC7. A reader-test note includes a real health profile: fails privacy review.

EC8. A source link rots after publication: triggers review before the page is
treated as current.

EC9. A condition page targets pregnancy, post-surgical care, or pediatric
training: fails excluded-scope guardrail.

EC10. A generic program includes an injury-specific substitution: fails program
boundary.

## Non-goals

- Personalized symptom checking, diagnosis, or treatment routing.
- Personalized workout plans, generated plans, or adaptive programming.
- Acute injury, post-surgical, pediatric, pregnancy, oncology-related,
  mental-health-treatment, or sport-specific content.
- AI-generated content as source of truth.
- Per-card legal disclaimer scaffolding or reader-visible risk tiers.
- Hosted app, CMS, user accounts, tracking, API, or runtime decision support.
- Broad content production beyond the first expanded-scope proof slice.

## Acceptance criteria

AC1. Spec review approves this spec before architecture, planning, test-spec, or
implementation rely on it.

AC2. Architecture review approves repository layout, content-state boundaries,
media/provenance impact, and validation boundaries before implementation.

AC3. Test-spec maps every requirement to automated or manual proof before
implementation.

AC4. The first expanded-scope proof slice contains the required five page
categories and no broader scaled content.

AC5. Automated checks or manual proof verify required sections, metadata,
red-flag links, source counts, source-index validity, excluded-scope guardrails,
and media provenance.

AC6. Manual proof verifies source quality and semantic support for safety,
condition, pattern, programming, and program-example claims.

AC7. Manual proof verifies that pattern and condition pages are non-diagnostic.

AC8. Manual proof verifies that program examples are static illustrations rather
than prescriptions.

AC9. Reader comprehension evidence exists for every page in the first expanded
proof slice.

AC10. README or active navigation does not promote expanded-scope pages until
the slice passes review and verification.

AC-COMP-1. The spec states that `specs/markdown-first-primer.md` remains
governing for the original five-page v0.1 slice.

AC-COMP-2. The spec states that Responsible Breadth governs only accepted
expanded page classes.

AC-COMP-3. The spec states that Responsible Breadth supersedes Markdown-first
R21/R22 content-scope restrictions only for Responsible Breadth page classes.

AC-COMP-4. The spec states that shared Markdown source-of-truth, citation,
media, privacy, validation, and mdBook-derived-output rules continue to apply.

AC-COMP-5. The spec includes a conflict-resolution order for same-rank
requirements.

AC-COMP-6. The spec preserves prohibitions on diagnosis, personalized
treatment, personalized programming, rehab protocols, acute injury guidance,
post-surgical guidance, specialized-population guidance, AI-generated
source-of-truth content, and clinical-authority claims.

AC-COMP-7. `specs/markdown-first-primer.md` contains a compatibility note
pointing to `specs/responsible-breadth.md` for expanded page classes.

AC-COMP-8. Test-spec can map original v0.1 pages and Responsible Breadth pages
to different governing requirement sets without guessing.

AC-COMP-9. A pattern page is allowed only if it satisfies Responsible Breadth
page-contract requirements and shared Markdown-first rules.

AC-COMP-10. A page that gives diagnosis, treatment, rehab progression, or
personalized programming fails even if it is placed under a Responsible Breadth
path.

## Open questions

None for spec review. Architecture and test-spec still need to choose exact
validation mechanics, file-state markers, and proof artifact paths.

## Next artifacts

1. Spec review for `specs/responsible-breadth.md`.
2. ADR and architecture updates for Responsible Breadth layout, source-of-truth,
   media, and validation boundaries.
3. Test-spec update mapping Responsible Breadth requirements to automated and
   manual proof.
4. Execution plan for the first expanded-scope proof slice.

## Follow-on artifacts

None yet

## Readiness

Ready for spec-review R2 as a draft contract. Not ready for architecture,
planning, test-spec, implementation, or content publication until spec review is
recorded and any findings are resolved.
