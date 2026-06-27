# Code Review: Content Schema Foundation M2 R1

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m2-r1.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`, `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`, `docs/changes/beginner-fitness-exercise-education-platform/change.yaml`, `docs/plans/2026-06-26-content-schema-foundation.md`, `docs/plan.md`, `docs/workflows.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M2-1, CR-M2-2
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m2-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Review resolution: `docs/changes/beginner-fitness-exercise-education-platform/review-resolution.md`
- Reviewed milestone: M2
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M2, M3, M4
- Required review-resolution: yes
- Finding IDs: CR-M2-1, CR-M2-2
- Verify readiness: not-claimed

## Review Inputs

- Review surface: commit `089cfe6` (`M2: validate card content contract`)
- Plan: `docs/plans/2026-06-26-content-schema-foundation.md`
- Spec: `specs/content-schema.md`
- Test spec: `specs/content-schema.test.md`
- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-26-repository-native-reviewed-content.md`
- Validation evidence: `generated/test-results.txt`, `generated/validation-report.json`, `generated/invalid-fixture-report.json`, `generated/privacy-scan-report.json`, `generated/manual-proof/MP3-fixture-privacy-spot-check.md`

## Diff Summary

M2 expands the M1 validator into executable card content validation:

- Adds `content/taxonomy/v1.json`, one example lat pulldown card, and three canonical SVG examples.
- Updates schema summary files for card, taxonomy, and media contract fields.
- Extends `tools/validation/validate_content.py` with locale, enum, taxonomy, canonical SVG, disclaimer, safety-claim, licensing, provenance, and review-metadata checks.
- Adds `tests/test_content_contract_m2.py` plus one invalid fixture tree.
- Updates generated validation evidence and workflow routing metadata for M2 review handoff.

## Findings

## Finding CR-M2-1

- Finding ID: CR-M2-1
- Severity: major
- Location: `tools/validation/validate_content.py:499`; `tests/test_content_contract_m2.py:264`; `specs/content-schema.md:483`
- Evidence: AC26 requires a public card using a media asset with `license_kind = unlicensed_internal_only` to be rejected with `license_not_public`. The implementation checks only the top-level card `license.license_kind` at `tools/validation/validate_content.py:499-510`; `supplemental_media` is not inspected anywhere. The test named `test_unlicensed_internal_only_asset_is_rejected` mutates the card-level license at `tests/test_content_contract_m2.py:264-268`, so it does not prove media-asset behavior. A throwaway validator probe with `supplemental_media: [{ "media_kind": "video", "license_kind": "unlicensed_internal_only" }]` exited `0` and reported the card as valid.
- Required outcome: Public cards must reject any media asset, including supplemental media, whose `license_kind` is `unlicensed_internal_only`, and the test must prove the media-asset case rather than only the card-level content-license case.
- Safe resolution path: Add explicit supplemental/media asset validation that iterates media references, validates `media_kind` and `license_kind` against v1 enums, and emits `license_not_public` for public cards using internal-only media assets. Add a regression fixture/test where the top-level card license is public-safe but a supplemental media asset is internal-only.
- needs-decision rationale: none

## Finding CR-M2-2

- Finding ID: CR-M2-2
- Severity: major
- Location: `tools/validation/validate_content.py:473`; `tests/test_content_contract_m2.py:220`; `specs/content-schema.md:101`; `specs/content-schema.test.md:123`
- Evidence: R13 says supplemental media must not override, contradict, or replace reviewed text or canonical SVG steps. T7 requires invalid variants for supplemental video without required metadata and supplemental video contradicting canonical steps. The implementation validates canonical SVG references at `tools/validation/validate_content.py:473-498` but never validates `supplemental_media`, and the M2 media tests at `tests/test_content_contract_m2.py:220-247` cover SVG step count and accessible text only. A throwaway validator probe with supplemental video copy claiming it replaces the SVG steps exited `0` and reported the card as valid.
- Required outcome: Supplemental media must remain optional, but when present it must have required metadata and must not claim to override, replace, or contradict canonical reviewed text/SVG steps.
- Safe resolution path: Define a minimal M2 supplemental-media contract in the validator, such as required `media_kind`, `license_kind`, and non-authoritative status/copy fields; reject records that mark themselves as source of truth or contain override/replace language. Add regression tests for missing supplemental-media metadata and explicit replace/override language.
- needs-decision rationale: none

## Checklist Coverage

| Check | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | block | CR-M2-1 and CR-M2-2 show gaps against AC26/R13/T7. Other reviewed M2 areas align with locale, enum, taxonomy, canonical SVG count/text, disclaimer, diagnosis-claim, provenance, and review-metadata requirements. |
| Test coverage | block | Tests cover many M2 negatives, but the media-asset license and supplemental-media contradiction cases required by AC26/T7 are not covered. |
| Edge cases | block | Named media edge cases EC6 and EC12 are not directly proven. |
| Error handling | pass | Validator returns `1` for validation findings, `2` for missing paths/I/O errors, and writes structured JSON reports without stack traces. |
| Architecture boundaries | pass | Source content, taxonomy, media, schemas, validation tools, generated reports, and workflow evidence remain separated and repository-native. |
| Compatibility | pass | Locale aliases are handled via explicit `en-US`/`zh-Hans` enum behavior, and CLI aliases preserve recorded command shapes. |
| Security/privacy | pass | Generated reports do not include local absolute paths; MP3 records fixture inspection; privacy scan evidence is present. The media-license gap is tracked separately as CR-M2-1. |
| Derived artifact currency | pass | Generated validation, invalid-fixture, privacy, and test-result reports correspond to the M2 handoff commands. |
| Unrelated changes | pass | The diff is scoped to M2 content/schema/test/evidence plus routing metadata. |
| Validation evidence | concern | The recorded M2 commands pass, but passing evidence does not cover the missing supplemental-media cases. |

## No-Finding Rationale

Not applicable; material findings were recorded.

## Residual Risks

- Stop-sign coverage for emergency-like symptoms is still narrow in M2 and should be watched during review-resolution or M3 review-routing work. The current material findings focus on direct, demonstrable M2 media-contract gaps.
- CI is not configured, as expected by the approved plan.

## Milestone Handoff

M2 remains open and moves to `resolution-needed`. The next stage is `review-resolution` for CR-M2-1 and CR-M2-2. No automatic downstream handoff to M3 is allowed until M2 is fixed, rerun, and re-reviewed.
