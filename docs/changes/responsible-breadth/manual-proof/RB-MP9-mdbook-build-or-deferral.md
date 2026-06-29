# RB-MP9: mdBook Build or Deferral Proof

- Owner role: release/check maintainer
- Owning milestone: M4
- Automation rationale: mdBook is optional and derived; the proof must distinguish a real build from an explicit deferral.
- Files inspected: repository root, `README.md`, `docs/plans/2026-06-29-responsible-breadth.md`
- Exact steps:
  - Ran `command -v mdbook || true`.
  - Checked for `book.toml` and `SUMMARY.md`.
  - Confirmed Markdown remains canonical when mdBook is unavailable.
- Pass/fail result: pass
- Failure notes: `mdbook` is not installed and no `book.toml` or `SUMMARY.md` is configured, so no build is claimed.
- Re-run trigger: Any addition of `book.toml`, `SUMMARY.md`, generated HTML, mdBook workflow, or hosted documentation surface.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.
