from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:

    def __init__(self, df):

        self.df = df

        self.vectorizer = TfidfVectorizer()

        self.product_features = (
            df["category"].astype(str) + " " +
            df["product_color"].astype(str) + " " +
            df["product_size"].astype(str)
        )

        self.feature_matrix = self.vectorizer.fit_transform(self.product_features)

        self.similarity = cosine_similarity(self.feature_matrix)

    def recommend(self, product_id, top_n=5):

        idx = self.df[self.df["product_id"] == product_id].index[0]

        scores = list(enumerate(self.similarity[idx]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        top_indices = [i[0] for i in scores[1:top_n+1]]

        return self.df.iloc[top_indices][["product_id", "category", "price"]]
