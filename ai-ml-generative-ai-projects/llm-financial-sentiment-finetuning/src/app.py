import streamlit as st
from inference import SentimentPredictor
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Sentiment AI", layout="centered")

st.title("💬 Financial Sentiment Analysis (LLM + BERT)")
st.write("Analyze sentiment of financial news/headlines using a fine-tuned transformer model.")

@st.cache_resource
def load_model():
    return SentimentPredictor()

predictor = load_model()

user_input = st.text_area("Enter financial text:", height=120)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        sentiment, confidence, probs = predictor.predict(user_input)

        st.subheader("📊 Prediction Result")
        st.success(f"Sentiment: {sentiment}")
        st.write(f"Confidence: {confidence:.4f}")

        # Probability chart
        labels = ["Negative", "Positive"]

        fig, ax = plt.subplots()
        ax.bar(labels, probs)
        ax.set_title("Prediction Probabilities")

        st.pyplot(fig)
