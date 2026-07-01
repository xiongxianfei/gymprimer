from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
VERIFY_REPORT = ROOT / "docs/changes/markdown-first-gym-primer/verify-report.md"


class MarkdownFirstCompatibilityTest(unittest.TestCase):
    def test_generated_book_output_is_not_source_of_truth(self) -> None:
        readme = README.read_text(encoding="utf-8").lower()
        report = VERIFY_REPORT.read_text(encoding="utf-8").lower()

        self.assertIn("markdown remains the source of truth", readme)
        self.assertIn("markdown remains canonical", report)

    def test_no_mdbook_summary_when_mdbook_is_deferred(self) -> None:
        if (ROOT / "book.toml").is_file():
            self.skipTest("mdBook config exists; deferral-specific check is not active")

        self.assertFalse((ROOT / "SUMMARY.md").exists())
        self.assertFalse((ROOT / "book").exists())


if __name__ == "__main__":
    unittest.main()
