# Test Spec Review R2: Brisk Walking Required Images

## Result

- Skill: test-spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/test-spec-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: implement
- Implementation handoff: allowed
- Stop condition: none

## Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The M4 proof map follows the approved amended spec, architecture-review R2, plan-review R2, and the M4 plan boundary without overriding the two-image brisk-walking media contract. |
| Requirement coverage | pass | BWG-R24 through BWG-R26 and BWG-R29 map to BWG-T8, BWG-T9, BWG-MP3, and M4 command IDs; earlier BWG-R1 through BWG-R23, BWG-R27, BWG-R28, and BWG-R30 remain mapped to existing M1-M3 proof. |
| Example coverage | pass | E5 maps to BWG-T8, BWG-T9, and BWG-MP3 for required movement and muscle-attention image behavior. |
| Negative and boundary coverage | pass | EC7, EC7A, and EC7B cover unsafe image wording, missing required images, and exact-anatomy muscle-image drift; scope guards keep everyday walking text-only. |
| Proof-level adequacy | pass | Automated tests cover image references, purposes, prompt/provenance wiring, page refs, and no everyday-walking image; manual proof covers visual-safety semantics that deterministic checks cannot prove. |
| Milestone mapping | pass | M4 owns the new required-image tests, manual proof, prompt records, provenance rows, visual-safety evidence, and validation commands without reopening closed M3. |
| Command validity | pass | M4 commands have stable IDs, classifications, owners, milestone ownership, first required milestone, failure behavior, zero-test behavior where applicable, evidence artifacts, and local side-effect boundaries. |
| Fixture and data design | pass | The proof map names real walking pages, local media assets, prompt records, `media/PROVENANCE.md`, and existing temporary-fixture image-standard tests. |
| Manual-proof boundary | pass | BWG-MP3 is limited to image decision and visual-safety evidence, with exact checks for form image constraints, broad muscle-attention constraints, rejected-asset notes, provenance, alt text, and residual risk. |
| Observability | pass | Failures can be traced through requirement IDs, test IDs, command IDs, asset paths, prompt-record paths, provenance rows, page refs, and manual-proof artifacts. |
| Determinism and isolation | pass | Commands are local unittest, checker, privacy, and diff checks; no network validation, publication, external link checking, or image generation is part of the review-time proof. |
| Scope and non-goals | pass | The proof map does not add trackers, calculators, personalized walking plans, medical programs, extra walking images, generated HTML, or runtime behavior. |
| Execution economics | pass | Focused M4 image and real-page commands are separated from broader regression checks, while the full focused command remains required before M4 code-review. |
| Traceability | pass | Requirement, example, edge-case, command, milestone, test, and manual proof IDs link consistently for M4 and preserve historical M1-M3 proof boundaries. |
| Implementation handoff | pass | Implementation can proceed without guessing how the required images, prompt records, provenance, visual-safety proof, and no everyday-walking image constraint will be proved. |

## Recommendation

Approve the M4 test spec for implementation handoff. This review does not start implementation, generate images, run validation commands, or claim branch readiness.
