# Reproducibility guide

## Repository utilities

The curated utilities support Python 3.10+ and use only the standard library at runtime; tests use pytest.

```bash
python -m venv .venv
source .venv/bin/activate                 # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest -q
python scripts/summarize_benchmark.py kaggle/benchmarks/results.csv
```

CI tests utilities and compiles Python source. It does not emulate or certify the camera, detector, Arduino, servos, MQTT broker, dashboard, or conveyor.

## External Kaggle artifacts

Canonical dataset: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

Keep training images, detection/segmentation labels, LabelMe annotations, metadata, original notebook, and weights outside normal Git. The repository record reports 119 images (95 train / 24 validation) and classes `bottle`, `cap`, `label`, `liquid`.

After downloading a pinned Kaggle version locally:

```bash
python -m industrial_inspection.dataset_report \
  data/raw/industrial-inspection-system \
  --class-names bottle cap label liquid \
  --output artifacts/dataset_report.json
```

Record Kaggle version, download date, archive/manifest SHA-256, file counts, class counts, and any resplitting. This inventory is not model evaluation.

## Uploaded benchmark provenance

The committed `kaggle/benchmarks/results.csv` has 121 epoch rows. `args.yaml` records a one-hour time limit and nominal 200 epochs, which can explain why the row count is shorter but does not prove run completion semantics. Machine-specific paths remain in the configuration for provenance.

The summary tool reports final and independently peaked values. To rerun validation rather than summarize history, obtain and hash the exact Kaggle-only weights, data, labels, notebook/source revision, and Python/Ultralytics/CUDA environment. Preserve the full command and output.

## Thesis and firmware provenance

The thesis and uploaded firmware hashes are listed in [`artifact-inventory.md`](artifact-inventory.md). The sketch does not match several thesis firmware claims. Preserve both records; do not edit the sketch to manufacture consistency. A reproducible hardware release needs:

- Arduino board/core and Servo library versions;
- sketch and compiled-binary hashes;
- host source revision and matching serial settings;
- wiring/power/mechanical revisions;
- a safe bring-up procedure;
- timestamped per-item command, sensor, actuation, and lane outcomes.

Compilation alone is not physical validation.

## Rebuild the annotated thesis revision

The original PDF is checksum-verified and never overwritten. To recreate the annotated 157-page revision:

```bash
python -m pip install -e ".[pdf]"
python scripts/build_revised_thesis.py
```

The generator adds visible banners to affected source pages and appends the controlling correction record. Its human-readable source summary is [`thesis-revision-notes.md`](thesis-revision-notes.md). Regeneration must fail if the original PDF hash or page count changes.

## Result reproduction hierarchy

1. **Artifact extraction:** rerun the CSV summary and verify hashes.
2. **Detector reevaluation:** run exact weights against an immutable split/config.
3. **Inspection replay:** execute detector plus OpenCV/rules against per-item ground truth.
4. **Hardware bench:** verify one command/sensor/actuator path safely.
5. **Physical trial:** log every item and actual lane under declared speed/geometry.
6. **End-to-end timing:** synchronize clocks and report distributions, not only averages.

Do not skip from level 1 to a claim about level 5.
