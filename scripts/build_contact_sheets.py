#!/usr/bin/env python3
"""Placeholder contact-sheet builder for generated benchmark videos."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from _registry import repo_root


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", default="outputs", help="Directory containing generated videos")
    parser.add_argument("--output", default="reports/contact_sheets_manifest.json", help="Placeholder manifest path")
    parser.add_argument("--dry-run", action="store_true", help="Record planned action only")
    args = parser.parse_args()

    root = repo_root()
    output = Path(args.output)
    if not output.is_absolute():
        output = root / output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": args.input_dir,
        "dry_run": args.dry_run,
        "note": "Future implementation will build contact sheets from generated benchmark videos without adding heavy dependencies to the skeleton.",
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"planned contact-sheet build; manifest={output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
