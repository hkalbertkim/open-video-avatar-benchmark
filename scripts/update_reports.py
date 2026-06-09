#!/usr/bin/env python3
"""Regenerate rich candidate reports from the candidate registry."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from _registry import load_candidates, repo_root


REPORTS = {
    "inventory": "reports/00_candidate_inventory.md",
    "reproducibility": "reports/01_reproducibility_matrix.md",
    "license_weights": "reports/02_license_and_weights_matrix.md",
}

NO_REDISTRIBUTION_NOTE = (
    "This repository does not redistribute third-party weights, checkpoints, "
    "datasets, source videos, identity-bearing media, or restricted generated outputs."
)


def cell(value: object) -> str:
    if isinstance(value, list):
        text = ", ".join(str(item) for item in value)
    else:
        text = str(value)
    return text.replace("\n", " ").replace("|", "\\|")


def candidate_value(candidate: dict[str, object], key: str, default: str = "CHECK_REQUIRED") -> str:
    value = candidate.get(key, default)
    if value in (None, "", []):
        return default
    return cell(value)


def paper_project(candidate: dict[str, object]) -> str:
    paper = candidate_value(candidate, "paper_url")
    project = candidate_value(candidate, "project_url")
    return f"Paper: {paper}; Project: {project}"


def weights_status(candidate: dict[str, object]) -> str:
    status = candidate_value(candidate, "weights_status")
    source = candidate_value(candidate, "weights_source")
    return f"{status}; {source}"


def generated_header(title: str, registry: str, generated_at: str) -> list[str]:
    return [
        f"# {title}",
        "",
        f"Generated: {generated_at}",
        "",
        f"Source file: `{registry}`",
        "",
        NO_REDISTRIBUTION_NOTE,
        "",
    ]


def render_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def render_inventory(candidates: list[dict[str, object]], registry: str, generated_at: str) -> str:
    lines = generated_header("Candidate Inventory", registry, generated_at)
    lines.extend(
        [
            "Fields are generated from candidate metadata. Update `candidates/candidates.yaml` first, then rerun `python3 scripts/update_reports.py`.",
            "",
        ]
    )
    headers = [
        "id",
        "name",
        "category",
        "repo",
        "paper/project",
        "license",
        "weights status",
        "training code status",
        "inference code status",
        "metadata status",
        "notes",
    ]
    rows = [
        [
            candidate_value(candidate, "id"),
            candidate_value(candidate, "name"),
            candidate_value(candidate, "category"),
            candidate_value(candidate, "repo_url"),
            paper_project(candidate),
            candidate_value(candidate, "license"),
            candidate_value(candidate, "weights_status"),
            candidate_value(candidate, "training_code_status"),
            candidate_value(candidate, "inference_code_status"),
            candidate_value(candidate, "status"),
            candidate_value(candidate, "notes"),
        ]
        for candidate in candidates
    ]
    lines.extend(render_table(headers, rows))
    return "\n".join(lines)


def render_reproducibility(candidates: list[dict[str, object]], registry: str, generated_at: str) -> str:
    lines = generated_header("Reproducibility Matrix", registry, generated_at)
    lines.extend(
        [
            "Failure and blocked states remain first-class benchmark outcomes. Execution appendices should capture commit hash, exact environment, hardware, input manifest, output manifest, metrics, and failure label for both successful and failed candidates.",
            "",
        ]
    )
    headers = [
        "id",
        "code availability",
        "weights availability",
        "training support",
        "inference support",
        "install risk",
        "sample command known",
        "custom input readiness",
        "known setup risks",
        "metadata status",
    ]
    rows = [
        [
            candidate_value(candidate, "id"),
            f"Official repo: {candidate_value(candidate, 'repo_url')}",
            weights_status(candidate),
            candidate_value(candidate, "training_code_status"),
            candidate_value(candidate, "inference_code_status"),
            candidate_value(candidate, "install_risk"),
            candidate_value(candidate, "sample_command_known"),
            candidate_value(candidate, "custom_input_readiness"),
            candidate_value(candidate, "known_setup_risks"),
            candidate_value(candidate, "status"),
        ]
        for candidate in candidates
    ]
    lines.extend(render_table(headers, rows))
    return "\n".join(lines)


def render_license_weights(candidates: list[dict[str, object]], registry: str, generated_at: str) -> str:
    lines = generated_header("License and Weights Matrix", registry, generated_at)
    lines.extend(
        [
            "Candidate models remain governed by their original licenses and terms. The repository license applies only to benchmark harness code and documentation authored here.",
            "",
        ]
    )
    headers = [
        "id",
        "license",
        "weights source/status",
        "redistribution note",
        "commercial/use caution",
        "remaining CHECK_REQUIRED fields",
    ]
    rows = [
        [
            candidate_value(candidate, "id"),
            candidate_value(candidate, "license"),
            weights_status(candidate),
            candidate_value(candidate, "redistribution_note"),
            candidate_value(candidate, "commercial_caution", candidate_value(candidate, "license_caution")),
            candidate_value(candidate, "remaining_check_required"),
        ]
        for candidate in candidates
    ]
    lines.extend(render_table(headers, rows))
    return "\n".join(lines)


def write_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="candidates/candidates.yaml", help="Candidate registry path")
    parser.add_argument("--reports-dir", default="reports", help="Directory for generated report files")
    args = parser.parse_args()

    candidates = load_candidates(args.registry)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    root = repo_root()
    reports_dir = Path(args.reports_dir)
    if not reports_dir.is_absolute():
        reports_dir = root / reports_dir

    outputs = {
        reports_dir / "00_candidate_inventory.md": render_inventory(candidates, args.registry, generated_at),
        reports_dir / "01_reproducibility_matrix.md": render_reproducibility(candidates, args.registry, generated_at),
        reports_dir / "02_license_and_weights_matrix.md": render_license_weights(candidates, args.registry, generated_at),
    }
    for path, content in outputs.items():
        write_report(path, content)
        print(f"updated {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
