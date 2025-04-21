# Fake News Detection

A Jupyter‑notebook–driven pipeline to detect fake news articles using classic ML models — and a simple Flask API for inference.

## Project Overview

Fake-News-Detection is a lightweight ML pipeline built in Jupyter notebooks that:

- Preprocesses and cleans a merged dataset of fake & real news.
- Extracts TF‑IDF features (unigrams & bigrams).
- Trains and compares Logistic Regression, Naïve Bayes, SVM & Random Forest.
- Exposes a simple Flask endpoint for real‑time predictions.

## Features

- **Notebook‑driven**: EDA, preprocessing, modeling & evaluation in 2 notebooks.  
- **Modular ML**: TF‑IDF vectorizer + common classifiers.  
- **Visualization**: Word clouds, bar charts of top TF‑IDF terms, model comparison.  
- **API**: Single‑endpoint Flask service for “real” vs. “fake” inference.

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/vishalpatel2023/Fake-News-Detection.git
cd Fake-News-Detection
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate.bat     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Data Preparation

Place raw files in `data/raw/` as `fake.csv` & `true.csv`.

Run `02_Preprocess.ipynb` to generate `data/processed/preprocessed_news.csv`.

### Running Notebooks

Open Jupyter:

```bash
jupyter notebook
```

Then execute:
- `02_Preprocess.ipynb`
- `03_Modeling.ipynb`

### Running the Flask API

```bash
cd backend
export FLASK_APP=app.py    # or set in .env
flask run
```

## Folder Structure

```
Fake-News-Detection/
│
├── data/                # Processed datasets
├── frontend/            # Web frontend
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   └── templates/
│       └── index.html
├── backend/             # Backend code (Flask APIs)
├── models/              # Trained model files like model.pkl, vectorizer.pkl
├── notebooks/           # Main development work
│   ├── 02_Preprocess.ipynb
│   └── 03_Modeling.ipynb
├── reports/             # Any visualizations, evaluation metrics
├── requirements.txt     # List of Python dependencies
├── README.md            # Project summary and instructions
└── .gitignore           # Git housekeeping
```

## 👥 Contributors

This project was developed collaboratively by the following team members:

- **Vishal Patel** (Reg. No. 20233314) – *Team Leader*  
- **Virajsingh Mohansingh Rajput** (Reg. No. 20233360)  
- **Vilhekar Sojwal Awdhut** (Reg. No. 20233359)  
- **Shib Chandan Mistry** (Reg. No. 20233263)  
- **Varun Kumar** (Reg. No. 20233581)  

**🙏 Special thanks to each team member for their valuable contribution in successfully completing this project.**
