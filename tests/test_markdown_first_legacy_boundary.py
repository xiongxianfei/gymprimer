from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class MarkdownFirstLegacyBoundaryTest(unittest.TestCase):
    def test_old_platform_surfaces_are_marked_superseded(self) -> None:
        for relative_path in (
            "docs/plans/2026-06-26-content-schema-foundation.md",
            "docs/adr/2026-06-26-repository-native-reviewed-content.md",
            "content/README.md",
            "schemas/README.md",
            "generated/README.md",
            "tools/validation/README.md",
        ):
            text = (ROOT / relative_path).read_text(encoding="utf-8").lower()
            with self.subTest(path=relative_path):
                self.assertIn("superseded", text)
                self.assertIn("markdown-first", text)

    def test_readme_does_not_route_to_old_generated_json_product(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertNotIn("generated/public-content.json", text)
        self.assertNotIn("content-schema foundation", text.lower())


if __name__ == "__main__":
    unittest.main()
