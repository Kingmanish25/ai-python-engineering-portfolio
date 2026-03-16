import argparse
import logging
import pandas as pd
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def analyze_dataset(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    df = pd.read_csv(input_file)

    logging.info(f"Dataset loaded successfully")
    logging.info(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    stats = df.describe()

    stats.to_csv(output_file)

    logging.info(f"Dataset statistics saved to: {output_file}")

    print("\nDataset Summary Statistics:\n")
    print(stats)


def main():

    parser = argparse.ArgumentParser(description="Dataset Statistics Analyzer")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV dataset"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output statistics CSV file"
    )

    args = parser.parse_args()

    analyze_dataset(args.input, args.output)


if __name__ == "__main__":
    main()
