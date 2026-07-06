# Code Review M2 R1: Brisk Walking and Everyday Walking Guidance

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m2-r1.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`; `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`; `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml`; `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M2
- Milestone closeout: closed
- Remaining implementation milestones: M3
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Review surface: committed branch diff at `92e3d5f M2: add walking guidance pages`.
- Tracked governing branch state: accepted proposal, approved walking spec, active test spec, reviewed plan, M1 code-review closeout, M2 validation ledger, walking pages, and tests are present in tracked branch state.
- Active plan: `docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Approved spec: `specs/brisk-walking-and-everyday-walking.md`.
- Active test spec: `specs/brisk-walking-and-everyday-walking.test.md`.
- Implementation files inspected: `exercises/brisk-walking.md`, `principles/everyday-walking.md`, and `tests/test_markdown_first_real_pages.py`.
- Validation evidence: M2 validation ledger plus review-time reruns listed below.

## Diff Summary

M2 adds the two approved walking pages and real-page coverage:

- `exercises/brisk-walking.md` teaches brisk walking as deliberate moderate-intensity cardio, includes the talk test, pace reference, `Method type: basic_cardio_activity`, 5-10 minute starter guidance, progression order, role-based muscle guidance, feel cues, walking technique, safety routing, and page-local sources.
- `principles/everyday-walking.md` teaches everyday walking as daily movement, sitting interruption, and habit-building, distinguishes it from brisk walking, links to the brisk walking page when intensity rises, includes practical examples, safety routing, and page-local sources.
- `tests/test_markdown_first_real_pages.py` adds checks for page existence, required sections, brisk/everyday distinction, method shape, safety terms, forbidden scope, source IDs, text-only media, and brisk walking muscle/feel guidance.
- Lifecycle artifacts record M2 validation and mark M2 ready for code-review.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | The two approved page paths exist; brisk walking is an exercise page and everyday walking is a principle page; both keep static educational scope and avoid excluded tracker, weight-loss, medical-program, running, hiking, treadmill, incline, and adaptive-plan framing. |
| Test coverage | pass | `tests/test_markdown_first_real_pages.py` covers BWG-T3, BWG-T4, BWG-T6, BWG-T7, and BWG-T8 surfaces; existing method and muscle tests are included in M2 validation. |
| Edge cases | pass | EC1 is covered by everyday walking not equating all walking with brisk cardio; EC2 and EC4 are covered by short brisk-walk and hills-as-later-progression wording; EC5 is covered by page-local `## Sources`; EC8 is covered by practical everyday walking examples. |
| Error handling | pass | Checker validation confirms required headings, page-local source definitions, active `basic_cardio_activity`, RED-FLAGS routing, and text-only media behavior. |
| Architecture boundaries | pass | Markdown remains the source of truth; no image, generated guidance source of truth, runtime, tracker, calculator, wearable integration, or user input flow was added. |
| Compatibility | pass | The change is additive, keeps stable existing pages, reuses existing source IDs, and does not alter `SOURCES.md` or `RED-FLAGS.md` because no compatibility edit was needed. |
| Security/privacy | pass | No secrets, private reader data, private health information, accounts, analytics, or storage were introduced; privacy scan passed. |
| Derived artifact currency | pass | No generated media or derived artifact is introduced in M2; `media/PROVENANCE.md` checker path passes with the text-only pages. |
| Unrelated changes | pass | The reviewed diff is limited to the two walking pages, M2 tests, validation ledger, and lifecycle state updates. |
| Validation evidence | pass | Review-time validation reruns passed locally; CI was not observed and is not claimed. |

## No-Finding Rationale

The implementation satisfies the M2 contract without expanding into M3.

The brisk walking page uses time, effort, repeatability, progression, and stop rules instead of sets and reps as the primary method shape. It also keeps the talk test and pace reference page-local and source-backed.

The everyday walking page remains a principle page, not an exercise method page. It includes practical walking examples and explicitly says not every step is brisk cardio.

Both pages route to `../RED-FLAGS.md`, include page-local sources, reuse indexed global source IDs, and remain text-only.

The added tests directly exercise the M2 surfaces named in the test spec, while the manual semantic source audit, beginner comprehension proof, and optional image decision correctly remain for M3.

## Review-Time Validation

| Command | Result |
| --- | --- |
| `python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md` | pass; checked 5 Markdown files |
| `python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_markdown_first_real_pages` | pass; 44 tests |
| `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | pass; 65 tests |
| `python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking` | pass; checked 16 files |

## Residual Risks

- M3 is not implemented yet; semantic source audit, beginner comprehension proof, and the optional image/no-image decision remain pending.
- CI was not observed.
- This review closes M2 only; it does not claim branch readiness, PR readiness, final verification, or CI success.

## Milestone Handoff

M2 is closed.

The next stage is implementation of M3: manual proof, optional media decision, and promotion gate.
