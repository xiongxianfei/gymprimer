from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
OLD_MACHINE_DIR = "02" + "-machines"
OLD_RED_FLAGS = "about/" + "red-flags.md"
FORWARD_HEAD_EXERCISES = (
    "chin-nod",
    "thoracic-extension",
    "wall-slide",
    "prone-y-t",
    "band-pull-apart",
)


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

            [nhs-neck]: https://www.nhs.uk/conditions/neck-pain/
            [mayo-back]: https://www.mayoclinic.org/diseases-conditions/back-pain/
            [cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
            [acsm-resistance-training]: https://acsm.org/resistance-training-guidelines-update-2026/
            """
        ),
        encoding="utf-8",
    )


def write_red_flags(root: Path) -> None:
    (root / "RED-FLAGS.md").write_text(
        textwrap.dedent(
            """\
            # Red Flags

            General safety routing reference.
            """
        ),
        encoding="utf-8",
    )


def rb_sources() -> str:
    return textwrap.dedent(
        """\
        ## Sources

        - [NHS neck pain][nhs-neck]
        - [Mayo Clinic back pain][mayo-back]
        - [CDC adult activity][cdc-adult-activity]
        - [ACSM resistance training][acsm-resistance-training]

        [nhs-neck]: https://www.nhs.uk/conditions/neck-pain/
        [mayo-back]: https://www.mayoclinic.org/diseases-conditions/back-pain/
        [cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
        [acsm-resistance-training]: https://acsm.org/resistance-training-guidelines-update-2026/
        """
    )


def forward_head_exercise_links() -> str:
    labels = {
        "chin-nod": "Chin nod",
        "thoracic-extension": "Thoracic extension",
        "wall-slide": "Wall slide",
        "prone-y-t": "Prone Y/T",
        "band-pull-apart": "Band pull-apart",
    }
    blocks = []
    for slug in FORWARD_HEAD_EXERCISES:
        blocks.append(
            textwrap.dedent(
                f"""\
                - **[{labels[slug]}](../exercises/{slug}.md)**
                  - *Fix reason:* trains a contributor without promising correction.
                  - *Used muscles:* neck, upper-back, and shoulder support muscles.
                  - *Important note:* keep this as an option, not a routine.
                """
            )
        )
    return "\n".join(blocks)


def forward_head_pattern_page(extra_help: str = "", image_markdown: str = "") -> str:
    return (
        "# Forward Head Posture\n\n"
        "Author: Fixture Maintainer\n"
        "Created: 2026-06-30\n"
        "Last reviewed: 2026-06-30\n"
        "Next review due: 2026-09-28\n"
        "Review scope: sources, red flags, scope boundary, comprehension\n\n"
        "## What this page is\n\n"
        "Static consumer education about an observable pattern. [NHS][nhs-neck]\n\n"
        f"{image_markdown}\n"
        "## What this page is not\n\n"
        "This page does not diagnose you, prove a posture is harmful, provide individualized care, promise correction, or explain all pain. [Mayo Clinic][mayo-back]\n\n"
        "## Red flags: when to stop reading and seek care\n\n"
        "See [the red-flags reference](../RED-FLAGS.md) before exercise options. [Mayo Clinic][mayo-back]\n\n"
        "## Why beginners come to this page\n\n"
        "- head looks forward in side-view photos\n"
        "- neck gets tired at the desk\n"
        "- shoulders look rounded in mirrors\n\n"
        "## Working definition\n\n"
        "Forward head posture is an observable head, neck, upper-back, and rib-cage relationship, not a medical condition. [NHS][nhs-neck]\n\n"
        "## How to notice this in yourself\n\n"
        "Use observations, not diagnosis. [NHS][nhs-neck]\n\n"
        "## The core reason\n\n"
        "**Daily-position load.** Long static positions can affect what feels normal. [NHS][nhs-neck]\n\n"
        "**Head-and-neck control.** Gentle neck control can be trained as awareness. [Mayo Clinic][mayo-back]\n\n"
        "**Scapular support.** Upper-back and shoulder-blade support can change how the position feels. [CDC][cdc-adult-activity]\n\n"
        "## What is uncertain or mixed\n\n"
        "Exercise can improve group posture measures, but no page can promise one person's posture correction or pain relief. [NHS][nhs-neck]\n\n"
        "## What commonly helps\n\n"
        "Read this as an educational menu, not a routine.\n\n"
        f"{forward_head_exercise_links()}"
        f"{extra_help}\n"
        "## What to avoid\n\n"
        "Avoid posture-shaming, guaranteed correction promises, and generic routines for pain. [Mayo Clinic][mayo-back]\n\n"
        "## When to see a professional\n\n"
        "See a qualified professional for individual assessment. [NHS][nhs-neck]\n\n"
        "## Where to next in this primer\n\n"
        "- [Chin nod](../exercises/chin-nod.md)\n"
        "- [Thoracic extension](../exercises/thoracic-extension.md)\n"
        "- [Beginner training principles](../principles/how-many-days-a-week.md)\n\n"
        f"{rb_sources()}\n"
        "## Author and review date\n\n"
        "Fixture Maintainer, 2026-06-30\n"
    )


def pattern_page(extra: str = "", red_flags_after_self_management: bool = False) -> str:
    red_flags = f"## Red flags: when to stop reading and seek care\n\nSee [the red-flags reference](../{OLD_RED_FLAGS}) before trying self-management.\n\n"
    self_management = "## Commonly recommended self-management themes\n\nMainstream sources commonly discuss gradual activity and exercise education. [NHS][nhs-neck]\n\n"
    middle = self_management + red_flags if red_flags_after_self_management else red_flags + self_management
    return (
        "# Forward head posture\n\n"
        "Author: Fixture Maintainer\n"
        "Created: 2026-06-29\n"
        "Last reviewed: 2026-06-29\n"
        "Next review due: 2026-09-27\n"
        "Review scope: sources, red flags, scope boundary, comprehension\n\n"
        "## What this page is\n\n"
        "Static consumer education about an observable pattern. [NHS][nhs-neck]\n\n"
        "## What this page is not\n\n"
        "This page does not diagnose you or prescribe treatment. [Mayo Clinic][mayo-back]\n\n"
        f"{middle}"
        "## Plain-language overview\n\n"
        "This page explains common language and context for a posture pattern. [CDC][cdc-adult-activity]\n\n"
        "## What mainstream sources generally agree on\n\n"
        "Staying active and seeking care for concerning symptoms are common themes. [Mayo Clinic][mayo-back]\n\n"
        "## What is uncertain or mixed\n\n"
        "A single posture does not explain every person's pain. [NHS][nhs-neck]\n\n"
        "## What to avoid\n\n"
        "Do not treat this page as a diagnosis. [Mayo Clinic][mayo-back]\n\n"
        "## When to see a professional\n\n"
        "See a qualified professional for individual assessment. [NHS][nhs-neck]\n\n"
        f"{extra}\n"
        f"{rb_sources()}\n"
        "## Author and review date\n\n"
        "Fixture Maintainer, 2026-06-29\n"
    )


def apt_pattern_page(extra_help: str = "") -> str:
    return (
        "# Anterior Pelvic Tilt\n\n"
        "Author: Fixture Maintainer\n"
        "Created: 2026-06-29\n"
        "Last reviewed: 2026-06-29\n"
        "Next review due: 2026-09-27\n"
        "Review scope: sources, red flags, scope boundary, comprehension\n\n"
        "## What this page is\n\n"
        "Static consumer education about an observable pattern. [NHS][nhs-neck]\n\n"
        "## What this page is not\n\n"
        "This page does not diagnose you or prescribe treatment. [Mayo Clinic][mayo-back]\n\n"
        "## Red flags: when to stop reading and seek care\n\n"
        f"See [the red-flags reference](../{OLD_RED_FLAGS}) before exercise options. [Mayo Clinic][mayo-back]\n\n"
        "## Why beginners come to this page\n\n"
        "- their low back arches in standing\n"
        "- planks feel like low-back arching\n"
        "- squats feel hard to control\n\n"
        "## Working definition\n\n"
        "APT is an observable pelvis position, not a diagnosis. [NHS][nhs-neck]\n\n"
        "## How to notice this in yourself\n\n"
        "Use observations, not diagnosis. [NHS][nhs-neck]\n\n"
        "## The core reason\n\n"
        "**Hip-flexor stiffness.** Hip flexors can influence pelvis position. [NHS][nhs-neck]\n\n"
        "**Hip-extensor capacity.** Glutes and hamstrings extend the hip. [Mayo Clinic][mayo-back]\n\n"
        "**Trunk control.** Ribs and pelvis need coordination under movement. [CDC][cdc-adult-activity]\n\n"
        "## What is uncertain or mixed\n\n"
        "Posture does not explain every person's pain. [NHS][nhs-neck]\n\n"
        "## What commonly helps\n\n"
        "Read this as an educational menu, not a routine.\n\n"
        "- **[Dead bug](../exercises/dead-bug.md)**\n"
        "  - *Fix reason:* trains anti-extension trunk control.\n"
        "  - *Used muscles:* rectus abdominis and obliques.\n"
        "  - *Important note:* shorten the reach if the low back lifts.\n"
        f"{extra_help}\n"
        "## What to avoid\n\n"
        "Avoid posture-shaming and guaranteed correction promises. [Mayo Clinic][mayo-back]\n\n"
        "## When to see a professional\n\n"
        "See a qualified professional for individual assessment. [NHS][nhs-neck]\n\n"
        "## Where to next in this primer\n\n"
        "- [Dead bug](../exercises/dead-bug.md)\n\n"
        f"{rb_sources()}\n"
        "## Author and review date\n\n"
        "Fixture Maintainer, 2026-06-29\n"
    )


def write_minimal_exercise(root: Path, slug: str = "dead-bug") -> None:
    (root / "exercises").mkdir(exist_ok=True)
    (root / f"exercises/{slug}.md").write_text(
        textwrap.dedent(
            f"""\
            # {slug.replace('-', ' ').title()}

            Author: Fixture Maintainer
            Created: 2026-06-29
            Last reviewed: 2026-06-29
            Next review due: 2027-06-29
            Review scope: sources, scope boundary, comprehension

            ## Purpose

            General exercise education. [NHS][nhs-neck]

            ## Used muscles

            Primary and secondary muscles.

            ## Equipment and setup

            No equipment.

            ## Movement phases

            Move with control.

            ## Important notes

            Stop for unsafe symptoms. [Mayo Clinic][mayo-back]

            ## Example pictures

            None.

            ## Patterns and conditions where this exercise appears

            - [APT](../patterns/anterior-pelvic-tilt.md)

            {rb_sources()}
            ## Author and review date

            Fixture Maintainer, 2026-06-29
            """
        ),
        encoding="utf-8",
    )


def write_forward_head_exercises(root: Path, omit_section: str | None = None) -> None:
    (root / "exercises").mkdir(exist_ok=True)
    sections = (
        ("## What this exercise is for", "General exercise education. [NHS][nhs-neck]\n"),
        ("## Equipment setup", "Use simple equipment or bodyweight setup.\n"),
        ("## Muscles involved", "Primary and secondary muscles used by the option.\n"),
        ("## Movement breakdown", "Move with control and avoid forcing range. [Mayo Clinic][mayo-back]\n"),
        ("## What you should feel", "A mild training effort in the intended area.\n"),
        ("## Common mistakes", "- Treating it as a required correction.\n"),
        ("## Easier version", "Use less range or resistance.\n"),
        ("## Harder version", "Use more control before more load.\n"),
        ("## Safety notes", "Stop for sharp, worsening, or unsafe symptoms. [Mayo Clinic][mayo-back]\n"),
    )
    for slug in FORWARD_HEAD_EXERCISES:
        body = [
            f"# {slug.replace('-', ' ').title()}",
            "",
            "Author: Fixture Maintainer",
            "Created: 2026-06-30",
            "Last reviewed: 2026-06-30",
            "Next review due: 2027-06-30",
            "Review scope: sources, scope boundary, comprehension",
            "",
            "> Disclaimer: GymPrimer is educational content for general exercise literacy.",
            "> It is not medical advice and not personalized coaching.",
            "",
        ]
        for heading, text in sections:
            if heading == omit_section and slug == "wall-slide":
                continue
            body.extend([heading, "", text, ""])
        body.extend(
            [
                "## Sources",
                "",
                "- [NHS neck pain][nhs-neck]",
                "- [Mayo Clinic back pain][mayo-back]",
                "- [CDC adult activity][cdc-adult-activity]",
                "",
                "[nhs-neck]: https://www.nhs.uk/conditions/neck-pain/",
                "[mayo-back]: https://www.mayoclinic.org/diseases-conditions/back-pain/",
                "[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
                "",
                "## Author and review date",
                "",
                "Fixture Maintainer, 2026-06-30",
                "",
            ]
        )
        (root / f"exercises/{slug}.md").write_text("\n".join(body), encoding="utf-8")


def write_media_provenance(root: Path, rows: list[dict[str, str]]) -> None:
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
    for row in rows:
        lines.append("| " + " | ".join(row.get(header, "fixture") for header in headers) + " |")
    (root / "media/PROVENANCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def principle_page() -> str:
    return (
        "# How many days a week should I train?\n\n"
        "Author: Fixture Maintainer\n"
        "Created: 2026-06-29\n"
        "Last reviewed: 2026-06-29\n"
        "Next review due: 2027-06-29\n"
        "Review scope: sources, scope boundary, comprehension\n\n"
        "## What this page is\n\n"
        "General training literacy for healthy adults. [CDC][cdc-adult-activity]\n\n"
        "## What this page is not\n\n"
        "This is not your personal program. [ACSM][acsm-resistance-training]\n\n"
        "## Plain-language overview\n\n"
        "Many adults can start with a few weekly sessions. [CDC][cdc-adult-activity]\n\n"
        "## General ranges\n\n"
        "Use broad ranges, not symptom-specific instructions. [ACSM][acsm-resistance-training]\n\n"
        f"{rb_sources()}"
    )


def program_page(extra: str = "") -> str:
    return (
        "# Generic 3-day full-body example\n\n"
        "Author: Fixture Maintainer\n"
        "Created: 2026-06-29\n"
        "Last reviewed: 2026-06-29\n"
        "Next review due: 2026-09-27\n"
        "Review scope: sources, scope boundary, comprehension\n\n"
        "## What this page is\n\n"
        "A static worked example for general healthy beginners. [CDC][cdc-adult-activity]\n\n"
        "## What this page is not\n\n"
        "It is not your prescription and does not adapt to symptoms, goals, or equipment. [ACSM][acsm-resistance-training]\n\n"
        "## Example week\n\n"
        "Day 1, day 2, and day 3 illustrate how general principles compose. [CDC][cdc-adult-activity]\n\n"
        f"{extra}\n"
        f"{rb_sources()}"
    )


class ResponsibleBreadthM1Test(unittest.TestCase):
    def test_evidence_contract_does_not_require_separate_proof_scaffold(self) -> None:
        text = (ROOT / "specs/responsible-breadth.test.md").read_text(encoding="utf-8")

        self.assertIn("Bounded audit evidence ownership", text)
        self.assertIn("Separate proof artifact trees are not required", text)
        self.assertIn("owner role", text)
        self.assertIn("files inspected", text)
        self.assertIn("pass/fail", text)
        self.assertIn("re-run trigger", text)
        self.assertNotIn("RB-" + "MP", text)
        self.assertNotIn("manual" + "-proof/", text)

    def test_valid_responsible_breadth_paths_pass_without_v0_1_disclaimer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_minimal_exercise(root)
            (root / "patterns").mkdir()
            (root / "principles").mkdir()
            pattern = root / "patterns/anterior-pelvic-tilt.md"
            principle = root / "principles/how-many-days-a-week.md"
            pattern.write_text(apt_pattern_page(), encoding="utf-8")
            principle.write_text(principle_page(), encoding="utf-8")

            result = run_check_with_root(root, root / "patterns", root / "principles")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_responsible_breadth_page_requires_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            page = root / "patterns/missing-metadata.md"
            page.write_text(apt_pattern_page().replace("Next review due: 2026-09-27\n", ""), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB003", result.stdout)
        self.assertIn("Next review due", result.stdout)

    def test_safety_relevant_page_first_review_due_within_90_days(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "conditions").mkdir()
            page = root / "conditions/stale-review.md"
            page.write_text(pattern_page().replace("Next review due: 2026-09-27", "Next review due: 2026-12-29"), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB003", result.stdout)
        self.assertIn("90 days", result.stdout)

    def test_pattern_page_requires_contract_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            page = root / "patterns/missing-section.md"
            page.write_text(apt_pattern_page().replace("## What this page is not\n", "## Boundary\n"), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB002", result.stdout)
        self.assertIn("What this page is not", result.stdout)

    def test_red_flags_must_precede_self_management(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "conditions").mkdir()
            page = root / "conditions/neck-pain.md"
            page.write_text(pattern_page(red_flags_after_self_management=True), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB004", result.stdout)

    def test_responsible_breadth_pages_need_three_cited_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            page = root / "patterns/too-few-sources.md"
            text = apt_pattern_page().replace("[CDC][cdc-adult-activity]", "CDC")
            text = text.replace("- [ACSM resistance training][acsm-resistance-training]\n", "")
            text = text.replace("[acsm-resistance-training]: https://acsm.org/resistance-training-guidelines-update-2026/\n", "")
            text = text.replace("- [CDC adult activity][cdc-adult-activity]\n", "")
            text = text.replace("[cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html\n", "")
            page.write_text(text, encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB005", result.stdout)

    def test_scope_guardrails_reject_diagnosis_and_prescription(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "programs").mkdir()
            page = root / "programs/generic.md"
            page.write_text(program_page("Follow this program exactly for your knee pain.\n"), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB006", result.stdout)

    def test_old_v0_1_pages_still_reject_original_excluded_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / OLD_MACHINE_DIR).mkdir()
            page = root / OLD_MACHINE_DIR / "page.md"
            page.write_text(pattern_page(), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF007", result.stdout)

    def test_forward_head_pattern_requires_exact_title_and_five_exercise_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_forward_head_exercises(root)
            (root / "patterns").mkdir()
            page = root / "patterns/forward-head-posture.md"
            text = forward_head_pattern_page().replace("# Forward Head Posture", "# Head Sits Forward")
            text = text.replace("- **[Wall slide](../exercises/wall-slide.md)**", "- **Wall slide**")
            page.write_text(text, encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB008", result.stdout)
        self.assertIn("title must be exactly", result.stdout)
        self.assertIn("../exercises/wall-slide.md", result.stdout)

    def test_forward_head_pattern_requires_same_slice_exercise_pages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_forward_head_exercises(root)
            (root / "exercises/wall-slide.md").unlink()
            (root / "patterns").mkdir()
            page = root / "patterns/forward-head-posture.md"
            page.write_text(forward_head_pattern_page(), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB007", result.stdout)
        self.assertIn("missing exercise page", result.stdout)
        self.assertIn("../exercises/wall-slide.md", result.stdout)

    def test_forward_head_real_pattern_page_passes_contract(self) -> None:
        page = ROOT / "patterns/forward-head-posture.md"
        self.assertTrue(page.exists(), "patterns/forward-head-posture.md is required for M3")

        result = run_check_with_root(ROOT, ROOT / "SOURCES.md", ROOT / "RED-FLAGS.md", page)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_forward_head_exercise_pages_require_exercise_contract_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_forward_head_exercises(root, omit_section="## Safety notes")

            result = run_check_with_root(root, root / "exercises/wall-slide.md")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB010", result.stdout)
        self.assertIn("Safety notes", result.stdout)

    def test_forward_head_real_exercise_pages_exist_and_pass_contract(self) -> None:
        paths = [ROOT / "exercises" / f"{slug}.md" for slug in FORWARD_HEAD_EXERCISES]
        missing = [str(path.relative_to(ROOT)) for path in paths if not path.exists()]
        self.assertEqual(missing, [])

        result = run_check_with_root(ROOT, ROOT / "SOURCES.md", ROOT / "RED-FLAGS.md", *paths)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_forward_head_pattern_image_limit_and_text_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_forward_head_exercises(root)
            (root / "patterns").mkdir()
            (root / "media/patterns/forward-head-posture").mkdir(parents=True)
            (root / "media/patterns/forward-head-posture/one.png").write_bytes(b"fixture")
            (root / "media/patterns/forward-head-posture/two.png").write_bytes(b"fixture")
            write_media_provenance(
                root,
                [
                    {
                        "asset_path": "media/patterns/forward-head-posture/one.png",
                        "asset_type": "ai_generated_raster",
                        "media_purpose": "pattern_alignment_illustration",
                        "prompt_or_creation_notes": "comparison image with label text",
                        "review_status": "approved",
                        "page_refs": "patterns/forward-head-posture.md",
                    },
                    {
                        "asset_path": "media/patterns/forward-head-posture/two.png",
                        "asset_type": "ai_generated_raster",
                        "media_purpose": "pattern_alignment_illustration",
                        "review_status": "approved",
                        "page_refs": "patterns/forward-head-posture.md",
                    },
                ],
            )
            image_markdown = (
                "![Forward head comparison with labels](../media/patterns/forward-head-posture/one.png)\n\n"
                "![Second comparison](../media/patterns/forward-head-posture/two.png)\n\n"
            )
            page = root / "patterns/forward-head-posture.md"
            page.write_text(forward_head_pattern_page(image_markdown=image_markdown), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB009", result.stdout)
        self.assertIn("no more than one", result.stdout)
        self.assertIn("media_usage_out_of_scope", result.stdout)
        self.assertIn("in-image text", result.stdout)


class ResponsibleBreadthM2Test(unittest.TestCase):
    def test_red_flags_reference_contract(self) -> None:
        text = (ROOT / "RED-FLAGS.md").read_text(encoding="utf-8")

        for expected in (
            "Disclaimer",
            "not medical advice",
            "## What this page is",
            "## What this page is not",
            "## Emergency care now",
            "## Prompt medical care",
            "## Professional assessment",
            "does not tell you what condition you have",
            "## Sources",
            "[nhs-back-pain]",
            "[mayo-back-pain-when-to-see-doctor]",
            "[medlineplus-low-back-pain-acute]",
        ):
            self.assertIn(expected, text)

        forbidden_triage = (
            "you have cauda equina",
            "you have a fracture",
            "you have cancer",
            "choose this level of care",
        )
        lowered = text.lower()
        for phrase in forbidden_triage:
            self.assertNotIn(phrase, lowered)

    def test_responsible_breadth_templates_exist_and_carry_contract(self) -> None:
        templates = {
            "docs/templates/pattern-page.md": ("## Red flags", "## What is uncertain or mixed"),
            "docs/templates/condition-page.md": ("## Red flags", "## When to see a professional"),
            "docs/templates/programming-principle-page.md": ("## General ranges", "not your personal program"),
            "docs/templates/program-example-page.md": ("## Example week", "not your prescription"),
        }

        for relative_path, expected_parts in templates.items():
            with self.subTest(relative_path=relative_path):
                text = (ROOT / relative_path).read_text(encoding="utf-8")
                for field in ("Author:", "Created:", "Last reviewed:", "Next review due:", "Review scope:"):
                    self.assertIn(field, text)
                for expected in expected_parts:
                    self.assertIn(expected, text)
                self.assertIn("## Sources", text)

        pattern_template = (ROOT / "docs/templates/pattern-page.md").read_text(encoding="utf-8")
        for expected in (
            "../RED-FLAGS.md",
            "## Why beginners come to this page",
            "## Working definition",
            "## How to notice this in yourself",
            "## The core reason",
            "## What commonly helps",
        ):
            self.assertIn(expected, pattern_template)
        for stale in (
            "../about/red-flags.md",
            "## Plain-language overview",
            "## What mainstream sources generally agree on",
            "## Commonly recommended self-management themes",
        ):
            self.assertNotIn(stale, pattern_template)

    def test_sources_and_contributor_guidance_support_responsible_breadth(self) -> None:
        sources = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

        for source_id in (
            "nhs-back-pain",
            "nhs-inform-back-problems",
            "mayo-back-pain-when-to-see-doctor",
            "medlineplus-low-back-pain-acute",
            "nice-low-back-pain-sciatica",
        ):
            self.assertIn(f"[{source_id}]", sources)

        for expected in (
            "Responsible Breadth",
            "higher-bar review",
            "source traceability",
            "red-flag routing",
            "non-diagnostic language",
            "no individualized treatment",
            "no personalized programming",
        ):
            self.assertIn(expected, contributing)


class ResponsibleBreadthM3Test(unittest.TestCase):
    def test_first_expanded_proof_slice_real_pages_pass_checker(self) -> None:
        required_paths = (
            "RED-FLAGS.md",
            "patterns/anterior-pelvic-tilt.md",
            "conditions/non-specific-chronic-low-back-pain.md",
            "principles/how-many-days-a-week.md",
            "programs/generic-3-day-full-body-example.md",
        )
        for relative_path in required_paths:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

        result = subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "SOURCES.md",
                "RED-FLAGS.md",
                "patterns",
                "conditions",
                "principles",
                "programs",
                "exercises",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_apt_pattern_page_follows_reader_journey_architecture(self) -> None:
        page = ROOT / "patterns/anterior-pelvic-tilt.md"
        text = page.read_text(encoding="utf-8")

        for heading in (
            "## Why beginners come to this page",
            "## Working definition",
            "## How to notice this in yourself",
            "## The core reason",
            "## What commonly helps",
        ):
            self.assertIn(heading, text)

        result = subprocess.run(
            [sys.executable, str(CHECK), "SOURCES.md", "patterns/anterior-pelvic-tilt.md", "exercises"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_anterior_pelvic_tilt_solution_links_have_real_targets(self) -> None:
        page = ROOT / "patterns/anterior-pelvic-tilt.md"
        text = page.read_text(encoding="utf-8")
        expected_exercises = (
            "exercises/dead-bug.md",
            "exercises/plank.md",
            "exercises/bird-dog.md",
            "exercises/glute-bridge.md",
            "exercises/hip-hinge.md",
            "exercises/kneeling-hip-flexor-stretch.md",
        )

        for relative_path in expected_exercises:
            pattern_link = "../" + relative_path
            self.assertIn(pattern_link, text)
            exercise_path = ROOT / relative_path
            self.assertTrue(exercise_path.exists(), relative_path)

            exercise_text = exercise_path.read_text(encoding="utf-8")
            image_links = re.findall(r"!\[[^\]]+\]\((../media/exercises/[^)]+\.png)\)", exercise_text)
            self.assertTrue(image_links, f"{relative_path} needs at least one raster example")
            for image_link in image_links:
                image_path = (exercise_path.parent / image_link).resolve()
                self.assertTrue(image_path.exists(), image_link)

    def test_pattern_exercise_preview_requires_annotation_and_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_minimal_exercise(root)
            (root / "patterns").mkdir()
            page = root / "patterns/anterior-pelvic-tilt.md"
            text = apt_pattern_page().replace("  - *Used muscles:* rectus abdominis and obliques.\n", "")
            page.write_text(text, encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB007", result.stdout)
        self.assertIn("Used muscles", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            page = root / "patterns/anterior-pelvic-tilt.md"
            page.write_text(apt_pattern_page(), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RB007", result.stdout)
        self.assertIn("missing exercise page", result.stdout)

    def test_pattern_alignment_media_requires_pattern_alignment_purpose(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_minimal_exercise(root)
            (root / "patterns").mkdir()
            (root / "media/patterns/anterior-pelvic-tilt").mkdir(parents=True)
            (root / "media/patterns/anterior-pelvic-tilt/apt.png").write_bytes(b"fixture")
            write_media_provenance(
                root,
                [
                    {
                        "asset_path": "media/patterns/anterior-pelvic-tilt/apt.png",
                        "asset_type": "ai_generated_raster",
                        "media_purpose": "key_movement_illustration",
                        "review_status": "approved",
                        "page_refs": "patterns/anterior-pelvic-tilt.md",
                    }
                ],
            )
            page = root / "patterns/anterior-pelvic-tilt.md"
            page.write_text(
                apt_pattern_page().replace(
                    "## What this page is not",
                    "![APT comparison](../media/patterns/anterior-pelvic-tilt/apt.png)\n\n## What this page is not",
                ),
                encoding="utf-8",
            )

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_usage_out_of_scope", result.stdout)
        self.assertIn("pattern_alignment_illustration", result.stdout)

    def test_condition_anatomy_media_must_not_imply_diagnosis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "conditions").mkdir()
            (root / "media/conditions").mkdir(parents=True)
            (root / "media/conditions/back.png").write_bytes(b"fixture")
            write_media_provenance(
                root,
                [
                    {
                        "asset_path": "media/conditions/back.png",
                        "asset_type": "ai_generated_raster",
                        "media_purpose": "anatomical_region_illustration",
                        "review_status": "approved",
                        "page_refs": "conditions/back-pain.md",
                    }
                ],
            )
            page = root / "conditions/back-pain.md"
            page.write_text(
                pattern_page().replace(
                    "## What this page is not",
                    "![Diagnosis of damaged spine](../media/conditions/back.png)\n\n## What this page is not",
                ),
                encoding="utf-8",
            )

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_usage_out_of_scope", result.stdout)
        self.assertIn("diagnosis", result.stdout)

    def test_first_expanded_pages_are_promoted_after_m4_evidence(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for promoted_link in (
            "patterns/anterior-pelvic-tilt.md",
            "conditions/non-specific-chronic-low-back-pain.md",
            "principles/how-many-days-a-week.md",
            "programs/generic-3-day-full-body-example.md",
        ):
            self.assertIn(promoted_link, readme)

        spec = (ROOT / "specs/responsible-breadth.test.md").read_text(encoding="utf-8")
        self.assertIn("Final validation ledger and lifecycle sync", spec)
        self.assertIn("mdBook build or deferral", spec)

    def test_forward_head_page_is_not_promoted_from_readme_before_pattern_set(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("patterns/forward-head-posture.md", readme)

    def test_m3_audit_evidence_contract_is_documented(self) -> None:
        text = (ROOT / "specs/responsible-breadth.test.md").read_text(encoding="utf-8")
        for expected in (
            "Pattern/condition semantic safety proof",
            "Programming and program-example semantic boundary proof",
            "Reader comprehension proof",
            "Visual necessity and media provenance",
            "audit-record",
            "bounded audit",
        ):
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
