from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest

from tools.checks.check_markdown_first import load_media_provenance, split_page_refs


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/checks/check_markdown_first.py"
M3_TARGETS = {
    "chin-nod": {
        "movement": "Chin nod movement reference with separate start and small chin-in finish positions",
        "muscle": "Chin nod muscle-attention reference with the front-neck region subtly highlighted",
    },
    "thoracic-extension": {
        "movement": "Thoracic extension movement reference with separate upright start and gentle chair-extension finish positions",
        "muscle": "Thoracic extension muscle-attention reference with the upper-back region subtly highlighted",
    },
    "wall-slide": {
        "movement": "Wall slide movement reference with separate forearms-on-wall start and raised finish positions",
        "muscle": "Wall slide muscle-attention reference with the shoulder-blade and side-rib region subtly highlighted",
    },
    "prone-y-t": {
        "movement": "Prone Y/T movement reference with separate prone Y and prone T arm positions",
        "muscle": "Prone Y/T muscle-attention reference with the upper-back and shoulder-blade region subtly highlighted",
    },
    "band-pull-apart": {
        "movement": "Band pull-apart movement reference with separate chest-height start and open-arm finish positions",
        "muscle": "Band pull-apart muscle-attention reference with the upper-back and rear-shoulder region subtly highlighted",
    },
}
M3_PROMPT_RECORD_REPLACEMENTS = {
    "media/exercises/chin-nod/movement.png",
    "media/exercises/thoracic-extension/movement.png",
    "media/exercises/prone-y-t/movement.png",
    "media/exercises/band-pull-apart/movement.png",
    "media/exercises/band-pull-apart/muscle-attention.png",
}
M3_PROMPT_RECORD_COMPATIBILITY_ASSETS = {
    "media/exercises/chin-nod/muscle-attention.png",
    "media/exercises/thoracic-extension/muscle-attention.png",
    "media/exercises/wall-slide/movement.png",
    "media/exercises/wall-slide/muscle-attention.png",
    "media/exercises/prone-y-t/muscle-attention.png",
}
TAI_CHI_ASSETS = (
    (
        "setup",
        "exercise_setup_illustration",
        "Tai Chi setup image showing a relaxed ready stance",
    ),
    (
        "weight-shift",
        "exercise_movement_illustration",
        "Tai Chi weight-shift image showing weight moving between feet",
    ),
    (
        "muscle-attention",
        "exercise_muscle_attention_illustration",
        "Tai Chi muscle-attention image showing broad leg and trunk regions",
    ),
)
BADUANJIN_ASSETS = (
    (
        "setup",
        "exercise_setup_illustration",
        "Baduanjin setup image showing comfortable ready stance with soft knees",
    ),
    (
        "two-hands-lift",
        "exercise_movement_illustration",
        "Baduanjin two-hands-lift image showing a slow upward reach with relaxed shoulders",
    ),
    (
        "drawing-bow",
        "exercise_movement_illustration",
        "Baduanjin drawing-bow image showing a calm side stance and non-combat arm path",
    ),
    (
        "alternating-reach",
        "exercise_movement_illustration",
        "Baduanjin alternating-reach image showing one hand up and one hand lowering gently",
    ),
    (
        "muscle-attention",
        "exercise_muscle_attention_illustration",
        "Baduanjin muscle-attention image showing broad leg trunk shoulder upper-back foot and ankle regions",
    ),
)
SAFER_RUNNING_ASSETS = (
    (
        "posture",
        "exercise_movement_illustration",
        "Safer running posture image showing tall posture and relaxed arm swing",
    ),
    (
        "landing",
        "exercise_movement_illustration",
        "Safer running landing image showing the foot close to the body with a short quiet stride",
    ),
    (
        "run-walk",
        "exercise_movement_illustration",
        "Safer running run-walk image showing easy running and walking recovery",
    ),
    (
        "warm-up",
        "exercise_movement_illustration",
        "Safer running warm-up image showing walking easy jogging and dynamic preparation",
    ),
    (
        "muscle-attention",
        "exercise_muscle_attention_illustration",
        "Safer running muscle-attention image showing broad glute thigh calf foot ankle trunk and shoulder regions",
    ),
    (
        "overstride-comparison",
        "exercise_movement_illustration",
        "Safer running overstride comparison image showing an overreaching step beside a shorter neutral step",
    ),
)
TOP_FIVE_M3_ASSETS = {
    "brisk-walking": {
        "expected_count": 5,
        "assets": {
            "media/exercises/brisk-walking/setup.png": ("exercise_setup_illustration", "Brisk walking setup reference showing upright posture before starting on a flat path"),
            "media/exercises/brisk-walking/brisk-pace-posture.png": ("exercise_movement_illustration", "Brisk walking posture reference with forward gaze, relaxed shoulders, and natural arm swing"),
            "media/exercises/brisk-walking/shorter-walk-option.png": ("exercise_movement_illustration", "Brisk walking shorter-walk option reference on a flat path with a comfortable stride"),
        },
    },
    "chest-press": {
        "expected_count": 5,
        "assets": {
            "media/exercises/chest-press/setup.png": ("exercise_setup_illustration", "Chest press setup reference with back against pad, feet flat, and hands on handles"),
            "media/exercises/chest-press/start-position.png": ("exercise_movement_illustration", "Chest press start-position reference with elbows bent and handles near chest height"),
            "media/exercises/chest-press/finish-position.png": ("exercise_movement_illustration", "Chest press finish-position reference with handles pressed forward and elbows not locked"),
        },
    },
    "chin-nod": {
        "expected_count": 5,
        "assets": {
            "media/exercises/chin-nod/setup.png": ("exercise_setup_illustration", "Chin nod setup reference showing seated upright posture with head level and neck long"),
            "media/exercises/chin-nod/start-crop.png": ("exercise_movement_illustration", "Chin nod start reference with head level and gaze forward"),
            "media/exercises/chin-nod/chin-in-crop.png": ("exercise_movement_illustration", "Chin nod finish reference showing a small chin-in motion with neck long"),
        },
    },
    "dead-bug": {
        "expected_count": 5,
        "assets": {
            "media/exercises/dead-bug/setup-crop.png": ("exercise_setup_illustration", "Dead bug setup reference lying on back with hips and knees bent and arms reaching up"),
            "media/exercises/dead-bug/opposite-reach-crop.png": ("exercise_movement_illustration", "Dead bug opposite-reach reference with one arm and opposite leg moving away from center"),
            "media/exercises/dead-bug/range-limit-crop.png": ("exercise_movement_illustration", "Dead bug smaller-range reference showing controlled reach while the low back stays quiet"),
            "media/exercises/dead-bug/muscle-attention.png": ("exercise_muscle_attention_illustration", "Dead bug muscle-attention reference with broad highlights on trunk, hip, and shoulder support regions"),
        },
    },
    "glute-bridge": {
        "expected_count": 5,
        "assets": {
            "media/exercises/glute-bridge/setup-crop.png": ("exercise_setup_illustration", "Glute bridge setup reference lying on back with knees bent and feet flat"),
            "media/exercises/glute-bridge/bridge-top-crop.png": ("exercise_movement_illustration", "Glute bridge top-position reference with hips lifted and ribs quiet"),
            "media/exercises/glute-bridge/rib-control-crop.png": ("exercise_movement_illustration", "Glute bridge rib-control reference showing a smaller lift with steady trunk position"),
            "media/exercises/glute-bridge/muscle-attention.png": ("exercise_muscle_attention_illustration", "Glute bridge muscle-attention reference with broad highlights on glutes, hamstrings, and trunk support"),
        },
    },
    "hip-hinge": {
        "expected_count": 5,
        "assets": {
            "media/exercises/hip-hinge/tall-start-crop.png": ("exercise_setup_illustration", "Hip hinge tall-start reference standing upright with soft knees and long spine"),
            "media/exercises/hip-hinge/hips-back-crop.png": ("exercise_movement_illustration", "Hip hinge hips-back reference showing hips moving back with a long spine"),
            "media/exercises/hip-hinge/spine-change-crop.png": ("exercise_movement_illustration", "Hip hinge control reference showing range limited before spine position changes"),
            "media/exercises/hip-hinge/muscle-attention.png": ("exercise_muscle_attention_illustration", "Hip hinge muscle-attention reference with broad highlights on hamstrings, glutes, trunk, upper back, and lat regions"),
        },
    },
    "incline-push-up": {
        "expected_count": 5,
        "assets": {
            "media/exercises/incline-push-up/start-crop.png": ("exercise_movement_illustration", "Incline push-up start reference with hands on a stable surface and body in a straight line"),
            "media/exercises/incline-push-up/lowered-crop.png": ("exercise_movement_illustration", "Incline push-up lowered-position reference with elbows bending under control"),
            "media/exercises/incline-push-up/muscle-attention.png": ("exercise_muscle_attention_illustration", "Incline push-up muscle-attention reference with broad highlights on chest, shoulders, triceps, and trunk"),
            "media/exercises/incline-push-up/higher-surface.png": ("exercise_setup_illustration", "Incline push-up easier setup reference using a higher stable surface"),
        },
    },
    "kneeling-hip-flexor-stretch": {
        "expected_count": 5,
        "assets": {
            "media/exercises/kneeling-hip-flexor-stretch/setup-crop.png": ("exercise_setup_illustration", "Kneeling hip flexor stretch setup reference in a half-kneeling position with upright trunk"),
            "media/exercises/kneeling-hip-flexor-stretch/stretch-position-crop.png": ("exercise_movement_illustration", "Kneeling hip flexor stretch position reference with hips gently shifting forward"),
            "media/exercises/kneeling-hip-flexor-stretch/low-back-control-crop.png": ("exercise_movement_illustration", "Kneeling hip flexor stretch control reference showing smaller range with steady low back"),
            "media/exercises/kneeling-hip-flexor-stretch/muscle-attention.png": ("exercise_muscle_attention_illustration", "Kneeling hip flexor stretch muscle-attention reference with broad highlights on rear hip, thigh, glute, trunk, and front-leg support"),
        },
    },
    "lat-pulldown": {
        "expected_count": 5,
        "assets": {
            "media/exercises/lat-pulldown/setup.png": ("exercise_setup_illustration", "Lat pulldown setup reference seated under the bar with thighs supported and hands on the bar"),
            "media/exercises/lat-pulldown/muscle-attention.png": ("exercise_muscle_attention_illustration", "Lat pulldown muscle-attention reference with broad highlights on lats, upper back, rear shoulders, arms, grip, and trunk"),
            "media/exercises/lat-pulldown/controlled-finish.png": ("exercise_movement_illustration", "Lat pulldown controlled-finish reference with bar near upper chest and elbows down"),
        },
    },
    "plank": {
        "expected_count": 5,
        "assets": {
            "media/exercises/plank/full-plank-crop.png": ("exercise_movement_illustration", "Plank full-position reference with straight body line from head to heels"),
            "media/exercises/plank/knee-plank-crop.png": ("exercise_movement_illustration", "Plank knee-option reference with knees down and trunk steady"),
            "media/exercises/plank/hip-control-crop.png": ("exercise_movement_illustration", "Plank hip-control reference showing a steady line without hips dropping"),
        },
    },
    "prone-y-t": {
        "expected_count": 5,
        "assets": {
            "media/exercises/prone-y-t/setup.png": ("exercise_setup_illustration", "Prone Y/T setup reference lying face down with gaze down and arms relaxed near the sides"),
            "media/exercises/prone-y-t/prone-y-crop.png": ("exercise_movement_illustration", "Prone Y reference with arms lifted diagonally overhead while the neck stays relaxed"),
            "media/exercises/prone-y-t/prone-t-crop.png": ("exercise_movement_illustration", "Prone T reference with arms lifted out to the sides while the neck stays relaxed"),
        },
    },
    "rowing-machine": {
        "expected_count": 5,
        "assets": {
            "media/exercises/rowing-machine/drive-crop.png": ("exercise_movement_illustration", "Rowing machine drive reference with legs pressing and handle moving toward the body"),
            "media/exercises/rowing-machine/finish-crop.png": ("exercise_movement_illustration", "Rowing machine finish reference with tall posture and handle close to the lower ribs"),
        },
    },
    "seated-row": {
        "expected_count": 5,
        "assets": {
            "media/exercises/seated-row/setup.png": ("exercise_setup_illustration", "Seated row setup reference with feet supported, trunk upright, and hands on handles"),
            "media/exercises/seated-row/start-position.png": ("exercise_movement_illustration", "Seated row start-position reference with arms extended and trunk upright"),
            "media/exercises/seated-row/finish-position.png": ("exercise_movement_illustration", "Seated row finish-position reference with handles near lower ribs and elbows close"),
        },
    },
    "tai-chi-basics": {
        "expected_count": 5,
        "assets": {
            "media/exercises/tai-chi-basics/slow-arm-path.png": ("exercise_movement_illustration", "Tai Chi slow arm-path reference with rounded arms moving gently at chest height"),
            "media/exercises/tai-chi-basics/smaller-range.png": ("exercise_movement_illustration", "Tai Chi smaller-range option reference with small weight shift and arms close to the body"),
        },
    },
    "thoracic-extension": {
        "expected_count": 5,
        "assets": {
            "media/exercises/thoracic-extension/setup.png": ("exercise_setup_illustration", "Thoracic extension setup reference seated tall with upper back lightly against the chair edge"),
            "media/exercises/thoracic-extension/upright-start-crop.png": ("exercise_movement_illustration", "Thoracic extension upright-start reference with ribs quiet and head supported"),
            "media/exercises/thoracic-extension/extension-finish-crop.png": ("exercise_movement_illustration", "Thoracic extension finish reference showing gentle upper-back extension over the chair"),
        },
    },
    "wall-slide": {
        "expected_count": 5,
        "assets": {
            "media/exercises/wall-slide/setup.png": ("exercise_setup_illustration", "Wall slide setup reference facing the wall with forearms on the wall and ribs quiet"),
            "media/exercises/wall-slide/start-crop.png": ("exercise_movement_illustration", "Wall slide start reference with forearms on the wall at shoulder height"),
            "media/exercises/wall-slide/raised-finish-crop.png": ("exercise_movement_illustration", "Wall slide raised-finish reference with arms sliding upward while shoulders stay relaxed"),
        },
    },
}


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


def write_prompt_record(
    root: Path,
    prompt_record: str = "media/prompts/exercises/fixture-exercise/setup.md",
    asset_path: str = "media/exercises/fixture-exercise/setup.png",
    exact_prompt: str = "Fixture exact full prompt text for the accepted image.",
    extra_fields: dict[str, str] | None = None,
) -> None:
    record_path = root / prompt_record
    record_path.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "asset_path": asset_path,
        "generator": "fixture generator",
        "created_date": "2026-07-03",
        "human_reviewer": "@fixture-maintainer",
        "review_status": "approved",
    }
    if extra_fields:
        fields |= extra_fields
    record_path.write_text(
        textwrap.dedent(
            f"""\
            # Prompt Record

            asset_path: {fields.get("asset_path", "")}
            generator: {fields.get("generator", "")}
            created_date: {fields.get("created_date", "")}
            human_reviewer: {fields.get("human_reviewer", "")}
            review_status: {fields.get("review_status", "")}

            ## Exact prompt

            {exact_prompt}
            """
        ),
        encoding="utf-8",
    )


def write_provenance(root: Path, rows: list[dict[str, str]], create_prompt_records: bool = True) -> None:
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
    defaults = {
        "asset_path": "media/exercises/fixture-exercise/setup.png",
        "asset_type": "ai_generated_raster",
        "media_purpose": "exercise_setup_illustration",
        "prompt_record": "media/prompts/exercises/fixture-exercise/setup.md",
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
        if create_prompt_records and merged.get("prompt_record") and merged["media_purpose"].startswith("exercise_"):
            write_prompt_record(root, merged["prompt_record"], merged["asset_path"])
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


def write_top_five_reviewer_exception_fixture(
    root: Path,
    slug: str = "bird-dog",
    prompt_record: str = "media/prompts/exercises/bird-dog/setup.md",
    include_prompt_record: bool = True,
) -> Path:
    asset_path = f"media/exercises/{slug}/setup.png"
    write_asset(root, asset_path)
    write_provenance(
        root,
        [
            {
                "asset_path": asset_path,
                "media_purpose": "exercise_setup_illustration",
                "prompt_record": prompt_record,
                "human_reviewer": "",
                "page_refs": f"exercises/{slug}.md",
            }
        ],
        create_prompt_records=False,
    )
    if include_prompt_record:
        write_prompt_record(
            root,
            prompt_record=prompt_record,
            asset_path=asset_path,
            extra_fields={"human_reviewer": ""},
        )
    return write_exercise_page(
        root,
        f"![{slug} setup image](../{asset_path})",
        slug=slug,
    )


def write_tai_chi_image_fixture(root: Path, assets: tuple[tuple[str, str, str], ...] = TAI_CHI_ASSETS) -> Path:
    rows = []
    image_blocks = []
    for stem, purpose, alt_text in assets:
        asset_path = f"media/exercises/tai-chi-basics/{stem}.png"
        prompt_record = f"media/prompts/exercises/tai-chi-basics/{stem}.md"
        write_asset(root, asset_path)
        rows.append(
            {
                "asset_path": asset_path,
                "media_purpose": purpose,
                "prompt_record": prompt_record,
                "page_refs": "exercises/tai-chi-basics.md",
            }
        )
        image_blocks.append(f"![{alt_text}](../{asset_path})")
    write_provenance(root, rows)
    return write_exercise_page(root, "\n".join(image_blocks), slug="tai-chi-basics")


def write_baduanjin_image_fixture(root: Path, assets: tuple[tuple[str, str, str], ...] = BADUANJIN_ASSETS) -> Path:
    rows = []
    image_blocks = []
    for stem, purpose, alt_text in assets:
        asset_path = f"media/exercises/baduanjin-basics/{stem}.png"
        prompt_record = f"media/prompts/exercises/baduanjin-basics/{stem}.md"
        write_asset(root, asset_path)
        rows.append(
            {
                "asset_path": asset_path,
                "media_purpose": purpose,
                "prompt_record": prompt_record,
                "page_refs": "exercises/baduanjin-basics.md",
            }
        )
        image_blocks.append(f"![{alt_text}](../{asset_path})")
    write_provenance(root, rows)
    return write_exercise_page(root, "\n".join(image_blocks), slug="baduanjin-basics")


def write_safer_running_image_fixture(root: Path, assets: tuple[tuple[str, str, str], ...] = SAFER_RUNNING_ASSETS) -> Path:
    rows = []
    image_blocks = []
    for stem, purpose, alt_text in assets:
        asset_path = f"media/exercises/safer-running-basics/{stem}.png"
        prompt_record = f"media/prompts/exercises/safer-running-basics/{stem}.md"
        write_asset(root, asset_path)
        rows.append(
            {
                "asset_path": asset_path,
                "media_purpose": purpose,
                "prompt_record": prompt_record,
                "page_refs": "exercises/safer-running-basics.md",
            }
        )
        image_blocks.append(f"![{alt_text}](../{asset_path})")
    write_provenance(root, rows)
    (root / "exercises").mkdir(exist_ok=True)
    page = root / "exercises/safer-running-basics.md"
    page.write_text(
        (
            "# Safer Running Basics\n\n"
            "Author: Fixture Maintainer\n"
            "Created: 2026-07-06\n"
            "Last reviewed: 2026-07-06\n"
            "Next review due: 2027-07-06\n"
            "Review scope: safer running image validation\n\n"
            "Also searched as: injury-free running, beginner running, running without getting hurt\n\n"
            "General beginner running education. [Fixture][fixture-training]\n\n"
            + "\n".join(image_blocks)
            + "\n\n"
            "## What this is for\n\n"
            "Use this page to learn a simple beginner running start. [Fixture][fixture-training]\n\n"
            "## What this page cannot promise\n\n"
            "No page can guarantee injury-free running; this is general education. [Fixture][fixture-setup]\n\n"
            "## Before you start\n\n"
            "Start easy and stop for unusual symptoms. [Fixture][fixture-training]\n\n"
            "## Warm up\n\n"
            "Begin with easy walking before running. [Fixture][fixture-setup]\n\n"
            "## Running form basics\n\n"
            "Run tall, keep the shoulders relaxed, and avoid forcing a specific foot strike. [Fixture][fixture-movement]\n\n"
            "## Muscles involved\n\n"
            "| Role | Muscle region | What it helps do |\n"
            "|---|---|---|\n"
            "| Support and push-off | Glutes, thighs, and calves | Help support each step. [Fixture][fixture-movement] |\n"
            "| Landing control | Feet, ankles, calves, and thighs | Help control each landing. |\n"
            "| Posture and transfer | Trunk | Helps you stay tall. |\n"
            "| Rhythm and balance | Shoulders, upper back, and arms | Help arm swing stay relaxed. |\n\n"
            "## What you should feel\n\n"
            "You should feel warm and slightly out of breath. Stop for chest pain, dizziness, unusual shortness of breath, sharp pain, or worsening symptoms. [Fixture][fixture-training]\n\n"
            "## How much to do\n\n"
            "Method type: basic_cardio_activity\n\n"
            "Beginner starting point: Try 10-20 minutes total with short easy running intervals and walking breaks.\n"
            "Effort: Keep the running portions easy enough that you could speak in short sentences.\n"
            "Progression: First make running feel smoother, then add a little total time.\n"
            "Stop if: Stop for chest pain, dizziness, unusual shortness of breath, sharp pain, or worsening symptoms. [Fixture][fixture-training]\n\n"
            "## Common mistakes\n\n"
            "| Mistake | Safer framing |\n"
            "|---|---|\n"
            "| Running too far too soon | Use run/walk intervals and increase gradually. [Fixture][fixture-training] |\n"
            "| Ignoring sharp or worsening symptoms | Stop and use the safety guidance. [Fixture][fixture-training] |\n\n"
            "## Easier version\n\n"
            "Use shorter total time, more walking, flatter routes, and fewer running days.\n\n"
            "## Harder version\n\n"
            "First add a little total time or a little more easy running inside the same session.\n\n"
            "## Safety notes\n\n"
            "Use the central [red flags](../RED-FLAGS.md) page for chest pain, dizziness, fainting, unusual shortness of breath, numbness, weakness, sharp pain, or worsening symptoms. [Fixture][fixture-training]\n\n"
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


class ExerciseImageStandardTest(unittest.TestCase):
    def test_safer_running_first_batch_six_images_passes_with_path_scoped_exception(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_safer_running_image_fixture(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_safer_running_seventh_image_second_muscle_and_unapproved_asset_fail(self) -> None:
        seventh_image_assets = SAFER_RUNNING_ASSETS + (
            (
                "shoes",
                "exercise_setup_illustration",
                "Safer running shoe and clothing setup image showing simple running gear",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_safer_running_image_fixture(root, seventh_image_assets)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)
        self.assertIn("exercise_image_unapproved_exception_asset", result.stdout)

        second_muscle_assets = SAFER_RUNNING_ASSETS + (
            (
                "second-muscle-attention",
                "exercise_muscle_attention_illustration",
                "Safer running second muscle-attention image showing another broad body-region reference",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_safer_running_image_fixture(root, second_muscle_assets)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)
        self.assertIn("exercise_muscle_attention_limit", result.stdout)

        unapproved_within_limit = SAFER_RUNNING_ASSETS[:5] + (
            (
                "shoes",
                "exercise_setup_illustration",
                "Safer running shoe and clothing setup image showing simple running gear",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_safer_running_image_fixture(root, unapproved_within_limit)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_unapproved_exception_asset", result.stdout)

    def test_baduanjin_candidate_pool_records_deferred_alternatives(self) -> None:
        evidence = (ROOT / "docs/changes/2026-07-06-necessary-images-and-baduanjin-exercise/image-candidate-pool.md").read_text(encoding="utf-8")

        for rank in range(1, 11):
            self.assertIn(f"| {rank} |", evidence)

        self.assertIn("Baduanjin Basics", evidence)
        self.assertIn("setup.png", evidence)
        self.assertIn("two-hands-lift.png", evidence)
        self.assertIn("drawing-bow.png", evidence)
        self.assertIn("alternating-reach.png", evidence)
        self.assertIn("muscle-attention.png", evidence)
        self.assertIn("Candidates 6-10", evidence)
        self.assertIn("deferred alternatives", evidence)
        self.assertIn("not approval to publish a sixth image", evidence)

    def test_baduanjin_first_batch_five_images_passes_with_path_scoped_exception(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_baduanjin_image_fixture(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_baduanjin_sixth_image_and_second_muscle_attention_fail(self) -> None:
        sixth_image_assets = BADUANJIN_ASSETS + (
            (
                "look-back",
                "exercise_movement_illustration",
                "Baduanjin look-back image showing gentle trunk rotation within comfortable range",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_baduanjin_image_fixture(root, sixth_image_assets)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_count_exceeded", result.stdout)

        second_muscle_assets = BADUANJIN_ASSETS + (
            (
                "second-muscle-attention",
                "exercise_muscle_attention_illustration",
                "Baduanjin second muscle-attention image showing another broad body-region reference",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_baduanjin_image_fixture(root, second_muscle_assets)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_muscle_attention_limit", result.stdout)

    def test_baduanjin_exception_does_not_change_default_three_image_limit(self) -> None:
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

    def test_baduanjin_prompt_record_and_visual_text_failures_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            asset_path = "media/exercises/baduanjin-basics/drawing-bow.png"
            write_asset(root, asset_path)
            write_provenance(
                root,
                [
                    {
                        "asset_path": asset_path,
                        "media_purpose": "exercise_movement_illustration",
                        "prompt_record": "",
                        "page_refs": "exercises/baduanjin-basics.md",
                    }
                ],
                create_prompt_records=False,
            )
            page = write_exercise_page(root, "![Baduanjin drawing-bow image showing calm stance](../media/exercises/baduanjin-basics/drawing-bow.png)", slug="baduanjin-basics")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_prompt_record_missing", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            asset_path = "media/exercises/baduanjin-basics/drawing-bow.png"
            write_asset(root, asset_path)
            write_provenance(
                root,
                [
                    {
                        "asset_path": asset_path,
                        "media_purpose": "exercise_movement_illustration",
                        "prompt_record": "media/prompts/exercises/baduanjin-basics/drawing-bow.md",
                        "page_refs": "exercises/baduanjin-basics.md",
                        "prompt_or_creation_notes": "Baduanjin image with weapon target and combat warning badge",
                    }
                ],
            )
            page = write_exercise_page(root, "![Baduanjin drawing-bow combat image](../media/exercises/baduanjin-basics/drawing-bow.png)", slug="baduanjin-basics")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_visual_safety_text", result.stdout)

    def test_baduanjin_forbidden_scope_wording_fails(self) -> None:
        cases = (
            "This Baduanjin page is a treatment protocol for balance problems.",
            "This Baduanjin page teaches the full traditional form and all eight brocades.",
            "This Baduanjin page is a fall-prevention program.",
            "This Baduanjin page provides adaptive coaching for balance practice.",
        )
        for body_text in cases:
            with self.subTest(body_text=body_text), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                page = write_exercise_page(root, body_text, slug="baduanjin-basics")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("RB006", result.stdout)

    def test_tai_chi_candidate_pool_records_deferred_alternatives(self) -> None:
        spec = (ROOT / "specs/necessary-images-and-tai-chi-exercise.md").read_text(encoding="utf-8")
        plan = (ROOT / "docs/plans/2026-07-05-necessary-images-and-tai-chi-exercise.md").read_text(encoding="utf-8")
        proposal = (ROOT / "docs/proposals/2026-07-05-necessary-images-and-tai-chi-exercise.md").read_text(encoding="utf-8")

        for text in (spec, plan, proposal):
            with self.subTest(surface=text[:40]):
                self.assertIn("Tai Chi", text)
                self.assertTrue("top-10" in text or "ten-candidate" in text)
                self.assertIn("exactly three", text)
                self.assertIn("Candidates 4-10", text)
                self.assertIn("deferred alternatives", text)
                self.assertTrue("fourth image" in text or "more than three images" in text)

        self.assertIn("setup.png", spec)
        self.assertIn("weight-shift.png", spec)
        self.assertIn("muscle-attention.png", spec)
        self.assertIn("media/exercises/tai-chi-basics/", plan)

    def test_tai_chi_first_batch_exact_three_paths_and_purposes_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_tai_chi_image_fixture(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_tai_chi_top_five_exception_allows_fourth_image_but_second_muscle_attention_fails(self) -> None:
        fourth_image_assets = TAI_CHI_ASSETS + (
            (
                "opening",
                "exercise_movement_illustration",
                "Tai Chi opening movement image showing relaxed arms rising",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_tai_chi_image_fixture(root, fourth_image_assets)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        second_muscle_assets = TAI_CHI_ASSETS + (
            (
                "second-muscle-attention",
                "exercise_muscle_attention_illustration",
                "Tai Chi second muscle-attention image showing another broad region",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_tai_chi_image_fixture(root, second_muscle_assets)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_muscle_attention_limit", result.stdout)

    def test_tai_chi_prompt_record_and_alt_text_failures_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            asset_path = "media/exercises/tai-chi-basics/setup.png"
            write_asset(root, asset_path)
            write_provenance(
                root,
                [
                    {
                        "asset_path": asset_path,
                        "media_purpose": "exercise_setup_illustration",
                        "prompt_record": "",
                        "page_refs": "exercises/tai-chi-basics.md",
                    }
                ],
                create_prompt_records=False,
            )
            page = write_exercise_page(root, "![Tai Chi setup image](../media/exercises/tai-chi-basics/setup.png)", slug="tai-chi-basics")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_prompt_record_missing", result.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            asset_path = "media/exercises/tai-chi-basics/setup.png"
            prompt_record = "media/prompts/exercises/tai-chi-basics/setup.md"
            write_asset(root, asset_path)
            write_provenance(
                root,
                [
                    {
                        "asset_path": asset_path,
                        "media_purpose": "exercise_setup_illustration",
                        "prompt_record": prompt_record,
                        "page_refs": "exercises/tai-chi-basics.md",
                    }
                ],
            )
            page = write_exercise_page(root, "![image](../media/exercises/tai-chi-basics/setup.png)", slug="tai-chi-basics")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_alt_text_generic", result.stdout)

    def test_tai_chi_visual_semantic_text_failures_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            asset_path = "media/exercises/tai-chi-basics/weight-shift.png"
            write_asset(root, asset_path)
            write_provenance(
                root,
                [
                    {
                        "asset_path": asset_path,
                        "media_purpose": "exercise_movement_illustration",
                        "prompt_record": "media/prompts/exercises/tai-chi-basics/weight-shift.md",
                        "page_refs": "exercises/tai-chi-basics.md",
                        "prompt_or_creation_notes": "Tai Chi image with red pain warning badge",
                    }
                ],
            )
            page = write_exercise_page(root, "![Tai Chi weight-shift image with calm posture](../media/exercises/tai-chi-basics/weight-shift.png)", slug="tai-chi-basics")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exercise_image_visual_safety_text", result.stdout)

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

    def test_prompt_record_contract_fails_invalid_links_and_files(self) -> None:
        variants = (
            ({"prompt_record": ""}, True, "media_prompt_record_missing"),
            ({"prompt_record": "https://example.com/prompt.md"}, True, "media_prompt_record_invalid"),
            ({"prompt_record": "../prompt.md"}, True, "media_prompt_record_invalid"),
            ({"prompt_record": "media/prompts/exercises/fixture-exercise/setup.txt"}, True, "media_prompt_record_invalid"),
            ({"prompt_record": "media/prompts/fixture-exercise/setup.md"}, True, "media_prompt_record_invalid"),
            ({"prompt_record": "media/prompts/exercises/other-exercise/setup.md"}, True, "media_prompt_record_invalid"),
            ({"prompt_record": "media/prompts/exercises/fixture-exercise/other.md"}, True, "media_prompt_record_invalid"),
            ({}, False, "media_prompt_record_missing"),
        )
        for row, create_prompt_records, expected_code in variants:
            with self.subTest(expected_code=expected_code, row=row), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                write_provenance(root, [row], create_prompt_records=create_prompt_records)
                page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_prompt_record_contract_fails_invalid_content(self) -> None:
        variants = (
            (
                {"asset_path": "media/exercises/fixture-exercise/other.png"},
                "Fixture exact full prompt text for the accepted image.",
                "media_prompt_record_mismatch",
            ),
            (
                {},
                "",
                "media_prompt_record_incomplete",
            ),
            (
                {"human_reviewer": ""},
                "Fixture exact full prompt text for the accepted image.",
                "media_prompt_record_incomplete",
            ),
        )
        for extra_fields, exact_prompt, expected_code in variants:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write_sources(root)
                write_red_flags(root)
                write_asset(root)
                write_provenance(root, [{}], create_prompt_records=False)
                write_prompt_record(root, extra_fields=extra_fields, exact_prompt=exact_prompt)
                page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

                result = run_check_with_root(root, page)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_code, result.stdout)

    def test_prompt_record_contract_accepts_explicit_redaction_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_asset(root)
            write_provenance(root, [{}], create_prompt_records=False)
            write_prompt_record(
                root,
                exact_prompt="",
                extra_fields={"review_status": "approved"},
            )
            prompt_record = root / "media/prompts/exercises/fixture-exercise/setup.md"
            prompt_record.write_text(
                prompt_record.read_text(encoding="utf-8")
                + "\n## Redaction note\n\nPrompt text redacted because it contained private source material.\n",
                encoding="utf-8",
            )
            page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_top_five_named_initiative_allows_blank_reviewer_but_keeps_prompt_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_top_five_reviewer_exception_fixture(root)

            result = run_check_with_root(root, page)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_top_five_reviewer_exception_fixture(root, include_prompt_record=False)

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_prompt_record_missing", result.stdout)

    def test_top_five_reviewer_exception_is_path_scoped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            page = write_top_five_reviewer_exception_fixture(root, slug="fixture-exercise")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_provenance_incomplete", result.stdout)

    def test_media_prompt_records_are_not_checked_as_content_pages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            exercise = root / "exercises/fixture-exercise.md"
            exercise.parent.mkdir(parents=True, exist_ok=True)
            exercise.write_text(
                textwrap.dedent(
                    """\
                    # Fixture Exercise

                    Author: fixture
                    Created: 2026-07-04
                    Last reviewed: 2026-07-04
                    Next review due: 2027-07-04
                    Review scope: fixture prompt-record skip

                    > Disclaimer: GymPrimer is educational content for general exercise literacy.
                    > It is not medical advice and not personalized coaching.

                    ## What this is for

                    A fixture exercise. [Fixture][fixture-training]

                    ## How to do it

                    Move with control. [Fixture][fixture-movement]

                    ## Sources

                    - [Fixture][fixture-training]
                    - [Fixture][fixture-movement]
                    - [Fixture][fixture-setup]

                    [fixture-training]: https://example.org/fixture-training
                    [fixture-movement]: https://example.org/fixture-movement
                    [fixture-setup]: https://example.org/fixture-setup
                    """
                ),
                encoding="utf-8",
            )
            write_prompt_record(
                root,
                exact_prompt="Fixture prompt text may mention no diagnosis symbols in the generated image.",
            )

            result = run_check_with_root(root, root / "exercises", root / "media")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_prompt_record_compatibility_limitation_is_scoped_to_m3_assets(self) -> None:
        compatibility_note = "M3 pre-amendment prompt unavailable; compatibility limitation recorded"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_sources(root)
            write_red_flags(root)
            write_asset(root)
            write_provenance(root, [{"prompt_record": "", "notes": compatibility_note}], create_prompt_records=False)
            page = write_exercise_page(root, "![Fixture exercise setup image](../media/exercises/fixture-exercise/setup.png)")

            result = run_check_with_root(root, page)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("media_prompt_record_missing", result.stdout)

        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        for asset_path in M3_PROMPT_RECORD_COMPATIBILITY_ASSETS:
            rows = provenance.get(asset_path, [])
            with self.subTest(asset_path=asset_path):
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0].get("prompt_record", ""), "")
                self.assertEqual(rows[0].get("notes"), compatibility_note)

        for asset_path in M3_PROMPT_RECORD_REPLACEMENTS:
            rows = provenance.get(asset_path, [])
            slug = asset_path.split("/")[2]
            stem = Path(asset_path).stem
            with self.subTest(asset_path=asset_path):
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0].get("prompt_record", ""), f"media/prompts/exercises/{slug}/{stem}.md")
                self.assertNotEqual(rows[0].get("notes"), compatibility_note)

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

    def test_m3_forward_head_support_batch_has_page_images_and_review_evidence(self) -> None:
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected_assets = {
            "movement": "exercise_movement_illustration",
            "muscle-attention": "exercise_muscle_attention_illustration",
        }
        for slug, alt_texts in M3_TARGETS.items():
            with self.subTest(slug=slug):
                page_path = ROOT / f"exercises/{slug}.md"
                page_text = page_path.read_text(encoding="utf-8")

                for stem, purpose in expected_assets.items():
                    asset_path = f"media/exercises/{slug}/{stem}.png"
                    alt_key = "movement" if stem == "movement" else "muscle"
                    self.assertIn(f"![{alt_texts[alt_key]}](../{asset_path})", page_text)
                    self.assertTrue((ROOT / asset_path).exists(), f"{asset_path} is missing")

                    rows = provenance.get(asset_path, [])
                    self.assertEqual(len(rows), 1, f"{asset_path} must have exactly one provenance row")
                    self.assertEqual(rows[0].get("asset_type"), "ai_generated_raster")
                    self.assertEqual(rows[0].get("media_purpose"), purpose)
                    self.assertEqual(rows[0].get("review_status"), "approved")
                    self.assertIn(f"exercises/{slug}.md", split_page_refs(rows[0].get("page_refs", "")))
                    if rows[0].get("notes") != "M3 pre-amendment prompt unavailable; compatibility limitation recorded":
                        prompt_record = rows[0].get("prompt_record", "")
                        self.assertEqual(prompt_record, f"media/prompts/exercises/{slug}/{stem}.md")
                        self.assertTrue((ROOT / prompt_record).exists(), f"{prompt_record} is missing")

        evidence_root = ROOT / "docs/changes/exercise-image-standard-and-optimization/evidence"
        self.assertTrue((evidence_root / "m3-visual-safety-review.md").exists())
        self.assertTrue((evidence_root / "m3-beginner-comprehension.md").exists())
        self.assertTrue((evidence_root / "m3a-prompt-record-backfill.md").exists())

    def test_tai_chi_m3_support_batch_has_page_images_prompt_records_and_visual_review(self) -> None:
        page_path = ROOT / "exercises/tai-chi-basics.md"
        page_text = page_path.read_text(encoding="utf-8")
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected = {
            "media/exercises/tai-chi-basics/setup.png": (
                "exercise_setup_illustration",
                "Tai Chi setup reference showing relaxed ready stance with soft knees, upright trunk, relaxed shoulders, and natural arms",
            ),
            "media/exercises/tai-chi-basics/weight-shift.png": (
                "exercise_movement_illustration",
                "Tai Chi weight-shift reference showing smooth weight transfer between feet with calm upper body",
            ),
            "media/exercises/tai-chi-basics/muscle-attention.png": (
                "exercise_muscle_attention_illustration",
                "Tai Chi muscle-attention reference with broad highlights on legs, glutes, trunk, shoulders, upper back, feet, and ankles",
            ),
        }

        self.assertEqual(page_text.count("![Tai Chi "), 5)
        self.assertIn("Use these images as broad visual references.", page_text)

        for asset_path, (purpose, alt_text) in expected.items():
            with self.subTest(asset_path=asset_path):
                self.assertIn(f"![{alt_text}](../{asset_path})", page_text)
                self.assertTrue((ROOT / asset_path).is_file())

                rows = provenance.get(asset_path, [])
                self.assertEqual(len(rows), 1)
                row = rows[0]
                self.assertEqual(row.get("asset_type"), "ai_generated_raster")
                self.assertEqual(row.get("media_purpose"), purpose)
                self.assertEqual(row.get("review_status"), "approved")
                self.assertIn("exercises/tai-chi-basics.md", split_page_refs(row.get("page_refs", "")))

                prompt_record = row.get("prompt_record", "")
                self.assertEqual(prompt_record, f"media/prompts/exercises/tai-chi-basics/{Path(asset_path).stem}.md")
                self.assertTrue((ROOT / prompt_record).is_file())

                prompt_text = (ROOT / prompt_record).read_text(encoding="utf-8")
                self.assertIn(f"asset_path: {asset_path}", prompt_text)
                self.assertIn("## Exact prompt", prompt_text)
                self.assertIn("no in-image text", prompt_text.lower())
                self.assertIn("no combat framing", prompt_text.lower())

        visual_safety = ROOT / "docs/changes/2026-07-05-necessary-images-and-tai-chi-exercise/visual-safety-review.md"
        self.assertTrue(visual_safety.is_file())
        visual_text = visual_safety.read_text(encoding="utf-8").lower()
        for token in (
            "media/exercises/tai-chi-basics/setup.png",
            "media/exercises/tai-chi-basics/weight-shift.png",
            "media/exercises/tai-chi-basics/muscle-attention.png",
            "exercise_setup_illustration",
            "exercise_movement_illustration",
            "exercise_muscle_attention_illustration",
            "one concept",
            "matches nearby markdown",
            "no in-image text",
            "no identifiable person",
            "no brand mark",
            "no clinical",
            "no combat",
            "no unsupported claim",
            "color-accessible",
            "broad muscle highlighting",
            "approved",
            "residual risk",
        ):
            with self.subTest(token=token):
                self.assertIn(token, visual_text)

    def test_top_five_m2_first_batch_has_page_images_prompt_records_and_audit_evidence(self) -> None:
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        expected_pages = {
            "band-pull-apart": {
                "expected_count": 4,
                "assets": {
                    "media/exercises/band-pull-apart/setup.png": (
                        "exercise_setup_illustration",
                        "Band pull-apart setup reference with arms forward at chest height and light band slack",
                    ),
                    "media/exercises/band-pull-apart/quiet-ribs-neck.png": (
                        "exercise_movement_illustration",
                        "Band pull-apart posture reference with relaxed neck, quiet ribs, and open arms at chest height",
                    ),
                },
            },
            "bird-dog": {
                "expected_count": 5,
                "assets": {
                    "media/exercises/bird-dog/setup.png": (
                        "exercise_setup_illustration",
                        "Bird dog setup reference on hands and knees with hands under shoulders, knees under hips, and a long spine",
                    ),
                    "media/exercises/bird-dog/level-pelvis-reach.png": (
                        "exercise_movement_illustration",
                        "Bird dog movement reference with opposite arm and leg reaching while the pelvis stays level",
                    ),
                    "media/exercises/bird-dog/short-reach.png": (
                        "exercise_movement_illustration",
                        "Bird dog shorter-reach reference showing a smaller arm and leg reach with a steady trunk",
                    ),
                    "media/exercises/bird-dog/muscle-attention.png": (
                        "exercise_muscle_attention_illustration",
                        "Bird dog muscle-attention reference with broad highlights on glutes, trunk, shoulder support, and hamstring regions",
                    ),
                },
            },
        }

        for slug, expected in expected_pages.items():
            page_path = ROOT / f"exercises/{slug}.md"
            page_text = page_path.read_text(encoding="utf-8")
            self.assertEqual(page_text.count(f"](../media/exercises/{slug}/"), expected["expected_count"])

            for asset_path, (purpose, alt_text) in expected["assets"].items():
                with self.subTest(asset_path=asset_path):
                    self.assertIn(f"![{alt_text}](../{asset_path})", page_text)
                    self.assertTrue((ROOT / asset_path).is_file())

                    rows = provenance.get(asset_path, [])
                    self.assertEqual(len(rows), 1)
                    row = rows[0]
                    self.assertEqual(row.get("asset_type"), "ai_generated_raster")
                    self.assertEqual(row.get("media_purpose"), purpose)
                    self.assertEqual(row.get("human_reviewer"), "")
                    self.assertEqual(row.get("review_status"), "approved")
                    self.assertIn(f"exercises/{slug}.md", split_page_refs(row.get("page_refs", "")))

                    prompt_record = row.get("prompt_record", "")
                    self.assertEqual(prompt_record, f"media/prompts/exercises/{slug}/{Path(asset_path).stem}.md")
                    self.assertTrue((ROOT / prompt_record).is_file())

                    prompt_text = (ROOT / prompt_record).read_text(encoding="utf-8")
                    self.assertIn(f"asset_path: {asset_path}", prompt_text)
                    self.assertIn("## Exact prompt", prompt_text)
                    self.assertIn("no text", prompt_text.lower())
                    self.assertIn("no labels", prompt_text.lower())

        audit_path = ROOT / "docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m2-first-batch-audit.md"
        audit_text = audit_path.read_text(encoding="utf-8")
        self.assertIn("Scores use 1-5 values", audit_text)
        self.assertNotIn("Scores use 0-3 values", audit_text)
        score_rows = [
            row
            for row in audit_text.splitlines()
            if re.match(r"\| \d+ \|", row)
        ]
        self.assertGreaterEqual(len(score_rows), 20)
        for row in score_rows:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            scores = [int(value) for value in cells[2:7]]
            with self.subTest(row=row):
                self.assertTrue(all(1 <= score <= 5 for score in scores))
                self.assertNotIn(0, scores)

        for token in (
            "`exercises/band-pull-apart.md`",
            "`exercises/bird-dog.md`",
            "Coverage-limit outcome",
            "beginner_comprehension",
            "setup_value",
            "muscle_attention_value",
            "page_value",
            "readiness",
            "Generated chest-height path candidate",
            "rejected_duplicate_coverage",
        ):
            with self.subTest(token=token):
                self.assertIn(token, audit_text)

    def test_top_five_m3_remaining_batch_has_page_images_prompt_records_and_audit_evidence(self) -> None:
        provenance = load_media_provenance(ROOT / "media/PROVENANCE.md")
        audit_path = ROOT / "docs/changes/2026-07-06-top-five-generated-images-for-fewer-than-five-exercise-documents/evidence/m3-remaining-batch-audit.md"
        self.assertTrue(audit_path.is_file())
        audit_text = audit_path.read_text(encoding="utf-8")
        self.assertIn("Scores use 1-5 values", audit_text)
        self.assertNotIn("Scores use 0-3 values", audit_text)
        self.assertIn("Rollback proof", audit_text)
        self.assertIn("beginner_comprehension", audit_text)
        self.assertIn("setup_value", audit_text)
        self.assertIn("muscle_attention_value", audit_text)
        self.assertIn("page_value", audit_text)
        self.assertIn("readiness", audit_text)

        score_rows = [
            row
            for row in audit_text.splitlines()
            if re.match(r"\| \d+ \|", row)
        ]
        self.assertGreaterEqual(len(score_rows), 160)
        for row in score_rows:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            scores = [int(value) for value in cells[2:7]]
            with self.subTest(row=row):
                self.assertTrue(all(1 <= score <= 5 for score in scores))
                self.assertNotIn(0, scores)

        for slug, expected in TOP_FIVE_M3_ASSETS.items():
            with self.subTest(slug=slug):
                page_path = ROOT / f"exercises/{slug}.md"
                page_text = page_path.read_text(encoding="utf-8")
                self.assertEqual(page_text.count(f"](../media/exercises/{slug}/"), expected["expected_count"])
                muscle_assets = [
                    path
                    for path, (purpose, _alt_text) in expected["assets"].items()
                    if purpose == "exercise_muscle_attention_illustration"
                ]
                page_assets = re.findall(r"\]\(\.\./(media/exercises/[^)]+)\)", page_text)
                page_muscle_count = sum(
                    1
                    for asset_path in page_assets
                    for row in provenance.get(asset_path, [])
                    if row.get("media_purpose") == "exercise_muscle_attention_illustration"
                )
                self.assertLessEqual(page_muscle_count, 1)

                for asset_path, (purpose, alt_text) in expected["assets"].items():
                    self.assertIn(f"![{alt_text}](../{asset_path})", page_text)
                    self.assertTrue((ROOT / asset_path).is_file())
                    rows = provenance.get(asset_path, [])
                    self.assertEqual(len(rows), 1)
                    row = rows[0]
                    self.assertEqual(row.get("asset_type"), "ai_generated_raster")
                    self.assertEqual(row.get("media_purpose"), purpose)
                    self.assertEqual(row.get("human_reviewer"), "")
                    self.assertEqual(row.get("review_status"), "approved")
                    self.assertIn(f"exercises/{slug}.md", split_page_refs(row.get("page_refs", "")))
                    prompt_record = row.get("prompt_record", "")
                    self.assertEqual(prompt_record, f"media/prompts/exercises/{slug}/{Path(asset_path).stem}.md")
                    self.assertTrue((ROOT / prompt_record).is_file())
                    prompt_text = (ROOT / prompt_record).read_text(encoding="utf-8")
                    self.assertIn(f"asset_path: {asset_path}", prompt_text)
                    self.assertIn("## Exact prompt", prompt_text)

                self.assertIn(f"`exercises/{slug}.md`", audit_text)
                for asset_path in expected["assets"]:
                    self.assertIn(Path(asset_path).name, audit_text)

    def test_m4_exercise_audit_covers_current_exercise_pages(self) -> None:
        audit_path = ROOT / "docs/changes/exercise-image-standard-and-optimization/evidence/m4-exercise-audit.md"
        audit_text = audit_path.read_text(encoding="utf-8")
        exercise_pages = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "exercises").glob("*.md"))

        for page in exercise_pages:
            with self.subTest(page=page):
                self.assertIn(f"`{page}`", audit_text)

        self.assertIn("Do not edit an exercise page solely to migrate", audit_text)


if __name__ == "__main__":
    unittest.main()
