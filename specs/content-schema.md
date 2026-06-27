# Spec: Content Schema and Review Contract

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
- Proposal review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/proposal-review-r1.md`

## Goal and context

This spec defines the observable content contract for GymPrimer exercise cards, taxonomy records, locale-aware fields, canonical SVG media references, review metadata, safety notes, and validation outcomes.

The goal is to make the first exercise library reviewable, testable, accessible, English-first, and ready for future Chinese content without requiring a schema migration. The spec covers the data and validation contract only. It does not choose the implementation stack, storage backend, frontend framework, CMS, or deployment model.

## Glossary

- Exercise card: A structured record that teaches one exercise, machine, drill, or cardio-equipment use case.
- Locale: A language-specific content branch identified by a controlled BCP-47-style locale key from the v1 locale enum, such as `en-US` or `zh-Hans`.
- Canonical media: The reviewed SVG step-card media and accessible text alternatives that are treated as source-of-truth movement media.
- Supplemental media: Optional non-canonical media, such as later community video, that may clarify but cannot replace reviewed text and SVG steps.
- Review tier: The content-risk review level used to determine who must approve a card or policy.
- Taxonomy: Controlled names for equipment, muscles, movement patterns, difficulty, card type, and safety categories.
- Stop sign: A symptom or situation where the card tells the user to stop and seek qualified help.

## Examples first

Example E1: valid English exercise card
Given an exercise card for "Lat pulldown" with stable ID `ex-lat-pulldown`
And the card has required `en-US` locale fields, taxonomy references, SVG step references, safety notes, review metadata, and a visible disclaimer
When the content validator checks the card
Then validation passes and the card is eligible for publication after required review approvals are present.

Example E2: Chinese locale can be added without changing the card shape
Given an approved English card with locale key `en-US`
When a contributor adds `zh-Hans` values for localized title, aliases, body text, glossary labels, and accessible media text
Then validation accepts the same field structure under `zh-Hans` and does not require a migration of the English content.

Example E3: unreviewed safety change blocks publication
Given a published card with an approved safety note
When an author edits a stop sign, contraindication, progression criterion, or pain-language field
Then the card becomes unpublished or pending review until the required safety review tier approves the change.

Example E3a: trainer-only mechanics change
Given a front lat pulldown card is updated from "pull down fast" to "pull the bar toward the upper chest with controlled tempo"
When the content validator classifies the change
Then the change routes to `trainer` or `strength_coach` review and does not require physical-therapist or sports-medicine-clinician review unless safety-sensitive fields also changed.

Example E3b: policy-sensitive emergency language change
Given an editor changes the global stop-rule template for dizziness, fainting, chest pain, or unusual shortness of breath
When the validator evaluates dependent cards
Then sports-medicine-clinician review is required and dependent cards are blocked or marked `review_expired` if the policy meaning changes.

Example E3c: elevated-risk deferral
Given an author drafts a sprint-interval progression card with `safety_category = elevated_risk`
And elevated-risk category definitions are not yet approved
When a publication request is made
Then the request is rejected with `elevated_risk_policy_not_defined`.

Example E3d: review-sensitive media edit
Given a published rowing-machine card receives a new diagram that changes the sequence from "legs-body-arms"
When the edit is saved
Then the published version remains unchanged and a new unpublished version is created for review.

Example E4: video cannot become source of truth
Given a card has reviewed text and SVG step cards
When a contributor attaches a supplemental video
Then the video must have licensing, attribution, captions or transcript, and review metadata, and the card remains valid only if reviewed text and SVG steps still carry the canonical instruction.

Example E5: unsafe medical wording fails validation
Given a card says an exercise "fixes sciatica" or "treats knee pain"
When the content validator checks safety language
Then validation fails because the card diagnoses or promises treatment.

## Requirements

R1. The system MUST represent every exercise card with a stable, unique card ID that does not change when localized text changes.

R2. The system MUST represent every publishable exercise card with at least one English locale branch keyed as `en-US`.

R3. The system MUST allow additional locale branches, including `zh-Hans`, using the same field structure as `en-US`.

R4. The system MUST NOT require bilingual content for initial publication when the English branch satisfies all required fields and reviews.

R5. Each exercise card MUST include localized title, aliases, summary, purpose, equipment setup, start position, movement phases, breathing and bracing cues, common mistakes, regressions, progressions, what-you-should-feel cues, what-you-should-not-feel cues, and safety notes.

R6. Each exercise card MUST include nonlocalized taxonomy references for card type, equipment, movement pattern, difficulty, primary muscles, secondary muscles, stabilizers, and safety category.

R7. The taxonomy MUST use stable IDs for equipment, muscles, movement patterns, card types, difficulty levels, and safety categories.

R8. The system MUST reject cards that reference unknown taxonomy IDs.

R9. Each card MUST include at least three and at most six canonical SVG step references before publication.

R10. Each canonical SVG step reference MUST include localized accessible text for every published locale on that card.

R11. Canonical SVG step media MUST be treated as source-of-truth media together with reviewed text.

R12. Supplemental video or other media MUST NOT be required for publication.

R13. Supplemental media MUST NOT override, contradict, or replace reviewed text or canonical SVG steps.

R14. Each card MUST include a plain-language disclaimer equivalent in meaning to: "GymPrimer is educational content, not medical advice. Talk to a qualified professional before starting a new exercise program; stop and seek qualified help for sharp, radiating, worsening, or unusual symptoms."

R15. Each card MUST include stop signs for sharp pain, radiating symptoms, worsening symptoms, unusual symptoms, dizziness, fainting, chest pain, unusual shortness of breath, new numbness, or other emergency-like symptoms when applicable.

R16. Card language MUST NOT diagnose injuries, promise treatment, prescribe rehabilitation, or claim that an exercise cures a condition.

R17. Progressions MUST be framed as optional harder versions tied to readiness cues, not as automatic recommendations.

R18. Regressions MUST be present for every strength or mobility exercise card.

R19. Each card version MUST store lifecycle state in two separate fields: `review_status` and `publication_status`. The two fields MUST NOT be collapsed into a single status enum.

R20. `review_status` MUST be one of `draft`, `in_review`, `changes_requested`, `approved`, or `review_expired`.

R21. `publication_status` MUST be one of `unpublished`, `published`, `hidden`, or `superseded`.

R22. A card version MUST be publication-eligible only when all of these conditions are true: `review_status = approved`; `publication_status` is `unpublished` or `hidden`; all required reviews from the review-routing matrix are complete for the current content digest; all required locales for the release stage are present and valid; all controlled taxonomy IDs validate against the active v1 taxonomy fixture or a later approved taxonomy version; the card is not blocked by safety category, missing elevated-risk definitions, licensing, media rights, or policy gates; and the version is not `superseded` or already replaced by a newer canonical successor for the same locale.

R23. Review transitions MUST be limited to the allowed transition table in this spec unless a later reviewed migration explicitly adds more.

R24. Publication transitions MUST be limited to the allowed transition table in this spec unless a later reviewed migration explicitly adds more.

R25. Review-sensitive edit behavior MUST follow the review-sensitive edit rules in this spec, including creation of a new unpublished version for review-sensitive edits to published content.

R26. Every lifecycle change MUST emit an immutable audit event with separate before and after values for `review_status` and `publication_status`.

R27. Published card history MUST preserve previous content version, reviewer identity, review date, and change summary.

R28. The content contract MUST support hiding a card without deleting its history.

R29. The content contract MUST support reverting a card to the last approved version.

R30. The system MUST expose enough validation output for contributors to know which field, taxonomy reference, locale branch, media reference, or review rule failed.

R31. Validation output MUST NOT expose private reviewer contact details, private health information, credentials, secrets, or machine-local paths.

R32. The schema MUST support content licensing metadata that distinguishes code from educational content and records content attribution.

R33. The schema MUST support DCO sign-off evidence or contribution provenance for public content contributions.

R34. The schema MUST allow cards to be discovered by equipment, exercise name, aliases, movement pattern, muscle, and difficulty.

R35. The schema SHOULD support card relationships such as alternative exercises, regressions, progressions, and related glossary terms because they improve beginner navigation.

R36. The schema SHOULD support comprehension-check prompts linked to a card because the vision defines beginner comprehension as a falsifiability check.

R37. The system MUST NOT encode personalized workout plans, user-specific prescriptions, diagnoses, injury-treatment pathways, or medical screening results in exercise cards.

R38. The first schema version MUST include a version identifier that can be used for migration checks.

R39. Breaking schema changes MUST include migration notes and compatibility checks before existing published cards are converted.

R40. The content contract MUST be usable without collecting personally identifiable user data.

## Lifecycle semantics

`review_status` answers whether a content version has the required approvals. `publication_status` answers whether that version is visible, hidden, unpublished, or replaced.

Review status values:

| Value | Meaning | Public visibility implication |
| --- | --- | --- |
| `draft` | The version is editable and has not been submitted for review. | Not publishable. |
| `in_review` | The version has been submitted and is awaiting one or more required reviews. | Not publishable. |
| `changes_requested` | At least one required reviewer requested changes. | Not publishable. |
| `approved` | All required reviews for the current version, locale, safety category, and change category are complete and current. | Eligible for publication if publication and validation invariants pass. |
| `review_expired` | The version was previously approved, but a review-sensitive edit or policy/taxonomy change invalidated the approval. | Not publishable until reapproved. |

Publication status values:

| Value | Meaning | Allowed with review states |
| --- | --- | --- |
| `unpublished` | The version is not publicly visible. | Any review status. |
| `published` | The version is publicly visible and canonical for its locale and card identity. | Only with `review_status = approved`. |
| `hidden` | The version is not publicly visible but remains retained for audit, emergency takedown, or temporary suppression. | Usually `approved`, but emergency hiding may occur regardless of review status. |
| `superseded` | The version has been replaced by a newer canonical version. | Terminal for public-canonical use; not publishable. |

Allowed review transitions:

| From | To | Trigger |
| --- | --- | --- |
| `draft` | `in_review` | Submit for review. |
| `in_review` | `approved` | All required reviewer approvals complete for current content digest. |
| `in_review` | `changes_requested` | Any required reviewer requests changes. |
| `changes_requested` | `draft` | Author resumes editing. |
| `changes_requested` | `in_review` | Author resubmits after changes. |
| `approved` | `review_expired` | Review-sensitive edit, policy change, safety category change, or taxonomy change invalidates approval. |
| `review_expired` | `in_review` | Resubmit invalidated version for review. |
| `review_expired` | `approved` | Only through a recorded review completion event; direct system mutation is forbidden. |

Validation MUST reject direct transitions from `draft` to `approved`, from `changes_requested` to `approved`, and from any non-approved state to `published`.

Allowed publication transitions:

| From | To | Trigger |
| --- | --- | --- |
| `unpublished` | `published` | Publish approved and eligible version. |
| `published` | `hidden` | Manual takedown, policy takedown, licensing issue, or safety issue. |
| `hidden` | `published` | Restore hidden version after eligibility recheck. |
| `published` | `superseded` | Newer approved successor is published. |
| `hidden` | `superseded` | Newer approved successor replaces hidden version. |
| `unpublished` | `superseded` | Draft or reviewed version is abandoned in favor of a newer version. |

`superseded` is terminal for canonical publication. Superseded versions may receive audit metadata corrections but MUST NOT become `published` again.

Review-sensitive edit rules:

1. Review-sensitive edits to `review_status = approved` and `publication_status = unpublished` versions MUST set `review_status = review_expired`.
2. Review-sensitive edits to `publication_status = published` versions MUST create a new unpublished version rather than mutating the published version in place.
3. The new version created from a published version MUST have `publication_status = unpublished` and `review_status = review_expired` unless the edit is an authoring-only clone before any review; in that case it may start as `draft`.
4. The previously published version remains `published` until an approved successor is published, hidden, or superseded.
5. Non-review-sensitive metadata edits, such as internal tags that do not affect user-facing meaning, may preserve `review_status`, but MUST be recorded in the audit log.

Lifecycle audit events MUST include `card_id`, `version_id`, `locale`, `event_type`, `review_status_before`, `review_status_after`, `publication_status_before`, `publication_status_after`, `actor_id`, `actor_role`, `required_review_tiers`, `completed_review_tiers`, `content_digest_before`, `content_digest_after`, `timestamp`, and `reason`. Audit output MUST NOT present review and publication state as one combined status.

## Review routing matrix

Publication eligibility MUST be computed from this matrix.

| Change category | Example fields | Required review tier | Review scope | Publication behavior |
| --- | --- | --- | --- | --- |
| Exercise mechanics | `setup`, `start_position`, `movement_phases`, `breathing`, `tempo`, `primary_muscles`, `secondary_muscles`, `stabilizers`, `common_mistakes`, `regressions`, `progressions` | `trainer` or `strength_coach` | Card-level content accuracy | Publishable after required card-level approval if no higher-risk fields changed. |
| Equipment setup | `equipment_adjustment`, `machine_settings`, `seat_height`, `strap_position`, `safety_stops`, `handle_options` | `trainer` or `strength_coach` | Card-level equipment safety and clarity | Publishable after card-level approval if no higher-risk fields changed. |
| General training principle | `sets_reps`, `effort_level`, `progressive_overload`, `warmup`, `rest`, `weekly_balance` | `strength_coach` or `trainer` | Card-level training principle accuracy | Publishable after card-level approval if no medical or pain-policy claims are introduced. |
| Standard safety note copied unchanged from approved template | `standard_safety_note_id` | `trainer` or `strength_coach` confirms correct template selection | Template application only | Publishable if the underlying template remains approved. |
| Card-specific pain, symptom, contraindication, or referral language | `what_not_to_feel`, `stop_rules`, `contraindications`, `when_to_seek_help`, `pain_notes` | `physical_therapist` | Card-level safety-language review | Not publishable until PT review is complete. |
| Safety-language policy template | Global safety copy, pain-rule templates, non-emergency referral prompts | `physical_therapist` | Policy-level safety-language review | Existing cards using the changed template become `review_expired` if the change alters meaning. |
| Emergency criteria, medical disclaimer, urgent-care criteria | Emergency stop rules, chest-pain/dizziness/fainting rules, medical disclaimer, clinical escalation text | `sports_medicine_clinician` | Policy-level clinical-safety review | Not publishable until clinician review is complete. Existing dependent cards become blocked or `review_expired` if semantics change. |
| Elevated-risk card | Barbell maximal lifting, plyometrics, sprinting, complex Olympic-lift derivatives, pain/injury-adjacent content, or any card tagged `safety_category = elevated_risk` | `sports_medicine_clinician` plus `strength_coach` or `trainer` | Card-level elevated-risk review | Not publishable unless elevated-risk category definitions are approved and both card-level reviews are complete. |
| Rehab, diagnosis, injury treatment, or medical-condition programming | Any content presenting diagnosis, treatment, post-surgical rehab, disease-specific programming, or injury-resolution claims | `sports_medicine_clinician` and legal/product policy review if later admitted | Out of MVP scope | Blocked from publication in v1 by `safety_category = blocked_rehab`. |
| Media that changes exercise interpretation | New video, diagram, animation, labeled muscle map, or photo sequence | Same tier as the content fields depicted | Media-content equivalence and safety review | Not publishable until media and corresponding content review are aligned. |
| Locale translation with no semantic change | `localized_title`, `localized_steps`, captions, transcript | `locale_reviewer`; safety-sensitive text also requires same domain tier or verified approved source equivalence | Translation equivalence | Publishable only when translation preserves approved source meaning. |
| Taxonomy enum addition or semantic change | `card_type`, `difficulty`, `safety_category`, `review_tier`, `license_kind`, `media_kind`, movement/equipment/muscle taxonomy | `schema_owner`; domain reviewer required for safety, muscle, equipment, or review-tier semantics | Taxonomy governance | Not active until approved taxonomy version is published. Fixtures must validate against the active taxonomy version. |
| Licensing or rights change | `license_kind`, `rights_holder`, `asset_license`, `attribution`, `expiration_date` | `content_ops` or legal owner; elevated risk if safety media is removed or altered | Rights and publication eligibility | Public publication blocked if rights are missing, expired, or `unlicensed_internal_only`. |

`review_tier` identifies the minimum credential or role required for an approval event. The approval event MUST include the tier, reviewer identity, scope, timestamp, and content digest reviewed.

Allowed v1 review tiers are `trainer`, `strength_coach`, `physical_therapist`, `sports_medicine_clinician`, `schema_owner`, `locale_reviewer`, `content_ops`, and `legal_policy`.

If multiple rows apply to a change, the highest-risk applicable review obligations are cumulative. A trainer approval does not satisfy a physical-therapist or sports-medicine-clinician requirement.

Before elevated-risk categories and clinician-review criteria are approved, content with `safety_category = elevated_risk` MUST be allowed only with `publication_status = unpublished`. It MUST NOT be publication-eligible. Publication requests MUST fail with `elevated_risk_policy_not_defined`.

## Minimum v1 controlled enums

All enum values in this section are normative for `content-schema-v1`. New values require a reviewed taxonomy change.

`card_type`: `exercise`, `equipment_guide`, `movement_pattern`, `training_principle`, `safety_policy`, `glossary`.

`difficulty`: `beginner`, `beginner_plus`, `intermediate`, `advanced`. V1 beginner release may block `advanced` cards from public publication through release policy, but the enum is valid.

`safety_category`:

| Value | Meaning | Publication rule |
| --- | --- | --- |
| `standard` | General beginner fitness education with no special pain, injury, medical, or high-complexity risk. | Publishable with trainer/strength-coach approval. |
| `caution` | Includes common risk notes, body-area caution, or non-diagnostic stop rules. | Requires review matrix routing; may require PT review. |
| `elevated_risk` | Movement, intensity, population, or context requires clinician-defined elevated-risk handling. | Blocked unless elevated-risk definitions and required clinician/card reviews are approved. |
| `blocked_rehab` | Diagnosis, rehab, injury treatment, medical condition programming, or post-surgical guidance. | Not publishable in v1. |
| `policy_only` | Safety, disclaimer, or governance policy content not rendered as a standard exercise card. | Governed by policy review rows. |

`review_status`: `draft`, `in_review`, `changes_requested`, `approved`, `review_expired`.

`publication_status`: `unpublished`, `published`, `hidden`, `superseded`.

`review_tier`: `trainer`, `strength_coach`, `physical_therapist`, `sports_medicine_clinician`, `schema_owner`, `locale_reviewer`, `content_ops`, `legal_policy`.

`review_scope`: `card_content`, `equipment_setup`, `movement_mechanics`, `training_principle`, `safety_language_policy`, `card_safety_language`, `emergency_criteria_policy`, `elevated_risk_card`, `taxonomy_change`, `media_equivalence`, `translation_equivalence`, `licensing`.

`locale`: `en-US`, `zh-Hans`. Additional locales require reviewed taxonomy extension.

Bare `en` is not a valid v1 locale key. Future English variants such as `en-GB`, `en-CA`, or `en-AU` require reviewed taxonomy extension before content validation may accept them.

`contribution_provenance`: `expert_authored`, `staff_authored_expert_reviewed`, `ai_assisted_expert_reviewed`, `imported_licensed_expert_reviewed`, `user_submitted_unreviewed`. `user_submitted_unreviewed` is never publishable. AI-assisted content is publishable only when the final content digest has completed the same required expert review as non-AI content.

`media_kind`: `video`, `image`, `diagram`, `animation`, `thumbnail`, `caption_file`, `transcript`, `audio`.

`license_kind`: `owned`, `third_party_licensed`, `cc_by`, `cc_by_sa`, `public_domain`, `unlicensed_internal_only`. `unlicensed_internal_only` assets are not publishable in public cards.

`movement_pattern`: `squat`, `hinge`, `lunge`, `push_horizontal`, `push_vertical`, `pull_horizontal`, `pull_vertical`, `carry`, `brace_anti_extension`, `brace_anti_rotation`, `rotation`, `locomotion`, `cardio_rowing`, `cardio_cycling`, `cardio_running`, `mobility`.

`muscle_role`: `primary`, `secondary`, `stabilizer`.

`equipment_kind`: `bodyweight`, `dumbbell`, `barbell`, `kettlebell`, `cable_machine`, `selectorized_machine`, `bench`, `resistance_band`, `rowing_machine`, `stationary_bike`, `treadmill`, `mat`, `sled`, `pullup_assist_machine`.

Full muscle and equipment lists may live in a companion taxonomy fixture, but validation fixtures MUST include at least the enum values above before architecture or test-spec relies on taxonomy validation.

## Inputs and outputs

Inputs:

- Exercise-card records authored or edited by contributors.
- Taxonomy records for equipment, muscles, movement patterns, card types, difficulty levels, and safety categories.
- Canonical SVG step media references and accessible text.
- Supplemental media references when present.
- Review metadata, review decisions, lifecycle state, and lifecycle audit events.
- Contribution provenance and content licensing metadata.

Outputs:

- Validated card records eligible for publication.
- Validation error reports with field-level or rule-level failures.
- Review-state changes for `review_status`.
- Publication-state changes for `publication_status`.
- Publication-ready structured content for future UI, search, and static rendering.
- Audit history for content versions and review-sensitive changes.

## State and invariants

- Published cards always have `review_status = approved`.
- Published cards always have at least one valid English locale branch.
- Published cards always have canonical SVG steps and accessible text.
- Published cards always satisfy all applicable review matrix rows.
- Review-sensitive changes cannot silently remain published.
- Locale additions do not change stable card IDs.
- Hiding a card does not delete review history.
- Superseded versions cannot become canonical published versions again.
- Supplemental media is never the source of truth.
- Exercise cards never store user health profiles, diagnoses, or personalized workout plans.

## Error and boundary behavior

- Missing required localized fields produce validation errors naming the locale and field.
- A publishable card without `locales.en-US` produces a validation error.
- A card using `locales.en` produces an unknown-locale validation error in v1.
- A source containing both `locales.en` and `locales.en-US` is invalid and requires manual migration resolution.
- A future locale such as `en-GB` is invalid until an approved taxonomy extension containing that locale is active.
- Unknown taxonomy references produce validation errors naming the reference and allowed taxonomy type.
- Missing canonical SVG steps, too few steps, or too many steps produce validation errors.
- Missing accessible text for canonical media produces validation errors.
- Medical-diagnosis or treatment language blocks publication until removed or reclassified by a safety-governance spec.
- Missing required review metadata blocks publication.
- Invalid review or publication transitions are rejected with transition-specific errors.
- Review-sensitive edits to published cards create a new unpublished version and leave the published version unchanged unless separately hidden or superseded.
- Publication requests for elevated-risk content fail with `elevated_risk_policy_not_defined` until elevated-risk policy and required review routes are approved.
- Publication requests for `blocked_rehab` content fail in v1.
- Licensing or attribution gaps block public content contribution acceptance.
- Unsupported locale keys are rejected unless the locale is added to the allowed locale list through a reviewed schema change.

## Compatibility and migration

- The initial schema version is `content-schema-v1`.
- Existing cards created under `content-schema-v1` must remain readable after non-breaking additions.
- Adding a new optional field is compatible when validation supplies a safe default or treats the field as absent.
- Renaming, deleting, or changing meaning of stable fields, taxonomy IDs, review statuses, publication statuses, locale keys, or media-reference semantics is breaking.
- Breaking changes require migration notes, test fixtures for old and new records, and rollback guidance.
- The schema must support adding Chinese locale branches without migrating English-only cards.

### Locale migration note

Earlier draft examples used `en` as the English locale key. In v1, `en` is not a valid locale key. Any draft fixture, example, or unpublished content using `locales.en` should be migrated to `locales.en-US`.

If both `locales.en` and `locales.en-US` appear in the same source during migration, the migration must fail and require manual resolution. The system MUST NOT merge locale branches automatically.

## Observability

- Validation must report counts of valid cards, invalid cards, warnings, and review-sensitive changes.
- Validation must report failures by card ID, locale, field, taxonomy type, media reference, review rule, or licensing rule.
- Review and publication state changes must record actor or reviewer identity as intended for publication, timestamp or date, previous state, new state, content digest, required review tiers, completed review tiers, and change summary.
- Hidden and reverted cards must remain auditable.
- Audit output must keep `review_status` and `publication_status` separate.
- No runtime analytics are required by this spec; analytics belong to a later UX or product telemetry spec.

## Security and privacy

- Exercise-card records must not contain secrets, credentials, private machine paths, private reviewer contact details, private user data, or personal health information.
- The schema must not require user accounts, user profiles, or personally identifiable information.
- Public reviewer identity may be recorded only as the name or public identifier intended for display.
- Legal and licensing metadata must be sufficient to distinguish Apache 2.0 code from CC BY 4.0 educational content before public content contributions begin.
- Content must not include unconstrained AI-generated exercise guidance as source-of-truth text.

## Accessibility and UX

- Required content fields must support plain-language explanations.
- Canonical SVG steps must have localized accessible text for each published locale.
- Supplemental video, when later allowed, must include captions or transcript references before publication.
- Error messages should identify the contributor action needed to fix validation failures.
- The schema must support glossary links for technical terms so future UI can explain anatomy and movement language.

## Performance expectations

- Validation of the first-release pilot set of 40 to 60 cards should complete in under 10 seconds on a typical developer machine.
- Validation output should remain deterministic for the same inputs.
- Search indexing performance is not specified here; search behavior belongs to a later UX/search spec.

## Edge cases

EC1. A card has English content but no Chinese content: valid when all English requirements and reviews pass.

EC2. A card has Chinese localized text but missing Chinese accessible text for SVG steps: invalid for publishing the Chinese locale.

EC3. A contributor changes only an alias: valid without safety re-review unless the alias introduces medical, misleading, or unsafe language.

EC4. A contributor changes a stop sign: review-sensitive and cannot stay published without required review approval.

EC5. A taxonomy ID is deprecated: existing cards remain readable, and migration notes define the replacement.

EC6. A supplemental video contradicts reviewed text: invalid until removed or reconciled through review.

EC7. A card for a mobility drill appears to imply pain treatment: invalid because rehab or diagnosis claims are out of scope.

EC8. A reviewer leaves the project: historical review records remain visible, and future changes require a current reviewer.

EC9. A published version receives a review-sensitive edit: the public version remains unchanged and a new unpublished version is created for review.

EC10. A hidden approved version is restored: eligibility is recalculated before publication.

EC11. A card uses `safety_category = elevated_risk` before elevated-risk policy is approved: publication is rejected.

EC12. A public card uses a media asset with `license_kind = unlicensed_internal_only`: publication is rejected.

## Non-goals

- This spec does not define the frontend page layout, search UI, quizzes, learning paths, or analytics UI.
- This spec does not choose the repository format, database, CMS, framework, package manager, hosting model, or deployment model.
- This spec does not define Terms of Use, Privacy Policy, incident response, or final legal language.
- This spec does not define the full safety-governance policy or the exact elevated-risk card taxonomy.
- This spec does not define personalized workout generation, AI answer behavior, camera form analysis, coach dashboards, or rehabilitation pathways.
- This spec does not select the exact first 40 to 60 exercise cards.

## Acceptance criteria

AC1. A valid sample English card for lat pulldown can be represented with all required fields, taxonomy references, SVG step references, review metadata, safety notes, and disclaimer text.

AC2. A valid sample card can add a `zh-Hans` locale branch without changing the card ID or schema shape.

AC3. Validation rejects a card with an unknown muscle, equipment, movement-pattern, difficulty, or safety taxonomy ID.

AC4. Validation rejects a publishable card with fewer than three or more than six canonical SVG step references.

AC5. Validation rejects canonical SVG steps missing localized accessible text for a published locale.

AC6. Validation rejects diagnosis or treatment claims such as "fixes sciatica" or "treats knee pain."

AC7. Validation blocks publication when required review metadata is missing.

AC8. Given a card version with `review_status = draft` and `publication_status = unpublished`, a publish attempt is rejected with `review_not_approved`.

AC9. Given a card version with `review_status = approved`, `publication_status = unpublished`, valid taxonomy, valid licensing, and complete required reviews, a publish attempt transitions `publication_status` to `published`.

AC10. Given a card version with `review_status = approved` and `publication_status = published`, a review-sensitive edit creates a new version with `publication_status = unpublished` and does not mutate the public version in place.

AC11. Given an approved unpublished version, a review-sensitive edit transitions `review_status` to `review_expired`.

AC12. Given a published version, a manual safety takedown transitions `publication_status` to `hidden` and records an audit event with before/after review and publication states.

AC13. Given a hidden approved version, restoring it to `published` succeeds only if publication eligibility is recalculated and passes.

AC14. Given a newer approved successor version is published, the previous canonical published version transitions to `superseded`.

AC15. Given a `superseded` version, a publish attempt is rejected with `version_superseded`.

AC16. A change only to exercise setup or movement-phase instructions routes to `trainer` or `strength_coach` review and does not require PT or clinician review unless safety-sensitive fields changed.

AC17. A card-specific change to `stop_rules`, `what_not_to_feel`, `contraindications`, or `when_to_seek_help` requires `physical_therapist` review before publication.

AC18. A change to emergency criteria or medical-disclaimer policy requires `sports_medicine_clinician` review before any dependent content is publication-eligible.

AC19. A card tagged `safety_category = elevated_risk` is not publication-eligible until elevated-risk definitions are approved and card-level clinician plus strength-coach/trainer reviews are complete.

AC20. A card tagged `safety_category = blocked_rehab` is rejected for public publication in v1 regardless of other approvals.

AC21. When multiple review-matrix rows apply, validation requires all applicable review tiers and reports every missing tier.

AC22. Validation accepts every enum value listed in the v1 controlled enums section.

AC23. Validation rejects unknown values for `card_type`, `difficulty`, `safety_category`, `review_status`, `publication_status`, `review_tier`, `media_kind`, `locale`, `contribution_provenance`, and `license_kind`; specifically, `locale = en` is rejected as an unknown v1 locale key.

AC24. A taxonomy extension is unavailable to content validation until an approved taxonomy version containing the new value is active.

AC25. A card using `locale = zh-Hans` and `locale = en-US` validates if all locale-required fields are present.

AC25a. A publishable card without `locales.en-US` is rejected.

AC25b. A migration source containing both `locales.en` and `locales.en-US` is rejected and requires manual resolution.

AC25c. A card using a future English variant such as `en-GB` is rejected until an approved taxonomy extension containing that locale is active.

AC26. A public card using a media asset with `license_kind = unlicensed_internal_only` is rejected with `license_not_public`.

AC27. A card with `contribution_provenance = user_submitted_unreviewed` is rejected for publication with `expert_review_required`.

AC28. Every review-status change records `review_status_before` and `review_status_after`.

AC29. Every publication-status change records `publication_status_before` and `publication_status_after`.

AC30. Lifecycle audit output never uses a single combined lifecycle status in place of the two required fields.

AC31. Review approval events include reviewer tier, scope, reviewer identity, timestamp, and content digest.

AC32. The content contract can represent attribution and content-license metadata for educational content separately from code licensing.

AC33. Validation output identifies the failing card ID, field or rule, and actionable reason without exposing secrets or private data.

AC34. The spec is sufficient for architecture to decide storage, validation pipeline, review workflow, media handling, and publication boundaries.

## Open questions

- What concrete storage format will implement this contract: repository files, CMS records, generated static data, or another model?
- Who approves the final disclaimer language before public beta?
- What exact content-license metadata is required for CC BY 4.0 attribution?
- What companion taxonomy fixture format will hold full muscle and equipment lists beyond the v1 seed enums?

These questions do not block spec review because the contract defines the required behavior and leaves implementation and policy details to downstream architecture and companion specs.

## Next artifacts

1. Spec review for this content/schema spec.
2. Safety and governance spec for disclaimers, stop rules, elevated-risk categories, review tiers, and incident response.
3. Contribution and licensing spec for CC BY 4.0 content, Apache 2.0 code, DCO sign-offs, attribution, and no-CLA posture.
4. UX/search spec for exercise pages, equipment lookup, glossary, comprehension checks, and accessibility expectations.
5. Architecture package after core specs are reviewed.
6. Test specification mapping requirements and acceptance criteria to automated and manual checks.

## Follow-on artifacts

- Architecture: `docs/architecture/system/architecture.md`
- ADR: `docs/adr/2026-06-26-repository-native-reviewed-content.md`

## Readiness

This spec is approved by `docs/changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r3.md`. It is ready for architecture. It is not plan-ready, implementation-ready, or release-ready until architecture review, planning, test specification, and required reviews are complete.
