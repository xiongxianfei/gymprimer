# Code Review M2 R1: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r1.md`, `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`, `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`, `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`, `docs/changes/rowing-machine-basics-and-beginner-workouts/change.yaml`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-RMB-M2-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: yes
- Finding IDs: CR-RMB-M2-1
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `ed65ef5` for M2 implementation, especially
  `exercises/rowing-machine.md`, `SOURCES.md`, and
  `tests/test_markdown_first_real_pages.py`.
- Tracked governing branch state: commit `ed65ef5` includes the accepted
  proposal, approved spec, approved architecture update, active plan, active
  test spec, M1 clean code-review, M2 implementation, and M2 validation notes.
- Governing artifacts:
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m1-r1.md`
  - `specs/markdown-first-primer.md`
  - `specs/exercise-method-guidance.md`
- Validation evidence:
  - plan validation notes for M2;
  - commit message validation evidence in `ed65ef5`;
  - independent reviewer rerun of
    `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`;
  - direct source check of the Mayo Clinic page cited by
    `local-rowing-machine-safety`.

## Diff Summary

M2 adds `exercises/rowing-machine.md` with the approved page structure,
text-first rowing technique guidance, `basic_cardio_equipment` method guidance,
static workout examples, weekly aerobic-plus-strength framing, central
`RED-FLAGS.md` routing, and page-local sources.

M2 also adds reusable Concept2 rowing sources to `SOURCES.md` and extends
`tests/test_markdown_first_real_pages.py` with real-page assertions for
required sections, stroke sequence, setup and damper wording, method labels,
stop-condition presence, central safety link, source IDs, and forbidden scope.

## Findings

## Finding CR-RMB-M2-1

- Finding ID: CR-RMB-M2-1
- Severity: major
- Location: `exercises/rowing-machine.md:164`
- Evidence: R27 requires concrete safety and stop-condition claims to have
  page-local source support. The safety sentence cites only
  `[Mayo Clinic][local-rowing-machine-safety]` for the full stop-condition list:
  chest pain, dizziness, fainting, unusual shortness of breath, sharp pain,
  numbness, worsening symptoms, painful technique, and jerky or uncontrolled
  movement. The cited Mayo Clinic heart-attack symptoms page supports heart
  attack warning signs such as chest pain, shortness of breath,
  lightheadedness/sudden dizziness, and feeling like you might pass out, but it
  does not support the whole rowing stop-condition list, especially numbness,
  general worsening symptoms, painful technique, or jerky/uncontrolled
  technique breakdown.
- Required outcome: Every concrete stop condition in the rowing-machine page
  must either be directly supported by nearby page-local citations or narrowed
  to claims supported by the cited source.
- Safe resolution path: Split the safety note into source-supported groups,
  add or reuse appropriate page-local sources that directly support the
  non-cardiopulmonary stop conditions, or narrow/remove unsupported terms while
  preserving R26. Rerun M2 validation and request M2 code-review again.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | R26 requires the stop-condition list, and R27 requires concrete safety claims to have page-local source support. `exercises/rowing-machine.md:164` over-uses one source for unsupported stop-condition claims. |
| Test coverage | concern | The M2 real-page tests prove the stop-condition terms and link exist, but they do not verify semantic source support for each safety claim. |
| Edge cases | concern | EC8 warns that sources must support the specific gym-beginner claim or the claim should be narrowed; the safety citation currently mixes supported and unsupported safety concepts. |
| Error handling | pass | No runtime error path or parser fallback is introduced by M2. |
| Architecture boundaries | pass | The implementation remains Markdown-first and adds no app, API, tracker, calculator, hidden metadata source of truth, or generated output. |
| Compatibility | pass | Existing source-index and Markdown-first checks still pass locally; no existing exercise page contract is migrated. |
| Security/privacy | pass | The reviewed diff contains no secrets, private health details, user data, or identifying beginner-comprehension evidence. |
| Derived artifact currency | pass | No generated raster media, provenance row, prompt record, or derived output is introduced in M2. |
| Unrelated changes | pass | The diff is limited to the rowing page, reusable sources, real-page tests, and lifecycle metadata for M2. |
| Validation evidence | concern | Required M2 commands pass, and the reviewer reran the combined unittest command, but the semantic source-support issue is not caught by those automated checks. |

## Direct-Proof Gaps

The direct automated proof for R27 currently checks the presence of source
markers and stop-condition text, not whether the cited source supports every
claim. M3 will run a broader manual source audit, but M2 itself claims
source-backed stop conditions in the plan and includes the concrete safety
sentence now, so the unsupported citation must be resolved before M2 can close.

## Milestone Handoff State

- Reviewed milestone: M2.
- Review status: changes-requested.
- Milestone state after review: resolution-needed.
- Required review-resolution: yes, for CR-RMB-M2-1.
- Remaining in-scope implementation milestones: M2, M3, M4.
- Next stage: review-resolution for CR-RMB-M2-1.
- Final closeout readiness: not-ready because M2 needs review-resolution and
  re-review, and M3-M4 remain open.

## Residual Risks

This review focused on the M2 implementation slice. It does not claim manual
source-audit completion, beginner-comprehension proof, optional media
readiness, final verification, branch readiness, PR readiness, hosted CI
success, or completion of M3-M4.
