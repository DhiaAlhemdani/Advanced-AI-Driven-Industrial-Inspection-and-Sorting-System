"""Fetch and stage the original Kaggle notebook and non-media dataset artifacts.

This script intentionally leaves images and model weights in a staging directory.
It requires the official Kaggle CLI to be authenticated on the machine running it.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

DATASET = "dhiaalhemdani/industrial-inspection-system"
NOTEBOOK = "dhiaalhemdani/advanced-ai-driven-quality-control-system"


def run(command: list[str]) -> None:
    print("$", " ".join(command))
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, default=Path("staging/kaggle"))
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()

    stage = args.stage.resolve()
    repo_root = args.repo_root.resolve()
    dataset_stage = stage / "dataset"
    notebook_stage = stage / "notebooks" / "advanced-ai-driven-quality-control-system"
    dataset_stage.mkdir(parents=True, exist_ok=True)
    notebook_stage.mkdir(parents=True, exist_ok=True)

    # The archive is staged outside Git. The dataset is public but large.
    run([
        "kaggle", "datasets", "download", "-d", DATASET,
        "--dataset-version-number", "10", "-p", str(dataset_stage), "--unzip",
    ])
    run(["kaggle", "kernels", "pull", NOTEBOOK, "-p", str(notebook_stage), "--metadata"])

    # Copy only reproducible, non-media source artifacts into the repository.
    # Images, *.pt weights, and generated plots remain in staging for owner review.
    copy_files = [
        "data_detect.yaml",
        "data_segment.yaml",
        "README.md",
        "metadata.csv",
        "benchmarks/args.yaml",
        "benchmarks/results.csv",
    ]
    for relative in copy_files:
        source = dataset_stage / relative
        if not source.is_file():
            print(f"warning: missing staged file: {source}")
            continue
        destination = repo_root / "kaggle" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    # Keep labels and JSON annotations available for a separate review commit.
    # They are data artifacts, not executable source, and should be checked for
    # size/license before being committed publicly.
    for directory in ("labels", "labels_seg", "annotations_labelme"):
        source = dataset_stage / directory
        destination = repo_root / "kaggle" / directory
        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)

    print(f"Staged Kaggle download under {stage}")
    print("Review provenance, file sizes, and licensing before committing data artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
