import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

movies["genre"] = movies["genre"].fillna("")
movies["overview"] = movies["overview"].fillna("")

movies["content"] = movies["genre"] + " " + movies["overview"]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["content"])

similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend(movie_name, num_recommendations=5):
    """
    Recommend similar movies using Content-Based Filtering.
    """

    movie_name = movie_name.lower()

    movie_indices = movies[
        movies["title"].str.lower() == movie_name
    ].index

    if len(movie_indices) == 0:
        return None

    movie_index = movie_indices[0]

    similarity_scores = list(enumerate(similarity[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:num_recommendations + 1]

    recommendations = []

    for i in similarity_scores:
        recommendations.append(movies.iloc[i[0]]["title"])

    return recommendations