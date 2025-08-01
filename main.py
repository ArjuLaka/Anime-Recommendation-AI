import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from recommender import recommend

# === Load Dataset ===
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/RecentViewedAnime.csv")
    df['features'] = df.apply(lambda row: f"{row['genres']} {row['demographic']} {row['studio']}", axis=1)
    return df

df = load_data()

# === Vectorization and Similarity ===
vectorizer = CountVectorizer().fit_transform(df['features'])
similarity_matrix = cosine_similarity(vectorizer)

# === Streamlit UI ===
st.set_page_config(page_title="Anime Recommender", layout="centered")
st.title("🎌 Anime Recommendation System")
st.write("Rekomendasi anime berdasarkan genre, studio, dan demografi.")

anime_titles = df['title'].tolist()
selected_title = st.selectbox("Pilih anime favorit kamu:", anime_titles)

top_n = st.slider("Jumlah rekomendasi", 1, 10, 5)

if st.button("Tampilkan Rekomendasi"):
    results = recommend(selected_title, top_n, False)
    if not results:
        st.warning("Anime tidak ditemukan dalam database.")
    else:
        st.subheader("Rekomendasi Anime:")
        for anime in results:
            st.markdown(f"**{anime['title']}**")
            st.markdown(f"- 🎯 Rating: {anime['rating']}")
            st.markdown(f"- 📆 Tahun: {anime['yearReleased']}")
            st.markdown(f"- 📺 Studio: {anime['studio']}")
            st.markdown(f"- 🧬 Genre: {anime['genres']}")
            st.markdown("---")
