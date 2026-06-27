# ADR 2026-06-26: Repository-Native Reviewed Content

## Status

accepted

## Context

GymPrimer needs a content architecture for reviewed beginner exercise education before implementation planning. The approved spec requires locale-aware card records, controlled taxonomy, canonical SVG step media, separate review and publication lifecycle state, immutable audit events, content digests, deterministic validation, licensing checks, and publication gates. The repository currently has no CMS, app stack, package manager, CI, content fixtures, or deployment target.

A durable decision is needed because storage and validation boundaries will shape content authoring, review workflow, migration behavior, generated output, and future UI/search/AI integration.

## Decision

Use repository-native reviewed content as the initial source of truth.

The architecture will store source content, taxonomy fixtures, policy templates, media metadata, canonical SVG assets, review events, and audit events as reviewable repository files. A deterministic validator will read those files and machine-readable schemas, compute content digests, enforce the approved content contract, and emit generated publication-ready content only when all gates pass.

Generated output may feed a future website, search index, or constrained retrieval layer, but generated output is not the reviewed source of truth. A future CMS may be added only as an adapter that preserves repository source files, digest-scoped review evidence, audit events, and publication eligibility rules.

## Alternatives considered

- CMS-first content storage: rejected for v1 because it adds provider choice, authentication, export, audit, and migration complexity before the schema and review workflow are proven.
- Application database as source of truth: rejected for v1 because there is no app stack yet and it would make OSS content review less diffable.
- Static Markdown pages only: rejected because the approved spec requires structured locales, taxonomy, review routing, lifecycle state, audit events, licensing, and media validation.
- Video/media platform as source of truth: rejected because the vision and spec make reviewed text plus SVG step cards canonical and video supplemental only.

## Consequences

Benefits:

- Content, schema, media metadata, review evidence, and audit records are diffable in pull requests.
- Validation can run locally and later in CI without a hosted CMS.
- The architecture fits the open-source contribution model and Apache 2.0 / CC BY 4.0 licensing posture.
- Future UI, search, and AI layers can consume generated reviewed content without becoming authoritative.

Costs and risks:

- The project must implement schema files, fixtures, validator tooling, generated-output conventions, and CI later.
- Large media assets and high-volume audit records may eventually require storage conventions or an external asset adapter.
- A future CMS integration will need careful round-trip and digest preservation rules.
- Repository-native authoring may be less friendly for non-technical reviewers until review tooling improves.

Compatibility and migration:

- Public schema fields, locale keys, taxonomy IDs, lifecycle states, review event shape, audit event shape, and media references are compatibility surfaces.
- Migration from earlier draft `locales.en` to `locales.en-US` must fail on conflict and must not merge locale branches automatically.

## Follow-up

- Define concrete file formats and schema files during planning or implementation.
- Add validation fixtures for cards, taxonomy, media metadata, review events, audit events, and generated output.
- Add CI once validation tooling exists.
- Revisit CMS adapter only after repository-native validation and review workflow are stable.
