from serpapi import GoogleSearch

FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

API_KEY = "YOUR_SERPAPI_KEY"


def fetch_image(product_title):
    """
    Fetch product image using Google Shopping results.
    This usually returns the exact product model image.
    """

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