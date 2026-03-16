import argparse
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_log(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Log file not found: {input_file}")

    error_count = 0

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:

        for line in infile:

            if "ERROR" in line:
                outfile.write(line)
                error_count += 1

    logging.info(f"Total ERROR entries found: {error_count}")
    logging.info(f"Filtered log saved to: {output_file}")


def main():

    parser = argparse.ArgumentParser(description="Log File Parser")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to log file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output filtered log file"
    )

    args = parser.parse_args()

    parse_log(args.input, args.output)


if __name__ == "__main__":
    main()
