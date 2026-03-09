Movie Recommendation System 🎬

This project is a Machine Learning based Movie Recommendation Web Application built using Python, Flask, and HTML/CSS.
It uses the MovieLens 100K Dataset to recommend movies based on user rating patterns.

The system applies collaborative filtering with the K-Nearest Neighbors algorithm to find movies that are similar to the selected movie.

📌 Project Overview

Online platforms like Netflix, Amazon Prime, and YouTube recommend content to users based on their preferences.
This project demonstrates a basic recommendation system that suggests similar movies using historical user ratings.

The web application allows users to:

Select a movie from a dropdown list

Get recommendations for similar movies

View results instantly through a Flask web interface

📂 Dataset

The project uses the MovieLens 100K Dataset which contains:

ratings.csv – user ratings for movies

movies.csv – movie titles and genres

These datasets help the model understand how users rate different movies and identify patterns.

⚙️ Technologies Used

Python

Flask

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

HTML & CSS

🧠 Machine Learning Approach

The recommendation system follows these steps:

Load movie ratings dataset.

Merge movie titles with rating data.

Convert the data into a user-movie matrix.

Train a K-Nearest Neighbors (KNN) model using cosine similarity.

When a user selects a movie, the system finds nearest movies with similar rating patterns.

The top recommended movies are returned and displayed on the web page.

This approach is known as Item-Based Collaborative Filtering.

📊 Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand the dataset:

Distribution of movie ratings

Most popular movies (highest number of ratings)

Top rated movies

User rating activity

These visualizations help understand patterns in the dataset before building the model.

🖥️ Web Application

The recommendation model is integrated into a Flask web application.

Features of the interface:

Simple and clean user interface

Dropdown list to choose a movie

Displays recommended movies

Basic visualization of recommendation results

The Flask backend loads the trained model and returns recommendations dynamically.

📁 Project Structure
ml_model_movie_ratings_system
│
├── notebooks
│   └── eda.ipynb
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── ratings.csv
├── movies.csv
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Train the recommendation model
python train_model.py
3️⃣ Run the Flask application
python app.py
4️⃣ Open the application
http://127.0.0.1:5000

Select a movie from the list to see recommended movies.

📈 Example

If the user selects a movie like Toy Story, the system may recommend movies such as:

Toy Story 2

A Bug's Life

Monsters Inc

Finding Nemo

Shrek

These recommendations are based on similar user rating patterns.
