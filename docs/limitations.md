# Limitations and responsible claims

## Dataset and detector

- The reported dataset has 119 images with only 24 validation images. Results from one small split may be sensitive to leakage, scene repetition, lighting, camera pose, and bottle identity.
- The training data, labels, annotations, notebook, and weights remain on Kaggle. This checkout cannot rerun inference or verify the weight used by either published evaluation.
- Sources name `yolov8l-worldv2.pt`, YOLO-World, YOLOv11, and `yolo11m.pt`; exact model lineage is unresolved.
- The uploaded CSV and plots are internally useful but do not encode the validation image/instance count. Quick Inference reports 24 images and 83 instances and produces different metrics.
- Selecting peak precision, recall, and mAP from different epochs does not describe one checkpoint.
- High component-box mAP does not validate label skew, fill ratio, defect severity, bottle-level decisions, or routing.

## Numerical contradictions

- Thesis runtime inspection accuracy is stated as a broad 85–95% range without item counts or a standard metric definition.
- A thesis three-class matrix claims 245/245 and 100% precision/sensitivity, conflicting with the 85–95% range and sorting table.
- Sorting Table 6:5 reports SC-05 as 20/35 but prints 62% (arithmetic: 57.14%). It reports 230/245 but prints 95% (arithmetic: 93.88%). Nearby prose and the abstract nevertheless claim flawless/100% sorting.
- The raw per-item route ledger and timer/logic-analyzer traces are absent, so these conflicts cannot be resolved from aggregate prose.

## Firmware and physical system

- The uploaded sketch is source evidence, not proof that this exact revision was flashed for thesis trials.
- Its 9600-baud polling design, 500 ms dwell, 35° requested travel, queue behavior, and supported commands differ materially from the thesis's 115200-baud ISR/timer design, 250 ms dwell, 45–50° sweep, and `S` emergency command.
- The sketch has no acknowledgements, item IDs, pending timeout, queue-overflow reporting, emergency stop, conveyor control, or explicit communication-loss safe state.
- Pin numbers and servo angles have not been reconciled with a wiring diagram. Requested angles do not establish mechanical positions or safe travel.
- Prototype photographs, screenshots, and video show/demonstrate a system but are not exhaustive trial logs and cannot establish denominators, exclusions, repeatability, or long-duration reliability.
- A laboratory prototype does not establish production safety, ingress protection, EMC tolerance, guarding, fail-safe operation, or regulatory compliance.

## Timing and throughput

- The reported 20.6 ms computational sum excludes bottle flight and completed mechanical routing; the thesis separately reports 2–4 seconds end to end.
- Hardware accelerator, timing instrumentation, clock synchronization, variance/percentiles, warm-up policy, and raw samples are not available.
- Claims of perfect operation through 45 bottles/min conflict with the aggregate sorting table and lack a stress-test log.

## Monitoring and predictive maintenance

- Dashboard counters and screenshots are snapshots, not synchronized evidence of the 245-item trial.
- MQTT source, broker configuration, payload trace, duplicate/loss handling, and clock behavior are not committed.
- The thesis explicitly uses simulated vibration, temperature, and current. Health scores and failure probabilities demonstrate a formula/state machine, not prediction performance against physical failures.
- No failure labels, temporal train/test split, false-alert analysis, calibration assessment, or remaining-useful-life evaluation is available.

## Reproducibility boundary

The Python tests cover curated dataset/metric/CSV-summary utilities only. They do not test the detector, original notebook, dashboard, MQTT path, firmware compilation, electrical wiring, or physical sorter. Keep the Kaggle-only artifacts external, but record immutable versions and checksums when producing a reproducible release.
