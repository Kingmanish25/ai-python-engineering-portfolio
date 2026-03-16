import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler


def prepare_data(series, window=50):

    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(series.values.reshape(-1, 1))

    X = []
    y = []

    for i in range(window, len(scaled)):
        X.append(scaled[i - window:i])
        y.append(scaled[i])

    X = np.array(X)
    y = np.array(y)

    return X, y, scaler


def train_lstm(series):

    X, y, scaler = prepare_data(series)

    model = Sequential()

    model.add(LSTM(50, return_sequences=False, input_shape=(X.shape[1], 1)))
    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    model.fit(X, y, epochs=10, batch_size=32, verbose=1)

    return model, scaler
