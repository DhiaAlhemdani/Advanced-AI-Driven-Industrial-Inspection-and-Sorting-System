# Control and integration boundary

The host-side control implementation remains in the external Kaggle notebook; preserve the exact notebook export before refactoring it here. The notebook audit and thesis describe `A` for reprocess and `B` for scrap/reject, with pass represented by no command.

The uploaded board sketch is preserved at [`../../firmware/sketch_may1a.ino`](../../firmware/sketch_may1a.ino). Its observable interface is documented in [`../../docs/hardware.md`](../../docs/hardware.md). Do not hide its differences from the host/thesis record: it uses 9600 baud, polling, sensor-gated per-route queues, and 500 ms dwell, and it does not implement acknowledgements, item IDs, distance timers, conveyor control, or `S` emergency stop.

Any future adapter must be based on a confirmed firmware/host pair and safe bench procedure, not guessed compatibility changes.
