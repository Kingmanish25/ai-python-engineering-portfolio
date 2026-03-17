from data_loader import load_data
from feature_engineering import prepare_features, split_data
from model_training import train_model
from evaluation import evaluate


def run_pipeline():

    print("Loading data...")

    df = load_data("../data/data.csv")

    print("Dataset shape:", df.shape)

    print("\nPreparing features...")

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    print("Training model...")

    model = train_model(X_train, y_train)

    print("Evaluating model...")

    metrics = evaluate(model, X_test, y_test)

    print("\nModel Performance:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")


if __name__ == "__main__":
    run_pipeline()
