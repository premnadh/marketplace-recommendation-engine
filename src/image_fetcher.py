from serpapi import GoogleSearch
import os

FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

API_KEY = "1b02ea2fa9e8fe14663389532a54d5b62a99db084ed802e6a30ec230d535e583"


def fetch_image(product_title):

    if not API_KEY:
        return FALLBACK_IMAGE

    try:
        params = {
            "engine": "google_shopping",
            "q": product_title,
            "api_key": "1b02ea2fa9e8fe14663389532a54d5b62a99db084ed802e6a30ec230d535e583",
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