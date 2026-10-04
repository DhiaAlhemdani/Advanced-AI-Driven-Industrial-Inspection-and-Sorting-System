# System architecture and evidence map

## Scope

The project combines component detection, geometric quality rules, serial actuation, physical routing, monitoring, and a simulated condition-health layer. This page identifies the source and implementation boundary for each layer.

## Data flow

```mermaid
flowchart TB
    subgraph Host[Host-side inspection design]
      C[Camera frame] --> D[YOLO component boxes]
      D --> O[OpenCV geometry / fill checks]
      O --> Q{Quality decision}
      Q -->|pass: no command| PASS[Continue main lane]
      Q -->|A: rework| U[Serial transport]
      Q -->|B: scrap/reject| U
      Q --> OBS[MQTT / dashboard path]
      SIM[Virtual sensor inputs] --> PM[Rule-based health score]
      PM --> OBS
    end

    subgraph UploadedSketch[Current uploaded firmware specification]
      U --> RX[Single-character serial read]
      RX --> QA[Queue A, capacity 10]
      RX --> QB[Queue B, capacity 10]
      PA[Proximity A, pin 2, active low] --> GA[Pending-A gate]
      PB[Proximity B, pin 3, active low] --> GB[Pending-B gate]
      QA --> GA
      QB --> GB
      GA --> SA[Servo A, pin 9]
      GB --> SB[Servo B, pin 10]
    end
```

A line in this diagram records a documented software or source-code connection. Hardware reproduction additionally requires a dated wiring, build, and test record.

## Layer-by-layer record

| Boundary | Repository evidence | Documented scope | Reproduction input still needed |
| --- | --- | --- | --- |
| Dataset | Kaggle YAML and public record | Four classes; reported 95/24 image split | Downloaded manifest and archive hash |
| Detector training | `results.csv`, plots, `args.yaml`, settings | Source-specific metrics and configuration | Weight checksum, environment, exact input, rerun |
| Inspection logic | Thesis and public-notebook audit | YOLO plus OpenCV/rule architecture | Exact notebook export and replay package |
| Host → controller | Thesis/notebook protocol record and uploaded sketch | `A` and `B` route commands; pass sends no byte | Versioned host implementation and serial trace |
| Controller | Uploaded `.ino` | Current pins, states, queues, and timing constants | Board/core/library build record and wiring |
| Physical sorting | Thesis count table and media | Five scenarios and count-derived rates | Item-level expected/observed route ledger |
| Monitoring | Screenshots and notebook audit | Dashboard concepts and user interface | Dashboard source, MQTT trace, synchronized trial record |
| Maintenance | Thesis and screenshots | Virtual-sensing health formula and state demonstration | Physical signals and field labels for predictive evaluation |

## Uploaded firmware contract — code inspection

The uploaded sketch is the canonical current firmware specification for this repository:

- Arduino `Servo` library; serial initialized at **9600 baud**.
- Servo A attaches to **pin 9**, is labeled `reprocess`, rests at 35°, and activates at 0°.
- Servo B attaches to **pin 10**, is labeled `defected`, rests at 0°, and activates at 35°.
- Proximity inputs use **pins 2 and 3**, plain `INPUT`, and trigger when read `LOW`.
- `A` and `B` set independent pending states; actuation waits for the corresponding sensor.
- Each route has a ten-character circular queue.
- Active position is held for **500 ms**, then returned to rest.
- Sensor values are printed on the command serial stream approximately once per second.
- Pass is represented by no command.

Acknowledgements, item identifiers, checksums, retries, pending timeouts, queue-overflow reports, distance-based flight timers, an `S` command, conveyor output, and MQTT are outside this sketch's implementation scope.

## Timing boundaries

The documented **20.6 ms** value covers host computational stages. The **2–4 s** value covers field-of-view entry through completed physical deflection. The sketch's **500 ms** constant is an active hold after a sensor-gated command. These values are retained with their respective timing boundaries.

## Operational validation questions

Before deployment, define and test:

1. Behavior when a command is pending and its sensor does not trigger.
2. Handling of a command received when a route queue is full.
3. Host handling of periodic sensor diagnostic text.
4. Safe state after reset, USB loss, servo power loss, or a stuck-low sensor.
5. Method used to associate a vision decision with a physical bottle.
6. Simultaneous-servo power and mechanical clearance.

Until those tests are logged, the source defines a prototype interface rather than a production control contract.
