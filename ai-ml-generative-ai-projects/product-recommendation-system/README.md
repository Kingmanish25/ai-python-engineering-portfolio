# Product Recommendation System

This project implements a **scalable hybrid recommendation system** combining:

* Content-Based Filtering
* Collaborative Filtering
* Hybrid Recommendation Engine

It simulates real-world recommendation systems used by platforms like:

* Amazon
* Netflix
* Flipkart

The system is built using **user behavior data, product features, and interaction signals** to generate personalized recommendations.

---

# Project Overview

Recommendation systems are a core component of modern digital platforms.

This project demonstrates how to:

* model user-product interactions
* extract product features
* compute similarity between users and items
* generate personalized recommendations
* combine multiple recommendation strategies

---

# Dataset

The dataset contains **60,000+ user-product interaction records**.

Features include:

* user behavior (clicks, session duration, page views)
* product attributes (category, price, color, size)
* purchase signals (add-to-cart, purchase history)
* demographics (age, gender, location)
* engagement metrics

Example:

```
user_id,product_id,category,price,rating,...
78517,1645,Books,842.23,2,...
```

---

# Recommendation Techniques

## Content-Based Filtering

Recommends products based on similarity of product features.

Uses:

* TF-IDF vectorization
* cosine similarity

Features used:

* category
* product color
* product size

---

## Collaborative Filtering

Recommends products based on **user behavior similarity**.

Approach:

* user-item interaction matrix
* cosine similarity between users

Captures:

* similar users
* shared preferences

---

## Hybrid Recommender

Combines:

* content-based recommendations
* collaborative filtering outputs

This improves:

* recommendation accuracy
* diversity
* robustness

---

# Project Structure

```
product-recommendation-system
│
├── data
│   └── data.csv
│
├── screenshots
│   └── img.png
│
├── src
│   ├── data_loader.py
│   ├── content_based_filtering.py
│   ├── collaborative_filtering.py
│   ├── hybrid_recommender.py
│   └── recommender_app.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Streamlit Web App

This project includes an **interactive UI using Streamlit**.

Features:

* select user
* select product
* view recommendations
* real-time results

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd product-recommendation-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

## Run CLI version

```
python src/recommender_app.py
```

---

## Run Streamlit App

```
streamlit run streamlit_app.py
```

---

# Example Output

* Recommended products for a user
* Similar products based on features
* Personalized suggestions

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* TF-IDF
* Cosine Similarity

---

# Applications

This project demonstrates techniques used in:

* e-commerce recommendation engines
* personalized marketing systems
* content recommendation platforms
* user behavior analytics

---

# Future Improvements

* Matrix factorization (ALS)
* Deep learning recommenders
* real-time recommendation API
* ranking metrics (Precision@K)
* A/B testing pipeline

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

