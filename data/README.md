# Data

Raw data is not committed to this repository. Use the canonical Kaggle source:

<https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

The project record describes **119 images**, split into **95 training** and **24 validation** images, with four component classes: `bottle`, `cap`, `label`, and `liquid`. Verify those values locally after downloading the export:

```bash
python -m industrial_inspection.dataset_report \
  data/raw/industrial-inspection-system \
  --class-names bottle cap label liquid \
  --output artifacts/dataset_report.json
```

Do not commit the downloaded images or any private source files. If the Kaggle export changes, record the download date, dataset version/hash, directory layout, and any re-splitting in the reproducibility record.
