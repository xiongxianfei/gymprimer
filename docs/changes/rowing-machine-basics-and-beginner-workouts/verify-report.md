# Verify Report: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: verify
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/verify-report.md`; lifecycle routing metadata
- Open blockers: none
- Next stage: pr
- Validation: local validation passed; hosted CI not observed
- Readiness: branch-ready for PR handoff; not PR body ready and not PR open ready

## Verification Verdict

ready

The final change pack is coherent across governing artifacts, implementation,
tests, manual proof, review records, validation evidence, and lifecycle state.
The branch is ready for PR handoff based on local verification evidence.

## Traceability

| Requirement group | Test IDs | Files changed | Evidence | Status |
| --- | --- | --- | --- | --- |
| R1-R14 page shape, setup, movement, damper, muscles, and broad wording | RMB-T2, RMB-T3, RMB-T4, RMB-T5, RMB-T11; RMB-M1, RMB-M2 | `exercises/rowing-machine.md`; `tests/test_markdown_first_real_pages.py` | Real-page tests passed; source audit and comprehension proof recorded. | pass |
| R15-R22 and R39-R40 scoped `basic_cardio_equipment` and static beginner method | RMB-T1, RMB-T6, RMB-T11; RMB-M1 | `tools/checks/check_markdown_first.py`; `tests/test_exercise_method_guidance.py`; `exercises/rowing-machine.md` | Unit and real-page tests passed; loaded-carry remains deferred. | pass |
| R23-R30 weekly activity, safety routing, page-local sources, and source index | RMB-T8, RMB-T9, RMB-T10; RMB-M1 | `exercises/rowing-machine.md`; `SOURCES.md`; `tests/test_markdown_first_real_pages.py` | Source audit recorded; M2 review-resolution closed CR-RMB-M2-1; tests passed. | pass |
| R31-R36 generated support media | RMB-T12; RMB-M4 | `media/exercises/rowing-machine/*.png`; `media/PROVENANCE.md`; `media/prompts/exercises/rowing-machine/*.md`; `manual-proof/visual-safety-review.md` | Image tests passed; visual-safety review approved all three assets. | pass |
| R37-R38 product and clinical boundaries | RMB-T11 | `exercises/rowing-machine.md`; tests and checkers | Forbidden-scope tests and Markdown-first checks passed. | pass |
| AC6-AC7 manual proof | RMB-M1 through RMB-M5 | `manual-proof/*.md`; `specs/rowing-machine-basics-and-beginner-workouts.test.md` | Manual proof metadata scan passed; proof artifacts exist. | pass |

## Validation Commands

All commands were run locally from the repository root on branch
`proposal/rowing-machine-basics`.

| Command | Result | Evidence |
| --- | --- | --- |
| `python3 -m unittest discover -s tests` | pass | Ran 121 tests; result `OK`. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns` | pass | Checked 24 Markdown files; result `pass`. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns` | pass | Checked 364 files; result `privacy pass`. |
| `git diff --check` | pass | No whitespace errors reported. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media` | pass | Checked 27 Markdown files; result `pass`. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md specs/rowing-machine-basics-and-beginner-workouts.test.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md` | pass | Checked 86 files; result `privacy pass`. |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages` | pass | Ran 20 tests; result `OK`. |
| `python3 -m unittest discover -s tests -p 'test_*image*.py'` | pass | Ran 14 tests; result `OK`. |
| coverage scan for R1-R40, E1-E5, and EC1-EC10 in `specs/rowing-machine-basics-and-beginner-workouts.test.md` | pass | All requirement, example, and edge-case IDs present. |
| manual proof metadata scan for RMB-M1 through RMB-M5 | pass | Each proof includes automation rationale, required environment, evidence artifact, pass condition, failure condition, owning stage, and re-run trigger. |
| review closeout scan for `review-resolution.md` and `review-log.md` | pass | `review-resolution.md` is closed; no open finding terms found. |
| lifecycle state-sync check across `docs/plan.md`, active plan, `change.yaml`, and `explain-change.md` | pass | Artifacts were in verify state before this report. |

## Post-Report Recording Checks

| Command | Result | Evidence |
| --- | --- | --- |
| `python3 tools/checks/check_privacy.py docs/changes/rowing-machine-basics-and-beginner-workouts/verify-report.md docs/changes/rowing-machine-basics-and-beginner-workouts/explain-change.md docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md docs/plan.md` | pass | Checked 5 files; result `privacy pass`. |
| `git diff --check` | pass | No whitespace errors reported after verify-report recording. |
| lifecycle state-sync check after verify-report recording | pass | Plan index, active plan, change metadata, verify report, and explain-change all route to `pr`. |
| stale verify-stage wording scan | pass | No stale `verify` next-stage or pre-verify readiness wording found. |

## CI Status

`.github/workflows/ci.yml` exists and runs unit tests, Markdown-first checks,
privacy checks, and `git diff --check` for pull requests, pushes to `main`,
workflow dispatch, and a weekly schedule. Hosted CI was not observed during
this verification, so this report claims local validation only.

## Artifact Drift

No blocking drift found.

- `docs/plan.md`, the active plan, and `change.yaml` agreed that the change was
  at `verify` before this report.
- `review-resolution.md` is closed and review-log entries show later approving
  reviews for each material finding.
- `explain-change.md` existed and was current before verification.
- The final verification state is recorded by this report and routed to `pr`.

## Risk Closure

- Rollback remains Markdown-first: remove the rower page/media/provenance rows
  and keep global sources only if still reused.
- Generated media risk is controlled by local assets, provenance, prompt
  records, visual-safety review, alt text, and tests.
- Safety-source risk was resolved in CR-RMB-M2-1 by splitting safety notes into
  source-supported groups.
- Privacy risk is controlled by privacy scans and non-identifying manual proof.

## Remaining Risks

- Hosted CI has not been observed.
- PR body preparation and PR opening are downstream `pr` responsibilities.

## Handoff

Branch-ready local evidence is complete. The next valid lifecycle stage is
`pr`. This report does not claim PR body readiness, PR open readiness, hosted CI
success, merge readiness, or Done.
