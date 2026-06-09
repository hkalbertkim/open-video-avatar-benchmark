#!/usr/bin/env python3
"""Regenerate deterministic report tables from the candidate registry."""

from __future__ import annotations

import argparse
from pathlib import Path

from _registry import load_candidates, repo_root


def render_inventory(registry: str) -> str:
    candidates = load_candidates(registry)
    lines = [
        "# Candidate Inventory",
        "",
        "Generated from `candidates/candidates.yaml`.",
        "",
        "| ID | Name | Category | Repo | License | Weights | Status | Adapter |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for candidate in candidates:
        lines.append(
            "| {id} | {name} | {category} | {repo_url} | {license} | {weights_status} | {status} | {adapter} |".format(
                **{key: str(value) for key, value in candidate.items()}
            )
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="candidates/candidates.yaml", help="Candidate registry path")
    parser.add_argument("--output", default="reports/00_candidate_inventory.md", help="Inventory report path")
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = repo_root() / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_inventory(args.registry), encoding="utf-8")
    print(f"updated {output.relative_to(repo_root())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
