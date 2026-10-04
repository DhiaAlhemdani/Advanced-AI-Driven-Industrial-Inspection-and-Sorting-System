# Hardware integration record

## Reported hardware

The project brief identifies an **Arduino Mega 2560**, a conveyor sorting mechanism, and **two servos**. This repository does not currently contain the original sketch, wiring diagram, board photo, or hardware log. The sections below are an integration-record template, not a reconstructed wiring plan.

## Bill of materials record

| Subsystem | Reported item | Exact part/revision | Evidence |
| --- | --- | --- | --- |
| Controller | Arduino Mega 2560 | To be filled from original build | Firmware/build record |
| Actuation | Dual servos | To be filled | Wiring/photo and trial log |
| Conveyor | Conveyor mechanism | To be filled | Build record |
| Inspection | Camera/image source | To be filled | CV source/config |
| Communications | MQTT path or bridge | To be filled | Sanitized trace |
| Monitoring | Dashboard | To be filled | Source/screenshot |

## Integration information required before claiming reproducibility

- Complete wiring diagram and pin assignments.
- Board revision, power arrangement, and servo power budget.
- Servo model, mechanical range, neutral position, and route mapping.
- Conveyor speed, item spacing, camera-to-actuator distance, and timing budget.
- Command transport between the CV host and the controller.
- Acknowledgement and timeout behavior.
- Reset/startup behavior and safe state on lost communication.
- Test procedure, item count, route ground truth, observed outcomes, and log reference.

## Hardware test record template

```text
Date/time:
Operator:
Board/firmware revision:
Mechanical revision:
Camera and lighting:
Conveyor speed:
Test item set and ground truth:
Trial count:
Correct routes:
Missed/extra/double routes:
Communication faults:
Servo/conveyor faults:
Raw log path:
Thesis or benchmark reference:
```

Do not describe the firmware or sorter as hardware-tested until this record is backed by the original source and a dated log. A successful software test, a dashboard screenshot, or a detection metric does not establish physical sorting accuracy.
