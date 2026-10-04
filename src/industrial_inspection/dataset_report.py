"""Command-line entry point for the dataset inventory utility."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .dataset import build_dataset_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inventory image splits and YOLO-style labels; do not interpret counts as accuracy."
    )
    parser.add_argument("dataset_root", type=Path, help="Unpacked dataset directory")
    parser.add_argument(
        "--class-names",
        nargs="*",
        default=None,
        help="Optional ordered class names, for example: bottle cap label liquid",
    )
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = build_dataset_report(args.dataset_root, args.class_names)
    except (FileNotFoundError, OSError) as exc:
        print(f"dataset-report: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
