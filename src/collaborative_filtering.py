import pandas as pd
from sklearn.decomposition import TruncatedSVD


class CollaborativeFilteringEngine:

    def __init__(self, interactions_path):
        print("Loading interaction data...")

        interactions = pd.read_csv(interactions_path)

        # Create user-item interaction matrix
        self.user_item_matrix = interactions.pivot_table(
            index="user_id",
            columns="item_id",
            values="rating",
            fill_value=0
        )

        print("Training collaborative filtering model...")

        self.svd = TruncatedSVD(n_components=20, random_state=42)

        # Latent user features
        self.user_factors = self.svd.fit_transform(self.user_item_matrix)

        print("Collaborative filtering ready.")

    def recommend(self, user_id, top_n=10):

        # Cold start handling
        if user_id not in self.user_item_matrix.index:
            print("User not found, returning empty recommendations.")
            return []

        # Get index position
        user_idx = self.user_item_matrix.index.get_loc(user_id)

        # Latent user representation
        user_vector = self.user_factors[user_idx]

        # Reconstruct predicted ratings
        predicted_ratings = self.svd.inverse_transform(
            user_vector.reshape(1, -1)
        )[0]

        # Rank items
        recommendations = pd.Series(
            predicted_ratings,
            index=self.user_item_matrix.columns
        )

        return (
            recommendations
            .sort_values(ascending=False)
            .head(top_n)
            .index
            .tolist()
        )