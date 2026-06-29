from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class MarkdownFirstContractTest(unittest.TestCase):
    def test_readme_routes_to_markdown_first_source_of_truth(self) -> None:
        text = read_text("README.md")

        for expected in (
            "Markdown-first",
            "source of truth",
            "SOURCES.md",
            "CONTRIBUTING.md",
            "CONTENT_LICENSE.md",
            "01-getting-started/",
            "02-machines/",
            "03-bodyweight/",
        ):
            self.assertIn(expected, text)

        stale_product_claims = (
            "Future UI or search layers should consume generated public content",
            "Validate repository content and emit deterministic public output",
            "The generated public package is",
        )
        for stale_claim in stale_product_claims:
            self.assertNotIn(stale_claim, text)

    def test_contributor_and_license_terms_are_explicit(self) -> None:
        combined = "\n".join(
            [
                read_text("CONTRIBUTING.md"),
                read_text("CONTENT_LICENSE.md"),
            ]
        )

        for expected in (
            "Apache-2.0",
            "CC BY 4.0",
            "right to submit",
            "third-party media",
            "claim-level",
            "not medical advice",
            "not personalized coaching",
        ):
            self.assertIn(expected, combined)

    def test_source_index_exists_and_describes_reuse(self) -> None:
        text = read_text("SOURCES.md")

        self.assertIn("Global Source Index", text)
        self.assertIn("reused across more than one page", text)
        self.assertIn("claim-level", text)


if __name__ == "__main__":
    unittest.main()
