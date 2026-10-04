# Control and integration boundary

The host-side control implementation remains in the external Kaggle notebook; preserve the exact notebook export before refactoring it here. The notebook and project documentation use `A` for reprocess and `B` for scrap/reject, with pass represented by no command.

The uploaded board sketch is preserved at [`../../firmware/sketch_may1a.ino`](../../firmware/sketch_may1a.ino) and defines the canonical current firmware parameters: 9600 baud, loop polling, sensor-gated per-route queues, and a 500 ms hold. Its observable interface is documented in [`../../docs/hardware.md`](../../docs/hardware.md).

Any future host adapter should pin the firmware hash, serial settings, command format, and safe bench procedure.
