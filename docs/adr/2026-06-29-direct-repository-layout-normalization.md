# ADR-20260629-direct-repository-layout-normalization: Direct Repository Layout Normalization

## Status

accepted

Amended on 2026-06-30 by the forward-head-posture pattern architecture work to
replace separate audit-artifact requirements with recorded review evidence
under the normal change record.

## Context

GymPrimer's approved architecture target is five logical blocks: project
references, content, media, governance, and tooling/operations. The current
physical tree still carries compatibility debt from earlier slices:
`01-getting-started/`, `02-machines/`, `03-bodyweight/`,
`about/red-flags.md`, image-type media buckets, and historical
structured-platform artifacts.

`specs/repository-layout-normalization.md` now requires a deterministic
migration: old paths are removed directly, `RED-FLAGS.md` becomes the root
red-flags reference, promoted media moves to `media/<content-type>/<slug>/`,
and active dependencies are inventoried and updated before removal.

This is a durable architecture decision because it changes repository path
compatibility, contributor navigation, validation scope, and media layout.

## Decision

Normalize the repository layout by direct migration rather than compatibility
stubs.

- Fold `02-machines/` and `03-bodyweight/` exercise pages into `exercises/`.
- Fold `01-getting-started/beginner-training-principles.md` into
  `principles/beginner-training-principles.md`.
- Move `about/red-flags.md` to root `RED-FLAGS.md`.
- Move promoted media to subject-co-located paths under
  `media/<content-type>/<slug>/`.
- Remove old numbered content paths, old media-bucket paths, and
  `about/red-flags.md` directly after active dependencies are updated.
- Do not leave compatibility stubs.
- Remove historical structured-platform artifacts directly when no active
  approved spec, test, workflow guide, or validation command relies on them.
  If an active dependency still requires retention, label the artifact
  historical or archive it.

Before a file is removed, the migration must identify active dependencies in
Markdown links, README navigation, `SUMMARY.md`, `book.toml`, source
references, tests, checkers, review evidence, change metadata, and provenance
rows, then update or remove those dependencies first.

## Alternatives considered

1. Keep old paths with compatibility stubs for one review window.

   Rejected. Stubs reduce immediate path breakage but preserve duplicate
   surface area and make validation more complex. The project is still early,
   and the owner chose direct removal.

2. Keep `about/red-flags.md` canonical.

   Rejected. A root `RED-FLAGS.md` is more visible as a project-level safety
   reference and matches the simplified building-block view.

3. Defer media co-location.

   Rejected. Deferral would keep the current image-type buckets and preserve
   the broken-link risk that the layout normalization is meant to remove.

4. Remove historical artifacts without dependency inventory.

   Rejected. That could remove fixtures, validation evidence, or traceability
   still referenced by active specs, tests, or workflow records.

## Consequences

Benefits:

- One canonical location per content type.
- Root-level red flags become easier to discover.
- Media paths become predictable from the content they support.
- Dependency-first migration reduces broken references during direct removal.
- Historical structured-platform artifacts stop looking like active product
  architecture once removed, archived, or labeled.

Costs and risks:

- External links to old repository paths may break because compatibility stubs
  are intentionally not used.
- The migration diff will be larger because links, tests, checkers, review
  records, media paths, and provenance rows must change together.
- A missed dependency can break validation or contributor navigation.
- Moving red flags to root requires every safety-relevant page and checker to
  update references consistently.

## Follow-up

- Architecture review for this ADR and the canonical architecture package.
- Test-spec mapping for dependency inventory, canonical paths, direct removal,
  red-flags path, media co-location, provenance updates, and historical artifact
  disposition.
- Migration plan before implementation.
