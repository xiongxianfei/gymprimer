# RB-MP7: Visual Necessity and Media Review

- Owner role: media reviewer
- Owning milestone: M3/M4 when media exists
- Automation rationale: Visual necessity is semantic and cannot be fully automated.
- Files inspected: `patterns/anterior-pelvic-tilt.md`, `conditions/non-specific-chronic-low-back-pain.md`, `principles/how-many-days-a-week.md`, `programs/generic-3-day-full-body-example.md`
- Exact steps:
  - Inspect each first expanded proof-slice page for media references.
  - Confirm whether media exists.
  - If media exists, inspect necessity, alt text, adjacent explanation, and provenance.
- Pass/fail result: pass
- Failure notes: `patterns/anterior-pelvic-tilt.md` now uses one original SVG alignment comparison at `media/svg/patterns/anterior-pelvic-tilt-comparison.svg`. The visual is necessary because anterior pelvic tilt is an alignment pattern, includes alt text and adjacent explanation, and is an original SVG rather than a raster asset, so no `media/PROVENANCE.md` row is required.
- Re-run trigger: Any media added to a Responsible Breadth page.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
