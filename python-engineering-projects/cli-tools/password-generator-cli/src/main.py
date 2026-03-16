import argparse
import random
import string
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_password(length):

    if length < 6:
        raise ValueError("Password length should be at least 6 characters")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():

    parser = argparse.ArgumentParser(
        description="Password Generator CLI Tool"
    )

    parser.add_argument(
        "--length",
        type=int,
        default=12,
        help="Length of the generated password"
    )

    args = parser.parse_args()

    password = generate_password(args.length)

    logging.info(f"Generated password: {password}")


if __name__ == "__main__":
    main()
