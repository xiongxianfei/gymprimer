# Plan Review R2: Media Provenance Plan Amendment

## Result

- Skill: plan-review
- Review status: changes-requested
- Material findings: PR-MEDIA-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/plan-review-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: PR-MEDIA-1
- Immediate next stage: plan revision

## Findings

### PR-MEDIA-1 - M3A sequencing conflicts with the live blocked milestone

- Severity: major
- Location:
  `docs/plans/2026-06-27-markdown-first-gym-primer.md`,
  Current Handoff Summary and M3A milestone.
- Evidence: The plan adds M3A as the milestone that must make media
  classification and provenance executable before generated pictures are added.
  However, the Current Handoff Summary still says the current milestone is
  `M3. Five-Page First Slice and Beginner Read-Test Evidence`, its state is
  `blocked`, and remaining implementation milestones are `M3, M3A, M4`. Under
  the plan's normal milestone loop, a blocked M3 prevents a clear handoff to
  implement M3A after test-spec review. The plan therefore does not say whether
  the next implementation target is still blocked M3/MP3 evidence or the new
  M3A media validation work.
- Required outcome: The plan must make the next executable implementation
  target unambiguous before test-spec and implementation handoff.
- Safe resolution path: Revise the Current Handoff Summary, plan index, change
  metadata, and M3/M3A dependency text to choose one sequence:
  - Option A: make M3A the next implementation milestone after test-spec
    review, while keeping M3 promotion/code-review blocked until MP3 beginner
    read-test evidence is collected and any referenced media passes M3A; or
  - Option B: keep M3 as the next implementation milestone and state that M3A
    cannot start until MP3 closes M3.

## Review dimensions

- Self-contained context: pass. The plan names the approved spec,
  architecture-review R3, media ADR, and old-platform supersession context.
- Source alignment: pass. M3A maps to R41-R53, AC15-AC19, and the approved
  media architecture without expanding media scope.
- Milestone size: pass. M3A is a coherent implementation slice: checker,
  fixtures, provenance table, and optional images.
- Sequencing: block. PR-MEDIA-1 leaves the next executable milestone ambiguous
  because M3 remains blocked while M3A is introduced as planned work.
- Scope discipline: pass. The plan keeps AI raster images limited to equipment
  identification or key movement illustration and excludes third-party,
  medical, rehab, identifying-person, and non-AI raster media.
- Validation quality: concern. M3A has strong unit/checker commands; the
  non-gating `rg ... || true` command should be treated only as inspection
  evidence, not as a closeout gate.
- TDD readiness: pass after PR-MEDIA-1. The listed media fixtures are specific
  enough for a test-spec update once sequencing is clarified.
- Risk coverage: pass. The plan names parser gaps, brittle provenance-table
  parsing, and misleading generated images.
- Architecture alignment: pass. The plan follows the extension-based classifier
  and centralized `media/PROVENANCE.md` decision.
- Operational readiness: concern. The plan should clarify whether
  `media/PROVENANCE.md` is created empty in M3A even if no optional raster
  images are added, but this does not block review.
- Plan maintainability: concern. The plan is long and has known MD013 debt, but
  the new M3A content is findable and scoped.

## Advisory notes

- Treat the M3A `rg ... || true` command as an observability check only. The
  closeout gate should be the unit/checker suite and checker output.
- If Option A is chosen, update `current_milestone` in
  `docs/changes/markdown-first-gym-primer/change.yaml` only when the workflow
  actually advances to implementation after test-spec review.

## Readiness

The plan is not ready for test-spec handoff until PR-MEDIA-1 is resolved and
plan-review R3 approves the revised sequencing.
