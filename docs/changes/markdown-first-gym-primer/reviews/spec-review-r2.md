# Spec Review R2: Markdown-First Gym Primer Media Amendment

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-MEDIA-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/spec-review-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: SR-MEDIA-1
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: media provenance contract is underspecified

## Review inputs

- Spec reviewed: `specs/markdown-first-primer.md`
- Review scope: draft amendment allowing human-reviewed AI-generated raster
  illustrations with provenance.
- Related workflow state: `docs/workflows.md`,
  `docs/changes/markdown-first-gym-primer/change.yaml`, and `docs/plan.md`.
- Governing sources: `CONSTITUTION.md`, `AGENTS.md`,
  `docs/proposals/2026-06-27-markdown-first-gym-primer.md`, and
  `docs/changes/markdown-first-gym-primer/reviews/proposal-review-r2.md`.

## Findings

## Finding SR-MEDIA-1

- Finding ID: SR-MEDIA-1
- Severity: major
- Location: `specs/markdown-first-primer.md`, R41-R42, Inputs and outputs,
  Observability, AC8, AC14
- Evidence: The amended spec requires every AI-generated raster illustration to
  have a media provenance record and lists high-level record contents, but it
  does not define where the record lives, whether provenance is centralized or
  sidecar-per-asset, what stable field names are required, or how an image
  reference deterministically maps to its provenance record. That leaves
  contributor guidance, validators, and review records guessing how to prove
  R41-R42 and AC14.
- Required outcome: The spec must define an observable provenance record shape
  and location convention precise enough for tests and implementation.
- Safe resolution path: Add a narrow media provenance contract. For example,
  require one repository-tracked `media/PROVENANCE.md` table or one sidecar file
  per image, and define stable fields such as `asset_path`, `generator`,
  `prompt_or_creation_notes`, `created_date`, `human_reviewer`,
  `license_assertion`, `source_inputs`, `review_status`, and `page_refs`.
  State that a promoted page referencing an AI-generated image fails validation
  when the matching provenance record is missing or incomplete.
- needs-decision rationale: none

## Review dimensions

- Requirement clarity: block. The provenance concept is required but lacks a
  concrete record location and field contract.
- Normative language: concern. The new MUST clauses are mostly testable, but
  R42's record contents are not tied to stable field names.
- Completeness: concern. Safety, licensing, and visual-support boundaries are
  present; provenance storage and mapping are missing.
- Testability: block. Tests cannot deterministically find or validate
  provenance records from the spec alone.
- Examples: pass. E6 covers the happy path for adding an AI-generated
  illustration.
- Compatibility: concern. The spec permits `media/` assets but does not define
  whether future paths or sidecars become compatibility surfaces.
- Observability: block. Observability does not state how validation reports
  identify missing or incomplete media provenance.
- Security/privacy: pass. The spec excludes private people, identifying marks,
  unsafe setup, medical treatment, and undocumented inputs.
- Non-goals: pass. The amendment preserves the no external photos,
  screenshots, stock-assets boundary.
- Acceptance criteria: concern. AC8 and AC14 require provenance but do not
  identify the concrete artifact shape to inspect.

## Exact wording suggestion

One acceptable resolution would be to add a requirement like:

```text
R46. AI-generated raster illustration provenance MUST be recorded in
`media/PROVENANCE.md` using one row per asset with these fields:
`asset_path`, `generator`, `prompt_or_creation_notes`, `created_date`,
`human_reviewer`, `license_assertion`, `source_inputs`, `review_status`,
and `page_refs`.
```

And a boundary rule like:

```text
A promoted Markdown page MUST fail media validation when it references an
AI-generated raster illustration whose `asset_path` is absent from
`media/PROVENANCE.md`, whose required fields are blank, or whose
`review_status` is not approved.
```

The exact file format can differ, but the spec needs an equally deterministic
location and required field contract.

## No-finding notes

- The amendment correctly keeps AI-generated media as supporting visual aids,
  not instructional source of truth.
- The amendment correctly keeps third-party screenshots, stock assets, borrowed
  web images, and commercial machine screenshots out of v0.1.
- The amendment correctly requires human review and rejects unsafe,
  out-of-scope, identifying, or misleading branded imagery.

## Immediate next stage

spec revision

## Eventual test-spec readiness

not-ready until SR-MEDIA-1 is resolved.
