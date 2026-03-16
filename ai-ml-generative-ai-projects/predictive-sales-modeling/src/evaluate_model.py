import numpy as np


def mae(y_true, y_pred):

    return np.mean(np.abs(y_true - y_pred))


def rmse(y_true, y_pred):

    return np.sqrt(np.mean((y_true - y_pred) ** 2))


def evaluate(y_true, y_pred):

    return {
        "MAE": mae(y_true, y_pred),
        "RMSE": rmse(y_true, y_pred)
    }
