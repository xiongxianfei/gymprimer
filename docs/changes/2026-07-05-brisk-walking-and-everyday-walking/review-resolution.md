# Review Resolution: Brisk Walking and Everyday Walking Guidance

## Status

closed

## Closeout status

closed

All material findings have final dispositions.
No finding has `needs-decision`.
`review-log.md` records the same-stage or owner-approved follow-up reviews that closed each material finding.
`change.yaml` lists `open_findings: []`.

## Resolution overview

| Finding | Final disposition | Closing evidence |
| --- | --- | --- |
| PR-WALK-1 | accepted | Proposal-review R2 approved the revised proposal and confirmed Option C, both page paths, and `basic_cardio_activity` are decisions rather than open questions. |
| SR-WALK-IMG-1 | accepted | Proposal-review R3 approved the required-image proposal amendment, and spec-review R3 approved the amended spec that matches it. |

## Findings

| Finding | Status | Disposition | Resolution notes |
| --- | --- | --- | --- |
| PR-WALK-1 | closed | accepted | Proposal-review R2 confirmed the revision resolves the inconsistency. The proposal keeps Option C, `exercises/brisk-walking.md`, `principles/everyday-walking.md`, and `basic_cardio_activity` as decisions while downstream spec decides only contract details. |
| SR-WALK-IMG-1 | closed | accepted | Proposal-review R3 accepted the amended proposal requiring brisk-walking movement and muscle-attention images. Spec-review R3 confirmed the amended spec now matches the accepted proposal and the approved exercise-image standard. |

## Validation

Local validation after the proposal revision:

- `python tools/checks/check_privacy.py docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md` passed.

Review closeout:

- `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r2.md` recorded an approved R2 review with no material findings.

Review closeout:

- `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r2.md` recorded changes requested with SR-WALK-IMG-1 open.
- `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r3.md` accepted the amended proposal. Spec re-review is required before closing SR-WALK-IMG-1.
- `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r3.md` approved the amended spec and closed SR-WALK-IMG-1.

Verification hardening:

- `python3 tools/checks/check_privacy.py docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml` passed during final verify.
