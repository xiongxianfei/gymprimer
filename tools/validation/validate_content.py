#!/usr/bin/env python3
"""Validate repository-native GymPrimer content cards."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_SCHEMA_VERSION = "content-schema-v1"
CARD_SUFFIXES = {".json"}

CONTROLLED_ENUMS: dict[str, set[str]] = {
    "card_type": {
        "exercise",
        "equipment_guide",
        "movement_pattern",
        "training_principle",
        "safety_policy",
        "glossary",
    },
    "difficulty": {"beginner", "beginner_plus", "intermediate", "advanced"},
    "safety_category": {"standard", "caution", "elevated_risk", "blocked_rehab", "policy_only"},
    "review_status": {"draft", "in_review", "changes_requested", "approved", "review_expired"},
    "publication_status": {"unpublished", "published", "hidden", "superseded"},
    "review_tier": {
        "trainer",
        "strength_coach",
        "physical_therapist",
        "sports_medicine_clinician",
        "schema_owner",
        "locale_reviewer",
        "content_ops",
        "legal_policy",
    },
    "locale": {"en-US", "zh-Hans"},
    "contribution_provenance": {
        "expert_authored",
        "staff_authored_expert_reviewed",
        "ai_assisted_expert_reviewed",
        "imported_licensed_expert_reviewed",
        "user_submitted_unreviewed",
    },
    "media_kind": {"video", "image", "diagram", "animation", "thumbnail", "caption_file", "transcript", "audio"},
    "license_kind": {
        "owned",
        "third_party_licensed",
        "cc_by",
        "cc_by_sa",
        "public_domain",
        "unlicensed_internal_only",
    },
    "movement_pattern": {
        "squat",
        "hinge",
        "lunge",
        "push_horizontal",
        "push_vertical",
        "pull_horizontal",
        "pull_vertical",
        "carry",
        "brace_anti_extension",
        "brace_anti_rotation",
        "rotation",
        "locomotion",
        "cardio_rowing",
        "cardio_cycling",
        "cardio_running",
        "mobility",
    },
    "equipment_kind": {
        "bodyweight",
        "dumbbell",
        "barbell",
        "kettlebell",
        "cable_machine",
        "selectorized_machine",
        "bench",
        "resistance_band",
        "rowing_machine",
        "stationary_bike",
        "treadmill",
        "mat",
        "sled",
        "pullup_assist_machine",
    },
}

DEFAULT_MUSCLES = {
    "latissimus_dorsi",
    "biceps_brachii",
    "posterior_deltoid",
    "pectoralis_major",
    "quadriceps",
    "hamstrings",
    "gluteus_maximus",
    "gluteus_medius",
    "hip_flexors",
    "core",
}

LOCALIZED_REQUIRED_FIELDS = {
    "title",
    "aliases",
    "summary",
    "purpose",
    "equipment_setup",
    "start_position",
    "movement_phases",
    "breathing_bracing",
    "common_mistakes",
    "regressions",
    "progressions",
    "what_you_should_feel",
    "what_you_should_not_feel",
    "safety_notes",
    "canonical_svg_text",
}

TOP_LEVEL_REQUIRED_FIELDS = {
    "schema_version",
    "card_id",
    "version_id",
    "card_type",
    "review_status",
    "publication_status",
    "difficulty",
    "safety_category",
    "equipment",
    "movement_patterns",
    "primary_muscles",
    "secondary_muscles",
    "stabilizers",
    "canonical_svg_steps",
    "license",
    "contribution_provenance",
    "locales",
}

DISCLAIMER_TEXT = (
    "GymPrimer is educational content, not medical advice. Talk to a qualified professional before starting a new "
    "exercise program; stop and seek qualified help for sharp, radiating, worsening, or unusual symptoms."
)

DIAGNOSIS_OR_TREATMENT_PATTERN = re.compile(
    r"\b(diagnose|diagnoses|diagnosis|treat|treats|treatment|cure|cures|rehab|rehabilitate|rehabilitation)\b",
    re.IGNORECASE,
)

PROHIBITED_PERSONALIZATION_FIELDS = {
    "personalized_workout_plan",
    "user_profile",
    "medical_screening_results",
    "injury_diagnosis",
    "rehab_protocol",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate GymPrimer source content.")
    parser.add_argument("--source", help="Content source directory.")
    parser.add_argument("--fixtures", help="Fixture source directory. Alias for --source.")
    parser.add_argument("--schemas", required=True, help="Schema directory.")
    parser.add_argument("--media", required=True, help="Media directory.")
    parser.add_argument("--out", help="Validation report output path.")
    parser.add_argument("--report", help="Validation report output path. Alias for --out.")
    parser.add_argument(
        "--expect-invalid",
        action="store_true",
        help="Exit 0 only when validation completes and at least one content finding is produced.",
    )
    return parser


def schema_version(schemas: Path) -> str:
    version_file = schemas / "content-schema-version.txt"
    if version_file.exists():
        version = version_file.read_text(encoding="utf-8").strip()
        return version or DEFAULT_SCHEMA_VERSION

    report_schema = schemas / "validation-report.schema.json"
    if report_schema.exists():
        try:
            data = json.loads(report_schema.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return DEFAULT_SCHEMA_VERSION
        value = data.get("schema_version")
        if isinstance(value, str) and value:
            return value

    return DEFAULT_SCHEMA_VERSION


def base_report(version: str, status: str) -> dict[str, Any]:
    return {
        "schema_version": version,
        "status": status,
        "counts": {
            "valid_cards": 0,
            "invalid_cards": 0,
            "warnings": 0,
            "review_sensitive_changes": 0,
        },
        "findings": [],
        "warnings": [],
        "privacy": {
            "pii_required": False,
            "sensitive_data_allowed": False,
            "absolute_paths_redacted": True,
        },
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def missing_path_finding(role: str) -> dict[str, str]:
    return {
        "code": "missing_path",
        "path_role": role,
        "message": f"Required {role} path does not exist.",
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_taxonomy(source: Path) -> dict[str, set[str]]:
    taxonomy = {key: set(values) for key, values in CONTROLLED_ENUMS.items()}
    taxonomy["muscles"] = set(DEFAULT_MUSCLES)

    candidates = [
        source / "taxonomy" / "v1.json",
        source / "content" / "taxonomy" / "v1.json",
        Path.cwd() / "content" / "taxonomy" / "v1.json",
    ]
    for candidate in candidates:
        if not candidate.exists():
            continue
        try:
            data = load_json(candidate)
        except (json.JSONDecodeError, OSError):
            continue
        for key, value in data.items():
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                taxonomy[key] = set(value)
        break

    return taxonomy


def discover_card_files(source: Path) -> list[Path]:
    return sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and path.suffix.lower() in CARD_SUFFIXES and "cards" in path.parts
    )


def is_public(card: dict[str, Any]) -> bool:
    return card.get("publication_status") == "published" or card.get("publishable") is True


def finding(code: str, card_id: str, field: str, message: str, locale: str | None = None) -> dict[str, str]:
    item = {
        "code": code,
        "card_id": card_id,
        "field": field,
        "message": message,
    }
    if locale is not None:
        item["locale"] = locale
    return item


def is_nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def iter_text(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        texts: list[str] = []
        for item in value:
            texts.extend(iter_text(item))
        return texts
    if isinstance(value, dict):
        texts = []
        for item in value.values():
            texts.extend(iter_text(item))
        return texts
    return []


def validate_enum(
    card: dict[str, Any],
    findings: list[dict[str, str]],
    taxonomy: dict[str, set[str]],
    card_id: str,
    field: str,
    enum_name: str | None = None,
) -> None:
    enum_key = enum_name or field
    value = card.get(field)
    if value is None:
        return
    if not isinstance(value, str) or value not in taxonomy.get(enum_key, set()):
        findings.append(finding("enum_unknown", card_id, field, f"Unknown controlled value for {field}."))


def validate_string_list_taxonomy(
    card: dict[str, Any],
    findings: list[dict[str, str]],
    taxonomy: dict[str, set[str]],
    card_id: str,
    field: str,
    taxonomy_key: str,
) -> None:
    values = card.get(field)
    if not isinstance(values, list) or not values:
        findings.append(finding("required_field_missing", card_id, field, f"{field} must be a nonempty list."))
        return
    allowed = taxonomy.get(taxonomy_key, set())
    for value in values:
        if not isinstance(value, str) or value not in allowed:
            findings.append(finding("taxonomy_unknown", card_id, field, f"Unknown taxonomy id in {field}."))


def validate_locale(
    locale: str,
    branch: Any,
    card: dict[str, Any],
    findings: list[dict[str, str]],
    card_id: str,
) -> None:
    if not isinstance(branch, dict):
        findings.append(finding("locale_branch_invalid", card_id, f"locales.{locale}", "Locale branch must be an object.", locale))
        return

    for field_name in sorted(LOCALIZED_REQUIRED_FIELDS):
        if not is_nonempty(branch.get(field_name)):
            findings.append(
                finding(
                    "required_localized_field_missing",
                    card_id,
                    f"locales.{locale}.{field_name}",
                    f"Required localized field {field_name} is missing.",
                    locale,
                )
            )

    accessible_text = branch.get("canonical_svg_text")
    svg_steps = card.get("canonical_svg_steps", [])
    if isinstance(accessible_text, dict) and isinstance(svg_steps, list):
        for step in svg_steps:
            if not isinstance(step, str) or not is_nonempty(accessible_text.get(step)):
                findings.append(
                    finding(
                        "media_accessible_text_missing",
                        card_id,
                        f"locales.{locale}.canonical_svg_text",
                        "Every canonical SVG step needs accessible text in each published locale.",
                        locale,
                    )
                )

    safety_notes = branch.get("safety_notes", [])
    if is_public(card) and DISCLAIMER_TEXT not in "\n".join(iter_text(safety_notes)):
        findings.append(
            finding(
                "disclaimer_missing",
                card_id,
                f"locales.{locale}.safety_notes",
                "Public content requires the approved educational disclaimer.",
                locale,
            )
        )

    combined_text = "\n".join(iter_text(branch))
    if DIAGNOSIS_OR_TREATMENT_PATTERN.search(combined_text):
        findings.append(
            finding(
                "diagnosis_treatment_claim",
                card_id,
                f"locales.{locale}",
                "Content must not claim diagnosis, treatment, cure, or rehabilitation.",
                locale,
            )
        )


def validate_card(card: dict[str, Any], taxonomy: dict[str, set[str]], media: Path) -> list[dict[str, str]]:
    card_id = str(card.get("card_id") or "unknown-card")
    findings: list[dict[str, str]] = []

    for field_name in sorted(TOP_LEVEL_REQUIRED_FIELDS):
        if not is_nonempty(card.get(field_name)):
            findings.append(finding("required_field_missing", card_id, field_name, f"Required field {field_name} is missing."))

    for prohibited in sorted(PROHIBITED_PERSONALIZATION_FIELDS):
        if prohibited in card:
            findings.append(
                finding(
                    "prohibited_personalization_field",
                    card_id,
                    prohibited,
                    "Content cards must not collect user-specific screening, advice, or program fields.",
                )
            )

    validate_enum(card, findings, taxonomy, card_id, "card_type")
    validate_enum(card, findings, taxonomy, card_id, "difficulty")
    validate_enum(card, findings, taxonomy, card_id, "safety_category")
    validate_enum(card, findings, taxonomy, card_id, "review_status")
    validate_enum(card, findings, taxonomy, card_id, "publication_status")
    validate_enum(card, findings, taxonomy, card_id, "contribution_provenance")

    validate_string_list_taxonomy(card, findings, taxonomy, card_id, "equipment", "equipment_kind")
    validate_string_list_taxonomy(card, findings, taxonomy, card_id, "movement_patterns", "movement_pattern")
    validate_string_list_taxonomy(card, findings, taxonomy, card_id, "primary_muscles", "muscles")
    validate_string_list_taxonomy(card, findings, taxonomy, card_id, "secondary_muscles", "muscles")
    validate_string_list_taxonomy(card, findings, taxonomy, card_id, "stabilizers", "muscles")

    locales = card.get("locales")
    if not isinstance(locales, dict) or not locales:
        findings.append(finding("required_field_missing", card_id, "locales", "Card requires locale branches."))
        if is_public(card):
            findings.append(
                finding(
                    "required_locale_missing",
                    card_id,
                    "locales.en-US",
                    "Public content requires the en-US locale branch.",
                )
            )
    else:
        if "en" in locales and "en-US" in locales:
            findings.append(
                finding(
                    "locale_migration_conflict",
                    card_id,
                    "locales",
                    "Bare en and en-US cannot coexist; migration requires manual resolution.",
                )
            )
        for locale, branch in sorted(locales.items()):
            if locale not in taxonomy.get("locale", set()):
                findings.append(finding("locale_unknown", card_id, f"locales.{locale}", "Unknown v1 locale key.", locale))
                continue
            validate_locale(locale, branch, card, findings, card_id)
        if is_public(card) and "en-US" not in locales:
            findings.append(
                finding(
                    "required_locale_missing",
                    card_id,
                    "locales.en-US",
                    "Public content requires the en-US locale branch.",
                )
            )

    svg_steps = card.get("canonical_svg_steps")
    if not isinstance(svg_steps, list) or not 3 <= len(svg_steps) <= 6:
        findings.append(
            finding(
                "canonical_svg_step_count",
                card_id,
                "canonical_svg_steps",
                "Canonical SVG cards require three to six steps.",
            )
        )
    elif any(not isinstance(step, str) or not step.endswith(".svg") for step in svg_steps):
        findings.append(
            finding("canonical_svg_reference_invalid", card_id, "canonical_svg_steps", "Canonical SVG references must be SVG paths.")
        )
    else:
        for step in svg_steps:
            if not (media / "svg" / step).exists():
                findings.append(
                    finding(
                        "canonical_svg_missing",
                        card_id,
                        "canonical_svg_steps",
                        "Canonical SVG reference is missing from media/svg.",
                    )
                )

    license_info = card.get("license")
    if not isinstance(license_info, dict):
        findings.append(finding("license_metadata_missing", card_id, "license", "License metadata is required."))
    else:
        license_kind = license_info.get("license_kind")
        if not isinstance(license_kind, str) or license_kind not in taxonomy.get("license_kind", set()):
            findings.append(finding("enum_unknown", card_id, "license.license_kind", "Unknown license kind."))
        if is_public(card) and license_kind == "unlicensed_internal_only":
            findings.append(finding("license_not_public", card_id, "license.license_kind", "Public cards cannot use internal-only rights."))
        for required in ("code_license", "content_license", "attribution"):
            if is_public(card) and not is_nonempty(license_info.get(required)):
                findings.append(finding("license_metadata_missing", card_id, f"license.{required}", "Public license metadata is incomplete."))

    if is_public(card) and card.get("contribution_provenance") == "user_submitted_unreviewed":
        findings.append(
            finding(
                "expert_review_required",
                card_id,
                "contribution_provenance",
                "Unreviewed user-submitted content cannot be published.",
            )
        )

    progressions = []
    if isinstance(locales, dict):
        branch = locales.get("en-US")
        if isinstance(branch, dict) and isinstance(branch.get("progressions"), list):
            progressions = branch["progressions"]
    for index, progression in enumerate(progressions):
        if not isinstance(progression, dict) or not is_nonempty(progression.get("readiness_cue")):
            findings.append(
                finding(
                    "progression_readiness_missing",
                    card_id,
                    f"locales.en-US.progressions[{index}]",
                    "Progressions require beginner-readable readiness cues.",
                )
            )

    if is_public(card):
        review = card.get("review")
        if not isinstance(review, dict):
            findings.append(finding("review_metadata_missing", card_id, "review", "Public cards require review metadata."))
        else:
            for required in ("reviewer_public_id", "review_tier", "review_date", "content_digest"):
                if not is_nonempty(review.get(required)):
                    findings.append(finding("review_metadata_missing", card_id, f"review.{required}", "Public review metadata is incomplete."))
            tier = review.get("review_tier")
            if isinstance(tier, str) and tier not in taxonomy.get("review_tier", set()):
                findings.append(finding("enum_unknown", card_id, "review.review_tier", "Unknown review tier."))

    return findings


def validate(args: argparse.Namespace) -> int:
    source_arg = args.source or args.fixtures
    out_arg = args.out or args.report or "generated/validation-report.json"
    source = Path(source_arg) if source_arg else Path("__missing_source__")
    schemas = Path(args.schemas)
    media = Path(args.media)
    out = Path(out_arg)

    version = schema_version(schemas) if schemas.exists() else DEFAULT_SCHEMA_VERSION
    report = base_report(version, "pass")

    missing_roles = [
        role
        for role, path in (("source", source), ("schemas", schemas), ("media", media))
        if not path.exists()
    ]
    if missing_roles:
        report["status"] = "error"
        report["findings"] = [missing_path_finding(role) for role in missing_roles]
        write_report(out, report)
        return 2

    taxonomy = load_taxonomy(source)
    card_files = discover_card_files(source)
    if not card_files:
        report["warnings"].append(
            {
                "code": "no_cards_found",
                "message": "No content card files were found under the source path.",
            }
        )
        report["counts"]["warnings"] = 1

    for card_file in card_files:
        try:
            card = load_json(card_file)
        except json.JSONDecodeError:
            report["findings"].append(finding("json_invalid", "unknown-card", card_file.name, "Card JSON is invalid."))
            report["counts"]["invalid_cards"] += 1
            continue

        if not isinstance(card, dict):
            report["findings"].append(finding("card_invalid", "unknown-card", card_file.name, "Card file must contain a JSON object."))
            report["counts"]["invalid_cards"] += 1
            continue

        card_findings = validate_card(card, taxonomy, media)
        if card_findings:
            report["counts"]["invalid_cards"] += 1
            report["findings"].extend(card_findings)
        else:
            report["counts"]["valid_cards"] += 1

    if report["findings"]:
        report["status"] = "fail"

    write_report(out, report)

    if args.expect_invalid:
        return 0 if report["status"] == "fail" and report["findings"] else 1
    return 1 if report["status"] == "fail" else 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return validate(args)
    except OSError as exc:
        out = Path(args.out)
        report = base_report(DEFAULT_SCHEMA_VERSION, "error")
        report["findings"] = [
            {
                "code": "io_error",
                "message": exc.__class__.__name__,
            }
        ]
        write_report(out, report)
        return 2


if __name__ == "__main__":
    sys.exit(main())
