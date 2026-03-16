import os


def get_invoice_files(folder):

    if not os.path.exists(folder):
        raise FileNotFoundError("Invoice folder not found")

    files = []

    for file in os.listdir(folder):

        if file.lower().endswith(".pdf"):
            files.append(os.path.join(folder, file))

    return files
