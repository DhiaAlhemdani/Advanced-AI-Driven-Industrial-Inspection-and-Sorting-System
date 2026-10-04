# Arduino firmware

[`sketch_may1a.ino`](sketch_may1a.ino) is the owner-uploaded Arduino artifact (SHA-256 `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77`). It is preserved as supplied; this repository has not reconstructed missing thesis behavior or made portability edits.

Static inspection shows a 9600-baud, polling-based, dual-servo controller. It accepts `A` and `B`, waits for separate active-low proximity inputs on pins 2/3, drives servos on pins 9/10, maintains independent ten-entry queues, and holds an active command for 500 ms. It prints sensor diagnostics on the command serial stream.

This differs from the thesis's 115200-baud, ISR/timer, 250 ms dwell, 45–50° sweep, flight-delay, and emergency-`S` description. There is no evidence in this checkout that this exact sketch revision generated the thesis trials. There is also no acknowledgement, item ID, timeout, queue-overflow report, conveyor control, or emergency-stop handler in the sketch.

Do not infer wiring or connect powered actuators from the source alone. See [`../docs/hardware.md`](../docs/hardware.md) for the observed pin/command contract, mismatch table, and required bench record.
