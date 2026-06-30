# Architecture Review R2: Expanded Raster Media Purposes

Date: 2026-06-29
Review surface: canonical-architecture-update with ADR
Reviewer role: architecture reviewer

Reviewed artifacts:

- `docs/architecture/system/architecture.md`
- `docs/architecture/system/diagrams/container.mmd`
- `docs/adr/2026-06-29-expanded-raster-media-purposes.md`
- `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
- `specs/responsible-breadth.md`
- `docs/changes/apt-pattern-architecture/reviews/spec-review-r2.md`
- `docs/workflows.md`

## Result

- Review surface: canonical-architecture-update
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/apt-pattern-architecture/reviews/architecture-review-r2.md`
- Review log: `docs/changes/apt-pattern-architecture/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Required canonical updates: normalize `docs/architecture/system/architecture.md` status to `approved` before downstream reliance
- Required ADR updates: normalize `docs/adr/2026-06-29-expanded-raster-media-purposes.md` status to `accepted` before downstream reliance
- Next stage: architecture and ADR status normalization, then test-spec update

## Findings

None.

## Dimension Review

| Dimension | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | The architecture implements approved Responsible Breadth R29a-R29b and R35a-R35f without changing the original Markdown-first v0.1 media purposes. |
| Package shape | pass | The update is in the canonical architecture package, updates the C4 container diagram, and records the durable enum decision in an ADR. |
| Boundary clarity | pass | The design separates original v0.1 purposes from expanded Responsible Breadth purposes and keeps generated raster images as support assets. |
| Data ownership | pass | `media/PROVENANCE.md` remains the single provenance index; no new data store or schema owner is introduced. |
| Interface safety | pass | Existing `equipment_identification` and `key_movement_illustration` provenance rows remain valid; new purposes apply only to expanded pages. |
| Runtime and failure handling | pass | Media validation flow now states classification, exact provenance matching, allowed-purpose checks, and promotion blockers. |
| Deployment and execution boundaries | pass | No hosted app, CMS, runtime API, account system, analytics, or external service is introduced. |
| Security/privacy | pass | The update preserves no-private-data rules and adds diagnosis/pathology safeguards for condition-region images. |
| Quality and operations | pass | Quality scenarios and risks now cover expanded media-purpose checks, anatomical-region safety, and manual visual review. |
| Testing feasibility | pass | The architecture gives test-spec exact enum values and failure conditions to map into automated validation and manual visual-safety proof. |
| Complexity discipline | pass | The design extends the existing centralized provenance model instead of adding sidecar metadata, new storage, or a media service. |
| ADR quality | pass | The new ADR includes context, decision, alternatives, consequences, compatibility, and follow-up. |
| Plan readiness | pass | No architecture blocker remains; downstream work should wait only for lifecycle normalization and test-spec update. |

## Summary

The expanded media-purpose architecture is safe to rely on after status
normalization. It preserves the original Markdown-first media contract while
adding deterministic purpose values for expanded pattern, condition, and
exercise-preview raster images. The ADR records the durable decision without
requiring physical media-path migration.

No automatic downstream handoff is performed. This direct architecture-review
request remains isolated.
