# Models

Kaggle version 10 lists `benchmarks/weights/best.pt`, and the public notebook loads it for validation/inference. The weight is intentionally not included in this repository. Available records reference `yolov8l-worldv2.pt`, YOLO-World, YOLOv11, and `yolo11m.pt`; preserve the exact source context when adding any model export.

Record:

- training source commit and dataset version/hash;
- model family and exact configuration;
- preprocessing and augmentation;
- confidence and IoU thresholds;
- class order (`bottle`, `cap`, `label`, `liquid` if unchanged);
- export/runtime version;
- license and file checksum.

A model file alone is not sufficient evidence for detection performance. Link the reproducible evaluation command and source record for every reported number.
