from pathlib import Path

from config import IMAGE_EXTENSIONS


def load_vggface2(dataset_dir: Path) -> list[dict]:
    """
    Scan the VGGFace2 112x112 dataset.

    Expected structure:

    vggface2_112x112/
        id_000/
            image1.jpg
            image2.jpg

        id_001/
            image1.jpg
    """

    records = []

    if not dataset_dir.exists():
        raise FileNotFoundError(
            f"VGGFace2 dataset not found: {dataset_dir}"
        )

    for identity_dir in sorted(dataset_dir.iterdir()):

        if not identity_dir.is_dir():
            continue

        original_identity = identity_dir.name

        identity = (
            f"vggface2_{original_identity}"
        )

        for image_path in sorted(identity_dir.iterdir()):

            if not image_path.is_file():
                continue

            if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            records.append(
                {
                    "image_path": str(image_path.resolve()),
                    "dataset": "vggface2",
                    "identity": identity,
                    "original_identity": original_identity,
                }
            )

    return records