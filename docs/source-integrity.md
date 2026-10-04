# Source integrity and provenance

## Status labels

- **Owner-uploaded artifact** — supplied in the repository upload and preserved; use does not by itself prove it was the exact thesis/test revision.
- **External original reference** — canonical project artifact hosted on Kaggle but not copied here.
- **Curated** — documentation, packaging, tests, or audit utilities added for reproducibility.
- **Generated** — produced from named inputs by a recorded command; include source hashes.

Current owner-uploaded artifacts include the thesis PDF, Arduino sketch, benchmark bundle, and media listed in [`artifact-inventory.md`](artifact-inventory.md). The public Kaggle notebook is an external original reference. `src/industrial_inspection/`, scripts, tests, and evidence documentation are curated.

## Intake and preservation rules

For each new artifact:

1. Record original filename/path, source, date received, size, and SHA-256.
2. Preserve an unmodified copy where licensing/privacy permits.
3. State whether its use in the thesis/demo is confirmed, reported, or unknown.
4. Identify dependencies, runtime/tool versions, and machine-specific paths.
5. Link the relevant thesis page, figure, table, or trial record.
6. Redact secrets and personal/private data without silently altering technical meaning.
7. Never replace absent code or evidence with a plausible reconstruction labeled as original.

## Source-specific reporting

Each value is retained with its source and measurement type:

- percentages are calculated from published counts;
- source-code behavior is documented from the uploaded sketch;
- final-row, selected-checkpoint, peak, and Quick Inference metrics are labeled separately;
- physical results retain their denominator and evidence requirements;
- canonical current parameters are stated in the updated thesis edition and hardware record.

This policy applies to detector results, sorting counts, serial configuration, control architecture, servo timing/angles, and command scope.

## Numerical-result checklist

Before publishing a result, identify:

- evaluator/source artifact and checksum;
- model/checkpoint and code environment;
- dataset version, split, instances, and class order;
- confidence, IoU, aggregation, and selection criterion;
- whether the unit is a box, bottle decision, physical route, or maintenance event;
- denominator, exclusions, raw log, and arithmetic check;
- corresponding limitations.

The uploaded benchmark CSV passes artifact extraction, but not independent model reproduction. The updated physical table presents count-derived rates, while independent physical reproduction still requires the item-level ledger.
