# Code Review M3A R1: Prompt Record Validation

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r1.md`, `docs/changes/exercise-image-standard-and-optimization/review-log.md`, `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`, `docs/changes/exercise-image-standard-and-optimization/change.yaml`, `docs/plans/2026-07-03-exercise-image-standard.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-EIS-M3A-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/code-review-m3a-r1.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Reviewed milestone: M3A
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3A resolution, M3 re-review/resolution, M4, lifecycle closeout
- Required review-resolution: yes
- Finding IDs: CR-EIS-M3A-1
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: commit `9f8beb5` (`M3A: implement prompt record validation`), especially `tools/checks/check_markdown_first.py`, `tests/test_exercise_image_standard.py`, `media/PROVENANCE.md`, `docs/changes/exercise-image-standard-and-optimization/evidence/m3a-prompt-record-backfill.md`, and lifecycle state updates.
- Tracked governing branch state: approved prompt-record spec amendment, approved architecture/ADR, approved plan amendment, approved test-spec-review R5, and M3A review-requested state are present in tracked branch state.
- Governing artifacts: `specs/exercise-image-standard.md` R20-R20H, `specs/exercise-image-standard.test.md` EIS-T19 through EIS-T21, and `docs/plans/2026-07-03-exercise-image-standard.md` M3A.
- Validation evidence inspected: M3A validation notes in the active plan and change metadata; reviewer direct probe for the compatibility limitation path.

## Diff summary

M3A adds prompt-record validation helpers to the Markdown-first checker, adds fixture coverage for prompt-record link and content failures, adds the `prompt_record` column to `media/PROVENANCE.md`, and records explicit compatibility evidence for the ten in-flight M3 generated exercise images whose exact prompts were not recoverable from durable repository evidence.

The core validation behavior is mostly present, but the compatibility exception is not scoped to the ten recorded pre-amendment M3 assets.

## Findings

## Finding CR-EIS-M3A-1

- Finding ID: CR-EIS-M3A-1
- Severity: major
- Location: `tools/checks/check_markdown_first.py:550`
- Evidence: R20 requires a generated raster exercise image provenance row to include non-blank `prompt_record`, and EIS-T21 limits unavailable-prompt handling to an explicit compatibility limitation for a pre-amendment asset or replacement. The implementation accepts any governed exercise image with a blank `prompt_record` when `notes` exactly equals `M3 pre-amendment prompt unavailable; compatibility limitation recorded` (`tools/checks/check_markdown_first.py:550-553`). The M3A evidence scopes that limitation to ten listed M3 assets, but the checker does not check that asset list. A reviewer temporary-root probe created a non-M3 `media/exercises/fixture-exercise/setup.png` row with blank `prompt_record` and that note; `check_markdown_first.py` returned `0` and reported `checked 1 Markdown file(s): pass`.
- Required outcome: The compatibility bypass must be constrained to the explicitly recorded pre-amendment M3 assets, and future governed generated raster exercise images must fail without a valid `prompt_record`.
- Safe resolution path: Add a deterministic allowlist or equivalent scoped predicate for the ten M3A compatibility assets recorded in `m3a-prompt-record-backfill.md`; require normal prompt-record validation for every other `exercise_*` generated raster exercise image. Add a regression test proving a non-M3 governed exercise image with the compatibility note and blank `prompt_record` fails, while the recorded M3 compatibility rows remain accepted. Rerun the M3A validation commands and return M3A to `review-requested`.
- needs-decision rationale: none
- auto_fix_class: none

## Checklist coverage

- Spec alignment: block. The compatibility record is allowed for the in-flight M3 images, but the checker turns it into a general bypass for R20/R20A on any future governed generated raster exercise image.
- Test coverage: concern. The new tests cover missing/invalid prompt-record fields and the redaction path, but they do not cover the critical boundary that the compatibility limitation applies only to the recorded M3 assets.
- Edge cases: block. EC8E/EIS-T21 are not fully protected because an unrelated new exercise image can silently enter the pre-amendment compatibility path.
- Error handling: concern. Missing prompt-record handling has stable categories for normal failures, but the fallback branch returns success before proving the asset is eligible for the fallback.
- Architecture boundaries: pass. The diff stays within static checker, central provenance, change-local evidence, and tests; no runtime, CMS, hosted media, API, or generated JSON path is introduced.
- Compatibility: concern. Legacy-compatible purposes remain valid, but the new compatibility note can be copied onto non-legacy, new-purpose exercise images and bypass prompt-record migration requirements.
- Security/privacy: pass. The reviewed diff does not expose secrets or private data, and the scoped privacy validation passed over the changed review/provenance/checker/test surfaces.
- Derived artifact currency: pass. The plan, plan index, change metadata, provenance table, and M3A evidence were updated together for the implementation handoff.
- Unrelated changes: pass. The diff is scoped to M3A prompt-record validation, provenance schema, evidence, tests, and lifecycle routing.
- Validation evidence: concern. The recorded validation commands are relevant and credible for the implemented happy and failure paths, but they do not exercise the unscoped compatibility bypass found during review.

## No-finding rationale

Not applicable; this review has one material finding.

## Direct-proof gaps

- No direct proof shows that a non-M3 governed generated raster exercise image with the compatibility note and blank `prompt_record` fails. The reviewer probe shows the opposite.
- Direct proof exists for the normal prompt-record path via `tests/test_exercise_image_standard.py`, but the compatibility boundary needs its own regression.

## Validation run during review

- Temporary-root probe: non-M3 generated exercise image with blank `prompt_record` and the M3 compatibility note returned `0` from `check_markdown_first.py`, proving CR-EIS-M3A-1.

## Milestone handoff state

- Reviewed milestone: M3A
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M3A resolution, M3 re-review/resolution, M4, lifecycle closeout
- Next stage: review-resolution for CR-EIS-M3A-1
- Final closeout readiness: not ready because M3A has an unresolved material finding, M3 still has unresolved reader-prompt evidence, and M4, explain-change, final verification, and PR handoff remain open.
