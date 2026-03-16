import os
import email
from email import policy
from email.parser import BytesParser


def parse_email(file_path, attachment_dir="../data"):

    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    attachments = []

    for part in msg.iter_attachments():

        filename = part.get_filename()

        if filename:

            filepath = os.path.join(attachment_dir, filename)

            with open(filepath, "wb") as f:
                f.write(part.get_payload(decode=True))

            attachments.append(filepath)

    print("Attachments extracted:", attachments)

    return attachments
