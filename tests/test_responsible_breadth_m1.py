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

            [nhs-neck]: https://www.nhs.uk/conditions/neck-pain/
            [mayo-back]: https://www.mayoclinic.org/diseases-conditions/back-pain/
            [cdc-adult-activity]: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
            [acsm-resistance-training]: https://acsm.org/resistance-training-guidelines-update-2026/
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


def pattern_page(extra: str = "", red_flags_after_self_management: bool = False) -> str:
    red_flags = "## Red flags: when to stop reading and seek care\n\nSee [the red-flags reference](../about/red-flags.md) before trying self-management.\n\n"
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
    def test_manual_proof_scaffold_lists_required_records(self) -> None:
        text = (ROOT / "docs/changes/responsible-breadth/manual-proof/README.md").read_text(encoding="utf-8")

        for expected in (
            "RB-MP1-red-flags-review.md",
            "RB-MP2-pattern-source-scope.md",
            "RB-MP3-condition-source-scope.md",
            "RB-MP4-principle-source-review.md",
            "RB-MP5-program-boundary-review.md",
            "RB-MP6-comprehension-proof.md",
            "RB-MP7-visual-media-review.md",
            "RB-MP8-validation-ledger.md",
            "RB-MP9-mdbook-build-or-deferral.md",
            "owner role",
            "files inspected",
            "pass/fail result",
            "re-run trigger",
            "No identifying reader details",
        ):
            self.assertIn(expected, text)

    def test_valid_responsible_breadth_paths_pass_without_v0_1_disclaimer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            (root / "principles").mkdir()
            pattern = root / "patterns/forward-head-posture.md"
            principle = root / "principles/how-many-days-a-week.md"
            pattern.write_text(pattern_page(), encoding="utf-8")
            principle.write_text(principle_page(), encoding="utf-8")

            result = run_check_with_root(root, root / "patterns", root / "principles")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_responsible_breadth_page_requires_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            (root / "patterns").mkdir()
            page = root / "patterns/missing-metadata.md"
            page.write_text(pattern_page().replace("Next review due: 2026-09-27\n", ""), encoding="utf-8")

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
            page.write_text(pattern_page().replace("## What this page is not\n", "## Boundary\n"), encoding="utf-8")

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
            text = pattern_page().replace("[CDC][cdc-adult-activity]", "CDC")
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
            (root / "02-machines").mkdir()
            page = root / "02-machines/page.md"
            page.write_text(pattern_page(), encoding="utf-8")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF007", result.stdout)


class ResponsibleBreadthM2Test(unittest.TestCase):
    def test_red_flags_reference_contract(self) -> None:
        text = (ROOT / "about/red-flags.md").read_text(encoding="utf-8")

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
            "about/red-flags.md",
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
                "about",
                "patterns",
                "conditions",
                "principles",
                "programs",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_first_expanded_pages_are_promoted_after_m4_evidence(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for promoted_link in (
            "patterns/anterior-pelvic-tilt.md",
            "conditions/non-specific-chronic-low-back-pain.md",
            "principles/how-many-days-a-week.md",
            "programs/generic-3-day-full-body-example.md",
        ):
            self.assertIn(promoted_link, readme)

        for proof in (
            "docs/changes/responsible-breadth/manual-proof/RB-MP8-validation-ledger.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP9-mdbook-build-or-deferral.md",
        ):
            text = (ROOT / proof).read_text(encoding="utf-8")
            self.assertIn("Pass/fail result: pass", text)
            self.assertIn("Privacy statement:", text)

    def test_m3_manual_proof_records_exist(self) -> None:
        for relative_path in (
            "docs/changes/responsible-breadth/manual-proof/RB-MP2-pattern-source-scope.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP3-condition-source-scope.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP4-principle-source-review.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP5-program-boundary-review.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP6-comprehension-proof.md",
            "docs/changes/responsible-breadth/manual-proof/RB-MP7-visual-media-review.md",
        ):
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("Pass/fail result: pass", text)
            self.assertIn("Privacy statement:", text)


if __name__ == "__main__":
    unittest.main()
