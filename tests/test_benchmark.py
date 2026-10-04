from pathlib import Path

import pytest

from industrial_inspection.benchmark import summarize_results_csv


HEADER = (
    "epoch,metrics/precision(B),metrics/recall(B),"
    "metrics/mAP50(B),metrics/mAP50-95(B)\n"
)


def test_summarizes_final_and_peak_metrics(tmp_path: Path) -> None:
    results = tmp_path / "results.csv"
    results.write_text(
        HEADER
        + "1,0.80,0.70,0.75,0.50\n"
        + "2,0.90,0.85,0.88,0.60\n"
        + "3,0.89,0.95,0.91,0.59\n",
        encoding="utf-8",
    )

    summary = summarize_results_csv(results)

    assert summary["row_count"] == 3
    assert summary["final_epoch"] == 3
    assert summary["final"]["metrics/precision(B)"] == pytest.approx(0.89)
    assert summary["peaks"]["metrics/precision(B)"] == {"value": 0.9, "epoch": 2}
    assert summary["peaks"]["metrics/recall(B)"] == {"value": 0.95, "epoch": 3}


def test_rejects_missing_metric_columns(tmp_path: Path) -> None:
    results = tmp_path / "results.csv"
    results.write_text("epoch,metrics/precision(B)\n1,0.9\n", encoding="utf-8")

    with pytest.raises(ValueError, match="missing columns"):
        summarize_results_csv(results)
