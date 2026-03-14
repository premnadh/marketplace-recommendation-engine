import pandas as pd
from sklearn.decomposition import TruncatedSVD


class CollaborativeFilteringEngine:

    def __init__(self, interactions_path):
        print("Loading interaction data...")

        interactions = pd.read_csv(interactions_path)

        user_item_matrix = interactions.pivot_table(
            index="user_id",
            columns="item_id",
            values="rating",
            fill_value=0
        )

        self.user_item_matrix = user_item_matrix

        print("Training SVD model...")

        self.svd = TruncatedSVD(n_components=20, random_state=42)
        self.user_factors = self.svd.fit_transform(user_item_matrix)

        print("Collaborative filtering ready.")

    def recommend(self, user_id, top_n=10):

        if user_id not in self.user_item_matrix.index:
            return []

        user_index = list(self.user_item_matrix.index).index(user_id)

        scores = self.user_factors[user_index]

        item_scores = self.svd.inverse_transform(scores.reshape(1, -1))[0]

        recommendations = pd.Series(item_scores, index=self.user_item_matrix.columns)

        return recommendations.sort_values(ascending=False).head(top_n).index.tolist()