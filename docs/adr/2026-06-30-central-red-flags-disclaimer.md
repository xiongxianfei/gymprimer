# ADR 2026-06-30: Central Red-Flags Disclaimer Boundary

## Status

accepted

Supersedes the per-page disclaimer portion of
`docs/adr/2026-06-27-markdown-first-citation-based-authority.md`.

Complements `docs/adr/2026-06-29-direct-repository-layout-normalization.md`,
which moved the red-flags reference to root `RED-FLAGS.md`.

## Context

GymPrimer originally used page-local disclaimer scaffolding in the
Markdown-first v0.1 slice. Responsible Breadth later made per-card legal
disclaimer scaffolding a non-goal and established red-flag routing as the
project's safety boundary for pattern, condition, principle, program-example,
and expanded exercise pages.

The forward-head-posture review loop exposed the conflict: one code-review
finding treated a missing exercise-page disclaimer as a validation gap, while
the owner clarified that the prominent disclaimer should live in
`RED-FLAGS.md` and should not be repeated everywhere.

This is an architecture decision because it assigns ownership for disclaimer
text, authoring templates, and validation behavior across multiple page classes
and checker surfaces.

## Decision

`RED-FLAGS.md` owns the central GymPrimer disclaimer. The disclaimer must remain
near the top of that file and state that GymPrimer is educational content, not
medical advice, and not personalized coaching.

Content pages do not need to repeat the full disclaimer. Templates should route
authors to link `RED-FLAGS.md` when a page mentions pain, symptoms,
professional care, self-management themes, or other safety-relevant context.

Validation should check the central disclaimer on `RED-FLAGS.md`. Page-level
validation should check required page sections, page-local sources, claim-level
safety citations, red-flag routing links where applicable, forbidden scope
language, media/provenance rules, and privacy. It should not fail a page solely
because the full disclaimer block is absent from that page.

Existing pages may retain page-local disclaimers as harmless legacy wording, but
new templates should not scaffold repeated disclaimer blocks.

## Alternatives considered

1. Require the disclaimer on every safety-relevant page.

   Rejected. It creates repeated boilerplate, makes drift likely, and conflicts
   with the accepted Responsible Breadth non-goal against per-card legal
   disclaimer scaffolding.

2. Remove the explicit disclaimer requirement entirely.

   Rejected. The repository still needs a visible project-level boundary for
   educational content, medical advice, and personalized coaching.

3. Put disclaimer text in every template but make checker enforcement optional.

   Rejected. That keeps the duplicated authoring pattern while making the
   validation behavior ambiguous.

## Consequences

Benefits:

- One canonical disclaimer is easier to maintain and review.
- Authoring templates stay focused on page-specific education, sources, and
  safety routing.
- Validation becomes more precise: `RED-FLAGS.md` owns disclaimer wording, and
  pages own content-specific boundaries.
- Existing page-local disclaimers do not need churn-only removal.

Costs and risks:

- Readers who enter directly on a content page may not see the disclaimer unless
  the page links `RED-FLAGS.md` where safety context is relevant.
- Template and checker tests must prevent stale `about/red-flags.md` links and
  repeated disclaimer scaffolding from returning.
- Content review must still ensure safety-relevant pages link red flags before
  self-management or exercise-option discussion.

Compatibility and migration:

- `RED-FLAGS.md` remains the stable root safety-routing path.
- Existing content with page-local disclaimers remains valid.
- New content should not require page-local disclaimer blocks for promotion.
- The older `about/red-flags.md` path remains removed after layout
  normalization.

## Follow-up

- Architecture-review this ADR with the central-disclaimer architecture update.
- Re-review or settle the forward-head test spec after architecture-review.
- Re-review M1 validation after the source-of-truth and proof-map status are
  settled.
