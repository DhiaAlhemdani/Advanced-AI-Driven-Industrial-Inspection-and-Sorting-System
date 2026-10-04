# Limitations and responsible claims

## Dataset and detector

- The reported dataset has 119 images with 24 validation images. Results from one small split may be sensitive to scene repetition, lighting, camera pose, and bottle identity.
- Training data, labels, annotations, the notebook, and weights remain on Kaggle. This checkout cannot independently rerun inference.
- Available records reference `yolov8l-worldv2.pt`, YOLO-World, YOLOv11, and `yolo11m.pt`; every result should retain its source configuration.
- The uploaded CSV does not encode the validation image/instance count. Quick Inference records 24 images and 83 instances.
- Peak metrics selected independently across epochs do not describe one checkpoint; final and selected-checkpoint rows are identified explicitly.
- Component-box mAP does not directly evaluate label skew, fill ratio, defect severity, bottle-level decisions, or routing.

## Numerical evidence boundaries

- The thesis's 85–95% result is an integrated runtime inspection range rather than an annotation-based detector metric.
- Physical rates in the updated edition are calculated from the published counts: 20/35 = 57.14% for SC-05 and 230/245 = 93.88% overall.
- An item-level route ledger and raw timer/logic-analyzer traces are not included, so independent physical-trial reproduction is not currently possible.

## Firmware and physical system

- The uploaded sketch defines the current repository firmware specification; a dated flashed-binary record is needed for trial provenance.
- The sketch uses 9600-baud polling, a 500 ms hold, 35° requested travel, per-route queues, and `A`/`B` commands.
- It does not implement acknowledgements, item IDs, pending timeouts, queue-overflow reports, an `S` command, conveyor control, or a communication-loss safe state.
- Pin numbers and requested servo angles require confirmation against a physical wiring and calibration record before powered operation.
- Prototype photographs, screenshots, and video are qualitative evidence rather than exhaustive trial logs.
- A laboratory prototype does not establish production safety, ingress protection, EMC tolerance, guarding, fail-safe operation, or regulatory compliance.

## Timing and throughput

- The documented 20.6 ms host-processing sum excludes bottle flight and completed mechanical routing; the 2–4 second value uses an end-to-end boundary.
- Hardware accelerator, timing instrumentation, clock synchronization, variance/percentiles, warm-up policy, and raw samples are not available.
- Throughput evaluation requires a per-item stress-test log with speed, spacing, route, and fault outcomes.

## Monitoring and predictive maintenance

- Dashboard counters and screenshots are snapshots rather than synchronized evidence of the 245-item trial.
- MQTT source, broker configuration, payload trace, duplicate/loss handling, and clock behavior are not committed.
- The thesis uses simulated vibration, temperature, and current. Health scores and failure probabilities demonstrate a formula/state machine rather than prediction against physical failures.
- No failure labels, temporal train/test split, false-alert analysis, calibration assessment, or remaining-useful-life evaluation is available.

## Reproducibility boundary

The Python tests cover curated dataset, metric, and CSV-summary utilities. They do not test the detector, original notebook, dashboard, MQTT path, electrical wiring, or physical sorter. Kaggle artifacts should remain externally versioned and checksum-identified for reproducible releases.
