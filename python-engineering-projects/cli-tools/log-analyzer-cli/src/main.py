import argparse
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def analyze_log(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")

    with open(file_path, "r") as f:
        lines = f.readlines()

    error_count = sum(1 for line in lines if "ERROR" in line)

    logging.info(f"Total ERROR entries: {error_count}")


def main():

    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file"
    )

    args = parser.parse_args()

    analyze_log(args.file)


if __name__ == "__main__":
    main()
