# Intelligent Industrial Inspection and Sorting System

**Graduation-project engineering record by Deiaa Ahmed Abdo Lootf**

[![CI](https://github.com/DhiaAlhemdani/Advanced-AI-Driven-Industrial-Inspection-and-Sorting-System/actions/workflows/ci.yml/badge.svg)](https://github.com/DhiaAlhemdani/Advanced-AI-Driven-Industrial-Inspection-and-Sorting-System/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository documents a bottle inspection prototype combining object detection, rule-based/OpenCV checks, serially commanded Arduino actuation, a three-route conveyor concept, dashboard monitoring, and simulated predictive-maintenance telemetry.

> **Evidence boundary:** the thesis, Arduino sketch, benchmark CSV/plots, photographs, screenshots, and demo video are present and inventoried. Training images, labels, annotations, the original notebook, and model weights remain canonical on [Kaggle](https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system) and are intentionally not duplicated here. The historical thesis remains unchanged, while an [updated metrics and firmware edition](docs/Project%20Research%20-%20Updated%20Metrics%20and%20Firmware.pdf) adds the benchmark results, count-derived sorting rates, and uploaded firmware specification.

## Project record

| Area | Available evidence |
| --- | --- |
| Dataset | 119 images: 95 train / 24 validation; classes `bottle`, `cap`, `label`, `liquid` (Kaggle version-10 record) |
| Thesis | [Original historical PDF](docs/Project%20Research.pdf) plus [updated metrics and firmware edition](docs/Project%20Research%20-%20Updated%20Metrics%20and%20Firmware.pdf) and [update notes](docs/thesis-update-notes.md) |
| Detection bundle | 121-row Ultralytics `results.csv`, settings, curves, confusion matrices, and qualitative train/validation mosaics |
| Physical evaluation | Thesis describes 245 bottles across five scenarios; no item-level route log is present |
| Firmware | Owner-uploaded [`firmware/sketch_may1a.ino`](firmware/sketch_may1a.ino), preserved as supplied and documented separately |
| Media | One prototype photo, two dashboard/conveyor screenshots, banner, and demo video |
| External-only artifacts | Training data, labels, polygon/LabelMe annotations, original notebook, and model weights on Kaggle |

See the complete [artifact inventory](docs/artifact-inventory.md) for sizes, hashes, and inspection notes.

## Project media

The media below is qualitative project evidence, not a substitute for synchronized trial logs or evaluator output.

### Project banner

![Industrial inspection system project banner](media/kaggle_cover_banner.png)

### Conveyor prototype

![Bottle conveyor prototype in the workshop](media/20260414_235234.jpg)

### Dashboard and conveyor demonstration

| Dashboard inspection view | Dashboard accumulated-results view |
| --- | --- |
| [![Dashboard showing a live inspection and conveyor](media/Screenshot_20260725_202954_MX%20Player.jpg)](media/Screenshot_20260725_202954_MX%20Player.jpg) | [![Dashboard showing accumulated inspection results and conveyor](media/Screenshot_20260725_203316_MX%20Player.jpg)](media/Screenshot_20260725_203316_MX%20Player.jpg) |

### Demonstration video

<video src="media/lv_0_٢٠٢٦٠٧٠٥٠٠٢٦٤.mp4" controls width="100%">
  <a href="media/lv_0_٢٠٢٦٠٧٠٥٠٠٢٦٤.mp4">Open or download the project demonstration video</a>.
</video>

If the repository viewer does not render embedded MP4 video, use the [direct video link](media/lv_0_٢٠٢٦٠٧٠٥٠٠٢٦٤.mp4).

## Results at a glance

### Detection metrics (annotation evaluation)

| Evidence source | Precision | Recall | mAP@0.50 | mAP@0.50:0.95 |
| --- | ---: | ---: | ---: | ---: |
| Uploaded CSV, final epoch 121 | 97.367% | 98.584% | 99.414% | 94.317% |
| Uploaded CSV, best mAP@0.50:0.95 row (epoch 117) | 95.780% | 98.816% | 99.389% | 94.441% |
| Kaggle Quick Inference, 24 images / 83 instances | 98.1% | 95.7% | 96.47% | 92.12% |

The uploaded CSV table reports the final epoch and the checkpoint selected by mAP@0.50:0.95. Quick Inference is listed as its own 24-image, 83-instance evaluation. The thesis's **85–95% inspection accuracy** is retained as an integrated runtime range. These model and runtime results are documented separately from physical sorting accuracy.

### Physical sorting claims (route outcomes)

Using the counts in Thesis Table 6:5 and the Kaggle README, the documented count-derived rates are **230/245 = 93.88% overall** and **20/35 = 57.14% for SC-05**. The scenario counts and calculated percentages are shown together so the denominator is explicit. An item-level route ledger is still required for an independently repeatable physical sorting evaluation.

| Measurement type | What it answers | Evidence required |
| --- | --- | --- |
| Detection precision/recall/mAP | Did predicted boxes match annotations? | Weights, split, evaluator/config, annotations |
| Runtime inspection/classification | Did the full vision/rule pipeline assign the intended condition? | Per-item ground truth and decision log |
| Physical sorting accuracy | Did each physical item arrive in the intended lane? | Dated item-level route ledger and hardware revision |
| End-to-end latency | How long from item entry to completed routing? | Synchronized capture, command, sensor, and actuator timestamps |

The full source-specific results record is in [`results/kaggle-benchmark-snapshot.md`](results/kaggle-benchmark-snapshot.md).

## Benchmark gallery

These are the uploaded Ultralytics artifacts. Curves and confusion matrices describe **box detection** on the recorded validation run; they do not measure physical sorting.

### Training history

[![Ultralytics training and validation history](kaggle/benchmarks/results.png)](kaggle/benchmarks/results.png)

### Detection curves

| Precision–recall | F1–confidence |
| --- | --- |
| [![Box precision-recall curve](kaggle/benchmarks/BoxPR_curve.png)](kaggle/benchmarks/BoxPR_curve.png) | [![Box F1-confidence curve](kaggle/benchmarks/BoxF1_curve.png)](kaggle/benchmarks/BoxF1_curve.png) |
| **Precision–confidence** | **Recall–confidence** |
| [![Box precision-confidence curve](kaggle/benchmarks/BoxP_curve.png)](kaggle/benchmarks/BoxP_curve.png) | [![Box recall-confidence curve](kaggle/benchmarks/BoxR_curve.png)](kaggle/benchmarks/BoxR_curve.png) |

### Detector confusion matrices

| Counts | Normalized |
| --- | --- |
| [![Object-detector confusion matrix](kaggle/benchmarks/confusion_matrix.png)](kaggle/benchmarks/confusion_matrix.png) | [![Normalized object-detector confusion matrix](kaggle/benchmarks/confusion_matrix_normalized.png)](kaggle/benchmarks/confusion_matrix_normalized.png) |

### Label distribution and training batches

[![Dataset label distribution and bounding-box statistics](kaggle/benchmarks/labels.jpg)](kaggle/benchmarks/labels.jpg)

| Training batch 0 | Training batch 1 | Training batch 2 |
| --- | --- | --- |
| [![Training batch zero](kaggle/benchmarks/train_batch0.jpg)](kaggle/benchmarks/train_batch0.jpg) | [![Training batch one](kaggle/benchmarks/train_batch1.jpg)](kaggle/benchmarks/train_batch1.jpg) | [![Training batch two](kaggle/benchmarks/train_batch2.jpg)](kaggle/benchmarks/train_batch2.jpg) |

### Validation labels and predictions

| Batch | Ground-truth labels | Model predictions |
| ---: | --- | --- |
| 0 | [![Validation batch zero labels](kaggle/benchmarks/val_batch0_labels.jpg)](kaggle/benchmarks/val_batch0_labels.jpg) | [![Validation batch zero predictions](kaggle/benchmarks/val_batch0_pred.jpg)](kaggle/benchmarks/val_batch0_pred.jpg) |
| 1 | [![Validation batch one labels](kaggle/benchmarks/val_batch1_labels.jpg)](kaggle/benchmarks/val_batch1_labels.jpg) | [![Validation batch one predictions](kaggle/benchmarks/val_batch1_pred.jpg)](kaggle/benchmarks/val_batch1_pred.jpg) |
| 2 | [![Validation batch two labels](kaggle/benchmarks/val_batch2_labels.jpg)](kaggle/benchmarks/val_batch2_labels.jpg) | [![Validation batch two predictions](kaggle/benchmarks/val_batch2_pred.jpg)](kaggle/benchmarks/val_batch2_pred.jpg) |

## Architecture

```mermaid
flowchart LR
    C[Camera / frame] --> Y[YOLO component detection]
    Y --> R[OpenCV and rule checks]
    R -->|pass: no byte| P[Main lane]
    R -->|A| H[Host serial link]
    R -->|B| H
    H --> M[Arduino sketch]
    SA[Active-low proximity A] --> M
    SB[Active-low proximity B] --> M
    M -->|pin 9| A[Servo A / reprocess label]
    M -->|pin 10| B[Servo B / defect label]
    R --> T[MQTT/dashboard path in notebook record]
    VS[Simulated condition values] --> PM[Health-score rules]
    PM --> T
```

The diagram documents the current uploaded-sketch interface; it is not a wiring diagram. The firmware specification uses polling, 9600 baud, a 500 ms hold time, commands `A`/`B`, proximity pins 2/3, and servo pins 9/10. Acknowledgements, item identifiers, distance-based flight timers, conveyor control, MQTT, and an `S` command are outside this sketch's implementation scope. See [`docs/architecture.md`](docs/architecture.md) and [`docs/hardware.md`](docs/hardware.md).

## Repository map

```text
├── docs/                         thesis, inventory, architecture, hardware, validation
├── firmware/                     uploaded Arduino sketch and observed contract
├── kaggle/benchmarks/            uploaded CSV/configuration/plots and image mosaics
├── media/                        project photo, screenshots, banner, and demo video
├── results/                      source-specific result records and evidence templates
├── src/industrial_inspection/    curated inventory/metric/benchmark utilities
├── scripts/                      Kaggle staging and benchmark-summary tools
├── tests/                        tests for curated Python utilities
├── data/, models/, notebooks/    external-artifact instructions; no data or weights
└── src/{vision,control,monitoring}/ implementation boundaries
```

## Reproduce the repository checks

```bash
python -m venv .venv
source .venv/bin/activate                 # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest -q
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

To inventory a local Kaggle download without committing it:

```bash
python -m industrial_inspection.dataset_report \
  data/raw/industrial-inspection-system \
  --class-names bottle cap label liquid \
  --output artifacts/dataset_report.json
```

These commands test curation utilities and summarize an existing CSV. They do not rerun model inference or certify hardware.

Rebuild the annotated thesis copy from the checksum-verified original with:

```bash
python -m pip install -e ".[pdf]"
python scripts/build_updated_thesis.py
```

## Documentation

- [Original thesis](docs/Project%20Research.pdf) and [updated metrics and firmware edition](docs/Project%20Research%20-%20Updated%20Metrics%20and%20Firmware.pdf)
- [Thesis update notes and provenance](docs/thesis-update-notes.md)
- [Artifact inventory](docs/artifact-inventory.md)
- [Architecture and evidence boundaries](docs/architecture.md)
- [Hardware and firmware integration record](docs/hardware.md)
- [Validation protocol](docs/validation.md)
- [Source-specific results](results/kaggle-benchmark-snapshot.md)
- [Limitations](docs/limitations.md)
- [Reproducibility](docs/reproducibility.md)
- [External artifact policy](docs/artifact-storage.md)

## Current limitations

The validation split is small; model weights and the exact notebook/environment are external; the available records reference `yolov8l-worldv2`, YOLO-World, and YOLOv11m; raw timing and item-level trial logs are absent; and media is illustrative. The uploaded sketch defines the current firmware parameters documented in this repository. Predictive-maintenance values were generated through virtual sensing and are not field-failure prediction metrics.
