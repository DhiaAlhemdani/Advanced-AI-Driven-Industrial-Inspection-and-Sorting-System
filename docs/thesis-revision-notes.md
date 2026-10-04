# Evidence-reconciled thesis revision notes

**Revision date:** 2026-10-04  
**Applies to:** `Project Research - Evidence-Reconciled Revision.pdf`  
**Original preserved as:** `Project Research.pdf`

## Revision status

The revised PDF preserves every original thesis page and places a visible revision banner on pages containing superseded or disputed metric and firmware statements. A correction appendix is appended after the original 153 pages.

This revision does **not** retroactively prove that the uploaded Arduino sketch was used for the original physical trials. At the owner's direction, the uploaded sketch is treated as the canonical firmware specification for the revised document. Historical claims requiring an interrupt-driven or differently configured firmware revision remain unverified.

## Corrected metric interpretation

### Box-detection benchmark

| Source | Precision | Recall | mAP@0.50 | mAP@0.50:0.95 |
| --- | ---: | ---: | ---: | ---: |
| Uploaded `results.csv`, final epoch 121 | 97.367% | 98.584% | 99.414% | 94.317% |
| Uploaded CSV, best mAP@0.50:0.95 row (epoch 117) | 95.780% | 98.816% | 99.389% | 94.441% |
| Quick Inference, 24 images / 83 instances | 98.1% | 95.7% | 96.47% | 92.12% |

Peak recall reaches 100% first at epoch 55. Peak precision, recall, mAP@0.50, and mAP@0.50:0.95 occur at different epochs and must not be represented as one checkpoint result.

The thesis's 85–95% “inspection accuracy” is retained only as an incompletely defined historical runtime claim. It is not precision, recall, mAP, or verified physical sorting accuracy.

### Physical sorting table

| Scenario | Tested | Published routed count | Recomputed rate |
| --- | ---: | ---: | ---: |
| SC-01 compliant / pass | 100 | 100 | 100.00% |
| SC-02 missing cap / rework | 40 | 40 | 100.00% |
| SC-03 missing label / rework | 35 | 35 | 100.00% |
| SC-04 label skew / rework | 35 | 35 | 100.00% |
| SC-05 fluid defect / scrap | 35 | 20 | **57.14%** |
| Overall | 245 | 230 | **93.88%** |

The original 62% and 95% values do not follow from their displayed counts. Statements of flawless or 100% physical sorting conflict with this table. Because no item-level route ledger is available, 93.88% is an arithmetic reconciliation of published counts—not independently verified hardware accuracy.

## Canonical uploaded firmware parameters

The revised document uses the observable behavior of `firmware/sketch_may1a.ino` as its current firmware specification:

| Parameter | Canonical value in uploaded sketch |
| --- | --- |
| Serial rate | 9600 baud |
| Accepted commands | `A` and `B`; pass sends no command |
| Servo A | pin 9; rest 35°; active 0°; source comment identifies reprocess |
| Servo B | pin 10; rest 0°; active 35°; source comment identifies defected |
| Proximity A / B | pins 2 / 3; plain `INPUT`; active low |
| Control style | polling in `loop()`; no interrupt service routine |
| Dwell | `HOLD_TIME = 500` ms |
| Queues | independent ten-character circular queues |
| Trigger sequence | command becomes pending, then corresponding low sensor reading starts motion |
| Diagnostics | sensor text printed on the command serial stream approximately once per second |

The sketch does not implement acknowledgements, item IDs, checksums, pending-command timeouts, queue-overflow reporting, distance-based 400/1000 ms flight timers, conveyor control, MQTT, or an `S` emergency-stop command.

Accordingly, the original thesis descriptions of 115200 baud, INT0/ISR execution, 45–50° programmed sweep, 250 ms dwell, distance-based gate timers, and an `S` emergency command are superseded in the revised specification. The original `<3.2 µs` ISR and 68 ms sweep statements cannot be attributed to this sketch.

## Timing interpretation

- The thesis's 20.6 ms value is an unverified historical sum of host-side capture, inference, OpenCV, and serial-write averages.
- The thesis separately reports 2–4 seconds from field-of-view entry to completed physical deflection.
- The uploaded firmware establishes only a programmed 500 ms active hold after a pending command is sensor-triggered. It does not establish host inference, transport, bottle flight, physical servo movement, or end-to-end latency.

## Provenance

- Original thesis SHA-256: `8dee0b3dbc63031ca2e850f971fe0cfc85b40e3f688d5b190fabdf36dd1d03ed`
- Uploaded firmware SHA-256: `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77`
- Uploaded benchmark CSV SHA-256: `16c19565ecda02816316ea25c7102763e88bb9638a29c2daf7b0bb869270ac57`

Training data, labels, annotations, original notebook, and model weights remain external on Kaggle. The revised PDF does not claim an independent model rerun or physical hardware retest.
