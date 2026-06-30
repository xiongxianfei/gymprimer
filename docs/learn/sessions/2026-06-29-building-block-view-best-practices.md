# Learn Session: Building Block View Best Practices

## Frame

- Trigger: explicit `$learn` invocation asking for best practices for creating the building block view for this project.
- Trigger type: explicit maintainer request.
- Scope: architectural building-block views for GymPrimer repository structure and content/media/governance separation.
- Evidence in scope:
  - `docs/architecture/system/architecture.md`
  - `specs/repository-layout-normalization.md`
  - `docs/changes/repository-layout-normalization/reviews/spec-review-r1.md`
  - `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`
  - `docs/learn/topics/content-quality.md`
- Explicit exclusions:
  - No physical file moves.
  - No new architecture, spec, workflow, or policy rule.
  - No claim that the repository-layout-normalization spec is approved.
  - No CI, verification, branch-readiness, or PR-readiness claim.
- Prior learnings reviewed:
  - `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`
  - `docs/learn/topics/content-quality.md`
- Session record path: `docs/learn/sessions/2026-06-29-building-block-view-best-practices.md`

## Observe

- OBS-001: The approved architecture uses five logical blocks: project references, content, media, governance, and tooling/operations. It deliberately separates product content from governance and operational proof.
- OBS-002: The building-block view keeps current physical paths and target normalized paths separate. Current v0.1 compatibility paths remain visible, while the target names one canonical location per content type.
- OBS-003: The target content model uses durable content-type folders: `exercises/`, `patterns/`, `conditions/`, `principles/`, and `programs/`.
- OBS-004: Governance stays under `docs/proposals/`, `docs/adr/`, and `docs/architecture/` because `docs/workflows.md` standardizes RigorLoop artifact locations there. Root-level governance directories were considered but rejected for this repository.
- OBS-005: Media is a separate block because images support content but have their own provenance, path, and validation rules. The target shape is subject co-location under `media/<content-type>/<slug>/`.
- OBS-006: The repository-layout spec review found that a good architecture target is not enough for migration. Testable migration behavior still needs deterministic old-path, red-flags-path, and media-path rules before implementation.
- OBS-007: Prior content-quality learning says architecture and page contracts are floors, not final quality. The same applies to building-block views: the view should be simple enough to orient contributors and precise enough to drive downstream specs.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-007 | durable-lesson | durable-lesson | topic entry in `docs/learn/topics/architecture.md` | Explicit maintainer `$learn` request asking for best practices; approved architecture and spec-review findings provide evidence | The five-block architecture and the repository-layout review show a reusable pattern for future building-block views: separate product content, support media, governance, and operations; name current and target paths separately; avoid proposal codenames; and make migration implications explicit. |

## Route

- Added topic entry: `docs/learn/topics/architecture.md`.
- No architecture, spec, ADR, workflow, or policy artifact was changed by this learn session.
- Follow-up remains owned by the active repository-layout-normalization spec revision, which must resolve SR-RLN-1, SR-RLN-2, and SR-RLN-3 before downstream work.

## Best Practices For GymPrimer Building Block Views

1. Use five durable blocks: project references, content, media, governance, and tooling/operations.
2. Keep product content separate from workflow evidence. Content is what readers consume; specs, reviews, plans, proof, and validation tools serve the content.
3. Use one canonical location per content type. Exercises belong in `exercises/`; patterns in `patterns/`; conditions in `conditions/`; principles in `principles/`; program examples in `programs/`.
4. Treat equipment, difficulty, movement pattern, and modality as metadata or page content, not top-level folder identity.
5. Show current paths separately from target paths. A building-block view should tell contributors what exists now and what migration target is intended.
6. Keep governance under `docs/` for this repository: `docs/proposals/`, `docs/adr/`, and `docs/architecture/`.
7. Keep operations separate: `tools/`, `specs/`, `docs/changes/`, `docs/plans/`, and `docs/learn/` are support systems, not user-facing content blocks.
8. Organize media by subject when normalized: `media/<content-type>/<slug>/`, with provenance in `media/PROVENANCE.md`.
9. Avoid project-stage codenames in durable architecture. Use stable names such as pattern pages, condition pages, and program examples instead of proposal names.
10. Do not hide migration debt. If current folders remain for compatibility, say why, name the target shape, and require a migration spec before moving paths.
11. Make compatibility surfaces explicit: Markdown paths, media paths, navigation links, provenance rows, and workflow artifact paths are all contracts once referenced.
12. Keep the view small enough to be useful. A good building-block view should orient a contributor in a few rows, then push detailed migration behavior into specs.

## What To Improve Next

- Revise `specs/repository-layout-normalization.md` to choose deterministic old-path, red-flags-path, and media-path behavior.
- After that spec is approved, update architecture or ADRs only if the migration decision changes the approved target shape.
- Add test-spec coverage that maps building-block decisions to link validation, provenance validation, canonical-path checks, and compatibility-stub checks.

## Validation

- Session and topic entry created by direct inspection of the named evidence.
- No code, content page, spec, architecture, or policy artifact changed.
