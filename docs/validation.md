# Validation and evidence protocol

## Keep four measurements separate

### 1. Box detection

Precision, recall, F1, AP, and mAP compare predicted boxes with annotations using confidence ranking and IoU matching. Report the exact weights, dataset version/split, evaluator version, image size, confidence/IoU policy, class aggregation, and whether a value is a final epoch, selected checkpoint, or independently selected peak.

The uploaded benchmark artifacts belong to this layer. They do not establish route correctness.

### 2. Runtime inspection/classification

The full inspection decision may combine detector output with label-angle, fill-level, association, and rule logic. Its unit is a bottle/inspection event rather than a bounding box. Record one ground-truth condition and one decision per item, including unknown or low-confidence outcomes.

The thesis records an 85–95% integrated runtime inspection range. A per-item decision log is needed for independent reproduction.

### 3. Physical sorting

```text
sorting accuracy = correctly routed physical items / all physically inspected items
```

Record intended lane, actual lane, item ID, command, sensor/actuator events, exclusions, jams, missed/double actuations, conveyor speed, and hardware/firmware revisions. The count-derived rates from Table 6:5 are 57.14% for SC-05 and 93.88% overall.

### 4. End-to-end behavior

Define the start and end event. The documented 20.6 ms value is a host-processing sum, while 2–4 seconds covers field-of-view entry through completed physical deflection. Synchronized clocks are required to split capture, inference, rules, serial, flight, sensor wait, servo movement, and dwell.

## Evidence status

| Claim | Minimum evidence | Current status |
| --- | --- | --- |
| Dataset size/splits/classes | Versioned Kaggle export plus manifest | Public record says 119 images, 95/24, four classes; regenerate locally |
| Uploaded detector metrics | CSV/configuration and plot consistency | Extracted; weights/environment remain external |
| Quick Inference metrics | Preserved notebook output, version, model hash | Public output records 24 images / 83 instances |
| Runtime inspection accuracy | Per-item decisions and ground truth | Thesis records an 85–95% range; item log not included |
| Physical sorting accuracy | Item-level route ledger | Aggregate counts and calculated rates documented; ledger not included |
| Firmware behavior | Exact source, build record, board trace | Source present; build and physical execution require a dated record |
| MQTT/dashboard | Source/config and timestamped trace | Screenshots and notebook description available |
| Predictive maintenance | Physical signals, failure labels, time-aware evaluation | Virtual-sensing formula and dashboard-state demonstration available |

## Arithmetic and reporting checks

Every result table should satisfy these publication checks:

1. Row totals equal the declared denominator.
2. Displayed percentages recompute from displayed counts after stated rounding.
3. Selected metrics identify the selection criterion and checkpoint.
4. Independently selected peaks are labeled as peak values.
5. Detection instances are not counted as physical bottles.
6. Pass-through items are included in the physical denominator unless an exclusion is declared.
7. Failed, unknown, jammed, and unobserved outcomes have an explicit treatment.

Applied to the published route counts: `20/35 = 57.14%` and `230/245 = 93.88%`.

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

Use [`../results/templates/maintenance_events.csv`](../results/templates/maintenance_events.csv). Keep formula demonstrations using simulated values separate from prediction against physical failure/maintenance labels.

## Checks available in this checkout

```bash
pytest -q
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

The benchmark summary is deterministic extraction. Arduino compilation is not part of CI because the repository does not pin an Arduino core/toolchain, and compilation alone does not validate hardware operation.
