# Verify Report: Exercise Muscle Guidance

## Result

- Skill: verify
- Status: completed
- Artifacts changed: `docs/changes/exercise-muscle-guidance-standard/verify-report.md`, `docs/changes/exercise-muscle-guidance-standard/change.yaml`, `docs/plans/2026-07-04-exercise-muscle-guidance.md`, `docs/plan.md`
- Open blockers: none
- Next stage: pr
- Validation: local final verification passed; hosted CI not observed
- Readiness: branch-ready, not PR-body-ready and not PR-open-ready

## Verification Verdict

Ready with local branch-ready evidence. The implementation, tests, spec, architecture, plan, manual proof, review records, review-resolution, and explain-change artifact are coherent for PR handoff.

This report does not claim hosted CI success. PR body readiness and PR open readiness belong to the `pr` stage.

## Traceability

| Requirement group | Test IDs / proof | Files changed | Evidence | Status |
| --- | --- | --- | --- | --- |
| R1-R3 heading adoption and legacy compatibility | XMG-T2, XMG-T3, XMG-T6, XMG-T10 | `tools/checks/check_markdown_first.py`, `tests/test_exercise_muscle_guidance.py`, `tests/test_markdown_first_real_pages.py`, proof-slice exercise pages | Unit and real-page tests passed; untouched legacy pages remain compatible. | pass |
| R4-R15 role- and phase-based muscle guidance | XMG-T4, XMG-T5, XMG-T6, XMG-M1 | Checker, tests, `exercises/rowing-machine.md`, `chest-press.md`, `plank.md`, `chin-nod.md`, `thoracic-extension.md`, `band-pull-apart.md` | Proof-slice real-page tests passed; manual source audit recorded. | pass |
| R16-R20 paired feel cues and compensation wording | XMG-T6, XMG-T7, XMG-M2 | Proof-slice exercise pages, real-page tests, checker wording checks | Tests passed; beginner-comprehension proof recorded. | pass |
| R21-R31 activation, EMG, source-support, and clinical boundaries | XMG-T7, XMG-T8, XMG-M1 | Checker, focused tests, review-resolution, source audit | Source-surface tests passed; CR-XMG-M1-1 resolved; semantic truth remains manual by design. | pass |
| R32-R36 optional muscle-attention image alignment | XMG-T9, XMG-M3 | Manual proof records, existing media/provenance references | Existing image-standard checks passed; image-alignment proof recorded. | pass |
| R37 template guidance | XMG-T1 | `docs/templates/exercise-card.md`, `tests/test_markdown_first_templates.py` | Template tests passed. | pass |
| R38-R40 proof slice and broad rollout gate | XMG-T6, XMG-T11, XMG-M4 | Real-page tests, `manual-proof/broad-rollout-gate.md` | Six proof-slice categories covered; remaining pages classified for future batches. | pass |
| R41-R42 validation findings and observability | XMG-T2, XMG-T7, XMG-T8, XMG-T12 | Checker and focused tests | Stable `exercise_muscle_*` finding categories and paths are tested. | pass |
| R43-R44 manual source audit and beginner comprehension | XMG-M1, XMG-M2, XMG-M3 | Manual proof records | M3 tests assert required evidence surfaces; code-review M3 R1 accepted the proof. | pass |
| AC1-AC5 lifecycle gates | Review records and plan state | Proposal, spec, architecture, plan, test spec, reviews, explain-change | Proposal/spec/architecture/plan/test-spec reviews complete; M1-M3 code reviews complete; explain-change complete. | pass |

## Validation Commands

| Command | Working directory | Result | Output summary |
| --- | --- | --- | --- |
| `python3 -m unittest discover -s tests` | repository root | pass | Ran 136 tests. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns` | repository root | pass | Checked 24 Markdown files. |
| `python3 tools/checks/check_privacy.py docs/templates specs tools tests SOURCES.md RED-FLAGS.md exercises media docs/changes/exercise-muscle-guidance-standard` | repository root | pass | Checked 157 files. |
| `git diff --check` | repository root | pass | No whitespace errors. |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md docs/templates exercises media/PROVENANCE.md` | repository root | pass | Checked 25 Markdown files. |
| `python3 -m unittest tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages tests.test_markdown_first_templates` | repository root | pass | Ran 26 tests. |

## CI Status

Hosted CI was not observed. The repository has `.github/workflows/ci.yml`, which runs unit tests, Markdown-first checks, privacy checks, and `git diff --check` on pull requests. Local equivalents passed during this verification.

## Artifact Drift Assessment

| Surface | Assessment | Status |
| --- | --- | --- |
| `docs/plan.md` and plan body | Both route Exercise Muscle Guidance to `verify` before this report and are updated by this report to route to `pr`. The plan remains active because PR handoff and downstream merge/closeout are not complete. | pass |
| `change.yaml` | No open findings; all governing artifacts are recorded; updated by this report to `branch-ready` and `pr` next. | pass |
| Review records | M1 R1 material finding has a closed review-resolution and M1 R2 accepted it. M2 R1 and M3 R1 have no material findings. | pass |
| `explain-change.md` | Exists after M3 review and explains the final reviewed diff, tests, validation, review-resolution, alternatives, scope, and risks. | pass |
| Diff scope | Actual diff is limited to approved proposal/spec/architecture/plan/test/checker/template/proof-slice/manual-proof/review artifacts. | pass |
| CI workflow | Existing CI covers the same core local validation classes; hosted result is unobserved. | concern |

## Verification Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Spec coverage | pass | Implemented behavior maps to R1-R44 and AC1-AC5. |
| Requirement satisfaction | pass | MUST requirements have test, manual-proof, or review evidence. |
| Test coverage | pass | Required tests and manual proof are present. |
| Test validity | pass | Tests include failing-before-fix evidence for M2 and M3 and stable checker categories. |
| Architecture coherence | pass | Markdown remains source of truth; images remain optional/support-only; no app/runtime behavior added. |
| Artifact lifecycle state | pass | Lifecycle artifacts are synchronized by this report. |
| Plan completion | pass | M1-M3 are closed; plan remains active only for PR handoff and downstream closeout. |
| Validation evidence | pass | Final local validation commands passed and are recorded above. |
| Drift detection | pass | No blocking drift found. |
| Risk closure | pass | Broad migration is gated; semantic source truth remains manual by design; privacy passed. |
| Release readiness | pass | Branch has local branch-ready evidence; hosted CI remains unobserved until PR. |

## Remaining Risks

- Hosted CI has not been observed.
- Manual source audit and beginner comprehension proof are bounded, not exhaustive for future all-exercise migration.
- Remaining exercise pages outside the proof slice still need future batched migration and proof before adopting the new contract.

## Readiness Statement

The branch is ready for PR handoff with local branch-ready evidence. The next lifecycle stage is `pr`. This report does not claim PR body readiness, PR open readiness, hosted CI success, merge readiness, or final project Done.
