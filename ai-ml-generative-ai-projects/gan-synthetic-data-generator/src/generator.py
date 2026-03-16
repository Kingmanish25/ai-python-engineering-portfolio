import torch
import torch.nn as nn


class Generator(nn.Module):
    """
    Generator network
    Converts random noise into synthetic tabular samples
    """

    def __init__(self, noise_dim, output_dim):
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(noise_dim, 64),
            nn.BatchNorm1d(64),
            nn.LeakyReLU(0.2),

            nn.Linear(64, 128),
            nn.BatchNorm1d(128),
            nn.LeakyReLU(0.2),

            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, output_dim),
            nn.Tanh()
        )

    def forward(self, z):
        return self.model(z)
