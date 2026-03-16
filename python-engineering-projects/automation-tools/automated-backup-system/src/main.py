import os
import shutil
import argparse
import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def validate_source(source):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source folder does not exist: {source}")


def create_backup(source, backup_root):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(backup_root, f"backup_{timestamp}")

    os.makedirs(backup_root, exist_ok=True)

    shutil.copytree(source, destination)

    logging.info(f"Backup created successfully: {destination}")


def main():

    parser = argparse.ArgumentParser(description="Automated Folder Backup System")

    parser.add_argument(
        "--source",
        required=True,
        help="Source folder to backup"
    )

    parser.add_argument(
        "--destination",
        required=True,
        help="Backup folder location"
    )

    args = parser.parse_args()

    validate_source(args.source)

    create_backup(args.source, args.destination)


if __name__ == "__main__":
    main()
