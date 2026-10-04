# Validation and evidence protocol

## Keep four measurements separate

### 1. Box detection

Precision, recall, F1, AP, and mAP compare predicted boxes with annotations using confidence ranking and IoU matching. Report the exact weights, dataset version/split, evaluator version, image size, confidence/IoU policy, class aggregation, and whether a value is a final epoch, best checkpoint, or peak selected independently across epochs.

The uploaded benchmark artifacts belong here. They do **not** establish route correctness.

### 2. Runtime inspection/classification

The full inspection decision may combine detector output with label-angle, fill-level, association, and rule logic. Its unit is a bottle/inspection event, not a bounding box. Record one ground-truth condition and one decision per item, including unknown/low-confidence outcomes.

The thesis's 85–95% range appears to describe this layer, but provides no denominator or item log. Its separate 245/245 three-class matrix conflicts with that range.

### 3. Physical sorting

```text
sorting accuracy = correctly routed physical items / all physically inspected items
```

Record intended lane, actual lane, item ID, command, sensor/actuator events, exclusions, jams, missed/double actuations, conveyor speed, and hardware/firmware revisions. Table 6:5 supplies aggregate counts only and is arithmetically inconsistent; it is reported evidence, not a verified trial ledger.

### 4. End-to-end behavior

Define the start and end event. The thesis's 20.6 ms computational sum is not its 2–4 s camera-entry-to-deflection value. Synchronized clocks are required to split capture, inference, rules, serial, flight, sensor wait, servo movement, and dwell.

## Current source comparison

| Claim | Minimum evidence | Status |
| --- | --- | --- |
| Dataset size/splits/classes | Versioned Kaggle export plus manifest | Public record says 119 images, 95/24, four classes; regenerate locally |
| Uploaded detector metrics | CSV/configuration and plot consistency | Extracted; weights/environment absent, so not rerun |
| Quick Inference metrics | Preserved notebook output, version, model hash | Public output recorded as 24 images / 83 instances; differs from CSV |
| Runtime inspection accuracy | Per-item decisions and ground truth | Thesis gives 85–95% and a conflicting perfect matrix; log absent |
| Physical sorting accuracy | Item-level route ledger | Aggregate table implies 230/245; published percentages/narrative conflict |
| Firmware behavior | Exact source, build record, board trace | Source present; build and hardware execution unverified; thesis mismatch documented |
| MQTT/dashboard | Source/config and timestamped trace | Screenshots and notebook description only |
| Predictive maintenance | Physical signals, failure labels, time-aware evaluation | Thesis explicitly uses virtual sensing; no predictive-accuracy evidence |

## Arithmetic acceptance checks

Every result table must pass these before publication:

1. Row totals equal the declared denominator.
2. Displayed percentages recompute from displayed counts after stated rounding.
3. “Best” metrics identify the selection criterion and checkpoint.
4. Independently peaked metrics are not shown as though they came from one model state.
5. Detection instances are not counted as physical bottles.
6. Pass-through items are included in the physical denominator unless an exclusion is declared.
7. Failed, unknown, jammed, and unobserved outcomes have an explicit treatment.

Applied to Table 6:5: `20/35 = 57.14%`, not 62%; `230/245 = 93.88%`, not 95%; and neither supports the surrounding 100% narrative.

## Required evaluation packages

### Detector package

```text
weights checksum
model/config identity
code and Ultralytics versions
dataset archive/manifest checksum and split
validation command
confidence and IoU settings
machine-readable per-class and aggregate output
```

### Physical trial package

Use [`../results/templates/sorting_trials.csv`](../results/templates/sorting_trials.csv), one row per item. Add synchronized serial/sensor logs, firmware hash, wiring/mechanical revision, speed, operator/date, and an explanation of exclusions.

### Maintenance package

Use [`../results/templates/maintenance_events.csv`](../results/templates/maintenance_events.csv). Keep formula demonstrations using simulated values separate from prediction against real failure/maintenance labels.

## Checks available in this checkout

```bash
pytest -q
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

The benchmark summary is deterministic extraction, not reevaluation. Arduino compilation is not part of CI because the repository does not pin an Arduino core/toolchain and compilation alone would not verify the hardware claims.
