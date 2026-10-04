# Arduino firmware

[`sketch_may1a.ino`](sketch_may1a.ino) is the owner-uploaded Arduino artifact and the canonical current firmware specification for this repository. SHA-256: `c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77`. The source is preserved as supplied.

Static inspection documents a 9600-baud, polling-based, dual-servo controller. It accepts `A` and `B`, waits for separate active-low proximity inputs on pins 2/3, drives servos on pins 9/10, maintains independent ten-entry queues, and holds an active command for 500 ms. It prints sensor diagnostics on the command serial stream.

Acknowledgements, item IDs, pending timeouts, queue-overflow reports, conveyor control, MQTT, distance-based flight timers, and an `S` command are outside this sketch's implementation scope.

Do not infer wiring or connect powered actuators from the source alone. See [`../docs/hardware.md`](../docs/hardware.md) for the pin/command contract and required bench record.
