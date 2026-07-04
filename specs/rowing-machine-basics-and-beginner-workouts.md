# Spec: Rowing Machine Basics and Beginner Workout Guidance

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-04-rowing-machine-basics-and-beginner-workouts.md`
- Proposal review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/proposal-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Related exercise method spec: `specs/exercise-method-guidance.md`
- Related exercise image spec: `specs/exercise-image-standard.md`
- Related baseline spec: `specs/markdown-first-primer.md`
- Vision: `VISION.md`
- Constitution: `CONSTITUTION.md`

## Goal and context

This spec defines the observable contract for adding a beginner-facing rowing-machine page to GymPrimer and for activating the `basic_cardio_equipment` method type only where this spec allows it.

The page teaches rowing as skill-based cardio equipment. It emphasizes setup, stroke sequence, moderate/easy effort, controlled recovery, and static beginner workout examples. It does not turn GymPrimer into a rowing coach, workout planner, race-training product, rehabilitation guide, or video-first resource.

The contract is Markdown-first. The rowing page must be useful when read directly from the repository, with page-local sources, clear safety routing, and optional media only when media materially improves setup or movement comprehension.

## Glossary

- Rowing-machine page: The Markdown exercise page at `exercises/rowing-machine.md`.
- Basic cardio equipment: A method type for static beginner guidance on time, effort, rest/reset, progression, and stop conditions for cardio machines.
- Stroke sequence: The ordered movement pattern for the rowing stroke. Drive sequence is legs, then body, then arms. Recovery sequence is arms, then body, then legs.
- Catch: The start position of a rowing stroke before the drive.
- Drive: The work portion of the rowing stroke.
- Finish: The end position of the drive.
- Recovery: The controlled return from finish to catch.
- Damper: The rower setting that changes flywheel feel; it is not a standalone measure of work performed.
- Static workout example: A general example of how a beginner might try rowing, not a personalized plan or prescription.
- Page-local source support: Citations and source entries on the rowing page that support page claims.

## Examples first

Example E1: beginner learns the stroke sequence
Given `exercises/rowing-machine.md` exists
When a reader opens `## Movement breakdown`
Then the reader can identify catch, drive, finish, and recovery
And the page states that drive is legs, then body, then arms
And the page states that recovery is arms, then body, then legs.

Example E2: setup guidance is page-local and source-backed
Given the rowing-machine page says where the foot strap should cross the foot
When a reviewer checks the claim
Then the claim has a nearby citation
And the cited source appears in the rowing page's `## Sources` section.

Example E3: method guidance uses basic cardio equipment
Given the rowing-machine page includes `## How much to do`
When a reader opens that section
Then the section includes `Method type: basic_cardio_equipment`
And it explains a beginner starting point, effort, rest/reset, progression, and stop condition as static education.

Example E4: static examples do not become a plan
Given the page includes examples such as short easy rounds or an easy steady row
When a reviewer checks the wording
Then the examples are framed as examples for learning and conditioning
And the page does not prescribe a multi-week rowing program, race test, or personalized progression.

Example E5: optional media remains support-only
Given the rowing-machine page references a setup or stroke-sequence image
When media validation and manual review run
Then the image uses a local repository path, has meaningful alt text, has provenance if it is generated raster media, and does not introduce instructions that are absent from the Markdown.

## Requirements

R1. The system MUST add the rowing-machine page at `exercises/rowing-machine.md`.

R2. The rowing-machine page MUST be readable directly as Markdown without requiring generated HTML, JavaScript, video, a database, a user account, a tracking flow, or a local server.

R3. The rowing-machine page MUST include these top-level sections: `## What this is for`, `## Before you start`, `## Equipment setup`, `## Muscles involved`, `## Movement breakdown`, `## What you should feel`, `## Common mistakes`, `## How much to do`, `## Easier version`, `## Harder version`, `## Safety notes`, and `## Sources`.

R4. The `## Movement breakdown` section MUST include the stroke phases catch, drive, finish, and recovery.

R5. The movement instructions MUST teach the drive sequence as legs, then body, then arms.

R6. The movement instructions MUST teach the recovery sequence as arms, then body, then legs.

R7. The page MUST frame rowing-machine use as technique-first cardio equipment, not as a machine to pull as hard as possible.

R8. The setup guidance MUST include foot strap position, catch range, grip, shoulder position, posture, handle path, and damper meaning.

R9. The foot strap guidance MUST say the strap crosses the ball or widest part of the foot unless source review supports a narrower wording.

R10. The catch guidance MUST describe shins approaching vertical only as far as comfortable and MUST NOT require forced range of motion.

R11. The damper guidance MUST explain that the damper changes flywheel feel and MUST NOT present a high damper setting as inherently better, harder, or proof of more work.

R12. The page MUST state that the reader creates the work through stroke effort, not by blindly setting the damper high.

R13. The `## Muscles involved` section MUST describe broad muscle engagement for beginner literacy: legs and glutes for the drive, trunk for posture and transfer, and upper back/lats and arms for the finish.

R14. Muscle and feel wording MUST remain broad and educational and MUST NOT claim precise individualized muscle activation, diagnosis, treatment, or correction.

R15. This spec activates `basic_cardio_equipment` as an allowed exercise method type only for rowing-machine content governed by this spec and later cardio-equipment pages governed by approved downstream specs or amendments.

R16. The rowing-machine `## How much to do` section MUST include `Method type: basic_cardio_equipment`.

R17. The `basic_cardio_equipment` method section MUST include visible labels or equivalent plain-language lines for beginner starting point, effort, rest or reset, progression, and stop condition.

R18. The beginner starting point MUST begin with short easy rowing exposure, such as 3-5 minutes, and MUST allow a break to walk, breathe, or reset technique before any repeat round.

R19. The effort guidance MUST start with easy or moderate effort and MUST NOT instruct beginners to start with all-out effort, maximal damper, or sprint intervals.

R20. The progression guidance MUST prioritize smoother technique before adding time and MUST prioritize time before adding moderate effort.

R21. Static workout examples MAY include short easy rounds, easy steady rowing, easy/moderate intervals, or a short steady cardio session when each example is framed as an example rather than a prescription.

R22. Static workout examples MUST NOT become a race plan, 2k test plan, multi-week rowing program, weight-loss guarantee, heart-rate-zone prescription, or personalized conditioning plan.

R23. The page MUST explain that rowing can contribute to aerobic activity and MUST NOT imply that rowing replaces all strength training.

R24. The page MUST state that adult activity guidance includes both aerobic activity and muscle-strengthening activity on at least two days per week, with page-local citation support.

R25. The `## Safety notes` section MUST route readers to `../RED-FLAGS.md` or the correct relative path to the central safety reference.

R26. The page MUST tell readers to stop for chest pain, dizziness, fainting, unusual shortness of breath, sharp pain, numbness, symptoms that worsen, painful technique, or technique breakdown that makes the movement jerky or uncontrolled.

R27. Safety and stop-condition claims MUST have page-local source support when they make concrete safety claims.

R28. Technique, setup, damper, workout-example, and weekly-activity claims MUST have page-local source support.

R29. Every source used for page claims MUST appear in the rowing page's `## Sources` section.

R30. Reused source IDs MUST appear in `SOURCES.md` when the source is reused across more than one page or when existing source-index rules require it.

R31. The page MUST NOT use remote images, borrowed web images, commercial-machine screenshots, branded equipment photos, or identifiable people.

R32. The page MAY remain text-only when text is sufficient for beginner comprehension.

R33. If a setup image is added, it MUST teach only setup-relevant information such as foot strap, seat, handle, or catch position.

R34. If a stroke-sequence image is added, it MUST teach only the movement sequence or key positions for catch, drive, finish, and recovery.

R35. Rowing-machine images MUST NOT include in-image text instructions, citations, safety notes, red pain marks, diagnostic symbols, or "wrong/correct" labels.

R36. Generated raster rowing-machine images MUST satisfy `specs/exercise-image-standard.md`, including provenance, prompt-record, alt-text, page-reference, and visual-safety-review requirements.

R37. The implementation MUST NOT add a hosted app, calculator, workout tracker, user-input flow, generated public API, or hidden metadata source of truth.

R38. The implementation MUST NOT introduce diagnosis, treatment, rehabilitation protocol, return-to-training prescription, individualized medical advice, or personalized coaching.

R39. The implementation MUST preserve the existing exercise-method active method types and MUST NOT activate `loaded_carry`.

R40. Validation or manual proof MUST be able to distinguish `basic_cardio_equipment` from the existing resistance, bodyweight, control, isometric, mobility, and stretch method types.

## Inputs and outputs

Inputs:

- Accepted proposal and proposal-review record for rowing-machine basics.
- Existing Markdown-first, exercise-method, and exercise-image specs.
- Authoritative page-local rowing, physical-activity, and safety sources.
- Optional local media assets and provenance records if images are added.
- Existing `SOURCES.md` and `RED-FLAGS.md`.

Outputs:

- `exercises/rowing-machine.md` as a beginner-facing Markdown page.
- Page-local source references and `## Sources` entries.
- `SOURCES.md` updates when sources are reused or source-index rules require them.
- Optional local media under `media/exercises/rowing-machine/`.
- Optional provenance and prompt records for generated raster images.
- Automated validation results and manual proof records for source support, safety scope, and beginner comprehension.

No runtime API, database record, user profile, generated data package, hidden metadata contract, or hosted service is introduced by this spec.

## State and invariants

- Markdown remains the source of truth for the rowing-machine guidance.
- The rowing-machine page remains static education for general adult beginners.
- `basic_cardio_equipment` is active only for the scope allowed by this spec and later approved downstream artifacts.
- The visible `Method type: basic_cardio_equipment` line is the source of truth for the rowing page's method type.
- Page-local sources remain required for cited claims.
- Generated raster media remains subordinate to Markdown and cannot become source-of-truth exercise guidance.
- Rowing-machine examples remain examples, not personalized prescriptions.
- Existing exercise pages and method types remain valid unless later approved artifacts change them.

## Error and boundary behavior

- A rowing-machine page missing any required top-level section fails this spec.
- A movement breakdown that omits catch, drive, finish, or recovery fails this spec.
- A movement breakdown that reverses or obscures the required drive or recovery sequence fails this spec.
- A `## How much to do` section missing `Method type: basic_cardio_equipment` fails this spec.
- A method section that starts beginners with maximal damper, all-out effort, or sprint intervals fails this spec.
- A method section that adapts to reader goals, symptoms, medical history, body measurements, or training response fails this spec.
- A page that implies rowing replaces all strength training fails this spec.
- A page that lacks page-local source support for setup, technique, damper, method, weekly activity, or safety claims fails source review.
- A page that links remote images, borrowed images, screenshots, branded photos, or identifiable people fails media review.
- A generated raster image without an approved exact provenance row, prompt record where required, meaningful alt text, and visual-safety evidence fails promotion.
- A page that contains diagnosis, treatment, rehab, return-to-training, individualized medical advice, or personalized coaching fails the safety boundary.

## Compatibility and migration

This spec is additive. It adds one new exercise page and narrowly activates `basic_cardio_equipment` for rowing-machine content. It does not migrate existing exercise pages, existing method sections, existing media, existing source IDs, or existing templates unless downstream implementation determines a focused template or checker update is necessary.

Existing active exercise method types remain unchanged. `loaded_carry` remains deferred. Future treadmill, bike, elliptical, or other cardio-equipment pages need their own approved downstream scope before relying on this spec as a reusable pattern.

Rollback is Markdown-first. If the page is not ready for promotion, remove or keep draft-only navigation to `exercises/rowing-machine.md`, remove unused media references and assets, remove unused provenance rows, and keep global source-index entries only when still reused elsewhere.

## Observability

- Automated validation SHOULD report required-section, citation, source-index, forbidden-scope, method-type, media-path, provenance, prompt-record, internal-link, and privacy results when those checks are available.
- Manual source audit MUST record whether foot setup, stroke sequence, damper, beginner method, weekly activity, and stop-condition claims are supported.
- Manual beginner comprehension evidence MUST record non-identifying answers for what the rower is for, foot strap position, drive sequence, recovery sequence, beginner first step, stop condition, and source verification.
- Visual-safety review MUST be recorded if rowing-machine images are added.
- Local validation reports MUST name the exact commands run and their outcomes.
- Hosted CI MUST NOT be claimed unless an actual CI run is observed.

## Security and privacy

- The page and review evidence MUST NOT include secrets, credentials, private user data, private health information, private reviewer data, or identifiable beginner-reader data.
- Beginner comprehension records MUST be non-identifying.
- Media assets, prompt records, provenance rows, and validation output MUST avoid private data and private health details.
- The page MUST NOT ask readers for symptoms, medical history, goals, body measurements, location, account details, or training logs.

## Accessibility and UX

- The page MUST be understandable as plain Markdown.
- Headings MUST be descriptive enough for repository browsing and screen-reader navigation.
- Any image MUST have meaningful alt text that identifies the exercise context and image purpose.
- Image alt text and nearby text MUST NOT be the only place where essential setup, movement, safety, or method instructions appear.
- The page SHOULD keep safety routing calm and visible without overwhelming the technique and setup guidance.
- The page SHOULD use plain beginner language for the stroke sequence, damper, and effort guidance.

## Performance expectations

Not applicable to runtime performance. The page must remain a static Markdown artifact that can be opened directly from the repository without build, network, account, or server dependencies.

Validation performance should remain suitable for local documentation checks over the changed files; no requirement in this spec authorizes a new long-running build or service.

## Edge cases

EC1. If the rower has a different footplate design, the page should keep the foot-strap cue general enough to remain useful while preserving source support.

EC2. If a beginner cannot reach vertical shins comfortably, the page should allow a comfortable catch range rather than forcing position.

EC3. If a reader wants harder rowing, the page should direct progression toward smoother technique and more time before harder effort.

EC4. If a reader asks whether the damper is the resistance level, the page should explain that damper changes feel while effort creates work.

EC5. If workout examples are included, they must remain short static examples and not become a schedule, challenge, or plan.

EC6. If text-only guidance passes beginner comprehension review, images are not required.

EC7. If images are added but visual review finds unsupported technique, the image must be revised or removed before promotion.

EC8. If a source supports sport rowing but not gym-beginner rower setup, the implementation should narrow the claim or use a more direct source.

EC9. If a validation checker still treats `basic_cardio_equipment` as deferred, downstream implementation must update validation or record manual proof before promotion.

EC10. If `SOURCES.md` already contains a reused source under an existing ID, the page should use the compatible ID unless a downstream source-audit reason supports adding a new one.

## Non-goals

- No personalized rowing plan.
- No 2k race training plan.
- No sport-rowing performance program.
- No high-intensity beginner sprint protocol.
- No heart-rate-zone prescription.
- No weight-loss guarantee.
- No diagnosis, pain treatment, rehabilitation plan, return-to-training decision, or individualized medical advice.
- No claim that rowing replaces all strength training.
- No video-first product.
- No hosted app, calculator, workout tracker, account system, database, API, or user-input flow.
- No commercial-machine screenshots, borrowed web images, branded equipment photos, or identifiable people.
- No activation of `loaded_carry`.
- No broad rollout to all cardio-equipment pages in this spec.

## Acceptance criteria

AC1. The proposal status is normalized to `accepted` based on clean recorded proposal review before this spec is relied on.

AC2. Spec review confirms that `basic_cardio_equipment` activation is narrow enough to avoid conflicting with `specs/exercise-method-guidance.md`.

AC3. Spec review confirms that the rowing-machine page contract is clear enough to draft `exercises/rowing-machine.md` without adding a new product decision.

AC4. The required section list, stroke sequence, setup scope, damper guidance, method labels, source-support obligations, safety boundaries, and media boundaries are testable or manually verifiable.

AC5. The future implementation can run automated Markdown-first, privacy, source, method-type, internal-link, and media/provenance checks where available.

AC6. The future implementation can record manual source-audit evidence for setup, technique, damper, beginner method, weekly activity, and stop-condition claims.

AC7. The future implementation can record non-identifying beginner comprehension evidence before promotion.

AC8. No requirement in this spec requires a hosted app, database, user account, generated public API, hidden metadata source of truth, video-first product, or personalized coaching behavior.

AC9. No requirement in this spec authorizes diagnosis, treatment, rehabilitation, return-to-training prescription, individualized programming, sport-performance programming, or a rowing race plan.

## Open questions

None for spec review.

Downstream architecture assessment and planning should decide whether implementation needs a checker update for `basic_cardio_equipment`, a template update, one setup image, a setup plus sequence image, or text-only first-pass delivery.

## Next artifacts

- Spec review for this spec.
- Architecture assessment or architecture update for the `basic_cardio_equipment` method-type boundary, validation impact, and optional media/provenance impact.
- Execution plan for the rowing-machine page, source-index updates, optional media, validation, manual source audit, and beginner comprehension proof.
- Test specification mapping requirements to automated checks and manual proof.

## Follow-on artifacts

- Spec review: `docs/changes/rowing-machine-basics-and-beginner-workouts/reviews/spec-review-r1.md`
- Review log: `docs/changes/rowing-machine-basics-and-beginner-workouts/review-log.md`
- Architecture: `docs/architecture/system/architecture.md`

## Readiness

This spec was approved after clean spec review.

It is not ready for planning, test-spec, implementation, or promotion until architecture assessment or update, architecture review when required, planning, test specification, and required reviews are complete.
