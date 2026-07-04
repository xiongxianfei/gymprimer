# Code Review M4 R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m4-r1.md`
- Open blockers: none
- Next stage: final closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M4
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `f638c8f`, especially
  `docs/changes/rowing-machine-basics-and-beginner-workouts/validation-ledger.md`,
  `docs/changes/rowing-machine-basics-and-beginner-workouts/explain-change.md`,
  `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml`,
  `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`,
  and `docs/plan.md`.
- Cross-milestone surface: branch diff from `main...HEAD` for final
  implementation-slice interaction review, including the rowing page, method
  validation, media prompt-record handling, source/support records, test spec,
  architecture update, and lifecycle records.
- Tracked governing branch state: commit `f638c8f` includes accepted proposal,
  approved spec, approved architecture update, active plan, active test spec,
  plan/test-spec reviews, M1-M3 implementation and code-review records, and M4
  validation ledger.
- Governing artifacts:
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/architecture/system/architecture.md`
  - `CONSTITUTION.md`
  - `AGENTS.md`
- Validation evidence:
  - M4 validation ledger and plan validation notes;
  - independent reviewer rerun of `python3 -m unittest discover -s tests`;
  - independent reviewer rerun of
    `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media`;
  - independent reviewer rerun of
    `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md exercises patterns principles programs media docs/changes/rowing-machine-basics-and-beginner-workouts specs/rowing-machine-basics-and-beginner-workouts.md docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`;
  - independent reviewer rerun of `git diff --check`;
  - direct lifecycle state-sync check for M4 review-requested state and ledger
    contents.

## Diff Summary

M4 adds the validation ledger required by `RMB-M5`, recording the full local
test suite, broad Markdown-first validation, privacy scan, whitespace check,
CI observation status, residual risk, and promotion/navigation decision. It
updates the change-local rationale with an M4 section and moves the active plan,
plan index, and change metadata from `implement M4` to `code-review M4`.

The full branch surface remains aligned with the accepted implementation flow:
M1 scoped `basic_cardio_equipment`, M2 added the rowing page and source support,
M2 review-resolution narrowed safety source support, M3 recorded source audit,
beginner comprehension, and text-only media decision, and M4 records final
integration validation evidence. No README navigation, media asset, provenance
row, prompt record, hosted app, tracker, calculator, or user-input flow is
added in M4.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | M4 satisfies the plan and `RMB-M5` requirement for a durable ledger with exact commands, outcomes, residual risk, CI observation status, and promotion/navigation decision. The ledger also avoids claims forbidden by spec observability and the constitution. |
| Test coverage | pass | Reviewer reran the full local suite: `python3 -m unittest discover -s tests` passed with 120 tests. M4 itself is evidence-oriented; the proof surface is `validation-ledger.md` plus plan/change metadata. |
| Edge cases | pass | The ledger explicitly records hosted CI was not observed, no media is referenced, no provenance/prompt/visual-safety evidence is required, and README navigation is unchanged because the approved plan makes it conditional. |
| Error handling | pass | No runtime code path, parser behavior, fallback behavior, permissions handling, or user-input flow changes in M4. Validation failure handling remains represented by exact command/result ledger entries. |
| Architecture boundaries | pass | The branch remains Markdown-first content and local validation tooling. M4 adds no hosted runtime, generated API, database, tracker, calculator, hidden metadata source of truth, or media source-of-truth behavior. |
| Compatibility | pass | M4 preserves README navigation and existing content paths. The branch-level diff adds `exercises/rowing-machine.md` and scoped validator behavior without migrating existing exercise pages or activating `loaded_carry`. |
| Security/privacy | pass | The ledger and lifecycle records contain no private reader, contact, health, secret, or credential data. Reviewer privacy scan over the M4 surface passed. |
| Derived artifact currency | pass | M4 records that no rowing media is referenced and no rowing provenance row, prompt record, or visual-safety review is required. The earlier M3 exercise-image audit row keeps the current exercise inventory synchronized. |
| Unrelated changes | pass | The M4 commit is limited to validation ledger, rationale, and lifecycle handoff updates. Cross-milestone branch changes match the accepted rowing-machine scope and prior recorded reviews. |
| Validation evidence | pass | Reviewer reran the exact M4 validation commands and checked lifecycle state. All commands passed locally; CI remains explicitly unobserved. |

## No-Finding Rationale

The M4 implementation adds the missing evidence artifact rather than changing
reader-facing content. The ledger names every required M4 command, records
clear pass outcomes, includes residual risks, states that hosted CI was not
observed, explains why README navigation was not changed, and explicitly avoids
branch-readiness, PR-readiness, final-verification, final-closeout, and CI-pass
claims.

The plan, plan index, and change metadata agree that M4 is the current
review-requested milestone. Independent reruns reproduced the recorded local
validation results. The full branch diff was also sampled for cross-milestone
interaction risk: M1-M3 are closed by review, no required review-resolution is
open, media remains text-only, and the final implementation milestone now has
the required lifecycle evidence.

## Residual Risks

Final closeout still needs the downstream explain-change/final rationale pass,
final verification, and PR handoff. Hosted CI was not observed. This review
does not claim final verification, branch readiness, PR readiness, hosted CI
success, or merge readiness.
