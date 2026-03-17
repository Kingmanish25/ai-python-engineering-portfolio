import streamlit as st
import numpy as np

from src.data_loader import load_data
from src.feature_engineering import prepare_features, split_data
from src.model_training import train_model


st.set_page_config(page_title="Churn Prediction", layout="wide")

st.title("📊 Customer Churn Prediction")

st.write("Predict whether a customer is likely to churn.")


@st.cache_data
def load_model():

    df = load_data("data/data.csv")

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_model(X_train, y_train)

    return model


model = load_model()


st.sidebar.header("Customer Inputs")

balance = st.sidebar.number_input("Balance", 0.0, 200000.0, 50000.0)
products = st.sidebar.slider("Number of Products", 1, 5, 2)
credit_card = st.sidebar.selectbox("Has Credit Card", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure", 0, 10, 3)
active = st.sidebar.selectbox("Active Member", ["Yes", "No"])


if st.sidebar.button("Predict"):

    credit_card = 1 if credit_card == "Yes" else 0
    active = 1 if active == "Yes" else 0

    input_data = np.array([[balance, products, credit_card, tenure, active]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")
