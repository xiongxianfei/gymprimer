from pathlib import Path
import subprocess
import sys
import unittest

from tools.checks.check_markdown_first import (
    load_media_provenance,
    section_text,
    split_page_refs,
    validate_exercise_muscle_guidance,
)


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIRST_SLICE = (
    "principles/beginner-training-principles.md",
    "exercises/lat-pulldown.md",
    "exercises/seated-row.md",
    "exercises/chest-press.md",
    "exercises/incline-push-up.md",
)
ROWING_MACHINE_PAGE = ROOT / "exercises/rowing-machine.md"
MUSCLE_GUIDANCE_PROOF_SLICE = {
    "cardio equipment": {
        "path": "exercises/rowing-machine.md",
        "table": "| Phase | Muscle region | What it helps do |",
        "terms": ("Drive", "Transfer", "Finish", "Recovery"),
    },
    "machine or resistance": {
        "path": "exercises/chest-press.md",
        "table": "| Role | Muscle region | What it helps do |",
        "terms": ("Main driver", "Support", "Stabilizer"),
    },
    "hold or trunk": {
        "path": "exercises/plank.md",
        "table": "| Role | Muscle region | What it helps do |",
        "terms": ("Main control", "Support", "Stabilizer"),
    },
    "low-load control": {
        "path": "exercises/chin-nod.md",
        "table": "",
        "terms": ("Control focus", "Posture support"),
    },
    "mobility or stretch": {
        "path": "exercises/thoracic-extension.md",
        "table": "",
        "terms": ("Mobility focus", "Support"),
    },
    "band or shoulder control": {
        "path": "exercises/band-pull-apart.md",
        "table": "| Role | Muscle region | What it helps do |",
        "terms": ("Main driver", "Support", "Posture / control"),
    },
}
LEGACY_MUSCLE_GUIDANCE_PAGES_OUTSIDE_M2 = (
    "exercises/dead-bug.md",
    "exercises/bird-dog.md",
    "exercises/glute-bridge.md",
    "exercises/hip-hinge.md",
    "exercises/kneeling-hip-flexor-stretch.md",
)
ROWING_REQUIRED_SECTIONS = (
    "## What this is for",
    "## Before you start",
    "## Equipment setup",
    "## Muscles involved",
    "## Movement breakdown",
    "## What you should feel",
    "## Common mistakes",
    "## How much to do",
    "## Easier version",
    "## Harder version",
    "## Safety notes",
    "## Sources",
)


class MarkdownFirstRealPagesTest(unittest.TestCase):
    def test_first_slice_pages_exist(self) -> None:
        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_first_slice_pages_pass_checker(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "README.md",
                "SOURCES.md",
                "RED-FLAGS.md",
                "principles",
                "exercises",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_readme_links_first_slice_pages(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for relative_path in FIRST_SLICE:
            with self.subTest(path=relative_path):
                self.assertIn(f"]({relative_path})", readme)

    def test_muscle_guidance_proof_slice_covers_required_categories(self) -> None:
        self.assertEqual(
            set(MUSCLE_GUIDANCE_PROOF_SLICE),
            {
                "cardio equipment",
                "machine or resistance",
                "hold or trunk",
                "low-load control",
                "mobility or stretch",
                "band or shoulder control",
            },
        )
        for category, expected in MUSCLE_GUIDANCE_PROOF_SLICE.items():
            with self.subTest(category=category):
                path = ROOT / expected["path"]
                text = path.read_text(encoding="utf-8")
                muscle_section = section_text(text, "## Muscles involved")
                feel_section = section_text(text, "## What you should feel")
                finding_codes = [
                    finding.code for finding in validate_exercise_muscle_guidance(path, text)
                ]

                self.assertTrue(path.is_file())
                self.assertIn("## Muscles involved", text)
                self.assertNotIn("## Used muscles", text)
                self.assertIn("## What you should feel", text)
                self.assertEqual(finding_codes, [])
                self.assertTrue(muscle_section)
                self.assertTrue(feel_section)
                if expected["table"]:
                    self.assertIn(expected["table"], muscle_section)
                for term in expected["terms"]:
                    self.assertIn(term, muscle_section)
                self.assertRegex(feel_section.lower(), r"\b(you may feel|pay attention to|try to keep)\b")
                self.assertRegex(muscle_section, r"\]\[[a-z0-9-]+\]")

    def test_unselected_legacy_used_muscles_pages_remain_compatible(self) -> None:
        for relative_path in LEGACY_MUSCLE_GUIDANCE_PAGES_OUTSIDE_M2:
            with self.subTest(path=relative_path):
                path = ROOT / relative_path
                text = path.read_text(encoding="utf-8")
                finding_codes = [
                    finding.code for finding in validate_exercise_muscle_guidance(path, text)
                ]

                self.assertIn("## Used muscles", text)
                self.assertNotIn("## What you should feel", text)
                self.assertNotIn("exercise_muscle_legacy_heading_migrated", finding_codes)
                self.assertEqual(finding_codes, [])

    def rowing_text(self) -> str:
        return ROWING_MACHINE_PAGE.read_text(encoding="utf-8")

    def test_rowing_machine_page_has_required_shape(self) -> None:
        self.assertTrue(ROWING_MACHINE_PAGE.is_file())
        text = self.rowing_text()

        for section in ROWING_REQUIRED_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, text)

        forbidden_runtime_terms = (
            "JavaScript",
            "database",
            "user account",
            "tracking flow",
            "local server",
            "workout tracker",
            "calculator",
            "user input",
        )
        for term in forbidden_runtime_terms:
            with self.subTest(term=term):
                self.assertNotIn(term, text)

    def test_rowing_machine_stroke_sequence_setup_and_method(self) -> None:
        text = self.rowing_text().lower()
        compact = " ".join(text.split())

        for term in ("catch", "drive", "finish", "recovery"):
            with self.subTest(term=term):
                self.assertIn(term, text)

        self.assertIn("drive: legs -> body -> arms", text)
        self.assertIn("recovery: arms -> body -> legs", text)
        self.assertIn("foot strap", text)
        self.assertIn("ball or widest part", text)
        self.assertIn("shins approach vertical only as far as comfortable", compact)
        self.assertIn("damper changes the feel", text)
        self.assertIn("you create the work with your stroke effort", compact)
        self.assertIn("method type: basic_cardio_equipment", text)
        self.assertIn("beginner starting point:", text)
        self.assertIn("effort:", text)
        self.assertIn("rest/reset:", text)
        self.assertIn("progression:", text)
        self.assertIn("stop condition:", text)
        self.assertIn("3-5 minutes", text)
        self.assertIn("technique first, then time, then moderate effort", text)

    def test_rowing_machine_media_is_local_prompt_backed_and_reviewed(self) -> None:
        text = self.rowing_text()
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected = {
            "media/exercises/rowing-machine/setup.png": (
                "exercise_setup_illustration",
                "Rowing machine setup reference with foot strap, seat, handle, and catch position",
            ),
            "media/exercises/rowing-machine/movement.png": (
                "exercise_movement_illustration",
                "Rowing machine stroke sequence reference showing catch, drive, finish, and recovery",
            ),
            "media/exercises/rowing-machine/muscle-attention.png": (
                "exercise_muscle_attention_illustration",
                "Rowing machine muscle attention reference with broad highlights on legs, glutes, trunk, upper back, lats, and arms",
            ),
        }

        for asset_path, (purpose, alt_text) in expected.items():
            with self.subTest(asset_path=asset_path):
                self.assertIn(f"![{alt_text}](../{asset_path})", text)
                self.assertTrue((ROOT / asset_path).is_file())

                rows = provenance.get(asset_path, [])
                self.assertEqual(len(rows), 1)
                row = rows[0]
                self.assertEqual(row.get("asset_type"), "ai_generated_raster")
                self.assertEqual(row.get("media_purpose"), purpose)
                self.assertEqual(row.get("review_status"), "approved")
                self.assertIn("exercises/rowing-machine.md", split_page_refs(row.get("page_refs", "")))

                prompt_record = row.get("prompt_record", "")
                self.assertEqual(prompt_record, f"media/prompts/exercises/rowing-machine/{Path(asset_path).stem}.md")
                self.assertTrue((ROOT / prompt_record).is_file())

    def test_seated_row_muscle_attention_image_is_local_prompt_backed_and_reviewed(self) -> None:
        path = ROOT / "exercises/seated-row.md"
        text = path.read_text(encoding="utf-8")
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        asset_path = "media/exercises/seated-row/muscle-attention.png"
        alt_text = (
            "Seated row muscle-attention reference with broad highlights on the upper back, arms, grip, and trunk posture area"
        )

        self.assertIn(f"![{alt_text}](../{asset_path})", text)
        self.assertIn("| Role | Muscle region | What it helps do |", text)
        self.assertIn("Use the muscle-attention image only as a broad region reference.", text)
        self.assertTrue((ROOT / asset_path).is_file())

        rows = provenance.get(asset_path, [])
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row.get("asset_type"), "ai_generated_raster")
        self.assertEqual(row.get("media_purpose"), "exercise_muscle_attention_illustration")
        self.assertEqual(row.get("review_status"), "approved")
        self.assertIn("exercises/seated-row.md", split_page_refs(row.get("page_refs", "")))

        prompt_record = row.get("prompt_record", "")
        self.assertEqual(prompt_record, "media/prompts/exercises/seated-row/muscle-attention.md")
        self.assertTrue((ROOT / prompt_record).is_file())

    def test_rowing_machine_safety_sources_and_forbidden_scope(self) -> None:
        text = self.rowing_text()
        lower = text.lower()

        self.assertIn("../RED-FLAGS.md", text)
        for term in (
            "chest pain",
            "dizziness",
            "fainting",
            "unusual shortness of breath",
            "sharp pain",
            "numbness",
            "symptoms that worsen",
            "painful",
            "jerky or uncontrolled",
        ):
            with self.subTest(term=term):
                self.assertIn(term, lower)

        for term in (
            "all-out",
            "maximal damper",
            "2k test",
            "multi-week",
            "weight-loss",
            "heart-rate zone",
            "personalized conditioning plan",
            "diagnosis",
            "rehabilitation",
            "return-to-training",
        ):
            with self.subTest(term=term):
                self.assertNotIn(term, lower)

        for source_id in (
            "concept2-rowing-technique",
            "concept2-foot-position",
            "concept2-damper-setting",
            "concept2-getting-started-workouts",
            "cdc-adult-activity",
            "who-physical-activity",
            "local-rowing-machine-safety",
            "local-rowing-machine-exercise-pain",
            "nhs-back-pain",
            "mayo-weight-training",
        ):
            with self.subTest(source_id=source_id):
                self.assertIn(f"[{source_id}]:", text)
                self.assertIn(f"][{source_id}]", text)


if __name__ == "__main__":
    unittest.main()
