from data_loader import load_data
from content_based_filtering import ContentBasedRecommender
from collaborative_filtering import CollaborativeFiltering
from hybrid_recommender import HybridRecommender


def main():

    print("Loading dataset...")

    df = load_data("../data/data.csv")

    print("Total records:", len(df))

    print("Building models...")

    content_model = ContentBasedRecommender(df)

    collab_model = CollaborativeFiltering(df)

    hybrid = HybridRecommender(content_model, collab_model)

    # Example inputs
    sample_user = df["user_id"].iloc[0]
    sample_product = df["product_id"].iloc[0]

    print("\nRunning recommendations...")

    hybrid.recommend(sample_user, sample_product)


if __name__ == "__main__":
    main()
