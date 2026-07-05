# Spec: Exercise Muscle Guidance

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-04-exercise-muscle-guidance-standard.md`
- Proposal review: `docs/changes/exercise-muscle-guidance-standard/reviews/proposal-review-r1.md`
- Review log: `docs/changes/exercise-muscle-guidance-standard/review-log.md`
- Related baseline spec: `specs/markdown-first-primer.md`
- Related method spec: `specs/exercise-method-guidance.md`
- Related image spec: `specs/exercise-image-standard.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for exercise-page muscle guidance in GymPrimer. It turns the accepted proposal into requirements for section names, role-based muscle guidance, phase-linked wording, feel-cue pairing, source support, legacy `## Used muscles` compatibility, optional muscle-attention image alignment, proof-slice coverage, and validation behavior.

GymPrimer remains a Markdown-first, citation-backed beginner primer. Exercise muscle guidance helps a beginner understand broad body regions, what those regions contribute to the movement, what they may notice, and what not to overuse. It does not become an anatomy atlas, EMG guide, posture-correction protocol, diagnosis tool, rehabilitation pathway, personalized coaching system, or exact activation claim source.

## Glossary

- Exercise page: A Markdown page under `exercises/` that teaches one exercise, drill, stretch, or equipment movement.
- Muscle guidance: The page-local text that explains broad muscle regions involved in an exercise and what they help do.
- Role-based muscle guidance: Muscle wording organized by movement contribution, such as main driver, support, posture / transfer, finish / control, stabilizer, or mobility focus.
- Phase-linked muscle guidance: Muscle wording tied to a movement phase, such as setup, drive, pull, hold, return, or recovery.
- Feel cue: A practical beginner-facing statement about what a reader may notice during the exercise.
- Compensation cue: A practical statement about what the reader should avoid overusing or letting dominate, without diagnosing the reader.
- Exact activation claim: A claim that a precise muscle is activated, activated more than another muscle, activated by a specific percentage, or activated only when form is correct.
- Legacy muscle heading: The older `## Used muscles` heading on existing exercise pages.
- Muscle-attention image: An optional support image governed by `specs/exercise-image-standard.md` whose purpose is `exercise_muscle_attention_illustration`.

## Examples first

Example E1: new exercise page uses role-based `## Muscles involved`
Given a new exercise page is written under this spec
When a reader opens the page
Then the page includes `## Muscles involved`
And the section explains broad muscle regions by role rather than only listing anatomy terms.

Example E2: `What you should feel` translates muscle roles into body awareness
Given an exercise page says the chest is the main driver and the triceps support a press
When a reader opens `## What you should feel`
Then the section uses soft beginner language such as "you may feel" or "pay attention to"
And it does not say the reader is wrong if they feel the exercise differently.

Example E3: cardio equipment can use movement phases
Given `exercises/rowing-machine.md` is checked under this spec
When a reader opens `## Muscles involved`
Then the page can explain broad regions by stroke phase, such as legs and glutes for the drive, trunk for transfer, and upper back, lats, and arms for the finish.

Example E4: legacy pages are compatible until touched
Given `exercises/dead-bug.md` still uses `## Used muscles`
When the page is not otherwise being updated for muscle guidance, method guidance, images, or exercise-page contract work
Then the page remains legacy-compatible
But if the page is touched for this spec, the heading migrates to `## Muscles involved`.

Example E5: exact activation claim needs direct support or removal
Given an exercise page says "This exercise activates your lower trapezius exactly"
When source support is reviewed
Then the claim must either have direct page-local support and careful framing or be softened to broad role language.

Example E6: muscle-attention image remains subordinate to Markdown
Given an exercise page uses `exercise_muscle_attention_illustration`
When image and Markdown alignment are reviewed
Then nearby Markdown names the broad region, cues, caveats, and citations
And the image has meaningful alt text without in-image labels or precise anatomy as source of truth.

## Requirements

R1. New exercise pages created under this spec MUST include a top-level section headed exactly `## Muscles involved`.

R2. Existing exercise pages updated for muscle guidance, exercise-page template adoption, proof-slice content, or broad exercise-page contract migration MUST use `## Muscles involved` instead of `## Used muscles`.

R3. Existing exercise pages that still use `## Used muscles` MUST remain legacy-compatible until they are touched for muscle guidance, exercise-page template adoption, proof-slice content, or broad exercise-page contract migration.

R4. `## Muscles involved` MUST explain at least one broad muscle region and what that region helps do in the exercise.

R5. `## Muscles involved` MUST use role-based guidance when the exercise has more than one meaningful muscle contribution.

R6. Role-based guidance MAY be written as a Markdown table or as short bullets.

R7. A role table SHOULD use columns equivalent to `Role`, `Muscle region`, and `What it helps do` unless a phase-based table is clearer.

R8. A phase-based table SHOULD use columns equivalent to `Phase`, `Muscle region`, and `What it helps do`.

R9. Valid role labels for the first version are `main driver`, `support`, `posture / transfer`, `finish / control`, `stabilizer`, and `mobility focus`.

R10. Exercise pages MAY use equivalent plain-language role labels when the downstream source audit confirms the wording is clearer and does not create a second taxonomy.

R11. Machine and resistance exercise muscle guidance SHOULD identify the main driver, assisting regions, relevant posture or shoulder-blade control, and what should not take over.

R12. Low-load control drill muscle guidance MUST use soft wording such as "pay attention to", "may help", or "practice control" unless stronger wording has direct page-local source support.

R13. Hold and trunk exercise muscle guidance MUST explain bracing or position control rather than only saying "abs" or "core".

R14. Mobility and stretch page muscle guidance MUST distinguish the region being moved or stretched from a muscle being strengthened.

R15. Cardio-equipment muscle guidance SHOULD tie broad muscle roles to movement phases when the source support and exercise structure make those phases clear.

R16. Exercise pages updated under this spec MUST include `## What you should feel` unless a downstream approved spec records why the page type does not use feel cues.

R17. `## What you should feel` MUST align with `## Muscles involved` by translating muscle roles into practical beginner body awareness.

R18. Feel cues MUST use non-diagnostic and non-guaranteed language such as "you may feel", "pay attention to", or "try to keep".

R19. Feel cues MUST NOT say or imply that the reader is definitely using the wrong muscle because they do not feel the exercise exactly as described.

R20. Compensation cues MUST be framed as general movement guidance and MUST NOT diagnose weakness, dysfunction, posture fault, injury, or pain cause.

R21. Exercise muscle guidance MUST NOT include exact activation percentages.

R22. Exercise muscle guidance MUST NOT use EMG findings as direct beginner instruction unless the exact claim is directly supported, carefully framed, and still useful to a beginner.

R23. Exact activation claims MUST have direct page-local source support or be softened to broad role language.

R24. Broad role claims MUST have page-local source support from an exercise-specific instruction source, a reliable anatomy/context source, or another directly relevant public source.

R25. Exact setup or movement cues that appear inside muscle or feel sections MUST have direct exercise-instruction source support.

R26. Feel cues and compensation cues MUST have direct source support or use clearly soft practical language that avoids proof, diagnosis, and certainty.

R27. Safety stop conditions in muscle or feel sections MUST use institutional, clinical, or exercise-instruction source support when the claim is concrete.

R28. Global-only source indexing in `SOURCES.md` MUST NOT be the only support for specific muscle, feel-cue, compensation, setup, movement, or safety claims.

R29. Technical muscle names MAY appear only when they are useful for beginner understanding and source-supported.

R30. Common-language regions SHOULD appear before technical names when both are used.

R31. Exercise pages MUST NOT make posture-correction promises, treatment promises, rehabilitation claims, individualized cueing claims, or personalized coaching claims through muscle guidance.

R32. Muscle-attention images remain optional and MUST follow `specs/exercise-image-standard.md`.

R33. An exercise page MUST NOT use more than one `exercise_muscle_attention_illustration`.

R34. When a muscle-attention image is used, nearby Markdown MUST carry the exact muscle names, broad-region explanation, feel cues, caveats, and citations.

R35. Muscle-attention image alt text MUST describe the broad highlighted region without unsupported exact anatomy.

R36. Muscle-attention images MUST NOT contain in-image labels, red pain marks, wrong/correct framing, precise anatomy as source of truth, diagnosis claims, or treatment claims.

R37. The exercise template at `docs/templates/exercise-card.md` MUST prompt for role-based `## Muscles involved` guidance and its pairing with `## What you should feel`.

R38. The first proof slice MUST include representative pages from cardio equipment, machine or resistance, hold or trunk, low-load control, mobility or stretch, and band or shoulder-control categories.

R39. The first proof slice SHOULD use these pages unless planning records a better equivalent: `exercises/rowing-machine.md`, `exercises/chest-press.md` or `exercises/seated-row.md`, `exercises/plank.md` or `exercises/dead-bug.md`, `exercises/wall-slide.md` or `exercises/chin-nod.md`, `exercises/thoracic-extension.md` or `exercises/kneeling-hip-flexor-stretch.md`, and `exercises/band-pull-apart.md`.

R40. Broad rollout MUST update remaining exercise pages in batches rather than one unreviewed repository-wide rewrite.

R41. Validation SHOULD check new or adopted exercise pages for `## Muscles involved`, `## What you should feel`, forbidden exact activation wording where deterministic, forbidden diagnosis/treatment/cure/correction wording, and legacy `## Used muscles` only when the page is in migration scope.

R42. Validation SHOULD report stable failure categories and file paths for missing muscle sections, legacy heading misuse in migrated pages, missing feel sections, inactive image purpose usage, multiple muscle-attention images, generic alt text, and deterministic forbidden wording.

R43. Manual source audit MUST sample at least one main-driver claim, one support or stabilizer claim, one feel cue, one compensation cue, one safety cue, and one image-to-Markdown alignment check when a muscle-attention image is present.

R44. Beginner comprehension proof for the first proof slice MUST record whether a beginner can identify the muscle region to notice, what it helps do, what they may feel, what not to overuse, when to stop, and which source they would click to verify the claim.

## Inputs and outputs

Inputs:

- Exercise Markdown pages under `exercises/`.
- `docs/templates/exercise-card.md`.
- Page-local source sections and `SOURCES.md` when sources are reused.
- Optional exercise image references and `media/PROVENANCE.md` rows.
- Manual source-audit and beginner-comprehension evidence.

Outputs:

- Exercise pages with role-based `## Muscles involved` guidance.
- Exercise pages with aligned `## What you should feel` sections.
- Template prompts for future exercise authors.
- Optional validation findings for structure, wording, source-surface, and image-alignment issues.
- Review evidence for semantic source support and beginner comprehension.

## State and invariants

- Markdown exercise pages remain the source of truth for muscle names, roles, feel cues, caveats, safety notes, and citations.
- `## Muscles involved` is the preferred durable heading for new and revised exercise pages.
- `## Used muscles` remains legacy-compatible only until the page is touched for the relevant contract.
- Text-only pages remain valid when no muscle-attention image is needed.
- Muscle-attention images remain support assets, not source-of-truth anatomy diagrams.
- Page-local source support remains required for specific exercise claims.
- Existing exercise paths and source IDs remain compatibility surfaces.

## Error and boundary behavior

- A new exercise page missing `## Muscles involved` fails this spec.
- A migrated exercise page retaining `## Used muscles` fails this spec.
- A legacy exercise page retaining `## Used muscles` passes until it is touched for the muscle-guidance migration scope.
- A page with only a bare muscle list fails when the page is in proof-slice or migrated scope.
- A precise activation or EMG claim without direct page-local support fails source review.
- A feel cue that says the reader must feel one exact muscle fails wording review.
- A compensation cue that diagnoses weakness, dysfunction, posture fault, injury, or treatment need fails wording review.
- A muscle-attention image that introduces unsupported anatomy or lacks nearby Markdown support fails image-alignment review.
- Static validation may pass while semantic source support still fails manual review.

## Compatibility and migration

This spec is additive. It does not require immediate migration of every existing exercise page. Existing pages with `## Used muscles` remain compatible until touched for muscle guidance, exercise-page template adoption, proof-slice content, image-adjacent muscle guidance, or broad exercise-page contract migration.

Migration should happen in small slices. When a page is migrated, preserve the page path, page-local source IDs where possible, and existing source-index behavior. Add global `SOURCES.md` entries only when a source is reused across pages.

Rollback is text-first. If role tables are too long or confusing, the affected page can use shorter role bullets while keeping `## Muscles involved`. If a muscle-attention image misleads readers, remove the image reference and keep the Markdown guidance.

## Observability

- Validation output SHOULD identify the affected file path and stable failure category.
- Manual source-audit evidence MUST identify sampled pages, sampled claim types, supporting sources, pass/fail result, and residual risk.
- Beginner-comprehension evidence MUST identify the checked pages, prompts or criteria, reader-safe non-identifying outcomes, and residual confusion.
- Image-alignment evidence MUST identify the image path, nearby Markdown section, alt text, broad region check, and residual risk.
- Local validation reports MUST name exact commands run and outcomes before completion claims.

## Security and privacy

Exercise muscle guidance MUST NOT commit secrets, private data, private health information, private reader details, or private reviewer details.

Manual proof records MUST avoid storing private health information from beginner readers. Evidence may record non-identifying comprehension outcomes.

Muscle guidance MUST NOT diagnose, treat, prescribe rehabilitation, personalize cueing, promise posture correction, or infer a reader's weakness or dysfunction.

## Accessibility and UX

Role-based muscle guidance should be readable directly in Markdown. Tables are allowed only when they remain short enough for repository reading; otherwise bullets are preferred.

Muscle-attention images need meaningful alt text under `specs/exercise-image-standard.md`. The Markdown text must carry the same explanatory content needed by readers who cannot see the image.

## Performance expectations

Validation for this spec should remain suitable for local repository checks over Markdown and media metadata. Manual semantic source review is expected for claims that static parsing cannot verify.

## Edge cases

EC1. A new page uses `## Used muscles`. It fails because new pages must use `## Muscles involved`.

EC2. A legacy page still uses `## Used muscles` but is not touched in the current slice. It remains compatible.

EC3. A migrated page renames the heading but leaves `Muscles: back, arms, core.` without roles. It fails the role-guidance expectation for migrated pages.

EC4. A page uses `lower trapezius` because the source directly supports that muscle claim. It may pass if beginner-readable context and page-local citation are present.

EC5. A page says "you must feel your glutes or you are doing it wrong." It fails wording review.

EC6. A mobility page describes the target region as a hard strengthening contraction. It fails unless the exercise is actually a strengthening exercise and source support matches that claim.

EC7. A muscle-attention image alt text names exact anatomy not present in nearby Markdown. It fails image-alignment review.

EC8. A page has source links in `SOURCES.md` but no page-local source support for a specific muscle claim. It fails source review.

## Non-goals

- No exact muscle activation percentages.
- No EMG interpretation as routine beginner instruction.
- No individualized cueing, symptom-based substitution, adaptive coaching, or personal workout logic.
- No diagnosis, rehabilitation, pain treatment, posture-correction promise, or dysfunction claim.
- No requirement that every page use a muscle-attention image.
- No anatomy atlas or separate muscle reference section.
- No immediate migration of every exercise page in one implementation slice.
- No new exercise inventory.

## Acceptance criteria

AC1. Spec review confirms the section heading, legacy compatibility, role vocabulary, feel-cue pairing, wording boundaries, source-support rules, image relationship, proof-slice coverage, and migration behavior are clear enough for architecture and planning.

AC2. Architecture assessment records whether the template, validation, image-standard alignment, source-support, and manual-proof surfaces require a canonical architecture update.

AC3. Plan review confirms a small proof slice and separate broad migration slice rather than one unreviewed all-page rewrite.

AC4. Test-spec review maps deterministic checks, manual source audit, beginner comprehension proof, and image-alignment proof to concrete test IDs and evidence artifacts.

AC5. Implementation does not begin until spec, spec review, architecture assessment, plan, plan review, test spec, and test-spec review are complete for the relevant scope.

## Open questions

None blocking spec review.

Downstream planning may still choose the exact first proof-slice pages from the allowed representative set.

## Next artifacts

1. Spec review.
2. Architecture assessment and architecture or ADR update if required.
3. Execution plan.
4. Plan review.
5. Test spec.
6. Test-spec review.

## Follow-on artifacts

- Spec review: `docs/changes/exercise-muscle-guidance-standard/reviews/spec-review-r1.md`

## Readiness

This spec has a clean recorded spec review and is approved for downstream architecture assessment.
