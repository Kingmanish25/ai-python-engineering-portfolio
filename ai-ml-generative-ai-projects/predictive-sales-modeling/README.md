# Predictive Sales Modeling (Retail)

This project implements an **end-to-end retail sales forecasting system** using statistical baselines, machine learning, and deep learning techniques.

The goal is to predict future retail revenue using historical transaction data while following **production-style machine learning pipeline practices**.

---

# Project Overview

Retail businesses rely heavily on accurate demand forecasting to support:

* inventory planning
* marketing strategies
* supply chain optimization
* revenue forecasting

This project converts raw retail transaction data into **time-series datasets** and trains forecasting models using engineered features.

The pipeline includes:

1. Data ingestion and preprocessing
2. Time-series aggregation
3. Feature engineering
4. Baseline forecasting models
5. PyTorch-based neural network forecasting
6. Model evaluation and reporting

---

# Dataset

The dataset contains **retail transaction records** with customer and product information.

Example dataset structure:

```
Transaction ID,date,Customer ID,Gender,Age,Product Category,Quantity,Price per Unit,Total Amount
1,24-11-2023,CUST001,Male,34,Beauty,3,50,150
2,27-02-2023,CUST002,Female,26,Clothing,2,500,1000
3,13-01-2023,CUST003,Male,50,Electronics,1,30,30
```

Each row represents a **single transaction**.

For forecasting, transactions are aggregated into **daily sales revenue time-series data**.

---

# Feature Engineering

To improve forecasting performance, several features are generated:

### Calendar Features

* day_of_week
* month

These help capture seasonal purchasing patterns.

---

### Lag Features

* lag_1
* lag_7
* lag_14

Lag features allow the model to learn temporal dependencies.

---

### Rolling Statistics

* rolling_mean_7

Rolling averages smooth short-term fluctuations and capture local trends.

---

# Baseline Models

Before applying machine learning models, benchmark baselines are implemented:

### Naive Forecast

Uses the previous day's sales as prediction.

```
Sales(t) = Sales(t-1)
```

---

### Moving Average

Uses rolling averages of previous days to generate predictions.

These baselines provide **fair performance comparisons for ML models**.

---

# Machine Learning Model

The project implements a **PyTorch Feedforward Neural Network (MLP)** for sales forecasting.

Model architecture:

```
Input Features
      ↓
Linear Layer (64)
      ↓
ReLU
      ↓
Linear Layer (32)
      ↓
ReLU
      ↓
Output (Predicted Sales)
```

The neural network learns nonlinear relationships between engineered features and future sales.

---

# Evaluation Metrics

Model performance is evaluated using:

### Mean Absolute Error (MAE)

Measures average prediction error.

### Root Mean Squared Error (RMSE)

Penalizes large forecasting errors more strongly.

These metrics help compare baseline and machine learning models.

---

# Project Structure

```
predictive-sales-modeling
│
├── data
│   └── retail_sales.csv
│
├── notebooks
│   └── sales_forecasting_analysis.ipynb
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

1. Load retail transaction data
2. Aggregate daily revenue
3. Generate forecasting features
4. Train the PyTorch model
5. Evaluate model performance

---

# Notebook Analysis

The notebook contains:

* exploratory data analysis
* sales trend visualization
* baseline forecasting experiments
* feature engineering demonstrations

Run the notebook:

```
jupyter notebook notebooks/sales_forecasting_analysis.ipynb
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* PyTorch
* Scikit-learn
* Matplotlib
* Seaborn

---

# Applications

This project demonstrates techniques used in:

* retail demand forecasting
* revenue prediction
* supply chain analytics
* machine learning for business planning

---

# Future Improvements

Potential enhancements include:

* LSTM deep learning forecasting
* hyperparameter tuning
* MLflow experiment tracking
* automated forecast dashboards
* multi-category sales forecasting

---

# Author

Manish Rathi
AI & Python Engineering Portfolio
