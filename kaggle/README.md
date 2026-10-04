# Kaggle artifact snapshot

This directory preserves small, text-based configuration artifacts from the public Kaggle dataset **Industrial Inspection System**, version 10:

<https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

The dataset page reports version 10, 232.66 MB, 501 files, and the following artifact groups:

```text
annotations_labelme/{train,val}/   # LabelMe/X-AnyLabeling JSON
benchmarks/                         # args, results, plots, confusion matrices, weights
images/{train,val}/                 # 119 JPG images
labels/{train,val}/                 # YOLO detection boxes
labels_seg/{train,val}/             # YOLO segmentation polygons
data_detect.yaml
data_segment.yaml
metadata.csv
README.md
```

The two YAML files in this directory are captured from the dataset version 10 file view. They preserve the class order and split paths, but their absolute Kaggle path is only valid inside Kaggle. Use a repository-local path in a local run.

## Artifact handling policy

- Text configurations are small enough to version here.
- The original notebook is referenced in [`../notebooks/README.md`](../notebooks/README.md) and should be materialized byte-for-byte with the fetch workflow before being split into modules.
- Labels, polygon annotations, `metadata.csv`, and benchmark CSVs should be ingested with [`../scripts/fetch_kaggle_artifacts.py`](../scripts/fetch_kaggle_artifacts.py) when the Kaggle CLI/network is available.
- Images, media, and model weights are intentionally not copied into this commit. The project owner will upload those separately using the artifact policy in [`../docs/artifact-storage.md`](../docs/artifact-storage.md).
- No weight file or hardware media is represented as present merely because the Kaggle page lists it.

## Provenance

- Dataset owner: Deiaa Ahmed Abdo Lootf (`dhiaalhemdani`)
- Dataset current version at inspection: 10
- Dataset last-updated value exposed by Kaggle: 2026-10-03
- Dataset license exposed by Kaggle: MIT
- Dataset API view: `https://www.kaggle.com/api/v1/datasets/view/dhiaalhemdani/industrial-inspection-system`
