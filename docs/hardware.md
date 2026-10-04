# Hardware and firmware integration record

## Available evidence

The checkout contains a thesis, one Arduino sketch, a prototype photograph, two dashboard/conveyor screenshots, and a demo video. The project record identifies an Arduino Mega 2560/ATmega2560, DS3218MG servos, proximity sensing, a conveyor, a camera, and a dual-gate layout. Media provides qualitative evidence of the conveyor prototype.

The uploaded sketch has SHA-256 `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77` and is the canonical current firmware specification in this repository. It is preserved as supplied.

## Pin and command inventory

| Function | Value in uploaded sketch | Validation boundary |
| --- | --- | --- |
| Serial | 9600 baud | Explicit source constant; verify host setup before connection |
| Command `A` | Arms route A; servo comment says `reprocess` | Verify physical lane during bench setup |
| Command `B` | Arms route B; servo comment says `defected` | Verify physical lane during bench setup |
| Servo A | pin 9; rest 35°; active 0° | Requested angles; calibrate linkage mechanically |
| Servo B | pin 10; rest 0°; active 35° | Requested angles; calibrate linkage mechanically |
| Proximity A | pin 2, `INPUT`, active low | Confirm voltage and external pull-up arrangement |
| Proximity B | pin 3, `INPUT`, active low | Confirm voltage and external pull-up arrangement |
| Active hold | 500 ms | Software constant; measure physical movement separately |
| Queues | 10 characters per route | Add overflow telemetry for production use |

## Sketch sequence

1. Startup attaches both servos, writes rest positions, and configures both proximity pins as inputs.
2. Receiving `A` or `B` sets the corresponding route pending when idle; otherwise it attempts to enqueue the character.
3. A pending route actuates after its proximity input reads low.
4. After 500 ms, that servo returns to rest and one queued character is dequeued.
5. Sensor levels are printed to the same serial stream approximately once per second.

The two route state machines progress independently and use `millis()` timing. The source uses polling in `loop()`.

## Current implementation scope

The uploaded sketch implements `A`/`B` command ingestion, route-specific pending states, sensor-gated actuation, circular queues, servo return timing, and sensor diagnostics. Acknowledgements, item IDs, command framing/checksums, pending-command timeouts, queue-overflow reporting, conveyor control, MQTT, and an `S` command are not part of this sketch.

A dated flashed-binary hash and board log are still needed to associate a source revision with any physical trial.

## Integration constraints

Before a hardware run:

- identify the exact Mega board and servo power supply;
- trace pins 2, 3, 9, and 10 against a wiring diagram and continuity check;
- confirm active-low sensor voltage compatibility and external pull-ups;
- test requested servo angles with horns/linkages disconnected or safely constrained;
- establish whether debug output is acceptable on the command serial channel;
- define queue-overflow, stale-pending-command, reset, disconnect, and emergency behavior;
- validate simultaneous servo current and mechanical clearance;
- configure the host serial link for 9600 baud;
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

A software test, sketch review, dashboard screenshot, or video clip does not replace this physical validation record.
