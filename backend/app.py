from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from nltk.stem import WordNetLemmatizer
import joblib 
import os

# Initializing Flask app
app = Flask(__name__)
CORS(app)

# Download necessary NLTK resources quietly
nltk.download("wordnet", quiet=True)

# 1. LOADing oUR MODEL & VECTORIZER

# Dynamically find the models folder based on your directory structure

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # This is the /backend folder
MODELS_DIR = os.path.join(BASE_DIR, '..', 'models')   # This goes up one level to /models

# NOTE: Check your actual filenames in the models folder. 
# Based on your image, I am assuming they are named exactly this:
MODEL_PATH = os.path.join(MODELS_DIR, 'best_model.pkl')
VECTORIZER_PATH = os.path.join(MODELS_DIR, 'tfidf_vectorizer.pkl')

try:
    best_model = joblib.load(MODEL_PATH)
    tfidf_vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model and Vectorizer loaded successfully from the 'models' folder!")
except Exception as e:
    print(f"❌ Warning: Could not load model/vectorizer. Error: {e}")

# 2. NLP PREPROCESSING SETUP

stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', "he'd", "he'll", 'her', 'here', 'hers', 'herself', "he's", 'him', 'himself', 'his', 'how', 'i', "i'd", 'if', "i'll", "i'm", 'in', 'into', 'is', 'isn', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', "i've", 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'nor', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she'd", "she'll", "she's", 'should', 'shouldn', "shouldn't", "should've", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', "we'd", "we'll", "we're", 'were', 'weren', "weren't", "we've", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've"]

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

def preprocess_input(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text


# 3. API ENDPOINTS

@app.route('/api/predict', methods=['POST'])
def predict_news():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided. Please send JSON with a "text" key.'}), 400
        
    raw_text = data['text']
    
    try:
        processed_text = preprocess_input(raw_text)
        
        input_tfidf = tfidf_vectorizer.transform([processed_text])
        predicted_prob = best_model.predict_proba(input_tfidf)
        
        fake_probability = float(predicted_prob[0][1])
        real_probability = float(predicted_prob[0][0])
        prediction_label = "FAKE" if fake_probability > 0.5 else "REAL"
        
        return jsonify({
            'status': 'success',
            'prediction': prediction_label,
            'confidence': {
                'real_probability': real_probability,
                'fake_probability': fake_probability
            },
            'processed_text': processed_text
        }), 200
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Fake News Detection API is running!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)