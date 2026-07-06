from pathlib import Path
import subprocess
import sys
import unittest

from tools.checks.check_markdown_first import (
    load_media_provenance,
    section_text,
    split_page_refs,
    validate_exercise_method_guidance,
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
BRISK_WALKING_PAGE = ROOT / "exercises/brisk-walking.md"
EVERYDAY_WALKING_PAGE = ROOT / "principles/everyday-walking.md"
TAI_CHI_PAGE = ROOT / "exercises/tai-chi-basics.md"
WALKING_CHANGE_ROOT = ROOT / "docs/changes/2026-07-05-brisk-walking-and-everyday-walking"
WALKING_MANUAL_PROOF_ROOT = WALKING_CHANGE_ROOT / "manual-proof"
WALKING_VALIDATION_LEDGER = WALKING_CHANGE_ROOT / "validation-ledger.md"
TAI_CHI_CHANGE_ROOT = ROOT / "docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise"
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
BRISK_WALKING_REQUIRED_SECTIONS = (
    "## What this is for",
    "## Before you start",
    "## How to know the pace is brisk",
    "## Muscles involved",
    "## Walking technique",
    "## What you should feel",
    "## Common mistakes",
    "## How much to do",
    "## Easier version",
    "## Harder version",
    "## Safety notes",
    "## Sources",
)
EVERYDAY_WALKING_REQUIRED_SECTIONS = (
    "## What this page is",
    "## What this page is not",
    "## Plain-language overview",
    "## Everyday walking vs. brisk walking",
    "## Ways to add more walking",
    "## How much counts",
    "## What to pay attention to",
    "## Common mistakes",
    "## Safety notes",
    "## Sources",
)
TAI_CHI_REQUIRED_SECTIONS = (
    "## What this is for",
    "## Before you start",
    "## Setup",
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

    def brisk_walking_text(self) -> str:
        return BRISK_WALKING_PAGE.read_text(encoding="utf-8")

    def everyday_walking_text(self) -> str:
        return EVERYDAY_WALKING_PAGE.read_text(encoding="utf-8")

    def tai_chi_text(self) -> str:
        return TAI_CHI_PAGE.read_text(encoding="utf-8")

    def test_walking_pages_exist_and_have_required_shape(self) -> None:
        expected = {
            BRISK_WALKING_PAGE: BRISK_WALKING_REQUIRED_SECTIONS,
            EVERYDAY_WALKING_PAGE: EVERYDAY_WALKING_REQUIRED_SECTIONS,
        }

        for path, sections in expected.items():
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                self.assertIn("Disclaimer: GymPrimer is educational content", text)
                for section in sections:
                    self.assertIn(section, text)

    def test_tai_chi_page_exists_and_has_required_shape(self) -> None:
        self.assertTrue(TAI_CHI_PAGE.is_file())
        text = self.tai_chi_text()

        self.assertTrue(text.startswith("# Tai Chi Basics\n"))
        self.assertIn("Disclaimer: GymPrimer is educational content", text)
        for section in TAI_CHI_REQUIRED_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, text)
        for step in (
            "### 1. Ready stance",
            "### 2. Weight shift",
            "### 3. Opening movement",
            "### 4. Return to quiet standing",
        ):
            with self.subTest(step=step):
                self.assertIn(step, text)

    def test_tai_chi_beginner_scope_and_forbidden_product_language(self) -> None:
        text = self.tai_chi_text()
        lower = text.lower()
        compact = " ".join(lower.split())

        for term in (
            "low-impact mindful movement",
            "coordination",
            "relaxed posture",
            "breathing",
            "movement literacy",
            "ready stance",
            "weight shift",
            "opening movement",
            "return to quiet standing",
        ):
            with self.subTest(term=term):
                self.assertIn(term, lower)

        for term in (
            "martial application",
            "combat application",
            "competition form",
            "lineage",
            "long form",
            "fall-prevention program",
            "recovery plan",
            "treatment protocol",
            "individualized balance program",
            "adaptive coaching",
            "hosted app",
            "cms",
            "database",
            "user account",
            "user-input flow",
            "generated public json",
            "video-first",
            "generated exercise guidance as source of truth",
            "cures pain",
            "fixes posture",
            "replaces medical care",
            "guarantees",
        ):
            with self.subTest(term=term):
                self.assertNotIn(term, compact)

    def test_tai_chi_setup_safety_sources_and_source_index(self) -> None:
        text = self.tai_chi_text()
        lower = text.lower()
        sources = (ROOT / "SOURCES.md").read_text(encoding="utf-8")

        for term in (
            "clear, flat surface",
            "non-slip",
            "small, slow movements",
            "wall or stable chair",
            "balance is uncertain",
            "dizziness",
            "chest pain",
            "fainting",
            "unusual shortness of breath",
            "sharp pain",
            "worsening symptoms",
            "loss of balance control",
            "medical condition",
            "medication",
            "injury history",
            "../red-flags.md",
        ):
            with self.subTest(term=term):
                self.assertIn(term, lower)

        for source_id in (
            "nccih-tai-chi",
            "harvard-tai-chi",
            "va-tai-chi-qigong",
            "nhs-balance-exercises",
            "local-tai-chi-basics-red-flags",
        ):
            with self.subTest(source_id=source_id):
                self.assertIn(f"[{source_id}]:", text)
                self.assertIn(f"][{source_id}]", text)
                if not source_id.startswith("local-"):
                    self.assertIn(f"[{source_id}]:", sources)

    def test_tai_chi_low_load_method_guidance(self) -> None:
        text = self.tai_chi_text()
        lower = text.lower()
        finding_codes = [
            finding.code for finding in validate_exercise_method_guidance(TAI_CHI_PAGE, text)
        ]

        self.assertEqual(finding_codes, [])
        self.assertIn("method type: low_load_control_drill", lower)
        self.assertIn("beginner starting point:", lower)
        self.assertIn("3-5 minutes", lower)
        self.assertIn("effort:", lower)
        self.assertIn("rest:", lower)
        self.assertIn("progression:", lower)
        self.assertIn("first make the movement smoother", lower)
        self.assertIn("then practice for a little longer", lower)
        self.assertIn("do not make the movement bigger, deeper, faster, or more complex", lower)
        self.assertIn("stop if:", lower)
        self.assertNotIn("based on your", lower)

    def test_tai_chi_broad_muscle_and_feel_guidance(self) -> None:
        text = self.tai_chi_text()
        muscle_section = section_text(text, "## Muscles involved")
        feel_section = section_text(text, "## What you should feel")
        finding_codes = [
            finding.code for finding in validate_exercise_muscle_guidance(TAI_CHI_PAGE, text)
        ]

        self.assertEqual(finding_codes, [])
        self.assertIn("| Role | Muscle region | What it helps do |", muscle_section)
        for term in (
            "Support and weight shift",
            "Posture and balance",
            "Relaxed arm motion",
            "Foot control",
            "Legs and glutes",
            "Trunk",
            "Shoulders and upper back",
            "Feet and ankles",
        ):
            with self.subTest(term=term):
                self.assertIn(term, muscle_section)
        self.assertRegex(feel_section.lower(), r"\b(you may feel|pay attention to|try to keep)\b")
        self.assertNotIn("activation", muscle_section.lower())

    def test_tai_chi_m2_source_audit_records_required_claim_samples(self) -> None:
        path = TAI_CHI_CHANGE_ROOT / "source-audit.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for heading in (
            "# Tai Chi Source Audit",
            "## Scope",
            "## Claim Samples",
            "## Disposition",
            "## Residual Risk",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

        for claim_type in (
            "setup",
            "safety",
            "method",
            "movement",
            "muscle",
            "feel",
            "stop-condition",
        ):
            with self.subTest(claim_type=claim_type):
                self.assertIn(claim_type, text)

        for token in ("page_path", "claim_type", "supporting_source", "source_fit", "outcome", "residual_risk"):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_tai_chi_m4_beginner_comprehension_records_required_prompts(self) -> None:
        path = TAI_CHI_CHANGE_ROOT / "beginner-comprehension-proof.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for prompt in (
            "Tai Chi purpose",
            "ready stance",
            "weight shift",
            "body feel",
            "pause/stop conditions",
            "images helped more than text alone",
            "non-identifying",
            "residual confusion",
            "exercises/tai-chi-basics.md",
            "media/exercises/tai-chi-basics/setup.png",
            "media/exercises/tai-chi-basics/weight-shift.png",
            "media/exercises/tai-chi-basics/muscle-attention.png",
        ):
            with self.subTest(prompt=prompt):
                self.assertIn(prompt, text)

    def test_tai_chi_m4_rollback_proof_records_text_only_cleanup(self) -> None:
        path = TAI_CHI_CHANGE_ROOT / "rollback-proof.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for token in (
            "text-only",
            "temporary review state",
            "remove image references",
            "unused Tai Chi assets",
            "prompt records",
            "provenance rows",
            "exercises/tai-chi-basics.md",
            "media/exercises/tai-chi-basics/setup.png",
            "media/exercises/tai-chi-basics/weight-shift.png",
            "media/exercises/tai-chi-basics/muscle-attention.png",
            "media/prompts/exercises/tai-chi-basics/setup.md",
            "media/prompts/exercises/tai-chi-basics/weight-shift.md",
            "media/prompts/exercises/tai-chi-basics/muscle-attention.md",
            "python3 tools/checks/check_markdown_first.py",
            "python3 tools/checks/check_privacy.py",
            "pass",
        ):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_brisk_walking_page_contract(self) -> None:
        text = self.brisk_walking_text()
        lower = text.lower()
        compact = " ".join(lower.split())

        self.assertIn("deliberate moderate-intensity cardio activity", lower)
        self.assertIn("everyday walking", lower)
        self.assertIn("talk, but not comfortably sing", lower)
        self.assertIn("2.5 mph or faster", lower)
        self.assertIn("method type: basic_cardio_activity", lower)
        self.assertIn("beginner starting point:", lower)
        self.assertIn("5-10 minutes", lower)
        self.assertIn("effort:", lower)
        self.assertIn("progression:", lower)
        self.assertIn("first add total minutes", lower)
        self.assertIn("then add more brisk minutes", lower)
        self.assertIn("then add hills or faster sections", compact)
        self.assertIn("stop if:", lower)
        self.assertIn("sets and reps", lower)
        self.assertIn("not a schedule", lower)
        self.assertIn("look forward", lower)
        self.assertIn("neck and shoulders relaxed", lower)
        self.assertIn("natural arm swing", lower)
        self.assertIn("relaxed hands", lower)
        self.assertIn("stay tall", lower)
        self.assertIn("heel to toe", lower)
        self.assertIn("easy start", lower)
        self.assertIn("easy finish", lower)
        self.assertIn("not a personal walking plan", compact)

    def test_everyday_walking_page_contract(self) -> None:
        text = self.everyday_walking_text()
        lower = text.lower()

        self.assertIn("daily movement", lower)
        self.assertIn("sitting interruption", lower)
        self.assertIn("habit-building", lower)
        self.assertIn("not every step is brisk cardio", lower)
        self.assertIn("brisk walking is the version", lower)
        self.assertIn("errands", lower)
        self.assertIn("commuting", lower)
        self.assertIn("walking breaks", lower)
        self.assertIn("parking farther away", lower)
        self.assertIn("../exercises/brisk-walking.md", text)
        self.assertNotIn("method type:", lower)
        self.assertNotIn("## Muscles involved", text)

    def test_walking_pages_safety_sources_forbidden_scope_and_everyday_text_only_media(self) -> None:
        for path in (BRISK_WALKING_PAGE, EVERYDAY_WALKING_PAGE):
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                lower = text.lower()

                self.assertIn("../RED-FLAGS.md", text)
                for term in (
                    "chest pain",
                    "fainting",
                    "severe dizziness",
                    "unusual shortness of breath",
                    "new severe pain",
                    "numbness",
                    "weakness",
                    "neurological symptoms",
                    "symptoms that worsen",
                    "do not settle",
                ):
                    self.assertIn(term, lower)

                for term in (
                    "weight-loss",
                    "calorie target",
                    "10,000 steps",
                    "heart-rate zone",
                    "wearable",
                    "calculator",
                    "dashboard",
                    "adaptive recommendation",
                    "race-walking",
                    "running progression",
                    "hiking",
                    "rucking",
                    "treadmill protocol",
                    "incline protocol",
                    "medical walking program",
                        "return-to-walking",
                ):
                    self.assertNotIn(term, lower)

        everyday_text = self.everyday_walking_text()
        self.assertNotIn("![", everyday_text)
        self.assertNotIn("media/", everyday_text)

    def test_walking_pages_source_ids_are_page_local_and_indexed(self) -> None:
        expected = {
            BRISK_WALKING_PAGE: (
                "cdc-physical-activity-intensity",
                "cdc-adult-activity",
                "aha-physical-activity-recommendations",
                "mayo-walking",
                "nhs-walking-for-health",
                "local-brisk-walking-red-flags",
            ),
            EVERYDAY_WALKING_PAGE: (
                "cdc-adult-activity",
                "aha-physical-activity-recommendations",
                "nhs-walking-for-health",
                "local-everyday-walking-red-flags",
            ),
        }
        sources = (ROOT / "SOURCES.md").read_text(encoding="utf-8")

        for path, source_ids in expected.items():
            text = path.read_text(encoding="utf-8")
            for source_id in source_ids:
                with self.subTest(path=path.relative_to(ROOT), source_id=source_id):
                    self.assertIn(f"[{source_id}]:", text)
                    self.assertIn(f"][{source_id}]", text)
                    if not source_id.startswith("local-"):
                        self.assertIn(f"[{source_id}]:", sources)

    def test_brisk_walking_muscle_and_feel_guidance(self) -> None:
        text = self.brisk_walking_text()
        muscle_section = section_text(text, "## Muscles involved")
        feel_section = section_text(text, "## What you should feel")
        finding_codes = [
            finding.code for finding in validate_exercise_muscle_guidance(BRISK_WALKING_PAGE, text)
        ]

        self.assertEqual(finding_codes, [])
        self.assertIn("| Role | Muscle region | What it helps do |", muscle_section)
        for term in (
            "Main driver",
            "Posture / transfer",
            "Arm swing support",
            "Foot control",
            "Glutes, thighs, and calves",
            "Trunk",
            "Shoulders and upper back",
            "Feet and ankles",
        ):
            with self.subTest(term=term):
                self.assertIn(term, muscle_section)
        self.assertRegex(feel_section.lower(), r"\b(you may feel|pay attention to)\b")
        self.assertIn("able to talk", " ".join(feel_section.lower().split()))

    def test_walking_m3_source_audit_records_required_claim_samples(self) -> None:
        path = WALKING_MANUAL_PROOF_ROOT / "source-audit.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for heading in (
            "# Walking Source Audit",
            "## Scope",
            "## Claim Samples",
            "## Disposition",
            "## Residual Risk",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

        for claim_type in (
            "intensity",
            "talk-test",
            "weekly-activity-guidance",
            "less-sitting-framing",
            "walking-technique",
            "starter-duration-or-progression",
            "stop-rules",
        ):
            with self.subTest(claim_type=claim_type):
                self.assertIn(claim_type, text)

        for token in ("page_path", "claim_type", "supporting_source", "source_fit", "outcome", "residual_risk"):
            with self.subTest(token=token):
                self.assertIn(token, text)

        for page_path in ("exercises/brisk-walking.md", "principles/everyday-walking.md"):
            with self.subTest(page_path=page_path):
                self.assertIn(page_path, text)

    def test_walking_m3_beginner_comprehension_records_required_prompts(self) -> None:
        path = WALKING_MANUAL_PROOF_ROOT / "beginner-comprehension.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for prompt in (
            "difference between everyday walking and brisk walking",
            "how to know the pace is brisk",
            "reasonable starting duration",
            "what the body should feel",
            "stop conditions",
            "source supports the intensity claim",
            "non-identifying",
            "residual confusion",
        ):
            with self.subTest(prompt=prompt):
                self.assertIn(prompt, text)

        for page_path in ("exercises/brisk-walking.md", "principles/everyday-walking.md"):
            with self.subTest(page_path=page_path):
                self.assertIn(page_path, text)

    def test_walking_m3_optional_image_decision_keeps_first_slice_text_only(self) -> None:
        path = WALKING_MANUAL_PROOF_ROOT / "optional-image-decision.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")

        for token in (
            "# Optional Image Decision",
            "decision: text-only",
            "no image added",
            "exercises/brisk-walking.md",
            "principles/everyday-walking.md",
            "exercise_movement_illustration",
            "no comprehension gap",
            "media/PROVENANCE.md unaffected",
            "residual risk",
        ):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_walking_m3_validation_ledger_records_required_commands(self) -> None:
        self.assertTrue(WALKING_VALIDATION_LEDGER.is_file())
        text = WALKING_VALIDATION_LEDGER.read_text(encoding="utf-8")

        for command in (
            "python3 tools/checks/check_markdown_first.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media/PROVENANCE.md",
            "python3 -m unittest tests.test_exercise_method_guidance tests.test_exercise_muscle_guidance tests.test_exercise_image_standard tests.test_markdown_first_real_pages",
            "python3 -m unittest discover -s tests -p 'test_markdown_first_*.py'",
            "python3 tools/checks/check_privacy.py SOURCES.md RED-FLAGS.md exercises/brisk-walking.md principles/everyday-walking.md media docs/changes/2026-07-05-brisk-walking-and-everyday-walking",
        ):
            with self.subTest(command=command):
                self.assertIn(command, text)

    def test_brisk_walking_required_images_are_local_prompt_backed_and_reviewed(self) -> None:
        text = self.brisk_walking_text()
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected = {
            "media/exercises/brisk-walking/movement.png": (
                "exercise_movement_illustration",
                "Brisk walking movement reference showing upright posture, forward gaze, relaxed shoulders, natural arm swing, and heel-to-toe stride",
            ),
            "media/exercises/brisk-walking/muscle-attention.png": (
                "exercise_muscle_attention_illustration",
                "Brisk walking muscle-attention reference with broad highlights on glutes, thighs, calves, trunk, shoulders, upper back, feet, and ankles",
            ),
        }

        self.assertEqual(text.count("![Brisk walking "), 2)
        self.assertIn("Use these images as broad visual references.", text)

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
                self.assertIn("exercises/brisk-walking.md", split_page_refs(row.get("page_refs", "")))

                prompt_record = row.get("prompt_record", "")
                self.assertEqual(prompt_record, asset_path.replace("media/exercises/", "media/prompts/exercises/").replace(".png", ".md"))
                self.assertTrue((ROOT / prompt_record).is_file())

                prompt_text = (ROOT / prompt_record).read_text(encoding="utf-8")
                self.assertIn(f"asset_path: {asset_path}", prompt_text)
                self.assertIn("## Exact prompt", prompt_text)
                self.assertIn("no in-image text", prompt_text.lower())

    def test_walking_m4_required_image_proof_records_visual_safety(self) -> None:
        required_image_decision = WALKING_MANUAL_PROOF_ROOT / "required-image-decision.md"
        visual_safety = WALKING_MANUAL_PROOF_ROOT / "visual-safety.md"

        for path in (required_image_decision, visual_safety):
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                for token in (
                    "media/exercises/brisk-walking/movement.png",
                    "media/exercises/brisk-walking/muscle-attention.png",
                    "exercise_movement_illustration",
                    "exercise_muscle_attention_illustration",
                    "exercises/brisk-walking.md",
                    "principles/everyday-walking.md",
                    "approved",
                    "residual risk",
                ):
                    self.assertIn(token, text)

        visual_text = visual_safety.read_text(encoding="utf-8").lower()
        for token in (
            "upright posture",
            "forward gaze",
            "relaxed neck and shoulders",
            "natural arm swing",
            "heel-to-toe",
            "broad attention regions",
            "glutes",
            "thighs",
            "calves",
            "trunk",
            "shoulders",
            "feet",
            "no in-image labels",
            "no red pain marks",
            "no race-walking",
            "no running",
            "no treadmill",
            "no hiking",
            "no wearable",
            "no wrong/correct",
            "no clinical",
            "no precise anatomy",
            "no exposed musculature",
            "no exact activation",
        ):
            with self.subTest(token=token):
                self.assertIn(token, visual_text)

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

    def test_post_pr_muscle_attention_images_are_local_prompt_backed_and_reviewed(self) -> None:
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected = {
            "exercises/chest-press.md": (
                "media/exercises/chest-press/muscle-attention.png",
                "Chest press muscle-attention reference with broad highlights on the chest, front shoulders, triceps, and upper-back support area",
            ),
            "exercises/plank.md": (
                "media/exercises/plank/muscle-attention.png",
                "Plank muscle-attention reference with broad highlights on the abdomen, side trunk, glutes, shoulders, upper back, and legs",
            ),
            "exercises/seated-row.md": (
                "media/exercises/seated-row/muscle-attention.png",
                "Seated row muscle-attention reference with broad highlights on the upper back, arms, grip, and trunk posture area",
            ),
        }

        for page_path, (asset_path, alt_text) in expected.items():
            with self.subTest(page_path=page_path):
                path = ROOT / page_path
                text = path.read_text(encoding="utf-8")

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
                self.assertIn(page_path, split_page_refs(row.get("page_refs", "")))

                prompt_record = row.get("prompt_record", "")
                self.assertEqual(prompt_record, asset_path.replace("media/exercises/", "media/prompts/exercises/").replace(".png", ".md"))
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
