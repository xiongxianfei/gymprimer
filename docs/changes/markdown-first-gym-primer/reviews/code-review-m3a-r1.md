# Code Review M3A R1: Markdown-First Gym Primer

## Result

- Skill: code-review
- Status: completed
- Artifacts changed:
  - `docs/changes/markdown-first-gym-primer/reviews/code-review-m3a-r1.md`
  - `docs/changes/markdown-first-gym-primer/review-log.md`
  - `docs/plans/2026-06-27-markdown-first-gym-primer.md`
  - `docs/plan.md`
  - `docs/workflows.md`
  - `docs/changes/markdown-first-gym-primer/change.yaml`
- Open blockers: MP3 beginner read-test evidence is still missing for M3 closeout
- Next stage: blocked pending MP3 beginner read-test evidence for M3 closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/code-review-m3a-r1.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M3A. AI Raster Media Provenance Validation and Optional Page Images
- Milestone closeout: closed
- Remaining implementation milestones: M3 closeout, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: M3A implementation in `tools/checks/check_markdown_first.py`,
  `tools/checks/check_privacy.py`, `tests/test_markdown_first_guardrails.py`,
  `media/PROVENANCE.md`, `media/equipment/`, `media/movements/`,
  `docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md`,
  and M3A workflow metadata.
- Tracked governing branch state: working tree on
  `proposal/markdown-first-gym-primer`; artifacts are uncommitted, so this
  review is milestone-local and does not claim branch readiness.
- Governing artifacts: `specs/markdown-first-primer.md` R41-R53 and AC15-AC19,
  `specs/markdown-first-primer.test.md` T14/T15 and CMD10-CMD12,
  `docs/architecture/system/architecture.md`, `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`,
  and `docs/plans/2026-06-27-markdown-first-gym-primer.md` M3A.
- Validation evidence rerun during review:
  - `python3 -m unittest tests.test_markdown_first_guardrails`
  - `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'`
  - `python3 tools/checks/check_markdown_first.py README.md SOURCES.md 01-getting-started 02-machines 03-bodyweight`
  - `python3 tools/checks/check_privacy.py -- README.md SOURCES.md CONTRIBUTING.md CONTENT_LICENSE.md media docs/changes/markdown-first-gym-primer`
  - `markdownlint --disable MD013 -- media/PROVENANCE.md docs/changes/markdown-first-gym-primer/manual-proof/MP6-ai-raster-media-review.md docs/changes/markdown-first-gym-primer/explain-change.md docs/plans/2026-06-27-markdown-first-gym-primer.md docs/plan.md docs/workflows.md specs/markdown-first-primer.test.md`
  - `git diff --check`
  - A direct temporary duplicate-provenance check that exited nonzero with
    `media_provenance_incomplete`.

## Diff summary

M3A extends the Markdown-first checker with deterministic media classification
before provenance lookup. The checker now treats `.svg` files under `media/` as
original educational diagrams and treats `.png`, `.jpg`, `.jpeg`, and `.webp`
under `media/` as AI-generated raster illustrations that require one approved
matching `media/PROVENANCE.md` row. It rejects remote images, media outside
`media/`, unsupported extensions, missing media assets, missing provenance,
incomplete provenance, non-approved provenance, out-of-scope media purpose, and
`page_refs` mismatches with stable codes.

The implementation adds an empty centralized `media/PROVENANCE.md` table,
tracked first-slice media directories, M3A media guardrail tests, and MP6
manual proof stating that no AI-generated raster assets were added or referenced
by promoted pages in M3A.

The privacy checker was narrowed to avoid a false positive on policy wording
about private paths while preserving concrete private-path, secret, and PHI
detection.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | `tools/checks/check_markdown_first.py` implements R41-R53 behavior: exact `asset_path` matching, `asset_type = ai_generated_raster`, allowed `media_purpose`, `review_status = approved`, required fields, and `page_refs` validation. `media/PROVENANCE.md` exists with the approved table schema. |
| Test coverage | pass | `tests/test_markdown_first_guardrails.py` covers text-only pages, SVG without provenance, raster extensions requiring provenance, approved provenance, incomplete provenance, non-approved provenance, out-of-scope purpose, page-ref mismatch, remote images, outside-media paths, unsupported extensions, and missing assets. |
| Edge cases | pass | T14/EC6-EC10 have direct automated proof. Review also ran a duplicate-row check that failed with `media_provenance_incomplete`, covering the "one matching row" property. |
| Error handling | pass | Missing content paths remain setup errors; media validation findings return exit `1`; missing `SOURCES.md` remains a setup error. Unsupported or unsafe media inputs fail closed. |
| Architecture boundaries | pass | The checker classifies by path and extension before provenance lookup, as required by the media ADR. It does not allow third-party raster photos, screenshots, external URLs, hosted app behavior, generated JSON, or mdBook scope. |
| Compatibility | pass | Text-only pages remain valid, SVG pages remain possible without AI-raster provenance, and first-slice pages still pass the updated checker. |
| Security/privacy | pass | The privacy scan passes over media and change-local proof records; the narrowed pattern still catches concrete home-directory paths, credential-like assignments, PHI assignments, and profile-style health text. |
| Derived artifact currency | pass | No generated media or derived HTML is claimed current. MP6 explicitly records that no raster images were added in M3A. |
| Unrelated changes | concern | The working tree still contains broad uncommitted artifacts from previous workflow stages. This review is limited to M3A and does not claim branch-wide cleanliness. |
| Validation evidence | pass | Required M3A commands, scoped markdownlint, `git diff --check`, and the additional duplicate-provenance check passed during review. |

## No-finding rationale

The implementation satisfies the approved strict v0.1 media contract. Raster
classification is deterministic before provenance lookup, missing or invalid
provenance fails closed, valid text-only and SVG-only pages remain valid, and
manual proof records the no-raster M3A state. The required M3A validation
commands and direct edge-case checks passed during review.

## Residual risks

- The Markdown image parser is intentionally lightweight. It covers the
  current v0.1 image syntax used by the project, but not the full Markdown
  grammar.
- The provenance table parser is deterministic but simple; future richer media
  workflows may require a structured metadata format.
- M3A closes only the media validation milestone. M3 promotion remains blocked
  pending MP3 beginner read-test evidence, and M4 remains unimplemented.
- This review does not claim CI, verification, branch readiness, PR readiness,
  or final readiness.

## Milestone handoff state

- Reviewed milestone: M3A
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M3 closeout, M4
- Next stage: blocked pending MP3 beginner read-test evidence for M3 closeout
- Final closeout readiness: not-ready; M3 closeout and M4 remain open.
