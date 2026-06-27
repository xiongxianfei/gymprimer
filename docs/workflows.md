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

- Change ID: `beginner-fitness-exercise-education-platform`
- Proposal: `docs/proposals/2026-06-26-beginner-fitness-exercise-education-platform.md`
- Proposal status: `accepted`
- Proposal review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/proposal-review-r1.md`
- Review log: `docs/changes/beginner-fitness-exercise-education-platform/review-log.md`
- Current spec: `specs/content-schema.md`
- Current spec status: `approved`
- Current architecture: `docs/architecture/system/architecture.md`
- Current architecture review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/architecture-review-r1.md`
- Current plan: `docs/plans/2026-06-26-content-schema-foundation.md`
- Current plan review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/plan-review-r2.md`
- Current test spec: `specs/content-schema.test.md`
- Current test spec review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/test-spec-review-r2.md`
- Current code review: `docs/changes/beginner-fitness-exercise-education-platform/reviews/code-review-m1-r1.md`
- Current readiness: ready for `code-review` M2
- Next valid skill: `code-review`

## Routing notes

- Do not route this change to architecture until `specs/content-schema.md` has a clean recorded spec review and is normalized to `approved`.
- Do not route this change to planning until architecture and ADR status are normalized after clean `architecture-review-r1`.
- Do not route this change to implementation until test specification and required test-spec review are complete.
- Use `docs/changes/beginner-fitness-exercise-education-platform/` for formal review records and downstream change-local evidence for this initiative.

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
