import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

ratings = pd.read_csv("notebooks/ratings.csv")
movies = pd.read_csv("notebooks/movies.csv")

df = pd.merge(ratings, movies, on="movieId")

movie_matrix = df.pivot_table(index="title",
                              columns="userId",
                              values="rating").fillna(0)

model = NearestNeighbors(metric="cosine", algorithm="brute")

model.fit(movie_matrix)

joblib.dump(model,"movie_model.pkl")
joblib.dump(movie_matrix,"movie_matrix.pkl")

print("Model saved")