# Repository Layout Normalization Change Rationale

## M1 dependency inventory

M1 records the migration dependency surface before any file move. This follows `R15` and `R16`: active references must be identified and updated or removed before the referenced old path disappears.

The evidence lives at `docs/changes/repository-layout-normalization/evidence/dependency-inventory.md`. It identifies:

- old numbered Markdown content paths and their canonical targets;
- `the former nested red-flags path.md` references and the root `RED-FLAGS.md` target;
- media bucket assets that need subject-co-located destinations and provenance updates;
- historical structured-platform folders that require M4 disposition.

No content, media, generated output, schema, or tooling path is moved in M1. That is intentional: M2 adds validation coverage first, M3 moves Markdown content and project references, and M4 handles media plus historical artifacts.

## M2 validation tooling and regression tests

M2 adds the enforcement layer needed before the physical migration starts. It updates `tools/checks/check_markdown_first.py` so the checker can reject stale active references after the normalized root `RED-FLAGS.md` exists.

The new tests live in `tests/test_repository_layout_normalization.py`. They prove the post-migration target accepts canonical content paths, root red-flags references, subject-co-located raster media, and explicit historical/archive labels. They also prove failures for old numbered content paths, `the former nested red-flags path.md` references, compatibility stubs, old media buckets, stale `media/PROVENANCE.md` asset paths, root-level governance folders, and unclassified historical artifacts.

The checker intentionally gates the strict migration rules on `RED-FLAGS.md` existing at the checked repository root. That keeps M2 from breaking the current pre-migration tree while still making the target behavior testable before M3 moves files.

## M3 content and project-reference migration

M3 moves the Markdown content paths into the canonical content block: beginner principles now lives under `principles/`, the former machine and bodyweight exercise pages now live under `exercises/`, and the red-flags reference now lives at root `RED-FLAGS.md`.

Active README, pattern, condition, test, checker, and provenance page references were updated so the old content and red-flags paths are no longer required. Media asset paths remain in the old media buckets because M4 owns media co-location and historical artifact cleanup.
