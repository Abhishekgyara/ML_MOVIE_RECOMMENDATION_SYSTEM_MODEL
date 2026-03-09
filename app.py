from flask import Flask,render_template,request
import joblib

app = Flask(__name__)

model = joblib.load("movie_model.pkl")
movie_matrix = joblib.load("movie_matrix.pkl")

movie_list = movie_matrix.index.tolist()

@app.route("/")
def home():
    return render_template("index.html",movies=movie_list)

@app.route("/recommend",methods=["POST"])
def recommend():

    movie = request.form["movie"]

    distances,indices = model.kneighbors(
        movie_matrix.loc[[movie]], n_neighbors=6
    )

    rec_movies = []

    for i in indices.flatten()[1:]:
        rec_movies.append(movie_matrix.index[i])

    return render_template(
        "index.html",
        movies=movie_list,
        recommendations=rec_movies
    )

if __name__=="__main__":
    app.run(debug=True)