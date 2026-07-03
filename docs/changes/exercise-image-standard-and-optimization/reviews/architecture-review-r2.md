# Architecture Review R2: Generated Raster Prompt Records

## Result

- Review surface: canonical-architecture-update and ADR
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: not-required
- Open blockers: none for architecture-review; `CR-EIS-M3-2` remains open for M3 code-review resolution
- Required canonical updates: normalize `docs/architecture/system/architecture.md` status from `draft` to `approved` before downstream planning, test-spec, or implementation relies on the prompt-record amendment
- Required ADR updates: none
- Next stage: architecture status normalization, then plan and test-spec amendments for prompt-record validation and backfill

## Findings

None.

## Review Dimensions

| Dimension | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | `specs/exercise-image-standard.md` R20-R20H require a non-blank `prompt_record`, repository-local prompt-record path semantics, exact full prompt text, reverse `asset_path` matching, and no reader-facing prompt embedding. The architecture records the same validation flow, path shape, and Markdown-source-of-truth boundary. |
| Package shape | pass | The review surface is correctly split between the canonical architecture package, the C4 container diagram, and `docs/adr/2026-07-03-generated-raster-prompt-records.md`. No competing change-local architecture document was introduced. |
| Boundary clarity | pass | The Building Block View and container diagram separate media assets, centralized provenance, prompt records, content, governance, and tooling. Prompt records are audit media artifacts, not exercise-page content. |
| Data ownership | pass | `media/PROVENANCE.md` remains the central provenance index. Prompt records own exact full prompt text and must point back to the same normalized `asset_path`. |
| Interface safety | pass | The architecture treats `prompt_record`, normalized `asset_path`, prompt-record path shape, and reverse matching as validation-facing compatibility surfaces. Existing legacy exercise images are not forced into migration. |
| Runtime and failure handling | pass | The Runtime View now blocks promotion for missing or invalid `prompt_record`, missing prompt-record file, prompt-record path violations, prompt-record `asset_path` mismatch, and missing exact prompt text or explicit redaction evidence. |
| Deployment and execution boundaries | pass | The update keeps prompt records as repository-local source assets and does not introduce hosting, CMS, database, generated public JSON, user input, or runtime media services. |
| Security/privacy | pass | The architecture and ADR call out privacy and unsafe-prompt redaction discipline while preserving no-secrets, no-private-data, and no-private-health-information rules. |
| Quality and operations | pass | Quality scenarios and observability now cover prompt traceability and stable prompt-record findings. The risks section records added reviewer/checker overhead and prompt exposure risk. |
| Testing feasibility | pass | The architecture exposes deterministic checks for non-blank `prompt_record`, repository-local path shape, existing prompt-record file, reverse `asset_path` match, exact prompt text presence, and explicit redaction notes. |
| Complexity discipline | pass | The design keeps centralized provenance for compact index data and adds linked Markdown prompt records only for long exact prompts, avoiding broad sidecar provenance metadata. |
| ADR quality | pass | The new ADR includes status, context, decision, alternatives, consequences, compatibility/migration, and follow-up. It records the durable prompt-record decision without duplicating all canonical package structure. |
| Plan readiness | pass | No architecture design blocker remains. Downstream work still must update plan and test-spec artifacts before checker, provenance, prompt-record backfill, or exercise-page implementation resumes. |

## C4, Arc42, ADR, And Legacy Status

- Canonical source: pass. Current design truth is in `docs/architecture/system/architecture.md`.
- arc42 shape: pass. The amendment updates lifecycle metadata, Related artifacts, Architecture Constraints, Solution Strategy, Building Block View, Runtime View, Deployment View, Crosscutting Concepts, Architecture Decisions, Quality Requirements, Risks and Technical Debt, Glossary, Next artifacts, Follow-on artifacts, and Readiness.
- C4 sufficiency: pass. The existing system context diagram remains sufficient. The container diagram was appropriately updated to add the prompt-record container and its relationships to provenance, media, and validation tooling.
- ADR coverage: pass. `docs/adr/2026-07-03-generated-raster-prompt-records.md` records the durable decision and explicitly amends the prior AI-raster provenance and exercise-document image-purpose ADR trail.
- Legacy status: pass. Existing generated raster exercise images are not automatically migrated; downstream artifacts must decide whether to backfill, replace, or leave older images under the pre-amendment compatibility path.

## Exact Suggested Changes

No design changes are required.

Before downstream artifacts rely on this amendment, normalize `docs/architecture/system/architecture.md` from `draft` to `approved` and update workflow metadata to point at this R2 review.

## Command Checks Performed During Review

| Command | Result | Evidence |
|---|---|---|
| `python3 tools/checks/check_privacy.py -- docs/changes/exercise-image-standard-and-optimization/reviews/architecture-review-r2.md docs/changes/exercise-image-standard-and-optimization/review-log.md docs/changes/exercise-image-standard-and-optimization/change.yaml` | pass | checked 3 review/metadata files |
| `git diff --check` | pass | no whitespace errors |

## Readiness

The generated-raster prompt-record architecture amendment is approved for owner normalization to `approved`. This isolated review does not automatically start planning, test-spec amendment, implementation, or M3 code-review re-review.
