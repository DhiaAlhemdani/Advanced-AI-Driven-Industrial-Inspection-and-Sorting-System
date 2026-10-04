# Artifact storage policy

## Canonical external artifacts

The Kaggle dataset remains the canonical location for training images, detection labels, segmentation polygons, LabelMe annotations, metadata, the original notebook, and model weights:

<https://www.kaggle.com/datasets/dhiaalhemdani/industrial-inspection-system>

Do not copy those large or generated artifacts into normal Git. Pin a Kaggle version and record archive/file hashes for each reproducible experiment.

## Repository artifacts

Small source/configuration/CSV files and the owner-uploaded thesis, firmware, benchmark plots, and project media are currently tracked. Their inventory and hashes are in [`artifact-inventory.md`](artifact-inventory.md). Existing media is evidence material, not training data.

| Artifact | Preferred location |
| --- | --- |
| Documentation, source, YAML/JSON, small CSV | Git |
| Training images, labels, annotations, notebook, weights | Kaggle canonical record; stage locally under ignored paths |
| New large model exports | Kaggle, release asset, or Git LFS; always checksum |
| New long/high-resolution media | Release/external store or Git LFS after privacy review |
| Generated reports | `artifacts/` or `results/generated/` locally; commit only reviewed, necessary summaries |

`.gitignore` excludes local data and common weight formats. `.gitattributes` provides LFS patterns where LFS is deliberately used, but a pattern alone does not prove that a tracked file is an LFS object.

## Intake checklist

1. Confirm redistribution rights and privacy.
2. Record source, version/date, size, and SHA-256.
3. Identify whether the file was actually used in a reported experiment.
4. Scan configuration/logs for credentials and private paths.
5. Keep raw data/model artifacts external unless there is a documented reason to duplicate them.
6. Link numerical claims to machine-readable logs, not only screenshots or plots.
