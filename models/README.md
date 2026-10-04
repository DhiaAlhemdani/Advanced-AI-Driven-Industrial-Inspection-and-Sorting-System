# Models

No trained weights or model configuration are included in the current checkout. When adding an export, record:

- training source commit and dataset version/hash;
- model family and exact configuration;
- preprocessing and augmentation;
- confidence and IoU thresholds;
- class order (`bottle`, `cap`, `label`, `liquid` if unchanged);
- export/runtime version;
- license and file checksum.

A model file alone is not sufficient evidence for detection performance. Link the reproducible evaluation command and the thesis/benchmark record that produced each reported number.
