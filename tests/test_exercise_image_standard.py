from pathlib import Path
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"


def run_check_with_root(root: Path, *paths: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["GYMPRIMER_ROOT"] = str(root)
    return subprocess.run(
        [sys.executable, str(CHECK), *map(str, paths)],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def write_sources(root: Path) -> None:
    (root / "SOURCES.md").write_text(
        textwrap.dedent(
            """\
            # Sources

            [fixture-training]: https://example.org/fixture-training
            [fixture-setup]: https://example.org/fixture-setup
            [fixture-movement]: https://example.org/fixture-movement
            """
        ),
        encoding="utf-8",
    )


def write_red_flags(root: Path) -> None:
    (root / "RED-FLAGS.md").write_text(
        "# Red Flags\n\nGeneral safety routing reference.\n",
        encoding="utf-8",
    )


def write_provenance(root: Path, rows: list[dict[str, str]]) -> None:
    (root / "media").mkdir(exist_ok=True)
    headers = (
        "asset_path",
        "asset_type",
        "media_purpose",
        "generator",
        "prompt_or_creation_notes",
        "created_date",
        "human_reviewer",
        "license_assertion",
        "source_inputs",
        "review_status",
        "page_refs",
        "notes",
    )
    lines = [
        "# Media Provenance",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    defaults = {
        "asset_path": "media/exercises/fixture-exercise/setup.png",
        "asset_type": "ai_generated_raster",
        "media_purpose": "exercise_setup_illustration",
        "generator": "fixture generator",
        "prompt_or_creation_notes": "fixture prompt",
        "created_date": "2026-07-03",
        "human_reviewer": "@fixture-maintainer",
        "license_assertion": "project generated asset allowed for test use",
        "source_inputs": "none",
        "review_status": "approved",
        "page_refs": "exercises/fixture-exercise.md",
        "notes": "fixture note",
    }
    for row in rows:
        merged = defaults | row
        lines.append("| " + " | ".join(merged.get(header, "") for header in headers) + " |")
    (root / "media/PROVENANCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_exercise_page(root: Path, image_markdown: str = "", slug: str = "fixture-exercise") -> Path:
    (root / "exercises").mkdir(exist_ok=True)
    page = root / f"exercises/{slug}.md"
    page.write_text(
        (
            "# Fixture Exercise\n\n"
            "Author: Fixture Maintainer\n"
            "Created: 2026-07-03\n"
            "Last reviewed: 2026-07-03\n"
            "Next review due: 2027-07-03\n"
            "Review scope: fixture exercise-image validation\n\n"
            "General beginner exercise education. [Fixture][fixture-training]\n"
            "Setup context uses a stable fixture source. [Setup][fixture-setup]\n"
            "Movement context uses another stable fixture source. [Movement][fixture-movement]\n\n"
            f"{image_markdown}\n\n"
            "## Sources\n\n"
            "- [Fixture training][fixture-training]\n"
            "- [Fixture setup][fixture-setup]\n"
            "- [Fixture movement][fixture-movement]\n\n"
            "[fixture-training]: https://example.org/fixture-training\n"
            "[fixture-setup]: https://example.org/fixture-setup\n"
            "[fixture-movement]: https://example.org/fixture-movement\n"
        ),
        encoding="utf-8",
    )
    return page


def write_asset(root: Path, relative_path: str = "media/exercises/fixture-exercise/setup.png") -> None:
    asset = root / relative_path
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_bytes(b"fixture")


class ExerciseImageStandardTest(unittest.TestCase):
    def test_text_only_exercise_page_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_exercise_page(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_new_exercise_purposes_pass_and_out_of_scope_purposes_fail(self) -> None:
        allowed = (
            "exercise_setup_illustration",
            "exercise_movement_illustration",
            "exercise_muscle_attention_illustration",
        )
        for purpose in allowed:
            with self.subTest(purpose=purpose), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                write_provenance(root, [{"media_purpose": purpose}])
                page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        disallowed = (
            "pattern_alignment_illustration",
            "anatomical_region_illustration",
            "exercise_preview_illustration",
            "exercise_image",
        )
        for purpose in disallowed:
            with self.subTest(purpose=purpose), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                write_provenance(root, [{"media_purpose": purpose}])
                page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("media_usage_out_of_scope", result.stdout)

    def test_generated_raster_provenance_contract_fails_invalid_rows(self) -> None:
        variants = (
            ({}, "media_provenance_missing"),
            ({"generator": ""}, "media_provenance_incomplete"),
            ({"asset_type": "photo"}, "media_provenance_incomplete"),
            ({"review_status": "needs_revision"}, "media_provenance_not_approved"),
            ({"page_refs": "exercises/other.md"}, "media_page_refs_mismatch"),
            ({"human_reviewer": "OpenAI image generation tool"}, "media_human_reviewer_invalid"),
        )
        for row, expected_code in variants:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                if row:
                    write_provenance(root, [row])
                page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_exercise_image_count_and_muscle_attention_limits(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            rows = []
            image_blocks = []
            for index, purpose in enumerate(("exercise_setup_illustration", "exercise_movement_illustration", "exercise_movement_illustration", "exercise_movement_illustration"), start=1):
                asset_path = f"media/exercises/fixture-exercise/image-{index}.png"
                write_asset(root, asset_path)
                rows.append({"asset_path": asset_path, "media_purpose": purpose})
                image_blocks.append(f"![Fixture exercise image {index}](../{asset_path})")
            write_provenance(root, rows)
            page = write_exercise_page(root, "\n".join(image_blocks))

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            rows = []
            image_blocks = []
            for index in (1, 2):
                asset_path = f"media/exercises/fixture-exercise/muscle-{index}.png"
                write_asset(root, asset_path)
                rows.append({"asset_path": asset_path, "media_purpose": "exercise_muscle_attention_illustration"})
                image_blocks.append(f"![Fixture exercise broad shoulder region image {index}](../{asset_path})")
            write_provenance(root, rows)
            page = write_exercise_page(root, "\n".join(image_blocks))

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_muscle_attention_limit", result.stdout)

    def test_path_alt_text_and_unsafe_wording_boundaries(self) -> None:
        cases = (
            ("![Fixture exercise setup image](../media/other/setup.png)", "media/exercises/fixture-exercise/setup.png", "media/other/setup.png", "subject_media_path_mismatch"),
            ("![image](../media/exercises/fixture-exercise/setup.png)", "media/exercises/fixture-exercise/setup.png", "media/exercises/fixture-exercise/setup.png", "exercise_image_alt_text_generic"),
            ("![Fixture diagnosis cure warning badge](../media/exercises/fixture-exercise/setup.png)", "media/exercises/fixture-exercise/setup.png", "media/exercises/fixture-exercise/setup.png", "exercise_image_visual_safety_text"),
        )
        for image_markdown, row_asset_path, actual_asset_path, expected_code in cases:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root, actual_asset_path)
                write_provenance(root, [{"asset_path": row_asset_path}])
                page = write_exercise_page(root, image_markdown)

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_legacy_exercise_image_purposes_remain_valid_without_migration(self) -> None:
        for purpose in ("equipment_identification", "key_movement_illustration"):
            with self.subTest(purpose=purpose), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                write_provenance(root, [{"media_purpose": purpose}])
                page = write_exercise_page(root, "![Fixture exercise legacy image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_template_context_validates_placeholders_without_promoting_product_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            templates = root / "docs/templates"
            templates.mkdir(parents=True)
            template = templates / "exercise-card.md"
            template.write_text(
                textwrap.dedent(
                    """\
                    # Exercise Name

                    Use this template to avoid diagnosis, treatment, and rehabilitation framing.

                    ## Safety notes

                    Do not diagnose pain, prescribe rehab, or treat injuries.

                    ## Sources

                    - [Source name][source-id]

                    [source-id]: https://example.com/
                    """
                ),
                encoding="utf-8",
            )

            result = run_check_with_root(root, template)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            templates = root / "docs/templates"
            templates.mkdir(parents=True)
            template = templates / "exercise-card.md"
            template.write_text("![Remote fixture image](https://example.com/image.png)\n", encoding="utf-8")

            result = run_check_with_root(root, template)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("external_media_reference", result.stdout)


if __name__ == "__main__":
    unittest.main()
