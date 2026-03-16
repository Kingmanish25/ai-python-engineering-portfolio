import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


REAL_DATA_PATH = "data/dataset.csv"
SYNTH_DATA_PATH = "data/ctgan_synthetic_data.csv"
SCREENSHOT_DIR = "screenshots"


def load_data():

    real = pd.read_csv(REAL_DATA_PATH)
    synthetic = pd.read_csv(SYNTH_DATA_PATH)

    return real, synthetic


def statistical_similarity(real, synthetic):

    print("\n=== Statistical Comparison ===")

    stats = pd.DataFrame({
        "Real Mean": real.mean(),
        "Synthetic Mean": synthetic.mean(),
        "Real Std": real.std(),
        "Synthetic Std": synthetic.std()
    })

    print(stats)

    return stats


def correlation_similarity(real, synthetic):

    real_corr = real.corr()
    synth_corr = synthetic.corr()

    diff = np.abs(real_corr - synth_corr)

    score = diff.mean().mean()

    print("\nCorrelation difference score:", score)

    return real_corr, synth_corr


def plot_distributions(real, synthetic):

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    columns = real.columns

    for col in columns:

        plt.figure(figsize=(6,4))

        sns.kdeplot(real[col], label="Real")
        sns.kdeplot(synthetic[col], label="Synthetic")

        plt.title(f"Distribution Comparison: {col}")
        plt.legend()

        path = os.path.join(SCREENSHOT_DIR, f"dist_{col}.png")

        plt.savefig(path)

        plt.close()


def plot_correlation(real_corr, synth_corr):

    plt.figure(figsize=(8,6))

    sns.heatmap(real_corr, annot=False)

    plt.title("Real Data Correlation")

    plt.savefig(os.path.join(SCREENSHOT_DIR, "real_correlation.png"))

    plt.close()


    plt.figure(figsize=(8,6))

    sns.heatmap(synth_corr, annot=False)

    plt.title("Synthetic Data Correlation")

    plt.savefig(os.path.join(SCREENSHOT_DIR, "synthetic_correlation.png"))

    plt.close()


def run_evaluation():

    real, synthetic = load_data()

    stats = statistical_similarity(real, synthetic)

    real_corr, synth_corr = correlation_similarity(real, synthetic)

    plot_distributions(real, synthetic)

    plot_correlation(real_corr, synth_corr)

    print("\nEvaluation complete.")


if __name__ == "__main__":
    run_evaluation()
