# Architecture Review R1: Exercise Method Guidance

## Result

- Review surface: canonical-architecture-update
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-method-guidance/reviews/architecture-review-r1.md`
- Review log: `docs/changes/exercise-method-guidance/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Required canonical updates: normalize `docs/architecture/system/architecture.md` status wording from "drafted for review" to approved by this review before downstream planning relies on the amendment; no re-review required for that status-only cleanup
- Required ADR updates: none
- Next stage: isolated stop; `plan` is the next lifecycle stage only after an explicit workflow or user request

## Findings

None.

## Review Dimensions

| Dimension | Result | Evidence |
| --- | --- | --- |
| Spec alignment | pass | The architecture records visible Markdown `## How much to do` and `Method type:` as source of truth, matching spec R1-R5 and R14-R27. |
| Package shape | pass | The review surface is a canonical architecture update. The package keeps lifecycle metadata, arc42 sections, related artifacts, C4 links, ADR links, quality requirements, risks, and glossary terms. |
| Boundary clarity | pass | The Building Block View places exercise method guidance in exercise Markdown pages and keeps validation/review evidence in tooling and operations rather than a new product runtime. |
| Data ownership | pass | The architecture explicitly rejects hidden metadata, YAML front matter, shared taxonomy files, generated indexes, and generated data packages for the first exercise-method source of truth. |
| Interface safety | pass | The reader-facing contract is visible Markdown, while pattern-page previews remain compact summaries that must not contradict linked exercise pages. |
| Runtime and failure handling | pass | The exercise method authoring flow covers section addition, active method type declaration, principle-page linkage, validation hooks, semantic review evidence, and cross-page preview alignment. |
| Deployment and execution boundaries | pass | Deployment View states exercise method guidance is Markdown-only and introduces no runtime, CMS, API, search index, user-input flow, analytics, hidden metadata package, or generated public data package. |
| Security/privacy | pass | The architecture preserves the no-user-input boundary and records privacy expectations for content, examples, generated evidence, and reader-test notes. |
| Quality and operations | pass | Quality scenarios cover source of truth, enum validity, adaptive-programming boundary, source support, beginner comprehension, and pattern-preview alignment. |
| Testing feasibility | pass | Observability names deterministic validation outputs for missing sections, inactive method types, hidden-only metadata, forbidden personalization/treatment language, and preview contradictions, plus manual source-audit and comprehension evidence. |
| Complexity discipline | pass | The design extends existing Markdown-first and Responsible Breadth boundaries without adding a metadata store, generated package, runtime boundary, deployment, or new diagram level. |
| ADR quality | pass | Section 9 gives a credible no-new-ADR rationale because the change does not introduce a new source-of-truth mechanism, runtime boundary, generated package, taxonomy store, or deployment architecture. |
| Plan readiness | pass | No architecture question blocks planning. The plan can sequence template update, principle page, six proof-slice pages, validation, and manual evidence from the approved spec and architecture. |

## Architecture Assessment

The canonical architecture update is sufficient for this change. It records the durable design choice: exercise method guidance remains page-local visible Markdown, not a hidden metadata system or generated data model. The affected responsibilities are placed in existing blocks: content pages own the guidance, the principle page owns shared explanations, and tooling/review evidence owns validation and semantic proof.

No new C4 component or deployment diagram is required. The existing context and container diagrams remain adequate because the change does not introduce a new external system, container, adapter, runtime process, persistence layer, deployment target, or data flow.

No ADR is required. The architecture's no-ADR rationale is aligned with the approved spec: this is a content-contract and validation amendment inside the existing Markdown-first architecture, not a hard-to-reverse infrastructure or source-of-truth decision.

## Status Cleanup

After this review is accepted for downstream reliance, update the canonical architecture status note that currently says the exercise-method guidance amendment is drafted for review by this file. It should say the amendment was approved by this review. This is a status-only cleanup and does not require another architecture review.

## Recommendation

Approve the architecture amendment for downstream planning. This direct architecture-review request remains isolated and does not automatically hand off to `plan`.
