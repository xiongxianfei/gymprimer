# Contributing

Thanks for contributing.

GymPrimer is a Markdown-first, citation-based beginner primer. The repository Markdown files are the product source of truth; generated output and old structured-platform artifacts are not active v0.1 guidance.

## Pull requests

- Keep changes focused and reviewable.
- Explain why the change is needed.
- Include tests, structural checks, or manual proof when behavior, content contracts, or safety wording changes.
- Run relevant checks and mention the commands in the pull request.
- Do not describe draft pages as published, approved, expert-reviewed, or active source content before the reviewed milestone promotes them.

## Content scope

v0.1 accepts beginner training principles, common machine exercises, low-risk bodyweight progressions, simple dumbbell patterns, and basic cardio equipment.

Do not add barbell lifts, Olympic lifting, kettlebell ballistic lifts, plyometrics, sprint programming, sport-specific programming, injury-specific advice, posture-correction protocols, pain treatment, diagnosis, or rehabilitation pathways.

## Safety and citations

Every safety-relevant page needs a prominent disclaimer stating that GymPrimer is educational content, not medical advice and not personalized coaching.

Safety warnings require claim-level citations to public, named sources. A global source in `SOURCES.md` is not enough for a safety claim; readers must be able to verify the claim from the page they are reading.

Use page-local `Sources` sections and reference-style links for v0.1 citations. Add reused sources to `SOURCES.md` when the same source supports more than one page.

## Media

Images are optional in v0.1. Use them only when they materially help a beginner
identify equipment or understand a key movement position.

Preferred order:

1. No image when the page is clear without one.
2. Original SVG diagram under `media/`.
3. AI-generated raster illustration under `media/` with an approved row in
   `media/PROVENANCE.md`.

Do not submit undocumented third-party media, stock photos, borrowed public web
images, screenshots of commercial gym machines, decorative images, medical
illustrations, rehab illustrations, identifying people, or local private file
paths.

Every media reference must use a relative repository path and include alt text or nearby explanatory text.

### Image examples

Equipment identification example:

![Lat pulldown machine example](./media/equipment/lat-pulldown-machine-example.png)

This kind of image helps a beginner recognize the machine. It should not
replace setup instructions, safety notes, or sources.

Key movement illustration example:

![Incline push-up start and finish example](./media/movements/incline-push-up-phases-example.png)

This kind of image can show important movement positions. It should not add
advanced coaching, diagnosis, rehab guidance, or safety claims that are absent
from the Markdown page.

## Privacy

Do not include secrets, credentials, private contact details, local machine paths, private health information, real user health profiles, or identifying beginner read-test notes.

## License and contribution terms

By submitting a pull request, you agree that:

- code and tooling contributions are provided under Apache-2.0;
- written content, templates, original diagrams, and educational materials are provided under CC BY 4.0;
- you have the right to submit the contributed material;
- you are not submitting copyrighted third-party media unless its license is documented and compatible with the project;
- source wording, citations, and safety language may be edited by maintainers to keep the Markdown-first contract consistent.

## Issues

Use issues for bug reports, feature requests, and project questions. Include enough context for maintainers to reproduce or evaluate the request.
