# Kaggle artifact boundary

Canonical dataset: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

The version-10 record reports 232.66 MB, 501 files, 119 images (95 train / 24 validation), four classes, detection/segmentation labels, LabelMe annotations, metadata, a benchmark directory, and model weights.

## Committed here

- `data_detect.yaml` and `data_segment.yaml` class/split snapshots;
- `benchmarks/results.csv`, `args.yaml`, and `settings.json`;
- benchmark curves, confusion matrices, result/label plots, and train/validation mosaics.

These uploaded benchmark files are inventoried in [`../docs/artifact-inventory.md`](../docs/artifact-inventory.md) and reported by source in [`../results/kaggle-benchmark-snapshot.md`](../results/kaggle-benchmark-snapshot.md). Paths inside configuration files are retained for provenance and are not portable.

## Kept external on Kaggle

Training images, detection labels, segmentation labels, LabelMe JSON, `metadata.csv`, original notebook export, and model weights remain external. Pin the dataset/notebook version and checksum any local download used for reproduction.

## Result categories

The uploaded training CSV, Quick Inference notebook, integrated runtime inspection range, and physical route counts are documented as separate measurement categories. Detection and physical routing retain their own denominators and evidence requirements.
