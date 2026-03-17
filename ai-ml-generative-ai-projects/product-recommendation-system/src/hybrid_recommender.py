class HybridRecommender:

    def __init__(self, content_model, collab_model):

        self.content_model = content_model
        self.collab_model = collab_model

    def recommend(self, user_id, product_id):

        content_rec = self.content_model.recommend(product_id)

        collab_rec = self.collab_model.recommend(user_id)

        print("\nContent-Based Recommendations:")
        print(content_rec)

        print("\nCollaborative Filtering Recommendations:")
        print(collab_rec)
