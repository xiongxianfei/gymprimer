# Responsible Breadth Manual Proof Scaffold

Manual proof records belong in this directory. They cover semantic judgments
that local checks cannot prove safely, including source quality, clinical-scope
boundaries, visual necessity, reader comprehension, validation ledger state,
and mdBook build-or-deferral evidence.

Each proof record must include:

- owner role;
- owning milestone;
- automation rationale;
- files inspected;
- exact steps;
- pass/fail result;
- failure notes when applicable;
- re-run trigger;
- privacy statement.

No identifying reader details, private health profiles, symptom histories,
contact details, local absolute paths, or secrets may be included.

## Required Records

| Proof ID | File | Owning milestone | Purpose |
| --- | --- | --- | --- |
| RB-MP1 | `RB-MP1-red-flags-review.md` | M2 | Confirm the red-flags reference routes to emergency, prompt, or professional care without diagnosis or triage. |
| RB-MP2 | `RB-MP2-pattern-source-scope.md` | M3 | Confirm pattern-page source quality, non-diagnostic language, uncertainty language, and professional routing. |
| RB-MP3 | `RB-MP3-condition-source-scope.md` | M3 | Confirm condition-page source quality, red-flag routing, uncertainty language, and no treatment plan. |
| RB-MP4 | `RB-MP4-principle-source-review.md` | M3 | Confirm programming-principle pages use cited general ranges without individualized adaptation. |
| RB-MP5 | `RB-MP5-program-boundary-review.md` | M3 | Confirm program examples are static illustrations and not personalized prescriptions. |
| RB-MP6 | `RB-MP6-comprehension-proof.md` | M3 | Record non-identifying reader comprehension evidence for purpose, boundary, stop/red-flag condition, and source-verification understanding. |
| RB-MP7 | `RB-MP7-visual-media-review.md` | M3/M4 when media exists | Confirm media is necessary, non-decorative, explained, and compliant with provenance rules; otherwise record a no-media note. |
| RB-MP8 | `RB-MP8-validation-ledger.md` | M4 | Confirm commands, manual proof, lifecycle state, and CI-claim boundaries are current. |
| RB-MP9 | `RB-MP9-mdbook-build-or-deferral.md` | M4 | Record real mdBook build evidence or an explicit deferral that keeps Markdown canonical. |

## Record Template

```md
# RB-MP<n>: <proof name>

- Owner role:
- Owning milestone:
- Automation rationale:
- Files inspected:
- Exact steps:
- Pass/fail result:
- Failure notes:
- Re-run trigger:
- Privacy statement: No identifying reader details, private health profiles,
  symptom histories, contact details, local absolute paths, or secrets are
  included.
```
