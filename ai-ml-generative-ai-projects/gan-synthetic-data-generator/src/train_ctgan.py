import os
import pandas as pd
import matplotlib.pyplot as plt

from ctgan import CTGAN


DATA_PATH = "data/dataset.csv"
OUTPUT_DIR = "data"
SCREENSHOT_DIR = "screenshots"


def train_ctgan():

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Training CTGAN model...")

    model = CTGAN(
        epochs=300,
        batch_size=64,
        verbose=True
    )

    model.fit(df)

    print("Generating synthetic samples...")

    synthetic = model.sample(1000)

    synthetic_path = os.path.join(OUTPUT_DIR, "ctgan_synthetic_data.csv")

    synthetic.to_csv(synthetic_path, index=False)

    print(f"Synthetic data saved: {synthetic_path}")

    visualize(df, synthetic)


def visualize(real, synthetic):

    plt.figure(figsize=(8,5))

    plt.hist(real["Glucose"], bins=30, alpha=0.5, label="Real")
    plt.hist(synthetic["Glucose"], bins=30, alpha=0.5, label="Synthetic")

    plt.title("Real vs Synthetic Distribution (Glucose)")
    plt.legend()

    path = os.path.join(SCREENSHOT_DIR, "ctgan_distribution.jpg")

    plt.savefig(path)

    plt.close()

    print("Visualization saved:", path)


if __name__ == "__main__":
    train_ctgan()
