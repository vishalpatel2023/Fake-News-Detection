# Fake-News-Detection/app/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle, re, nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

proxy = "http://edcguest:edcguest@172.31.102.14:3128"
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# Manually set proxy for nltk downloader
nltk.set_proxy(proxy)
# (Download or ensure nltk resources are available)
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english")) - {"not", "no"}
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    return text.strip()

def remove_stopwords(text):
    return " ".join([word for word in text.split() if word not in stop_words])

def lemmatize_text(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

def preprocess_text(text):
    text = text.lower()
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text

# # Load your model and vectorizer (adjust paths as needed)
# with open("../models/tfidf_vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)
# with open("../models/best_model.pkl", "rb") as f:
#     model = pickle.load(f)

# with open("../models/tfidf_vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)
# with open("../models/best_model.pkl", "rb") as f:
#     model = pickle.load(f)

with open("C:/Users/HP/OneDrive/Desktop/Fake-News-Detection/models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("C:/Users/HP/OneDrive/Desktop/Fake-News-Detection/models/model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from your React app

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    news_text = data.get("news", "")
    if not news_text:
        return jsonify({"error": "No news text provided"}), 400
    processed_text = preprocess_text(news_text)
    input_vector = vectorizer.transform([processed_text])
    prediction = model.predict(input_vector)[0]
    probabilities = model.predict_proba(input_vector)[0].tolist()
    return jsonify({
        "prediction": "FAKE" if prediction == 1 else "REAL",
        "probabilities": probabilities
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Flask is working!'

# if __name__ == '__main__':
#     try:
#         app.run(debug=True)
#     except Exception as e:
#         print(f"Error starting the Flask app: {e}")
