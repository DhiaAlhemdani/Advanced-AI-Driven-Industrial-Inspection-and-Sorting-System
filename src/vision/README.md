# Computer-vision implementation boundary

Place the **original** training, inference, preprocessing, and model-export files here when they are supplied by the project owner. Preserve their provenance and cite the exact thesis section or commit in [`docs/source-integrity.md`](../../docs/source-integrity.md).

The original vision implementation is currently available as the public Kaggle notebook documented in [`../../notebooks/README.md`](../../notebooks/README.md), but its exact `.ipynb` export has not yet been committed here. Preserve it before extraction. Do not infer the final model family from one cell: the notebook uses `yolo11m.pt` in a training cell while the benchmark snapshot names `YOLOv8l-Worldv2` for `best.pt`. The dataset inventory utility under `src/industrial_inspection/` is a curation aid, not a reconstructed inspection pipeline.
