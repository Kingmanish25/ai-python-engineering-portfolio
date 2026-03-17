import streamlit as st

from src.data_loader import load_data
from src.content_based_filtering import ContentBasedRecommender
from src.collaborative_filtering import CollaborativeFiltering
from src.hybrid_recommender import HybridRecommender


st.set_page_config(page_title="Recommender System", layout="wide")

st.title("🛍️ Product Recommendation System")

st.write("Hybrid Recommendation Engine (Content + Collaborative)")


@st.cache_data
def load_models():

    df = load_data("data/data.csv")

    content_model = ContentBasedRecommender(df)

    collab_model = CollaborativeFiltering(df)

    return df, content_model, collab_model


df, content_model, collab_model = load_models()

# Sidebar
st.sidebar.header("User Input")

user_id = st.sidebar.selectbox(
    "Select User",
    df["user_id"].unique()
)

product_id = st.sidebar.selectbox(
    "Select Product",
    df["product_id"].unique()
)

if st.sidebar.button("Get Recommendations"):

    st.subheader("📌 Content-Based Recommendations")

    content_results = content_model.recommend(product_id)

    st.dataframe(content_results)

    st.subheader("👥 Collaborative Filtering Recommendations")

    collab_results = collab_model.recommend(user_id)

    st.write(collab_results)

    st.success("Recommendations generated successfully!")
