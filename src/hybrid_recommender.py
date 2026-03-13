import pandas as pd
from src.similarity_search import ProductSimilarityEngine
from src.collaborative_filtering import CollaborativeFilteringEngine


class HybridRecommender:

    def __init__(self, products_path, interactions_path):

        self.sim_engine = ProductSimilarityEngine(products_path)
        self.collab_engine = CollaborativeFilteringEngine(interactions_path)

        self.products = self.sim_engine.products


    def recommend(self, user_id, product_title, top_n=20):

        idx = self.products[
            self.products["title"].str.contains(
                product_title,
                case=False,
                na=False
            )
        ].index

        if len(idx) == 0:
            return None

        idx = idx[0]

        similarity_scores = list(
            enumerate(self.sim_engine.similarity_matrix[idx])
        )

        results = []

        for product_idx, sim_score in similarity_scores:

            product = self.products.iloc[product_idx]
            product_id = product["product_id"]

            try:
                collab_score = self.collab_engine.predict(
                    user_id,
                    product_id
                )
            except:
                collab_score = 0

            final_score = (0.6 * collab_score) + (0.4 * sim_score)

            results.append({
                "title": product["title"],
                "category": product["category"],
                "price": product["price"],
                "similarity_score": round(float(sim_score), 3),
                "collaborative_score": round(float(collab_score), 3),
                "final_score": round(float(final_score), 3)
            })

        results = sorted(
            results,
            key=lambda x: x["final_score"],
            reverse=True
        )

        results = results[1: top_n + 1]

        return pd.DataFrame(results)