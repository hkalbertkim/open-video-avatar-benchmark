#!/usr/bin/env python3
"""Collect lightweight GPU availability metrics."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from _registry import repo_root


def collect() -> dict[str, object]:
    timestamp = datetime.now(timezone.utc).isoformat()
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return {
            "created_at": timestamp,
            "available": False,
            "tool": "nvidia-smi",
            "note": "nvidia-smi unavailable on PATH",
        }

    result = subprocess.run(
        [nvidia_smi, "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
        check=False,
        capture_output=True,
        text=True,
    )
    return {
        "created_at": timestamp,
        "available": result.returncode == 0,
        "tool": nvidia_smi,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="logs/gpu_metrics.json", help="Output JSON path")
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = repo_root() / output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = collect()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output.relative_to(repo_root())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
