from src.similarity_search import ProductSimilarityEngine

engine = ProductSimilarityEngine("data/products.csv")

results = engine.recommend("Nike Running Shoes", top_n=5)

print(results)