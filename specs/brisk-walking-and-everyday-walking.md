# Brisk Walking and Everyday Walking Guidance

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md`
- Proposal review R1: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-resolution.md`
- Related method spec: `specs/exercise-method-guidance.md`
- Related baseline spec: `specs/markdown-first-primer.md`
- Related muscle spec: `specs/exercise-muscle-guidance.md`
- Related image spec: `specs/exercise-image-standard.md`

## Upstream status settlement

- Upstream artifact: `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md`
- Review evidence: proposal-review R2 approved the proposal with no findings after R1 finding PR-WALK-1 was closed in `review-resolution.md`.
- Previous status: accepted
- New status: accepted
- Settlement result: not-needed
- Settlement blocker: None

## Goal and context

This spec defines the observable contract for adding brisk walking and everyday walking guidance to GymPrimer after the accepted proposal chose Option C.

The change adds two complementary Markdown pages, keeps brisk walking and everyday walking distinct, introduces `basic_cardio_activity` as the non-equipment cardio method type for brisk walking, and keeps the work static, citation-backed, beginner-readable, and non-clinical.

This spec does not authorize page implementation, checker changes, image generation, publication, navigation promotion, or PR readiness. It prepares the change for `spec-review`.

## Glossary

- Brisk walking: A deliberate moderate-intensity walk taught as beginner cardio when effort is high enough.
- Everyday walking: Normal walking accumulated through errands, commuting, stairs, walking breaks, parking farther away, or similar daily movement.
- Basic cardio activity: A non-equipment aerobic activity method type, represented as `basic_cardio_activity`.
- Talk test: A beginner intensity check where moderate activity allows talking but not comfortable singing.
- Page-local sources: A page's own `## Sources` section supporting claims made on that page.
- Source index: `SOURCES.md`, used for sources reused across pages.
- Stop rule: Static safety language telling the reader when to stop walking and seek appropriate help.

## Examples first

Example E1: brisk walking page teaches deliberate moderate-intensity walking
Given `exercises/brisk-walking.md` is implemented under this spec
When a reader opens the page
Then the page explains that brisk walking is a deliberate moderate-intensity cardio activity
And the page distinguishes brisk walking from strolling and everyday walking
And the page uses the talk test and a pace reference as beginner intensity checks.

Example E2: everyday walking page teaches movement habit-building
Given `principles/everyday-walking.md` is implemented under this spec
When a reader opens the page
Then the page frames everyday walking as daily movement and sitting interruption
And the page does not imply that every step is equivalent to deliberate brisk cardio
And the page links or points readers toward brisk walking when intensity rises enough to become a workout.

Example E3: brisk walking uses `basic_cardio_activity`
Given `exercises/brisk-walking.md` includes `## How much to do`
When method guidance is checked
Then the section includes `Method type: basic_cardio_activity`
And the starting point is framed around time, effort, and progression rather than strength-training sets and reps.

Example E4: source support is page-local and reusable sources are indexed
Given a walking page claims that the talk test can identify moderate intensity
When citation support is reviewed
Then the claim has page-local source support
And the reused source ID appears in `SOURCES.md`.

Example E5: optional walking image remains support-only
Given `exercises/brisk-walking.md` includes a generated walking image
When image validation and visual-safety review run
Then the image uses `exercise_movement_illustration`, has meaningful alt text, has approved provenance, contains no in-image labels, and remains subordinate to the Markdown guidance.

## Requirements

BWG-R1. The implementation slice MUST create or update exactly these two primary page contracts for this walking change: `exercises/brisk-walking.md` and `principles/everyday-walking.md`.

BWG-R2. `exercises/brisk-walking.md` MUST teach brisk walking as a beginner cardio exercise, not as a casual movement habit, weight-loss prescription, medical walking program, running progression, or adaptive walking plan.

BWG-R3. `principles/everyday-walking.md` MUST teach everyday walking as daily movement, sitting interruption, and habit-building, not as a formal workout unless the page clearly says intensity can rise into brisk walking.

BWG-R4. The walking content MUST preserve the accepted distinction that everyday walking helps a reader move more while brisk walking is the version that usually counts as moderate-intensity cardio when effort is high enough.

BWG-R5. `exercises/brisk-walking.md` MUST include a `## How to know the pace is brisk` section or equivalent page-local section that explains the talk test, moderate effort, and a pace reference without making pace the only definition.

BWG-R6. The brisk walking intensity wording MUST be supported by page-local citations to sources that directly support the talk test, moderate-intensity framing, or brisk walking pace reference.

BWG-R7. `exercises/brisk-walking.md` MUST include a page-local section headed exactly `## How much to do`.

BWG-R8. `exercises/brisk-walking.md` MUST include the visible method line `Method type: basic_cardio_activity` in `## How much to do`.

BWG-R9. The downstream method contract MUST add `basic_cardio_activity` as an active visible method type for non-equipment aerobic activities before `exercises/brisk-walking.md` is promoted.

BWG-R10. `basic_cardio_activity` method guidance MUST use time, effort, frequency or repeatability, progression, and stop rules rather than strength-training sets and reps as the primary method shape.

BWG-R11. The brisk walking starter guidance MUST include a static beginner starting point of 5-10 minutes or narrower equivalent wording unless a later approved spec amendment records different source-supported wording.

BWG-R12. The brisk walking progression guidance MUST prioritize adding total minutes, then more brisk minutes, then hills or faster sections only when the walk remains comfortable.

BWG-R13. Walking method guidance MUST be framed as static general education and MUST NOT adapt walking time, pace, terrain, frequency, or progression based on reader symptoms, goals, medical history, body measurements, wearable data, step count, or training response.

BWG-R14. `exercises/brisk-walking.md` MUST include `## Muscles involved` with role-based muscle guidance for broad regions involved in walking.

BWG-R15. `exercises/brisk-walking.md` MUST include `## What you should feel` aligned with the muscle roles and intensity guidance.

BWG-R16. Brisk walking muscle and feel guidance MUST remain beginner-readable and MUST NOT make exact activation, diagnosis, treatment, rehabilitation, gait-correction, or posture-correction claims.

BWG-R17. `exercises/brisk-walking.md` MUST include walking technique guidance covering forward gaze, relaxed neck and shoulders, natural arm swing, relaxed hands, tall posture, smooth heel-to-toe walking, an easy start, and an easy finish, with page-local source support.

BWG-R18. Both walking pages MUST include safety notes and a resolving link or route to the central `RED-FLAGS.md` safety page.

BWG-R19. Walking safety notes MUST tell readers to stop and seek appropriate help for chest pain, fainting or severe dizziness, unusual shortness of breath, new severe pain, numbness, weakness, neurological symptoms, or symptoms that worsen or do not settle.

BWG-R20. Walking safety notes MUST NOT add symptom-specific plans for chronic disease, pregnancy, post-surgery recovery, injury recovery, cardiopulmonary conditions, or return-to-walking after medical events in this first slice.

BWG-R21. Both walking pages MUST include page-local `## Sources` sections.

BWG-R22. Reused walking, activity-guideline, intensity, technique, and safety sources MUST appear in `SOURCES.md` with stable source IDs before the pages are promoted.

BWG-R23. Source review MUST sample the claims for intensity, talk test, weekly activity guidance when used, less-sitting framing, walking technique, starter duration or progression, and stop rules.

BWG-R24. `exercises/brisk-walking.md` MAY include no image and MUST remain valid as a text-only page.

BWG-R25. If `exercises/brisk-walking.md` includes a generated raster image in the first slice, it MUST include no more than one walking image, the image MUST use `exercise_movement_illustration`, and the image MUST satisfy `specs/exercise-image-standard.md`.

BWG-R26. `principles/everyday-walking.md` MUST NOT include an image in the first implementation slice unless a later approved spec amendment records why the principle page needs one.

BWG-R27. Walking pages MUST NOT include a calorie target, weight-loss prescription, fixed daily step-count mandate, heart-rate-zone prescription, wearable integration, calculator, dashboard, user input flow, adaptive recommendation flow, or generated content as source of truth.

BWG-R28. Walking pages MUST NOT include race-walking technique, running progression, hiking, rucking, loaded walking, treadmill protocol, incline-walking protocol, or a full walking program in the first slice.

BWG-R29. Automated validation SHOULD check walking page existence, required headings, page-local sources, `SOURCES.md` reuse, `Method type: basic_cardio_activity`, central safety routing, forbidden personalization or medical wording, privacy, links, and image provenance when images are present.

BWG-R30. Manual beginner proof MUST record whether a beginner can distinguish everyday walking from brisk walking, identify how to know the pace is brisk, name a reasonable starting duration, describe what the body should feel, name stop conditions, and identify which source supports the intensity claim.

## Inputs and outputs

Inputs:

- Accepted proposal: `docs/proposals/2026-07-05-brisk-walking-and-everyday-walking.md`.
- Existing source index: `SOURCES.md`.
- Central safety page: `RED-FLAGS.md`.
- Existing governing specs listed in `Related proposal`.
- Public sources already named in the accepted proposal.

Outputs:

- New exercise page contract for `exercises/brisk-walking.md`.
- New principle page contract for `principles/everyday-walking.md`.
- Updated method contract recognizing `basic_cardio_activity`.
- Page-local sources and reused source IDs.
- Optional generated raster image, provenance row, and prompt record only if the first slice decides an image is needed.
- Review, validation, source-audit, and beginner proof evidence under the change root.

## State and invariants

- Markdown remains the source of truth for walking guidance.
- The accepted Option C two-page split remains the decision for this spec.
- `basic_cardio_activity` remains distinct from `basic_cardio_equipment`.
- Everyday walking and brisk walking must remain distinguishable in reader-facing text.
- Generated images, if any, support Markdown but never prove technique, safety, anatomy, or programming claims.
- Walking content remains static general education and never becomes personalized coaching, diagnosis, treatment, rehabilitation, or a walking program.
- Implementation remains blocked until downstream workflow artifacts approve it.

## Error and boundary behavior

- A one-page walking implementation fails this spec unless a later accepted proposal or approved spec amendment changes the two-page decision.
- A brisk walking page without `Method type: basic_cardio_activity` fails method-contract review.
- A brisk walking page that uses sets and reps as the primary method shape fails this spec.
- An everyday walking page that implies all walking counts as deliberate moderate-intensity cardio fails this spec.
- A walking page with source links only in `SOURCES.md` and no page-local source support fails source review.
- A walking page that gives disease-specific, pregnancy-specific, post-surgery, injury-recovery, cardiopulmonary, or return-to-walking advice fails first-slice scope.
- A generated walking image without approved provenance, meaningful alt text, local path, and image-purpose alignment fails promotion.
- If automated validation cannot prove semantic source support or beginner comprehension, manual source audit and read-test evidence remain required.

## Compatibility and migration

This change is additive. It adds two new Markdown pages and a new non-equipment cardio method type. It does not require migration of existing exercise pages.

The method-contract work must avoid reactivating `basic_cardio_equipment` or `loaded_carry` unless a separate approved spec or spec amendment does so.

Rollback is Markdown-first. If the brisk walking method guidance is too prescriptive, narrow or remove the problematic method wording while preserving safety routing and sources. If the everyday walking page duplicates the brisk page too heavily, revise cross-links and scope boundaries rather than merging the pages without a new approved decision. If an optional image is not useful or not valid, remove the image reference and related unused media artifacts while keeping the text-only page.

## Observability

Automated validation should report file-level failures for:

- missing walking pages;
- missing required headings;
- missing or inactive `Method type: basic_cardio_activity`;
- missing page-local `## Sources`;
- reused source IDs missing from `SOURCES.md`;
- unresolved `RED-FLAGS.md` links;
- forbidden medical, personalization, weight-loss, calorie, step-count mandate, heart-rate-zone, tracker, or adaptive-plan wording where deterministic;
- image path, alt-text, provenance, purpose, prompt-record, and page-reference failures when an image is present;
- privacy scan failures.

Manual validation must record:

- sampled source-support results for the claims listed in BWG-R23;
- beginner read-test outcomes for the prompts listed in BWG-R30;
- optional visual-safety evidence when a walking image is included;
- residual risk where automated checks cannot prove source support, tone, or comprehension.

Validation reports must not claim CI passed unless a CI run was actually observed.

## Security and privacy

This spec introduces no user input, accounts, analytics, trackers, databases, wearable integrations, private health data, or runtime storage.

Walking pages, media prompts, provenance rows, review records, source audits, validation output, and beginner proof notes MUST NOT include secrets, credentials, private machine paths, private reviewer data, private reader details, private health information, or identifiable private people.

Walking content MUST NOT ask readers to submit symptoms, medical history, pregnancy status, surgery history, cardiopulmonary status, body measurements, wearable data, training logs, or goals.

## Accessibility and UX

Walking pages must be readable as plain Markdown in GitHub or a cloned repository.

Headings must make the distinction between everyday walking and brisk walking easy to scan.

Tables may be used only when short enough to remain readable in plain Markdown. If a table becomes too wide, the implementation should use bullets instead.

If an image is used, it must have meaningful alt text and nearby Markdown must carry the instructional content for readers who cannot see the image.

The pages must not rely on color, icons, video, JavaScript, generated HTML, calculators, or interactive controls to communicate the walking guidance.

## Performance expectations

No runtime performance requirements apply. Validation should remain suitable for local repository checks and should report deterministic file-level failures when checks are automated.

## Edge cases

EC1. A reader walks slowly during errands. The everyday walking page can count it as daily movement, but it must not call it brisk cardio unless intensity rises enough for the talk-test framing.

EC2. A reader walks briskly for five minutes. The brisk walking page may explain that short brisk walks can add up when source-supported, but it must not turn that into a personalized weekly plan.

EC3. A reader wants 10,000 steps. The walking pages may avoid the topic or explain that this first slice does not mandate a step target; they must not prescribe a universal step count.

EC4. A brisk walking route includes hills. The brisk walking page may mention hills as a later progression if comfortable, but it must not include an incline protocol or hiking/rucking progression.

EC5. A walking page cites CDC or NHS for intensity but omits a page-local source entry. The page fails source review even if the source appears in `SOURCES.md`.

EC6. The method validator still knows only the six previous method types. The implementation is not promotable until validation timing is decided and active method-type handling is updated or a manual exception is recorded by downstream artifacts.

EC7. A generated image shows a person walking but includes in-image labels or red pain marks. The image fails visual-safety and image-standard review.

EC8. The everyday walking page begins to sound like motivational filler. The page fails content review unless it gives practical daily movement examples, scope boundaries, safety notes, and sources.

## Non-goals

- No personalized walking plan.
- No weight-loss prescription.
- No calorie target.
- No step-count mandate.
- No heart-rate-zone prescription.
- No medical walking program.
- No return-to-walking protocol after injury, surgery, illness, pregnancy, or cardiac events.
- No pain treatment, gait diagnosis, posture correction, or rehabilitation pathway.
- No race-walking technique.
- No running progression.
- No hiking, rucking, loaded walking, treadmill protocol, or incline-walking program in the first slice.
- No tracker app, wearable integration, calculator, dashboard, user input, or adaptive recommendation flow.
- No broad migration of existing exercise pages.
- No generated image as source of truth.

## Acceptance criteria

AC1. Spec review confirms that Option C, `exercises/brisk-walking.md`, `principles/everyday-walking.md`, and `basic_cardio_activity` are contract decisions rather than open product questions.

AC2. Spec review confirms that only downstream contract details remain open, including exact requirement wording in amended specs, validation timing, source ID finalization, optional image use, and exact read-test wording.

AC3. The spec defines testable page contracts for brisk walking and everyday walking.

AC4. The spec defines testable method-contract behavior for `basic_cardio_activity`.

AC5. The spec defines source-support, source-index, and manual source-audit obligations for walking claims.

AC6. The spec defines safety boundaries and stop-rule obligations without authorizing medical or personalized walking guidance.

AC7. The spec defines image-optional behavior and the required constraints if a brisk walking image is added.

AC8. The spec defines automated and manual validation surfaces for implementation planning and test-spec authoring.

AC9. No requirement in this spec requires a hosted app, database, account, tracker, wearable integration, calculator, generated public data package, or hidden metadata source of truth.

AC10. No requirement in this spec authorizes implementation before downstream review, architecture assessment, planning, test-spec, and required reviews complete.

## Open questions

None blocking spec-review.

Downstream artifacts may decide only contract details needed to implement the accepted decision:

- exact final wording for the `basic_cardio_activity` method-contract amendment;
- whether `basic_cardio_activity` validation is updated in the first implementation slice or covered by manual proof until validator work is approved;
- exact source IDs used on each page after `SOURCES.md` review;
- whether `exercises/brisk-walking.md` uses no image or one optional `exercise_movement_illustration`;
- exact beginner read-test wording and evidence format.

## Next artifacts

- Spec review.
- Architecture assessment or architecture artifact if spec review determines the method-contract and validation changes need one.
- Execution plan covering method contract, walking pages, source index, validation, optional media, source audit, and beginner proof.
- Test specification mapping requirements to automated checks and manual evidence.

## Follow-on artifacts

- Spec review R1: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r1.md`

## Readiness

Approved for downstream architecture assessment.

This spec is not ready for implementation until spec review is approved and required downstream architecture, planning, test-spec, test-spec-review, implementation, review, and verification artifacts are complete.
