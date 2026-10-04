import pytest

from industrial_inspection.metrics import (
    DetectionCounts,
    SortingCounts,
    detection_summary,
    sorting_summary,
)


def test_detection_metrics_are_computed_from_detection_counts() -> None:
    summary = detection_summary(DetectionCounts(true_positive=8, false_positive=2, false_negative=2))

    assert summary["precision"] == 0.8
    assert summary["recall"] == 0.8
    assert summary["f1"] == pytest.approx(0.8)


def test_sorting_accuracy_is_a_separate_physical_measure() -> None:
    summary = sorting_summary(SortingCounts(correct_routes=9, inspected_items=10))

    assert summary["sorting_accuracy"] == 0.9
    assert "precision" not in summary
    assert "recall" not in summary
