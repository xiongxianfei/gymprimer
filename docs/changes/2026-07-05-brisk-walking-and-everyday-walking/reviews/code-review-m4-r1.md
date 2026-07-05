# Code Review M4 R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m4-r1.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`; `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`; `docs/plan.md`
- Open blockers: none
- Next stage: final closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M4
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Review surface: committed branch diff at `ebb3791 M4: add required brisk walking images`.
- Tracked governing branch state: amended accepted proposal, approved amended walking spec, active amended test spec, approved architecture amendment, reviewed M4 plan, test-spec-review R2, M1-M3 code-review closeout, and M4 implementation commit are present in tracked branch state.
- Active plan: `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Approved spec: `specs/brisk-walking-and-everyday-walking.md`.
- Active test spec: `specs/brisk-walking-and-everyday-walking.test.md`.
- Implementation files inspected: `exercises/brisk-walking.md`, `principles/everyday-walking.md`, `media/exercises/brisk-walking/movement.png`, `media/exercises/brisk-walking/muscle-attention.png`, `media/prompts/exercises/brisk-walking/movement.md`, `media/prompts/exercises/brisk-walking/muscle-attention.md`, `media/PROVENANCE.md`, `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/required-image-decision.md`, `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/manual-proof/visual-safety.md`, and `tests/test_markdown_first_real_pages.py`.
- Validation evidence: M4 validation ledger plus review-time reruns listed below.

## Diff Summary

M4 implements the amended required-image contract for the brisk-walking exercise page:

- `exercises/brisk-walking.md` now includes exactly two local support images and keeps Markdown instructions as the source of truth.
- `media/exercises/brisk-walking/movement.png` provides the required movement/form reference.
- `media/exercises/brisk-walking/muscle-attention.png` provides the required broad muscle-attention reference.
- Prompt records under `media/prompts/exercises/brisk-walking/` preserve the exact prompts and asset paths.
- `media/PROVENANCE.md` records approved generated-raster rows with the expected purposes, prompt records, page refs, and creation notes.
- M4 manual proof records the required-image decision and visual-safety review.
- Real-page tests now assert the required image references, prompt/provenance wiring, visual-safety proof, and no image on `principles/everyday-walking.md`.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | BWG-R24-R26 are satisfied: exactly one movement image and one muscle-attention image appear on `exercises/brisk-walking.md`, and `principles/everyday-walking.md` remains text-only. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py` covers image count, local paths, alt text, approved provenance, prompt records, page refs, visual-safety proof, and the no-everyday-image boundary. |
| Edge cases | pass | The proof and tests cover missing image, wrong purpose, missing prompt/provenance wiring, unsafe image framing, and accidental principle-page media. |
| Error handling | pass | M4 adds static Markdown/media only; failures surface through the image-standard tests, real-page tests, Markdown-first checker, and privacy scan. |
| Architecture boundaries | pass | Images remain subordinate to Markdown and do not introduce a tracker, calculator, adaptive flow, diagnosis, treatment path, or generated guidance as source of truth. |
| Compatibility | pass | Existing exercise-image standard expectations are reused; no broad media-schema or checker rewrite was introduced. |
| Security/privacy | pass | The assets are faceless generated raster images; prompt/provenance records do not include private data, and privacy validation passed during implementation. |
| Derived artifact currency | pass | Prompt records, provenance rows, page refs, manual proof, validation ledger, and lifecycle routing were updated for the accepted assets. |
| Unrelated changes | pass | Review found no implementation drift outside the amended walking media scope. |
| Validation evidence | pass | Review-time validation reruns passed locally; CI was not observed and is not claimed. |

## No-Finding Rationale

The page-level image placement matches the amended product decision: the brisk-walking exercise document gets both necessary high-quality support images, while everyday walking remains text-only. The movement image shows a faceless adult walking outdoors with upright posture, forward gaze, relaxed shoulders, natural arm swing, relaxed hands, and a walking stride. It does not show race-walking, running, a treadmill, hiking, a wearable tracker, wrong/correct comparison, labels, or clinical framing.

The muscle-attention image uses broad blue regions for the approved walking body areas: glutes, thighs, calves, trunk, shoulders or upper back, and feet or ankles. It avoids in-image labels, red pain marks, exposed musculature, clinical diagnosis or treatment framing, and exact activation claims. The accompanying Markdown explicitly says the images are broad visual references and that the written instructions remain the source of truth.

The added tests are appropriately deterministic: they verify the traceable media contract and required proof files without claiming automated review can fully prove visual quality. The manual visual-safety record supplies that evidence for this slice.

## Review-Time Validation

| Command | Result |
| --- | --- |
| `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | pass; 36 tests |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass; checked 5 Markdown files |
| `git diff --check` | pass |

## Residual Risks

- Generated images remain approximate educational illustrations and should be replaced if later beginner review finds they confuse technique or muscle attention.
- CI was not observed.
- This review closes M4 only; it does not claim branch readiness, PR readiness, final verification, or CI success.

## Milestone Handoff

M4 is closed.

All implementation milestones are closed. The next stage is final closeout, starting with explain-change and then final verification and PR handoff.
