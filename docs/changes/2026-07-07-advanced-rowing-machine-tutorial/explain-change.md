# Explain Change: Advanced Rowing Machine Tutorial

## Status

explain-change complete

## Summary

This change adds an advanced rowing-machine companion tutorial while keeping the original rowing-machine page as the beginner entry point.

The implemented slice:

- updates project vision and governance from beginner-only positioning to general-audience static education;
- records an accepted proposal, approved spec, architecture amendment, reviewed plan, and active test spec for the advanced rowing work;
- adds `exercises/rowing-machine-advanced.md` as a Markdown-first advanced literacy page;
- links to that page from `exercises/rowing-machine.md`;
- adds scoped advanced-rowing validation for page shape, media governance, force-intensity overlays, technical diagram labels, and forbidden scope;
- adds eight governed generated image assets with prompt packets and provenance rows;
- records source audit, visual-safety review, grayscale review, advanced-reader comprehension proof, and final validation evidence.

All implementation milestones M1-M4 are closed by code review.
The next lifecycle stage is final verification.

## Problem

The existing `exercises/rowing-machine.md` page taught beginner rowing setup, stroke order, muscles, common mistakes, and a simple cardio-equipment method.
It did not serve readers who already understood the beginner stroke and wanted static literacy about drag factor, monitor metrics, rhythm, force curve feedback, rate control, workout types, and benchmark-preparation boundaries.

The user also clarified that GymPrimer should not be limited to beginners.
That required updating the higher-ranked project vision and governance before relying on advanced content as in-scope.

## Decision Trail

| Stage | Decision | Source |
| --- | --- | --- |
| Vision/governance | Reposition GymPrimer as general-audience static exercise, movement, and training literacy while preserving no-coaching, no-clinical, and no-runtime boundaries. | `docs/changes/2026-07-07-general-audience-vision/explain-change.md` |
| Proposal | Choose a separate advanced companion page, keep advanced rowing as literacy rather than coaching, retain eight first-batch images, and add a force-intensity visual system. | `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md` |
| Spec | Require the advanced page path, page sections, static scope, source-backed concepts, image-rich exception, prompt packets, provenance, force-intensity constraints, and manual proof. | `specs/advanced-rowing-machine-tutorial.md` |
| Architecture | Extend the existing Markdown-first, prompt-record, provenance, and validation architecture with a scoped advanced-rowing exception. | `docs/architecture/system/architecture.md` |
| Plan | Split delivery into M1 validation scaffolding, M2 page content, M3 governed media, and M4 manual proof and closeout evidence. | `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md` |
| Test spec | Map requirements to ART-T1 through ART-T13, ART-MP1 through ART-MP4, and ART-CMD1 through ART-CMD10. | `specs/advanced-rowing-machine-tutorial.test.md` |

## Requirement Trace

| Requirement area | Implemented by |
| --- | --- |
| R1-R9, R47-R48 | Beginner page preservation, advanced page path, Markdown-only page shape, prerequisite boundary, static-literacy framing, and forbidden-scope checks. |
| R10-R19 | Advanced content explaining damper, drag factor, monitor metrics, stroke rate, force curve, workout types, benchmark boundary, and `basic_cardio_equipment` method use. |
| R20-R21 | Page-local citations plus reused source IDs in `SOURCES.md` where required. |
| R22-R32 | Eight-image scoped exception, exact asset list, one-purpose images, prompt packets, provenance rows, and force-overlay asset allow/deny rules. |
| R33-R44 | Force-intensity 0-3 relative scale, non-measurement wording, non-color cues, grayscale expectations, body-label ban, technical diagram label exception, alt text, legends, and phase explanations. |
| R45-R46 | Visual-safety and grayscale proof records. |
| R49 | Advanced-reader comprehension proof. |
| R50 | Exact validation command and outcome records before completion claims. |

## Diff Rationale By Area

| File or area | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `CONSTITUTION.md`, `VISION.md`, `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/vision/strategic-positioning.md` | Updated project positioning from beginner-only to general-audience static education. | The user explicitly rejected a beginner-only project scope, and higher-ranked governance had to allow advanced literacy before the advanced rowing page could proceed. | General-audience vision change record; source-order rules. | General-audience explain-change validation; later broad M4 Markdown/privacy checks. |
| `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md` | Recorded the advanced rowing direction, options, risks, image plan, force-intensity system, and implementation boundaries. | The repository requires durable proposal review before material content, media, and validation changes. | Proposal-review R1. | Proposal-review record and change metadata. |
| `specs/advanced-rowing-machine-tutorial.md` | Added the contract for the advanced page, image-rich exception, force-intensity overlays, technical labels, manual proof, and acceptance criteria. | Needed testable requirements before architecture, planning, validation, and content work. | Spec-review R1. | Test-spec mapping and later code reviews. |
| `docs/architecture/system/architecture.md` | Added a scoped architecture amendment for advanced-rowing Markdown, media, prompt packets, provenance, validation, and method boundaries. | The change touches content, generated media, validation, and durable workflow evidence, so architecture needed to define the allowed boundaries without adding runtime software. | Architecture-review R1. | Architecture-review R1 approved with no material findings. |
| `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`, `docs/plan.md`, `change.yaml`, `review-log.md`, `reviews/*.md`, `review-resolution.md` | Recorded workflow state, milestone handoffs, review outcomes, and CR1/CR2 resolution. | Keeps the multi-milestone change auditable and prevents stale handoff state. | Plan-review R2; test-spec-review R2; code-review R1-R5. | Review records, closed review-resolution, lifecycle validation. |
| `tools/checks/check_markdown_first.py` | Added advanced-rowing validators for required sections, prerequisites, scoped image exception, prompt packet completeness, force-overlay rules, technical label exception, forbidden media text, and forbidden page scope. | The approved contract needed automated checks for the parts that can be statically enforced. | Spec R1-R44, R47-R48; test spec ART-T1 through ART-T12. | `tests/test_advanced_rowing_machine_tutorial.py`; real-page tests; full unittest discovery. |
| `tests/test_advanced_rowing_machine_tutorial.py` | Added temporary-root contract tests for valid and invalid advanced-rowing pages, image exceptions, prompt packets, label rules, media exclusions, and forbidden scope. | Gives direct regression proof for the new checker behavior before relying on the real page. | Test spec ART-T7 through ART-T12; CR1 and CR2. | Code-review R2 accepted CR1/CR2 fixes. |
| `tests/test_markdown_first_real_pages.py` | Added real-page integration checks for the beginner link, advanced page sections, source-backed concepts, workout boundaries, media batch, prompt packets, legends, and provenance. | Proves the production Markdown and media surfaces satisfy the approved contract. | Test spec ART-T1 through ART-T6 and ART-T8 through ART-T11. | Full unittest discovery passed in M4 and code-review R5. |
| `exercises/rowing-machine.md` | Added the advanced-page link at the bottom of the beginner page. | Preserves the beginner tutorial while giving prepared readers a path to advanced literacy. | Spec R1, R4; proposal Option B. | Real-page test `test_rowing_machine_links_to_advanced_page`. |
| `exercises/rowing-machine-advanced.md` | Added the advanced companion tutorial with monitor literacy, drag factor, rhythm, force curve, stroke-rate control, static workout types, image guides, force-intensity system, phase map, safety notes, and sources. | Implements the primary user-facing improvement without turning the page into coaching, a plan, or a clinical protocol. | Spec R2-R21, R33-R44, R47-R48. | Real-page tests, source audit M2/M4, code-review R3/R5. |
| `SOURCES.md` | Added reused Concept2, British Rowing, and W3C source IDs needed by the advanced page. | Reused source IDs must appear in the source index when repository source rules require it. | Spec R20-R21. | ART-T6 and broad Markdown-first validation. |
| `media/exercises/rowing-machine-advanced/*.png` | Added eight generated first-batch advanced rowing images. | The approved image-rich exception needed distinct visuals for timing, rhythm, monitor metrics, force curve, rate ladder, damper/drag factor, power per stroke, and interval structure. | Spec R22-R24, R30-R32, R39-R44. | M3 visual-safety proof, grayscale proof, provenance checks, real-page media tests. |
| `media/prompts/exercises/rowing-machine-advanced/*.md` | Added image-instruction packets with asset paths, page references, media purposes, layers, teaching goals, visual rules, prompts, review notes, and force maps where applicable. | Generated image assets need governed prompt records before promotion. | Spec R25-R29, R33-R44. | ART-T8 through ART-T11; code-review R4. |
| `media/PROVENANCE.md` | Added approved provenance rows for all eight advanced rowing image assets. | Generated raster assets need approved provenance, prompt record links, source inputs, license assertion, page refs, and review status. | Spec R25-R26. | ART-T8; broad Markdown-first validation. |
| `manual-proof/*.md`, `source-audit-m2.md`, `validation-ledger-m4.md` | Recorded source support, visual-safety review, grayscale review, reader comprehension proof, and command ledger. | Static checks cannot fully prove visual semantics, source adequacy, or reader comprehension. | Spec R45-R50; test spec ART-MP1 through ART-MP4. | Code-review R5 clean-with-notes. |

## Tests Added Or Changed

| Test coverage | What it proves | Level |
| --- | --- | --- |
| ART-T1 and ART-T2 | The beginner page remains the entry point, the advanced page exists, required sections are present, and prerequisites are editorial rather than medical or performance eligibility. | integration |
| ART-T3 and ART-T12 | Advanced content rejects coaching, runtime product, clinical, competition-programming, personal target, and benchmark-plan drift. | contract |
| ART-T4 through ART-T6 | Damper, drag factor, monitor metrics, stroke rate, force curve, workout examples, and source IDs are present and source-backed. | integration/manual |
| ART-T7 through ART-T9 | The image-rich exception is limited to the eight approved assets and each image has prompt and provenance support. | unit/integration |
| ART-T10 and ART-T11 | Force-intensity overlays, technical label exceptions, alt text, legends, and excluded media patterns are enforced. | unit/integration/manual |
| ART-T13 | Final evidence includes exact validation commands and outcomes. | smoke |
| ART-MP1 through ART-MP4 | Manual proof covers source support, visual safety, grayscale/non-color meaning, and advanced-reader comprehension. | manual |

The test level is mixed intentionally.
Static page shape, forbidden wording, prompt packets, and provenance are enforced automatically.
Visual semantics, grayscale distinction, source adequacy, and reader comprehension are recorded as manual proof because they cannot be fully determined by a text checker.

## Validation Evidence Available Before Final Verify

Local validation recorded before this explain-change stage includes:

| Command or proof | Result |
| --- | --- |
| `python3 -m unittest discover -s tests` | pass, latest reviewer-ran result recorded 237 tests |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md exercises media/PROVENANCE.md media/prompts docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass, checked 44 Markdown file(s) |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md RED-FLAGS.md exercises media docs/changes/2026-07-07-advanced-rowing-machine-tutorial` | pass, checked 249 file(s) |
| `git diff --check` | pass |
| Source audit, visual-safety review, grayscale review, and reader comprehension proof | pass per `validation-ledger-m4.md` and code-review R5 |

Hosted CI has not been observed.
Final verification has not run yet; final verification evidence belongs in `verify-report.md`.

## Review Resolution Summary

`docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md` is closed.

| Finding group | Count | Disposition |
| --- | ---: | --- |
| Code-review R1 findings | 2 | resolved by CR1/CR2 fixes and accepted by code-review R2 |
| Open material findings | 0 | none |

Key fixes:

- CR1 added advanced-rowing media-text forbidden checks and temporary-root tests for copied PM5 UI, screenshots, logos or brand marks, identifiable people, correct/wrong badges, red pain marks, elite/race-win framing, and unsupported promises.
- CR2 extended forbidden-scope validation for calculated personal targets, personal watts or paces, full benchmark plans, competition programming, active recovery protocols, and clinical protocol wording.

## Alternatives Rejected

| Alternative | Why rejected |
| --- | --- |
| Add all advanced content directly to `exercises/rowing-machine.md` | Would overload the beginner page and weaken the beginner teaching path. |
| Create an advanced rowing program page | Too close to personalized programming, race coaching, and sport-specific competition programming. |
| Keep advanced rowing out of GymPrimer | Conflicted with the user-updated general-audience vision and missed a useful static-literacy path. |
| Use PM5 screenshots, copied UI, branded monitor graphics, or third-party photos | Conflicts with media-source, privacy, and brand/copying boundaries. |
| Use force-intensity as an exact heatmap | Would imply unsupported force, EMG, injury-risk, or correctness measurement. |
| Add `advanced_basic_cardio_equipment` | The approved scope keeps `basic_cardio_equipment` and treats advanced examples as page-level literacy. |
| Build a calculator, tracker, PM5 data app, wearable integration, video product, or coaching engine | Outside the Markdown-first static education architecture and explicit non-goals. |

## Scope Control

The change preserves the approved non-goals:

- no personalized plan;
- no adaptive programming;
- no race strategy or competition programming;
- no full benchmark plan;
- no medical judgment, treatment plan, active recovery protocol, or injury-specific protocol;
- no hosted app, runtime API, calculator, tracker, wearable integration, generated public JSON, video platform, or coaching engine;
- no borrowed screenshots, copied PM5 UI, brand marks, identifiable people, correct/wrong badges, red pain marks, elite-race framing, or unsupported performance promise;
- no global increase to exercise-image limits for unrelated pages.

## Risks And Follow-Ups

| Risk or follow-up | Status |
| --- | --- |
| Hosted CI has not been observed. | Left for verify or PR-stage evidence. |
| Manual proof is qualitative. | Accepted because static checks cannot fully prove visual semantics, source adequacy, or reader comprehension. |
| Generated images may need future visual revision after broader human review. | Mitigated by prompt packets, provenance rows, visual-safety proof, grayscale proof, and rollback path. |
| Advanced rowing could drift toward coaching in future edits. | Mitigated by checker forbidden patterns, source-backed scope wording, and review evidence. |
| Final lifecycle gates remain. | Explain-change routes to verify; PR readiness is not claimed here. |

## Readiness

Explain-change is complete.
All implementation milestones are closed and review-resolution is closed.
The change is ready for final verification.

## Sources

- `docs/changes/2026-07-07-general-audience-vision/explain-change.md`
- `docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- `specs/advanced-rowing-machine-tutorial.md`
- `specs/advanced-rowing-machine-tutorial.test.md`
- `docs/architecture/system/architecture.md`
- `docs/plans/2026-07-07-advanced-rowing-machine-tutorial.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-resolution.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/review-log.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/reviews/code-review-r5.md`
- `docs/changes/2026-07-07-advanced-rowing-machine-tutorial/validation-ledger-m4.md`
