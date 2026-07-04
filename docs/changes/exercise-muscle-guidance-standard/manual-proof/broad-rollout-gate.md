# Broad Rollout Gate

## Scope

- Change ID: `exercise-muscle-guidance-standard`
- Milestone: M3
- Proof ID: XMG-M4
- Pages checked: current `exercises/` inventory outside the M2 proof slice.
- Criteria: list remaining exercise pages and classify each as keep as-is for now, rename only, rewrite role guidance, revise `## What you should feel`, source-audit needed, or future image candidate.
- Check date: 2026-07-04

## Result

Pass for M3 implementation handoff.

This gate records future migration decisions only. It does not authorize a broad unreviewed rewrite, checker escalation for all legacy pages, new images, new exercises, or source changes.

## Decision Categories

- keep as-is for now: leave outside the next batch unless a separate plan selects it.
- rename only: update `## Used muscles` to `## Muscles involved` only when nearby content already meets the accepted contract.
- rewrite role guidance: replace list-style anatomy wording with role-based or phase-linked guidance.
- revise `## What you should feel`: add or align the paired feel section with the muscle roles.
- source-audit needed: review page-local support for muscle, feel, compensation, setup, movement, and safety claims before or during migration.
- future image candidate: consider a broad-region support image only if Markdown is already clear and the image materially improves comprehension.

## Remaining Page Classification

| Page | Current state | Decision category | Rationale | Next safe slice |
| --- | --- | --- | --- | --- |
| `exercises/bird-dog.md` | legacy `## Used muscles`; no paired feel section | rewrite role guidance; revise `## What you should feel`; source-audit needed | Trunk/limb control should explain bracing and cross-body control rather than only listing muscles. | trunk-control batch |
| `exercises/dead-bug.md` | legacy `## Used muscles`; no paired feel section | rewrite role guidance; revise `## What you should feel`; source-audit needed | Similar to plank, but should explain ribs/pelvis control and limb motion. | trunk-control batch |
| `exercises/glute-bridge.md` | legacy `## Used muscles`; no paired feel section | rewrite role guidance; revise `## What you should feel`; source-audit needed | Needs driver/support wording and careful low-back compensation language. | lower-body control batch |
| `exercises/hip-hinge.md` | legacy `## Used muscles`; no paired feel section | rewrite role guidance; revise `## What you should feel`; source-audit needed | Needs hip/trunk role wording and non-diagnostic compensation cues. | lower-body control batch |
| `exercises/incline-push-up.md` | already newer exercise-method page; not in M2 proof slice | rewrite role guidance; revise `## What you should feel`; source-audit needed | Pressing pattern can reuse chest-press role structure, but bodyweight setup needs its own source audit. | upper-body push batch |
| `exercises/kneeling-hip-flexor-stretch.md` | legacy `## Used muscles`; no paired feel section | rename only only if stretch wording already distinguishes mobility/stretch from strengthening; otherwise rewrite role guidance; revise `## What you should feel`; source-audit needed | Stretch page must avoid treating the target region as hard contraction. | mobility/stretch batch |
| `exercises/lat-pulldown.md` | newer page already has `## Muscles involved` and feel section | keep as-is for now; source-audit needed before content edits | It is outside M2 and already passes current checker; later review should assess whether role table would improve clarity. | upper-body pull batch |
| `exercises/prone-y-t.md` | newer forward-head support page with muscle image | rewrite role guidance; revise `## What you should feel`; source-audit needed; future image candidate | Existing muscle-attention image should be aligned with role text if the page is selected. | shoulder-control batch |
| `exercises/seated-row.md` | newer first-slice exercise page | keep as-is for now; source-audit needed before content edits | It may be a good later role-table candidate, but M2 already used chest press for machine/resistance. | upper-body pull batch |
| `exercises/wall-slide.md` | newer forward-head support page with muscle image | rewrite role guidance; revise `## What you should feel`; source-audit needed; future image candidate | Shoulder-blade and rib control should be checked against source support and image alignment together. | shoulder-control batch |

## Rollout Rule

Future migration should use small reviewed batches. A later implementation slice should select one batch, add tests or manual proof for that batch, update pages, run source audit, and keep untouched legacy pages compatible until selected.

## Residual Risk

This gate is an inventory and batching decision, not a source audit for remaining pages. Any new exercise page, deleted page, source change, or broad checker escalation should update this gate or supersede it with a reviewed plan.
