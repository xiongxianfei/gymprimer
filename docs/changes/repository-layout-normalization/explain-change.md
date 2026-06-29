# Repository Layout Normalization Change Rationale

## M1 dependency inventory

M1 records the migration dependency surface before any file move. This follows `R15` and `R16`: active references must be identified and updated or removed before the referenced old path disappears.

The evidence lives at `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`. It identifies:

- old numbered Markdown content paths and their canonical targets;
- `about/red-flags.md` references and the root `RED-FLAGS.md` target;
- media bucket assets that need subject-co-located destinations and provenance updates;
- historical structured-platform folders that require M4 disposition.

No content, media, generated output, schema, or tooling path is moved in M1. That is intentional: M2 adds validation coverage first, M3 moves Markdown content and project references, and M4 handles media plus historical artifacts.
