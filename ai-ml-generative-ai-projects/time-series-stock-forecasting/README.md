# Time Series Stock Forecasting

This project demonstrates **time series forecasting for stock prices** using multiple machine learning and statistical models.

The system compares several forecasting approaches to predict future stock prices based on historical market data.

---

# Project Overview

Stock markets generate large volumes of time-series data.
Predicting future prices requires specialized models capable of capturing temporal patterns and trends.

This project implements multiple forecasting techniques including:

* ARIMA statistical forecasting
* Facebook Prophet forecasting
* LSTM deep learning forecasting

The pipeline loads historical market data, trains models, generates predictions, and visualizes forecast results.

---

# Dataset

The dataset contains historical stock market data including:

* Adjusted Close Price
* Closing Price
* High Price
* Low Price
* Opening Price
* Trading Volume

Example structure:

```
Date,Adj Close,Close,High,Low,Open,Volume
1980-12-12,0.0988,0.1283,0.1289,0.1283,0.1283,469033600
1980-12-15,0.0936,0.1216,0.1222,0.1216,0.1222,175884800
```

---

# Models Implemented

## ARIMA Model

A classical statistical forecasting model designed for time-series analysis.

Used to capture:

* trends
* seasonality
* autoregressive relationships

---

## Facebook Prophet

A forecasting library developed by Meta for business time-series forecasting.

Capabilities:

* automatic trend detection
* robust to missing values
* interpretable forecasts

---

## LSTM Neural Network

A deep learning model capable of learning long-term dependencies in sequential data.

LSTM models are widely used for:

* financial forecasting
* demand prediction
* sequential data modeling

---

# Project Structure

```
time-series-stock-forecasting
│
├── data
│   └── data.csv
│
├── screenshots
│   └── img.png
│
├── src
│   ├── arima_model.py
│   ├── data_loader.py
│   ├── forecasting_pipeline.py
│   ├── lstm_model.py
│   └── prophet_model.py
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd time-series-stock-forecasting
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Run the forecasting pipeline:

```
python src/forecasting_pipeline.py
```

The system will:

1. Load historical stock market data
2. Train forecasting models
3. Generate price predictions
4. Visualize forecast results

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Statsmodels
* Facebook Prophet
* TensorFlow
* Scikit-learn

---

# Applications

This project demonstrates techniques used in:

* financial time series forecasting
* quantitative finance
* algorithmic trading research
* machine learning for financial analytics

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

