import argparse
import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():

    parser = argparse.ArgumentParser(description="Generate secure password")

    parser.add_argument("--length", type=int, default=12)

    args = parser.parse_args()

    password = generate_password(args.length)

    print("Generated Password:", password)


if __name__ == "__main__":
    main()
