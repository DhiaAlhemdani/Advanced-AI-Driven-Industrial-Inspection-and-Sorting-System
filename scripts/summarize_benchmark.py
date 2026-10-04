#!/usr/bin/env python3
"""Print final and peak metrics from an Ultralytics results.csv artifact."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from industrial_inspection.benchmark import print_summary, summarize_results_csv


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results_csv", type=Path)
    args = parser.parse_args(argv)
    try:
        summary = summarize_results_csv(args.results_csv)
    except (OSError, ValueError) as exc:
        print(f"summarize-benchmark: {exc}", file=sys.stderr)
        return 2
    print_summary(summary, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
