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
    def test_templates_use_central_red_flags_and_avoid_disclaimer_scaffolding(self) -> None:
        for template in (ROOT / "docs/templates").glob("*.md"):
            text = template.read_text(encoding="utf-8")
            self.assertNotIn("about/red-flags.md", text, str(template))
            self.assertNotIn("Disclaimer:", text, str(template))

    def test_exercise_card_template_has_required_sections(self) -> None:
        template = ROOT / "docs/templates/exercise-card.md"
        self.assertTrue(template.exists(), "exercise-card.md template is missing")
        text = template.read_text(encoding="utf-8")

        for expected in (
            "Safety routing",
            "../RED-FLAGS.md",
            "Do not repeat the central disclaimer",
            "What this exercise is for",
            "Equipment setup",
            "Muscles involved",
            "role-based",
            "main driver",
            "What it helps do",
            "page-local source support",
            "Movement breakdown",
            "How much to do",
            "Method type:",
            "basic_cardio_activity",
            "Beginner starting point:",
            "Effort:",
            "time",
            "talk test",
            "Rest:",
            "repeatability",
            "Progression:",
            "Stop if:",
            "What you should feel",
            "you may feel",
            "pay attention to",
            "Common mistakes",
            "Easier version",
            "Harder version",
            "Optional exercise image",
            "setup, movement, or muscle attention",
            "Keep explanation, cues, safety notes, and citations in Markdown",
            "Do not add image labels, warning badges, pain marks, or diagnosis/treatment claims",
            "Safety notes",
            "Sources",
        ):
            self.assertIn(expected, text)

    def test_exercise_image_review_evidence_templates_exist(self) -> None:
        evidence_root = ROOT / "docs/changes/exercise-image-standard-and-optimization/evidence"
        visual = evidence_root / "visual-safety-review-template.md"
        comprehension = evidence_root / "beginner-comprehension-template.md"

        self.assertTrue(visual.exists(), "visual-safety review template is missing")
        self.assertTrue(comprehension.exists(), "beginner comprehension template is missing")

        visual_text = visual.read_text(encoding="utf-8")
        for expected in (
            "Image teaches one concept",
            "Matches nearby Markdown",
            "No in-image text",
            "No identifying person",
            "Avoids clinical framing",
            "Avoids unsupported claims",
            "Color is not the only communication method",
            "Residual risk",
        ):
            self.assertIn(expected, visual_text)

        comprehension_text = comprehension.read_text(encoding="utf-8")
        for expected in (
            "Purpose",
            "Setup or body position",
            "Movement steps",
            "What to notice or feel",
            "Stop condition",
            "Source verification",
            "Residual confusion",
            "No private health information",
        ):
            self.assertIn(expected, comprehension_text)

    def test_principle_page_template_has_required_sections(self) -> None:
        template = ROOT / "docs/templates/principle-page.md"
        self.assertTrue(template.exists(), "principle-page.md template is missing")
        text = template.read_text(encoding="utf-8")

        for expected in (
            "Safety routing",
            "../RED-FLAGS.md",
            "Do not repeat the central disclaimer",
            "Beginner explanation",
            "Scope boundaries",
            "Safety notes",
            "Sources",
        ):
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
