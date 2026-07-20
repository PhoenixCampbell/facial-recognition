from config import LFW_DIR
from config import VGGFACE2_DIR

from adapters.lfw import load_lfw
from adapters.vggface2 import load_vggface2


def main():

    # from lfw.py, make sure the dataset is reachable
    print("Scanning LFW...")

    lfw_records = load_lfw(LFW_DIR)

    print(
        f"LFW images found: "
        f"{len(lfw_records):,}"
    )

    print()
    # similarly find and validate vgg dataset
    print("Scanning VGGFace2...")

    vgg_records = load_vggface2(
        VGGFACE2_DIR
    )

    print(
        f"VGGFace2 images found: "
        f"{len(vgg_records):,}"
    )


if __name__ == "__main__":
    main()