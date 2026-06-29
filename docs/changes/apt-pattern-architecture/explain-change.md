# Explain Change: APT Pattern Architecture

## Problem

The first anterior pelvic tilt page was structurally compliant but still too thin to serve the user's main pattern-page journey. It explained the pattern and uncertainty, but it did not give a complete repository-native path from the beginner's pain point to mechanism-specific exercise options.

## Change

- Expanded `patterns/anterior-pelvic-tilt.md` into a fuller pattern page: pain-point entry, working definition, observation methods, core contributors, uncertainty, and an exercise menu.
- Kept the required Responsible Breadth headings so the page remains compatible with `specs/responsible-breadth.md`.
- Added `exercises/` pages for the first APT support set: dead bug, plank, bird dog, glute bridge, hip hinge, and kneeling hip-flexor stretch.
- Added AI-generated raster sequence images under `media/movements/` for those exercise pages.
- Removed the APT-specific SVG illustration from project content and updated older Responsible Breadth proof notes to point to this raster supersession.
- Updated `docs/templates/pattern-page.md` with the reusable architecture, including the inline exercise annotation contract.
- Added a regression test proving that the APT exercise links and raster image links resolve to real files.
- Added RB-T21/RB-T22 checker coverage for the pattern-page reader journey, exercise preview annotations, existing exercise targets, expanded raster `media_purpose` values, and condition anatomy-image safety boundaries.
- Split pattern-page preview image references from exercise-page sequence image references so provenance can distinguish `exercise_preview_illustration` from `key_movement_illustration`.

## Safety boundary

The page uses "commonly recommended self-management themes" and "education options" instead of a treatment plan or personal routine. Exercise annotations explain why an exercise maps to a movement contributor, but they do not tell a specific reader what they have, what caused it, or what program they should follow.

## Validation plan

- Run Responsible Breadth unit tests.
- Run the Markdown-first checker over `README.md`, `SOURCES.md`, `about`, `patterns`, `conditions`, `principles`, `programs`, and `exercises`.
- Run the privacy checker over changed content and media paths.
- Run `git diff --check`.
