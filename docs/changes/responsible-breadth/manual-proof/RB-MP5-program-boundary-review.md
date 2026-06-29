# RB-MP5: Program-Example Boundary Review

- Owner role: content maintainer
- Owning milestone: M3
- Automation rationale: Automated checks can reject some forbidden phrases, but the illustration-versus-prescription boundary requires manual review.
- Files inspected: `programs/generic-3-day-full-body-example.md`, `SOURCES.md`, `specs/responsible-breadth.md`
- Exact steps:
  - Confirm the page is a static worked example.
  - Confirm it does not route the reader into a plan.
  - Confirm it does not adapt to symptoms, goals, equipment, medical history, or training response.
  - Confirm scope boundaries exclude pain, injury, medical context, return-to-training decisions, and individualized loading.
- Pass/fail result: pass
- Failure notes: none
- Re-run trigger: Any edit to `programs/generic-3-day-full-body-example.md` or any reader report that the example reads like a personal prescription.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
