# Learn Session: Responsible Breadth Content Quality

## Frame

- Trigger: explicit `$learn` invocation after PR feedback and revision of the anterior-pelvic-tilt page, with maintainer confirmation that the document quality improved significantly.
- Trigger type: explicit maintainer request and contributor observation.
- Scope: quality-improvement approach for Responsible Breadth pattern/condition pages, using the anterior-pelvic-tilt page as the concrete example.
- Evidence in scope:
  - `patterns/anterior-pelvic-tilt.md`
  - `media/svg/patterns/anterior-pelvic-tilt-comparison.svg`
  - `SOURCES.md`
  - `docs/changes/responsible-breadth/explain-change.md`
  - `docs/changes/responsible-breadth/verify-report.md`
  - `docs/changes/responsible-breadth/manual-proof/RB-MP2-pattern-source-scope.md`
  - `docs/changes/responsible-breadth/manual-proof/RB-MP6-comprehension-proof.md`
  - `docs/changes/responsible-breadth/manual-proof/RB-MP7-visual-media-review.md`
  - Commit diff `HEAD~1..HEAD`
- Explicit exclusions:
  - No new spec, template, or page-contract amendment in this learn session.
  - No claim that one page proves all future pattern pages are solved.
  - No CI or PR-readiness claim.
  - No medical, diagnostic, or treatment guidance beyond summarizing the content-quality approach already used in the PR.
- Prior learnings reviewed:
  - `docs/learn/sessions/2026-06-27-unfriendly-exercise-learning-experience.md`
  - `docs/learn/sessions/2026-06-27-back-running-injury-learning-paths.md`
  - `docs/learn/sessions/2026-06-26-project-map-next-stage.md`
- Session record path: `docs/learn/sessions/2026-06-29-responsible-breadth-content-quality.md`

## Observe

- OBS-001: The first anterior-pelvic-tilt page satisfied the required Responsible Breadth page structure, metadata, citations, red-flag link, review date, and source section, but its body was too thin to give a beginner operational understanding.
- OBS-002: The successful revision kept the same page contract but expanded the educational payload: a working definition, neutral comparison, observation-not-diagnosis cues, topic-specific red flags, stronger uncertainty language, specific professional routing, and next-page routing.
- OBS-003: The revision changed the source mix from three supporting/professional pages to a stronger mix that includes institutional sources and peer-reviewed sources, and the manual proof was updated to name that source-quality improvement.
- OBS-004: Adding one original SVG alignment comparison improved beginner comprehension without adding raster provenance work, because the image is an original repository SVG and the pattern is inherently visual.
- OBS-005: The most valuable prose improvement was not more hedging. It was replacing vague boundary language with specific, cited claims plus explicit uncertainty where the evidence is mixed.
- OBS-006: The page-contract split suggested by the reviewer, making "How to notice this in yourself" a mandatory section, is plausible but belongs in a future spec/template amendment rather than a silent content-only change.
- OBS-007: Validation after the change caught a source-ID mistake, which confirms that automated structure checks remain useful even when the main quality improvement is semantic.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
| --- | --- | --- | --- | --- | --- |
| OBS-001 to OBS-005 | durable-lesson | durable-lesson | topic entry in `docs/learn/topics/content-quality.md` | Maintainer request states the document quality improved significantly and asks for best practices | The before/after diff and manual-proof updates show a reusable pattern for upgrading Responsible Breadth pages from structurally compliant placeholders into useful educational pages. |
| OBS-006 | process-follow-up | process-follow-up | future proposal/spec/template amendment | Maintainer request asks what can improve next; prior PR update explicitly deferred the contract change | Making "How to notice this in yourself" mandatory changes the page contract and needs the normal spec/template route. |
| OBS-007 | observation | observation | session record only | Local validation failure and fix during PR update | The source-ID check worked as intended; no new durable rule is needed beyond continuing to run validation after semantic edits. |

## Route

- Added topic entry: `docs/learn/topics/content-quality.md`.
- No spec, template, ADR, architecture, or workflow artifact was changed by this learn session.
- Follow-up candidate: propose a Responsible Breadth page-contract amendment that splits `Plain-language overview` into `Working definition` and `How to notice this in yourself` for pattern pages.

## Approach That Improved The Page

The improvement came from moving beyond structural compliance into reader usefulness:

1. Keep the page contract intact.
2. Start with a concrete working definition, not an abstract label.
3. Give the reader a comparison point, such as neutral alignment versus the pattern.
4. Add observation cues while repeatedly naming them as observation, not diagnosis.
5. Inline the most relevant red flags before linking the full red-flags reference.
6. Replace vague contributor lists with mechanisms and examples.
7. Make uncertainty explicit, especially where common coaching models outrun the evidence.
8. Use a necessary visual when the concept is visual.
9. Route to existing primer pages instead of leaving the reader with disconnected information.
10. Update sources and manual proof together so the content and evidence stay aligned.

## Best Practices

- Treat the contract as the floor, not the target. A page can pass required headings and still fail the beginner's real question.
- Define the thing in concrete body terms first: landmarks, positions, motion, or equipment parts.
- Use "how to notice" language for patterns, but keep it explicitly non-diagnostic.
- Prefer specific, source-backed claims over broad hedges.
- Put the strongest intellectual-honesty section where the evidence is mixed.
- Use at least two institutional or clinical/public-health sources plus supporting and peer-reviewed sources for health-adjacent pages.
- Add a visual only when it materially improves comprehension, and prefer original SVG for simple alignment diagrams.
- Avoid dead-end pages. End with "Where to next" links to real existing pages and name missing future pages as follow-ups rather than adding broken links.
- Keep manual proof records current after semantic edits, not only after structural edits.
- Rerun validation after content rewrites; citation/source-ID mistakes are easy to introduce during quality edits.

## What To Improve Next

- Amend the pattern-page contract, if accepted, to require a separate "How to notice this in yourself" section for pattern pages.
- Add the missing exercise pages that pattern pages naturally want to link to: glute bridge, dead bug, bird dog, plank, hip hinge/RDL, and kneeling hip-flexor stretch.
- Add a manual content-depth checklist for pattern and condition pages so "structurally valid but too thin" is caught before PR review.
- Add external beginner-reader testing before scaling beyond the proof slice.
- Consider a lightweight visual-review checklist for SVG pattern diagrams: labels, comparison frame, alt text, nearby explanation, and no unsupported anatomy claims.

## Validation

- Session and topic files created by direct inspection of the named evidence.
- No code or page contract changed.
