from serpapi import GoogleSearch
import os

FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

API_KEY = os.getenv("SERPAPI_KEY")


def fetch_image(product_title):
    """
    Fetch product image using Google Shopping results.
    """

    try:
        params = {
            "engine": "google_shopping",
            "q": product_title,
            "api_key": API_KEY,
            "num": 1
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        shopping_results = results.get("shopping_results", [])

        if shopping_results:
            return shopping_results[0]["thumbnail"]

    except Exception as e:
        print("Image fetch error:", e)

    return FALLBACK_IMAGE