# Code Review M4 R1: Safer Running Basics and High-Quality Running Images

Review date: 2026-07-07

Reviewed milestone: M4 Comprehension Proof and Final Readiness

Review target: `ee4fb66 M4: record safer running comprehension proof`

Review status: changes-requested

## Review Inputs

- Diff/review surface: `git show ee4fb66 -- tests/test_markdown_first_real_pages.py docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/beginner-comprehension-proof.md docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md docs/changes/2026-07-06-safer-running-basics-and-running-images/validation-ledger.md docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/changes/2026-07-06-safer-running-basics-and-running-images/change.yaml docs/plan.md docs/changes/2026-07-06-safer-running-basics-and-running-images/explain-change.md`
- Governing spec: `specs/safer-running-basics-and-running-images.md`
- Test spec: `specs/safer-running-basics-and-running-images.test.md`
- Plan: `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- Validation evidence reviewed: plan M4 validation notes and reviewer reruns listed below.

## Diff Summary

M4 adds focused proof tests, beginner-comprehension proof, text-only rollback proof, a validation ledger, and workflow-state updates for code-review handoff.

The beginner-comprehension proof covers the R12.3 prompts, uses a non-identifying reviewer simulation, and references the safer-running page and all six images.

The validation ledger records exact local commands and explicitly says CI was not observed.

## Findings

### Finding GP-SRB-M4-CR1

- Finding ID: GP-SRB-M4-CR1
- Severity: major
- Location: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md:47`, `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/rollback-proof.md:51`, `tests/test_markdown_first_real_pages.py:815`, temporary rollback page line 25
- Evidence: MP4 requires proof that image rollback leaves the page useful as a text-backed primer. The rollback proof command removes only Markdown image-reference lines. Replaying that command leaves this stale sentence in the temporary text-only page: `Use these images as broad visual references. The Markdown instructions below`. The focused M4 rollback test checks that the proof record exists and names cleanup surfaces, but it does not assert that the temporary text-only page removes this image-only prose.
- Required outcome: The rollback proof and its test must demonstrate a text-only temporary page without image-only instruction prose or image references.
- Safe resolution path: Update the rollback rehearsal to remove the `Use these images as broad visual references` paragraph along with image references, record the updated temporary-root commands and passing results, and add a regression assertion that the rollback proof covers removal of stale image-reference prose or otherwise proves it is absent from the temporary text-only page.
- needs-decision rationale: none

Detailed finding record: `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M4-CR1.md`

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | R12.3 beginner proof and R12.4 command reporting are covered; MP4 rollback proof is incomplete because the rehearsed text-only page retains image-only prose. |
| Test coverage | concern | New M4 tests cover proof-file presence and required tokens, but they do not prove the temporary rollback page is free of stale image-reference prose. |
| Edge cases | concern | The named text-only rollback edge case is only partially exercised; direct replay shows stale image-only prose remains after cleanup. |
| Error handling | pass | No runtime error handling changed; rollback is a documented temporary-root rehearsal. |
| Architecture boundaries | pass | The change stays within Markdown proof records, tests, and workflow artifacts. |
| Compatibility | pass | No public path, media path, source ID, app, schema, or runtime contract changes were introduced in M4. |
| Security/privacy | pass | The comprehension proof records no private reader, contact, route, pace, health, or training-log data, and the privacy scan passed. |
| Derived artifact currency | concern | Plan, metadata, and ledger are synchronized to the current proof, but the rollback proof content overstates the text-only cleanup result. |
| Unrelated changes | pass | The diff is scoped to M4 proof, validation evidence, tests, and lifecycle state. |
| Validation evidence | concern | Reviewer reruns passed, but a direct replay of the rollback command showed an uncovered proof gap. |

## Validation Rerun

Reviewer reran:

```bash
python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_rollback_proof_records_text_only_cleanup tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_safer_running_m4_validation_ledger_records_final_handoff_commands
python3 -m unittest tests.test_exercise_method_guidance
python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages
python3 tools/checks/check_markdown_first.py exercises/safer-running-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 tools/checks/check_privacy.py exercises/safer-running-basics.md media/PROVENANCE.md media/prompts/exercises/safer-running-basics/ docs/changes/2026-07-06-safer-running-basics-and-running-images docs/plans/2026-07-06-safer-running-basics-and-running-images.md docs/plan.md
python3 -m unittest discover -s tests
git diff --check
```

All commands passed locally during review.

Reviewer also replayed the rollback proof commands in `/tmp/gymprimer-safer-running-rollback.m4-review` and searched the temporary page for image-reference prose. The replayed temporary page still contained `Use these images as broad visual references.`

## Residual Risks

If this advances without resolution, a rollback could remove images while leaving text that tells readers to use images that are no longer present.

## Milestone Handoff

M4 should move to `resolution-needed`.

Required next stage is review-resolution for GP-SRB-M4-CR1.

This review does not claim branch readiness, PR readiness, final verification, or CI success.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `specs/safer-running-basics-and-running-images.test.md`
- `docs/plans/2026-07-06-safer-running-basics-and-running-images.md`
- `docs/changes/2026-07-06-safer-running-basics-and-running-images/reviews/findings/GP-SRB-M4-CR1.md`
