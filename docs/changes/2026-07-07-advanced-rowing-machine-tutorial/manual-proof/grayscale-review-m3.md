# M3 Grayscale Review

Date: 2026-07-07
Reviewer: xiongxianfei
Scope: advanced rowing force-intensity overlay assets

## Method

Force-intensity overlays were reviewed visually for non-color cues: brightness differences, outline strength, region boundaries, and texture. The goal was to confirm that broad emphasis remains understandable without relying only on hue.

## Results

| Asset | Force-intensity layer | Grayscale result | Notes |
| --- | --- | --- | --- |
| `media/exercises/rowing-machine-advanced/stroke-timing.png` | Yes | Pass | Phase panels retain distinguishable emphasis through lightness, outlines, and separated body regions. |
| `media/exercises/rowing-machine-advanced/rhythm-ratio.png` | Yes | Pass | Drive and recovery remain distinguishable through opacity/lightness and pose contrast. |
| `media/exercises/rowing-machine-advanced/force-curve.png` | Yes | Pass | Body emphasis and generic curve panel remain visually separable without relying only on color. |
| `media/exercises/rowing-machine-advanced/power-per-stroke.png` | Yes | Pass | Legs, trunk, and arm regions remain separated by outlines and lightness differences. |

## Non-overlay assets

The monitor, stroke-rate ladder, damper/drag-factor, and interval-structure assets do not use force-intensity overlays. They rely on abstract shape, size, position, and nearby Markdown rather than muscle-emphasis color.

## Disposition

All four force-intensity assets meet the M3 accessibility expectation that instructional emphasis remains understandable in grayscale. The page keeps the four-level legend in Markdown so color is not the only source of meaning.

## Sources

[local-advanced-rowing-page]: ../../../../exercises/rowing-machine-advanced.md
[local-advanced-rowing-test-spec]: ../../../../specs/advanced-rowing-machine-tutorial.test.md
[w3c-use-of-color]: https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
