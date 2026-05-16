# 🛡️ AI News Authenticator (Fake News Detection)

A full-stack machine learning project that detects fake news articles. It features a Jupyter notebook–driven training pipeline, a Flask API for real-time inference, and an interactive web frontend.

## Project Overview

This project provides a lightweight, modular ML pipeline that:

- Preprocesses and cleans a merged dataset of fake and real news
- Extracts TF-IDF features using unigrams and bigrams
- Trains and compares Logistic Regression, Naïve Bayes, SVM, and Random Forest models
- Exposes a Flask backend endpoint to serve the best-performing model
- Provides a clean, responsive HTML/CSS/JavaScript frontend for instant predictions

## ✨ Features

- **Notebook-driven ML**: EDA, text preprocessing, modeling, and evaluation in organized Jupyter notebooks
- **NLP Techniques**: Custom text cleaning, stopword removal, lemmatization, and TF-IDF vectorization
- **API Backend**: Single-endpoint Flask service (`/api/predict`) handling POST requests for real vs. fake inference
- **Interactive UI**: A modern glassmorphism web interface with animated confidence bars

## 📊 Datasets

This project uses the **Fake and Real News Dataset** from Kaggle.

You will need to download the raw CSV files to run the training notebooks from scratch:

- [Download Fake.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=Fake.csv)
- [Download True.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=True.csv)

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/vishalpatel2023/Fake-News-Detection.git
cd Fake-News-Detection
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 💻 How to Use

### Phase 1: Data Preparation & Model Training (Optional)

If you only want to run the app, you can skip this step as long as the `.pkl` files are already present in the `models/` folder.

1. Download the datasets from the Kaggle links above.
2. Place the raw files in `data/raw/` as `Fake.csv` and `True.csv`.
3. Open Jupyter Notebook and run `01_Preprocessing.ipynb` to clean the text and generate processed datasets.
4. Run `02_Modeling.ipynb` to train the models and export `best_model.pkl` and `tfidf_vectorizer.pkl` to the `models/` folder.

### Phase 2: Running the Application

To use the interactive web app, start the backend server and open the frontend.

#### 1. Start the Flask Backend

```bash
cd backend
python app.py
```

The server will start at `http://127.0.0.1:5000`.

#### 2. Open the Frontend UI

Keep the terminal running, then open the `frontend/` folder and launch `index.html` in your browser, or use a Live Server extension.

Paste an article, click **Analyze**, and view the prediction result.

## 📁 Folder Structure

```text
Fake-News-Detection/
│
├── backend/                 # Backend Flask API
│   └── app.py               # Main API application
│
├── data/                    # Data storage
│   ├── processed/           # Cleaned CSVs, TF-IDF features, and labels
│   └── raw/                 # Raw Kaggle datasets (Fake.csv, True.csv)
│
├── frontend/                # Web user interface
│   ├── index.html           # Main application page
│   ├── script.js            # API connection and UI logic
│   └── style.css            # Styling and animations
│
├── models/                  # Saved machine learning components
│   ├── best_model.pkl       # Trained classifier
│   └── tfidf_vectorizer.pkl # Fitted vectorizer
│
├── notebooks/               # Development and research notebooks
│   ├── 01_Preprocessing.ipynb
│   └── 02_Modeling.ipynb
│
├── reports/                 # Evaluation metrics and text outputs
│   └── accuracy_report.txt
│
├── .gitignore               # Git housekeeping
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## 👥 Contributors

This project was developed collaboratively by the following team members:

- **Vishal Patel** (Reg. No. 20233314) — Team Leader
- **Virajsingh Mohansingh Rajput** (Reg. No. 20233360)
- **Vilhekar Sojwal Awdhut** (Reg. No. 20233359)
- **Shib Chandan Mistry** (Reg. No. 20233263)
- **Varun Kumar** (Reg. No. 20233581)

🙏 Special thanks to each team member for their valuable contribution in successfully completing this project.
