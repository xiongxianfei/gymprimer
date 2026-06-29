# Manual Proof: Visual Media Review

- Owner role: media reviewer
- Files inspected: `media/movements/anterior-pelvic-tilt-comparison.png`, `media/movements/*-sequence.png`, pattern and exercise pages that reference them
- Exact steps:
  - Confirm every referenced PNG exists.
  - Confirm every visual has alt text through the Markdown image reference.
  - Confirm each visual is necessary for beginner comprehension.
  - Confirm assets have `media/PROVENANCE.md` rows because they are AI-generated raster assets.
- Pass/fail result: pass
- Failure notes: none. All referenced PNGs exist, have Markdown alt text, and have provenance rows. They are necessary because the updated APT page now routes readers into movement options where text-only descriptions would be weaker for beginners.
- Re-run trigger: Any media added to a pattern or exercise page.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
