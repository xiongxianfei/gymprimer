import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "tools" / "validation" / "validate_content.py"


def valid_card() -> dict:
    return {
        "schema_version": "content-schema-v1",
        "card_id": "ex-lat-pulldown",
        "version_id": "v1",
        "card_type": "exercise",
        "review_status": "approved",
        "publication_status": "published",
        "difficulty": "beginner",
        "safety_category": "standard",
        "equipment": ["selectorized_machine"],
        "movement_patterns": ["pull_vertical"],
        "primary_muscles": ["latissimus_dorsi"],
        "secondary_muscles": ["biceps_brachii"],
        "stabilizers": ["core"],
        "canonical_svg_steps": [
            "examples/lat-pulldown-step-1.svg",
            "examples/lat-pulldown-step-2.svg",
            "examples/lat-pulldown-step-3.svg",
        ],
        "supplemental_media": [],
        "license": {
            "code_license": "Apache-2.0",
            "content_license": "CC-BY-4.0",
            "license_kind": "cc_by",
            "attribution": "GymPrimer contributors",
        },
        "contribution_provenance": "staff_authored_expert_reviewed",
        "review": {
            "reviewer_public_id": "trainer-reviewer-a",
            "review_tier": "trainer",
            "review_date": "2026-06-27",
            "content_digest": "sha256:test-digest",
        },
        "locales": {
            "en-US": {
                "title": "Lat pulldown",
                "aliases": ["Front lat pulldown"],
                "summary": "A beginner pull exercise for learning how to train the upper back.",
                "purpose": "Teach a controlled vertical pulling pattern with machine support.",
                "equipment_setup": ["Adjust the thigh pad so your legs stay down without discomfort."],
                "start_position": "Sit tall, hold the bar just wider than shoulder width, and keep your ribs stacked.",
                "movement_phases": [
                    "Pull the bar toward the upper chest with controlled tempo.",
                    "Pause briefly without shrugging.",
                    "Return the bar upward under control.",
                ],
                "breathing_bracing": "Exhale as you pull and inhale as you return.",
                "common_mistakes": ["Leaning far back instead of pulling with control."],
                "regressions": ["Use a lighter pin setting and a shorter range you can control."],
                "progressions": [
                    {
                        "title": "Slower return",
                        "readiness_cue": "Use this only after you can keep the shoulders controlled for every rep.",
                    }
                ],
                "what_you_should_feel": ["Work through the sides of the upper back."],
                "what_you_should_not_feel": ["Sharp, radiating, worsening, or unusual symptoms."],
                "safety_notes": [
                    "GymPrimer is educational content, not medical advice. Talk to a qualified professional before starting a new exercise program; stop and seek qualified help for sharp, radiating, worsening, or unusual symptoms."
                ],
                "canonical_svg_text": {
                    "examples/lat-pulldown-step-1.svg": "Start seated with the bar overhead.",
                    "examples/lat-pulldown-step-2.svg": "Pull the bar toward the upper chest.",
                    "examples/lat-pulldown-step-3.svg": "Return the bar upward with control.",
                },
            }
        },
    }


def zh_hans_locale() -> dict:
    return {
        "title": "高位下拉",
        "aliases": ["前侧高位下拉"],
        "summary": "面向初学者的上背部下拉练习。",
        "purpose": "学习受控的垂直拉动作。",
        "equipment_setup": ["调整大腿垫，让腿部稳定但不过度挤压。"],
        "start_position": "坐直，双手略宽于肩握住把手。",
        "movement_phases": ["将把手拉向上胸。", "短暂停留。", "受控还原。"],
        "breathing_bracing": "下拉时呼气，还原时吸气。",
        "common_mistakes": ["身体过度后仰。"],
        "regressions": ["降低重量。"],
        "progressions": [{"title": "慢速还原", "readiness_cue": "全程能保持肩部稳定后再尝试。"}],
        "what_you_should_feel": ["上背部两侧发力。"],
        "what_you_should_not_feel": ["尖锐、放射、加重或异常症状。"],
        "safety_notes": [
            "GymPrimer is educational content, not medical advice. Talk to a qualified professional before starting a new exercise program; stop and seek qualified help for sharp, radiating, worsening, or unusual symptoms."
        ],
        "canonical_svg_text": {
            "examples/lat-pulldown-step-1.svg": "坐姿起始位。",
            "examples/lat-pulldown-step-2.svg": "向上胸方向下拉。",
            "examples/lat-pulldown-step-3.svg": "受控还原。",
        },
    }


def valid_supplemental_media() -> dict:
    return {
        "media_kind": "video",
        "license_kind": "cc_by",
        "authoritative_status": "supplemental",
        "title": "Lat pulldown side-view demonstration",
        "caption": "Supplemental demonstration of the reviewed setup and movement phases.",
    }


class ContentContractM2Tests(unittest.TestCase):
    def run_validator(self, source: Path, *extra: str) -> tuple[subprocess.CompletedProcess[str], dict]:
        report_dir = Path(tempfile.mkdtemp(prefix="gymprimer-validator-test-"))
        self.addCleanup(shutil.rmtree, report_dir)
        out = report_dir / "validation-report.json"
        cmd = [
            sys.executable,
            str(VALIDATOR),
            "--source",
            str(source),
            "--schemas",
            str(REPO_ROOT / "schemas"),
            "--media",
            str(REPO_ROOT / "media"),
            "--out",
            str(out),
            *extra,
        ]
        result = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
        report = json.loads(out.read_text(encoding="utf-8"))
        return result, report

    def write_card(self, root: Path, card: dict, name: str = "card.json") -> None:
        cards = root / "cards"
        cards.mkdir(parents=True, exist_ok=True)
        (cards / name).write_text(json.dumps(card, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def assert_invalid(self, mutation, expected_code: str):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            card = valid_card()
            mutation(card)
            self.write_card(source, card)

            result, report = self.run_validator(source)

            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(report["status"], "fail")
            self.assertIn(expected_code, {finding["code"] for finding in report["findings"]})

    def test_repo_example_card_validates(self):
        result, report = self.run_validator(REPO_ROOT / "content")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["status"], "pass")
        self.assertGreaterEqual(report["counts"]["valid_cards"], 1)
        self.assertEqual(report["counts"]["invalid_cards"], 0)

    def test_valid_en_us_card_shape_is_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            self.write_card(source, valid_card())

            result, report = self.run_validator(source)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(report["status"], "pass")
            self.assertEqual(report["counts"]["valid_cards"], 1)
            self.assertEqual(report["findings"], [])

    def test_zh_hans_branch_uses_same_required_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            card = valid_card()
            card["locales"]["zh-Hans"] = zh_hans_locale()
            self.write_card(source, card)

            result, report = self.run_validator(source)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(report["status"], "pass")

    def test_bare_en_locale_is_rejected(self):
        self.assert_invalid(
            lambda card: card["locales"].__setitem__("en", card["locales"].pop("en-US")),
            "locale_unknown",
        )

    def test_publishable_card_requires_en_us(self):
        self.assert_invalid(
            lambda card: card["locales"].pop("en-US"),
            "required_locale_missing",
        )

    def test_en_and_en_us_conflict_requires_manual_migration(self):
        self.assert_invalid(
            lambda card: card["locales"].__setitem__("en", copy.deepcopy(card["locales"]["en-US"])),
            "locale_migration_conflict",
        )

    def test_future_english_variant_requires_taxonomy_extension(self):
        self.assert_invalid(
            lambda card: card["locales"].__setitem__("en-GB", copy.deepcopy(card["locales"]["en-US"])),
            "locale_unknown",
        )

    def test_unknown_controlled_enum_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__("difficulty", "novice"),
            "enum_unknown",
        )

    def test_unknown_taxonomy_id_is_rejected(self):
        self.assert_invalid(
            lambda card: card["equipment"].append("mystery_machine"),
            "taxonomy_unknown",
        )

    def test_too_few_svg_steps_are_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__("canonical_svg_steps", card["canonical_svg_steps"][:2]),
            "canonical_svg_step_count",
        )

    def test_too_many_svg_steps_are_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "canonical_svg_steps",
                [
                    "examples/lat-pulldown-step-1.svg",
                    "examples/lat-pulldown-step-2.svg",
                    "examples/lat-pulldown-step-3.svg",
                    "examples/lat-pulldown-step-4.svg",
                    "examples/lat-pulldown-step-5.svg",
                    "examples/lat-pulldown-step-6.svg",
                    "examples/lat-pulldown-step-7.svg",
                ],
            ),
            "canonical_svg_step_count",
        )

    def test_missing_svg_accessible_text_is_rejected(self):
        self.assert_invalid(
            lambda card: card["locales"]["en-US"]["canonical_svg_text"].pop("examples/lat-pulldown-step-1.svg"),
            "media_accessible_text_missing",
        )

    def test_diagnosis_or_treatment_claim_is_rejected(self):
        self.assert_invalid(
            lambda card: card["locales"]["en-US"].__setitem__(
                "summary",
                "This exercise treats shoulder injury and diagnoses movement problems.",
            ),
            "diagnosis_treatment_claim",
        )

    def test_missing_disclaimer_is_rejected(self):
        self.assert_invalid(
            lambda card: card["locales"]["en-US"].__setitem__("safety_notes", ["Use controlled reps."]),
            "disclaimer_missing",
        )

    def test_unlicensed_internal_only_asset_is_rejected(self):
        self.assert_invalid(
            lambda card: card["license"].__setitem__("license_kind", "unlicensed_internal_only"),
            "license_not_public",
        )

    def test_public_card_rejects_internal_only_supplemental_media_asset(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [
                    {
                        **valid_supplemental_media(),
                        "license_kind": "unlicensed_internal_only",
                    }
                ],
            ),
            "license_not_public",
        )

    def test_supplemental_media_missing_media_kind_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{key: value for key, value in valid_supplemental_media().items() if key != "media_kind"}],
            ),
            "supplemental_media_missing_media_kind",
        )

    def test_supplemental_media_missing_license_kind_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{key: value for key, value in valid_supplemental_media().items() if key != "license_kind"}],
            ),
            "supplemental_media_missing_license_kind",
        )

    def test_supplemental_media_unknown_media_kind_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{**valid_supplemental_media(), "media_kind": "hologram"}],
            ),
            "unknown_media_kind",
        )

    def test_supplemental_media_unknown_license_kind_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{**valid_supplemental_media(), "license_kind": "cc_by_4_0"}],
            ),
            "unknown_license_kind",
        )

    def test_supplemental_media_source_of_truth_claim_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{**valid_supplemental_media(), "authoritative_status": "canonical"}],
            ),
            "supplemental_media_not_authoritative",
        )

    def test_supplemental_media_boolean_source_of_truth_claim_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [{**valid_supplemental_media(), "is_source_of_truth": True}],
            ),
            "supplemental_media_not_authoritative",
        )

    def test_supplemental_media_override_language_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__(
                "supplemental_media",
                [
                    {
                        **valid_supplemental_media(),
                        "caption": "This video replaces the canonical SVG steps.",
                    }
                ],
            ),
            "supplemental_media_overrides_canonical_steps",
        )

    def test_valid_supplemental_media_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            card = valid_card()
            card["supplemental_media"] = [valid_supplemental_media()]
            self.write_card(source, card)

            result, report = self.run_validator(source)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(report["status"], "pass")
            self.assertEqual(report["counts"]["valid_cards"], 1)

    def test_user_submitted_unreviewed_is_rejected(self):
        self.assert_invalid(
            lambda card: card.__setitem__("contribution_provenance", "user_submitted_unreviewed"),
            "expert_review_required",
        )

    def test_missing_public_review_metadata_is_rejected(self):
        self.assert_invalid(
            lambda card: card.pop("review"),
            "review_metadata_missing",
        )

    def test_expect_invalid_command_succeeds_for_invalid_fixture_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "invalid-fixture-report.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--source",
                    str(REPO_ROOT / "tests" / "fixtures" / "invalid"),
                    "--schemas",
                    str(REPO_ROOT / "schemas"),
                    "--media",
                    str(REPO_ROOT / "media"),
                    "--out",
                    str(out),
                    "--expect-invalid",
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "fail")
            self.assertGreaterEqual(report["counts"]["invalid_cards"], 1)

    def test_fixtures_and_report_aliases_are_supported(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "fixture-source"
            report_path = Path(tmp) / "report.json"
            self.write_card(source, valid_card())

            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--fixtures",
                    str(source),
                    "--schemas",
                    str(REPO_ROOT / "schemas"),
                    "--media",
                    str(REPO_ROOT / "media"),
                    "--report",
                    str(report_path),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(report_path.read_text(encoding="utf-8"))["status"], "pass")


if __name__ == "__main__":
    unittest.main()
