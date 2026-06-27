# Test Spec: Content Schema Foundation

## Status

draft

## Related spec and plan

- Spec: `specs/content-schema.md`
- Spec review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r3.md`
- Plan: `docs/plans/2026-06-26-content-schema-foundation.md`
- Plan review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/plan-review-r2.md`
- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-26-repository-native-reviewed-content.md`

## Testing strategy

The implementation should prove the content contract before any public UI, CMS, AI layer, or large exercise library exists.

- Unit tests cover validator argument parsing, rule helpers, controlled enums, locale checks, transition checks, review-routing classification, report redaction, and privacy-scan exit codes.
- Integration tests run `tools/validation/validate_content.py` against fixture directories that combine cards, taxonomy, media metadata, review events, audit events, policy fixtures, and generated output.
- Smoke tests prove the repository scaffold can validate the source tree and produce deterministic reports without stack traces before the full library exists.
- End-to-end tests are limited to local content-pipeline runs from repository source to generated public content; no browser or deployed app exists in this slice.
- Contract tests assert public schema behavior: valid records pass, invalid records fail with expected error codes, and generated output contains only publication-eligible content.
- Migration tests cover `locales.en` to `locales.en-US`, locale conflicts, future locale rejection before approved taxonomy extension, schema version checks, and breaking-change notes.
- Manual checks are limited to artifact state consistency and human review of generated public example content for source-of-truth boundaries.

Primary local validation commands:

```sh
python3 -m unittest discover -s tests
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json
python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --expect-invalid
python3 tools/validation/validate_content.py --source tests/fixtures/lifecycle --schemas schemas --media media --expect-mixed
python3 tools/validation/validate_content.py --source tests/fixtures/review-routing --schemas schemas --media media --expect-mixed
python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json
python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI|personal health" -- generated/
```

## Milestone and command ownership

This test spec is milestone-gated. A test, fixture, or validation command is not required to pass before its owning milestone unless explicitly marked as pre-milestone runnable.

Command classifications:

| Classification | Meaning |
| --- | --- |
| existing/configured | Command or tool already exists and is expected to run now. |
| planned until implemented | Command is part of this test contract but may not exist until its owning milestone. |
| manual-only | Proof is collected by a bounded manual procedure rather than automation. |
| release-owned | Command or proof belongs to a later release, CI, or governance slice and is not required for this implementation handoff. |

Unless otherwise stated, planned commands are allowed to be absent before their owning milestone. Once the owning milestone is reached, absence, configuration failure, fixture absence, unexpected nonzero exit, or missing evidence artifact is a test-spec failure.

### Validation command ownership

| Command ID | Command | Classification | Owner | Owning milestone | First milestone where command must pass | Allowed before owning milestone? | Expected nonzero behavior | Required evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python3 -m unittest discover -s tests` | planned until implemented | implementation milestone maintainer | M1 | M1 | yes; may fail before M1 if tests or harness do not exist | Nonzero means test failure after M1; before M1, absence is recorded as not-yet-owned. | test runner output or `generated/test-results.txt` |
| CMD2 | `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json` | planned until implemented | implementation milestone maintainer | M1 | M1 | yes; may fail before M1 if validator or source layout does not exist | Nonzero means repository source validation failure after M1; missing validator, schemas, media path, source path, or report after M1 is failure. | `generated/validation-report.json` |
| CMD3 | `python3 tools/validation/privacy_scan.py --pattern "private\|/home/\|secret\|PHI" -- generated/validation-report.json` | planned until implemented | implementation milestone maintainer | M1 | M1 | yes; may fail before M1 if helper or report does not exist | `0` means clean scan; `1` means forbidden pattern found; `2` or any execution error means scan/setup failure. | `generated/privacy-scan-report.json` or command transcript |
| CMD4 | `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --expect-invalid` | planned until implemented | implementation milestone maintainer | M2 | M2 | yes; may fail before M2 if invalid fixtures or content rules do not exist | Nonzero means invalid-fixture expectation failure after M2; missing validator or fixtures after M2 is failure. | test runner output and validation report excerpt |
| CMD5 | `python3 tools/validation/validate_content.py --source tests/fixtures/lifecycle --schemas schemas --media media --expect-mixed` | planned until implemented | implementation milestone maintainer | M3 | M3 | yes; may fail before M3 if lifecycle fixtures or rules do not exist | Nonzero means lifecycle fixture expectation failure after M3; missing lifecycle fields, reports, or fixtures after M3 is failure. | test runner output and lifecycle validation report excerpt |
| CMD6 | `python3 tools/validation/validate_content.py --source tests/fixtures/review-routing --schemas schemas --media media --expect-mixed` | planned until implemented | implementation milestone maintainer | M3 | M3 | yes; may fail before M3 if review-routing fixtures or rules do not exist | Nonzero means review-routing expectation failure after M3; missing review-tier evidence after M3 is failure. | test runner output and review-routing validation report excerpt |
| CMD7 | `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json` | planned until implemented | implementation milestone maintainer | M4 | M4 | yes; may fail before M4 if generated-output support does not exist | Nonzero means generated-output validation failure after M4; missing public output after M4 is failure. | `generated/validation-report.json` and `generated/public-content.json` |
| CMD8 | `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out /tmp/gymprimer-validation-report.json --emit-public /tmp/gymprimer-public-content.json` | planned until implemented | implementation milestone maintainer | M4 | M4 | yes; may fail before M4 if generated-output support does not exist | Nonzero means repeat generated-output validation failure after M4. | `/tmp/gymprimer-validation-report.json` and `/tmp/gymprimer-public-content.json` command transcript |
| CMD9 | `diff -u generated/public-content.json /tmp/gymprimer-public-content.json` | planned until implemented | implementation milestone maintainer | M4 | M4 | yes; may fail before M4 if generated outputs do not exist | Nonzero means deterministic generated output differs after M4. | diff output or `generated/diff-report.txt` |
| CMD10 | `python3 tools/validation/privacy_scan.py --pattern "private\|/home/\|secret\|PHI\|personal health" -- generated/` | planned until implemented | implementation milestone maintainer | M4 | M4 | yes; may fail before M4 if generated output does not exist | `0` means clean scan; `1` means forbidden pattern found; `2` or any execution error means scan/setup failure. | `generated/privacy-scan-report.json` |
| CMD11 | `rg -n "Current readiness\|Next valid skill\|Plan lifecycle state\|Status: approved\|accepted" docs/workflows.md docs/plans/2026-06-26-content-schema-foundation.md docs/architecture/system/architecture.md docs/adr/2026-06-26-repository-native-reviewed-content.md specs/content-schema.md` | planned until implemented | implementation milestone maintainer | M4 | M4 | yes; may fail before M4 if lifecycle routing has not reached final handoff | Nonzero means lifecycle state-sync evidence is missing or stale after M4. | command transcript or `generated/manual-proof/MP1-lifecycle-state-sync.md` |

Privacy scans use `privacy_scan.py` rather than plain `rg` because privacy scanning is a negative-match check. A clean scan must exit `0`; a forbidden finding exits `1`; scan/setup errors exit `2`.

### Test case milestone map

| Test ID | Test group | Owning milestone | First milestone where test must pass | Rationale |
| --- | --- | --- | --- | --- |
| T1 | Validator CLI and report contract | M1 | M1 | Establishes local validation harness, schema-version reporting, deterministic report shape, and privacy-safe output. |
| T2 | Privacy scan negative-match contract | M1 | M1 | Establishes the helper semantics required by the plan-review PR1 resolution. |
| T3 | Valid English card contract | M2 | M2 | Depends on content schema and card-shape validation. |
| T4 | Additional locale shape and accessible media | M2 | M2 | Depends on controlled locale enum and locale branch validation; required English key is `en-US`. |
| T5 | Locale canonicalization and migration blockers | M2 | M2 | Depends on locale migration and unknown-locale validation rules. |
| T6 | Controlled enum and taxonomy validation | M2 | M2 | Depends on v1 seed taxonomy and unknown-value rejection. |
| T7 | Media source-of-truth and supplemental-media constraints | M2 | M2 | Depends on media schema, SVG references, accessible text, and supplemental media rules. |
| T8 | Safety, progression, regression, and no-personalization checks | M2 | M2 | Depends on safety-language, progression, regression, and no-user-data rules. |
| T9 | Licensing and contribution provenance gates | M2 | M2 | Depends on v1 license and contribution-provenance enums. |
| T10 | Lifecycle transition and publication eligibility matrix | M3 | M3 | Depends on separate review/publication lifecycle rules. |
| T11 | Review-sensitive edits and version history | M3 | M3 | Depends on versioning, edit classification, and audit behavior. |
| T12 | Review-routing matrix and cumulative tier obligations | M3 | M3 | Depends on reviewer tier, review scope, and change-category routing rules. |
| T13 | Audit and approval event schema | M3 | M3 | Depends on lifecycle state transitions and approval-event reporting. |
| T14 | Generated public content package | M4 | M4 | Depends on all validation gates before generated output is produced. |
| T15 | Schema version, compatibility, and artifact state sync | M4 | M4 | Depends on generated-output maturity and cross-artifact lifecycle routing evidence. |
| T16 | Pilot-size validation performance | M4 | M4 | Depends on mature validator behavior and generated-output pipeline; not required before M4. |

### Milestone proof expectations

| Milestone | Required automated proof | Required manual proof | Handoff rule |
| --- | --- | --- | --- |
| M1 | CMD1, CMD2, and CMD3 pass; T1-T2 pass. | MP5 if developer-command documentation exists in this milestone. | M1 is complete only when the harness, report shape, and privacy-scan semantics are demonstrable. |
| M2 | CMD1, CMD2, CMD4, and relevant M2 tests T3-T9 pass. | MP3 if fixture privacy spot-check remains manual. | M2 is complete only when schema, locale, taxonomy, media, licensing, safety, and migration validation are executable. |
| M3 | CMD1, CMD2, CMD5, CMD6, and T10-T13 pass. | MP1 if lifecycle state synchronization cannot be fully automated yet. | M3 is complete only when lifecycle, publication eligibility, review routing, and audit-event behavior are validated. |
| M4 | CMD1, CMD7, CMD8, CMD9, CMD10, CMD11, and T14-T16 pass. | MP2 and MP4. | M4 is complete only when generated output is deterministic, source-bounded, privacy-clean, and scope-compliant. |

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T3, T4, T14 | integration | Stable card ID is asserted across locale additions and generated output. |
| R2 | T3, T5 | integration | Publishable cards require `locales.en-US`. |
| R3 | T4, T5 | integration | Additional locales use the same shape as `en-US`; `zh-Hans` is covered. |
| R4 | T3, T4 | integration | English-only publication remains valid when all English requirements pass. |
| R5 | T3, T4 | integration | Required localized card fields are validated. |
| R6 | T3, T6 | integration | Required nonlocalized taxonomy references are validated. |
| R7 | T6 | contract | Taxonomy fixtures use stable IDs. |
| R8 | T6 | integration | Unknown taxonomy IDs fail validation. |
| R9 | T7 | integration | Canonical SVG step count is enforced before publication. |
| R10 | T7 | integration | Localized accessible text is required for every published locale. |
| R11 | T7, T14 | integration | Reviewed text plus SVG steps remain source of truth. |
| R12 | T7 | integration | Supplemental media is not required for publication. |
| R13 | T7 | integration | Supplemental media cannot contradict canonical text or SVG steps. |
| R14 | T8 | integration | Plain-language disclaimer is required. |
| R15 | T8, T12 | integration | Stop signs and their review routing are checked. |
| R16 | T8 | integration | Diagnosis, treatment, cure, and rehab claims fail. |
| R17 | T8 | integration | Progressions must be optional and readiness-tied. |
| R18 | T8 | integration | Strength and mobility cards require regressions. |
| R19 | T10, T13 | contract | Review and publication states remain separate. |
| R20 | T6, T10 | unit, integration | Review-status enum and transitions are validated. |
| R21 | T6, T10 | unit, integration | Publication-status enum and transitions are validated. |
| R22 | T10, T12 | integration | Publication eligibility combines review, locale, taxonomy, safety, licensing, media, and successor gates. |
| R23 | T10 | unit, integration | Review transitions are limited to the spec table. |
| R24 | T10 | unit, integration | Publication transitions are limited to the spec table. |
| R25 | T11 | integration | Review-sensitive edits create or update versions according to status. |
| R26 | T13 | integration | Lifecycle changes emit immutable audit events with separate before/after state fields. |
| R27 | T11, T13 | integration | Published history preserves content version, reviewer identity, review date, and change summary. |
| R28 | T10, T11 | integration | Hiding does not delete history. |
| R29 | T11 | integration | Reverting to last approved version is represented and audited. |
| R30 | T1, T13 | smoke, integration | Validation output identifies failing field, reference, locale, media, or review rule. |
| R31 | T1, T2, T13 | unit, smoke | Reports and generated output avoid private contacts, PHI, secrets, credentials, and local paths. |
| R32 | T9 | integration | Content-license metadata is distinct from code licensing and includes attribution. |
| R33 | T9 | integration | DCO evidence or contribution provenance is required for public contributions. |
| R34 | T14 | integration | Generated records contain discovery fields for equipment, names, aliases, movement, muscle, and difficulty. |
| R35 | T14 | integration | Relationship fields are accepted when present and surfaced for generated output. |
| R36 | T14 | integration | Comprehension-check prompts are accepted and linked to cards. |
| R37 | T8 | integration | Exercise cards cannot encode personalized plans, diagnoses, rehab pathways, or medical screening data. |
| R38 | T1, T15 | smoke, migration | Schema version ID is present and checked. |
| R39 | T5, T15 | migration | Breaking changes require migration notes and compatibility checks. |
| R40 | T1, T2, T8 | smoke, integration | The content contract and validation flow require no PII. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 valid English exercise card | T3 | Valid `en-US` lat pulldown fixture. |
| E2 Chinese locale can be added | T4 | Adds `zh-Hans` without changing card ID or shape. |
| E3 unreviewed safety change blocks publication | T11, T12 | Safety edits trigger review expiration and required tiers. |
| E3a trainer-only mechanics change | T12 | Routes to `trainer` or `strength_coach` only. |
| E3b policy-sensitive emergency language change | T12 | Requires sports-medicine clinician policy review and blocks dependents when meaning changes. |
| E3c elevated-risk deferral | T12 | Rejects publication with `elevated_risk_policy_not_defined`. |
| E3d review-sensitive media edit | T11, T12 | Published version stays unchanged; new unpublished version requires media/mechanics review. |
| E4 video cannot become source of truth | T7 | Supplemental video requires metadata and cannot override canonical media. |
| E5 unsafe medical wording fails validation | T8 | Diagnosis and treatment claims fail. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 English content without Chinese content | T3 | integration | Valid when English requirements and reviews pass. |
| EC2 Chinese text missing SVG accessible text | T4, T7 | integration | Invalid for publishing the Chinese locale. |
| EC3 Alias-only change | T11, T12 | integration | No safety re-review unless alias introduces unsafe language. |
| EC4 Stop-sign change | T11, T12 | integration | Review-sensitive and cannot remain published without approval. |
| EC5 Deprecated taxonomy ID | T6, T15 | migration | Existing cards remain readable with migration notes. |
| EC6 Supplemental video contradiction | T7 | integration | Invalid until removed or reconciled. |
| EC7 Mobility drill implies pain treatment | T8 | integration | Invalid as diagnosis or rehab-adjacent claim. |
| EC8 Reviewer leaves project | T13 | integration | Historical records remain visible; future edits need current reviewer evidence. |
| EC9 Published version receives review-sensitive edit | T11 | integration | Public version remains unchanged; new unpublished version created. |
| EC10 Hidden approved version restored | T10 | integration | Eligibility recalculated before publication. |
| EC11 Elevated risk before policy approval | T12 | integration | Publication rejected. |
| EC12 Public card uses internal-only media | T9 | integration | Rejected with `license_not_public`. |

## Test cases

### T1. Validator CLI and report contract

- Covers: R30, R31, R38, R40, AC33, AC34
- Level: smoke
- Fixture/setup: Empty scaffolded `content/`, `schemas/`, `media/`, and a minimal schema-version fixture.
- Steps: Run the validator against the repository source tree and request `generated/validation-report.json`.
- Expected result: The command exits deterministically, writes a JSON report with schema version, counts, actionable failure records, and no stack trace.
- Failure proves: Contributors cannot run the validation gate or cannot identify field/rule failures safely.
- Automation location: `tests/test_validator_cli.py`; command `python3 -m unittest discover -s tests`.

### T2. Privacy scan negative-match contract

- Covers: R31, R40, plan PR1 resolution
- Level: unit
- Fixture/setup: `tests/fixtures/privacy_scan/clean`, `forbidden-term`, `missing-target`, and `invalid-regex`.
- Steps: Run `tools/validation/privacy_scan.py` against clean output, output containing forbidden patterns, a missing target, and an invalid regex.
- Expected result: Clean scan exits `0`; forbidden match exits `1`; missing target and invalid regex exit `2`; reports do not print raw secret-like values.
- Failure proves: Negative-match privacy scans cannot be used as reliable local or CI gates.
- Automation location: `tests/test_privacy_scan.py`.

### T3. Valid English card contract

- Covers: R1, R2, R4, R5, R6, E1, EC1, AC1
- Level: integration
- Fixture/setup: `tests/fixtures/cards/valid/en-us-lat-pulldown/` with card, taxonomy, canonical SVG metadata, review event, safety note, disclaimer, and license metadata.
- Steps: Run the validator against the fixture.
- Expected result: Validation passes; the card is publication-eligible after required review approvals; the stable card ID is preserved.
- Failure proves: The baseline `en-US` card shape cannot represent the approved MVP content contract.
- Automation location: `tests/test_card_contract.py`.

### T4. Additional locale shape and accessible media

- Covers: R1, R3, R4, R5, R10, E2, EC2, AC2, AC5, AC25
- Level: integration
- Fixture/setup: Valid English card plus `zh-Hans` branch, and an invalid variant missing Chinese SVG accessible text.
- Steps: Validate both fixtures.
- Expected result: Complete `zh-Hans` branch passes without changing card ID; missing locale-specific SVG accessible text fails for the Chinese locale.
- Failure proves: The bilingual schema is not first-class or can publish inaccessible localized media.
- Automation location: `tests/test_locale_validation.py`.

### T5. Locale canonicalization and migration blockers

- Covers: R2, R3, R8, R22, R39, AC23, AC25a, AC25b, AC25c
- Level: integration
- Fixture/setup: Invalid fixtures for bare `locales.en`, missing `locales.en-US` on a publishable card, both `locales.en` and `locales.en-US`, and `en-GB` before taxonomy extension.
- Steps: Run validator with `--expect-invalid`.
- Expected result: Bare `en` is rejected as unknown; publishable cards without `en-US` fail; `en` plus `en-US` fails with manual migration required; future English variants fail until active taxonomy extension.
- Failure proves: Locale semantics are ambiguous and SR4 can regress.
- Automation location: `tests/test_locale_migration.py`.

### T6. Controlled enum and taxonomy validation

- Covers: R6, R7, R8, R20, R21, AC3, AC22, AC23, AC24, EC5
- Level: unit
- Fixture/setup: Active `content/taxonomy/v1.json`, generated enum fixture, unknown enum fixture, unknown taxonomy reference fixture, inactive taxonomy extension fixture, and deprecated taxonomy fixture.
- Steps: Validate accepted enum values, unknown values, inactive extensions, and deprecated IDs.
- Expected result: All v1 enum values are accepted; unknown values fail; inactive extensions are unavailable; deprecated IDs remain readable only through compatibility/migration rules.
- Failure proves: Validators can accept out-of-contract values or reject valid v1 values.
- Automation location: `tests/test_taxonomy_validation.py`.

### T7. Media source-of-truth and supplemental-media constraints

- Covers: R9, R10, R11, R12, R13, E4, EC6, AC4, AC5
- Level: integration
- Fixture/setup: Valid card with three to six canonical SVG steps; invalid variants with too few steps, too many steps, missing accessible text, supplemental video without required metadata, and supplemental video contradicting canonical steps.
- Steps: Validate each media fixture.
- Expected result: Only cards with valid canonical SVG step references and accessible text pass; supplemental media is optional but must not contradict or replace canonical content.
- Failure proves: The implementation weakens the SVG-first source-of-truth media policy.
- Automation location: `tests/test_media_validation.py`.

### T8. Safety, progression, regression, and no-personalization checks

- Covers: R14, R15, R16, R17, R18, R37, R40, E5, EC7, AC6
- Level: integration
- Fixture/setup: Valid card with disclaimer, stop signs, readiness-tied progression, and regression; invalid fixtures for missing disclaimer, missing regression on strength/mobility card, automatic progression, diagnosis/treatment claims, rehab pathway, and user-specific medical screening fields.
- Steps: Validate the fixture set with expected valid and invalid outcomes.
- Expected result: Educational cards pass; diagnosis, cure, rehab, personalized prescription, unsafe progression, and missing required safety fields fail with actionable errors.
- Failure proves: The content contract allows clinical, personalized, or unsafe source content.
- Automation location: `tests/test_safety_boundaries.py`.

### T9. Licensing and contribution provenance gates

- Covers: R32, R33, AC26, AC27, AC32, EC12
- Level: integration
- Fixture/setup: Valid `cc_by` or owned content metadata; invalid `unlicensed_internal_only` media on public card; invalid `user_submitted_unreviewed` public contribution.
- Steps: Run validator with public publication checks enabled.
- Expected result: Valid content-license metadata passes; internal-only public media fails with `license_not_public`; unreviewed user-submitted content fails with `expert_review_required`.
- Failure proves: Public output can include unlicensed media or unsupported contribution provenance.
- Automation location: `tests/test_licensing_provenance.py`.

### T10. Lifecycle transition and publication eligibility matrix

- Covers: R19, R20, R21, R22, R23, R24, R28, AC7, AC8, AC9, AC12, AC13, AC14, AC15, EC10
- Level: integration
- Fixture/setup: `tests/fixtures/lifecycle/` with valid and invalid review/publication transition events.
- Steps: Validate direct `draft -> approved`, non-approved publication, approved unpublished publish, safety takedown, hidden restore, successor publish, and superseded publish attempt.
- Expected result: Invalid transitions fail with transition-specific errors; eligible approved unpublished or hidden records can publish only after eligibility recalculation; superseded records cannot publish.
- Failure proves: Publication can be confused with approval or invalid lifecycle paths can become public.
- Automation location: `tests/test_lifecycle_transitions.py`.

### T11. Review-sensitive edits and version history

- Covers: R25, R27, R28, R29, E3, E3d, EC3, EC4, EC8, EC9, AC10, AC11
- Level: integration
- Fixture/setup: Published card history fixtures with alias-only edit, stop-sign edit, media sequence edit, approved unpublished edit, hidden record, and revert event.
- Steps: Validate edit classification, resulting version records, and preserved history.
- Expected result: Review-sensitive edits to published cards create new unpublished versions; approved unpublished sensitive edits become `review_expired`; alias-only edits preserve review state unless unsafe; history and revert evidence remain auditable.
- Failure proves: Published content can be silently mutated or historical review evidence can be lost.
- Automation location: `tests/test_review_sensitive_edits.py`.

### T12. Review-routing matrix and cumulative tier obligations

- Covers: R15, R22, R23, E3, E3a, E3b, E3c, E3d, AC16, AC17, AC18, AC19, AC20, AC21, EC11
- Level: integration
- Fixture/setup: `tests/fixtures/review-routing/` with trainer-only mechanics, PT-required stop-rule change, clinician-required emergency policy change, elevated-risk card before policy approval, blocked rehab card, media-equivalence change, translation equivalence, and cumulative missing-tier case.
- Steps: Run validator with `--expect-mixed` and inspect missing review tiers and publication blockers.
- Expected result: Each change routes to the required tiers; cumulative obligations report every missing tier; elevated-risk publication fails with `elevated_risk_policy_not_defined`; `blocked_rehab` fails in v1.
- Failure proves: Tiered review obligations are nondeterministic or too weak for safety-sensitive changes.
- Automation location: `tests/test_review_routing.py`.

### T13. Audit and approval event schema

- Covers: R19, R26, R27, R30, R31, AC28, AC29, AC30, AC31, AC33
- Level: integration
- Fixture/setup: Valid and invalid audit/review event fixtures, including missing before/after state fields, combined lifecycle status, missing reviewer tier, missing scope, missing timestamp, missing digest, and private contact detail in reviewer metadata.
- Steps: Validate audit and review event fixtures.
- Expected result: Valid events pass; missing event fields fail; combined lifecycle status fails; private reviewer contact details do not appear in reports.
- Failure proves: Lifecycle evidence is not auditable or validation output can leak private data.
- Automation location: `tests/test_audit_events.py`.

### T14. Generated public content package

- Covers: R1, R11, R34, R35, R36, R38, AC32, AC34
- Level: e2e
- Fixture/setup: Minimal valid reviewed example set plus invalid draft, hidden, superseded, unlicensed, blocked, and review-expired records.
- Steps: Run validator with `--emit-public generated/public-content.json` twice against the same input, then compare outputs.
- Expected result: Generated public output includes only eligible reviewed content, includes discovery fields and optional relationships/prompts, preserves schema version, excludes raw draft source, and is byte-for-byte deterministic for the same inputs.
- Failure proves: The publication boundary can leak non-public content or produce unstable generated output.
- Automation location: `tests/test_generated_output.py`; commands in the plan validation section.

### T15. Schema version, compatibility, and artifact state sync

- Covers: R38, R39, EC5
- Level: integration
- Fixture/setup: `content-schema-v1` fixture, non-breaking optional-field fixture, breaking-change fixture without migration notes, old/new migration pair, and workflow-state files.
- Steps: Validate schema-version handling, compatibility fixtures, and run the artifact state-sync `rg` command from the plan.
- Expected result: Non-breaking additions remain readable; breaking changes fail without migration notes and compatibility fixtures; workflow artifacts route to the next expected stage.
- Failure proves: Implementers can change compatibility surfaces without migration proof or route from stale workflow state.
- Automation location: `tests/test_schema_compatibility.py` plus manual state-sync command.

### T16. Pilot-size validation performance

- Covers: Performance expectations, architecture quality requirement
- Level: smoke
- Fixture/setup: Generated or checked-in pilot-size fixture with 60 valid card records, canonical SVG metadata, taxonomy, review events, and audit records.
- Steps: Run validator against the pilot fixture on a typical developer machine and record elapsed wall time.
- Expected result: Validation completes in under 10 seconds and output remains deterministic.
- Failure proves: The repository-native validation approach may not scale to the first-release pilot set.
- Automation location: `tests/test_validation_performance.py`; skip only when the local machine cannot provide stable timing, with manual timing recorded instead.

## Fixtures and data

Create fixtures under `tests/fixtures/` with no real personal data, no private machine paths, no real reviewer contact details, no secrets, and no clinical case histories.

Required fixture groups:

- `tests/fixtures/privacy_scan/clean/`
- `tests/fixtures/privacy_scan/forbidden-term/`
- `tests/fixtures/cards/valid/en-us-lat-pulldown/`
- `tests/fixtures/cards/valid/en-us-zh-hans-lat-pulldown/`
- `tests/fixtures/invalid/locale-bare-en/`
- `tests/fixtures/invalid/missing-en-us-publishable/`
- `tests/fixtures/invalid/locale-conflict-en-and-en-us/`
- `tests/fixtures/invalid/future-locale-before-extension/`
- `tests/fixtures/invalid/unknown-taxonomy/`
- `tests/fixtures/invalid/unknown-enum/`
- `tests/fixtures/invalid/svg-too-few/`
- `tests/fixtures/invalid/svg-too-many/`
- `tests/fixtures/invalid/missing-svg-accessible-text/`
- `tests/fixtures/invalid/diagnosis-claim/`
- `tests/fixtures/invalid/missing-disclaimer/`
- `tests/fixtures/invalid/unlicensed-internal-only/`
- `tests/fixtures/invalid/user-submitted-unreviewed/`
- `tests/fixtures/lifecycle/`
- `tests/fixtures/review-routing/`
- `tests/fixtures/audit/`
- `tests/fixtures/generated-output/`
- `tests/fixtures/migration/`
- `tests/fixtures/performance/pilot-60/`

The first implementation may use JSON fixtures and Python standard-library tests as planned. Full muscle and equipment lists are not required beyond the v1 seed taxonomy unless a test explicitly needs one representative valid ID.

## Mocking/stubbing policy

- Do not mock the validator CLI in integration tests; run it against fixture directories.
- Unit tests may call rule functions directly when this makes edge failures easier to isolate.
- Do not mock file-system reads for schema, card, media, taxonomy, policy, review, or audit records in contract tests; repository-native wiring is the architecture boundary being proven.
- Do not call external scanners, hosted services, CMS APIs, AI APIs, legal systems, or CI providers in this slice.
- Privacy scanning remains the local wrapper contract. Semgrep, Gitleaks, Presidio, and OSV-Scanner are deferred unless a later reviewed slice adds them.

## Migration or compatibility tests

Migration coverage is required for:

- rejecting bare `locales.en` in v1;
- rejecting both `locales.en` and `locales.en-US` in the same source with manual resolution required;
- rejecting `en-GB` before active taxonomy extension;
- keeping English-only `content-schema-v1` cards readable when `zh-Hans` is added later;
- accepting non-breaking optional fields when absent or safely defaulted;
- rejecting breaking changes to stable fields, taxonomy IDs, lifecycle states, locale keys, or media semantics unless migration notes, old/new fixtures, and rollback guidance exist;
- keeping deprecated taxonomy IDs readable when migration notes define replacement behavior.

## Observability verification

Automated tests must verify validation reports include:

- counts of valid cards, invalid cards, warnings, and review-sensitive changes;
- card ID when applicable;
- locale branch when applicable;
- field, taxonomy type, media reference, review rule, lifecycle rule, licensing rule, or policy rule;
- machine-readable error code and actionable reason;
- separate `review_status_before`, `review_status_after`, `publication_status_before`, and `publication_status_after` for lifecycle audit output;
- approval event tier, scope, reviewer identity, timestamp, and content digest.

Reports must not collapse review and publication status into one lifecycle status.

## Security/privacy verification

Automated tests must verify:

- validation output and generated public output contain no secrets, credentials, private machine paths, private reviewer contact details, private user data, PHI, or user health profiles;
- public reviewer identity uses only a public name or public identifier;
- exercise cards do not require user accounts, user profiles, PII, or personalized health data;
- `tools/validation/privacy_scan.py` uses exit code `0` for clean, `1` for forbidden match, and `2` for setup or scanner error;
- generated output passes the planned negative-match privacy scan before milestone closeout.

## Performance checks

- Validate a 60-card pilot fixture in under 10 seconds on a typical developer machine.
- Re-run generated output with the same inputs and compare output for deterministic ordering and serialization.
- If timing is noisy locally, record the command, machine caveat, and observed time instead of claiming a hard performance pass.

## Manual proof records

Manual proof is allowed only when the proof target requires human judgment, cross-artifact consistency review, or scope interpretation that is not yet practical to automate. Manual proof records are bounded and must produce evidence artifacts.

### Manual proof index

| Proof ID | Name | Owning milestone | Evidence artifact | Required before milestone handoff? |
| --- | --- | --- | --- | --- |
| MP1 | Lifecycle-state synchronization inspection | M3 | `generated/manual-proof/MP1-lifecycle-state-sync.md` | yes, if M3 is in scope |
| MP2 | Generated-output source-boundary inspection | M4 | `generated/manual-proof/MP2-generated-output-source-boundary.md` | yes, if M4 is in scope |
| MP3 | Fixture privacy spot-check | M2 | `generated/manual-proof/MP3-fixture-privacy-spot-check.md` | yes, if M2 is in scope |
| MP4 | Scope and non-goal inspection | M4 | `generated/manual-proof/MP4-scope-non-goal-inspection.md` | yes, if M4 is in scope |
| MP5 | Developer-command documentation check | M1 | `generated/manual-proof/MP5-developer-command-documentation-check.md` | yes, if M1 documentation exists |

### MP1. Lifecycle-state synchronization inspection

| Field | Value |
| --- | --- |
| Manual proof ID | MP1 |
| Owning milestone | M3 |
| Owner | implementation milestone maintainer |
| Automation rationale | Full lifecycle transition validation is automated by T10-T13, but this proof checks that the human-readable spec, validator error messages, and generated report terminology stay synchronized. |
| Required environment | Local checkout containing `specs/content-schema.md`, `specs/content-schema.test.md`, validator output, and generated validation report. |
| Exact steps | 1. Open the lifecycle requirements in `specs/content-schema.md`. 2. Open T10-T13 in `specs/content-schema.test.md`. 3. Open `generated/validation-report.json`. 4. Confirm that `review_status`, `publication_status`, lifecycle transition names, approval-event names, and error identifiers use the same terms. 5. Record any mismatch. |
| Evidence artifact | `generated/manual-proof/MP1-lifecycle-state-sync.md` |
| Pass condition | All lifecycle and review/publication terms are consistent across spec, test spec, validator output, and generated report. |
| Failure condition | Any lifecycle term, status value, transition name, or audit-event label differs across artifacts without an explicit migration note. |
| Re-run trigger | Any change to lifecycle requirements, validator lifecycle output, approval events, or publication eligibility rules. |

### MP2. Generated-output source-boundary inspection

| Field | Value |
| --- | --- |
| Manual proof ID | MP2 |
| Owning milestone | M4 |
| Owner | implementation milestone maintainer |
| Automation rationale | T14 validates source-boundary rules mechanically, but a manual inspection is retained to catch accidental narrative claims that generated output came from non-reviewed, external, AI-generated, or private sources. |
| Required environment | Local checkout after generated output has been produced; access to `content/`, `media/`, `schemas/`, `generated/`, and validation reports. |
| Exact steps | 1. Open the generated content package and at least three generated card outputs. 2. Trace each generated output back to repository-native source files. 3. Confirm that generated output does not cite private files, local absolute paths, external web sources, AI chat text, or unreviewed reviewer notes. 4. Record inspected files and source paths. |
| Evidence artifact | `generated/manual-proof/MP2-generated-output-source-boundary.md` |
| Pass condition | Every inspected generated output traces only to approved repository-native content, schema, media metadata, or reviewed fixture sources. |
| Failure condition | Any inspected generated output depends on private notes, local absolute paths, external web content, AI-generated source text, or unreviewed source material. |
| Re-run trigger | Any change to generated-output logic, source-discovery logic, content indexing, or provenance handling. |

### MP3. Fixture privacy spot-check

| Field | Value |
| --- | --- |
| Manual proof ID | MP3 |
| Owning milestone | M2 |
| Owner | implementation milestone maintainer |
| Automation rationale | Privacy scans catch configured patterns, but manual review is retained for early fixtures to detect realistic personal data, private reviewer details, or health narratives that do not match configured patterns. |
| Required environment | Local checkout containing `tests/fixtures/`, `content/`, `media/`, and `generated/validation-report.json`. |
| Exact steps | 1. Review all positive and negative fixtures added in the milestone. 2. Confirm fixtures use synthetic names, synthetic IDs, and non-personal examples. 3. Confirm fixtures do not contain real contact details, private reviewer identities, real health histories, PHI-like narratives, secrets, or local absolute paths. 4. Record fixture paths inspected. |
| Evidence artifact | `generated/manual-proof/MP3-fixture-privacy-spot-check.md` |
| Pass condition | Inspected fixtures contain only synthetic, non-sensitive, repository-safe content. |
| Failure condition | Any fixture contains realistic personal data, real contact data, secrets, private reviewer details, local private paths, PHI-like narratives, or unexplained sensitive text. |
| Re-run trigger | Any new or modified fixture containing names, reviewer metadata, safety text, health-related text, provenance fields, or generated-output examples. |

### MP4. Scope and non-goal inspection

| Field | Value |
| --- | --- |
| Manual proof ID | MP4 |
| Owning milestone | M4 |
| Owner | implementation milestone maintainer |
| Automation rationale | Scope boundaries such as no UI, no CMS, no AI source-of-truth, no legal-policy implementation, and no rehab protocol are partly semantic and need human review at handoff. |
| Required environment | Local checkout containing changed files for the implementation slice, test spec, plan, generated output, and validation reports. |
| Exact steps | 1. Review changed file paths and generated outputs. 2. Confirm the slice remains limited to repository-native content schema, fixtures, validation, lifecycle/review gates, and deterministic generated output. 3. Confirm no UI, CMS, account system, AI assistant, public content library expansion, legal-policy implementation, or rehab/injury-treatment workflow was added. 4. Record any excluded-scope file or behavior. |
| Evidence artifact | `generated/manual-proof/MP4-scope-non-goal-inspection.md` |
| Pass condition | The implemented slice stays within the approved content-schema foundation scope and does not introduce deferred or excluded product areas. |
| Failure condition | Any changed artifact introduces UI, CMS, AI source-of-truth behavior, public content operations, legal-policy machinery, account/user-data features, rehab protocols, or other excluded scope without a new approved plan. |
| Re-run trigger | Any new directory, generated output class, validator capability, content category, or source boundary that may expand scope. |

### MP5. Developer-command documentation check

| Field | Value |
| --- | --- |
| Manual proof ID | MP5 |
| Owning milestone | M1 |
| Owner | implementation milestone maintainer |
| Automation rationale | Commands can be tested automatically, but the usability and accuracy of developer-facing command documentation requires human confirmation before handoff. |
| Required environment | Local checkout containing `specs/content-schema.test.md`, validation scripts, fixtures, and any developer command documentation used by this slice. |
| Exact steps | 1. Open the command documentation. 2. Run each command listed for the current milestone exactly as documented. 3. Confirm prerequisites, paths, expected outputs, and failure semantics are stated. 4. Confirm privacy-scan commands explain negative-match semantics. 5. Record command outputs or links to generated artifacts. |
| Evidence artifact | `generated/manual-proof/MP5-developer-command-documentation-check.md` |
| Pass condition | A developer can run the milestone validation commands from the documented instructions and obtain the expected artifacts and exit behavior. |
| Failure condition | Any documented command is missing, stale, path-invalid, has unexplained nonzero behavior, omits required evidence, or misstates privacy-scan semantics. |
| Re-run trigger | Any change to validation commands, script names, fixture paths, generated output paths, or privacy-scan behavior. |

## Manual QA checklist

Manual QA for this test spec is limited to executing the formal manual proof records MP1-MP5 when their owning milestones are in scope. No additional free-form manual checklist is approved for implementation handoff.

| Checklist item | Manual proof record |
| --- | --- |
| Cross-artifact lifecycle state synchronization | MP1 |
| Generated-output source-boundary inspection | MP2 |
| Fixture privacy spot-check | MP3 |
| Scope and non-goal inspection | MP4 |
| Developer-command documentation check | MP5 |

## What not to test and why

- Do not test frontend page layout, search UI, glossary UI, quizzes, or browser accessibility in this slice; no UI exists yet.
- Do not test real trainer, physical therapist, clinician, or legal reviewer credentials; this slice validates review-event shape and tier routing only.
- Do not test final Terms of Use, Privacy Policy, incident response, or elevated-risk clinical policy wording; those require follow-on specs.
- Do not test public CI success until CI exists and an observed run is available.
- Do not test unconstrained AI answers, camera form analysis, personalized workout generation, coach dashboards, or rehab pathways; they are out of scope.
- Do not treat generated snapshots alone as sufficient proof when behavior can be asserted structurally.

## Uncovered gaps

- No implementation, test harness, schemas, fixtures, validator, or CI exists yet. This test spec defines the required proof surface for implementation rather than reporting passing tests.
- Final legal wording, content-license attribution detail, incident response, and elevated-risk clinical policy remain follow-on specs before public beta.
- Full muscle and equipment taxonomy beyond seed v1 values remains out of this slice unless required by later approved taxonomy work.

## Review-blocker resolution acceptance criteria

### TSR1 acceptance criteria

| ID | Criterion |
| --- | --- |
| TSR1-AC1 | Every validation command has a stable command ID. |
| TSR1-AC2 | Every validation command has a classification: `existing/configured`, `planned until implemented`, `manual-only`, or `release-owned`. |
| TSR1-AC3 | Every planned command names an owner. |
| TSR1-AC4 | Every planned command names an owning milestone. |
| TSR1-AC5 | Every planned command states whether it may be absent or fail before its owning milestone. |
| TSR1-AC6 | Every command states expected nonzero behavior. |
| TSR1-AC7 | Every command states required evidence output. |
| TSR1-AC8 | Every test case T1-T16 maps to M1, M2, M3, or M4. |
| TSR1-AC9 | M4-only generated-output and performance tests are not required to pass before M4. |

### TSR2 acceptance criteria

| ID | Criterion |
| --- | --- |
| TSR2-AC1 | Manual QA bullets are replaced or supplemented by stable manual proof records. |
| TSR2-AC2 | Every manual proof has a stable proof ID. |
| TSR2-AC3 | Every manual proof gives an automation rationale. |
| TSR2-AC4 | Every manual proof provides exact steps. |
| TSR2-AC5 | Every manual proof names a required environment. |
| TSR2-AC6 | Every manual proof names an evidence artifact. |
| TSR2-AC7 | Every manual proof defines pass and failure conditions. |
| TSR2-AC8 | Every manual proof names an owning milestone or stage. |
| TSR2-AC9 | Manual proof is bounded to cases where automation is impractical, semantic, or used as a cross-artifact consistency check. |

## Next artifacts

1. Test-spec-review R2 for `specs/content-schema.test.md`.
2. Implementation of M1 after test-spec review approval.
3. Code review after each implemented milestone.
4. Explain-change, final verification, and PR handoff after milestone reviews and review-resolution are complete.

## Follow-on artifacts

None yet.

## Readiness

This test spec is ready for `test-spec-review`. It is not implementation approval by itself; implementation remains blocked until the required test-spec review records approval or resolves any findings.
