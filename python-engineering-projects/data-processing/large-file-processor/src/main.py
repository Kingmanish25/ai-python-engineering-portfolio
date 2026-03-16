import argparse
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def process_large_file(file_path, interval):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    logging.info("Starting large file processing")

    with open(file_path, "r") as f:

        for i, line in enumerate(f, 1):

            if i % interval == 0:
                logging.info(f"Processing line {i}: {line.strip()}")


def main():

    parser = argparse.ArgumentParser(description="Large File Processor")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to large text file"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=1000,
        help="Processing interval for lines"
    )

    args = parser.parse_args()

    process_large_file(args.input, args.interval)


if __name__ == "__main__":
    main()
