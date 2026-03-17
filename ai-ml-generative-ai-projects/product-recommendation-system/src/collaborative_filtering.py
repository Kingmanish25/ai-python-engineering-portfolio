import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class CollaborativeFiltering:

    def __init__(self, df):

        self.df = df

        # user-item matrix
        self.user_item = df.pivot_table(
            index="user_id",
            columns="product_id",
            values="rating"
        ).fillna(0)

        self.similarity = cosine_similarity(self.user_item)

        self.sim_df = pd.DataFrame(
            self.similarity,
            index=self.user_item.index,
            columns=self.user_item.index
        )

    def recommend(self, user_id, top_n=5):

        similar_users = self.sim_df[user_id].sort_values(ascending=False)[1:6]

        similar_users_ids = similar_users.index

        products = self.df[self.df["user_id"].isin(similar_users_ids)]

        recommendations = (
            products.groupby("product_id")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(top_n)
        )

        return recommendations
