# Validation and evidence protocol

## The two accuracy numbers are not interchangeable

### Detection performance

Detection performance measures a computer-vision model against annotations under a declared evaluation configuration. Typical outputs may include precision, recall, F1, mAP@0.50, or mAP@[0.50:0.95], but the metric name alone is not enough. Record the model, split, class order, confidence threshold, IoU threshold, matching policy, and whether values are per-class or aggregated.

A simple count-based sanity check is:

```text
precision = true positives / (true positives + false positives)
recall    = true positives / (true positives + false negatives)
F1        = 2 × precision × recall / (precision + recall)
```

The formulas do not replace the original evaluator, especially for object detection where IoU matching and confidence ranking matter.

### Physical sorting accuracy

Physical sorting accuracy measures route outcomes observed on the bench:

```text
sorting accuracy = correctly routed items / physically inspected items
```

Record the ground-truth route/bin, actual route/bin, unknown/reject outcomes, missed or double-triggered items, trial speed, and any item exclusions. This number must come from a physical trial log. It is not derived from detection precision or recall.

### End-to-end behavior

If an end-to-end result is reported, define the denominator and include the full chain: capture, inference, decision transport, conveyor timing, servo movement, and observed bin. Also record failures caused by communication, timing, jams, or maintenance conditions.

## Evidence matrix

| Claim | Minimum evidence | Status in this checkout |
| --- | --- | --- |
| Dataset size/splits/classes | Kaggle URL plus generated manifest | Reported by project owner; regenerate locally |
| Detection metric | Evaluator output plus model/config/split and thesis/log reference | Kaggle publishes two conflicting detector result sets; see [`results/kaggle-benchmark-snapshot.md`](../results/kaggle-benchmark-snapshot.md) |
| Sorting accuracy | Dated trial log with route ground truth and item count | Kaggle publishes a scenario table, but SC-05 and overall values need arithmetic/source reconciliation |
| Notebook implementation | Exact `.ipynb` export plus version metadata | Public Kaggle notebook version 2 identified; exact export not yet committed |
| Arduino/servo integration | Original firmware, wiring/board record, and trial log | Not available; no firmware reconstructed |
| MQTT monitoring | Source/config plus sanitized message trace or screenshot with provenance | Not available |
| Predictive maintenance | Signal definitions, labels, features, model/evaluation, and event log | Not available |

## Evidence-entry templates

Populate the CSV templates under [`results/templates/`](../results/templates/). Every non-empty result row must include a source reference such as a thesis page, benchmark-log filename/row, or a reproducible run artifact. Avoid vague references such as “testing” or “final result.”

Recommended evidence package for one release:

```text
results/
├── detection_metrics.csv
├── sorting_trials.csv
├── maintenance_events.csv
└── evidence/
    ├── dataset_report.json
    ├── benchmark-log-redacted.csv
    └── README.md
```

Keep private credentials, personally identifying information, and raw camera footage outside the public repository.

## Acceptance checks before publishing a headline result

1. Re-run the evaluator from a clean environment.
2. Confirm the dataset version and split against the thesis.
3. Check that the reported class order matches the label map.
4. Compare the number to the original benchmark log, not memory or a screenshot without provenance.
5. State whether the result is detection, physical sorting, or end-to-end.
6. State the sample size and exclusions.
7. Add the limitation and failure cases next to the result.
