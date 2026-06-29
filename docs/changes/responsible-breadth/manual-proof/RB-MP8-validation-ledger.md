# RB-MP8: Final Validation Ledger and Lifecycle Sync

- Owner role: release/check maintainer
- Owning milestone: M4
- Automation rationale: Automated commands prove selected checks pass, but final lifecycle coherence and CI-claim boundaries require a manual ledger.
- Files inspected: `README.md`, `SOURCES.md`, `CONTRIBUTING.md`, `about/`, `patterns/`, `conditions/`, `principles/`, `programs/`, `docs/changes/responsible-breadth/`, `docs/plans/2026-06-29-responsible-breadth.md`, `docs/plan.md`
- Exact steps:
  - Confirm proposal is accepted, spec is approved, architecture is approved, ADR is accepted, plan is active, and review-resolution is closed.
  - Confirm M1, M2, and M3 code-review records are clean and recorded.
  - Confirm M4 promotion links only the five Responsible Breadth proof-slice pages and red-flags reference.
  - Run the M4 validation commands and record results in the plan.
  - Confirm no CI pass is claimed.
- Pass/fail result: pass
- Failure notes: none
- Re-run trigger: Any edit to promoted navigation, first-slice pages, manual proof records, validation commands, or lifecycle routing.
- Privacy statement: No identifying reader details, private health profiles, symptom histories, contact details, local absolute paths, or secrets are included.

## Command Ledger

| Command | Result |
| --- | --- |
| `python3 -m unittest discover -s tests -p 'test_responsible_breadth_*.py'` | Passed: 15 tests. |
| `python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'` | Passed: 51 tests. |
| `python3 tools/checks/check_markdown_first.py README.md SOURCES.md about patterns conditions principles programs` | Passed: checked 7 Markdown files. |
| `python3 tools/checks/check_privacy.py README.md SOURCES.md CONTRIBUTING.md about patterns conditions principles programs docs/changes/responsible-breadth media` | Passed: checked 51 files. |
| `command -v mdbook \|\| true` | Ran with exit 0 and no path output; mdBook is unavailable in this environment. |
