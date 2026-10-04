"""Summarize an Ultralytics ``results.csv`` without evaluating a model.

This utility reports values already present in a training artifact. It does not load
weights, rerun validation, or turn a training-history row into physical sorting
accuracy.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import TextIO

METRIC_COLUMNS = (
    "metrics/precision(B)",
    "metrics/recall(B)",
    "metrics/mAP50(B)",
    "metrics/mAP50-95(B)",
)


def summarize_results_csv(path: str | Path) -> dict[str, object]:
    """Return final and peak box metrics from an Ultralytics results CSV."""

    source = Path(path)
    with source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise ValueError(f"no result rows in {source}")

    required = {"epoch", *METRIC_COLUMNS}
    missing = required.difference(rows[0])
    if missing:
        raise ValueError(f"missing columns in {source}: {', '.join(sorted(missing))}")

    def value(row: dict[str, str], column: str) -> float:
        return float(row[column].strip())

    final = rows[-1]
    return {
        "source": source.as_posix(),
        "row_count": len(rows),
        "first_epoch": int(float(rows[0]["epoch"])),
        "final_epoch": int(float(final["epoch"])),
        "final": {
            column: value(final, column)
            for column in METRIC_COLUMNS
        },
        "peaks": {
            column: {
                "value": value(best := max(rows, key=lambda row: value(row, column)), column),
                "epoch": int(float(best["epoch"])),
            }
            for column in METRIC_COLUMNS
        },
    }


def print_summary(summary: dict[str, object], output: TextIO) -> None:
    """Render a stable text summary suitable for an audit log."""

    print(f"source: {summary['source']}", file=output)
    print(f"rows: {summary['row_count']}", file=output)
    print(f"epochs: {summary['first_epoch']}..{summary['final_epoch']}", file=output)
    final = summary["final"]
    peaks = summary["peaks"]
    assert isinstance(final, dict) and isinstance(peaks, dict)
    for column in METRIC_COLUMNS:
        peak = peaks[column]
        assert isinstance(peak, dict)
        print(
            f"{column}: final={final[column]:.5f}; "
            f"peak={peak['value']:.5f} at epoch {peak['epoch']}",
            file=output,
        )


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point."""

    parser = argparse.ArgumentParser(
        description="Print final and peak metrics from an Ultralytics results.csv artifact."
    )
    parser.add_argument("results_csv", type=Path)
    args = parser.parse_args(argv)
    try:
        summary = summarize_results_csv(args.results_csv)
    except (OSError, ValueError) as exc:
        print(f"benchmark-summary: {exc}", file=sys.stderr)
        return 2
    print_summary(summary, sys.stdout)
    return 0
