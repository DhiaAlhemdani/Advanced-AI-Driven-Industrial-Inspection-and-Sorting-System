# Models

Kaggle version 10 lists `benchmarks/weights/best.pt` and the public notebook loads it for validation/inference, but the weight is intentionally not included in this commit. The exact model provenance is also unresolved because the notebook training cell uses `yolo11m.pt` while the benchmark README labels the exported detector `YOLOv8l-Worldv2`. When adding an export, record:

- training source commit and dataset version/hash;
- model family and exact configuration;
- preprocessing and augmentation;
- confidence and IoU thresholds;
- class order (`bottle`, `cap`, `label`, `liquid` if unchanged);
- export/runtime version;
- license and file checksum.

A model file alone is not sufficient evidence for detection performance. Link the reproducible evaluation command and the thesis/benchmark record that produced each reported number.
