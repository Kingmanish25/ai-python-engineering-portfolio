import os
import shutil

def organize_files(folder_path):

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            extension = filename.split(".")[-1]

            target_folder = os.path.join(folder_path, extension)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))


def main():

    folder = "downloads"

    organize_files(folder)

    print("Files organized successfully")


if __name__ == "__main__":
    main()
