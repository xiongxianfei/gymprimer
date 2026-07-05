# Architecture Review R2: Brisk Walking Required Media Amendment

## Result

- Review surface: canonical-architecture-update
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/architecture-review-r2.md`
- Review log: `docs/changes/2026-07-05-brisk-walking-and-everyday-walking/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Required canonical updates: normalize `docs/architecture/system/architecture.md` status from draft amendment to approved before downstream planning, test-spec, or image implementation relies on the required-media amendment
- Required ADR updates: none
- Next stage: architecture status normalization, then plan/test-spec updates for the required brisk-walking media contract

## Findings

None.

## Review Dimensions

| Dimension | Verdict | Evidence |
| --- | --- | --- |
| Spec alignment | pass | `specs/brisk-walking-and-everyday-walking.md` BWG-R24 through BWG-R26 require exactly one brisk-walking movement image, one brisk-walking muscle-attention image, exercise-image-standard compliance, and no everyday-walking image. The architecture records that requirement in Architecture Constraints, Building Block View, Runtime View, Crosscutting Concepts, Observability, and Quality Requirements. |
| Package shape | pass | The review surface is a canonical architecture update. Lifecycle metadata appears before the arc42 sections, the official arc42 sections remain present, and the existing C4 context/container diagram links remain sufficient. |
| Boundary clarity | pass | The Building Block View keeps walking content in Markdown, required walking media under `media/exercises/brisk-walking/`, exact prompts under `media/prompts/exercises/brisk-walking/`, provenance in `media/PROVENANCE.md`, and visual-safety evidence under change-local records. |
| Data ownership | pass | Markdown remains authoritative for walking guidance, technique, muscle names, feel cues, safety, and citations. Generated images remain support assets with prompt records and provenance; no new database, schema, taxonomy store, or hidden metadata owner is introduced. |
| Interface safety | pass | The public compatibility surfaces are repository-local Markdown image references, media-purpose values, prompt-record paths, approved provenance rows, page refs, alt text, and visual-safety evidence. The update preserves text-only validity for unrelated exercise pages. |
| Runtime and failure handling | pass | Runtime View and Observability identify promotion blockers for missing required movement or muscle-attention images, wrong purpose, missing local asset, missing or mismatched prompt record, missing approved provenance, missing page reference, generic alt text, and missing visual-safety evidence. |
| Deployment and execution boundaries | pass | Deployment View keeps walking guidance Markdown-only and adds no runtime, CMS, API, search index, user input, account system, analytics, tracker, wearable integration, calculator, walking program, or adaptive recommendation flow. |
| Security/privacy | pass | The architecture keeps the no-private-health-information boundary and routes generated media through existing prompt-record/provenance privacy controls. The muscle-attention image is constrained away from precise anatomy, labels, diagnosis, treatment, and exact activation claims. |
| Quality and operations | pass | Quality Requirements add a brisk-walking required-media scenario, while existing exercise-image quality scenarios cover provenance, prompt traceability, image purpose, count, visual safety, compatibility, and accessibility-adjacent review. |
| Testing feasibility | pass | The architecture exposes deterministic checks for required image references, image purpose, local asset, prompt-record/provenance/page-ref matching, generic alt text, and privacy, plus manual visual-safety evidence for semantics that cannot be automated. |
| Complexity discipline | pass | The amendment reuses the approved exercise-image purpose and generated-raster prompt-record architecture. It does not add a new diagram level, ADR, runtime component, metadata store, generated package, or validator architecture. |
| ADR quality | pass | No new ADR is required. Existing ADRs for exercise-document image purposes and generated raster prompt records already record the durable media-purpose and prompt-record decisions this amendment relies on. |
| Plan readiness | pass | No architecture question blocks downstream planning. Planning and test-spec updates can now focus on image asset creation, prompt records, provenance rows, visual-safety evidence, checker coverage, and rollback for invalid media. |

## C4, arc42, ADR, And Legacy Status

- C4 context diagram: unchanged and sufficient because no external actor, system, hosted service, or external dependency changes.
- C4 container diagram: unchanged and sufficient because the required walking images stay inside the existing `content`, `media`, `provenance`, `prompt_records`, and `ops` containers.
- Component diagram: not required; the amendment does not introduce internal component boundaries beyond existing checker/manual-proof responsibilities.
- Deployment diagram: not required; deployment remains repository Markdown with optional derived mdBook output.
- ADR: not required; `docs/adr/2026-07-03-exercise-document-image-purposes.md` and `docs/adr/2026-07-03-generated-raster-prompt-records.md` already cover the durable image-purpose and prompt-record decisions.
- Legacy status: pass. Existing exercise pages and legacy compatible image-purpose rows are not migrated by this amendment; only `exercises/brisk-walking.md` gets a required-media exception under the approved walking spec.

## Required Changes

No design changes are required.

Before downstream artifacts rely on this amendment, normalize `docs/architecture/system/architecture.md` from draft amendment wording to approved and update workflow metadata to point at this R2 review as the current approved architecture review.

## Command Checks Performed During Review

| Command | Result | Evidence |
| --- | --- | --- |
| `rg -n "^## " docs/architecture/system/architecture.md` | pass | Confirmed lifecycle metadata plus arc42 sections remain present. |
| `rg -n "BWG-R24|BWG-R25|BWG-R25A|BWG-R25B|BWG-R26|BWG-R29|E5|EC7A|EC7B" specs/brisk-walking-and-everyday-walking.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/reviews/spec-review-r3.md` | pass | Confirmed amended-media requirement and review tokens are present. |
| `python3 tools/checks/check_privacy.py docs/architecture/system/architecture.md docs/changes/2026-07-05-brisk-walking-and-everyday-walking/change.yaml docs/plans/2026-07-05-brisk-walking-and-everyday-walking.md docs/plan.md` | pass | Prior architecture authoring validation checked 4 files. |
| `git diff --check` | pass | Prior architecture authoring validation reported no whitespace errors. |

## Readiness

The required brisk-walking media architecture amendment is approved for status normalization. This direct architecture-review request remains isolated and does not automatically start plan, test-spec, implementation, or image generation.
