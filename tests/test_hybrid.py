from src.hybrid_recommender import HybridRecommender

engine = HybridRecommender(
    "data/products.csv",
    "data/interactions.csv"
)

results = engine.recommend(
    user_id=1,
    product_title="nike",
    top_n=5
)

print(results)