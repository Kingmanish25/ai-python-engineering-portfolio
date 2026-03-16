import torch
import torch.optim as optim
import pandas as pd
import numpy as np
import json

from data_loader import load_data, train_test_split_time
from feature_engineering import create_features
from sales_model import SalesMLP
from evaluate_model import evaluate


def run_pipeline():

    df = load_data()

    df = create_features(df)

    train, test = train_test_split_time(df)

    features = ["lag_1", "lag_7", "lag_14", "rolling_mean_7", "day_of_week", "month"]

    X_train = train[features].values
    y_train = train["sales"].values

    X_test = test[features].values
    y_test = test["sales"].values

    X_train = torch.tensor(X_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

    X_test = torch.tensor(X_test, dtype=torch.float32)

    model = SalesMLP(X_train.shape[1])

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    loss_fn = torch.nn.MSELoss()

    for epoch in range(50):

        preds = model(X_train)

        loss = loss_fn(preds, y_train)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        if epoch % 10 == 0:

            print("Epoch:", epoch, "Loss:", loss.item())

    predictions = model(X_test).detach().numpy().flatten()

    metrics = evaluate(y_test, predictions)

    print("\nModel Performance")
    print(metrics)

    with open("../metrics.json", "w") as f:

        json.dump(metrics, f)


if __name__ == "__main__":

    run_pipeline()
