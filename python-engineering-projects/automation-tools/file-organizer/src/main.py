import os
import shutil
import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def organize_files(folder_path):

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            name, extension = os.path.splitext(filename)

            if extension == "":
                extension = "no_extension"
            else:
                extension = extension.replace(".", "")

            target_folder = os.path.join(folder_path, extension)

            os.makedirs(target_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(target_folder, filename))

            logging.info(f"Moved {filename} → {extension}/")


def main():

    parser = argparse.ArgumentParser(description="File Organizer Tool")

    parser.add_argument(
        "--folder",
        required=True,
        help="Folder path containing files to organize"
    )

    args = parser.parse_args()

    organize_files(args.folder)

    logging.info("Files organized successfully")


if __name__ == "__main__":
    main()
