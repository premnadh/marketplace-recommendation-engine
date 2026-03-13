import pandas as pd
from surprise import Dataset, Reader, SVD


class CollaborativeFilteringEngine:

    def __init__(self, interactions_path):

        print("Loading interaction dataset...")

        df = pd.read_csv(interactions_path)

        reader = Reader(rating_scale=(1, 5))

        data = Dataset.load_from_df(
            df[['user_id', 'product_id', 'rating']],
            reader
        )

        trainset = data.build_full_trainset()

        print("Training collaborative filtering model...")

        self.model = SVD()

        self.model.fit(trainset)

        print("Collaborative filtering ready.")

    def predict(self, user_id, product_id):

        prediction = self.model.predict(user_id, product_id)

        return prediction.est
