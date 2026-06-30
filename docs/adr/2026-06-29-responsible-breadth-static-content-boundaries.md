# ADR 2026-06-29: Responsible Breadth Static Content Boundaries

## Status

accepted

Amended on 2026-06-30 by the forward-head-posture pattern architecture work to
replace separate audit-artifact requirements with recorded review evidence
under the normal change record.

## Context

GymPrimer has accepted the Responsible Breadth direction and approved
`specs/responsible-breadth.md`. The project is widening from the original
Markdown-first exercise-literacy v0.1 slice into static, citation-based
education for common patterns, well-studied conditions, programming principles,
static program examples, and expanded exercise pages.

The change affects repository layout, page classification, source-quality
validation, safety routing, review evidence, and promotion boundaries. It
must preserve the original Markdown-first five-page contract and must not turn
GymPrimer into a symptom checker, diagnostic product, treatment planner,
personalized programming engine, CMS, hosted app, or AI-generated source of
truth.

## Decision

Use path-classified Markdown page classes for the first Responsible Breadth
slice:

- `patterns/*.md` -> `pattern_page`
- `conditions/*.md` -> `condition_page`
- `principles/*.md` -> `programming_principle_page`
- `programs/*.md` -> `program_example_page`
- `exercises/*.md` -> `expanded_exercise_page`

Use `about/` for shared project-level references such as red flags and
authorship/sources guidance.

Keep `specs/markdown-first-primer.md` active for the original five-page v0.1
slice and for shared Markdown source-of-truth, citation mechanics, media
provenance, privacy, validation, mdBook-derived-output, and promotion behavior
unless `specs/responsible-breadth.md` gives a stricter rule.

Responsible Breadth supersedes Markdown-first R21/R22 content-scope exclusions
only for accepted expanded page classes. The prohibition on diagnosis,
personalized treatment, personalized programming, rehabilitation protocols,
acute injury guidance, post-surgical guidance, specialized-population guidance,
AI-generated source-of-truth content, and clinical-authority claims remains
active.

Validation remains repository-local and Markdown-first:

- structural checks classify page paths and required sections;
- citation checks verify page-local sources and source-index references;
- source count checks are automated where possible;
- source quality, non-diagnostic language, non-prescription boundaries, visual
  necessity, and reader comprehension use recorded review evidence when
  semantics cannot be fully automated;
- media provenance continues to use the existing `media/PROVENANCE.md` contract.

Responsible Breadth review evidence lives under the relevant
`docs/changes/<change-id>/` record for the reviewed change.

Expanded pages must not be linked as promoted content from active navigation
until architecture review, test-spec review, planning, implementation review,
and final verification for the slice are complete.

## Alternatives considered

- Supersede the entire Markdown-first spec: rejected because it would create
  unnecessary churn and risk breaking the original five-page v0.1 contract.
- Use front matter for page classification immediately: deferred because
  path-based classification is simpler and sufficient for the first expanded
  slice. A later spec may add front matter if page classes share directories.
- Build a symptom-checker or decision-tree router: rejected because that would
  move the project from static education into decision support.
- Store expanded content in a CMS or database: rejected because Markdown remains
  the source of truth and there is no runtime product boundary.
- Require a formal clinician review board: rejected for this slice because the
  accepted trust model is citation discipline, red-flag routing, honest
  authorship, and reviewable evidence records.

## Consequences

Benefits:

- Downstream tools can classify expanded pages deterministically from paths.
- The original Markdown-first v0.1 slice remains stable and closeable.
- Expanded pages inherit shared Markdown, citation, media, privacy, and mdBook
  rules without duplicating the whole architecture.
- Safety routing and source-quality expectations are visible in Markdown and
  review evidence.
- Semantic safety boundaries are recorded explicitly instead of hidden in chat.

Costs and risks:

- Review evidence remains necessary for source quality, non-diagnostic
  language, non-prescription boundaries, and comprehension outcomes when
  automated checks cannot verify semantics.
- Top-level directories may create navigation sprawl if promotion gates are not
  enforced.
- Red-flag and review-cadence requirements introduce ongoing maintenance debt.
- Path-based classification may need to evolve if future content classes become
  less cleanly separated.

Compatibility and migration:

- Existing numbered v0.1 directories remain valid for the original
  Markdown-first slice.
- Existing `media/PROVENANCE.md` semantics continue to apply to expanded pages.
- Expanded paths become compatibility surfaces only after pages are promoted
  through the reviewed workflow.
- Removing or narrowing a promoted expanded page is a content rollback: remove
  active navigation, mark the page draft or withdrawn, and keep correction
  history in the review record.

## Follow-up

- Review this ADR with the updated architecture package.
- Create the Responsible Breadth test specification after architecture review.
- Create the first expanded-scope execution plan after test-spec review.
