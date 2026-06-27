# Plan: Content Schema Foundation

## Status

- Status: draft
- Plan lifecycle state: draft
- Terminal disposition: not-applicable

## Purpose / big picture

Implement the repository-native content foundation described by the approved content schema and architecture. The first implementation slice should create the source layout, machine-readable schema contracts, validator CLI, fixtures, and generated-output boundary needed to prove GymPrimer can validate beginner exercise cards before any public UI, CMS, AI, or large content library exists.

This plan sequences implementation only. It does not revisit product direction, safety policy, legal language, UI/search behavior, or the exact first 40-60 exercise list.

## Source artifacts

- Proposal: `../proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
- Spec: `../../specs/content-schema.md`
- Spec review: `../changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r3.md`
- Architecture: `../architecture/system/architecture.md`
- Architecture review: `../changes/beginner-fitness-exercise-education-platform/reviews/architecture-review-r1.md`
- ADR: `../adr/2026-06-26-repository-native-reviewed-content.md`
- Test spec: `../../specs/content-schema.test.md`

## Context and orientation

The repository currently has governance, proposal, spec, architecture, and review artifacts but no implementation source tree, schemas, fixtures, tests, package manifest, CI, or validator. The approved architecture chooses repository-native reviewed content as the source of truth and generated content as non-authoritative output.

Implementation should establish these architecture areas:

- `schemas/` for machine-readable contracts.
- `content/cards/`, `content/taxonomy/`, `content/policies/`, and `content/audit/` for reviewed source data and lifecycle events.
- `media/svg/` and `media/supplemental/` for canonical and supplemental media metadata.
- `tools/validation/` for the validator CLI and rule modules.
- `tests/` for fixtures and regression coverage.
- `generated/` for deterministic publication output and validation reports.

Planning choice for the first slice: use JSON fixtures and Python standard-library validation tooling unless implementation discovers a hard blocker. This avoids adding a package manager or third-party dependency before the repository has any executable baseline. YAML, JSON Schema libraries, TypeScript, or a CMS adapter can be proposed later if the first validator becomes too constrained.

Privacy scanning is a negative-match validation check. It passes only when the scan completes successfully and no forbidden pattern is found. It fails when a forbidden pattern is found or when the scan cannot complete. The first implementation owns that contract in `tools/validation/privacy_scan.py`; open-source scanners such as Semgrep, Gitleaks, or Presidio are deferred validation-hardening layers unless a later reviewed slice adds them as pinned tooling dependencies with in-repository config, tests, license tracking, and redacted reports.

## Non-goals

- Do not build the frontend, search UI, glossary UI, quizzes, analytics, CMS integration, authentication, hosting, or AI layer.
- Do not create the full 40-60 card launch library.
- Do not define final legal Terms of Use, Privacy Policy, incident response, or elevated-risk clinical policy.
- Do not accept public community video as canonical media.
- Do not collect user accounts, user profiles, PHI, or personalized workout inputs.
- Do not bypass plan-review, test-spec, test-spec-review, code-review, or verification gates.

## Requirements covered

- R1-R5: M1 and M2 define card identity, locale structure, and required localized fields.
- R6-R8: M1 and M2 define taxonomy fixtures and unknown-taxonomy validation.
- R9-R13: M2 covers canonical SVG references, accessible text, and supplemental-media constraints.
- R14-R18: M2 covers disclaimer, stop-sign, no-diagnosis, progression, and regression validation.
- R19-R29: M3 covers lifecycle states, transitions, publication eligibility, review-sensitive edits, history, hiding, and reverting.
- R30-R31: M1-M3 cover validation error shape and privacy-safe output.
- R32-R33: M2 covers licensing metadata and contribution provenance.
- R34-R36: M4 covers generated discovery fields and comprehension-check placeholders without building UI.
- R37: M2 covers prohibited personalized, diagnosis, rehab, and user-health fields.
- R38-R39: M1 and M4 cover schema versioning, migration notes, and compatibility fixtures.
- R40: M1-M4 keep the content contract usable without PII.
- AC1-AC7: M2 covers valid card, locale branch, taxonomy/media/safety/review-metadata failures.
- AC8-AC15: M3 covers lifecycle and publication-state behavior.
- AC16-AC21: M3 covers review-routing behavior.
- AC22-AC25c: M2 covers enum, locale, taxonomy-extension, and locale-migration behavior.
- AC26-AC27: M2 covers public licensing and contribution-provenance blockers.
- AC28-AC31: M3 covers audit and approval-event fields.
- AC32-AC34: M1-M4 cover content-license metadata, privacy-safe validation output, and architecture-aligned storage/validation/publication boundaries.

## Current Handoff Summary

- Current milestone: M2
- Current milestone state: planned
- Last reviewed milestone: M1
- Review status: plan-review-r2 approved; test-spec-review-r2 approved
- Remaining in-scope implementation milestones: M2, M3, M4
- Next stage: implement
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M1 is closed after clean code review, but M2-M4 have not started.

## Milestones

### M1. Repository Scaffold, Schema Shells, and Validator Harness

- Milestone state: closed
- Goal: Create the repository-native source layout and a runnable validation harness with schema-version awareness, deterministic report shape, fixture discovery, and privacy-safe error output.
- Requirements: R1, R30, R31, R38, R40, AC33, AC34
- Files/components likely touched:
  - `schemas/`
  - `content/cards/`
  - `content/taxonomy/`
  - `content/policies/`
  - `content/audit/`
  - `media/svg/`
  - `media/supplemental/`
  - `tools/validation/`
  - `tests/`
  - `generated/`
- Dependencies:
  - Approved spec and architecture remain unchanged.
  - Python 3 is available in the local environment.
- Tests to add/update:
  - Unit tests for validator CLI argument parsing, fixture loading, deterministic report fields, schema version detection, and privacy-safe error output.
  - Smoke fixture proving an empty draft source tree reports actionable missing-content or no-content status without stack traces.
- Implementation steps:
  - Create source directories with placeholder README files where empty directories need to be retained.
  - Add initial JSON schema-shape documents or schema notes for card, taxonomy, media metadata, review event, audit event, and validation report records.
  - Add `tools/validation/validate_content.py` as the single local validation entry point.
  - Add `tools/validation/privacy_scan.py` with exit code `0` for no forbidden pattern found, `1` for forbidden pattern found, and `2` for scanner/setup errors such as missing path or invalid regex.
  - Add reusable validation report helpers that emit card ID, locale, field or rule, code, and reason without local machine paths or private details.
  - Add basic `unittest` coverage for CLI and report behavior.
  - Add privacy-scan fixtures for clean output, forbidden term, missing target, and invalid regex.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
  - `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" -- generated/validation-report.json`
- Expected observable result: A contributor can run one validator command and receive a deterministic validation report even before full content rules are implemented.
- Commit message: `M1: scaffold content validation foundation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Validator scaffolding could grow into an unreviewed schema design.
  - Empty directory handling may be inconsistent across Git.
- Rollback/recovery:
  - Revert the scaffold commit; no public content or generated output should depend on it yet.

### M2. Content, Taxonomy, Locale, Media, Licensing, and Safety Validation

- Milestone state: planned
- Goal: Implement card-shape validation for required localized fields, controlled enums, taxonomy references, locale migration rules, canonical SVG references, accessible text, licensing metadata, contribution provenance, and basic safety-language blockers.
- Requirements: R1-R18, R30-R33, R37-R40, AC1-AC7, AC22-AC27, AC32-AC34
- Files/components likely touched:
  - `schemas/card.schema.json`
  - `schemas/taxonomy.schema.json`
  - `schemas/media.schema.json`
  - `content/taxonomy/v1.json`
  - `content/cards/examples/`
  - `media/svg/examples/`
  - `tools/validation/`
  - `tests/fixtures/`
  - `tests/`
- Dependencies:
  - M1 validator harness.
- Tests to add/update:
  - Valid `en-US` lat pulldown fixture.
  - Valid `zh-Hans` branch shape fixture.
  - Invalid bare `locales.en` fixture.
  - Invalid missing `locales.en-US` publishable fixture.
  - Invalid `en` plus `en-US` migration conflict fixture.
  - Unknown taxonomy, unknown enum, unsupported future locale, too few SVG steps, too many SVG steps, missing accessible text, diagnosis claim, missing disclaimer, `unlicensed_internal_only`, and `user_submitted_unreviewed` fixtures.
- Implementation steps:
  - Encode v1 controlled enums from the approved spec.
  - Add seed taxonomy fixture for v1 enums and minimum movement/equipment values.
  - Implement locale validation and migration-conflict checks.
  - Implement card required-field validation for publishable records.
  - Implement canonical SVG step count and accessible-text checks.
  - Implement safety text blockers for diagnosis/treatment claims and required disclaimer presence.
  - Implement licensing and contribution-provenance blockers.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
  - `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --expect-invalid`
- Expected observable result: Fixtures prove the validator accepts valid v1 card shape and rejects the spec-defined taxonomy, locale, media, safety, licensing, and provenance failures.
- Commit message: `M2: validate card content contract`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Safety-language detection may be too broad or too narrow if implemented as simple text checks.
  - Full muscle taxonomy may be mistaken as in scope.
- Rollback/recovery:
  - Revert M2 and keep M1 scaffold. If only one rule is faulty, disable that rule behind an explicit failing fixture and record a review-resolution task before proceeding.

### M3. Lifecycle, Review Routing, Publication Eligibility, and Audit Validation

- Milestone state: planned
- Goal: Implement lifecycle state validation, allowed transitions, review-sensitive edit handling, review-routing matrix checks, publication eligibility, audit-event schema checks, and digest-scoped approval behavior.
- Requirements: R19-R29, R30-R31, R38-R40, AC8-AC21, AC28-AC31, AC33-AC34
- Files/components likely touched:
  - `schemas/review-event.schema.json`
  - `schemas/audit-event.schema.json`
  - `content/audit/examples/`
  - `content/policies/review-routing-v1.json`
  - `tools/validation/`
  - `tests/fixtures/lifecycle/`
  - `tests/fixtures/review-routing/`
  - `tests/`
- Dependencies:
  - M1 validator harness.
  - M2 enum and card validation.
- Tests to add/update:
  - Direct `draft -> approved` rejection.
  - Non-approved publication rejection with `review_not_approved`.
  - Approved unpublished publish success.
  - Review-sensitive edit to published card creates new unpublished version and leaves published version unchanged.
  - Approved unpublished review-sensitive edit becomes `review_expired`.
  - Safety takedown to `hidden`.
  - Hidden restore only after eligibility recheck.
  - Superseded publish rejection.
  - Trainer-only, PT-required, clinician-required, elevated-risk, blocked-rehab, and cumulative missing-tier fixtures.
  - Audit before/after field coverage and approval event digest coverage.
- Implementation steps:
  - Implement review and publication status enums and transition checks.
  - Implement publication eligibility calculation.
  - Encode the review-routing matrix as data, not hard-coded prose scattered through validation rules.
  - Implement review event validation by tier, scope, reviewer identity, timestamp, and content digest.
  - Implement audit event validation with separate review/publication before and after fields.
  - Implement elevated-risk default-deny and `blocked_rehab` public publication blocker.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`
  - `python3 tools/validation/validate_content.py --source tests/fixtures/lifecycle --schemas schemas --media media --expect-mixed`
  - `python3 tools/validation/validate_content.py --source tests/fixtures/review-routing --schemas schemas --media media --expect-mixed`
- Expected observable result: Publication eligibility is reproducible from source records, current content digests, review events, policy state, licensing, and lifecycle state.
- Commit message: `M3: validate lifecycle and review gates`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Content digest computation may be unstable if it includes non-semantic field order or generated metadata.
  - Review-routing rules may accidentally encode domain policy that belongs in a later safety-governance spec.
- Rollback/recovery:
  - Revert M3 while preserving M1-M2. If digest instability is the issue, freeze canonical serialization and rerun fixtures before restoring publication eligibility checks.

### M4. Generated Output, Example Content Set, Developer Documentation, and Local Quality Gate

- Milestone state: planned
- Goal: Produce deterministic generated publication output for a small reviewed example set, document the local validation workflow, and prepare the repository for later CI without claiming CI exists.
- Requirements: R30-R36, R38-R40, AC1-AC2, AC32-AC34
- Files/components likely touched:
  - `generated/`
  - `content/cards/examples/`
  - `content/taxonomy/`
  - `content/policies/`
  - `media/svg/examples/`
  - `tools/validation/`
  - `tests/`
  - `README.md` or a focused docs file if needed
- Dependencies:
  - M1-M3 closed or explicitly revised.
- Tests to add/update:
  - Generated output snapshot or structural fixture for valid example content.
  - Deterministic rerun test proving identical input produces identical generated output.
  - Discovery-field fixture for equipment, aliases, movement pattern, muscle, and difficulty.
  - Privacy scan fixture for validation output.
- Implementation steps:
  - Add one minimal valid example exercise card and associated media/taxonomy/review/audit fixtures.
  - Generate publication-ready structured output from validated content.
  - Ensure generated output excludes draft, hidden, superseded, invalid, and blocked content.
  - Document exact local validation commands and known no-CI gap.
  - Add a lifecycle state-sync check that verifies spec, architecture, ADR, plan, and workflow metadata agree before downstream handoff.
- Validation commands:
  - `python3 -m unittest discover -s tests`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json`
  - `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out /tmp/gymprimer-validation-report.json --emit-public /tmp/gymprimer-public-content.json`
  - `diff -u generated/public-content.json /tmp/gymprimer-public-content.json`
  - `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI|personal health" -- generated/`
  - `rg -n "Current readiness|Next valid skill|Plan lifecycle state|Status: approved|accepted" docs/workflows.md docs/plans/2026-06-26-content-schema-foundation.md docs/architecture/system/architecture.md docs/adr/2026-06-26-repository-native-reviewed-content.md specs/content-schema.md`
- Expected observable result: A reviewer can inspect source fixtures, run validation locally, and see deterministic public generated content only for eligible reviewed content.
- Commit message: `M4: emit validated content package`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Generated output snapshots can become noisy if record ordering is not canonical.
  - Example content may be mistaken for clinically reviewed public content.
- Rollback/recovery:
  - Revert generated-output and example-content changes while preserving validator rules. Mark example fixtures as test-only if review status is disputed.

## Validation plan

- `python3 -m unittest discover -s tests`: run all local validator and fixture tests once tests exist.
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`: validate repository source content.
- `python3 tools/validation/validate_content.py --source tests/fixtures/invalid --schemas schemas --media media --expect-invalid`: prove invalid fixtures fail for expected reasons.
- `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json --emit-public generated/public-content.json`: prove generated public output is gated by validation.
- `diff -u generated/public-content.json /tmp/gymprimer-public-content.json`: prove deterministic generated output when run twice against the same input.
- `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI|personal health" -- generated/`: check generated validation/public output for obvious forbidden private data leakage; exit `0` means the scan completed and no forbidden pattern was found.
- `rg -n "Current readiness|Next valid skill|Plan lifecycle state|Status: approved|accepted" docs/workflows.md docs/plans/2026-06-26-content-schema-foundation.md docs/architecture/system/architecture.md docs/adr/2026-06-26-repository-native-reviewed-content.md specs/content-schema.md`: artifact lifecycle state-sync check before downstream handoff.

## Risks and recovery

- Risk: The validator becomes a custom schema language that is hard to maintain.
  - Recovery: Keep rules data-driven where possible, isolate rule modules by spec area, and add fixture coverage before broadening.
- Risk: JSON-only first implementation frustrates future authoring ergonomics.
  - Recovery: Treat JSON as the initial source format only; add YAML or CMS adapters later through architecture/spec updates if needed.
- Risk: Safety-language validation overreaches into clinical policy.
  - Recovery: Implement only spec-defined blockers and route deeper safety decisions to the safety/governance spec.
- Risk: Generated output is treated as editable source.
  - Recovery: Document generated output as non-authoritative and make validator reruns overwrite it deterministically.
- Risk: No CI exists during initial implementation.
  - Recovery: Require local validation commands in every milestone and route CI setup through `ci-maintenance` once the validator exists.
- Risk: Open-source scanners are added prematurely and expand the first implementation slice.
  - Recovery: Keep PR1 resolved by the local `privacy_scan.py` contract. Add Semgrep for configurable forbidden-pattern rules, Gitleaks for secret scanning, or Presidio for PII/PHI-like detection only in a later reviewed validation-hardening slice with pinned versions, repository config, fixture coverage, license tracking, vulnerability checks, and redacted reports.

## Dependencies

- Plan review must approve this plan before implementation starts.
- Test specification and test-spec review must define proof coverage before implementation starts.
- Python 3 must be available locally for the initial validator approach.
- No package manager or CI is assumed.
- Safety/governance, contribution/licensing, and UX/search specs remain follow-on artifacts and must not be silently implemented in this slice.

## Progress

- 2026-06-26: Created plan after approved spec-review-r3 and architecture-review-r1. Normalized architecture status to `approved` and ADR status to `accepted` before relying on them.
- 2026-06-27: Added `../../specs/content-schema.test.md` and routed the next stage to test-spec-review.
- 2026-06-27: `test-spec-review-r1` requested revisions for command/milestone ownership and manual-proof evidence records.
- 2026-06-27: Revised `../../specs/content-schema.test.md` to address TSR1 and TSR2; routed next stage to test-spec-review R2.
- 2026-06-27: `test-spec-review-r2` approved the proof map and allowed implementation handoff for M1.
- 2026-06-27: M1 implementation started. Scope is limited to repository scaffold, schema notes, validator CLI/report contract, privacy scan helper, M1 tests, generated validation report, and change-local metadata/reasoning.
- 2026-06-27: M1 implementation completed and moved to review-requested. Added repository scaffold, schema shells, `validate_content.py`, `privacy_scan.py`, M1 unit tests, generated validation reports, MP5 manual proof, change metadata, and durable change explanation.
- 2026-06-27: `code-review-m1-r1` recorded a clean first-pass review with no material findings. M1 closed and workflow routed to M2 implementation.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-26 | Use JSON fixtures and Python standard-library validator for the first implementation slice. | The repository has no package manager or app stack, and the approved architecture defers implementation language to planning. This minimizes dependencies while proving the content contract. | CMS-first implementation; TypeScript package setup before UI requirements exist; YAML-first implementation requiring a dependency. |
| 2026-06-26 | Split implementation into scaffold, content validation, lifecycle/review validation, and generated-output milestones. | Each slice is reviewable and maps to distinct spec/architecture risks. | One large validator milestone; starting with generated output before validation gates exist. |
| 2026-06-27 | Resolve PR1 with a local `privacy_scan.py` wrapper instead of adding OSS scanners to the first slice. | PR1 is an exit-code contract problem, not a need for a broad privacy platform. The wrapper gives stable negative-match semantics now while preserving a path to Semgrep, Gitleaks, or Presidio later. | Plain `rg` commands; immediate Semgrep/Gitleaks/Presidio adoption; vendoring scanner source code. |

## Surprises and discoveries

- No implementation, test framework, package manifest, CI, source fixtures, or generated-output convention exists yet.
- The current plan can proceed without choosing a frontend framework or hosting provider.

## Validation notes

- 2026-06-26: Plan authoring validation was limited to artifact inspection and lifecycle state checks with `sed` and `rg`; no implementation validation command exists yet.
- 2026-06-27: PR1 revision replaced plain negative-match `rg` privacy scan commands with planned `tools/validation/privacy_scan.py` wrapper commands and documented deferred OSS scanner hardening.
- 2026-06-27: M1 red test run: `python3 -m unittest discover -s tests` failed because `tools/validation/validate_content.py` and `tools/validation/privacy_scan.py` did not exist yet.
- 2026-06-27: M1 validation passed: `python3 -m unittest discover -s tests`.
- 2026-06-27: M1 validation passed: `python3 tools/validation/validate_content.py --source content --schemas schemas --media media --out generated/validation-report.json`.
- 2026-06-27: M1 validation passed: `python3 tools/validation/privacy_scan.py --pattern "private|/home/|secret|PHI" -- generated/validation-report.json`.
- 2026-06-27: MP5 manual proof recorded at `generated/manual-proof/MP5-developer-command-documentation-check.md`.

## Outcome and retrospective

- Pending. Fill after all implementation milestones and downstream reviews complete.

## Readiness

- See `Current Handoff Summary`.
- Ready for implementation of M2. Not ready for verification, PR, or final closeout until M2-M4 implementation, code reviews, review-resolution if needed, explain-change, verification, and downstream gates complete.
