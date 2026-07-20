from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASETS_DIR = PROJECT_ROOT / "datasets"

RAW_DATA_DIR = DATASETS_DIR / "raw"
PROCESSED_DATA_DIR = DATASETS_DIR / "processed"

# raw datasets
CASIA_DIR = RAW_DATA_DIR / "casia-webface"
CELEBA_DIR = RAW_DATA_DIR / "celeba-dataset"
LFW_DIR = RAW_DATA_DIR / "lfw-deepfunneled"
VGGFACE2_DIR = RAW_DATA_DIR / "vggface2_112x112"


PROCESSED_IMAGES_DIR = PROCESSED_DATA_DIR / "images"

METADATA_DIR = PROCESSED_DATA_DIR / "metadata"

MASTER_METADATA_FILE = METADATA_DIR / "master.csv"

RECOGNITION_METADATA_FILE = (
    METADATA_DIR / "recognition.csv"
)

ATTRIBUTE_METADATA_FILE = (
    METADATA_DIR / "attributes.csv"
)


#! supported image extensions (change if need be for future datasets)
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
}