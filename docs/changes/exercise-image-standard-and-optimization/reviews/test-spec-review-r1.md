# Test Spec Review R1: Exercise Image Standard

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-EIS-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/exercise-image-standard-and-optimization/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/exercise-image-standard-and-optimization/review-log.md`
- Review resolution: `docs/changes/exercise-image-standard-and-optimization/review-resolution.md`
- Open blockers: TSR-EIS-1
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none
- Isolation: direct review request; no automatic downstream handoff.

## Findings

## Finding TSR-EIS-1

- Finding ID: TSR-EIS-1
- Severity: major
- Location: `specs/exercise-image-standard.test.md` planned validation command ownership, EIS-CMD5; mirrored plan command in `docs/plans/2026-07-03-exercise-image-standard.md` M2 validation.
- Evidence: EIS-CMD5 classifies `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md` as `existing and extended` for M2. A no-side-effect review dry-run of that exact command failed on current repository templates with product-page findings including `docs/templates/exercise-card.md: source_id_missing_from_sources_md`, `docs/templates/exercise-card.md: MF005`, `docs/templates/condition-page.md: MF003`, and excluded-scope terms in templates. The same command is named in the M2 validation section of the approved plan.
- Required outcome: The M2 validation command set must be executable and correctly classified before implementation relies on this proof map.
- Safe resolution path: Revise the test spec and the mirrored plan M2 validation command. Either replace EIS-CMD5 with an applicable template-specific check and keep the Markdown-first checker scoped to product pages, or explicitly make checker/template support a planned M1/M2 implementation obligation with tests proving the checker can validate templates without treating placeholder/template language as promoted product content.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Notes |
| --- | --- | --- |
| Governing-contract alignment | pass | The test spec maps the approved Exercise Image Standard requirements without changing product direction, architecture, or legacy image compatibility. |
| Requirement coverage | pass | R1-R38 each map to automated tests, manual proof, migration checks, or smoke checks. |
| Example coverage | pass | E1-E7 each map to stable EIS test IDs. |
| Negative and boundary coverage | pass | Empty, invalid purpose, missing provenance, non-approved provenance, bad paths, missing assets, generic alt text, unsafe wording, privacy, and compatibility cases are covered. |
| Proof-level adequacy | pass | Automated tests cover deterministic checker behavior; manual proof is reserved for visual semantics, beginner comprehension, and source-support fit. |
| Milestone mapping | concern | Milestone mapping is mostly clear, but TSR-EIS-1 leaves M2 command ownership ambiguous. |
| Command validity | block | EIS-CMD5 is labeled existing/extended but currently fails as a product-page checker command against templates. |
| Fixture and data design | pass | Temporary repositories, placeholder image bytes for deterministic tests, and final assets for manual review are separated. |
| Manual-proof boundary | pass | EIS-RO1 through EIS-RO4 include rationale, exact steps, environment, evidence artifact, pass/fail conditions, and owning stage. |
| Observability | pass | EIS-T15 covers stable categories and field/page visibility; manual evidence IDs are traceable. |
| Determinism and isolation | pass | Tests are local, fixture-driven, and avoid network, image generation services, time, and shared mutable state. |
| Scope and non-goals | pass | The proof map avoids runtime, CMS, generated JSON, video-first behavior, medical-effectiveness tests, and existing image migration. |
| Execution economics | pass | Focused M1 checks precede full-suite and final milestone checks. |
| Traceability | pass | Requirements, examples, edge cases, test IDs, review-only IDs, and command IDs are consistently linked. |
| Implementation handoff | block | Implementation cannot proceed until TSR-EIS-1 is resolved and re-reviewed. |

## Command Checks Performed During Review

- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md docs/templates media/PROVENANCE.md` failed as described in TSR-EIS-1.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media/PROVENANCE.md` returned zero.
- `python3 -m unittest tests.test_markdown_first_guardrails tests.test_responsible_breadth_m1` returned zero.

## Readiness

The test spec is not approved for implementation handoff. Revise the test spec
and mirrored plan M2 command ownership, then rerun test-spec-review.
