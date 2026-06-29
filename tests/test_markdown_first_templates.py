from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def headings(relative_path: str) -> set[str]:
    text = (ROOT / relative_path).read_text(encoding="utf-8")
    return {
        line.lstrip("# ").strip()
        for line in text.splitlines()
        if line.startswith("#")
    }


class MarkdownFirstTemplateTest(unittest.TestCase):
    def test_exercise_card_template_has_required_sections(self) -> None:
        template = ROOT / "docs/templates/exercise-card.md"
        self.assertTrue(template.exists(), "exercise-card.md template is missing")
        text = template.read_text(encoding="utf-8")

        for expected in (
            "Disclaimer",
            "not medical advice",
            "not personalized coaching",
            "What this exercise is for",
            "Equipment setup",
            "Muscles involved",
            "Movement breakdown",
            "What you should feel",
            "Common mistakes",
            "Easier version",
            "Harder version",
            "Safety notes",
            "Sources",
        ):
            self.assertIn(expected, text)

    def test_principle_page_template_has_required_sections(self) -> None:
        template = ROOT / "docs/templates/principle-page.md"
        self.assertTrue(template.exists(), "principle-page.md template is missing")
        text = template.read_text(encoding="utf-8")

        for expected in (
            "Disclaimer",
            "not medical advice",
            "not personalized coaching",
            "Beginner explanation",
            "Scope boundaries",
            "Safety notes",
            "Sources",
        ):
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
