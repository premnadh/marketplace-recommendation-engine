import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ProductSimilarityEngine:

    def __init__(self, products_path):
        print("Loading products dataset...")
        self.products = pd.read_csv(products_path)

        # combine text fields
        self.products["text"] = (
            self.products["title"].fillna("") + " " +
            self.products["description"].fillna("") + " " +
            self.products["category"].fillna("")
        )

        print("Building TF-IDF matrix...")

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.products["text"])

        print("Computing similarity matrix...")
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

        print("Similarity engine ready.")

    def recommend(self, product_title, top_n=5):

        idx = self.products[
            self.products["title"].str.contains(product_title, case=False, na=False)
        ].index

        if len(idx) == 0:
            print("Product not found")
            return None

        idx = idx[0]

        scores = list(enumerate(self.similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        scores = scores[1: top_n + 1]

        product_indices = [i[0] for i in scores]

        return self.products.iloc[product_indices][["title", "category", "price"]]
