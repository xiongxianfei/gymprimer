# Review Resolution: Beginner Fitness Exercise Education Platform

## Status

open

## Findings

| Finding ID | Review | Severity | Required outcome | Status |
| --- | --- | --- | --- | --- |
| SR1 | [spec-review-r1](reviews/spec-review-r1.md) | major | Define unambiguous review and publication state semantics. | resolved-in-r2 |
| SR2 | [spec-review-r1](reviews/spec-review-r1.md) | major | Make tiered review obligations testable for card publication and review-sensitive edits. | resolved-in-r2 |
| SR3 | [spec-review-r1](reviews/spec-review-r1.md) | major | Add minimum controlled values or a required seed taxonomy fixture. | resolved-in-r2 |
| SR4 | [spec-review-r2](reviews/spec-review-r2.md) | major | Use one normative English locale key consistently across requirements, examples, enums, acceptance criteria, and validation behavior. | resolved-in-r3 |
| PR1 | [plan-review-r1](reviews/plan-review-r1.md) | major | Make negative-match privacy scan validation commands executable with correct pass/fail semantics. | resolved-in-plan-review-r2 |
| TSR1 | [test-spec-review-r1](reviews/test-spec-review-r1.md) | major | Add explicit command classification, owner, milestone, failure behavior, and test-to-milestone mapping. | resolved-in-test-spec-review-r2 |
| TSR2 | [test-spec-review-r1](reviews/test-spec-review-r1.md) | major | Replace free-form manual QA bullets with stable manual proof records including evidence, environment, pass/fail conditions, rationale, and owner. | resolved-in-test-spec-review-r2 |
| CR-M2-1 | [code-review-m2-r1](reviews/code-review-m2-r1.md) | major | Reject public cards using a media asset with `license_kind = unlicensed_internal_only` and prove the media-asset case. | addressed-pending-rereview |
| CR-M2-2 | [code-review-m2-r1](reviews/code-review-m2-r1.md) | major | Validate supplemental-media metadata and reject supplemental media that overrides, replaces, or contradicts canonical text/SVG steps. | addressed-pending-rereview |

## Resolution notes

- SR1 addressed in `specs/content-schema.md` by splitting lifecycle into `review_status` and `publication_status`, adding allowed transition tables, publication eligibility invariants, review-sensitive edit behavior, and separate lifecycle audit fields.
- SR2 addressed in `specs/content-schema.md` by adding a review-routing matrix, reviewer-tier semantics, cumulative review obligations, and elevated-risk default-deny behavior.
- SR3 addressed in `specs/content-schema.md` by adding minimum v1 controlled enums and taxonomy-extension behavior.
- Additional examples and acceptance criteria were added for lifecycle transitions, review routing, taxonomy validation, and audit events.
- SR4 addressed in `specs/content-schema.md` by standardizing the required English locale key to `en-US`, rejecting bare `en` in v1, adding migration conflict behavior, and adding locale-specific acceptance criteria.

`spec-review-r3` approved the revised spec with no material findings. The next stage is architecture, after normalizing `specs/content-schema.md` status from `draft` to `approved` before downstream artifacts rely on it.

`plan-review-r1` requested changes because the plan's privacy scan commands used plain `rg`, which fails when no forbidden strings are found. PR1 is addressed in `docs/plans/2026-06-26-content-schema-foundation.md` by replacing those commands with planned `tools/validation/privacy_scan.py` wrapper commands, defining negative-match exit semantics, adding wrapper fixture expectations, and deferring Semgrep/Gitleaks/Presidio to later validation hardening.

`plan-review-r2` approved the revised plan with no material findings. The next stage is test-spec.

`test-spec-review-r1` requested changes because `specs/content-schema.test.md` did not make command ownership, command milestone timing, test-to-milestone mapping, or manual-proof evidence records explicit enough for implementation handoff. The revision was applied and approved by `test-spec-review-r2`.

## Test-spec-review R1 resolution

### TSR1 - Milestone and command ownership

Resolution: addressed in `specs/content-schema.test.md` by adding a `Milestone and command ownership` section.

Changes:

- Added command classifications.
- Added command ownership table for `unittest`, `validate_content.py`, `privacy_scan.py`, generated-output determinism, and lifecycle state-sync evidence commands.
- Added owner `implementation milestone maintainer` for planned implementation commands.
- Added owning milestone and first-pass milestone for each command.
- Added pre-milestone absence/failure behavior.
- Added expected nonzero behavior and evidence artifacts.
- Added T1-T16 milestone map.
- Added milestone proof expectations for M1-M4.

Status: resolved-in-test-spec-review-r2.

### TSR2 - Manual proof records

Resolution: addressed in `specs/content-schema.test.md` by replacing free-form manual QA bullets with formal manual proof records.

Changes:

- Added MP1 lifecycle-state synchronization inspection.
- Added MP2 generated-output source-boundary inspection.
- Added MP3 fixture privacy spot-check.
- Added MP4 scope/non-goal inspection.
- Added MP5 developer-command documentation check.
- Each manual proof now includes automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, owner, and owning milestone.
- Added TSR1 and TSR2 acceptance criteria to make review-blocker closure testable.

Status: resolved-in-test-spec-review-r2.

`test-spec-review-r2` approved the revised test spec with no material findings. Implementation handoff is allowed for M1 under the approved plan. This does not claim any implementation, tests, CI, verification, PR readiness, or final closeout has completed.

## Code-review M2 R1 resolution

Status: addressed-pending-rereview.

### CR-M2-1 - Media asset public-license gate

Required outcome: Public cards must reject any media asset, including supplemental media, whose `license_kind` is `unlicensed_internal_only`, and tests must prove the media-asset case.

Safe resolution path: Add supplemental/media asset validation for `media_kind`, `license_kind`, and public-publication rights; add a regression where the card-level license is publishable but supplemental media is internal-only.

Resolution: addressed by adding supplemental-media validation in `tools/validation/validate_content.py`. The validator now checks every supplemental media item for valid `media_kind`, valid `license_kind`, and rejects `license_kind = unlicensed_internal_only` on public cards with `license_not_public`.

Tests added:

- `test_public_card_rejects_internal_only_supplemental_media_asset`
- `test_supplemental_media_unknown_media_kind_is_rejected`
- `test_supplemental_media_unknown_license_kind_is_rejected`

Evidence:

- `generated/invalid-fixture-report.json` now includes `license_not_public` for `supplemental_media[0].license_kind`.

### CR-M2-2 - Supplemental-media source-of-truth boundary

Required outcome: Supplemental media must be optional, metadata-complete when present, and unable to override, replace, or contradict canonical reviewed text/SVG steps.

Safe resolution path: Add a minimal supplemental-media contract in the validator and regression tests for missing metadata and explicit replace/override language.

Resolution: addressed by adding a minimal supplemental-media contract. Supplemental media remains optional, but when present each item must be an object with valid `media_kind`, valid `license_kind`, a title or label, and `authoritative_status = supplemental`. The validator rejects `is_source_of_truth = true`, non-supplemental authority status, and explicit replace/override/source-of-truth language in selected copy fields.

Tests added:

- `test_supplemental_media_missing_media_kind_is_rejected`
- `test_supplemental_media_missing_license_kind_is_rejected`
- `test_supplemental_media_source_of_truth_claim_is_rejected`
- `test_supplemental_media_boolean_source_of_truth_claim_is_rejected`
- `test_supplemental_media_override_language_is_rejected`
- `test_valid_supplemental_media_is_allowed`

Evidence:

- `generated/invalid-fixture-report.json` now includes `supplemental_media_missing_authority` and `supplemental_media_overrides_canonical_steps` for the invalid supplemental media fixture.

Status: ready for code-review M2 R2.
