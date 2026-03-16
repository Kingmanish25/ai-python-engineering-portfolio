from itertools import product
from statsmodels.tsa.arima.model import ARIMA
import numpy as np


def tune_arima(series):

    p = d = q = range(0, 3)

    best_score = float("inf")
    best_order = None

    for order in product(p, d, q):

        try:

            model = ARIMA(series, order=order)

            results = model.fit()

            aic = results.aic

            if aic < best_score:

                best_score = aic
                best_order = order

        except:
            continue

    return best_order
