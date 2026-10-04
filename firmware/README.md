# Arduino firmware

The project brief identifies an **Arduino Mega 2560** and **dual servos** in the physical sorting system. The original firmware is not present in this checkout.

This file is intentionally a boundary marker, not a reconstructed sketch. Do not add guessed pin assignments, servo angles, serial commands, delays, MQTT bridges, or safety behavior and label them as the project implementation. When the original sketch is added, document:

- board and library versions;
- pin/wiring evidence and actuator mapping;
- command and acknowledgement format;
- timing assumptions and conveyor synchronization;
- fault handling and safe states;
- the hardware test date, setup, trial count, and source log.

See [`docs/hardware.md`](../docs/hardware.md) and [`docs/source-integrity.md`](../docs/source-integrity.md).
