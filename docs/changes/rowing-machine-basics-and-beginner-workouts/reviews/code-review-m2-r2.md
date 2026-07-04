# Code Review M2 R2: Rowing Machine Basics and Beginner Workout Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r2.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r2.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Review resolution: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: closed
- Remaining implementation milestones: M3, M4
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `c8c4683` resolving CR-RMB-M2-1, especially
  `exercises/rowing-machine.md`, `tests/test_markdown_first_real_pages.py`,
  and the M2 lifecycle records.
- Tracked governing branch state: commit `c8c4683` includes the accepted
  proposal, approved spec, approved architecture update, active plan, active
  test spec, M1 clean code-review, M2 R1 changes-requested review,
  review-resolution evidence, and M2 validation notes.
- Governing artifacts:
  - `specs/rowing-machine-basics-and-beginner-workouts.md`
  - `specs/rowing-machine-basics-and-beginner-workouts.test.md`
  - `docs/plans/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/code-review-m2-r1.md`
  - `docs/changes/rowing-machine-basics-and-beginner-workouts/review-resolution.md`
- Validation evidence:
  - plan validation notes for CR-RMB-M2-1 review-resolution;
  - commit message validation evidence in `c8c4683`;
  - independent reviewer rerun of
    `python3 -m unittest tests.test_exercise_method_guidance tests.test_markdown_first_real_pages`;
  - independent reviewer rerun of
    `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises principles patterns`;
  - independent reviewer rerun of
    `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises docs/changes/rowing-machine-basics-and-beginner-workouts`;
  - independent reviewer rerun of `git diff --check`;
  - direct source checks for the safety citations added or reused in the
    resolution.

## Diff Summary

The review-resolution diff splits the rowing-machine `## Safety notes` line
into three source-supported safety groups:

- chest pain, dizziness, fainting, and unusual shortness of breath cite the
  Mayo Clinic heart-attack symptoms reference;
- sharp pain, worsening symptoms, and numbness cite Mayo Clinic exercise-pain
  guidance plus NHS back-pain red-flag routing;
- painful, jerky, or uncontrolled technique cites Mayo Clinic weight-training
  technique guidance.

The rowing page now includes page-local source entries and reference
definitions for `local-rowing-machine-exercise-pain`, `nhs-back-pain`, and
`mayo-weight-training`. The real-page test now requires those safety source
IDs, preserving regression coverage for the prior source-support finding.

Lifecycle records move CR-RMB-M2-1 from open review-resolution to resolved
pending this re-review and route M2 back to code-review.

## Findings

No blocking or required-change findings.

## Prior Finding Reconciliation

| Finding ID | R1 disposition | R2 result | Evidence |
| --- | --- | --- | --- |
| CR-RMB-M2-1 | changes-requested | resolved | `exercises/rowing-machine.md:164-168` now separates the stop-condition groups and cites source IDs that appear in the page-local `## Sources` section; `tests/test_markdown_first_real_pages.py:147-161` now requires the relevant safety source IDs. |

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | R25-R27 require central red-flag routing, the listed stop conditions, and page-local safety source support. `exercises/rowing-machine.md:164-168` keeps the `../RED-FLAGS.md` link and all required stop-condition terms with nearby page-local citations. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py:117-161` checks the stop-condition terms, central safety link, and required safety source IDs. The implementer recorded a fail-before-fix for missing safety source definitions, and the reviewer reran the combined unittest command successfully. |
| Edge cases | pass | EC8 is addressed by narrowing the prior overbroad safety citation into source-specific groups instead of relying on one heart-attack page for unrelated stop conditions. |
| Error handling | pass | No runtime path, parser fallback, or user-input flow is introduced; Markdown-first validation still handles source ID and claim-level citation errors. |
| Architecture boundaries | pass | The change remains a static Markdown page plus tests and lifecycle records; it adds no app, API, tracker, calculator, hidden metadata source of truth, generated output, or media. |
| Compatibility | pass | Reused source IDs `nhs-back-pain` and `mayo-weight-training` are already present in `SOURCES.md`; the new `local-rowing-machine-exercise-pain` ID follows the page-local source convention and does not require global indexing. |
| Security/privacy | pass | The diff adds public source references and lifecycle records only; privacy scan over the content and change records passed. |
| Derived artifact currency | pass | No generated raster media, provenance row, prompt record, or derived output is introduced. |
| Unrelated changes | pass | The diff is limited to the rowing safety source fix, the targeted real-page test, and required lifecycle records. |
| Validation evidence | pass | Reviewer reran the M2 commands: combined unittests passed, Markdown-first check passed, privacy check passed, and `git diff --check` passed. |

## No-Finding Rationale

The prior material finding was that one Mayo heart-attack symptoms source was
used for the full stop-condition list. The re-review diff removes that
overbroad citation pattern and attaches the safety claims to narrower source
groups. The cited source roles are now plausible and auditable: heart-attack
symptoms for chest pain, shortness of breath, dizziness, and feeling like
passing out; exercise-pain guidance for sharp or worsening pain; NHS back-pain
routing for numbness-related red flags; and technique guidance for controlled
movement and stopping painful exercise.

The automated proof was also strengthened: the real-page test now fails when
the added safety source IDs are missing. The Markdown-first checker separately
proved claim-level safety citations and page-local/global source-index rules
for the current page.

## Residual Risks

M3 still needs the broader manual source-support audit, beginner-comprehension
proof, and media decision required by the plan. This M2 review does not claim
manual proof completion, optional media readiness, final verification, branch
readiness, PR readiness, hosted CI success, or completion of M3-M4.
