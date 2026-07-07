# Architecture Assessment: Safer Running Basics and High-Quality Running Images

Date: 2026-07-06

Change ID: `2026-07-06-safer-running-basics-and-running-images`

Assessment: architecture-not-required

## Rationale

This change uses existing GymPrimer surfaces:

- Markdown exercise pages under `exercises/`;
- generated exercise media under `media/exercises/`;
- prompt records under `media/prompts/`;
- asset provenance in `media/PROVENANCE.md`;
- shared source registration in `SOURCES.md`;
- static validation checks under `tools/checks/` and `tests/`.

The accepted spec does not introduce a new runtime component, data store, API, hosted workflow, generated JSON contract, user account, adaptive coaching flow, deployment concern, or cross-system data movement. The page-specific six-image exception and `basic_cardio_activity` method usage are content-contract and validation concerns, not architectural changes.

## Boundaries

Implementation planning may update tests or checkers if existing validation cannot enforce the spec, but those updates stay within the current Markdown-first validation architecture.

If later work proposes video, animation, adaptive coaching, user inputs, generated data exports, or a new media pipeline, that later work will need a fresh architecture assessment.

## Next Stage

Proceed to execution planning.

## Sources

- `specs/safer-running-basics-and-running-images.md`
- `docs/proposals/2026-07-06-safer-running-basics-and-running-images.md`
