# Movie Recommendation System 🎬

This project is a **machine learning based movie recommendation web application** built using **Python, Flask, and HTML/CSS**. The system recommends movies based on similarity in user rating patterns.

The project uses the **MovieLens 100K dataset**, which contains movie ratings given by users. Using this data, the system learns which movies are similar to each other.

## How It Works

1. The dataset containing **movie ratings and movie titles** is loaded.
2. A **user–movie rating matrix** is created from the ratings.
3. A **K-Nearest Neighbors (KNN)** model with cosine similarity is trained.
4. When a user selects a movie, the model finds **movies with similar rating patterns**.
5. The top similar movies are displayed as recommendations.

This method is called **Item-Based Collaborative Filtering**.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* HTML / CSS
* Matplotlib & Seaborn (for EDA)

## Project Structure

```text
ml_model_movie_ratings_system
│
├── notebooks/eda.ipynb
├── templates/index.html
├── static/style.css
├── ratings.csv
├── movies.csv
├── train_model.py
├── app.py
└── requirements.txt
```

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Train the model:

```
python train_model.py
```

Run the Flask app:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

Select a movie from the dropdown list to get recommended movies.

## Conclusion

This project demonstrates how **machine learning and collaborative filtering** can be used to build a simple movie recommendation system and deploy it as a **web application using Flask**.
