import streamlit as st
import sys
import urllib.parse
import pandas as pd
import time

# Fix imports
sys.path.append(".")

from src.hybrid_recommender import HybridRecommender
from src.image_fetcher import fetch_image


# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Marketplace Recommendation Engine",
    page_icon="🛍️",
    layout="wide"
)


# ---------------- STYLES ---------------- #
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:800;
}

.subtitle{
    text-align:center;
    font-size:20px;
    margin-bottom:30px;
    color:gray;
}

.search-box{
    max-width:900px;
    margin:auto;
}

.product-title{
    font-size:18px;
    font-weight:600;
}

.price{
    font-size:20px;
    font-weight:bold;
    color:#3CCF4E;
}

.card{
    padding:15px;
    border-radius:14px;
    background:#1e1e1e;
    text-align:center;
    margin-bottom:25px;
    transition:all 0.25s ease;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0px 10px 30px rgba(0,0,0,0.6);
}

.rating{
    color:#FFD700;
    font-size:18px;
}

.score{
    font-size:13px;
    margin-top:8px;
    color:#ccc;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ---------------- #
st.markdown("<div class='main-title'>🛍 Marketplace Recommendation Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Hybrid Recommender • Collaborative Filtering • Product Similarity</div>", unsafe_allow_html=True)


# ---------------- LOAD MODEL ---------------- #
@st.cache_resource
def load_engine():
    return HybridRecommender(
        "data/products.csv",
        "data/interactions.csv"
    )


engine = load_engine()


# ---------------- LOAD DATA ---------------- #
products_df = pd.read_csv("data/products.csv")
titles = products_df["title"].dropna().unique().tolist()


# ---------------- FILTERS ---------------- #
st.sidebar.header("🔧 Filters")

price_range = st.sidebar.slider(
    "Price Range",
    float(products_df["price"].min()),
    float(products_df["price"].max()),
    (float(products_df["price"].min()), float(products_df["price"].max()))
)

categories = products_df["category"].dropna().unique().tolist()

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(categories)
)

sort_option = st.sidebar.selectbox(
    "Sort By",
    ["Best Match", "Price Low → High", "Price High → Low"]
)


# ---------------- TRENDING ---------------- #
st.markdown("### 🔥 Trending Searches")

trend_cols = st.columns(5)

trending = [
    "Nike running shoes",
    "Nike Air Max",
    "Jordan shoes",
    "Converse sneakers",
    "Puma trainers"
]

selected_trend = None

for i, trend in enumerate(trending):
    if trend_cols[i].button(trend):
        selected_trend = trend


# ---------------- SEARCH ---------------- #
st.markdown("### 🔎 Search Products")

st.markdown("<div class='search-box'>", unsafe_allow_html=True)

query = st.selectbox(
    "Search for a product",
    titles,
    index=None,
    placeholder="Start typing: Nike running shoes..."
)

st.markdown("</div>", unsafe_allow_html=True)


# Use trending click
if selected_trend:
    query = selected_trend


# ---------------- DEFAULT STATE ---------------- #
if not query:
    st.markdown("""
    <div style='text-align:center;margin-top:80px;font-size:22px;color:gray'>
    🔍 Start typing or click a trending search to explore recommendations
    </div>
    """, unsafe_allow_html=True)


# ---------------- RESULTS ---------------- #
if query:

    with st.spinner("Finding best recommendations..."):
        time.sleep(1)

        results = engine.recommend(
            user_id=1,
            product_title=query,
            top_n=50
        )

    if results is None or len(results) == 0:
        st.warning("No recommendations found for this product.")
    else:

        # ---------------- APPLY FILTERS ---------------- #
        results = results[
            (results["price"] >= price_range[0]) &
            (results["price"] <= price_range[1])
        ]

        if selected_category != "All":
            results = results[results["category"] == selected_category]

        # ---------------- SORTING ---------------- #
        if sort_option == "Price Low → High":
            results = results.sort_values(by="price", ascending=True)

        elif sort_option == "Price High → Low":
            results = results.sort_values(by="price", ascending=False)

        # Keep top 20 results
        results = results.head(20)

        st.markdown("## 🧠 Recommended Products")

        cols = st.columns(4)

        for i, (_, row) in enumerate(results.iterrows()):

            img = fetch_image(row["title"])

            with cols[i % 4]:

                st.markdown("<div class='card'>", unsafe_allow_html=True)

                st.image(img, width=220)

                st.markdown(
                    f"<div class='product-title'>{row['title']}</div>",
                    unsafe_allow_html=True
                )

                st.caption(row["category"])

                st.markdown("<div class='rating'>⭐⭐⭐⭐☆</div>", unsafe_allow_html=True)

                st.markdown(
                    f"<div class='price'>${row['price']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class='score'>
                    <b>Why this was recommended:</b><br>
                    Similarity: {round(row['similarity_score'], 2)}<br>
                    User Preference: {round(row['collaborative_score'], 2)}<br>
                    Final Score: {round(row['final_score'], 2)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                link = f"https://www.amazon.com/s?k={urllib.parse.quote(row['title'])}"

                st.markdown(f"[🛒 Buy Product]({link})")

                st.markdown("</div>", unsafe_allow_html=True)