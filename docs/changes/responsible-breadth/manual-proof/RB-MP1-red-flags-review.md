# RB-MP1: Red-Flags Non-Triage Review

- Owner role: content maintainer
- Owning milestone: M2
- Automation rationale: Automated checks can confirm structure, citations, and privacy, but they cannot prove that reader-facing safety routing avoids triage or condition selection.
- Files inspected: `about/red-flags.md`, `SOURCES.md`, `specs/responsible-breadth.md`
- Exact steps:
  - Read `about/red-flags.md` top to bottom.
  - Confirm it routes to emergency care, prompt medical care, and professional assessment.
  - Confirm it does not tell the reader what condition they have.
  - Confirm it does not choose an exact care level for the reader.
  - Confirm each safety-routing statement has a page-local source link.
- Pass/fail result: pass
- Failure notes: none
- Re-run trigger: Any edit to `about/red-flags.md`, any source replacement affecting red-flag language, or any reader/contributor report that the page reads like diagnosis or triage.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
