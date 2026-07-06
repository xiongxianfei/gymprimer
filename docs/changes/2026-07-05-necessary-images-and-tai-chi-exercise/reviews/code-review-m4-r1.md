# Code Review M4 R1: Necessary Images and Tai Chi Exercise

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/code-review-m4-r1.md`, `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`, `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`, `docs/plan.md`, `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/change.yaml`
- Open blockers: none
- Next stage: final closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M4
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `4644afb` (`M4: record Tai Chi image review evidence`).
- Tracked governing branch state: accepted proposal, approved spec, approved architecture, reviewed plan, active test spec, M1-M3 code-review receipts, and M4 implementation commit are tracked on `proposal/necessary-images-and-tai-chi-exercise`.
- Governing artifacts: `specs/necessary-images-and-tai-chi-exercise.md`, `specs/necessary-images-and-tai-chi-exercise.test.md`, `docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md`, and `CONSTITUTION.md`.
- Validation evidence: M4 validation notes, M4 commit message validation evidence, reviewer reruns of focused M4 proof tests, Markdown-first check, privacy check, method-guidance test, focused suites, unittest discovery, diff check, and a temporary rollback rehearsal.

## Diff Summary

M4 adds `beginner-comprehension-proof.md`, `rollback-proof.md`, and `validation-notes.md`.
The proof files record MP3 beginner comprehension prompts, MP4 text-only rollback steps, non-identifying/privacy boundaries, residual risk, and local validation evidence.

The implementation adds real-page tests that require M4 proof files to name the required prompts, image paths, rollback cleanup surfaces, and validation commands.
Workflow metadata now moves the active handoff to code-review M4 before this review closes the milestone.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | pass | M4 satisfies R40-R43: MP2 visual review exists, MP3 records beginner comprehension prompts and residual confusion, MP4 preserves text-only rollback, and no hosted app, CMS, database, user flow, video-first path, or generated guidance source of truth was added. |
| Test coverage | pass | `test_tai_chi_m4_beginner_comprehension_records_required_prompts` and `test_tai_chi_m4_rollback_proof_records_text_only_cleanup` directly check the new M4 evidence files. Existing M1-M3 tests continue to cover the page, method guidance, media count, prompt records, provenance, alt text, and source rules. |
| Edge cases | pass | MP3 explicitly records no residual confusion for Tai Chi purpose, ready stance, weight shift, body feel, pause/stop conditions, and image helpfulness. MP4 exercises removal of image references, unused assets, prompt records, and provenance rows in a temporary text-only state. |
| Error handling | pass | Rollback is documented as non-destructive during proof and as a cleanup contract if an image later fails review. Reviewer rollback rehearsal passed without modifying live approved assets. |
| Architecture boundaries | pass | Markdown remains source of truth; generated rasters, prompt records, and provenance remain repository-local. The review evidence is static Markdown and does not introduce runtime behavior. |
| Compatibility | pass | Stable paths remain unchanged: `exercises/tai-chi-basics.md`, the three media paths, prompt-record paths, and `media/PROVENANCE.md` rows remain valid. The added tests check evidence without changing public content contracts. |
| Security/privacy | pass | M4 proof states no private reader, health, contact, location, or training-log data is recorded. Reviewer privacy scan passed across the page, provenance, prompts, and change-local evidence. |
| Derived artifact currency | pass | The plan, plan index, change metadata, explain-change, validation notes, and tests all point to M4 review evidence and final-closeout routing. No generated output artifact is introduced. |
| Unrelated changes | pass | The reviewed commit is scoped to M4 proof records, tests, validation notes, and workflow metadata. The unrelated untracked walking learn note remains outside the review surface. |
| Validation evidence | pass | Reviewer reruns passed for focused proof tests, CMD1-CMD5 coverage, CMD6 diff check, and a separate temporary rollback rehearsal. The `pytest` gap is recorded as an unavailable optional plan command because the active test spec uses unittest commands. |

## No-Finding Rationale

The M4 slice supplies the missing manual evidence without broadening product scope.
The beginner-comprehension proof records every required MP3 prompt and avoids private data.
The rollback proof records and exercises a text-only temporary state where image references, Tai Chi provenance rows, unused assets, and prompt records can be removed while the page still passes focused checks.
The added tests guard the presence and required content of those proof surfaces, and the reviewer reran the relevant validation commands successfully.

## Residual Risks

This clean review closes M4 only.
Final lifecycle closeout remains, starting with explain-change, followed by final verification and PR handoff if verification passes.
This review does not claim final verification, CI success, branch readiness, or PR readiness.

## Reviewer Validation

- `python3 -m unittest tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m4_beginner_comprehension_records_required_prompts tests.test_markdown_first_real_pages.MarkdownFirstRealPagesTest.test_tai_chi_m4_rollback_proof_records_text_only_cleanup` passed.
- `python3 tools/checks/check_privacy.py exercises/tai-chi-basics.md media/PROVENANCE.md media/prompts/exercises/tai-chi-basics/ docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/` passed.
- `python3 -m unittest tests.test_exercise_method_guidance` passed.
- `python3 tools/checks/check_markdown_first.py exercises/tai-chi-basics.md media/PROVENANCE.md SOURCES.md RED-FLAGS.md` passed.
- `python3 -m unittest tests.test_exercise_image_standard tests.test_markdown_first_real_pages` passed.
- `python3 -m unittest discover -s tests` passed.
- `git diff --check` passed.
- Temporary rollback rehearsal passed with `GYMPRIMER_ROOT=/tmp/gymprimer-tai-chi-review-rollback.xVxtIZ`: Markdown-first checked 4 files and privacy checked 4 files.
