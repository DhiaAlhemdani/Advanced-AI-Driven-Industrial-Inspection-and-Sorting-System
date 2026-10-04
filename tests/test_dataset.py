from pathlib import Path

from industrial_inspection.dataset import build_dataset_report


def _touch(path: Path, content: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_dataset_report_counts_splits_and_yolo_classes(tmp_path: Path) -> None:
    root = tmp_path / "dataset"
    _touch(root / "images" / "train" / "one.jpg")
    _touch(root / "images" / "train" / "two.png")
    _touch(root / "images" / "val" / "three.jpg")
    _touch(root / "labels" / "train" / "one.txt", "0 0.5 0.5 0.8 0.8\n1 0.4 0.4 0.2 0.2\n")
    _touch(root / "labels" / "train" / "two.txt", "2 0.5 0.5 0.1 0.1\n")
    _touch(root / "labels" / "val" / "three.txt", "3 0.5 0.5 0.3 0.3\n")

    report = build_dataset_report(root, ["bottle", "cap", "label", "liquid"])

    assert report["image_count"] == 3
    assert report["image_count_by_split"] == {"train": 2, "validation": 1}
    assert report["parsed_label_row_count"] == 4
    assert report["class_instance_counts"] == {
        "bottle": 1,
        "cap": 1,
        "label": 1,
        "liquid": 1,
    }
    assert report["warnings"] == []


def test_dataset_report_warns_for_malformed_rows(tmp_path: Path) -> None:
    root = tmp_path / "dataset"
    _touch(root / "images" / "train" / "one.jpg")
    _touch(root / "labels" / "train" / "one.txt", "not-a-yolo-row\n")

    report = build_dataset_report(root, ["bottle"])

    assert report["parsed_label_row_count"] == 0
    assert len(report["warnings"]) == 1
    assert "expected a YOLO row" in report["warnings"][0]
