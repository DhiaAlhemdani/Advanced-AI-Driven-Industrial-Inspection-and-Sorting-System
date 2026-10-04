# Source integrity and provenance

## Why this exists

A polished repository must distinguish original project artifacts from documentation added during curation. Reconstructed code can look plausible while silently changing timing, thresholds, pin mappings, or evaluation logic. This project therefore treats provenance as part of the engineering deliverable.

## Artifact status labels

Use one of these labels in commit messages, file headers, or the relevant README:

- **Original** — supplied from the graduation-project implementation and preserved with only documented portability edits.
- **Curated** — documentation, packaging, tests, or utilities added to make the original work understandable/reproducible.
- **Reference** — a new illustrative example that is not the project implementation and must not be reported as hardware-tested.
- **Generated** — produced by a command from a named source artifact; include the command and source hash.

The current `src/industrial_inspection/` utilities are **Curated**. The boundary READMEs are **Curated**. No original vision, firmware, MQTT, dashboard, or maintenance implementation is present in this checkout.

## Intake checklist for original files

For each file added from the project archive:

1. Record its original path and date received.
2. Mark whether it was used in the thesis/demo.
3. Preserve meaningful comments and constants.
4. Identify dependencies and runtime versions.
5. Run it in a safe offline mode before connecting hardware.
6. Link the relevant thesis page, figure, or benchmark-log row.
7. Redact credentials, private hosts, personal data, and raw camera footage.
8. Never replace an absent file with a guessed implementation and call it original.

## Numerical-result checklist

Before adding a metric to README or a release:

- identify the exact evaluator and commit;
- identify the dataset export/hash and split;
- capture configuration, class order, and thresholds;
- compare against the thesis and the benchmark log;
- state whether it measures detection, physical sorting, or end-to-end behavior;
- preserve the raw or redacted evidence path.

If sources disagree, report the discrepancy and keep both references visible until resolved. Do not silently choose the more impressive number.
