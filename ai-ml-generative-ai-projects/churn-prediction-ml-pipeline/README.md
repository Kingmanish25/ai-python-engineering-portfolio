# Customer Churn Prediction ML Pipeline

This project implements an **end-to-end machine learning pipeline** for predicting customer churn.

Customer churn prediction is a critical problem in industries such as:

* banking
* telecom
* SaaS platforms
* subscription services

The system identifies customers likely to leave, enabling proactive retention strategies.

---

# Project Overview

Customer churn has a direct impact on revenue and customer lifetime value.

This project demonstrates how to:

* preprocess customer data
* engineer meaningful features
* train a classification model
* evaluate model performance
* build an end-to-end ML pipeline

---

# Dataset

The dataset contains customer-level information such as:

* account balance
* number of products
* credit card ownership
* tenure
* activity status
* churn label (Exited)

Example:

```
CustomerId,Balance,NumOfProducts,HasCrCard,Tenure,IsActiveMember,Exited
15634602,0.0,1,Yes,2,Yes,1
15647311,83807.86,1,Yes,1,Yes,0
```

---

# Features

## Data Preprocessing

* currency cleaning (removal of € symbol)
* categorical encoding (Yes/No → 1/0)
* duplicate removal
* feature scaling

---

## Feature Engineering

* separation of features and target
* normalization using StandardScaler
* train-test split (80/20)

---

## Model Training

The project uses **Logistic Regression** as a baseline model.

Advantages:

* interpretable
* efficient
* strong baseline for classification

---

## Evaluation Metrics

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

These metrics provide a comprehensive understanding of classification performance.

---

# Project Structure

```
churn-prediction-ml-pipeline
│
├── data
│   └── data.csv
│
├── notebooks
│
├── screenshots
│   └── img.jpg
│
├── src
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── ml_pipeline.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Machine Learning Pipeline

```
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Evaluation
   ↓
Prediction
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd churn-prediction-ml-pipeline
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

## Run ML Pipeline

```
python src/ml_pipeline.py
```

---

## Run Streamlit App

```
streamlit run streamlit_app.py
```

---

# Streamlit App

The project includes an interactive UI where users can:

* input customer details
* predict churn probability
* analyze risk level

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

# Applications

This project demonstrates techniques used in:

* customer retention systems
* banking analytics
* subscription churn prediction
* business intelligence

---

# Future Improvements

* XGBoost / Random Forest models
* ROC-AUC curve visualization
* feature importance analysis
* model deployment (FastAPI)
* real-time prediction systems

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

