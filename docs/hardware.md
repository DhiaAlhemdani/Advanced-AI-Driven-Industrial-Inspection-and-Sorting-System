# Hardware and firmware integration record

## Available evidence

The checkout contains a thesis, one Arduino sketch, a prototype photograph, two dashboard/conveyor screenshots, and a demo video. The thesis identifies an Arduino Mega 2560/ATmega2560, DS3218MG servos, proximity sensing, a conveyor, a camera, and a dual-gate layout. Media visually supports the existence of a conveyor prototype, but does not resolve pin wiring, flashed firmware revision, or trial outcomes.

The uploaded sketch has SHA-256 `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77`. It is preserved as supplied. No behavior has been added to make it resemble the thesis.

## Source-level pin and command inventory

| Function | Value in uploaded sketch | Confidence / limitation |
| --- | --- | --- |
| Serial | 9600 baud | Explicit in source; host configuration is absent here |
| Command `A` | Arms route A; comment labels servo A “reprocess” | Semantic label only; physical lane not bench-verified |
| Command `B` | Arms route B; comment labels servo B “defected” | Semantic label only; physical lane not bench-verified |
| Servo A | pin 9; rest 35°; active 0° | Requested angles, not measured shaft/gate positions |
| Servo B | pin 10; rest 0°; active 35° | Requested angles, not measured shaft/gate positions |
| Proximity A | pin 2, `INPUT`, active low | Pull-up/external wiring not documented |
| Proximity B | pin 3, `INPUT`, active low | Pull-up/external wiring not documented |
| Dwell | 500 ms | Software constant; not measured motion time |
| Queues | 10 characters per route | Overflow is silently ignored by caller |

## Actual sketch sequence

1. Startup attaches both servos, writes rest positions, and configures both proximity pins as plain inputs.
2. Receiving `A` or `B` sets the corresponding route pending when idle; otherwise it attempts to enqueue the character.
3. A pending route actuates only after its proximity input reads low.
4. After 500 ms, that servo returns to rest and one queued character is dequeued.
5. Sensor levels are also printed to the same serial stream every ~1 second.

The sketch is non-blocking in the sense that it uses `millis()` rather than `delay()`, and the two route states can progress independently. It is **not** interrupt-driven and does not implement distance-based bottle tracking.

## Thesis-to-firmware reconciliation

The thesis describes 115200 bps UART, INT0/ISR capture, 20 cm and 50 cm gate offsets with 400 ms and 1000 ms timers, 45–50° sweeps, 68 ms movement, 250 ms dwell, and an emergency byte `S`. None of those mechanisms appears in the uploaded sketch as written. Conversely, the sketch's second proximity input, 9600 baud, 35° travel, 500 ms hold, per-route queues, and periodic serial diagnostics are not the firmware behavior summarized by the thesis.

Possible explanations include different firmware revisions, simplified test code, or thesis/document drift. There is no flashed-binary hash, dated build record, or board log to determine which revision produced the reported trials. The repository therefore does not claim that this sketch produced the thesis results.

## Integration constraints

Do not connect actuators based on this page alone. Before a hardware run:

- identify the exact Mega board and servo power supply; do not power high-torque servos from an unverified board rail;
- trace pins 2, 3, 9, and 10 against a wiring diagram and continuity check;
- confirm active-low sensor voltage compatibility and whether external pull-ups are installed;
- test requested servo angles with horns/linkages disconnected or mechanically constrained safely;
- establish whether debug output is acceptable on the command serial channel;
- define queue-overflow, stale-pending-command, reset, disconnect, and emergency-stop behavior;
- validate simultaneous servo current and mechanical clearance;
- match the host serial rate to the exact firmware revision;
- record board core/library versions and compile output.

## Required physical validation record

```text
Date/time and operator:
Board model/revision and flashed binary/sketch SHA-256:
Arduino core and Servo library versions:
Wiring diagram revision and power arrangement:
Servo/sensor part numbers and calibrated positions:
Host source revision and serial settings:
Conveyor speed, camera-to-sensor/gate geometry, item spacing:
Per-item ground truth, command, sensor timestamps, actual lane:
Queue overflows, timeouts, resets, communication and mechanical faults:
Raw log/video references and exclusions:
```

A successful Python test, sketch review, dashboard screenshot, or video clip does not replace this record.
