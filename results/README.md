# Results and evidence

The repository now contains an uploaded Ultralytics training bundle and a thesis, while Kaggle provides a dataset README and Quick Inference output. Their values are compared in [`kaggle-benchmark-snapshot.md`](kaggle-benchmark-snapshot.md).

Key boundaries:

- uploaded precision/recall/mAP are **box detection** metrics;
- the thesis's 85–95% value is an incompletely defined runtime inspection range;
- route counts are **physical sorting** evidence and contain arithmetic contradictions;
- simulated health scores are rule/formula outputs, not predictive-maintenance accuracy.

Use the templates in [`templates/`](templates/) for new evidence:

- `detection_metrics.csv` — exact model/split/evaluator result;
- `sorting_trials.csv` — one physically observed route per item;
- `maintenance_events.csv` — signals, labels/events, thresholds, and actions.

Summarize the committed training CSV reproducibly with:

```bash
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

That command extracts existing rows; it does not rerun validation.
