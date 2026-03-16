import argparse
import logging
import pandas as pd
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def remove_duplicates(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    df = pd.read_csv(input_file)

    logging.info(f"Original rows: {len(df)}")

    df_clean = df.drop_duplicates()

    logging.info(f"Rows after deduplication: {len(df_clean)}")

    df_clean.to_csv(output_file, index=False)

    logging.info(f"Deduplicated dataset saved to: {output_file}")


def main():

    parser = argparse.ArgumentParser(description="Data Deduplication Tool")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file"
    )

    args = parser.parse_args()

    remove_duplicates(args.input, args.output)


if __name__ == "__main__":
    main()
