# updated code**********************
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")
CORS(app)

# Ensure necessary NLTK resources are available
nltk.download("stopwords")
nltk.download("wordnet")

# Load your TF-IDF vectorizer and the best model (make sure these files are correctly saved)
with open("../models/tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)

with open("../models/best_model.pkl", "rb") as f:
    best_model = pickle.load(f)

# Define your stopwords and lemmatizer exactly as used during training
stop_words = set(stopwords.words("english")) - {"not", "no"}
lemmatizer = WordNetLemmatizer()

# Pre-processing functions
def clean_text(text):
    text = re.sub(r'\d+', '', text)            # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)          # Remove punctuation
    text = re.sub(r'\s+', ' ', text)             # Remove extra spaces
    text = re.sub(r"\S+@\S+", "", text)           # Remove emails
    text = re.sub(r"http\S+|www\S+", "", text)    # Remove URLs
    return text.strip()

def remove_stopwords(text):
    return " ".join([word for word in text.split() if word not in stop_words])

def lemmatize_text(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

def preprocess_input(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # First, pre-process the text like you did during training
    preprocessed_text = preprocess_input(text)
    
    # Then, vectorize the preprocessed text
    vectorized = tfidf_vectorizer.transform([preprocessed_text])
    
    # Get the prediction from the model
    prediction = best_model.predict(vectorized)[0]
    label = "Fake News" if prediction == 1 else "Real News"
    
    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(debug=True)
