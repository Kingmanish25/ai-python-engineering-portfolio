import argparse
import json
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def transform_json(input_file, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_file, "r") as f:
        data = json.load(f)

    logging.info("JSON file loaded successfully")

    # Example transformation: convert keys to uppercase
    transformed_data = {key.upper(): value for key, value in data.items()}

    with open(output_file, "w") as f:
        json.dump(transformed_data, f, indent=4)

    logging.info(f"Transformed JSON saved to: {output_file}")

    print("\nTransformed JSON:\n")
    print(json.dumps(transformed_data, indent=4))


def main():

    parser = argparse.ArgumentParser(description="JSON Data Transformer")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input JSON file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output JSON file"
    )

    args = parser.parse_args()

    transform_json(args.input, args.output)


if __name__ == "__main__":
    main()
