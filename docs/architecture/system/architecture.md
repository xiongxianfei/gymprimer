# GymPrimer System Architecture

## Status

- approved

## Related artifacts

- Proposal: `../../proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
- Spec: `../../../specs/content-schema.md`
- Spec review: `../../changes/beginner-fitness-exercise-education-platform/reviews/spec-review-r3.md`
- Plan: `../../plans/2026-06-26-content-schema-foundation.md`
- ADRs:
  - `../../adr/2026-06-26-repository-native-reviewed-content.md`

## Introduction and Goals

This architecture defines how GymPrimer should store, validate, review, publish, and render the approved content schema for beginner exercise education. It covers the content platform boundary, not a complete end-user application stack.

Goals:

- Keep reviewed exercise content, taxonomy, policy templates, audit events, and canonical SVG media versioned in the repository.
- Make publication a validation result, not an author assertion.
- Preserve English-first launch content with `en-US` as the required v1 English locale and `zh-Hans` as a first-class future locale.
- Keep reviewed text and SVG step cards as canonical source-of-truth media.
- Support later UI, search, analytics, and constrained AI layers without making them authoritative.

Stakeholders are beginner readers, content authors, expert reviewers, translators, illustrators, maintainers, and future application engineers.

## Architecture Constraints

- `CONSTITUTION.md` and `VISION.md` govern scope: GymPrimer is educational, not medical advice, rehab, workout prescription, or AI coaching.
- `specs/content-schema.md` is the approved behavior contract for content records, lifecycle state, locale keys, taxonomy values, review routing, audit events, and validation outcomes.
- Public cards must include `locales.en-US`; bare `en` is invalid in v1.
- Public content must pass schema, taxonomy, locale, review, lifecycle, licensing, safety-language, and media checks before publication.
- The repository currently has no app stack, package manager, CI, source tree, deployment target, or existing content fixtures; this architecture must not assume a framework.
- No user accounts, user health profiles, private reviewer contact details, secrets, PHI, or personalized medical data are part of this content architecture.

## Context and Scope

The system boundary is the GymPrimer repository plus generated publication artifacts produced from reviewed source content. Human contributors and agents edit files in the repository. Expert reviewers approve content through review events recorded against content digests. A validator checks source files and produces validation reports plus publication-ready structured output for a later website or app.

Out of scope for this architecture:

- Frontend page layout, search UI, quizzes, and analytics UI.
- Runtime hosting provider, CMS SaaS provider, authentication, payments, and AI services.
- Final Terms of Use, Privacy Policy, legal counsel review, and incident-response process.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

## Solution Strategy

Use repository-native reviewed content as the source of truth:

- Author canonical records as text files under `content/`.
- Store schema contracts under `schemas/`.
- Store canonical SVG step cards and accessible text references under `media/`.
- Store append-only lifecycle and review audit evidence under `content/audit/`.
- Run a validator that reads all source content, active taxonomy fixtures, media metadata, lifecycle states, and review events.
- Emit deterministic validation reports and publication-ready generated content under a generated-output boundary.

This favors diffability, OSS review, licensing clarity, and low launch complexity over CMS convenience. A CMS may be added later as an adapter only if it round-trips to the repository source-of-truth model and preserves content digests, review events, and publication gates.

## Building Block View

Top-level source layout:

| Area | Responsibility |
| --- | --- |
| `specs/` | Approved behavioral contracts and future test specifications. |
| `schemas/` | Machine-readable schema definitions for cards, taxonomy, media metadata, review events, audit events, and validation reports. |
| `content/cards/` | Versioned exercise, equipment, movement-pattern, training-principle, safety-policy, and glossary records. |
| `content/taxonomy/` | Active and historical taxonomy fixtures, including v1 controlled enum values and later reviewed extensions. |
| `content/policies/` | Safety-language templates, disclaimer templates, elevated-risk policy definitions, and review-routing policy records. |
| `content/audit/` | Immutable lifecycle, review, publication, migration, and takedown events keyed by card/version/locale/content digest. |
| `media/svg/` | Canonical SVG step cards and metadata for source-of-truth movement media. |
| `media/supplemental/` | Optional non-canonical media metadata and rights records; video is not required for publication. |
| `tools/validation/` | Validator CLI and reusable validation rules. Implementation language is deferred to planning. |
| `generated/` | Deterministic publication output and validation reports; generated content is not the reviewed source of truth. |

Logical containers:

- **Source content repository**: reviewed text, taxonomy, policy, media metadata, and audit files.
- **Validation and publication gate**: deterministic checks for schema, taxonomy, locales, lifecycle transitions, review routing, licensing, media, safety language, and migration conflicts.
- **Generated content package**: normalized public content consumed by future UI/search layers.
- **Future presentation layer**: website or app that renders only generated, validated content.
- **Future optional retrieval layer**: constrained AI or Q&A layer that may read generated reviewed content but cannot create source-of-truth exercise guidance.

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

## Runtime View

Primary authoring and publication flow:

1. An author creates or edits a content card, taxonomy fixture, policy template, media metadata, or SVG asset in repository source files.
2. The validator computes content digests and classifies changed fields against the review-routing matrix.
3. If required fields, locale keys, taxonomy IDs, media references, or license metadata are invalid, validation fails with card ID, locale, field or rule, and reason.
4. If review-sensitive fields changed, the validator requires matching review events for the current content digest and required review tiers.
5. A publish attempt succeeds only when `review_status = approved`, `publication_status` is `unpublished` or `hidden`, all required reviews are complete, licensing and media rights pass, locale requirements pass, and policy gates pass.
6. Publication emits generated public content and lifecycle audit events; the source content and audit records remain reviewable text.

Review-sensitive edit flow:

1. A published version is never mutated in place for review-sensitive edits.
2. The edit creates a new unpublished version with `review_status = review_expired` or `draft` when allowed by the spec.
3. The previous public version remains published until the successor is approved and published, hidden, or superseded.

Failure paths:

- Bare `locales.en`, missing `locales.en-US`, both `locales.en` and `locales.en-US`, unknown taxonomy values, missing SVG accessible text, `blocked_rehab`, unlicensed public media, and unresolved elevated-risk policy all fail before publication.
- Generated output is discarded on validation failure; source files remain for correction.

## Deployment View

The launch architecture is static-content friendly and repository-centered.

Environments:

- **Authoring environment**: local clone or pull request environment where contributors edit content and run validation.
- **Review environment**: pull request or maintainer review where domain approvals and lifecycle events are checked against content digests.
- **Publication environment**: CI or release job, once created, runs validation and publishes only generated artifacts that pass the content gate.

Packaging boundaries:

- `content/`, `schemas/`, `media/`, and `specs/` are source packages.
- `generated/` is reproducible output and may be ignored locally or attached to releases depending on the future deployment plan.
- The future website/app must consume generated validated content, not raw draft content.

No live deployment target is chosen here. Hosting and framework selection belong to a later architecture update or ADR once UX/search requirements are approved.

## Crosscutting Concepts

Validation:

- Validation is the central architecture boundary. It must be deterministic for the same inputs and complete under 10 seconds for the 40-60 card pilot set.
- Validation reports failures by card ID, locale, field, taxonomy type, media reference, review rule, licensing rule, or lifecycle rule.

Review and lifecycle:

- `review_status` and `publication_status` remain separate in source records, generated records, validation reports, and audit events.
- Review approvals are valid only for the content digest, locale, review scope, reviewer tier, and taxonomy/policy version they reviewed.

Localization:

- `en-US` is required for public cards.
- `zh-Hans` uses the same locale field shape.
- Future locales require reviewed taxonomy extension.

Security and privacy:

- Source and generated artifacts must not contain secrets, private paths, private reviewer contacts, user PII, PHI, or user health profiles.
- Public reviewer identity is limited to the public name or identifier intended for display.

Media:

- Canonical SVG media is reviewed source-of-truth media together with reviewed text.
- Supplemental media can never override reviewed text/SVG and must pass licensing, accessibility, and equivalence checks.

Licensing:

- Code remains Apache 2.0.
- Educational content is prepared for CC BY 4.0 attribution metadata.
- `unlicensed_internal_only` assets are blocked from public cards.

## Architecture Decisions

- [ADR 2026-06-26: Repository-native reviewed content](../../adr/2026-06-26-repository-native-reviewed-content.md) - Use repository versioned source files plus deterministic validation and generated publication output as the initial content architecture.

## Quality Requirements

| Quality | Scenario | Measure |
| --- | --- | --- |
| Reviewability | A reviewer opens a pull request changing an exercise card, taxonomy value, SVG step, or safety template. | The meaningful content, media metadata, review event, and audit changes are visible as text diffs, with SVG source diffable. |
| Safety | A contributor edits stop rules, contraindications, pain notes, emergency criteria, or elevated-risk content. | Validation identifies every missing required review tier and blocks publication until required current approvals exist. |
| Localization | A contributor adds `zh-Hans` to an approved `en-US` card. | Validation checks the same locale field shape and accessible media text without changing card ID. |
| Compatibility | A future locale such as `en-GB` appears before taxonomy approval. | Validation rejects it until an approved taxonomy extension is active. |
| Performance | A contributor validates the first-release pilot set. | Validation completes in under 10 seconds on a typical developer machine. |
| Privacy | Generated validation output is published in CI logs. | Output contains no secrets, private reviewer contacts, machine-local paths, PHI, or user private data. |

## Risks and Technical Debt

- No validator, schemas, content fixtures, package manager, CI, or generated-output convention exists yet.
- The architecture chooses a repository-native source-of-truth model before a CMS decision. A later CMS adapter must not weaken review digest, audit, or publication gates.
- Full muscle and equipment taxonomy fixtures are deferred beyond the v1 seed values.
- Legal documents, final disclaimer owner, incident response, and content-license metadata details need follow-on specs before public beta.
- The first real implementation must decide a validation toolchain and file serialization format details without changing the approved content contract.

## Glossary

- **Canonical source**: Reviewed repository content and SVG media that define public exercise guidance.
- **Generated content package**: Deterministic output produced from validated source content for a future UI or release.
- **Publication gate**: The validator rules that decide whether a content version may become public.
- **Review event**: A recorded approval or change request tied to reviewer tier, scope, content digest, locale, and timestamp.
- **Audit event**: Immutable lifecycle or publication event with before/after review and publication states.

## Next artifacts

- Plan review.

## Follow-on artifacts

- Test specification for the approved content schema and this architecture.
- Safety and governance spec for legal disclaimers, elevated-risk definitions, incident response, and policy ownership.
- Contribution and licensing spec for CC BY 4.0 attribution, DCO sign-offs, and content provenance.
- UX/search spec for rendering, discovery, glossary, and comprehension checks.

## Readiness

This architecture package was approved by `../../changes/beginner-fitness-exercise-education-platform/reviews/architecture-review-r1.md`. It is ready to support planning. It is not implementation-ready or release-ready until plan review, test specification, test-spec review, implementation, code review, final verification, and PR handoff are complete.
