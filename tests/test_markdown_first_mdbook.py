from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERIFY_REPORT = ROOT / "docs/changes/markdown-first-gym-primer/verify-report.md"
README = ROOT / "README.md"
FIRST_SLICE = (
    "principles/beginner-training-principles.md",
    "exercises/lat-pulldown.md",
    "exercises/seated-row.md",
    "exercises/chest-press.md",
    "exercises/incline-push-up.md",
)


class MarkdownFirstMdBookTest(unittest.TestCase):
    def test_mdbook_is_either_configured_or_deferred(self) -> None:
        has_config = (ROOT / "book.toml").is_file() and (ROOT / "SUMMARY.md").is_file()
        has_deferral = VERIFY_REPORT.is_file()

        self.assertTrue(has_config or has_deferral)

    def test_mdbook_deferral_keeps_markdown_canonical(self) -> None:
        if (ROOT / "book.toml").is_file():
            self.skipTest("mdBook config exists; deferral-specific check is not active")

        text = VERIFY_REPORT.read_text(encoding="utf-8").lower()
        self.assertIn("deferred", text)
        self.assertIn("mdbook", text)
        self.assertIn("not installed", text)
        self.assertIn("markdown remains canonical", text)

    def test_readme_links_first_slice_without_mdbook(self) -> None:
        readme = README.read_text(encoding="utf-8")

        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertIn(f"]({relative_path})", readme)


if __name__ == "__main__":
    unittest.main()
