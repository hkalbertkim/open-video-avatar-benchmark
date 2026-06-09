#!/usr/bin/env python3
"""Plan a benchmark stage for one candidate without heavy execution."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from _registry import find_candidate, repo_root


def run_candidate(candidate_id: str, stage: str, registry: str, dry_run: bool = True) -> int:
    candidate = find_candidate(candidate_id, registry)
    if candidate is None:
        print(f"unknown candidate: {candidate_id}", file=sys.stderr)
        return 2

    root = repo_root()
    log_dir = root / "logs" / candidate_id
    output_dir = root / "outputs" / candidate_id
    log_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    metadata = {
        "candidate": candidate_id,
        "name": candidate.get("name"),
        "stage": stage,
        "dry_run": dry_run,
        "registry": registry,
        "adapter": candidate.get("adapter"),
        "status_before_run": candidate.get("status"),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "planned_action": "No clone, download, or inference is executed in the initial skeleton.",
    }
    metadata_path = log_dir / f"{stage}_metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        f"[dry-run={dry_run}] planned {stage} stage for {candidate_id}; "
        f"metadata={metadata_path.relative_to(root)} output_dir={output_dir.relative_to(root)}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, help="Candidate id from candidates/candidates.yaml")
    parser.add_argument("--stage", default="smoke", help="Benchmark stage to plan")
    parser.add_argument("--registry", default="candidates/candidates.yaml", help="Candidate registry path")
    parser.add_argument("--dry-run", action="store_true", help="Plan only; do not execute heavy commands")
    args = parser.parse_args(argv)
    return run_candidate(args.candidate, args.stage, args.registry, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
