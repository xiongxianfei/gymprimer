from pathlib import Path
import tempfile
import textwrap
import unittest

from tests.test_exercise_image_standard import run_check_with_root, write_asset, write_red_flags, write_sources


ADVANCED_ROWING_ASSETS = (
    "stroke-timing",
    "rhythm-ratio",
    "monitor-metrics",
    "force-curve",
    "stroke-rate-ladder",
    "damper-drag-factor",
    "power-per-stroke",
    "interval-structure",
)
FORCE_OVERLAY_ASSETS = {"stroke-timing", "rhythm-ratio", "force-curve", "power-per-stroke"}


def write_advanced_rowing_page(root: Path, body: str = "", image_markdown: str = "") -> Path:
    (root / "exercises").mkdir(exist_ok=True)
    page = root / "exercises/rowing-machine-advanced.md"
    body_block = textwrap.indent(body, "            ") if body else ""
    image_block = textwrap.indent(image_markdown, "            ") if image_markdown else ""
    page.write_text(
        textwrap.dedent(
            f"""\
            # Rowing Machine: Advanced Technique and Workouts

            Author: Fixture Maintainer
            Created: 2026-07-07
            Last reviewed: 2026-07-07
            Next review due: 2027-07-07
            Review scope: advanced rowing fixture validation

            > Disclaimer: GymPrimer is educational content for general exercise literacy.
            > It is not medical advice and not personalized coaching.

            ## What this page is for

            This page is static advanced exercise literacy for readers who already understand the beginner rowing stroke. [Concept][fixture-training]

            ## What this page is not

            This page is not individualized coaching, clinical care, racing strategy, or a runtime training product. [Concept][fixture-training]

            ## Prerequisites

            Use this page after you can row 10-15 minutes with a smooth stroke and can explain legs -> body -> arms, then arms -> body -> legs. This threshold is an editorial boundary, not a medical, safety, performance, or eligibility test. [Technique][fixture-movement]

            ## Advanced setup: damper and drag factor

            Damper and drag factor are related but distinct setup concepts, and damper 10 is not proof of better technique. [Setup][fixture-setup]

            ## Monitor basics: split, watts, stroke rate, and distance

            Split, watts, stroke rate, distance, time, and force curve are monitor concepts, not personalized targets. [Concept][fixture-training]

            ## Rhythm and recovery ratio

            Higher stroke rate is not automatically higher quality or intensity. [Technique][fixture-movement]

            ## Force curve and power application

            The force curve is feedback for power application, not a form verdict. [Concept][fixture-training]

            ## Stroke-rate control

            Stroke rate changes should preserve organized technique. [Technique][fixture-movement]

            ## Workout types

            Steady rows, rate ladders, power-per-stroke work, intervals, and benchmark preparation are static examples. Benchmark preparation points to official plans instead of writing a full plan. [Concept][fixture-training]

            ## Muscles involved

            | Phase | Muscle region | What it helps do |
            |---|---|---|
            | Drive | Legs and glutes | Help press the machine away. [Technique][fixture-movement] |
            | Finish | Upper back, lats, and arms | Help finish the handle path. |

            ## What you should feel

            You should feel organized effort and stop for sharp pain, chest pain, dizziness, unusual shortness of breath, or worsening symptoms. [Concept][fixture-training]

            ## Common advanced mistakes

            | Mistake | Better framing |
            |---|---|
            | Chasing rate | Keep technique organized before raising stroke rate. [Technique][fixture-movement] |

            ## High-quality image guide

            Images support Markdown and each image has one teaching purpose. [Setup][fixture-setup]

            {image_block}

            ## Force-intensity visual system

            Color intensity uses a 0-3 relative instructional emphasis scale. It is not exact force output, not EMG activation, not injury risk, and not proof of correct form. Use outline thickness, texture, alt text, and a phase table so color is not the only cue.

            ## Rowing phase force map

            | Stroke phase | Level 3 primary effort | Level 2 support | Level 1 control |
            |---|---|---|---|
            | Drive: leg push | legs and glutes | trunk | upper back and arms |
            | Finish | upper back, lats, and arms | trunk | legs extended and grip controlled |

            ## Safety notes

            Use the central [red flags](../RED-FLAGS.md) page for chest pain, dizziness, fainting, unusual shortness of breath, numbness, weakness, sharp pain, or worsening symptoms. [Concept][fixture-training]

            {body_block}

            ## Sources

            - [Concept][fixture-training]
            - [Setup][fixture-setup]
            - [Technique][fixture-movement]

            [fixture-training]: https://example.org/fixture-training
            [fixture-setup]: https://example.org/fixture-setup
            [fixture-movement]: https://example.org/fixture-movement
            """
        ),
        encoding="utf-8",
    )
    return page


def write_advanced_prompt_packet(root: Path, stem: str, layer: str | None = None, extra: str = "") -> None:
    asset_path = f"media/exercises/rowing-machine-advanced/{stem}.png"
    prompt_path = root / f"media/prompts/exercises/rowing-machine-advanced/{stem}.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    instructional_layer = layer or ("force_intensity_overlay" if stem in FORCE_OVERLAY_ASSETS else "technical_diagram")
    force_map = ""
    if instructional_layer == "force_intensity_overlay":
        force_map = (
            "\nForce-intensity map: 0-3 relative instructional emphasis using blue/purple tint plus outline and texture cues.\n"
            "| Phase | Level 3 | Level 2 | Level 1 |\n"
            "|---|---|---|---|\n"
            "| Drive | legs and glutes | trunk | arms |\n"
        )
    force_map_block = textwrap.indent(force_map, "            ") if force_map else ""
    extra_block = textwrap.indent(extra, "            ") if extra else ""
    prompt_path.write_text(
        textwrap.dedent(
            f"""\
            # Image instruction packet

            asset_path: {asset_path}
            page_reference: exercises/rowing-machine-advanced.md
            media_purpose: exercise_movement_illustration
            instructional_layer: {instructional_layer}
            teaching_goal: Show one advanced rowing concept for static exercise literacy.
            visual_rules: no logos; no red pain-map styling; no copied UI; grayscale review; use outline and texture cues.
            in_image_labels: no
            generator: fixture generator
            created_date: 2026-07-07
            human_reviewer: @fixture-maintainer
            review_status: approved
            review_notes: Fixture visual review placeholder for one teaching purpose.
            {force_map_block}
            {extra_block}

            ## Exact prompt

            Fixture prompt for {stem} showing a generic advanced rowing teaching illustration without logos or identifiable people.
            """
        ),
        encoding="utf-8",
    )


def write_advanced_provenance(root: Path, stems: tuple[str, ...] = ADVANCED_ROWING_ASSETS) -> None:
    (root / "media").mkdir(exist_ok=True)
    headers = (
        "asset_path",
        "asset_type",
        "media_purpose",
        "prompt_record",
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
    for stem in stems:
        asset_path = f"media/exercises/rowing-machine-advanced/{stem}.png"
        row = {
            "asset_path": asset_path,
            "asset_type": "ai_generated_raster",
            "media_purpose": "exercise_movement_illustration",
            "prompt_record": f"media/prompts/exercises/rowing-machine-advanced/{stem}.md",
            "generator": "fixture generator",
            "prompt_or_creation_notes": "fixture one teaching purpose",
            "created_date": "2026-07-07",
            "human_reviewer": "@fixture-maintainer",
            "license_assertion": "project generated asset allowed for test use",
            "source_inputs": "none",
            "review_status": "approved",
            "page_refs": "exercises/rowing-machine-advanced.md",
            "notes": "fixture approved visual-safety review",
        }
        lines.append("| " + " | ".join(row[header] for header in headers) + " |")
    (root / "media/PROVENANCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


class AdvancedRowingMachineTutorialTest(unittest.TestCase):
    def test_valid_advanced_rowing_page_with_eight_scoped_images_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            for stem in ADVANCED_ROWING_ASSETS:
                write_asset(root, f"media/exercises/rowing-machine-advanced/{stem}.png")
                write_advanced_prompt_packet(root, stem)
            write_advanced_provenance(root)
            image_markdown = "\n".join(
                f"![Advanced rowing {stem} image teaching {stem.replace('-', ' ')}](../media/exercises/rowing-machine-advanced/{stem}.png)"
                for stem in ADVANCED_ROWING_ASSETS
            )
            page = write_advanced_rowing_page(root, image_markdown=image_markdown)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_advanced_rowing_exception_rejects_unapproved_asset_and_unrelated_pages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            stems = ADVANCED_ROWING_ASSETS + ("extra-image",)
            for stem in stems:
                write_asset(root, f"media/exercises/rowing-machine-advanced/{stem}.png")
                write_advanced_prompt_packet(root, stem, layer="technical_diagram")
            write_advanced_provenance(root, stems)
            image_markdown = "\n".join(
                f"![Advanced rowing {stem} image teaching {stem.replace('-', ' ')}](../media/exercises/rowing-machine-advanced/{stem}.png)"
                for stem in stems
            )
            page = write_advanced_rowing_page(root, image_markdown=image_markdown)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)
        self.assertIn("exercise_image_unapproved_exception_asset", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            image_blocks = []
            for index in range(4):
                asset_path = f"media/exercises/fixture-exercise/image-{index}.png"
                write_asset(root, asset_path)
                image_blocks.append(f"![Fixture exercise image {index}](../{asset_path})")
            page = root / "exercises/fixture-exercise.md"
            page.parent.mkdir(exist_ok=True)
            page.write_text(
                textwrap.dedent(
                    f"""\
                    # Fixture Exercise

                    Author: Fixture
                    Created: 2026-07-07
                    Last reviewed: 2026-07-07
                    Next review due: 2027-07-07
                    Review scope: default image limit fixture

                    Fixture exercise text. [Fixture][fixture-training]

                    {"\n".join(image_blocks)}

                    ## Sources

                    - [Fixture][fixture-training]
                    - [Setup][fixture-setup]
                    - [Movement][fixture-movement]

                    [fixture-training]: https://example.org/fixture-training
                    [fixture-setup]: https://example.org/fixture-setup
                    [fixture-movement]: https://example.org/fixture-movement
                    """
                ),
                encoding="utf-8",
            )
            write_advanced_provenance(root, ())
            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)

    def test_advanced_prompt_packet_force_overlay_boundaries_fail(self) -> None:
        cases = (
            ("stroke-timing", "force_intensity_overlay", "Force-intensity map:", "advanced_rowing_force_map_missing"),
            ("monitor-metrics", "force_intensity_overlay", "", "advanced_rowing_force_overlay_disallowed"),
            ("stroke-rate-ladder", "force_intensity_overlay", "", "advanced_rowing_force_overlay_rationale_missing"),
        )
        for stem, layer, remove_text, expected_code in cases:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root, f"media/exercises/rowing-machine-advanced/{stem}.png")
                write_advanced_prompt_packet(root, stem, layer=layer)
                prompt = root / f"media/prompts/exercises/rowing-machine-advanced/{stem}.md"
                if remove_text:
                    prompt.write_text(prompt.read_text(encoding="utf-8").replace(remove_text, "Removed map:"), encoding="utf-8")
                write_advanced_provenance(root, (stem,))
                page = write_advanced_rowing_page(
                    root,
                    image_markdown=f"![Advanced rowing {stem} image teaching force overlay boundaries](../media/exercises/rowing-machine-advanced/{stem}.png)",
                )

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_advanced_prompt_packet_required_fields_and_label_rules_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_asset(root, "media/exercises/rowing-machine-advanced/power-per-stroke.png")
            write_advanced_prompt_packet(root, "power-per-stroke")
            prompt = root / "media/prompts/exercises/rowing-machine-advanced/power-per-stroke.md"
            prompt.write_text(prompt.read_text(encoding="utf-8").replace("teaching_goal: Show one advanced rowing concept for static exercise literacy.\n", ""), encoding="utf-8")
            write_advanced_provenance(root, ("power-per-stroke",))
            page = write_advanced_rowing_page(
                root,
                image_markdown="![Advanced rowing power per stroke image teaching controlled drive](../media/exercises/rowing-machine-advanced/power-per-stroke.png)",
            )

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("advanced_rowing_prompt_packet_incomplete", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_asset(root, "media/exercises/rowing-machine-advanced/stroke-timing.png")
            write_advanced_prompt_packet(root, "stroke-timing", extra="label duplication: labels repeated in Markdown and alt text\n")
            prompt = root / "media/prompts/exercises/rowing-machine-advanced/stroke-timing.md"
            prompt.write_text(prompt.read_text(encoding="utf-8").replace("in_image_labels: no", "in_image_labels: yes"), encoding="utf-8")
            write_advanced_provenance(root, ("stroke-timing",))
            page = write_advanced_rowing_page(
                root,
                image_markdown="![Advanced rowing stroke timing image teaching broad effort phases](../media/exercises/rowing-machine-advanced/stroke-timing.png)",
            )

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("advanced_rowing_body_label_disallowed", result.stdout)

    def test_advanced_prompt_packet_excluded_media_text_fails(self) -> None:
        cases = (
            "copied PM5 UI with logo and identifiable person",
            "borrowed screenshot with brand mark",
            "correct/wrong badge and red pain mark",
            "elite-race framing with unsupported promise",
        )
        for review_note in cases:
            with self.subTest(review_note=review_note), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root, "media/exercises/rowing-machine-advanced/monitor-metrics.png")
                write_advanced_prompt_packet(root, "monitor-metrics", extra=f"review_notes: {review_note}\n")
                write_advanced_provenance(root, ("monitor-metrics",))
                page = write_advanced_rowing_page(
                    root,
                    image_markdown="![Advanced rowing monitor metrics image teaching split watts stroke rate and distance concepts](../media/exercises/rowing-machine-advanced/monitor-metrics.png)",
                )

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("advanced_rowing_media_text_forbidden", result.stdout)

    def test_advanced_rowing_page_sections_and_forbidden_scope_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_advanced_rowing_page(root)
            page.write_text(page.read_text(encoding="utf-8").replace("## Stroke-rate control", "## Rate control"), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("advanced_rowing_section_missing", result.stdout)

        forbidden_cases = (
            "This page provides a personalized pace target.",
            "This page calculates personal watts and paces.",
            "This page writes a full benchmark plan for the reader.",
            "This page gives competition programming for a 2k race.",
            "This page provides active recovery protocols.",
            "This page provides medical judgment.",
            "This page provides a treatment plan.",
            "This page gives injury-specific protocols.",
            "This page gives race strategy for a 2k test.",
            "This page creates a tracker for PM5 data.",
            "Method type: advanced_basic_cardio_equipment",
        )
        for forbidden in forbidden_cases:
            with self.subTest(forbidden=forbidden), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                page = write_advanced_rowing_page(root, body=forbidden)

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("advanced_rowing_forbidden_scope", result.stdout)


if __name__ == "__main__":
    unittest.main()
