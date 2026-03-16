import json
import csv
import argparse
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def convert_json_to_csv(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_file, "r") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list of objects")

    with open(output_file, "w", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=data[0].keys())

        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Conversion completed: {input_file} → {output_file}")


def main():

    parser = argparse.ArgumentParser(description="JSON to CSV Converter CLI Tool")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input JSON file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file"
    )

    args = parser.parse_args()

    convert_json_to_csv(args.input, args.output)


if __name__ == "__main__":
    main()
