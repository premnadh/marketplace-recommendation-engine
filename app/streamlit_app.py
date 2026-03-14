import streamlit as st
import sys
import urllib.parse
import pandas as pd
import time

sys.path.append(".")

from src.hybrid_recommender import HybridRecommender
from src.image_fetcher import fetch_image


st.set_page_config(
    page_title="Marketplace Recommendation Engine",
    page_icon="🛍️",
    layout="wide"
)


# -----------------------------
# UI STYLE
# -----------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:800;
}

.subtitle{
    text-align:center;
    font-size:20px;
    margin-bottom:40px;
}

.search-box{
    max-width:900px;
    margin:auto;
}

.product-title{
    font-size:20px;
    font-weight:600;
}

.price{
    font-size:22px;
    font-weight:bold;
    color:#3CCF4E;
}

.card{
    padding:15px;
    border-radius:14px;
    background:#1e1e1e;
    text-align:center;
    margin-bottom:20px;
    transition:all 0.25s ease;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0px 8px 25px rgba(0,0,0,0.6);
}

.rating{
    color:#FFD700;
    font-size:18px;
}

.score{
    font-size:14px;
    margin-top:5px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='main-title'>🛍 Marketplace Recommendation Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Hybrid Recommender • Collaborative Filtering • Product Similarity</div>", unsafe_allow_html=True)


# -----------------------------
# LOAD RECOMMENDER
# -----------------------------
@st.cache_resource
def load_engine():
    try:
        return HybridRecommender(
            "data/products.csv",
            "data/interactions.csv"
        )
    except Exception as e:
        st.error(f"Engine loading failed: {e}")
        return None


engine = load_engine()

if engine is None:
    st.stop()


# -----------------------------
# LOAD PRODUCTS
# -----------------------------
try:
    products_df = pd.read_csv("data/products.csv")
except Exception as e:
    st.error(f"Products file failed to load: {e}")
    st.stop()

titles = products_df["title"].dropna().unique().tolist()


# -----------------------------
# TRENDING SEARCHES
# -----------------------------
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


# -----------------------------
# SEARCH BAR
# -----------------------------
st.markdown("### 🔎 Search Products")

st.markdown("<div class='search-box'>", unsafe_allow_html=True)

query = st.selectbox(
    "Search for a product",
    titles,
    index=None,
    placeholder="Start typing: Nike running shoes..."
)

st.markdown("</div>", unsafe_allow_html=True)


if selected_trend:
    query = selected_trend


# -----------------------------
# RECOMMENDATION ENGINE
# -----------------------------
if query:

    with st.spinner("Finding best recommendations..."):
        time.sleep(1)

        try:
            results = engine.recommend(
                user_id=1,
                product_title=query,
                top_n=20
            )
        except Exception as e:
            st.error(f"Recommendation error: {e}")
            results = None

    if results is None or len(results) == 0:

        st.warning("No recommendations found for this product.")

    else:

        st.markdown("## Recommended Products")

        cols = st.columns(4)

        for i, (_, row) in enumerate(results.iterrows()):

            try:
                img = fetch_image(row["title"])
            except:
                img = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

            with cols[i % 4]:

                st.markdown("<div class='card'>", unsafe_allow_html=True)

                st.image(img, width=220)

                st.markdown(
                    f"<div class='product-title'>{row['title']}</div>",
                    unsafe_allow_html=True
                )

                st.caption(row.get("category", ""))

                st.markdown(
                    "<div class='rating'>⭐⭐⭐⭐☆</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='price'>${row['price']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class='score'>
                    <b>Recommended Because</b><br>
                    Similarity Score: {row.get('similarity_score', 0):.2f}<br>
                    User Preference Score: {row.get('collaborative_score', 0):.2f}<br>
                    Final Hybrid Score: {row.get('final_score', 0):.2f}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                link = f"https://www.amazon.com/s?k={urllib.parse.quote(row['title'])}"

                st.markdown(f"[🛒 Buy Product]({link})")

                st.markdown("</div>", unsafe_allow_html=True)

else:

    st.markdown("""
    <div style='text-align:center;margin-top:80px;font-size:22px'>
    🔍 Search for a product to get personalized recommendations
    </div>
    """, unsafe_allow_html=True)