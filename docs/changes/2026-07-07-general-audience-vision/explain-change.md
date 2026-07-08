# Explain Change: General-Audience Vision

## Status

draft

## Summary

This change updates GymPrimer from a beginner-only primer to a general-audience exercise, movement, and training-literacy primer.

The user explicitly requested that the project not be limited only to beginners and that it should be useful for everyone.
Because `CONSTITUTION.md` outranks `VISION.md`, the governance update is made alongside the vision update instead of changing vision text alone.

## Positioning Delta

| Area | Before | After |
| --- | --- | --- |
| Audience | Adults in their first ninety days of regular gym training or returning after a long break. | People who want to train with more understanding, from first-time gym users to experienced readers. |
| Product promise | Verifiable beginner understanding. | Verifiable exercise, movement, and training understanding. |
| Scope boundary | Conservative beginner scope. | Conservative static-education scope. |
| Advanced content | Treated as likely out of vision. | Allowed when framed as exercise literacy and governed by proposal, spec, architecture, plan, tests, and review. |
| Refusals | No diagnosis, individualized medical advice, personal plans, clinical product, AI coach, or media-first product. | Same refusals preserved. |

The positioning rationale is recorded in `docs/vision/strategic-positioning.md`.

## Files Changed

| File | Reason |
| --- | --- |
| `CONSTITUTION.md` | Updates the highest-ranked project purpose and active content model. |
| `VISION.md` | Rewrites the canonical project vision for a general audience. |
| `README.md` | Synchronizes the generated vision front matter from `VISION.md`. |
| `AGENTS.md` | Aligns agent quick rules with the broader source-of-truth scope. |
| `CONTRIBUTING.md` | Aligns contributor-facing scope with general-audience static education. |
| `docs/vision/strategic-positioning.md` | Records strategic-positioning rationale for material repositioning. |

## Preserved Boundaries

The change does not authorize personalized plans, diagnosis, medical advice, treatment, recovery protocols, sport-specific competition programming, hosted coaching flows, user tracking, or media-first instruction.

It does not implement advanced pages directly.
Downstream proposals, specs, architecture, plans, tests, reviews, and verification are still required for material content or validation changes.

## Validation

Local validation passed:

- `python3 -m unittest discover -s tests`
- `python3 tools/checks/check_markdown_first.py README.md docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- `python3 tools/checks/check_privacy.py AGENTS.md CONSTITUTION.md VISION.md README.md CONTRIBUTING.md docs/project-map.md docs/vision/strategic-positioning.md docs/changes/2026-07-07-general-audience-vision docs/proposals/2026-07-07-advanced-rowing-machine-tutorial.md`
- `git diff --check`
- `python3 tools/checks/check_markdown_first.py README.md SOURCES.md RED-FLAGS.md principles exercises patterns`
- `python3 tools/checks/check_privacy.py README.md SOURCES.md RED-FLAGS.md docs specs tools tests principles exercises patterns`
- `wc -w VISION.md`

The word-count check reported 693 words for `VISION.md`, below the 900-word hard limit.
Hosted CI was not observed.
