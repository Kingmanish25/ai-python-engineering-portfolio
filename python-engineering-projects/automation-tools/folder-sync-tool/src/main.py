import os
import shutil
import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_folder(path, name):

    if not os.path.exists(path):
        raise FileNotFoundError(f"{name} folder does not exist: {path}")


def sync_folders(source, destination):

    os.makedirs(destination, exist_ok=True)

    for file in os.listdir(source):

        src_file = os.path.join(source, file)
        dst_file = os.path.join(destination, file)

        if os.path.isfile(src_file):

            shutil.copy2(src_file, dst_file)

            logging.info(f"Copied {file} → {destination}")


def main():

    parser = argparse.ArgumentParser(description="Folder Sync Tool")

    parser.add_argument(
        "--source",
        required=True,
        help="Source folder path"
    )

    parser.add_argument(
        "--destination",
        required=True,
        help="Destination folder path"
    )

    args = parser.parse_args()

    validate_folder(args.source, "Source")

    sync_folders(args.source, args.destination)

    logging.info("Folder synchronization completed")


if __name__ == "__main__":
    main()
