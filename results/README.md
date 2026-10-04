# Results and evidence

This directory is for measured evidence, not aspirational numbers. The current checkout has no thesis PDF or benchmark log, so no detection or physical sorting result is asserted.

Use the templates in [`templates/`](templates/) and cite the source for every populated row. Start with [`kaggle-benchmark-snapshot.md`](kaggle-benchmark-snapshot.md) for the current source comparison, not as a substitute for the thesis/log evidence.

- `detection_metrics.csv` — model-vs-annotation performance on a named split and evaluation configuration;
- `sorting_trials.csv` — physically observed route outcomes, with inspected-item count and route definition;
- `maintenance_events.csv` — condition signals, thresholds, events, and actions.

Keep these concepts separate in README tables and presentations. A high detection score does not prove a servo routed the item correctly, and a correct physical route does not prove the model detected every component correctly.
