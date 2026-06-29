# Workflow Guide

## Purpose

This guide records GymPrimer's project-local artifact locations and workflow routing rules. It complements `CONSTITUTION.md` and `AGENTS.md`; it does not replace the stage skills that author proposals, specs, architecture, plans, tests, implementation, reviews, verification, or PR handoff.

## Source of truth

When workflow artifacts conflict, use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved or accepted lifecycle artifacts
4. This workflow guide for artifact placement and routing
5. Stage-skill portable defaults when this guide is silent
6. Chat context

## Standard workflow

GymPrimer uses the standard spec-driven and test-driven sequence:

```text
proposal -> proposal-review -> spec -> spec-review -> architecture -> architecture-review -> plan -> plan-review -> test-spec -> test-spec-review -> implement -> code-review -> review-resolution when triggered -> ci-maintenance when triggered -> explain-change -> verify -> pr
```

Manual skill invocations are allowed, but they are isolated by default unless the user explicitly asks to continue through the full workflow or a tracked workflow-managed context requires continuation.

Implementation is not allowed until proposal, spec, spec review, architecture assessment, planning, test specification, and required reviews have been completed for the relevant scope.

## Artifact location map

| Artifact type | Location |
| --- | --- |
| Agent quick rules | `AGENTS.md` |
| Constitution | `CONSTITUTION.md` |
| Vision | `VISION.md` |
| Project map | `docs/project-map.md` |
| Workflow guide | `docs/workflows.md` |
| Proposals | `docs/proposals/YYYY-MM-DD-slug.md` |
| Specs | `specs/slug.md` |
| Test specs | `specs/slug.test.md` |
| Canonical system architecture | `docs/architecture/system/architecture.md` |
| Architecture diagrams | `docs/architecture/system/diagrams/` |
| ADRs | `docs/adr/YYYY-MM-DD-slug.md` |
| Detailed plan body | `docs/plans/YYYY-MM-DD-slug.md` |
| Plan index | `docs/plan.md` |
| Change root | `docs/changes/<change-id>/` |
| Change metadata | `docs/changes/<change-id>/change.yaml` |
| Formal review records | `docs/changes/<change-id>/reviews/<stage>-r<n>.md` |
| Review log | `docs/changes/<change-id>/review-log.md` |
| Review resolution | `docs/changes/<change-id>/review-resolution.md` |
| Explain-change | `docs/changes/<change-id>/explain-change.md` |
| Verify report | `docs/changes/<change-id>/verify-report.md` |
| Learn sessions | `docs/learn/sessions/YYYY-MM-DD-slug.md` |
| Follow-ups without a better owner | `docs/follow-ups.md` |

If this guide is silent for an artifact type and a stage skill has a safe portable default, use that default. If neither this guide nor the owning skill gives a safe path, stop and ask for an explicit path.

## Current change

- Change ID: `markdown-first-gym-primer`
- Proposal: `docs/proposals/2026-06-27-markdown-first-gym-primer.md`
- Proposal status: `accepted`
- Proposal review: `docs/changes/markdown-first-gym-primer/reviews/proposal-review-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Current vision: `VISION.md`
- Current constitution: `CONSTITUTION.md`
- Current spec: `specs/markdown-first-primer.md`
- Current spec status: `approved`
- Current spec review: `docs/changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
- Current architecture: `docs/architecture/system/architecture.md`
- Current architecture status: `approved`
- Current ADR: `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`
- Current media ADR: `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
- Current media ADR status: `accepted`
- Current architecture review: `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`
- Current plan: `docs/plans/2026-06-27-markdown-first-gym-primer.md`
- Current plan review: `docs/changes/markdown-first-gym-primer/reviews/plan-review-r3.md`
- Current code review: `docs/changes/markdown-first-gym-primer/reviews/code-review-m4-r1.md`
- Current verification: `docs/changes/markdown-first-gym-primer/verify-report.md`
- Current test spec: `specs/markdown-first-primer.test.md`
- Current test spec status: `active`
- Current test spec review: `docs/changes/markdown-first-gym-primer/reviews/test-spec-review-r4.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Plan index: `docs/plan.md`
- Current readiness: branch-ready for `pr` after local final verification.
  Hosted CI is absent and not claimed.
- Next valid skill: `pr`

## Routing notes

- Do not route this change to implementation until plan-review, test-spec, and test-spec-review are complete.
- Do not route this change to content spike implementation until card-template, citation, disclaimer, media, license, and validation expectations have a reviewed downstream artifact.
- Use `docs/changes/markdown-first-gym-primer/` for formal review records and downstream change-local evidence for this initiative.

## Follow-up routing

- Proposal or product-direction changes go to a proposal artifact.
- Requirement or behavior changes go to the relevant spec.
- Architecture, schema-storage, data-flow, deployment, or boundary decisions go to the architecture package or ADRs.
- Execution tasks go to a plan after architecture review.
- Review findings go to the relevant review record and, when material, `review-resolution.md`.
- Incidents, repeated mistakes, or explicit learning triggers go to `docs/learn/sessions/`.
- Deferred work with no better owner goes to `docs/follow-ups.md`.

Deferred execution work must not be stored in `docs/project-map.md`; the project map is only an orientation artifact.

## Workflow guide change record

- 2026-06-26: Created guide because the repository adopted staged RigorLoop artifacts and no project-local workflow guide existed. Added locations for proposals, specs, architecture, ADRs, plans, change-local reviews, explain-change, verify reports, learn sessions, and follow-ups. No migration is needed because existing artifacts already match these paths.
- 2026-06-27: Updated current-change routing from the superseded structured-platform track to the accepted Markdown-first direction after proposal-review R2, vision revision, and constitution revision.
- 2026-06-27: Routed the Markdown-first change to `spec-review` after drafting `specs/markdown-first-primer.md`.
- 2026-06-27: Routed the Markdown-first change to architecture after clean `spec-review-r1`; spec status still needs normalization to `approved` before downstream reliance.
- 2026-06-27: Normalized the Markdown-first spec to approved, updated the canonical architecture package, added the superseding Markdown-first ADR, and routed to `architecture-review`.
- 2026-06-27: Recorded clean `architecture-review-r1` and routed the Markdown-first change to planning; architecture status still needs normalization to `approved` before downstream reliance.
- 2026-06-27: Normalized the Markdown-first architecture to approved, drafted `docs/plans/2026-06-27-markdown-first-gym-primer.md`, superseded the old content-schema plan in the plan index, and routed to `plan-review`.
- 2026-06-27: Recorded clean `plan-review-r1` for the Markdown-first execution plan and routed to `test-spec`.
- 2026-06-27: Drafted `specs/markdown-first-primer.test.md` and routed to `test-spec-review`.
- 2026-06-27: Recorded `test-spec-review-r1` with changes requested for TSR1 and routed back to `test-spec` revision.
- 2026-06-27: Revised `specs/markdown-first-primer.test.md` with milestone/proof ownership for TSR1 and routed to `test-spec-review` R2.
- 2026-06-27: Recorded clean `test-spec-review-r2`, closed TSR1, and routed to `implement` for M1.
- 2026-06-28: Recorded clean `plan-review-r3`, closed PR-MEDIA-1, and routed
  to `test-spec` for the M3A media proof-map update.
- 2026-06-28: Revised `specs/markdown-first-primer.test.md` with M3A media
  classification/provenance test ownership and routed to `test-spec-review`.
- 2026-06-28: Recorded `test-spec-review-r3` with TSR-M3A-1 and routed back
  to `test-spec` revision.
- 2026-06-28: Addressed TSR-M3A-1 by aligning stale edge-case IDs in the M3A
  proof-map test cases and routed to `test-spec-review` R4.
- 2026-06-28: Recorded clean `test-spec-review-r4`, closed TSR-M3A-1, and
  routed to `implement` for M3A.
- 2026-06-28: Implemented M3A media classification and provenance validation,
  created the empty `media/PROVENANCE.md` contract, added M3A fixtures and
  manual no-raster proof, refreshed local validation, and routed to
  `code-review`.
- 2026-06-28: Recorded clean `code-review-m3a-r1`, closed M3A, and returned
  the workflow to the M3 closeout blocker pending MP3 beginner read-test
  evidence.
- 2026-06-28: Recorded MP3 beginner read-test evidence after a non-identifying
  beginner reader reviewed the first-slice documents, identified readability
  issues, and approved the implementation after example pictures were added;
  routed to `code-review` M3 R2.
- 2026-06-28: Recorded `code-review-m3-r2` with CR-M3-1 and routed to
  `review-resolution` because MP3 lacks required per-page comprehension
  outcomes.
- 2026-06-29: Addressed CR-M3-1 by updating MP3 with non-identifying
  per-page comprehension outcomes and routed to `code-review` M3 R3.
- 2026-06-29: Recorded clean `code-review-m3-r3`, closed CR-M3-1, closed M3,
  and routed to `implement` for M4.
- 2026-06-29: Implemented M4 with mdBook deferral proof, final local quality
  ledger, M4 tests, and validation evidence; routed to `code-review` M4 R1.
- 2026-06-29: Recorded clean `code-review-m4-r1`, closed M4, and routed to
  `explain-change`.
- 2026-06-29: Recorded durable `explain-change` rationale for the final
  reviewed M1-M4 diff and routed to `verify`.
- 2026-06-29: Recorded final local verification in
  `docs/changes/markdown-first-gym-primer/verify-report.md`, marked the change
  branch-ready for PR handoff, and routed to `pr`.
- 2026-06-27: Implemented M1 active route, contributor/license contract, source index, templates, legacy supersession notices, and M1 contract tests; routed to `code-review`.
- 2026-06-27: Recorded clean `code-review-m1-r1`, closed M1, and routed to `implement` for M2.
- 2026-06-27: Implemented M2 Markdown-first checker tooling, fixture tests, and privacy checks; routed to `code-review`.
- 2026-06-27: Recorded `code-review-m2-r1` with CR-M2-1 and routed to `review-resolution`.
- 2026-06-27: Addressed CR-M2-1 by adding `SOURCES.md` source-index validation and regression fixtures; routed to `code-review` M2 R2.
- 2026-06-27: Recorded clean `code-review-m2-r2`, closed M2, and routed to `implement` for M3.
- 2026-06-27: Implemented M3 draft pages, README draft links, real-page
  tests, and MP1/MP2 manual proof records; M3 is blocked pending MP3 beginner
  read-test evidence and must not route to code-review yet.
- 2026-06-27: Drafted a media-policy amendment to allow human-reviewed
  AI-generated raster illustrations with provenance; routed to `spec-review`
  before any media implementation.
- 2026-06-27: Recorded `spec-review-r2` with SR-MEDIA-1 and routed back to
  `spec` revision for a deterministic media provenance contract.
- 2026-06-27: Revised the spec for SR-MEDIA-1 with centralized
  `media/PROVENANCE.md` provenance, exact `asset_path` mapping, required
  fields, media purpose limits, and stable validation failures; routed to
  `spec-review` R3.
- 2026-06-27: Recorded clean `spec-review-r3`, resolved SR-MEDIA-1, and routed
  to architecture for the media provenance boundary update.
- 2026-06-28: Normalized the media provenance spec amendment to approved,
  updated the architecture package and ADR trail for centralized
  `media/PROVENANCE.md`, and routed to `architecture-review` R2.
- 2026-06-28: Recorded `architecture-review-r2` with AR-MEDIA-1 and routed
  back to `architecture` for deterministic raster-media classification.
- 2026-06-28: Addressed AR-MEDIA-1 by defining the v0.1 extension-based media
  classifier in the architecture and media ADR; routed to
  `architecture-review` R3.
- 2026-06-28: Recorded clean `architecture-review-r3`, closed AR-MEDIA-1, and
  routed to architecture status normalization.
- 2026-06-28: Normalized the media provenance architecture package to
  `approved` and the media ADR to `accepted`; routed to `test-spec`.
- 2026-06-28: Revised the active plan for the media provenance amendment by
  adding M3A for deterministic media classification, provenance validation, and
  optional first-slice images; routed to `plan-review` R2.
- 2026-06-28: Recorded `plan-review-r2` with PR-MEDIA-1 and routed back to
  `plan` for milestone sequencing clarification.
- 2026-06-28: Addressed PR-MEDIA-1 by choosing Option A: M3A is next after
  test-spec review, while M3 remains promotion-blocked on MP3 and M3A media
  validation; routed to `plan-review` R3.
