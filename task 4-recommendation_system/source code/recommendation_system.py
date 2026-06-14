#Movie Recommendation System
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    'Movie': [
        'Avengers',
        'Iron Man',
        'Captain America',
        'Thor',
        'Batman',
        'Superman'
    ],

    'Genre': [
        'action superhero marvel',
        'action superhero marvel',
        'action superhero marvel',
        'action superhero marvel',
        'action dc hero',
        'action dc hero'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text data into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(df['Genre'])

# Calculate similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie_name):

    movie_index = df[df['Movie'] == movie_name].index[0]

    scores = list(enumerate(similarity[movie_index]))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended movies for {movie_name}:\n")

    for movie in sorted_scores[1:4]:
        print(df.iloc[movie[0]].Movie)

# User input
movie = input("Enter movie name: ")

recommend(movie)