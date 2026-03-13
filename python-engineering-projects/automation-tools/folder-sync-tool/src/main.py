import os
import shutil

def sync_folders(source, destination):

    for file in os.listdir(source):

        src_file = os.path.join(source, file)
        dst_file = os.path.join(destination, file)

        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)

    print("Folders synchronized")

if __name__ == "__main__":

    sync_folders("source_folder", "destination_folder")
