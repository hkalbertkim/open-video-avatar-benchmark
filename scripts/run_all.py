#!/usr/bin/env python3
"""Plan a benchmark stage for all registered candidates."""

from __future__ import annotations

import argparse

from _registry import load_candidates
from run_candidate import run_candidate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", default="smoke", help="Benchmark stage to plan")
    parser.add_argument("--registry", default="candidates/candidates.yaml", help="Candidate registry path")
    parser.add_argument("--dry-run", action="store_true", help="Plan only; do not execute heavy commands")
    args = parser.parse_args()

    exit_code = 0
    for candidate in load_candidates(args.registry):
        candidate_id = str(candidate["id"])
        result = run_candidate(candidate_id, args.stage, args.registry, dry_run=args.dry_run)
        exit_code = max(exit_code, result)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
