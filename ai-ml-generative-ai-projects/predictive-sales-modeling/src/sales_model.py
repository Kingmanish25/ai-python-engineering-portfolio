import torch
import torch.nn as nn
import numpy as np


class SalesMLP(nn.Module):

    def __init__(self, input_size):

        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):

        return self.model(x)


class SalesLSTM(nn.Module):

    def __init__(self, input_size):

        super().__init__()

        self.lstm = nn.LSTM(input_size, 64, batch_first=True)

        self.fc = nn.Linear(64, 1)

    def forward(self, x):

        out, _ = self.lstm(x)

        out = out[:, -1, :]

        return self.fc(out)


def naive_forecast(series):

    return series.shift(1)


def moving_average(series, window=7):

    return series.rolling(window).mean()
