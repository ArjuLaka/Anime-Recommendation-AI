import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === Load Dataset ===
def load_data():
    df = pd.read_csv("datasets/RecentViewedAnime.csv")
    df['features'] = df.apply(lambda row: f"{row['genres']} {row['demographic']} {row['studio']}", axis=1)
    return df

df = load_data()

# === Vectorization and Similarity ===
vectorizer = CountVectorizer().fit_transform(df['features'])
similarity_matrix = cosine_similarity(vectorizer)

# === Recommendation Function ===
def recommend(title, top_n=5, using_cmd=True):
    index = df[df.title.str.lower() == title.lower()].index
    if len(index) == 0:
        return []
    index = index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    if using_cmd == True:
        recommendations = [df.iloc[i[0]].title for i in scores[1:top_n+1]]
    else: 
        recommendations = [df.iloc[i[0]] for i in scores[1:top_n+1]]
    return recommendations

if __name__ == "__main__":
    print(recommend(sys.argv[1], int(sys.argv[2])))