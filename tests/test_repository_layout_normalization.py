from pathlib import Path
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
OLD_MACHINE_DIR = "02" + "-machines"
OLD_BODYWEIGHT_DIR = "03" + "-bodyweight"
OLD_RED_FLAGS = "about/" + "red-flags.md"
OLD_MEDIA_MOVEMENTS = "media/" + "movements/"
HISTORICAL_CONTENT_CARDS = "content" + "/" + "cards"


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


def write_root_references(root: Path, readme_body: str = "") -> None:
    (root / "README.md").write_text("# GymPrimer\n\n" + readme_body, encoding="utf-8")
    (root / "SOURCES.md").write_text(
        "# Sources\n\n"
        "[mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842\n",
        encoding="utf-8",
    )
    (root / "RED-FLAGS.md").write_text(
        "# Red Flags\n\n"
        "> Disclaimer: GymPrimer is educational content. It is not medical advice and not personalized coaching.\n\n"
        "Use qualified care for emergencies.\n",
        encoding="utf-8",
    )


def exercise_page(image_markdown: str = "") -> str:
    return textwrap.dedent(
        f"""\
        # Glute Bridge

        Author: Fixture Maintainer
        Created: 2026-06-29
        Last reviewed: 2026-06-29
        Next review due: 2027-06-29
        Review scope: sources, scope boundary, comprehension

        {image_markdown}

        General exercise education. Stop if something feels sharp. [Mayo Clinic][mayo-weight-training] [Mayo Clinic][local-glute-bridge-setup] [Mayo Clinic][local-glute-bridge-safety]

        ## Sources

        - [Mayo Clinic - Weight training][mayo-weight-training]
        - [Mayo Clinic - setup][local-glute-bridge-setup]
        - [Mayo Clinic - safety][local-glute-bridge-safety]

        [mayo-weight-training]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
        [local-glute-bridge-setup]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
        [local-glute-bridge-safety]: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/weight-training/art-20045842
        """
    )


def write_exercise(root: Path, image_markdown: str = "") -> Path:
    (root / "exercises").mkdir(exist_ok=True)
    page = root / "exercises/glute-bridge.md"
    page.write_text(exercise_page(image_markdown), encoding="utf-8")
    return page


def write_provenance(root: Path, asset_path: str, page_refs: str = "exercises/glute-bridge.md") -> None:
    (root / "media").mkdir(exist_ok=True)
    (root / "media/PROVENANCE.md").write_text(
        "# Media Provenance\n\n"
        "| asset_path | asset_type | media_purpose | generator | prompt_or_creation_notes | created_date | human_reviewer | license_assertion | source_inputs | review_status | page_refs | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        f"| {asset_path} | ai_generated_raster | key_movement_illustration | fixture generator | fixture prompt | 2026-06-29 | fixture reviewer | project generated asset allowed for test use | none | approved | {page_refs} | fixture note |\n",
        encoding="utf-8",
    )


class RepositoryLayoutNormalizationTest(unittest.TestCase):
    def test_canonical_content_paths_pass_after_red_flags_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            page = write_exercise(root)

            result = run_check_with_root(root, root / "README.md", root / "SOURCES.md", root / "RED-FLAGS.md", page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_old_numbered_content_path_fails_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            (root / OLD_MACHINE_DIR).mkdir()
            old_page = root / OLD_MACHINE_DIR / "lat-pulldown.md"
            old_page.write_text(exercise_page(), encoding="utf-8")

            result = run_check_with_root(root, old_page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("old_content_path_active", result.stdout)

    def test_old_red_flags_link_fails_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root, f"[Old red flags]({OLD_RED_FLAGS})\n")

            result = run_check_with_root(root, root / "README.md")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale_old_path_reference", result.stdout)
        self.assertIn(OLD_RED_FLAGS, result.stdout)

    def test_compatibility_stub_at_old_path_fails_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            (root / OLD_BODYWEIGHT_DIR).mkdir()
            stub = root / OLD_BODYWEIGHT_DIR / "incline-push-up.md"
            stub.write_text("Moved to [Incline push-up](../exercises/incline-push-up.md).\n", encoding="utf-8")

            result = run_check_with_root(root, stub)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("compatibility_stub_forbidden", result.stdout)

    def test_subject_co_located_media_with_matching_provenance_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            asset = root / "media/exercises/glute-bridge/sequence.png"
            asset.parent.mkdir(parents=True)
            asset.write_text("fixture image bytes\n", encoding="utf-8")
            write_provenance(root, "media/exercises/glute-bridge/sequence.png")
            page = write_exercise(root, "![Glute bridge sequence](../media/exercises/glute-bridge/sequence.png)")

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_old_media_bucket_reference_fails_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            write_provenance(root, f"{OLD_MEDIA_MOVEMENTS}glute-bridge-sequence.png")
            page = write_exercise(root, f"![Glute bridge sequence](../{OLD_MEDIA_MOVEMENTS}glute-bridge-sequence.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("old_media_bucket_reference", result.stdout)

    def test_stale_provenance_asset_path_fails_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            asset = root / "media/exercises/glute-bridge/sequence.png"
            asset.parent.mkdir(parents=True)
            asset.write_text("fixture image bytes\n", encoding="utf-8")
            write_provenance(root, f"{OLD_MEDIA_MOVEMENTS}glute-bridge-sequence.png")
            page = write_exercise(root, "![Glute bridge sequence](../media/exercises/glute-bridge/sequence.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_provenance_missing", result.stdout)
        self.assertIn("stale_media_provenance_path", result.stdout)

    def test_root_level_governance_folders_fail_after_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            (root / "proposals").mkdir()

            result = run_check_with_root(root, root / "README.md")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("governance_path_not_under_docs", result.stdout)

    def test_unclassified_historical_artifact_fails_when_checked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            (root / HISTORICAL_CONTENT_CARDS).mkdir(parents=True)
            historical_note = root / HISTORICAL_CONTENT_CARDS / "legacy.md"
            historical_note.write_text("# Legacy\n\nStill active.\n", encoding="utf-8")

            result = run_check_with_root(root, historical_note)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("historical_artifact_unclassified", result.stdout)

    def test_historical_artifact_with_archive_label_passes_when_checked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_root_references(root)
            (root / HISTORICAL_CONTENT_CARDS).mkdir(parents=True)
            historical_note = root / HISTORICAL_CONTENT_CARDS / "legacy.md"
            historical_note.write_text("# Legacy\n\nHistorical archive retained for traceability.\n", encoding="utf-8")

            result = run_check_with_root(root, historical_note)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
