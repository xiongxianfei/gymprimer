from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MP4 = (
    ROOT
    / "docs/changes/markdown-first-gym-primer/manual-proof/MP4-mdbook-build-or-deferral.md"
)
README = ROOT / "README.md"
FIRST_SLICE = (
    "01-getting-started/beginner-training-principles.md",
    "02-machines/lat-pulldown.md",
    "02-machines/seated-row.md",
    "02-machines/chest-press.md",
    "03-bodyweight/incline-push-up.md",
)


class MarkdownFirstMdBookTest(unittest.TestCase):
    def test_mdbook_is_either_configured_or_deferred(self) -> None:
        has_config = (ROOT / "book.toml").is_file() and (ROOT / "SUMMARY.md").is_file()
        has_deferral = MP4.is_file()

        self.assertTrue(has_config or has_deferral)

    def test_mdbook_deferral_keeps_markdown_canonical(self) -> None:
        if (ROOT / "book.toml").is_file():
            self.skipTest("mdBook config exists; deferral-specific check is not active")

        text = MP4.read_text(encoding="utf-8").lower()
        self.assertIn("deferred", text)
        self.assertIn("mdbook", text)
        self.assertIn("not installed", text)
        self.assertIn("markdown remains the source of truth", text)

    def test_readme_links_first_slice_without_mdbook(self) -> None:
        readme = README.read_text(encoding="utf-8")

        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertIn(f"]({relative_path})", readme)


if __name__ == "__main__":
    unittest.main()
