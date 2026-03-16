import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


class InvoiceClassifier:

    def __init__(self):

        self.pipeline = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("model", LogisticRegression())
        ])

    def train(self, texts, labels):

        self.pipeline.fit(texts, labels)

    def predict(self, text):

        return self.pipeline.predict([text])[0]
