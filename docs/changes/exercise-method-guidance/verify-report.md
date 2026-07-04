# Verify Report: Exercise Method Guidance

## Result

- Skill: verify
- Status: branch-ready
- Verified change ID: `exercise-method-guidance`
- Verification date: 2026-07-04
- Working directory: `<repo-root>`
- Next stage: `pr`
- PR readiness: not claimed; PR body and PR open readiness belong to the `pr` stage.
- Hosted CI status: not observed; this repository has no `.github` workflow directory in the checked workspace.

## Scope

This verification covers the exercise-method guidance change pack after M1-M4 implementation, code-review closeout, and durable explain-change. It also covers the narrow privacy cleanup made during verify to remove pre-existing literal private-path and privacy-pattern examples from historical `docs/changes/` records so the required broad privacy scan can run successfully.

## Traceability

| Requirement area | Test/proof IDs | Files changed | Evidence | Status |
| --- | --- | --- | --- | --- |
| Visible method section and active method types | EMG-T1, EMG-T2, EMG-T3, EMG-T6, EMG-T13 | `docs/templates/exercise-card.md`, `tools/checks/check_markdown_first.py`, `tests/test_exercise_method_guidance.py`, six proof-slice exercise pages | Full unittest suite; Markdown-first check; code-review M1-M3 | pass |
| Static education, forbidden adaptive/treatment wording, and source support | EMG-T4, EMG-T5, EMG-M1 | checker tests, proof-slice pages, `manual-proof/method-source-audit.md` | Full unittest suite; manual source audit; code-review M4 | pass |
| Training-type starter shapes and proof slice mappings | EMG-T6, EMG-M1 | six proof-slice exercise pages, `tests/test_exercise_method_guidance.py` | Real-page tests; manual source audit; M3/M4 reviews | pass |
| Principle page dependency | EMG-T7 | `principles/sets-reps-holds-rest-and-progression.md`, `tests/test_responsible_breadth_m1.py` | Full unittest suite includes Responsible Breadth tests; M2 review | pass |
| Pattern-preview alignment and additive migration | EMG-T8, EMG-T9, EMG-M2 | `patterns/anterior-pelvic-tilt.md`, existing unselected exercise pages, comprehension proof | Real-page tests; Markdown-first check; beginner-comprehension proof | pass |
| Compatibility and deferred method types | EMG-T3, EMG-T11, EMG-M3 | related specs, checker tests, validation ledger | Full unittest suite; deferred-type guardrail in `validation-ledger.md` | pass |
| Lifecycle closeout validation | EMG-T12 | `explain-change.md`, `verify-report.md`, workflow artifacts | Final local command set below | pass |

## Verification Dimensions

| Dimension | Result | Evidence |
| --- | --- | --- |
| Spec coverage | pass | `explain-change.md` maps the actual diff to R1-R42, EMG-T1 through EMG-T13, and EMG-M1 through EMG-M3. |
| Requirement satisfaction | pass | M1-M4 code reviews are clean or resolved; required manual proofs exist and pass. |
| Test coverage | pass | Full unittest suite passed; manual proof records cover semantic source and comprehension obligations. |
| Test validity | pass | Focused tests include negative cases for missing headings, empty labels, hidden-only metadata, inactive types, adaptive programming, and forbidden scope. |
| Architecture coherence | pass | Visible Markdown remains source of truth; no hidden taxonomy, generated source of truth, runtime service, user profile, or adaptive logic was added. |
| Artifact lifecycle state | pass | `docs/plan.md`, the active plan, `change.yaml`, review log, review-resolution, explain-change, and verify report agree on current stage and closed implementation milestones. |
| Plan completion | pass | M1-M4 are closed. Lifecycle Closeout remains active only for PR handoff after this verify. |
| Validation evidence | pass | Final command set passed locally after privacy baseline cleanup. |
| Drift detection | pass | No stale active handoff state found for M4 review-requested or explain-change. |
| Risk closure | pass | Broad rollout is explicitly gated to a later reviewed plan; manual proof re-run triggers are recorded. |
| Release readiness | pass for branch-ready | Local branch is ready for PR handoff. Hosted CI is absent/unobserved and PR body/open readiness are deferred to `pr`. |

## Commands Run

| Command | Result | Important output |
| --- | --- | --- |
| `python3 -m unittest discover -s tests` | pass | Ran 114 tests; OK. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns` | pass | Checked 23 Markdown files. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns` | pass | Checked 337 files. |
| `git diff --check` | pass | No whitespace errors. |

## Privacy Baseline Cleanup

The first run of the broad privacy command failed on historical docs outside `exercise-method-guidance`, including `docs/changes/beginner-fitness-exercise-education-platform/` and `docs/changes/markdown-first-gym-primer/`. Those files contained literal local path examples and raw privacy-pattern command examples. The exercise-method scoped privacy command already passed.

Resolution during verify:

- replaced literal local workspace paths in historical review/verify records with `<repo-root>` or relative file references;
- replaced raw privacy-pattern examples in historical records with `<privacy-pattern>`;
- reran the full privacy command successfully.

This cleanup is not part of the exercise-method feature contract, but it was required for the lifecycle broad privacy command to pass.

## CI Status

No hosted CI run was observed. The checked workspace has no `.github` workflow directory, so this verify report records local validation only.

## Remaining Risks

- PR body and PR-open readiness are not claimed here.
- Hosted CI is absent or unobserved.
- Broad exercise-page rollout remains blocked until a later reviewed plan selects another batch.
- Manual proof records are bounded to the six proof-slice pages and must be rerun after edits to method wording, source citations, starter ranges, stop guidance, method type assignments, principle links, or promoted pattern previews.

## Verdict

Branch-ready for PR handoff based on local verification. Next stage: `pr`.
