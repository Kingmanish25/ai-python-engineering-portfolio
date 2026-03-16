import torch
import pandas as pd
import numpy as np
from generator import Generator


MODEL_PATH = "models/generator.pth"
OUTPUT_PATH = "data/generated_samples.csv"

NOISE_DIM = 32
OUTPUT_DIM = 9
SAMPLES = 500


def generate():

    generator = Generator(NOISE_DIM, OUTPUT_DIM)

    generator.load_state_dict(torch.load(MODEL_PATH))
    generator.eval()

    noise = torch.randn(SAMPLES, NOISE_DIM)

    with torch.no_grad():
        synthetic = generator(noise).numpy()

    columns = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
        "Outcome"
    ]

    df = pd.DataFrame(synthetic, columns=columns)

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Synthetic dataset saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    generate()
