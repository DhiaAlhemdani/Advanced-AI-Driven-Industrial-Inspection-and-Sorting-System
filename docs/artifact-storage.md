# Artifact storage and upload plan

## Keep Git usable

The Kaggle dataset is about 232.66 MB and includes images, annotations, benchmark outputs, and model weights. Do not commit the raw archive, camera media, or large model files blindly.

Recommended public-repository policy:

| Artifact | Recommended location | Git status |
| --- | --- | --- |
| README, YAML, small CSV, source code | Git | Commit normally |
| Labels and LabelMe JSON | Git if reviewed and size is acceptable; otherwise release asset | Review before commit |
| Training images | Kaggle link or Git LFS/release | Do not commit in normal Git |
| `best.pt` and CLIP/text-embedding weights | Git LFS, release asset, or Kaggle | Do not commit in normal Git |
| Demo video and high-resolution media | Release asset or external artifact store | Do not commit in normal Git |
| Thesis PDF | Git if publication rights permit; otherwise private attachment/release | Add after owner upload |

## Owner upload checklist

1. Upload the thesis PDF and confirm it may be publicly redistributed.
2. Upload model weights/media through Git LFS or a GitHub release rather than the web editor if any file is large.
3. Add SHA-256 checksums and source/version identifiers.
4. Confirm whether labels/annotations are original project artifacts and may be redistributed under the dataset MIT license.
5. Run the dataset inventory and annotation validators after upload.
6. Link each benchmark result to the thesis page and raw log row.

The repository must never treat a successful file upload as proof that the file was used in the hardware-tested graduation system.
