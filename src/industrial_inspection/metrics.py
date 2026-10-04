"""Metric primitives with an explicit boundary between detection and sorting."""

from __future__ import annotations

from dataclasses import dataclass


def _safe_ratio(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


@dataclass(frozen=True)
class DetectionCounts:
    """Counts for one declared detection task and evaluation configuration."""

    true_positive: int
    false_positive: int
    false_negative: int

    @property
    def precision(self) -> float:
        return _safe_ratio(self.true_positive, self.true_positive + self.false_positive)

    @property
    def recall(self) -> float:
        return _safe_ratio(self.true_positive, self.true_positive + self.false_negative)

    @property
    def f1(self) -> float:
        return _safe_ratio(2 * self.precision * self.recall, self.precision + self.recall)


@dataclass(frozen=True)
class SortingCounts:
    """Physical route outcomes from a trial log, not model detections."""

    correct_routes: int
    inspected_items: int

    @property
    def accuracy(self) -> float:
        return _safe_ratio(self.correct_routes, self.inspected_items)


def detection_summary(counts: DetectionCounts) -> dict[str, float | int]:
    """Serialize detection counts and derived metrics for an evidence table."""

    return {
        "true_positive": counts.true_positive,
        "false_positive": counts.false_positive,
        "false_negative": counts.false_negative,
        "precision": counts.precision,
        "recall": counts.recall,
        "f1": counts.f1,
    }


def sorting_summary(counts: SortingCounts) -> dict[str, float | int]:
    """Serialize physical sorting outcomes without conflating them with CV metrics."""

    return {
        "correct_routes": counts.correct_routes,
        "inspected_items": counts.inspected_items,
        "sorting_accuracy": counts.accuracy,
    }
