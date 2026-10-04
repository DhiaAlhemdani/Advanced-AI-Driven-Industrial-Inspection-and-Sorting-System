"""Inventory a local object-detection dataset without evaluating a model.

The project dataset is kept outside Git and downloaded from Kaggle. This module
only inventories files and YOLO-style annotations; it deliberately does not
infer detection quality from image or label counts.
"""

from __future__ import annotations

import ast
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
SPLIT_ALIASES = {
    "train": "train",
    "val": "validation",
    "valid": "validation",
    "validation": "validation",
    "test": "test",
}


def _split_for(path: Path, root: Path) -> str:
    """Return a conventional split name based on path components."""

    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    for part in parts:
        split = SPLIT_ALIASES.get(part.lower())
        if split:
            return split
    return "unspecified"


def _names_from_data_yaml(root: Path) -> list[str]:
    """Read simple ``names: [...]`` declarations without requiring PyYAML.

    This is intentionally conservative. Complex YAML is left for the original
    training environment rather than being guessed by a reporting utility.
    """

    candidates = sorted(root.rglob("data.yaml")) + sorted(root.rglob("data.yml"))
    for candidate in candidates:
        text = candidate.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"^\s*names\s*:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if not match:
            continue
        raw = match.group(1).strip()
        try:
            parsed = ast.literal_eval(raw)
        except (SyntaxError, ValueError):
            if raw.startswith("[") and raw.endswith("]"):
                parsed = [item.strip().strip("'\"") for item in raw[1:-1].split(",")]
            else:
                continue
        if isinstance(parsed, (list, tuple)) and all(isinstance(item, str) for item in parsed):
            return list(parsed)
    return []


def _iter_images(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def _iter_label_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.txt") if path.is_file())


def _read_class_ids(label_path: Path) -> tuple[list[int], list[str]]:
    """Read class ids from YOLO rows and return ids plus parse warnings."""

    class_ids: list[int] = []
    warnings: list[str] = []
    for line_number, raw_line in enumerate(
        label_path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 5:
            warnings.append(f"{label_path}:{line_number}: expected a YOLO row with at least 5 fields")
            continue
        try:
            class_id = int(float(fields[0]))
        except ValueError:
            warnings.append(f"{label_path}:{line_number}: class id is not numeric")
            continue
        if class_id < 0:
            warnings.append(f"{label_path}:{line_number}: class id is negative")
            continue
        class_ids.append(class_id)
    return class_ids, warnings


def build_dataset_report(
    dataset_root: str | Path,
    class_names: Iterable[str] | None = None,
) -> dict:
    """Build a deterministic inventory report for a local dataset directory.

    The report is useful for checking a download and split layout. It is not a
    training report and contains no model-derived metric.
    """

    root = Path(dataset_root).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Dataset directory does not exist: {root}")

    names = list(class_names or _names_from_data_yaml(root))
    images = _iter_images(root)
    labels = _iter_label_files(root)
    split_counts = Counter(_split_for(path, root) for path in images)
    class_counts: Counter[str] = Counter()
    warnings: list[str] = []
    parsed_label_rows = 0

    for label_path in labels:
        class_ids, label_warnings = _read_class_ids(label_path)
        warnings.extend(label_warnings)
        parsed_label_rows += len(class_ids)
        for class_id in class_ids:
            if names and class_id >= len(names):
                warnings.append(
                    f"{label_path}: class id {class_id} is outside the supplied class list"
                )
                key = str(class_id)
            elif names:
                key = names[class_id]
            else:
                key = str(class_id)
            class_counts[key] += 1

    return {
        "schema_version": "1.0",
        "dataset_name": root.name,
        "image_count": len(images),
        "image_count_by_split": dict(sorted(split_counts.items())),
        "label_file_count": len(labels),
        "parsed_label_row_count": parsed_label_rows,
        "class_names": names,
        "class_instance_counts": dict(sorted(class_counts.items())),
        "warnings": sorted(set(warnings)),
    }
