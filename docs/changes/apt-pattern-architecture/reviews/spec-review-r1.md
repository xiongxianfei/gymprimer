# Spec Review R1: APT Pattern Architecture Spec Amendment

Date: 2026-06-29
Review surface: `specs/responsible-breadth.md`
Reviewer role: spec reviewer

Reviewed artifacts:

- `specs/responsible-breadth.md`
- `specs/markdown-first-primer.md`
- `docs/architecture/system/architecture.md`
- `docs/changes/apt-pattern-architecture/reviews/architecture-review-r1.md`
- `docs/workflows.md`

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: SR-APT-SPEC-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/apt-pattern-architecture/reviews/spec-review-r1.md`
- Review log: `docs/changes/apt-pattern-architecture/review-log.md`
- Review resolution: `docs/changes/apt-pattern-architecture/review-resolution.md`
- Open blockers: SR-APT-SPEC-1
- Immediate next stage: spec revision
- Eventual test-spec readiness: not-ready
- Stop condition: resolve SR-APT-SPEC-1 before test-spec, planning, or implementation relies on the amended media requirements

## Findings

## Finding SR-APT-SPEC-1

- Finding ID: SR-APT-SPEC-1
- Severity: major
- Location: `specs/responsible-breadth.md` R35a, R63, AC12; inherited `specs/markdown-first-primer.md` R50
- Evidence: The amended Responsible Breadth spec says pattern, condition, and exercise visuals may use high-quality human-reviewed AI-generated raster illustrations when an SVG is hard to interpret, and it allows optional example pictures for pattern-page exercise previews when media provenance passes. It also inherits the existing Markdown-first media provenance contract. The inherited contract allows only `media_purpose = equipment_identification` or `key_movement_illustration`. Pattern alignment visuals and condition anatomical-region visuals are not deterministically equipment-identification or key-movement illustrations, so a validator or reviewer would have to guess whether those new image uses fit the old enum.
- Required outcome: The spec must define a deterministic media-purpose compatibility rule for generated raster images used by pattern and condition pages before downstream test-spec or implementation relies on R35a, R63, or AC12.
- Safe resolution path: Revise `specs/responsible-breadth.md` to either: (a) limit generated raster support in this amendment to existing allowed purposes only, such as exercise movement and equipment images, while keeping pattern/condition alignment or anatomy visuals SVG/text-only until a later media-purpose amendment; or (b) explicitly extend the Responsible Breadth media-purpose enum for expanded pages with values such as `pattern_alignment_illustration` and `anatomical_region_illustration`, then add matching compatibility, validation, edge-case, and acceptance-criteria language. If option (b) is chosen, update or supersede the media provenance contract in the appropriate spec/ADR path before implementation.
- needs-decision rationale: none

## Dimension Review

| Review dimension | Verdict | Notes |
| --- | --- | --- |
| requirement clarity | concern | Pattern-page requirements R57-R63 are clear; media-purpose compatibility for generated pattern/condition images is ambiguous. |
| normative language | pass | The amendment uses testable MUST/MUST NOT language and bounded MAY/SHOULD clauses. |
| completeness | concern | The new media allowance is missing the closed-enum compatibility rule needed for pattern and condition visuals. |
| testability | block | Test-spec cannot deterministically map generated pattern/condition raster images to valid provenance purpose values until SR-APT-SPEC-1 is resolved. |
| examples | concern | Existing examples cover necessary visuals and provenance generally, but no example covers a generated pattern-alignment or condition-region image. |
| compatibility | block | The amended media allowance conflicts with, or at least underspecifies interaction with, the inherited Markdown-first `media_purpose` enum. |
| observability | pass | Review records, manual proof, validation output, and provenance evidence remain observable once the enum ambiguity is resolved. |
| security/privacy | pass | No new user-data, symptom collection, identification, or AI source-of-truth behavior is introduced. |
| non-goals | pass | Diagnosis, treatment, rehab, personalization, hosted app, CMS, and AI source-of-truth exclusions remain intact. |
| acceptance criteria | concern | AC12 requires approved provenance for generated raster images, but approved provenance depends on an allowed purpose that is ambiguous for pattern/condition visuals. |

## Summary

The pattern-page architecture amendment is directionally sound and specific
enough for downstream proof once the media-purpose ambiguity is fixed. The
review does not challenge the approved architecture status or the pain-point to
exercise-option page contract. The only material blocker is the generated raster
visual allowance for pattern and condition pages without a deterministic
provenance-purpose mapping.

No automatic downstream handoff is performed. This direct spec-review request
remains isolated.
