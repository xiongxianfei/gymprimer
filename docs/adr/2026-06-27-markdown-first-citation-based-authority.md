# ADR 2026-06-27: Markdown-First Citation-Based Authority

## Status

accepted

Amended on 2026-06-30 by the forward-head-posture pattern architecture work to
replace separate audit-artifact requirements with recorded review evidence
under the normal change record.

Supersedes: `docs/adr/2026-06-26-repository-native-reviewed-content.md`

## Context

GymPrimer's accepted direction changed from a structured, expert-reviewed content platform to a Markdown-first beginner primer. The approved spec for v0.1 requires five GitHub-readable Markdown pages, page-local disclaimers and sources, claim-level safety citations, conservative beginner scope, no external media assets, optional derived mdBook output, and a non-canonical first-card spike before broad promotion.

The prior ADR chose repository-native reviewed content with schemas, lifecycle state, review events, audit events, deterministic validation, and generated public content. That architecture was coherent for a future reviewed platform, but it is too heavy for the current proof: whether beginners can use the Markdown content.

## Decision

Use Markdown files as the canonical source of truth for GymPrimer v0.1.

The initial architecture is a repository-readable Markdown corpus with:

- root navigation in `README.md`;
- reusable source index in `SOURCES.md`;
- contribution rules in `CONTRIBUTING.md`;
- content license clarification in `CONTENT_LICENSE.md`;
- five first-slice pages under numbered beginner directories;
- optional original diagrams under `media/`;
- optional minimal mdBook configuration only after Markdown pages work directly;
- lightweight checks for disclaimers, page-local sources, claim-level safety citations, excluded scope, media paths, links, privacy, and optional mdBook build.

Citation-based authority replaces the unavailable expert-review lifecycle for v0.1. The project must not claim a page is expert-reviewed unless a named reviewer and review evidence exist for that specific page.

## Alternatives considered

- Continue repository-native reviewed content with schemas, review lifecycle, audit events, and generated public JSON: rejected for v0.1 because it delays content proof and depends on reviewers and platform machinery the project does not yet have.
- Markdown-only repository with no derived output: viable but too austere once the five pages exist; mdBook remains a low-cost optional derived output.
- Hosted static site using Astro, Hugo, or Next.js: rejected for v0.1 because framework, routing, deployment, styling, and maintenance distract from content proof.
- CMS or database source of truth: rejected because the repository itself is the product and there is no operational need for content infrastructure yet.
- AI-assisted explainer: rejected because fitness guidance needs a stable, source-backed corpus and safety guardrails before conversational behavior is considered.

## Consequences

Benefits:

- Beginners and contributors can inspect the product directly in GitHub.
- Content proof can happen before platform proof.
- Citation requirements are page-local and auditable.
- The repo can still generate optional static HTML later without changing source authority.
- Old schema and generated-output work remains traceable as history.

Costs and risks:

- Search, filtering, generated public packages, and lifecycle automation are deferred.
- Citation quality and scope discipline depend on maintainer review until check tooling exists.
- GitHub navigation must be kept clear enough for beginners.
- Future translation, media, and reviewer attribution need later architecture/spec work before becoming active.

Compatibility and migration:

- Stable Markdown paths and headings become compatibility surfaces once linked.
- Existing structured-platform artifacts are historical unless reactivated by a later accepted proposal.
- Generated JSON from the old platform is not a v0.1 product surface.
- mdBook output, if added, is derived and can be removed without invalidating Markdown pages.

## Follow-up

- Review this architecture package.
- Decide whether old artifacts are marked superseded in place or moved under an archive path.
- Create first-slice check tooling or recorded review evidence.
- Create the card template and contributor guidance.
