# Predictive Sales Modeling (Retail)

This project implements a **production-style retail sales forecasting system** using statistical baselines, machine learning, and deep learning models.

The system predicts future sales using historical retail transaction data and evaluates multiple forecasting approaches.

---

# Project Overview

Retail businesses rely heavily on accurate demand forecasting to optimize inventory planning and supply chain decisions.

This project builds a complete machine learning pipeline that:

1. Loads raw transactional sales data
2. Aggregates time-series features
3. Generates lag-based forecasting features
4. Trains machine learning and deep learning models
5. Evaluates predictions using regression metrics

---

# Features

The system implements:

* Time-aware train/test splitting (no data leakage)
* Lag feature engineering
* Calendar feature extraction
* Benchmark baseline models
* PyTorch neural networks for forecasting
* Model evaluation using MAE and RMSE
* JSON-based metric reporting

---

# Models Implemented

### Naive Baseline

Uses the previous day's sales as prediction.

---

### Moving Average Baseline

Computes rolling averages to smooth short-term fluctuations.

---

### Feedforward Neural Network (MLP)

A PyTorch-based regression model trained on lag-based features.

Used for category-level sales prediction.

---

### LSTM Model

Deep learning model designed for sequential time-series data.

Captures temporal dependencies across historical sales sequences.

---

# Project Structure

```
predictive-sales-modeling
│
├── data
│   └── retail_sales.csv
│
├── notebooks
│
├── screenshots
│   └── img.jpg
│
├── src
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── sales_model.py
│   ├── evaluate_model.py
│   └── training_pipeline.py
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd predictive-sales-modeling
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Run the training pipeline:

```
python src/training_pipeline.py
```

The pipeline will:

* load retail sales data
* engineer time-series features
* train machine learning models
* evaluate forecasting performance

---

# Evaluation Metrics

Models are evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

These metrics help measure forecasting accuracy and business impact.

---

# Technologies Used

* Python
* PyTorch
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

# Applications

This project demonstrates techniques used in:

* retail demand forecasting
* supply chain analytics
* sales prediction systems
* AI-driven business planning

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

