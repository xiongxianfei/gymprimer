# RB-MP2: Pattern Source and Scope Review

- Owner role: content maintainer
- Owning milestone: M3
- Automation rationale: Automated checks can verify structure and citations, but source quality and non-diagnostic framing require manual review.
- Files inspected: `patterns/anterior-pelvic-tilt.md`, `SOURCES.md`, `specs/responsible-breadth.md`
- Exact steps:
  - Confirm the page frames anterior pelvic tilt as an observable pattern.
  - Confirm the page says it does not diagnose or prescribe individualized care.
  - Confirm the red-flags link appears before self-management themes.
  - Confirm sources are named and public, including institutional and peer-reviewed sources.
  - Confirm uncertainty language is present.
- Pass/fail result: pass
- Failure notes: none. Re-run after PR feedback found the expanded page now uses Mayo Clinic, MedlinePlus, PubMed-indexed Lederman 2011, PubMed-indexed Herrington 2011, NASM, and Physiopedia; it keeps the posture-pain link explicitly contested and avoids diagnosis, treatment, corrective-routine, and posture-promise framing.
- Re-run trigger: Any edit to `patterns/anterior-pelvic-tilt.md`, any replacement of its sources, or any reader report that it reads like diagnosis or correction promise.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
