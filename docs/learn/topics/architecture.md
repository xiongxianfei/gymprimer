# Architecture Lessons

## 2026-06-29: Building-block views should separate content, media, governance, and operations

- Source session: `docs/learn/sessions/2026-06-29-building-block-view-best-practices.md`
- Primary classification: durable-lesson
- Secondary routes: repository-layout-normalization spec revision for deterministic migration behavior

For GymPrimer, a useful building-block view has five durable blocks:

- Project references: root entry, contribution, source-index, safety, and license files.
- Content: `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`.
- Media: `media/`, subject-co-located assets, and `media/PROVENANCE.md`.
- Governance: `docs/proposals/`, `docs/adr/`, and `docs/architecture/`.
- Tooling and operations: validation tools, specs, change records, plans, learning records, and optional derived-site config.

Best practice is one canonical location per content type. Equipment type, difficulty, movement pattern, and modality should be metadata or page content, not top-level folder identity. Governance stays under `docs/` in this repository because the workflow guide standardizes those paths.

The building-block view should separate current compatibility paths from the target normalized shape. If old paths, media buckets, or historical folders remain, the view should name them as compatibility debt and require a migration spec before implementation.

This is curated guidance, not a migration authorization. Physical path moves still require approved spec, architecture or ADR review, test-spec, plan, and implementation review.
