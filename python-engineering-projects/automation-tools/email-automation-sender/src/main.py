import smtplib
import argparse
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def send_email(sender, password, receiver, subject, body):

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

        logging.info("Email sent successfully")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def main():

    parser = argparse.ArgumentParser(description="Email Automation Sender")

    parser.add_argument("--receiver", required=True, help="Receiver email address")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email message body")

    args = parser.parse_args()

    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        raise EnvironmentError(
            "Environment variables EMAIL_SENDER and EMAIL_PASSWORD must be set"
        )

    send_email(sender, password, args.receiver, args.subject, args.body)


if __name__ == "__main__":
    main()
