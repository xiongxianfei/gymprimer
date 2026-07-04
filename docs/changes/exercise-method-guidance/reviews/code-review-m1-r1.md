# Code Review M1 R1: Exercise Method Guidance

## Result

- Skill: code-review
- Status: completed
- Review status: changes-requested
- Material findings: CR-EMG-M1-1, CR-EMG-M1-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: `docs/changes/exercise-method-guidance/review-resolution.md`
- Reviewed milestone: M1
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M1 resolution, M2, M3, M4, Lifecycle Closeout
- Required review-resolution: yes
- Finding IDs: CR-EMG-M1-1, CR-EMG-M1-2
- Verify readiness: not-claimed
- Open blockers: none
- Next stage: review-resolution

## Review Inputs

- Diff/review surface: commit `473710d` (`M1: add exercise method validation and template`).
- Tracked governing branch state: exercise-method proposal, spec, architecture amendment, plan, active test spec, test-spec-review R2, and M1 implementation are tracked in commit `473710d`.
- Governing artifacts: `specs/exercise-method-guidance.md`, `specs/exercise-method-guidance.test.md`, `docs/plans/2026-07-04-exercise-method-guidance.md`, `docs/architecture/system/architecture.md`.
- Changed implementation files reviewed: `tools/checks/check_markdown_first.py`, `docs/templates/exercise-card.md`, `tests/test_exercise_method_guidance.py`, `tests/test_markdown_first_templates.py`, `specs/markdown-first-primer.md`, `specs/responsible-breadth.md`.
- Validation evidence reviewed: M1 validation notes in `docs/plans/2026-07-04-exercise-method-guidance.md` and `docs/changes/exercise-method-guidance/change.yaml`.

## Diff Summary

M1 added `## How much to do` to `docs/templates/exercise-card.md`, added visible-Markdown method validation to `tools/checks/check_markdown_first.py`, added focused method-guidance tests, added compatibility-note assertions, and updated workflow state to request code-review for M1.

## Findings

## Finding CR-EMG-M1-1 - Method heading validation accepts non-exact headings

- Finding ID: CR-EMG-M1-1
- Severity: major
- Location: `tools/checks/check_markdown_first.py:1126`, `specs/exercise-method-guidance.md:121`
- Evidence: R1 requires exercise pages updated under this spec to include a section headed exactly `## How much to do`. The validator obtains the section with `section_text(text, "## How much to do")`, which uses the shared prefix-oriented heading helper. Direct review proof showed a page with `## How much to do wrong` returned no method findings: `invalid_heading []`.
- Required outcome: The method validator must reject non-exact method headings and require the exact visible heading `## How much to do`.
- Safe resolution path: Add an exact-heading check for method guidance, or add a method-specific section extractor that matches only `^## How much to do$`. Add a focused test with a heading such as `## How much to do wrong` or `## How much to do:` and assert a stable method-section failure category.
- needs-decision rationale: none

## Finding CR-EMG-M1-2 - Required method labels can be empty

- Finding ID: CR-EMG-M1-2
- Severity: major
- Location: `tools/checks/check_markdown_first.py:1155`, `tests/test_exercise_method_guidance.py:52`, `specs/exercise-method-guidance.md:138`
- Evidence: R6 requires visible method labels or equivalent plain-language lines, and EMG-T2 says missing starter range text must fail required label/content checks. The validator only checks whether each label string appears in the section. Direct review proof showed a section containing `Beginner starting point:`, `Effort:`, `Rest:`, `Progression:`, and `Stop if:` with no content after any label returned no findings: `empty_labels []`.
- Required outcome: The method validator must require each mandatory label line to carry non-empty content, or otherwise prove equivalent plain-language content is present.
- Safe resolution path: Parse method-section lines for the required labels and fail with a stable category when a label is absent or the label line has no text after the colon. Add focused tests for empty required labels, including at least `Beginner starting point:`.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | CR-EMG-M1-1 and CR-EMG-M1-2 show R1 and R6 are not fully enforced by the new validator. |
| Test coverage | block | Existing tests cover missing labels but not non-exact headings or empty label content. |
| Edge cases | block | Named edge cases around exact section shape and missing starter range text are not directly proved. |
| Error handling | pass | Invalid method type, deferred method type, hidden-only metadata, adaptive programming, and forbidden scope language produce stable findings in focused tests. |
| Architecture boundaries | pass | The implementation keeps visible Markdown as source of truth and does not introduce hidden metadata, generated data, runtime behavior, or a taxonomy store. |
| Compatibility | pass | The checker is additive for unselected pages without method sections, and related specs point to the focused spec without duplicating enum tables. |
| Security/privacy | pass | Reviewed diff adds no user input, private data, secrets, logs, or network behavior; privacy validation is recorded as passing. |
| Derived artifact currency | pass | No generated artifact is part of M1. |
| Unrelated changes | pass | The implementation changes are scoped to exercise-method governance, template, validation, tests, and workflow state. |
| Validation evidence | concern | Recorded M1 commands are relevant and passing, but the selected tests missed the two direct proof gaps above. |

## No-Finding Rationale

No clean no-finding rationale applies because CR-EMG-M1-1 and CR-EMG-M1-2 require changes before M1 can close.

## Residual Risks

Semantic source support and beginner comprehension remain intentionally deferred to later M3/M4 proof records. This review does not claim those later obligations are satisfied.

## Handoff

M1 remains the active milestone. Set M1 to `resolution-needed`, keep remaining milestones unchanged, and route to review-resolution for CR-EMG-M1-1 and CR-EMG-M1-2 before M1 code-review re-review.
