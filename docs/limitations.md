# Limitations and responsible claims

## Dataset and vision

- The reported dataset contains 119 images, with 95 training and 24 validation images. This is a small validation surface for a deployment claim.
- A single validation split can hide sensitivity to lighting, camera pose, bottle geometry, backgrounds, and conveyor motion.
- The four component classes describe the annotation vocabulary; they do not, by themselves, define defect severity, acceptable quality, or route logic.
- No model architecture, training configuration, confidence threshold, IoU policy, or benchmark output is available in this checkout.
- Dataset counts and annotation counts do not measure detection quality.

## Physical system

- Detection performance does not measure conveyor timing, servo repeatability, mechanical interference, or route correctness.
- Physical sorting accuracy requires a logged denominator and ground truth for every inspected item.
- Without the original firmware and wiring record, pin assignments, servo angles, timing, and safe-state behavior must remain unspecified.
- A lab demonstration does not establish production throughput, safety compliance, long-duration reliability, or operation under changing lighting and contamination.

## Monitoring and predictive maintenance

- MQTT connectivity and a dashboard provide observability; they do not automatically make a system predictive-maintenance capable.
- Predictive maintenance needs time-stamped condition signals, a defined failure/maintenance label, a time-aware evaluation protocol, and a documented alert policy.
- No maintenance time series, failure labels, feature set, model, or false-alert analysis is available in this checkout.
- Broker outages, clock drift, duplicated messages, stale commands, and missing telemetry need explicit handling in the original implementation.

## Scope of this curation

The added Python utilities validate repository evidence and compute simple metric primitives. They are not the original model, firmware, dashboard, or hardware test harness. Until the missing artifacts are added, the strongest defensible claims are the supplied project scope, the public dataset reference, and the documented architecture—not numerical performance or hardware validation.
