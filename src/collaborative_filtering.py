import pandas as pd
from surprise import Dataset, Reader, SVD


class CollaborativeFilteringEngine:

    def __init__(self, interactions_path):

        print("Loading interaction data...")

        interactions = pd.read_csv(interactions_path)

        # ✅ Clean column names (important for real-world data)
        interactions.columns = interactions.columns.str.strip().str.lower()

        # ✅ Fix common column mismatch
        if "product_id" in interactions.columns:
            interactions = interactions.rename(columns={"product_id": "item_id"})

        # ✅ Validate required columns
        required_cols = ["user_id", "item_id", "rating"]
        if not all(col in interactions.columns for col in required_cols):
            raise ValueError(
                f"CSV must contain columns: {required_cols}, found: {interactions.columns.tolist()}"
            )

        print("Interactions shape:", interactions.shape)
        print("Unique users:", interactions["user_id"].nunique())
        print("Unique items:", interactions["item_id"].nunique())

        # ✅ Prepare Surprise dataset
        reader = Reader(rating_scale=(1, 5))

        data = Dataset.load_from_df(
            interactions[["user_id", "item_id", "rating"]],
            reader
        )

        trainset = data.build_full_trainset()

        print("Training SVD model...")

        self.model = SVD()
        self.model.fit(trainset)

        self.interactions = interactions

        print("Collaborative filtering ready.")

    def recommend(self, user_id, items, top_n=10):

        scores = []

        for item in items:
            pred = self.model.predict(user_id, item)
            scores.append((item, pred.est))

        # ✅ Sort by predicted rating
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        return [item for item, _ in scores[:top_n]]