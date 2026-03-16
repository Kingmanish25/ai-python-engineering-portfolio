import argparse
import logging
import pandas as pd
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_csv(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    df = pd.read_csv(input_file)

    logging.info(f"Original rows: {len(df)}")

    df_clean = df.dropna()

    logging.info(f"Rows after cleaning: {len(df_clean)}")

    df_clean.to_csv(output_file, index=False)

    logging.info(f"Cleaned data saved to: {output_file}")


def main():

    parser = argparse.ArgumentParser(description="CSV Data Cleaner")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output cleaned CSV file"
    )

    args = parser.parse_args()

    clean_csv(args.input, args.output)


if __name__ == "__main__":
    main()
