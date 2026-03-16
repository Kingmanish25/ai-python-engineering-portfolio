import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler


def prepare_data(series, lookback=10):

    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(series.values.reshape(-1, 1))

    X, y = [], []

    for i in range(len(scaled) - lookback):

        X.append(scaled[i:i + lookback])

        y.append(scaled[i + lookback])

    X = np.array(X)
    y = np.array(y)

    return X, y, scaler


def train_lstm(series):

    X, y, scaler = prepare_data(series)

    model = Sequential()

    model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))

    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    model.fit(X, y, epochs=10, batch_size=32, verbose=1)

    return model, scaler
