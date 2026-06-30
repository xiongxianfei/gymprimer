from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
FIXTURES = ROOT / "tests/fixtures/markdown-first/guardrails"


def run_check(*paths: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), *map(str, paths)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
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


def write_fixture_repo(root: Path) -> None:
    (root / "SOURCES.md").write_text(
        "# Sources\n\n"
        "[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842\n",
        encoding="utf-8",
    )
    (root / "pages").mkdir()
    (root / "media/pages/page").mkdir(parents=True)


def page_text(image_markdown: str = "") -> str:
    return (
        "# Fixture Page\n\n"
        "> Disclaimer: GymPrimer is educational content. It is not medical advice and not personalized coaching.\n\n"
        f"{image_markdown}\n\n"
        "## Safety notes\n\n"
        "Stop if something feels sharp. [Mayo Clinic][mayo-weight-training]\n\n"
        "## Sources\n\n"
        "- [Mayo Clinic - Weight training][mayo-weight-training]\n\n"
        "[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842\n"
    )


def write_page(root: Path, image_markdown: str = "") -> Path:
    page = root / "pages/page.md"
    page.write_text(page_text(image_markdown), encoding="utf-8")
    return page


def provenance_table(row: str = "") -> str:
    return (
        "# Media Provenance\n\n"
        "| asset_path | asset_type | media_purpose | generator | prompt_or_creation_notes | created_date | human_reviewer | license_assertion | source_inputs | review_status | page_refs | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        f"{row}"
    )


def provenance_row(
    *,
    asset_path: str = "media/pages/page/machine.png",
    asset_type: str = "ai_generated_raster",
    media_purpose: str = "equipment_identification",
    generator: str = "fixture generator",
    review_status: str = "approved",
    page_refs: str = "pages/page.md",
) -> str:
    return (
        f"| {asset_path} | {asset_type} | {media_purpose} | {generator} | "
        "fixture prompt | 2026-06-28 | fixture reviewer | project generated asset allowed for test use | "
        f"none | {review_status} | {page_refs} | fixture note |\n"
    )


class MarkdownFirstGuardrailTest(unittest.TestCase):
    def test_chinese_alias_passes(self) -> None:
        result = run_check(FIXTURES / "allowed-chinese-alias.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_full_chinese_translation_fails(self) -> None:
        result = run_check(FIXTURES / "full-chinese-translation.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF006", result.stdout)

    def test_excluded_scope_terms_fail(self) -> None:
        result = run_check(FIXTURES / "excluded-scope.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("MF007", result.stdout)

    def test_external_image_fails(self) -> None:
        result = run_check(FIXTURES / "external-image.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("external_media_reference", result.stdout)

    def test_relative_image_with_alt_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row()),
                encoding="utf-8",
            )
            page = write_page(root, "![Simple setup diagram](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_text_only_page_passes_without_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            page = write_page(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_svg_under_media_passes_without_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/setup.svg").write_text("<svg></svg>\n", encoding="utf-8")
            page = write_page(root, "![Setup diagram](../media/pages/page/setup.svg)")

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_raster_under_media_requires_provenance(self) -> None:
        for extension in ("png", "jpg", "jpeg", "webp"):
            with self.subTest(extension=extension), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_fixture_repo(root)
                asset = root / f"media/pages/page/machine.{extension}"
                asset.write_text("fixture image bytes\n", encoding="utf-8")
                page = write_page(root, f"![Machine](../media/pages/page/machine.{extension})")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("media_provenance_missing", result.stdout)

    def test_png_with_approved_provenance_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row()),
                encoding="utf-8",
            )
            page = write_page(root, "![Machine](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_png_with_unapproved_provenance_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row(review_status="needs_revision")),
                encoding="utf-8",
            )
            page = write_page(root, "![Machine](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_provenance_not_approved", result.stdout)

    def test_png_with_incomplete_provenance_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row(generator="")),
                encoding="utf-8",
            )
            page = write_page(root, "![Machine](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_provenance_incomplete", result.stdout)

    def test_png_with_out_of_scope_purpose_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row(media_purpose="decorative")),
                encoding="utf-8",
            )
            page = write_page(root, "![Machine](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_usage_out_of_scope", result.stdout)

    def test_png_with_page_ref_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            (root / "media/PROVENANCE.md").write_text(
                provenance_table(provenance_row(page_refs="pages/other.md")),
                encoding="utf-8",
            )
            page = write_page(root, "![Machine](../media/pages/page/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_page_refs_mismatch", result.stdout)

    def test_remote_image_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            page = write_page(root, "![Machine](https://example.com/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("external_media_reference", result.stdout)

    def test_image_outside_media_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "assets").mkdir()
            (root / "assets/machine.png").write_text("fixture image bytes\n", encoding="utf-8")
            page = write_page(root, "![Machine](../assets/machine.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_outside_allowed_directory", result.stdout)

    def test_unsupported_extension_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            (root / "media/pages/page/demo.gif").write_text("fixture image bytes\n", encoding="utf-8")
            page = write_page(root, "![Demo](../media/pages/page/demo.gif)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported_media_type", result.stdout)

    def test_missing_local_media_asset_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture_repo(root)
            page = write_page(root, "![Machine](../media/pages/page/missing.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_asset_missing", result.stdout)


if __name__ == "__main__":
    unittest.main()
