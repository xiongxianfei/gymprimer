# Code Review M4 R2: Necessary Images and Baduanjin Exercise

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r2.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: final closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r2.md`
- Review log: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-log.md`
- Review resolution: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`
- Reviewed milestone: M4
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `5608911` (`Resolve M4 rollback proof review finding`).
- Tracked governing branch state: `proposal/baduanjin-exercise-images` at `5608911`.
- Governing artifacts: `specs/necessary-images-and-baduanjin-exercise.md`, `specs/necessary-images-and-baduanjin-exercise.test.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`.
- Prior finding: `CR-M4-001` from `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/reviews/code-review-m4-r1.md`.
- Review-resolution evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`.
- Validation evidence: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md` plus reviewer reruns listed below.
- Relevant implementation files: `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/rollback-proof.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/validation-notes.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/review-resolution.md`, `docs/plans/2026-07-06-necessary-images-and-baduanjin-exercise.md`, `docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/change.yaml`, `docs/plan.md`.

## Diff Summary

The resolution replaces the invalid wildcard rollback evidence with a concrete temporary root, `/tmp/gymprimer-baduanjin-rollback.cr-m4-001`.
`rollback-proof.md` now records setup commands that rebuild the text-only temporary page, remove Baduanjin provenance rows, omit unused image and prompt directories, and run focused Markdown-first and privacy checks from that temporary root.
Validation notes, review-resolution evidence, the active plan, change metadata, and the plan index were updated to route M4 back to code-review rereview.

## Findings

No blocking or required-change findings.

## Prior Finding Reconciliation

| Finding | Rereview disposition | Evidence |
|---|---|---|
| CR-M4-001 | resolved | The proof and validation records now use concrete temporary-root commands, and reviewer reruns of the recorded setup plus Markdown-first and privacy checks passed. |

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | pass | R42/MP4 requires a text-only rollback path after image references, unused assets, provenance rows, and prompt records are removed. The revised proof creates a temporary text-only page, removes Baduanjin provenance rows, omits Baduanjin asset and prompt directories, and validates the temporary state. |
| Test coverage | pass | The existing M4 proof-record tests still pass and require the rollback proof to name the text-only cleanup surfaces, asset paths, prompt-record paths, validation commands, and pass result. |
| Edge cases | pass | E4/MP4 is directly exercised by the concrete temporary-root rollback rehearsal. The reviewer reran the recorded setup and focused checks successfully. |
| Error handling | pass | The proof remains non-destructive to the working tree and documents the cleanup contract if a Baduanjin image fails later review. |
| Architecture boundaries | pass | The change is static Markdown and lifecycle evidence only. It introduces no hosted app, CMS, database, user-input flow, video path, or generated guidance source-of-truth behavior. |
| Compatibility | pass | The recorded commands use ordinary shell variable expansion instead of wildcard environment assignment and are reproducible from the repository root. |
| Security/privacy | pass | Reviewer privacy rerun passed on the temporary rollback root, and the changed proof records do not add private reader, health, contact, location, or training-log data. |
| Derived artifact currency | pass | Rollback proof, validation notes, review-resolution, active plan, change metadata, and plan index now agree that CR-M4-001 is implemented and M4 is ready for rereview. |
| Unrelated changes | pass | The diff is limited to CR-M4-001 evidence correction and lifecycle state updates. |
| Validation evidence | pass | Reviewer reruns passed for the recorded temporary rollback Markdown-first check, temporary rollback privacy check, M4 proof-record tests, and `git diff --check HEAD^ HEAD`. |

## No-Finding Rationale

The previous finding was about reproducibility of the rollback command evidence, not the Baduanjin page content or generated media.
The resolution records a concrete temporary-root setup and the reviewer reran that exact setup and both focused checks successfully.
The updated lifecycle artifacts consistently move CR-M4-001 out of open-findings state and return M4 to review before this review closes it.

## Residual Risks

- The beginner-comprehension proof remains a non-identifying reviewer simulation, not live public-reader research.
- Final lifecycle closeout remains, including final holistic code-review if required by the active workflow, explain-change, final verification, and PR handoff.
- This review does not claim final verification, CI success, branch readiness, or PR readiness.

## Reviewer Validation

- `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; if [ -e "$tmp" ]; then rm -rf "$tmp"; fi; mkdir -p "$tmp/exercises" "$tmp/media"; awk 'NR < 22 || NR > 32' exercises/baduanjin-basics.md > "$tmp/exercises/baduanjin-basics.md"; awk '!/media\/exercises\/baduanjin-basics\//' media/PROVENANCE.md > "$tmp/media/PROVENANCE.md"; cp SOURCES.md RED-FLAGS.md "$tmp"/; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_markdown_first.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` passed: checked 4 Markdown files.
- `tmp=/tmp/gymprimer-baduanjin-rollback.cr-m4-001; GYMPRIMER_ROOT="$tmp" python3 tools/checks/check_privacy.py "$tmp/exercises/baduanjin-basics.md" "$tmp/media/PROVENANCE.md" "$tmp/SOURCES.md" "$tmp/RED-FLAGS.md"` passed: checked 4 files.
- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_baduanjin_m4_rollback_proof_records_text_only_cleanup` passed: 2 tests.
- `git diff --check HEAD^ HEAD` passed.

## Milestone Handoff State

- Reviewed milestone: M4
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: none
- Next stage: final closeout
- Final closeout readiness: ready to start final closeout sequence because M1-M4 are closed and no review-resolution remains open; final verification and PR handoff have not happened.

## Sources

- [Necessary Images and Baduanjin Exercise spec](../../../specs/necessary-images-and-baduanjin-exercise.md)
- [Necessary Images and Baduanjin Exercise test spec](../../../specs/necessary-images-and-baduanjin-exercise.test.md)
- [Necessary Images and Baduanjin Exercise plan](../../plans/2026-07-06-necessary-images-and-baduanjin-exercise.md)
- [Code Review M4 R1](code-review-m4-r1.md)
- [Review Resolution](../review-resolution.md)
