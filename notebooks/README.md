# Original Kaggle notebooks

## Advanced AI-Driven Quality Control System

- Notebook: <https://www.kaggle.com/code/dhiaalhemdani/advanced-ai-driven-quality-control-system>
- Notebook API source: `https://www.kaggle.com/api/v1/kernels/pull?user_name=dhiaalhemdani&kernel_slug=advanced-ai-driven-quality-control-system`
- Current Kaggle notebook version observed: **2**
- Latest run exposed by Kaggle: **2026-10-01**, successful, approximately 8 seconds
- Dataset input: `dhiaalhemdani/industrial-inspection-system`
- Language: Python
- Kernel type: Notebook

The notebook is the original integration source for the CV training/inference flow, geometric inspection heuristics, simulated/serial actuation, defect-source rules, predictive maintenance, MQTT, Dash/Plotly, and Flask MJPEG streaming. It is intentionally not silently rewritten into a set of new modules: first preserve the exact notebook export, then split it with an import map and tests.

## Notebook module map captured from the Kaggle source

| Notebook section | Role | Extraction target |
| --- | --- | --- |
| Global environment | Imports and runtime dependencies | `src/vision/`, `src/monitoring/`, `pyproject.toml` |
| Dataset Visualizer | YOLO box rendering and split audit | `src/vision/visualization.py` |
| YOLO Model Training | Ultralytics training configuration | `src/vision/train.py` and `configs/` |
| Training Results | Plot discovery and rendering | `scripts/` or `src/vision/visualization.py` |
| Test Trained Model | Validation/inference visualization | `src/vision/infer.py` |
| Diverters Actuation | Serial command path and simulation | `src/control/` and `firmware/` |
| Defect Source Identification | Rule-based root-cause model | `src/monitoring/defect_source.py` |
| Predictive Maintenance | Sensor schema, thresholds, health score | `src/monitoring/predictive_maintenance.py` |
| Interactive Dashboard | MQTT callbacks and Dash UI | `src/monitoring/dashboard.py` |
| AI Vision Inspection Logic | ROI, tracking, component heuristics | `src/vision/inspection.py` |
| System Operations | Flask/MQTT/PM/vision threads | `src/app.py` or explicit launch services |

## Important source notes

- The notebook uses both `YOLO("yolo11m.pt")` in a training cell and benchmark `best.pt` weights described as `YOLOv8l-Worldv2` elsewhere. This model identity must be resolved against the thesis and benchmark files before publishing a single headline model claim.
- The notebook contains simulation defaults (`USE_ARDUINO = False`, `USE_SIMULATION = True`) as well as serial/hardware branches. Notebook execution is not evidence that the physical branches were tested.
- The notebook contains environment-specific addresses such as `localhost`, `COM3`, `COM4`, `127.0.0.1`, and a LAN camera URL. These must become configuration values before a portable repository runtime is claimed.

## Exact fetch workflow

Run this from a machine with the Kaggle CLI configured:

```bash
python -m pip install kaggle
kaggle kernels pull dhiaalhemdani/advanced-ai-driven-quality-control-system \
  -p staging/kaggle/notebooks/advanced-ai-driven-quality-control-system \
  --metadata
```

The repository ingestion script also records the dataset version and copies non-media artifacts. Do not replace the original notebook with a hand-reconstructed equivalent.
