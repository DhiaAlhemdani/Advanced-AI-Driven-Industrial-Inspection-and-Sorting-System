# Thesis metrics and firmware update notes

**Edition date:** 2026-10-04

**Applies to:** `Project Research - Updated Metrics and Firmware.pdf`

**Original preserved as:** `Project Research.pdf`

## Edition status

The updated PDF preserves every original thesis page and adds visible update banners to pages associated with benchmark metrics or firmware implementation details. A four-page technical update is appended after the original 153 pages.

The uploaded Arduino sketch is used as the canonical current firmware specification for this edition. Hardware-trial provenance still requires a dated board, build, wiring, and item-level test record.

## Detection metrics

| Source | Precision | Recall | mAP@0.50 | mAP@0.50:0.95 |
| --- | ---: | ---: | ---: | ---: |
| Uploaded `results.csv`, final epoch 121 | 97.367% | 98.584% | 99.414% | 94.317% |
| Uploaded CSV, best mAP@0.50:0.95 row (epoch 117) | 95.780% | 98.816% | 99.389% | 94.441% |
| Quick Inference, 24 images / 83 instances | 98.1% | 95.7% | 96.47% | 92.12% |

Peak recall reaches 100% first at epoch 55. Final-row, selected-checkpoint, and Quick Inference values are identified by source and evaluation context.

The thesis's 85–95% inspection range remains an integrated runtime result. It is listed independently from annotation-based box detection and physical route rates.

## Physical sorting counts and calculated rates

| Scenario | Tested | Routed count | Count-derived rate |
| --- | ---: | ---: | ---: |
| SC-01 compliant / pass | 100 | 100 | 100.00% |
| SC-02 missing cap / rework | 40 | 40 | 100.00% |
| SC-03 missing label / rework | 35 | 35 | 100.00% |
| SC-04 label skew / rework | 35 | 35 | 100.00% |
| SC-05 fluid defect / scrap | 35 | 20 | **57.14%** |
| Overall | 245 | 230 | **93.88%** |

The rates above are calculated directly from the published scenario counts. An item-level route ledger is needed for independent physical-trial reproduction.

## Canonical uploaded firmware parameters

| Parameter | Canonical value in uploaded sketch |
| --- | --- |
| Serial rate | 9600 baud |
| Accepted commands | `A` and `B`; pass sends no command |
| Servo A | pin 9; rest 35°; active 0°; source comment identifies reprocess |
| Servo B | pin 10; rest 0°; active 35°; source comment identifies defected |
| Proximity A / B | pins 2 / 3; plain `INPUT`; active low |
| Control style | polling in `loop()` |
| Dwell | `HOLD_TIME = 500` ms |
| Queues | independent ten-character circular queues |
| Trigger sequence | command becomes pending, then the corresponding low sensor reading starts motion |
| Diagnostics | sensor text printed on the command serial stream approximately once per second |

The sketch handles its documented `A` and `B` routes and sensor-gated servo operations. Acknowledgements, item IDs, checksums, pending-command timeouts, queue-overflow reports, distance-based flight timers, conveyor control, MQTT, and an `S` command are outside this sketch's implementation scope.

## Timing scope

- The thesis records a 20.6 ms host-processing sum from capture, inference, OpenCV, and serial-write components.
- The thesis records a 2–4 second field-of-view-entry to completed-deflection range.
- The uploaded firmware defines a 500 ms active hold after a pending command is sensor-triggered.

These values are labeled by timing boundary rather than combined into one latency figure.

## Provenance

- Original thesis SHA-256: `8dee0b3dbc63031ca2e850f971fe0cfc85b40e3f688d5b190fabdf36dd1d03ed`
- Uploaded firmware SHA-256: `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77`
- Uploaded benchmark CSV SHA-256: `16c19565ecda02816316ea25c7102763e88bb9638a29c2daf7b0bb869270ac57`

Training data, labels, annotations, original notebook, and model weights remain external on Kaggle. The updated PDF is a documentation edition and does not represent a new model run or physical hardware retest.
