# Spec Review R3: Markdown-First Gym Primer Media Provenance

## Result

- Skill: spec-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/spec-review-r3.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: none
- Immediate next stage: architecture
- Eventual test-spec readiness: conditionally-ready
- Stop condition: no automatic downstream handoff; normalize spec status to
  `approved` before architecture, test-spec, plan, or implementation relies on
  the amended spec

## Review inputs

- Spec reviewed: `specs/markdown-first-primer.md`
- Review scope: SR-MEDIA-1 rereview for the AI-generated raster illustration
  media provenance amendment.
- Prior finding: `docs/changes/markdown-first-gym-primer/reviews/spec-review-r2.md`
- Resolution record: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Workflow state: `docs/workflows.md`,
  `docs/changes/markdown-first-gym-primer/change.yaml`, and `docs/plan.md`

## Findings

None

## Finding reconciliation

- Finding ID: SR-MEDIA-1
- Prior status: open from `spec-review-r2`
- R3 result: resolved
- Evidence: The spec now defines `media/PROVENANCE.md`, required fields, exact
  `asset_path` matching, allowed `media_purpose` values, `review_status`
  values, `page_refs`, and stable media failure codes.

## Review dimensions

- Requirement clarity: pass. The amended requirements now define allowed media
  purpose values, centralized provenance, exact path matching, required fields,
  review status values, and page-reference consistency.
- Normative language: pass. The new `MUST` clauses are testable by inspecting
  Markdown image references, `media/PROVENANCE.md`, and validation output.
- Completeness: pass. The spec covers text-only pages, allowed image purposes,
  preference order, provenance shape, missing/incomplete/non-approved
  provenance, out-of-scope media use, and page-ref mismatch.
- Testability: pass. R46-R53 and AC15-AC19 can be mapped to deterministic
  fixtures and checker cases.
- Examples: pass. E6 covers valid AI media, E7 covers no-image pages, and E8
  covers missing provenance.
- Compatibility: pass. `asset_path` values become compatibility surfaces once
  referenced by promoted pages.
- Observability: pass. The spec names stable failure codes:
  `media_provenance_missing`, `media_provenance_incomplete`,
  `media_provenance_not_approved`, `media_usage_out_of_scope`, and
  `media_page_refs_mismatch`.
- Security/privacy: pass. The amendment keeps private people, identifying
  marks, undocumented source images, unsafe setup, medical treatment, and
  misleading branding out of scope.
- Non-goals: pass. It still excludes external photos, screenshots, stock
  assets, borrowed web images, commercial machine screenshots, unreviewed AI
  media, AI coaching, rehab, and advanced lifting.
- Acceptance criteria: pass. AC15-AC19 make optional media, allowed purposes,
  required provenance fields, approved status, and failure modes observable.

## Routing Assessment

Immediate next stage is `architecture` because the approved media amendment
adds a repository-level media provenance surface under `media/PROVENANCE.md`
and affects validation-tool boundaries, contributor guidance, and downstream
proof obligations.

Eventual test-spec readiness is `conditionally-ready`: test-spec revision can
proceed after architecture confirms the media provenance boundary and the spec
status is normalized from `draft` to `approved`.

## Recommended Edits

No required spec edits before approval.

Before downstream reliance, normalize `specs/markdown-first-primer.md` status
from `draft` to `approved`.

## Recommendation

Approve the media provenance amendment. SR-MEDIA-1 is resolved.
