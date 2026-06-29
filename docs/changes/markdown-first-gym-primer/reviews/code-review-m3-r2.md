# Code Review M3 R2: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed:
  - `docs/changes/markdown-first-gym-primer/reviews/code-review-m3-r2.md`
  - `docs/changes/markdown-first-gym-primer/review-log.md`
  - `docs/changes/markdown-first-gym-primer/review-resolution.md`
  - `docs/plans/2026-06-27-markdown-first-gym-primer.md`
  - `docs/plan.md`
  - `docs/workflows.md`
  - `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M3-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m3-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Reviewed milestone: M3. Five-Page First Slice and Beginner Read-Test Evidence
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3, M4
- Required review-resolution: yes
- Finding IDs: CR-M3-1
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M3 first-slice Markdown pages, first-slice media
  references and provenance rows, manual proof records MP1/MP2/MP3/MP7, README
  navigation, and workflow handoff metadata.
- Tracked governing branch state: working tree on
  `proposal/markdown-first-gym-primer`; artifacts are uncommitted, so this
  review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md` R1-R25, R29-R30,
  R36-R40, R41-R53; `specs/markdown-first-primer.test.md` T8-T10, T14/T15,
  MP1-MP3, MP6; and
  `docs/plans/2026-06-27-markdown-first-gym-primer.md` M3.
- Validation evidence rerun during review:
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md 01-getting-started 02-machines 03-bodyweight media docs/changes/markdown-first-gym-primer/manual-proof`
  - `if rg -n "barbell|deadlift|bench press|Olympic|kettlebell|plyometric|sprint|diagnos|rehab|treat pain|posture correction" 01-getting-started 02-machines 03-bodyweight; then exit 1; else printf "no excluded-scope terms found\n"; fi`
  - Visual inspection of the five AI-generated raster examples under
    `media/equipment/` and `media/movements/`.

## Diff summary

M3 now contains the five first-slice Markdown pages, README navigation to those
pages, page-local sources, conservative beginner scope, five-use-case additions
for the machine pages, AI-generated raster examples with centralized
`media/PROVENANCE.md` rows, and manual proof records. M3A media validation is
closed, and the current M3 validation commands pass.

The MP3 proof record was updated after a non-identifying beginner reader
reviewed `01-*`, `02-*`, and `03-*`, reported that the documents were not easy
enough to understand, and approved the implementation after example pictures
were added.

## Findings

### Finding CR-M3-1

- Finding ID: CR-M3-1
- Severity: major
- Location:
  `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md:39`
- Evidence: `specs/markdown-first-primer.md:176` requires at least one
  beginner read test before promotion, and `specs/markdown-first-primer.md:178`
  requires the read-test evidence to record whether the reader could explain
  each exercise page's purpose, setup, steps, and stop condition after reading.
  The test spec repeats this MP3 pass condition at
  `specs/markdown-first-primer.test.md:97`. The current MP3 record says the
  beginner reader reviewed the document groups, found them not easy enough to
  understand, and approved the implementation after pictures were added, but it
  does not record per-page or per-exercise outcomes for purpose, setup, steps,
  or stop condition.
- Required outcome: MP3 must record non-identifying beginner-read evidence that
  explicitly states whether the reader could explain the required comprehension
  fields for each first-slice exercise page, and the principle-page equivalents
  already listed in the MP3 procedure, before M3 can close.
- Safe resolution path: Update
  `docs/changes/markdown-first-gym-primer/manual-proof/MP3-beginner-read-test.md`
  with a compact non-identifying table for each first-slice page. For exercise
  pages, record purpose, setup or body position, movement steps, stop condition,
  and source-verification outcome as pass/fail or clear short notes. For the
  principle page, record the listed principle-page questions. Do not add reader
  names, contact details, health history, or private training data. Rerun the
  M3 validation commands and request code-review M3 R3.
- needs-decision rationale: none

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | block | R39 requires the MP3 evidence to record whether the beginner could explain purpose, setup, steps, and stop condition. MP3 currently records approval after readability revisions, but not those required outcomes. |
| Test coverage | concern | The 44-test Markdown-first suite passes, but T10/MP3 is manual-only and the manual record is incomplete for R39. |
| Edge cases | concern | Reader confusion was found and addressed with images, but the final comprehension outcome for each required field was not recorded. |
| Error handling | pass | The workflow now routes to review-resolution instead of closing M3 with incomplete manual proof. |
| Architecture boundaries | pass | The pages remain Markdown-first, use no hosted app/generated JSON/CMS behavior, and keep mdBook out of M3. |
| Compatibility | pass | README still labels the pages as draft/not yet promoted, preserving the promotion boundary while M3 is unresolved. |
| Security/privacy | pass | The privacy scan passed over first-slice pages, media, and manual proof records; MP3 does not include identifying reader data. |
| Derived artifact currency | pass | No derived HTML or CI result is claimed. M4 remains open for mdBook build-or-deferral. |
| Unrelated changes | concern | The working tree contains broad prior milestone artifacts, so this review is milestone-local and does not claim branch-wide cleanliness. |
| Validation evidence | pass | Tests, Markdown-first checker, privacy scan, excluded-scope scan, and visual image inspection were rerun during review. The finding is a manual-proof content gap, not an automated validation failure. |

## Residual risks

- The generated images were visually inspected and appear generic, non-branded,
  and within allowed scope, but final media acceptance still depends on
  resolving the MP3 evidence gap and downstream review.
- M4 remains unimplemented, so this review does not claim final closeout,
  verification, branch readiness, PR readiness, CI success, or mdBook currency.

## Milestone handoff state

- Reviewed milestone: M3
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M3, M4
- Next stage: review-resolution for CR-M3-1
- Final closeout readiness: not-ready; M3 has an open material finding and M4
  remains unimplemented.
