import os
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, TensorDataset

from generator import Generator
from discriminator import Discriminator


DATA_PATH = "data/dataset.csv"
MODEL_DIR = "models"
SCREENSHOT_DIR = "screenshots"

BATCH_SIZE = 64
EPOCHS = 200
NOISE_DIM = 32
LR = 0.0002


def load_dataset():

    df = pd.read_csv(DATA_PATH)

    features = df.drop(columns=["Outcome"])
    outcome = df["Outcome"]

    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    data = np.hstack([scaled_features, outcome.values.reshape(-1, 1)])

    return torch.tensor(data, dtype=torch.float32), scaler


def train():

    os.makedirs(MODEL_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    dataset, scaler = load_dataset()

    dataloader = DataLoader(
        TensorDataset(dataset),
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    input_dim = dataset.shape[1]

    generator = Generator(NOISE_DIM, input_dim)
    discriminator = Discriminator(input_dim)

    criterion = nn.BCELoss()

    g_optimizer = optim.Adam(generator.parameters(), lr=LR)
    d_optimizer = optim.Adam(discriminator.parameters(), lr=LR)

    g_losses = []
    d_losses = []

    for epoch in range(EPOCHS):

        for real_batch, in dataloader:

            batch_size = real_batch.size(0)

            real_labels = torch.ones(batch_size, 1)
            fake_labels = torch.zeros(batch_size, 1)

            # -----------------
            # Train Discriminator
            # -----------------

            noise = torch.randn(batch_size, NOISE_DIM)
            fake_data = generator(noise)

            real_output = discriminator(real_batch)
            fake_output = discriminator(fake_data.detach())

            d_loss_real = criterion(real_output, real_labels)
            d_loss_fake = criterion(fake_output, fake_labels)

            d_loss = d_loss_real + d_loss_fake

            d_optimizer.zero_grad()
            d_loss.backward()
            d_optimizer.step()

            # -----------------
            # Train Generator
            # -----------------

            noise = torch.randn(batch_size, NOISE_DIM)
            fake_data = generator(noise)

            output = discriminator(fake_data)

            g_loss = criterion(output, real_labels)

            g_optimizer.zero_grad()
            g_loss.backward()
            g_optimizer.step()

        g_losses.append(g_loss.item())
        d_losses.append(d_loss.item())

        if epoch % 20 == 0:
            print(f"Epoch {epoch}/{EPOCHS} | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

    torch.save(generator.state_dict(), os.path.join(MODEL_DIR, "generator.pth"))

    plot_training(g_losses, d_losses)


def plot_training(g_losses, d_losses):

    plt.figure(figsize=(8, 5))

    plt.plot(g_losses, label="Generator Loss")
    plt.plot(d_losses, label="Discriminator Loss")

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("GAN Training Loss")
    plt.legend()

    plt.savefig(os.path.join(SCREENSHOT_DIR, "img.jpg"))
    plt.close()


if __name__ == "__main__":
    train()
