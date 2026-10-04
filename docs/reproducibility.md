# Reproducibility guide

## 1. Environment

The repository utilities support Python 3.10+ and have no runtime dependency beyond the standard library. Development tests use pytest.

```bash
python -m venv .venv
source .venv/bin/activate                 # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest -q
```

The CI workflow checks these utilities only. It does not emulate the camera, Arduino, servos, MQTT broker, dashboard, or maintenance model.

## 2. Dataset provenance

Canonical source: <https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

The project record currently states:

- 119 images;
- 95 training images and 24 validation images;
- four classes: `bottle`, `cap`, `label`, and `liquid`.

Download and unpack the dataset locally. Do not commit raw images:

```bash
mkdir -p data/raw/industrial-inspection-system
# Download from the Kaggle page using the method appropriate to your account.
# Unpack the export into data/raw/industrial-inspection-system/.

python -m industrial_inspection.dataset_report \
  data/raw/industrial-inspection-system \
  --class-names bottle cap label liquid \
  --output artifacts/dataset_report.json
```

The report is a file inventory and YOLO-label sanity check. It is not a model evaluation. Preserve the generated JSON with the experiment record if its counts are used in a result claim. Record the Kaggle download date/version and a SHA-256 hash of the archive or a stable manifest.

## 3. Original implementation

The original integration notebook is public on Kaggle and is documented in [`../notebooks/README.md`](../notebooks/README.md). It contains the CV training/inference flow, host-side serial actuation branch, defect-source rules, predictive-maintenance heuristic, MQTT callbacks, Dash dashboard, and Flask video stream. The Arduino board firmware itself is not present.

Preserve the exact notebook export first, then add split modules in the boundaries described by the repository map rather than silently replacing the source with a reconstruction. For each runnable experiment, record:

- source commit;
- Python/Arduino/runtime versions;
- dataset version/hash and split;
- model configuration and weights checksum;
- preprocessing, confidence, and IoU settings;
- hardware revision and wiring assumptions;
- broker and topic configuration, redacted as needed;
- output artifact paths.

See [`source-integrity.md`](source-integrity.md) before importing files from another copy.

## 4. Validation commands

A complete evidence drop should make the following commands or their exact project-specific equivalents reproducible:

```bash
# Dataset inventory
python -m industrial_inspection.dataset_report <dataset-root> \
  --class-names bottle cap label liquid \
  --output artifacts/dataset_report.json

# Software checks
pytest -q

# Vision evaluation: add the original implementation command here.
# Physical sorter trial: add the bench procedure and log path here.
# MQTT/dashboard replay: add the sanitized replay command here.
```

Do not fill the last three lines with guessed commands. They should point to the actual implementation and evidence.

## 5. Reproducibility checklist

- [ ] Dataset export and split are identified.
- [ ] The training/evaluation source commit is recorded.
- [ ] Model artifact and checksum are recorded.
- [ ] Detection metric configuration is recorded.
- [ ] Physical trial item count and route/bin definitions are recorded.
- [ ] Hardware firmware and board revision are recorded.
- [ ] MQTT payloads are sanitized and replayable, or the limitation is stated.
- [ ] Thesis section and benchmark-log row are cited for every headline number.
