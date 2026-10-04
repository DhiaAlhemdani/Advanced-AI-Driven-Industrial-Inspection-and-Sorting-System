# Thesis, benchmark, and Kaggle results record

This page lists each result with its measurement type, source, and evaluation context. Detection, runtime inspection, physical routing, timing, and simulated maintenance values are kept as distinct result categories.

## Source records

- Thesis: [`docs/Project Research.pdf`](../docs/Project%20Research.pdf), SHA-256 `8dee0b3dbc63031ca2e850f971fe0cfc85b40e3f688d5b190fabdf36dd1d03ed`
- Updated thesis edition: [`docs/Project Research - Updated Metrics and Firmware.pdf`](../docs/Project%20Research%20-%20Updated%20Metrics%20and%20Firmware.pdf)
- Uploaded training bundle: [`kaggle/benchmarks/`](../kaggle/benchmarks/)
- Dataset: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>
- Main notebook: <https://www.kaggle.com/code/dhiaalhemdani/advanced-ai-driven-quality-control-system>
- Quick Inference: <https://www.kaggle.com/code/dhiaalhemdani/quick-inference>

Page references give the thesis's printed page followed by the PDF page where useful.

## 1. Object-detection metrics

These are model-versus-annotation **box detection** metrics. They do not measure the physical destination of a bottle.

| Source / run | Images / instances | Precision | Recall | mAP@0.50 | mAP@0.50:0.95 | Selection context |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Uploaded `results.csv`, final epoch 121 | Not encoded in CSV | **97.367%** | **98.584%** | **99.414%** | **94.317%** | Exact final row |
| Uploaded `results.csv`, best mAP@0.50:0.95 row, epoch 117 | Not encoded in CSV | 95.780% | 98.816% | 99.389% | **94.441%** | Metric-selected row |
| Uploaded artifacts, peak values | Not encoded in CSV | 97.367% (e121) | 100.000% (first at e55) | 99.414% (first at e90) | 94.441% (e117) | Independently selected peaks |
| Kaggle Quick Inference | 24 / 83 | 98.1% | 95.7% | 96.47% | 92.12% | Notebook validation output |

The uploaded PR plot reports AP@0.50 of bottle **0.992**, cap **0.995**, label **0.995**, liquid **0.994**, and all classes **0.994**. The F1 curve reports all-class **F1 0.97 at confidence 0.609**.

### Training configuration record

`args.yaml` records task `detect`, a model path ending in `yolov8l-worldv2.pt`, 640-pixel images, batch 4, AdamW, cosine learning rate, multi-scale training, IoU 0.7, a nominal 200 epochs, and a one-hour time limit. The CSV contains 121 epoch rows. The thesis and notebook also document YOLO-World and YOLOv11/YOLOv11m components. Weights and an environment lockfile remain external.

## 2. Runtime inspection results

The thesis reports an **85–95% overall inspection/classification range** in the abstract and printed pp. 125–126. This result describes integrated runtime inspection and is listed independently from annotation-based detector metrics and physical route rates.

Printed pp. 105–106 also present a three-class container summary with 100 compliant, 110 rework, and 35 scrap samples. The original item-level decision log is not included in the repository.

## 3. Physical sorting counts and calculated rates

The thesis describes 245 items across five scenarios. Rates below are calculated directly from the published tested and routed counts.

| Scenario | Tested | Routed count | Count-derived rate |
| --- | ---: | ---: | ---: |
| SC-01 compliant / pass | 100 | 100 | 100.00% |
| SC-02 missing cap / rework | 40 | 40 | 100.00% |
| SC-03 missing label / rework | 35 | 35 | 100.00% |
| SC-04 label skew / rework | 35 | 35 | 100.00% |
| SC-05 fluid defect / scrap | 35 | 20 | **57.14%** |
| Overall | 245 | 230 | **93.88%** |

“Routed count” is retained as the source table's term. Independent reproduction requires an item-level record containing expected and observed lanes, exclusions, and hardware/software revisions.

## 4. Timing and throughput records

| Measurement | Value | Scope |
| --- | ---: | --- |
| Frame ingestion | 4.2 ms average | Thesis host-side component, stated over 245 iterations |
| YOLO inference | 12.8 ms average | Thesis host-side component |
| OpenCV filtering | 3.5 ms average | Canny/Hough/Otsu aggregate |
| Serial write | 0.1 ms average | Thesis host-side component |
| Computational decision total | **20.6 ms** | Sum of the four host-side components |
| End-to-end capture-to-deflection | **2–4 s** | Thesis field-of-view entry through completed physical deflection |
| Uploaded-sketch active hold | **500 ms** | `HOLD_TIME` after sensor-triggered actuation |
| Nominal throughput | 30 bottles/min | Thesis Chapter 5 operating point |

Raw synchronized timing samples are not included in this repository.

## 5. Predictive-maintenance values

The thesis identifies a **Virtual Sensing Simulation Protocol**. It reports example health/failure calculations: nominal **94.20% / 16.44%**, warning **55.78% / 82.64%**, and critical **9.84% / 99.90%**, plus 120 simulated telemetry samples in Table 7:5. These are formula and dashboard-state outputs rather than field prediction metrics.

## Reproduce the CSV extraction

```bash
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

This reads the uploaded CSV. Re-running model evaluation requires the Kaggle-hosted weights, data/labels, original notebook, exact environment, and validation command.
