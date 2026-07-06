# Code Review M3 R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m3-r1.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`; `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`; `docs/plan.md`
- Open blockers: none
- Next stage: explain-change
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M3
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Review surface: committed branch diff at `5a40dcf M3: record walking guidance proof`.
- Tracked governing branch state: accepted proposal, approved walking spec, active test spec, reviewed plan, M1 and M2 code-review closeout, walking pages, manual proof records, validation ledger, and tests are present in tracked branch state.
- Active plan: `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Approved spec: `specs/brisk-walking-and-everyday-walking.md`.
- Active test spec: `specs/brisk-walking-and-everyday-walking.test.md`.
- Implementation files inspected: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/source-audit.md`, `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/beginner-comprehension.md`, `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/optional-image-decision.md`, `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/validation-ledger.md`, `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md`, and `tests/test_markdown_first_real_pages.py`.
- Validation evidence: M3 validation ledger plus review-time reruns listed below.

## Diff Summary

M3 records the manual proof and promotion-gate evidence required after the walking pages were drafted:

- `manual-proof/source-audit.md` samples semantic support for intensity, talk test, weekly activity guidance, less-sitting framing, technique, starter/progression, and stop-rule claims.
- `manual-proof/beginner-comprehension.md` records non-identifying outcomes for the approved walking comprehension prompts.
- `manual-proof/optional-image-decision.md` keeps the first walking slice text-only and records the future gate if an image is later justified.
- `tests/test_markdown_first_real_pages.py` adds checks that the M3 manual proof files and validation-ledger commands exist and cover the required surfaces.
- `docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md` adds the new text-only `exercises/brisk-walking.md` page to the existing exercise-image audit inventory.
- Lifecycle artifacts record M3 validation and mark M3 ready for code-review.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M3 records BWG-R23 source-support samples, BWG-R30 comprehension proof, and BWG-R24-R26 text-only media disposition without changing the approved Option C page paths or `basic_cardio_activity`. |
| Test coverage | pass | Focused real-page tests assert the manual proof files, required claim categories, approved comprehension prompts, optional image decision, and M3 validation-ledger commands. |
| Edge cases | pass | The source audit and comprehension proof cover EC1, EC2, EC4, EC5, and EC8 surfaces; the text-only image decision avoids EC7 media risk. |
| Error handling | pass | M3 does not add runtime behavior; validation failures would surface through the focused checker, unittest suites, and privacy scan. |
| Architecture boundaries | pass | Markdown remains the source of truth; no tracker, calculator, generated image, provenance row, prompt record, or adaptive flow was introduced. |
| Compatibility | pass | The exercise-image audit inventory was updated to include the newly added text-only exercise page, keeping existing image-standard coverage current. |
| Security/privacy | pass | Beginner proof uses non-identifying prompt outcomes and the privacy scan passed over media and the change record. |
| Derived artifact currency | pass | No generated media was added, and `media/PROVENANCE.md` remains unaffected by the text-only decision. |
| Unrelated changes | pass | The only cross-change edit is the existing exercise-image audit inventory update required by current image-standard tests for all exercise pages. |
| Validation evidence | pass | Review-time validation reruns passed locally; CI was not observed and is not claimed. |

## No-Finding Rationale

The manual proof records are concrete enough for the approved M3 gate. The source audit ties each required claim class to page-local source IDs and records residual risk. The comprehension proof is prompt-specific and non-identifying, not generic reader approval. The optional image decision records why no first-slice image is needed and preserves the exercise-image standard for any later generated raster asset.

The tests added in M3 verify the existence and minimum content of the proof records without pretending that automated checks can prove semantic source adequacy or reader comprehension. That matches the test spec's split between deterministic checks and manual proof.

## Review-Time Validation

| Command | Result |
| --- | --- |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass; checked 5 Markdown files |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass; 62 tests |
| `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass; 69 tests |
| `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass; checked 62 files |

## Residual Risks

- Manual proof is still evidence for this repository change, not a substitute for future public-reader feedback after publication.
- Source URLs and public-health wording can change over time; semantic source support should be rechecked if walking wording changes before publication.
- CI was not observed.
- This review closes M3 only; it does not claim branch readiness, PR readiness, final verification, or CI success.

## Milestone Handoff

M3 is closed.

All implementation milestones are closed. The next stage is final closeout starting with explain-change, followed by final verification and PR handoff.
