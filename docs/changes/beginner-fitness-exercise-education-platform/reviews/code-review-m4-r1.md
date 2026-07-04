# Code Review: Content Schema Foundation M4 R1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m4-r1.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`, `docs/changes/beginner-fitness-exercise-education-platform/change.yaml`, `docs/plans/2026-06-26-content-schema-foundation.md`, `docs/plan.md`, `docs/workflows.md`
- Open blockers: CR-M4-1
- Next stage: review-resolution and implementation fix for M4
- Review status: changes-requested
- Material findings: CR-M4-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Reviewed milestone: M4
- Milestone closeout: blocked
- Remaining implementation milestones: M4 resolution
- Required review-resolution: yes
- Finding IDs: CR-M4-1
- Verify readiness: not-claimed

## Review Inputs

- Review surface: M4 implementation commit `fe8bba8`
- Plan: `docs/plans/2026-06-26-content-schema-foundation.md`
- Spec: `specs/content-schema.md`
- Test spec: `specs/content-schema.test.md`
- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-26-repository-native-reviewed-content.md`
- Validation evidence: `generated/test-results.txt`, `generated/validation-report.json`, `generated/public-content.json`, `generated/privacy-scan-report.json`, `generated/manual-proof/MP2-generated-output-source-boundary.md`, `generated/manual-proof/MP4-scope-non-goal-inspection.md`
- Reviewer-side checks:
  - `python3 -m unittest tests.test_generated_output_m4`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out /tmp/review-m4-validation-report.json --emit-public /tmp/review-m4-public-content.json && diff -u generated/public-content.json /tmp/review-m4-public-content.json`
  - `python3 tools/validation/privacy_scan.py --pattern '<privacy-pattern>' -- generated/`
  - `python3 -m unittest discover -s tests`

## Diff Summary

The M4 implementation adds deterministic public package emission to `tools/validation/validate_content.py`, including `--emit-public`, canonical JSON writing, public card payload shaping, discovery fields, locale payloads, relationships, and comprehension-prompt placeholders. It adds generated-output tests for deterministic filtering and a 60-card performance smoke test, writes `generated/public-content.json`, adds MP2 and MP4 manual proof records, updates local developer documentation, and records M4 validation evidence.

## Findings

### CR-M4-1 - Generated-output exclusion tests do not prove all M4 publication-boundary cases

Severity: material

Evidence:

- `tests/test_generated_output_m4.py:58` creates the M4 generated-output exclusion test.
- `tests/test_generated_output_m4.py:60` covers an unpublished draft.
- `tests/test_generated_output_m4.py:61` covers a hidden card.
- `tests/test_generated_output_m4.py:62` covers a superseded card.
- `tests/test_generated_output_m4.py:63` changes a card to `license_kind = unlicensed_internal_only`, but also leaves it `publication_status = unpublished`, so the record is excluded even if the license/publication-rights filter is broken.
- The test does not include a generated-output fixture or assertion for `review_status = review_expired`.
- The test does not include a generated-output fixture or assertion for `safety_category = blocked_rehab` or another blocked safety category.

Why this matters:

M4's test spec says T14 must prove generated public output excludes draft, hidden, superseded, unlicensed, blocked, and review-expired records. The current test proves status filtering for draft/hidden/superseded and deterministic output, but it does not prove the unlicensed, blocked, or review-expired publication-boundary cases at the generated-package layer. Because generated output is the future UI/search boundary, this is a contract proof gap even though the current eligibility predicate appears to include the right checks.

Required resolution:

- Add M4 regression coverage that isolates and proves generated output excludes each required category: draft/unpublished, hidden, superseded, unlicensed/internal-only, blocked safety category, and review-expired.
- Ensure the unlicensed case is not excluded only because of `publication_status = unpublished`; the test should prove license/publication-rights gating independently, either through direct eligibility tests or a generated-output fixture that exercises the relevant branch.
- Ensure blocked and review-expired cases are asserted at the generated-output boundary.
- Refresh generated evidence and rerun the M4 validation commands after the tests are added.

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | changes requested | Generated output includes schema version, discovery fields, relationships, and public-safe locale payloads, but the T14 proof is incomplete for required exclusion categories. |
| Test coverage | fail | T14 does not yet prove unlicensed, blocked, or review-expired generated-output exclusion. |
| Edge cases | changes requested | Status-only exclusions are covered; publication-rights, safety-blocked, and expired-review exclusions need direct proof. |
| Error handling | pass | Existing validator error behavior remains structured; reviewer-side unit and validation commands did not expose stack traces or path leakage. |
| Architecture boundaries | pass | The diff stays within repository-native source validation, generated output, tests, documentation, and workflow evidence. |
| Compatibility | pass | `--emit-public` is additive and existing validation commands still run. |
| Security/privacy | pass | Reviewer-side privacy scan over `generated/` passed and public output excludes reviewer identity fields. |
| Derived artifact currency | changes requested | Generated reports and public output are current for the implemented behavior, but evidence must be refreshed after CR-M4-1 is resolved. |
| Unrelated changes | pass | The diff is scoped to M4 generated output, local quality evidence, and workflow metadata. |
| Validation evidence | pass with coverage gap | `python3 -m unittest discover -s tests` reports 59 passing tests; the missing proof is about untested M4 exclusion branches, not failing local commands. |

## Reviewer-Side Validation

Commands run:

```sh
python3 -m unittest tests.test_generated_output_m4
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out /tmp/review-m4-validation-report.json --emit-public /tmp/review-m4-public-content.json && diff -u generated/public-content.json /tmp/review-m4-public-content.json
python3 tools/validation/privacy_scan.py --pattern '<privacy-pattern>' -- generated/
python3 -m unittest discover -s tests
```

Observed result:

- M4 generated-output tests passed.
- Repository public output reproduced byte-for-byte.
- Generated privacy scan passed.
- Full local test suite passed with 59 tests.

These checks confirm the implemented happy path and deterministic output, but they do not close CR-M4-1.

## Residual Risks

- CI is not configured, as expected by the approved plan.
- The public generated package currently contains one reviewed example card. That is acceptable for M4, but publication-boundary exclusions still need direct regression proof before final closeout.

## Milestone Handoff

M4 is not closed. The next stage is review-resolution and an M4 implementation fix for CR-M4-1, followed by code-review M4 R2.
