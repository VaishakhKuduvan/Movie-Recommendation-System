import joblib
import os

# Change directory to where your model file is
os.chdir('C:\\Users\\imbat\\movie reccomendation system')

# Check if the model file exists
if not os.path.isfile('movie_recommendation_model.pkl'):
    print("Model file not found!")
else:
    # Load the model
    try:
        model = joblib.load('movie_recommendation_model.pkl')
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
