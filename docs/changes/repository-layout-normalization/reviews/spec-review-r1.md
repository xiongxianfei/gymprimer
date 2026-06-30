# Spec Review R1: Repository Layout Normalization

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-RLN-1, SR-RLN-2, SR-RLN-3
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/repository-layout-normalization/reviews/spec-review-r1.md`
- Review log: `docs/changes/repository-layout-normalization/review-log.md`
- Review resolution: `docs/changes/repository-layout-normalization/review-resolution.md`
- Open blockers: old-path policy, root red-flags policy, media migration determinism
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: do not route to architecture, test-spec, plan, or implementation until SR-RLN-1, SR-RLN-2, and SR-RLN-3 are resolved.

## Review Dimensions

| Review dimension | Verdict |
| --- | --- |
| requirement clarity | concern |
| normative language | concern |
| completeness | block |
| testability | block |
| examples | concern |
| compatibility | concern |
| observability | pass |
| security/privacy | pass |
| non-goals | pass |
| acceptance criteria | concern |

## Findings

## Finding SR-RLN-1

- Finding ID: SR-RLN-1
- Severity: blocking
- Location: `specs/repository-layout-normalization.md` lines 41-46, 145-152, 198-202, 290-294
- Evidence: Example E1 allows either removing old paths or keeping compatibility stubs. R20-R22 define stub constraints but leave the removal-versus-stub decision to the migration plan. Open question 1 asks the same unresolved question. This is a compatibility surface because the old v0.1 paths are currently required by `specs/markdown-first-primer.md` R2.
- Required outcome: The spec must choose the old-path compatibility policy before downstream test-spec and migration planning rely on it.
- Safe resolution path: Add a "Legacy path policy" section that chooses one deterministic rule. Recommended rule: keep short compatibility stubs for the original five v0.1 Markdown paths for one review window, exclude those stubs from duplicate content validation, remove them from active navigation, and require all promoted content to link to canonical paths. Then update E1, R20-R22, error behavior, acceptance criteria, and open questions to match.
- needs-decision rationale: none

## Finding SR-RLN-2

- Finding ID: SR-RLN-2
- Severity: major
- Location: `specs/repository-layout-normalization.md` lines 96-97, 243-247, 292-293; `docs/architecture/system/architecture.md` lines 175-176
- Evidence: R5 chooses `principles/` for `the former getting-started directory/` unless spec-review approves a root orientation exception, while open question 2 leaves the canonical red-flags path undecided. The architecture explicitly says root `RED-FLAGS.md` requires a spec update because current pages and checks reference `the former nested red-flags path.md`.
- Required outcome: The spec must define canonical treatment for root/project-reference safety routing and beginner orientation paths, rather than asking spec-review or a later plan to choose implicitly.
- Safe resolution path: Keep `the former nested red-flags path.md` as canonical for this migration and state that root `RED-FLAGS.md` is out of scope for this spec unless a later spec changes it. For `the former getting-started directory/beginner-training-principles.md`, choose `principles/beginner-training-principles.md` as canonical, or explicitly define one root orientation exception in the spec. Remove the "unless spec-review approves" phrasing.
- needs-decision rationale: none

## Finding SR-RLN-3

- Finding ID: SR-RLN-3
- Severity: major
- Location: `specs/repository-layout-normalization.md` lines 61-67, 103-104, 204-213, 257-259
- Evidence: Example E4 and EC1 treat subject-co-located media as the concrete expected path, but R7 only says media "SHOULD be moved toward" that layout. "Toward" and "where feasible" are not testable enough for a migration spec that will drive link and provenance checks.
- Required outcome: The spec must make media migration determinism observable: either require moved promoted media to end at `media/<content-type>/<slug>/...`, or explicitly limit this migration to content paths and defer media co-location.
- Safe resolution path: Replace R7 with a deterministic rule. Recommended rule: promoted raster media touched by this migration MUST move to `media/<content-type>/<slug>/`, and any promoted raster media not moved must be listed in the migration plan with a reason and no stale references. Then update AC6-AC7 and EC1-EC2 to match.
- needs-decision rationale: none

## Exact Wording Suggestions

Add a legacy path policy:

```md
## Legacy path policy

The original v0.1 Markdown paths are kept as compatibility stubs for one review window after canonical replacements are promoted. Compatibility stubs are short redirect-style Markdown files that link to the canonical page, contain no exercise instructions, are excluded from duplicate content validation, and are not listed in active navigation.

All promoted Markdown content must link to canonical paths after migration.
```

Replace R5:

```md
R5. The migration MUST fold `the former getting-started directory/beginner-training-principles.md` into `principles/beginner-training-principles.md`. Root orientation files are out of scope for this migration.
```

Add red-flags treatment:

```md
R5a. `the former nested red-flags path.md` remains the canonical red-flags reference for this migration. Moving it to root `RED-FLAGS.md` is out of scope unless a later spec changes the safety-reference path.
```

Replace R7:

```md
R7. Promoted raster media touched by this migration MUST use subject-co-located paths under `media/<content-type>/<slug>/`, with Markdown references and `media/PROVENANCE.md` updated in the same change.
```

## Routing

Immediate next stage is `spec revision`. This direct review is isolated; there is no automatic downstream handoff.
