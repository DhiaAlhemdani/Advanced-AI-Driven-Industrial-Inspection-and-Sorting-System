# Kaggle artifact boundary

Canonical dataset: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

The prior version-10 audit reported 232.66 MB, 501 files, 119 images (95 train / 24 validation), four classes, detection/segmentation labels, LabelMe annotations, metadata, a benchmark directory, and model weights.

## Committed here

- `data_detect.yaml` and `data_segment.yaml` class/split snapshots;
- `benchmarks/results.csv`, `args.yaml`, and `settings.json`;
- benchmark curves, confusion matrices, result/label plots, and train/validation mosaics.

These uploaded benchmark files are inventoried in [`../docs/artifact-inventory.md`](../docs/artifact-inventory.md) and numerically reconciled in [`../results/kaggle-benchmark-snapshot.md`](../results/kaggle-benchmark-snapshot.md). Paths inside configuration files are retained for provenance and are not portable.

## Kept external on Kaggle

Training images, detection labels, segmentation labels, LabelMe JSON, `metadata.csv`, original notebook export, and model weights remain external. Do not imply that a listed Kaggle file is present in Git. Pin the dataset/notebook version and checksum any local download used for reproduction.

## Important comparison

The dataset README's rounded detector headline aligns with values selected from the uploaded training CSV, while the Quick Inference notebook reports a separate run over 24 images / 83 instances with lower mAP. The dataset README also reproduces the thesis physical-sorting table, whose percentages and “flawless” narrative conflict with its counts. Detection and physical routing are documented separately.
