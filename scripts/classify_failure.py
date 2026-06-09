#!/usr/bin/env python3
"""Classify common benchmark failure text into status labels."""

from __future__ import annotations

import argparse
from pathlib import Path


LABELS = [
    "PASS_VIVIDO_INPUT",
    "PASS_SAMPLE_ONLY",
    "PATCHED_PASS",
    "BLOCKED_WEIGHTS",
    "BLOCKED_LICENSE",
    "BLOCKED_DEPENDENCY",
    "BLOCKED_HARDWARE",
    "FAIL_OUTPUT_CORRUPTED",
    "FAIL_TOO_SLOW",
    "RETEST_REQUIRED",
]


KEYWORDS = [
    ("BLOCKED_WEIGHTS", ["checkpoint", "weight", "model file", "safetensors", "pth", "ckpt"]),
    ("BLOCKED_LICENSE", ["license", "terms", "commercial use", "permission"]),
    ("BLOCKED_DEPENDENCY", ["modulenotfounderror", "importerror", "dependency", "package not found"]),
    ("BLOCKED_HARDWARE", ["cuda out of memory", "no cuda", "gpu", "vram", "mps unavailable"]),
    ("FAIL_OUTPUT_CORRUPTED", ["corrupt", "invalid video", "ffmpeg error", "nan", "black frames"]),
    ("FAIL_TOO_SLOW", ["too slow", "timeout", "seconds per frame", "below real-time"]),
    ("RETEST_REQUIRED", ["flaky", "inconclusive", "stale", "rerun", "retest"]),
]


def classify_failure(text: str) -> str:
    lowered = text.lower()
    for label, keywords in KEYWORDS:
        if any(keyword in lowered for keyword in keywords):
            return label
    return "RETEST_REQUIRED"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Log text to classify")
    parser.add_argument("--file", help="Path to a log file to classify")
    parser.add_argument("--list-labels", action="store_true", help="Print supported labels")
    args = parser.parse_args()

    if args.list_labels:
        print("\n".join(LABELS))
        return 0
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8", errors="replace")
    else:
        text = args.text or ""
    print(classify_failure(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
