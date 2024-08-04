from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('movie_recommendation_model.pkl')

# Load movie data
movies_data = pd.read_csv('movies.csv')

@app.route('/')
def home():
    return "Welcome to the Movie Recommendation API!"

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie')
    if not movie_name:
        return jsonify({'error': 'No movie name provided'}), 400

    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return jsonify({'error': 'No close match found for the movie'}), 404

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(model[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for movie in sorted_similar_movies[:10]:  # Top 10 recommendations
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        recommended_movies.append(title_from_index)

    return jsonify({'recommendations': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)
