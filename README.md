# 🛍️ Marketplace Recommendation Engine
### Hybrid AI Recommendation System for Product Discovery

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered product recommendation system** that simulates how modern e-commerce platforms suggest relevant products to users.

The system combines **Collaborative Filtering and Content-Based Similarity Search** to generate personalized product recommendations and presents them through an **interactive Streamlit web interface**.

---

# 🎯 Project Objective

The goal of this project is to build a **production-style recommendation engine** similar to those used by modern marketplace platforms.

Users can:

- Search for a product
- Receive **AI-generated recommendations**
- View similar products with images
- Navigate to purchase pages
- Explore product discovery through a recommendation system

---

# 🧠 Recommendation System Architecture

The system uses a **Hybrid Recommendation Model** combining two approaches.

```
User Query
     ↓
Product Similarity Engine
(TF-IDF + Cosine Similarity)
     ↓
Collaborative Filtering
(SVD Matrix Factorization)
     ↓
Hybrid Scoring System
     ↓
Top-N Product Recommendations
```

This hybrid approach improves recommendation quality by combining:

- User behavior patterns
- Product similarity relationships

---

# 🚀 Key Features

## 🔎 Smart Product Search

Users can search products such as:

```
Nike running shoes
Jordan sneakers
Adidas ultraboost
```

The system returns **20 recommended products** based on similarity and user interaction patterns.

---

## 🤖 Hybrid Recommendation Engine

Two recommendation algorithms are combined.

### Content-Based Filtering

- TF-IDF vectorization
- Cosine similarity
- Finds similar products based on descriptions

### Collaborative Filtering

- Matrix factorization using SVD
- Learns patterns from user-item interactions

Final recommendation score:

```
Final Score =
0.6 × Collaborative Score
+
0.4 × Similarity Score
```

---

# 🖥️ Interactive Web Interface

A modern UI built with **Streamlit** allows users to:

- Search products
- View recommendations in a **grid layout**
- See product images
- Access purchase links

The UI simulates a **marketplace product discovery page**.

---

# 🛒 External Purchase Links

Each recommendation includes a **purchase link** that redirects to an online marketplace search.

Example:

```
Nike Running Shoes
Price: $45
Category: Athletic

Buy Product → Opens marketplace search
```

---

# 📊 Dataset

This project uses a dataset derived from the **Mercari Price Suggestion Dataset**.

Dataset contains:

- Product titles
- Categories
- Descriptions
- Prices

Additional **synthetic user interactions** were generated to train the collaborative filtering model.

---

# 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Machine Learning | Scikit-learn |
| Recommendation Algorithm | TF-IDF + Cosine Similarity + SVD |
| Web Interface | Streamlit |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Version Control | Git & GitHub |

---

# ⚙️ Project Architecture

```
marketplace-recommendation-engine
│
├── app
│   └── streamlit_app.py
│
├── src
│   ├── similarity_search.py
│   ├── collaborative_filtering.py
│   ├── hybrid_recommender.py
│   └── image_fetcher.py
│
├── data
│   ├── products.csv
│   └── interactions.csv
│
├── tests
│   ├── test_similarity.py
│   ├── test_collaborative.py
│   └── test_hybrid.py
│
├── prepare_products.py
├── requirements.txt
└── README.md
```

---

# ▶️ Run Locally

Clone repository

```
git clone https://github.com/yourusername/marketplace-recommendation-engine.git
```

Navigate into project

```
cd marketplace-recommendation-engine
```

Create virtual environment

```
python3 -m venv venv
```

Activate environment (Mac / Linux)

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
streamlit run app/streamlit_app.py
```

Open in browser

```
http://localhost:8501
```

---

# 📈 Example Workflow

```
User searches: "Nike running shoes"
        ↓
System finds similar products
        ↓
Collaborative filtering adjusts rankings
        ↓
Top 20 recommendations displayed
        ↓
User explores recommended products
```

---

# 🌟 Key Highlights

- Hybrid recommendation system
- Machine learning powered product discovery
- Interactive web application
- Real marketplace dataset
- Scalable recommendation architecture

---

# 🚀 Future Improvements

- Real-time recommendation updates
- Vector search using FAISS
- User behavior tracking
- Product rating prediction
- Cloud deployment
- Full e-commerce frontend integration

---

# 👤 Author

**Prem Nadh Gajula**

Aspiring **Data Scientist / Machine Learning Engineer**

Interested in:

- AI systems
- recommendation engines
- scalable data platforms

If you find this project useful, please ⭐ the repository!