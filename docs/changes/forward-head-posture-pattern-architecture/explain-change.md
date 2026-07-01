# Change Rationale: Forward Head Posture Pattern Architecture

## Summary

This change implements the reviewed forward-head-posture proof slice as a
repeatable pattern-page architecture. It adds deterministic validation first,
then five same-slice exercise pages, then `patterns/forward-head-posture.md`
with one approved comparison image, and finally README non-promotion evidence.

The work stays inside GymPrimer's Markdown-first boundary: static Markdown
pages, local checks, tests, media provenance, and review records. It does not
add a runtime app, user-input flow, symptom checker, hosted surface, CMS,
database, generated output path, CI workflow, or README promotion for the
single pattern page.

## Problem

The repository needed a best-practice pattern architecture that could explain
why a pattern matters, route red flags before self-management themes, connect
likely contributors to exercise options, and keep source support and media
governance strong enough for future pattern pages.

The selected proof slice was `Forward Head Posture`. The page needed to be
beginner-readable without diagnosing the reader, promising posture correction,
or turning exercise options into a treatment routine.

## Decision Trail

The accepted proposal chose a two-pattern future direction, but this
implementation focuses only on `patterns/forward-head-posture.md`. The title is
`Forward Head Posture`; README promotion waits for the approved pattern set;
and the first proof slice uses one comparison image only, not exercise
thumbnails.

The approved spec is `specs/forward-head-posture-pattern-architecture.md`.
Key requirements are R1-R11 for the pattern page, R12-R19 for the complete
exercise loop, R20-R23 for the one-image media boundary, R24-R27 for automated
link, image, source, privacy, and README-gate checks, and R28-R32 for scope,
artifact responsibility, validation reporting, and focused assertions.

The approved test spec is
`specs/forward-head-posture-pattern-architecture.test.md`. It maps R1-R32 and
AC1-AC17 to FHP-T1 through FHP-T12, FHP-CMD1 through FHP-CMD13, and review-only
semantic checks FHP-RO1 through FHP-RO3. Review-only evidence is recorded in
normal code-review records, not in a separate manual-proof artifact.

The architecture update keeps pattern pages as static Markdown under
`patterns/`, exercise support pages under `exercises/`, reusable sources in
`SOURCES.md`, central safety routing in `RED-FLAGS.md`, and optional raster
media under `media/` with `media/PROVENANCE.md`. ADR
`docs/adr/2026-06-30-central-red-flags-disclaimer.md` assigns the prominent
disclaimer to `RED-FLAGS.md` instead of repeating it on every page.

The execution plan closed four implementation milestones: M1 validation
contract, M2 same-slice exercise pages, M3 pattern page and media, and M4 README
promotion-gate evidence.

## Diff Rationale By Area

| Area | Files | Change | Reason | Evidence |
| --- | --- | --- | --- | --- |
| Governing scope | `CONSTITUTION.md`, `CONTRIBUTING.md`, `specs/markdown-first-primer.md`, `specs/responsible-breadth.md`, related test specs | Aligned language around root `RED-FLAGS.md`, central disclaimer ownership, expanded static content, and non-runtime boundaries. | Needed after owner clarification that the prominent disclaimer belongs in `RED-FLAGS.md`, not repeated everywhere. | Spec-review R2, architecture-review R2, test-spec-review R3, code-review M1 R2. |
| Forward-head contract | `docs/proposals/2026-06-30-forward-head-posture-pattern-architecture.md`, `specs/forward-head-posture-pattern-architecture.md`, `specs/forward-head-posture-pattern-architecture.test.md` | Recorded the accepted title, five selected exercises, broader secondary exercise list, README pattern-set gate, source-family requirements, and validation command ownership. | Made chat decisions durable before implementation. | Proposal-review R2, spec-review R1/R2, test-spec-review R2/R3. |
| Architecture | `docs/architecture/system/architecture.md`, `docs/architecture/system/diagrams/container.mmd`, ADRs | Located pattern pages, exercise pages, central red flags, source index, media provenance, and promotion gates in the system architecture. | Future pattern pages need a model stronger than a template-only convention. | Architecture-review R1/R2. |
| Authoring templates | `docs/templates/pattern-page.md`, `docs/templates/exercise-card.md`, related templates | Kept templates as authoring prompts and routed safety context to root red flags instead of embedding repeated disclaimer text. | Templates should help authors, while the spec and architecture own normative policy. | Template tests and Markdown-first checks. |
| Validation tooling | `tools/checks/check_markdown_first.py`, Markdown-first tests, Responsible Breadth tests | Added focused checks for forward-head pattern sections, detailed exercise links, same-slice exercise-page contract, image existence, media provenance, central disclaimer availability, forbidden language, and README non-promotion. | R24-R27 and R32 required deterministic checks or focused assertions before claiming coverage. | FHP-CMD1 through FHP-CMD13; code-review M1 R2 and M4 R1. |
| Exercise content | `exercises/chin-nod.md`, `exercises/thoracic-extension.md`, `exercises/wall-slide.md`, `exercises/prone-y-t.md`, `exercises/band-pull-apart.md`, `SOURCES.md` | Added the five complete-loop exercise pages with setup, movement, muscle, cue, mistake, progression, safety, and source sections. | The pattern page's detailed exercise options must link to real same-slice exercise pages. | M2 validation and code-review M2 R3. |
| Exercise source support | Same five exercise pages, `docs/changes/.../review-resolution.md` | Replaced broad source uses with direct page-local instruction sources for setup and technique, kept PubMed/PMC sources for muscle/activity claims, softened unsupported claims, and removed no-longer-reused global source entries. | CR-FHP-M2-1 showed semantic source-to-claim fit was the real blocker. | FHP-RO2 evidence and remediation table; code-review M2 R3. |
| Pattern content | `patterns/forward-head-posture.md` | Added a non-diagnostic page with title, red flags, beginner observations, self-observation, core reasons, uncertainty, detailed exercise annotations, secondary exercise list, routing, and page-local sources. | R1-R14 and R18-R19 required a complete pattern page that explains the pattern without becoming a treatment plan. | M3 validation and code-review M3 R2. |
| Pattern source support | `patterns/forward-head-posture.md` | Used four source families: red flags and professional routing, posture-pattern uncertainty, shoulder/scapular context, and general resistance-training framing. Revised contributors to include anterior neck or chest tone and posterior upper-back strength. | CR-FHP-M3-1 found the first core-reason model did not fully project R8. | FHP-RO1 evidence; code-review M3 R2. |
| Media | `media/patterns/forward-head-posture/forward-head-posture-comparison.png`, `media/PROVENANCE.md`, media-purpose ADR | Added one generated raster comparison image with approved provenance and `pattern_alignment_illustration` purpose. | The proposal recommended one comparison image only, with no in-image text or exercise thumbnails. | FHP-T9, FHP-RO3, M3 checks. |
| README gate | `tests/test_responsible_breadth_m1.py`; README intentionally unchanged | Added a focused assertion and command evidence that README does not link to the single forward-head pattern page. | R27 requires promotion to wait for the full approved pattern set. | FHP-T10/FHP-CMD12; code-review M4 R1. |
| Fixture alignment | `tests/test_repository_layout_normalization.py` | Updated a temporary `RED-FLAGS.md` fixture to include the central disclaimer. | Full-suite M4 validation exposed a stale fixture that no longer matched the active checker contract. | M4 validation and code-review M4 R1. |
| Workflow records | `docs/changes/forward-head-posture-pattern-architecture/*`, `docs/plans/2026-06-30-forward-head-posture-pattern-architecture.md`, `docs/plan.md` | Recorded proposal/spec/architecture/test/plan/code-review outcomes, review-resolution evidence, milestone state, validation commands, and current handoff. | The workflow requires durable state and review traceability before final verification and PR handoff. | Review log, review-resolution, M4 R1. |

## Tests Added Or Changed

M1 extended Responsible Breadth and Markdown-first validation so missing
pattern sections, broken detailed exercise links, invalid media references,
forbidden diagnostic or treatment language, missing central disclaimer
availability, and invalid source sections fail locally.

M2 added real-page coverage for the five exercise pages. The implementation
first ran the focused exercise-page test before content existed and observed
the expected missing-page failure, then reran it after adding the pages.

M3 added real-page coverage for `patterns/forward-head-posture.md` and media
contract checks. The focused pattern-page test first failed with the expected
missing page, then passed after implementation.

M4 added
`test_forward_head_page_is_not_promoted_from_readme_before_pattern_set` and
kept README unchanged. It also aligned the repository-layout fixture so full
unittest validation reflects the current central-disclaimer contract.

## Validation Evidence Available Before Final Verify

The latest implementation review, code-review M4 R1, reran and passed:

- `python3 -m unittest discover -s tests` - 88 tests.
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises` - checked 24 Markdown files.
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md patterns conditions principles programs exercises media docs/changes/forward-head-posture-pattern-architecture` - checked 60 files.
- `if rg -n "patterns/forward-head-posture.md" README.md; then exit 1; else echo 'README promotion gate passed: no forward-head pattern link'; fi`.
- `git diff --check`.

Earlier milestone validation is recorded in the plan's validation notes. No
hosted CI run has been observed or claimed. Final `verify` remains pending.

## Review Resolution Summary

Material finding closeout is recorded in
`docs/changes/forward-head-posture-pattern-architecture/review-resolution.md`.
Seven material findings were recorded and closed or superseded:

- PR-FHP-1 and PR-FHP-2 were resolved by proposal-review R2.
- TSR-FHP-1 and TSR-FHP-2 were resolved by test-spec-review R2.
- CR-FHP-M1-1 was superseded by the approved central-disclaimer amendment and
  confirmed by code-review M1 R2.
- CR-FHP-M2-1 was resolved by direct exercise-instruction source support and
  code-review M2 R3.
- CR-FHP-M3-1 was resolved by revising the core-reason contributor model and
  code-review M3 R2.

Code-review M4 R1 found no material issues and closed the final implementation
milestone. There are no open findings in `review-log.md`.

## Alternatives Rejected

The change did not promote the single forward-head pattern from README because
the approved requirement gates promotion on the full pattern set.

It did not add exercise thumbnails to the pattern page. Exercise pages carry
their own details; the pattern page uses one comparison image as support only.

It did not keep broad sources attached to specific exercise setup or technique
claims. Those claims now use direct instruction sources or are softened or
removed.

It did not repeat the prominent disclaimer on every page. `RED-FLAGS.md` owns
the central disclaimer, and page content routes safety context there.

It did not add new tooling for semantic source support. Claim-to-source fit is
handled through review-only FHP-RO1 and FHP-RO2 evidence because static parsing
cannot reliably prove semantic support.

## Scope Control

This slice added one pattern page, five supporting exercise pages, one optional
pattern image, and directly needed validation and governance updates. It did
not implement rounded shoulders or another pattern page, create a clinical
workflow, personalize recommendations, define a routine, or expand README
navigation.

The broader collected exercise list on the pattern page remains secondary and
does not become a detailed routine because those additional exercises are not
part of the same-slice complete loop.

## Risks And Follow-Ups

Final `verify` still needs to rerun the final readiness checks and record a
verify report before PR handoff.

Semantic source support remains partly review-owned. The current slice records
FHP-RO1, FHP-RO2, and FHP-RO3 evidence, but future pattern pages must repeat
that discipline instead of relying on checker existence alone.

README promotion is intentionally blocked until the approved pattern set is
ready. A later change should promote pattern navigation only after the complete
set passes its own review and verification.

## Current Handoff

M1 through M4 are closed, code-review M4 R1 recorded no material findings, and
review-resolution is closed with no open findings. This explain-change artifact
is the durable rationale for the reviewed diff. The next workflow stage is
`verify`; final verification and PR handoff are not yet claimed.
