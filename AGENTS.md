# Agent Operating Rules

This file is the quick-start rule set for AI agents working in this repository. `CONSTITUTION.md` is authoritative when more detail is needed.

## Source Order

Agents MUST resolve conflicts in this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Accepted proposals in `docs/proposals/`
4. Approved specs in `specs/`
5. Architecture artifacts and ADRs in `docs/architecture/` and `docs/adr/`
6. Execution plans and rationale in `docs/changes/<change-id>/`
7. Tests, fixtures, and validation evidence
8. Code, content, schemas, configuration, and generated artifacts
9. Chat context

When sources conflict, agents MUST stop and surface the conflict unless the requested change explicitly updates the higher-ranked source.

## Work Rules

- Agents MUST keep GymPrimer aligned with `CONSTITUTION.md` and `VISION.md`: a Markdown-first, citation-based beginner primer, not a workout planner, clinical product, AI coach, hosted app, or video-first media project. Expanded pattern, condition, programming-literacy, or program-example content MUST NOT rely on the Responsible Breadth direction until ADRs, specs, architecture, plans, tests, and validation are updated in source-of-truth order.
- Agents MUST use the standard workflow for material changes: proposal when direction is uncertain, spec before behavior or content-contract changes, architecture before cross-component or data-model decisions, plan before multi-step implementation, tests before production changes, review before completion claims, and verification before handoff.
- Agents MAY invoke an individual skill directly for isolated work, but MUST report what artifact was changed and what validation was run.
- Agents MUST NOT implement substantive behavior, Markdown content contracts, citation policy, safety, localization, licensing, generated output, or media-source changes from chat alone. Capture the requirement in the appropriate durable artifact first.
- Agents MUST add or update tests for behavior changes and regression tests for bugs. If no test framework exists yet, agents MUST document the validation gap and prefer establishing minimal test infrastructure before broad implementation.
- Agents MUST NOT claim CI passed unless a CI run was actually observed. Local command results MUST be reported with the exact command.
- Agents MUST NOT introduce secrets, private data, unlicensed media, generated exercise guidance as source of truth, unsupported safety claims, or medical advice.
- Agents MUST keep changes focused. Unrelated refactors, broad rewrites, and formatting churn require explicit justification.
- Agents MUST preserve user changes in the working tree and MUST NOT reset, overwrite, or discard them without explicit instruction.
