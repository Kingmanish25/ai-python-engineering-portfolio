from statsmodels.tsa.arima.model import ARIMA


def train_arima(series, order=(5, 1, 0)):
    """
    Train ARIMA forecasting model
    """

    model = ARIMA(series, order=order)
    model_fit = model.fit()

    return model_fit


def forecast_arima(model, steps=30):
    """
    Generate ARIMA forecast
    """

    forecast = model.forecast(steps=steps)

    return forecast
