# Thesis, benchmark, and Kaggle result reconciliation

This is an evidence comparison, not a declaration that one source is authoritative. The thesis, uploaded benchmark bundle, Kaggle dataset README, and Quick Inference notebook describe different measurements and contain unresolved contradictions.

## Source records

- Thesis: [`docs/Project Research.pdf`](../docs/Project%20Research.pdf), SHA-256 `8dee0b3dbc63031ca2e850f971fe0cfc85b40e3f688d5b190fabdf36dd1d03ed`
- Uploaded training bundle: [`kaggle/benchmarks/`](../kaggle/benchmarks/)
- Dataset README: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system> (version 10 at the prior audit)
- Main notebook: <https://www.kaggle.com/code/dhiaalhemdani/advanced-ai-driven-quality-control-system>
- Quick Inference: <https://www.kaggle.com/code/dhiaalhemdani/quick-inference>

Page references below give the thesis's printed page followed by the PDF page where useful.

## 1. Object-detection metrics

These are model-vs-annotation **box detection** metrics. They do not measure whether a bottle reached the correct physical lane.

| Source / run | Images / instances | Precision | Recall | mAP@0.50 | mAP@0.50:0.95 | Notes |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Uploaded `results.csv`, final epoch 121 | Not encoded in CSV | **97.367%** | **98.584%** | **99.414%** | **94.317%** | Exact final row. |
| Uploaded `results.csv`, best mAP@0.50:0.95 row (epoch 117) | Not encoded in CSV | 95.780% | 98.816% | 99.389% | **94.441%** | Metric-selected row, not the final row. |
| Uploaded artifacts, peak values across independent epochs | Not encoded in CSV | 97.367% (e121) | 100.000% (first at e55; also reached later) | 99.414% (first at e90) | 94.441% (e117) | Peaks must not be represented as one checkpoint row. |
| Kaggle dataset README/main-notebook headline | Not stated with the headline | 97.37% | 100.00% peak / 98.58% final | 99.41% | 94.44% | Matches rounded, independently selected peaks/final values from the uploaded CSV. |
| Quick Inference notebook validation | 24 / 83 | 98.1% | 95.7% | 96.47% | 92.12% | Separate public evaluation output; lower mAP than the training bundle. |

The uploaded PR plot reports AP@0.50 of bottle **0.992**, cap **0.995**, label **0.995**, liquid **0.994**, and all classes **0.994**. The F1 curve reports all-class **F1 0.97 at confidence 0.609**. Those values are plot annotations, not additional physical tests.

### Configuration attached to the uploaded training bundle

`args.yaml` records task `detect`, model path ending in `yolov8l-worldv2.pt`, 640-pixel images, batch 4, AdamW, cosine learning rate, multi-scale training, IoU 0.7, a nominal 200 epochs, and a one-hour time limit. The CSV stops after 121 rows. The settings contain machine-specific Windows paths, and no weights or environment lockfile are present, so this checkout cannot rerun the evaluator.

The thesis instead describes YOLO-World and YOLOv11m/YOLOv11 in its abstract and Chapters 4–5, while the public notebook has also been observed loading `yolo11m.pt`. Model identity therefore remains unresolved; do not combine these records into a single model claim.

## 2. Thesis runtime inspection claims

The thesis reports an **85–95% overall inspection/classification accuracy range** in the abstract (PDF pp. 5–6) and printed pp. 125–126 (PDF pp. 141–142). It attributes variability primarily to lighting/reflection and transparent liquid. This is not defined as precision, recall, or mAP, and no correct/total count is supplied for that range. It is an integrated runtime claim, not interchangeable with the box metrics above.

Printed pp. 105–106 (PDF pp. 121–122) separately present a three-class container matrix with 100 compliant, 110 rework, and 35 scrap predictions all on the diagonal, then claim 100% sensitivity and precision. That 245/245 matrix conflicts with:

- the 85–95% runtime inspection range;
- the physical sorting table's 230 routed units; and
- the statement that fluid inspection was the weakest case.

The repository preserves all claims and flags the conflict rather than selecting the largest value.

## 3. Physical sorting arithmetic

These rows are presented in thesis Table 6:5, printed p. 99 (PDF p. 115), and reproduced in the Kaggle README. They concern **physical route outcomes**, not detector mAP.

| Scenario | Tested | Thesis/Kaggle “routed” | Published accuracy | Recomputed from counts |
| --- | ---: | ---: | ---: | ---: |
| SC-01 compliant / pass | 100 | 100 | 100.00% | 100.00% |
| SC-02 missing cap / rework | 40 | 40 | 100.00% | 100.00% |
| SC-03 missing label / rework | 35 | 35 | 100.00% | 100.00% |
| SC-04 label skew / rework | 35 | 35 | 100.00% | 100.00% |
| SC-05 fluid defect / scrap | 35 | 20 | 62.00% | **57.14%** |
| Overall | 245 | 230 | 95.00% (Kaggle also reports 93.88%) | **93.88%** |

The row counts sum correctly (`100 + 40 + 35 + 35 + 35 = 245`; routed `100 + 40 + 35 + 35 + 20 = 230`), but two printed percentages do not. The same page calls the record “flawless,” and the abstract and printed p. 107 claim 100% physical sorting. Those narratives contradict the table. Without the item-level trial ledger, the most reproducible statement is: **the published counts imply 230/245 = 93.88%, with SC-05 at 20/35 = 57.14%; the thesis nevertheless also claims 95% and 100%.**

“Routed units” is not defined tightly enough to determine whether it means correct destination, any diversion, or another event. It is therefore not promoted to verified sorting accuracy.

## 4. Timing and throughput claims

| Measurement | Thesis value | Source / scope | Repository interpretation |
| --- | ---: | --- | --- |
| Frame ingestion | 4.2 ms average | printed p. 95 (PDF p. 111), stated over 245 iterations | Computational component; raw timer log absent. |
| YOLO inference | 12.8 ms average | same | Hardware accelerator not identified in the result table. |
| OpenCV filtering | 3.5 ms average | same | Canny/Hough/Otsu aggregate. |
| Serial write | 0.1 ms average | printed p. 96 (PDF p. 112) | Thesis configuration says 115200 bps; uploaded sketch says 9600 bps. |
| Computational decision total | **20.6 ms** | 4.2 + 12.8 + 3.5 + 0.1 | Arithmetic is correct; not end-to-end latency. |
| ISR response | <3.2 µs | printed p. 98 (PDF p. 114) | Uploaded sketch uses polling and defines no ISR; not verified by this firmware. |
| Servo sweep | 68 ms | same | Raw logic-analyzer trace absent. |
| Thesis dwell | 250 ms | same | Uploaded sketch uses `HOLD_TIME = 500` ms. |
| End-to-end capture-to-deflection | **2–4 s** | printed p. 126 (PDF p. 142) | Distinct from 20.6 ms computational latency. |
| Nominal throughput | 30 bottles/min | Chapter 5 | Thesis claim. |
| Perfect sorting through | 45 bottles/min | printed p. 106 (PDF p. 122) | Contradicted by Table 6:5; raw stress log absent. |
| Mechanical overlap/slip observed | 60 bottles/min | same | Thesis observation; not reproduced here. |

## 5. Predictive-maintenance numbers

The thesis explicitly describes a **Virtual Sensing Simulation Protocol** (printed p. 87, PDF p. 103), not a learned predictive-maintenance model evaluated on physical failure labels. It reports example health/failure calculations: nominal **94.20% / 16.44%**, warning **55.78% / 82.64%**, and critical **9.84% / 99.90%**, plus 120 simulated telemetry samples in Table 7:5. These numbers validate the behavior of a formula and dashboard state transitions only; they are not predictive accuracy, false-alert rate, remaining useful life, or field reliability.

## Reproduce the CSV extraction

```bash
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

This reads the uploaded CSV only. Reproducing the model evaluation still requires the Kaggle-only weights, data/labels, original notebook, exact environment, and validation command.
