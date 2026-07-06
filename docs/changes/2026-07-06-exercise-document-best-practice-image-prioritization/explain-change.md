# Explain Change: Exercise Document Best-Practice Image Prioritization

## Status

explain-change complete

## Summary

This change turns the user's per-exercise-document image-improvement request into a governed audit and proof workflow.
It does not generate images directly from chat and does not require exercise pages to reach five images.

The implemented slice:

- records the current fewer-than-five exercise-document evaluation population;
- defines a page-local top-10 candidate audit contract;
- audits `exercises/bird-dog.md` as the first page-specific slice;
- preserves the existing Bird Dog sequence image;
- selects zero generated images for the first slice;
- records visual-safety, source-support, beginner-comprehension, privacy, rollback, and non-goal proof for the zero-generated-image outcome;
- adds focused validation helpers and tests for audit and closeout-proof contracts.

All implementation milestones M1-M3 are closed by code review.
The next lifecycle stage is final verification.

## Problem

The original request asked to list top images and generate useful exercise-document images.
The user clarified that evaluation must happen for each exercise document, not as one repository-wide list.

The repository rules also require durable artifacts before substantive media, content-contract, generated-output, provenance, or validation changes.
Directly generating a top-five image batch from chat would have bypassed prompt records, provenance, visual-safety review, image-count policy, and page-local proof.

## Decision Trail

| Stage | Decision | Source |
|---|---|---|
| Proposal | Use per-exercise-document top-10 candidate tables and treat the top five as backlog, not an automatic generation target. | `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md` |
| Proposal review | Clarified that documents with fewer than five images are an evaluation trigger, not an image-count target. | `reviews/proposal-review-r2.md` |
| Spec | Required page-local audits, minimum-needed generated subsets, existing-image preservation, source-of-truth Markdown, rollback proof, and non-goal preservation. | `specs/exercise-document-best-practice-image-prioritization.md` |
| Architecture | Recorded `architecture-not-required`; existing exercise-image, prompt-record, provenance, and validation architecture is sufficient. | `architecture-assessment.md` |
| Plan | Split work into M1 audit proof, M2 first page-specific slice, and M3 closeout proof. | `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md` |
| Test spec | Mapped requirements to EDIP-T1 through EDIP-T14 plus manual proof EDIP-MP1 through EDIP-MP4. | `specs/exercise-document-best-practice-image-prioritization.test.md` |

## Requirement Trace

| Requirement area | Implemented by |
|---|---|
| R1-R2, AC1 | M1 current inventory and tests for the fewer-than-five evaluation trigger. |
| R3-R9, AC2-AC3 | Audit-record validator, M1 criteria, and M2 Bird Dog page-local top-10 table. |
| R10-R15, AC4 | M2 generation-decision validation for minimum-needed subset, count exceptions, purpose boundaries, and muscle-attention limits. |
| R16-R18, AC6 | M2/M3 guardrails for prompt/provenance boundaries, Markdown source of truth, forbidden claims, and zero-generated-image visual proof. |
| R19-R22, AC5 | Existing-image decision validation and change-local criteria before template updates. |
| R23 | First-slice scope validation and Bird Dog-only M2 audit. |
| R24, AC7 | M3 rollback proof and closeout-proof validation. |
| R25-R26, AC8 | M3 non-goal smoke and lifecycle evidence that no runtime, hosted, clinical, coaching, video-first, or PR-rule behavior was introduced. |

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|
| `tools/checks/exercise_document_image_prioritization.py` | Added helpers for image-count inventory, audit-record validation, candidate scoring, generation decisions, replacement reasons, slice scope, and closeout proof. | Needed deterministic local proof for the audit and closeout contracts without changing shared media architecture. | Spec R1-R24; architecture-not-required assessment; plan M1-M3. | `tests/test_exercise_document_image_prioritization.py`; full test discovery. |
| `tests/test_exercise_document_image_prioritization.py` | Added focused unit tests for EDIP-T1 through EDIP-T14. | Gives direct proof for the new audit and closeout rules before relying on manual review. | Test spec EDIP-T1 through EDIP-T14. | `python3 -m unittest tests.test_exercise_document_image_prioritization`; `python3 -m unittest discover -s tests`. |
| `evidence/m1-audit-criteria.md` | Recorded the evaluation population and audit criteria. | M1 needed change-local criteria before template changes or image promotion. | Spec R1-R9, R19-R22; plan M1. | M1 code review and Markdown/privacy checks. |
| `evidence/m2-bird-dog-page-audit.md` | Recorded Bird Dog current image state, section coverage, existing-image decision, top-10 candidate backlog, scoring matrix, generation decision, and rollback path. | Applies the per-document audit to one selected page while preserving the existing sequence image and selecting zero generated images. | Spec R3-R18, R23; plan M2. | Code-review M2 R2; CR-EDIP-M2-1 resolution. |
| `evidence/m3-review-closeout-proof.md` | Recorded visual-safety status, source-support audit, beginner-comprehension proof, privacy review, rollback proof, and non-goal smoke. | M3 needed closeout evidence even though the generated subset is zero. | Spec R16-R18, R24-R26; AC6-AC8; plan M3. | Code-review M3 R1; rollback worktree proof. |
| `review-resolution.md` | Tracked and closed proposal and code-review findings. | Material findings had to be resolved before final closeout. | Proposal-review R1, code-review M1 R1, code-review M2 R1. | Code-review M1 R2 and M2 R2. |
| `review-log.md` and `reviews/*.md` | Recorded proposal, spec, plan, test-spec, and code-review outcomes. | Maintains lifecycle traceability and downstream handoff state. | Workflow review requirements. | Review-record Markdown/privacy checks. |
| `change.yaml`, `docs/plan.md`, and active plan | Kept current stage, milestone state, validation notes, and next handoff synchronized. | Prevents stale routing between implementation, review, explain-change, verify, and PR stages. | Plan handoff rules. | State-sync `rg` checks. |
| `docs/proposals/...`, `specs/...`, and `specs/...test.md` | Captured accepted direction, observable contract, and proof map before implementation. | Repository rules prohibit substantive media/content-contract changes from chat alone. | AGENTS.md source order and workflow rules. | Proposal-review, spec-review, and test-spec-review approvals. |

## Tests Added Or Changed

| Test coverage | What it proves | Level |
|---|---|---|
| EDIP-T1 and EDIP-T2 | Pages with fewer than five images enter evaluation, but that trigger does not mandate generation. | unit |
| EDIP-T3 and EDIP-T4 | Page-local audits require core fields, ten candidates or rationale, five scoring dimensions, and correct totals. | unit |
| EDIP-T5 | Top-five candidates cannot use direct generation dispositions, and candidate six needs churn rationale. | unit |
| EDIP-T6 and EDIP-T7 | Fourth/fifth image additions need exception approval, purposes are bounded, and second muscle-attention images are rejected. | unit |
| EDIP-T8 and EDIP-T9 | Markdown remains source of truth and forbidden image-adjacent clinical/coaching claims are rejected. | unit/integration |
| EDIP-T10 and EDIP-T11 | Existing acceptable images are preserved and template updates remain deferred. | unit/integration |
| EDIP-T12 | First-slice scope stays one page unless a small-batch rationale exists. | contract |
| EDIP-T13 and EDIP-T14 | Closeout proof requires rollback commands, generated-image visual review when images exist, privacy status, and non-goal flags. | unit/smoke |

The test level is intentionally mostly unit/contract because the first slice is proof and Markdown evidence, not media generation.
Existing Markdown-first, privacy, exercise-image, and real-page tests provide broader integration coverage.

## Validation Evidence Before Final Verify

Local validation recorded before this explain-change stage includes:

| Command or proof | Result |
|---|---|
| `python3 -m unittest tests.test_exercise_document_image_prioritization` | passed during M1, M2 review-resolution, and M3 focused validation |
| `python3 -m unittest tests.test_exercise_document_image_prioritization tests.test_exercise_image_standard tests.test_markdown_first_real_pages` | passed for M2 |
| `python3 -m unittest discover -s tests` | passed for M3 and reviewer rerun, 198 tests in the latest recorded run |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization` | passed for M3 and reviewer rerun |
| `python3 tools/checks/check_privacy.py -- README.md SOURCES.md RED-FLAGS.md specs docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization docs/plans media exercises tools tests` | passed for M3 and reviewer rerun |
| Rollback worktree proof for `exercises/bird-dog.md` | passed Markdown-first and privacy checks |
| `git diff --check` | passed after each milestone and review handoff |

Hosted CI had not been observed when explain-change was recorded.
Final verification had not run yet when explain-change was recorded; later final verification evidence belongs in `verify-report.md`.

## Review Resolution Summary

`docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md` is closed.

| Finding group | Count | Disposition |
|---|---:|---|
| Proposal-review findings | 2 | resolved by proposal revision and proposal-review R2 |
| Code-review findings | 2 | resolved by M1 and M2 review-resolution, confirmed by code-review M1 R2 and M2 R2 |
| Open material findings | 0 | none |

Key fixes:

- PR-EDIP-001 clarified that fewer than five images is an evaluation trigger, not a generation target.
- PR-EDIP-002 removed proposal-specific PR-review rule language.
- CR-EDIP-M1-1 made top-five direct generation dispositions fail validation.
- CR-EDIP-M2-1 added the required per-rank scoring matrix to the Bird Dog audit.

## Alternatives Rejected

| Alternative | Why rejected |
|---|---|
| Generate top-five images immediately from chat | Would bypass prompt records, provenance, visual-safety review, tests, and source-of-truth Markdown. |
| Create one repository-wide top-10 image list | Conflicts with the user's clarification that evaluation is per exercise document. |
| Normalize all fewer-than-five pages to five images | Conflicts with the approved exercise-image count policy and the final proposal direction. |
| Replace older sequence images for style consistency | Spec R19-R21 require preserving acceptable images unless a concrete page-local replacement reason exists. |
| Update `docs/templates/exercise-card.md` in M1 | Rejected until first-slice criteria prove stable and reusable. |
| Add generated media in the Bird Dog slice | The page-local audit found the existing sequence image and Markdown sufficient for this first slice. |

## Scope Control

The change preserves the approved non-goals:

- no generated image was promoted;
- no exercise page was edited;
- no media asset, prompt record, or provenance row was added;
- no exercise template was updated;
- no new exercise page was created;
- no hosted app, CMS, database, account, API, video-first path, or personalized coaching behavior was introduced;
- no clinical treatment, cure, recovery protocol, exact-anatomy-as-authority, or workout-planner behavior was added.

## Risks And Follow-Ups

| Risk or follow-up | Status |
|---|---|
| Manual beginner-comprehension proof is qualitative. | Accepted for this slice because no generated image is promoted and final verify still remains. |
| The audit helper validates structured records, while Markdown evidence is still partly manually reviewed. | Mitigated by code reviews and the CR-EDIP-M2-1 scoring-matrix fix. |
| Remaining exercise documents still need their own page-specific audits. | Deferred to future slices; this change proves the first page-specific workflow. |
| Final lifecycle gates remain. | `verify-report.md` records final local verify; PR body/open readiness is not claimed here. |

## Readiness

Explain-change is complete.
All implementation milestones are closed and review-resolution is closed.
The change is ready for final verification.

## Sources

- `docs/proposals/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.md`
- `specs/exercise-document-best-practice-image-prioritization.test.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/architecture-assessment.md`
- `docs/plans/2026-07-06-exercise-document-best-practice-image-prioritization.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-resolution.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/review-log.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m1-audit-criteria.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m2-bird-dog-page-audit.md`
- `docs/changes/2026-07-06-exercise-document-best-practice-image-prioritization/evidence/m3-review-closeout-proof.md`
