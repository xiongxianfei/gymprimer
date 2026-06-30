from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERIFY_REPORT = ROOT / "docs/changes/markdown-first-gym-primer/verify-report.md"


class MarkdownFirstObservabilityTest(unittest.TestCase):
    def test_final_validation_ledger_records_required_commands(self) -> None:
        text = VERIFY_REPORT.read_text(encoding="utf-8")

        required_fragments = (
            "if command -v mdbook >/dev/null 2>&1; then mdbook build; else printf",
            "python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'",
            "python3 tools/checks/check_markdown_first.py",
            "python3 tools/checks/check_privacy.py",
            "git diff --check",
        )

        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, text)

    def test_final_validation_ledger_does_not_claim_ci(self) -> None:
        text = VERIFY_REPORT.read_text(encoding="utf-8").lower()

        self.assertIn("ci was not run", text)
        self.assertNotIn("ci passed", text)


if __name__ == "__main__":
    unittest.main()
