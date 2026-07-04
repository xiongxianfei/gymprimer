# ADR 2026-07-03: Generated Raster Prompt Records

## Status

accepted

## Context

The approved Exercise Image Standard prompt-record amendment requires exact
full prompts to be preserved for generated raster exercise images. Earlier
media architecture kept `media/PROVENANCE.md` as the centralized provenance
index and rejected sidecar-per-image metadata for the first slice because the
media library was small.

That centralized provenance table remains the right index for asset identity,
purpose, approval, license assertion, page references, and reviewer
accountability. However, exact full prompts can be long, multiline, and
iteration-specific. Storing them directly inside the provenance table would make
the table hard to review and fragile to edit.

The architecture needs a deterministic link from each governed generated raster
exercise image provenance row to the exact prompt record, while preserving the
existing extension-based raster classification and exact `asset_path`
provenance matching.

## Decision

Keep `media/PROVENANCE.md` as the centralized provenance index for generated
raster media.

For generated raster exercise images governed by the prompt-record amendment,
add `prompt_record` as a required non-blank provenance field. The value is a
repository-local Markdown path to the prompt record.

Prompt records live under:

```text
media/prompts/exercises/<exercise-slug>/<asset-stem>.md
```

Each prompt record preserves the exact full prompt text for the accepted image
and identifies the generated asset path. Validation resolves `prompt_record`,
confirms the path is repository-local and has the required prompt-record path
shape, reads the prompt record, and checks that the prompt record points back to
the same normalized `asset_path` as the provenance row.

The `prompt_or_creation_notes` field remains a short provenance summary. It is
not a substitute for the exact prompt record.

Prompt records are governance/audit media artifacts, not reader-facing exercise
content. Exercise Markdown pages must not embed raw prompt records.

## Alternatives considered

- Store exact prompts in `prompt_or_creation_notes`: rejected because full
  prompts are long and multiline, making the central table hard to read and
  error-prone.
- Derive the prompt-record path only from `asset_path`: rejected because an
  explicit `prompt_record` field is easier to validate, review, and migrate
  when a later architecture changes prompt-record placement.
- Keep only chat history or generated-image tool output paths: rejected because
  those are not durable repository artifacts.
- Add a broad sidecar metadata file per image containing all provenance:
  rejected because `media/PROVENANCE.md` remains the central index for asset
  identity, purpose, approval, licensing, and page references.
- Do not preserve exact prompts: rejected because prompt auditability is now an
  approved part of the exercise-image standard.

## Consequences

Benefits:

- Exact prompts become durable, reviewable repository artifacts.
- `media/PROVENANCE.md` remains compact enough to scan while still linking to
  full prompt evidence.
- Validators can deterministically check prompt-record presence, location,
  repository-local path safety, and reverse `asset_path` matching.
- Prompt records can document rejected variants, selected-output notes, and
  explicit redaction reasons when needed.

Costs and risks:

- Generated raster exercise images now require both a provenance row and a
  prompt record.
- Reviewers must inspect another artifact class for generated images.
- Prompt records can expose unsafe or private prompt material unless redaction
  discipline and privacy checks are applied.
- Existing generated raster images may lack exact prompts; migration planning
  must decide whether to backfill, replace, or leave them under the
  pre-amendment compatibility path.

Compatibility and migration:

- Existing centralized provenance matching by `asset_path` remains unchanged.
- Existing generated raster exercise images using legacy compatible purposes are
  not automatically migrated by this ADR.
- New generated raster exercise images governed by the prompt-record amendment
  require `prompt_record`.
- If exact prompt text is unavailable for an older image, downstream artifacts
  must record that limitation or replace the image with a newly generated asset
  that has a prompt record.

## Follow-up

- Update the test spec to cover `prompt_record` field validation,
  repository-local path shape, missing prompt records, reverse `asset_path`
  mismatch, exact prompt text presence, and redaction notes.
- Update the execution plan for prompt-record backfill and checker support.
- Update validation tooling only after architecture review, test-spec review,
  and plan review approve the implementation slice.
