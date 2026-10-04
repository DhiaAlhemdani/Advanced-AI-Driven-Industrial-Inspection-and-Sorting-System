# Kaggle benchmark snapshot — requires thesis reconciliation

This page records what is currently published on Kaggle version 10 and the two related notebooks. It is **not** the final validated results table. The thesis PDF and raw benchmark files are still required before a headline number is presented as authoritative.

## Source records

- Dataset: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>
- Main notebook: <https://www.kaggle.com/code/dhiaalhemdani/advanced-ai-driven-quality-control-system>
- Quick inference notebook: <https://www.kaggle.com/code/dhiaalhemdani/quick-inference>
- Dataset version observed: 10

## Detection results published by the dataset README/main notebook

| Metric | Published value | Measurement type |
| --- | ---: | --- |
| Precision (box) | 97.37% | Validation detector metric |
| Recall | 100.00% peak / 98.58% final | Validation detector metric |
| mAP@50 | 99.41% | Validation detector metric |
| mAP@50–95 | 94.44% | Validation detector metric |

The dataset README describes these values as `YOLOv8l-Worldv2` results at 640×640 with AdamW, cosine learning rate scheduling, and multi-scale training.

## Quick-inference notebook output

The public Quick Inference notebook output shows a separate validation run over 24 images and 83 instances:

| Metric | Notebook output |
| --- | ---: |
| Precision | 0.981 |
| Recall | 0.957 |
| mAP@50 | 0.9647 |
| mAP@50–95 | 0.9212 |

These values do not match the dataset README/main-notebook headline values. They must remain separate until the model weight, Ultralytics version, evaluator configuration, and benchmark CSV are reconciled.

## Physical sorting arithmetic check

The dataset README publishes the following scenario table:

| Scenario | Tested | Correct | Published accuracy | Recomputed from counts |
| --- | ---: | ---: | ---: | ---: |
| SC-01 compliant/pass | 100 | 100 | 100.00% | 100.00% |
| SC-02 missing cap/rework | 40 | 40 | 100.00% | 100.00% |
| SC-03 missing label/rework | 35 | 35 | 100.00% | 100.00% |
| SC-04 label skew/rework | 35 | 35 | 100.00% | 100.00% |
| SC-05 fluid defect/scrap | 35 | 20 | 62.00% | **57.14%** |
| Overall | 245 | 230 | 93.88% / 95.0% | **93.88%** |

The SC-05 published percentage does not equal 20/35, and the overall `95.0%` value has no denominator or exclusion rule in the public table. The repository will not silently promote either value to a verified claim.

## Latency

The public source gives a computational latency sum of 4.2 ms capture + 12.8 ms YOLO + 3.5 ms OpenCV + 0.1 ms serial = **20.6 ms**, measured over 245 iterations. The raw latency log is still required.

## Required reconciliation with the thesis

Before moving any value into `README.md` as a headline result, compare this snapshot with:

- the thesis table/page;
- `benchmarks/results.csv` and `benchmarks/args.yaml`;
- the exact `best.pt` checksum;
- the exact validation command and Ultralytics version;
- the physical trial log and route ground truth.
