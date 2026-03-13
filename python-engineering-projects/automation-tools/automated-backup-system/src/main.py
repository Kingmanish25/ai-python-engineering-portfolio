import os
import shutil
from datetime import datetime

SOURCE_FOLDER = "data"
BACKUP_FOLDER = "backup"


def backup_files():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    destination = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")

    shutil.copytree(SOURCE_FOLDER, destination)

    print("Backup created:", destination)


if __name__ == "__main__":
    backup_files()
