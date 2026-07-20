from pathlib import Path

from config import IMAGE_EXTENSIONS


def load_lfw(dataset_dir: Path) -> list[dict]:
    """
    Scan the LFW dataset.

    Expected structure:

    lfw-deepfunneled/
        Person_Name/
            Person_Name_0001.jpg
            Person_Name_0002.jpg

    Each directory represents one identity.
    """

    records = []

    if not dataset_dir.exists():
        raise FileNotFoundError(
            f"LFW dataset not found: {dataset_dir}"
        )

    for identity_dir in sorted(dataset_dir.iterdir()):

        if not identity_dir.is_dir():
            continue

        identity = f"lfw_{identity_dir.name}"

        for image_path in sorted(identity_dir.iterdir()):

            if not image_path.is_file():
                continue

            if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            records.append(
                {
                    "image_path": str(image_path.resolve()),
                    "dataset": "lfw",
                    "identity": identity,
                    "original_identity": identity_dir.name,
                }
            )

    return records