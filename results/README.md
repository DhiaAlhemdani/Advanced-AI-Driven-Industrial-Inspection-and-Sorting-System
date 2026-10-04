# Results and evidence

This directory records the uploaded Ultralytics training bundle, thesis result categories, Kaggle dataset documentation, and Quick Inference output. Each value is labeled by source and measurement type in [`kaggle-benchmark-snapshot.md`](kaggle-benchmark-snapshot.md).

Key boundaries:

- uploaded precision/recall/mAP are **box detection** metrics;
- the thesis's 85–95% value is an integrated runtime inspection range;
- route counts are **physical sorting** evidence, with rates calculated directly from counts;
- simulated health scores are rule/formula outputs rather than predictive-maintenance accuracy.

Use the templates in [`templates/`](templates/) for new evidence:

- `detection_metrics.csv` — exact model/split/evaluator result;
- `sorting_trials.csv` — one physically observed route per item;
- `maintenance_events.csv` — signals, labels/events, thresholds, and actions.

Summarize the committed training CSV reproducibly with:

```bash
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

That command extracts existing rows; it does not rerun validation.
