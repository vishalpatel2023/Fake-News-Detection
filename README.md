# Fake News Detection

This project detects fake news using machine learning.

## Features
- Uses `scikit-learn` for text classification
- `Flask` web API for prediction
- NLP preprocessing with `nltk`
- Data visualization with `matplotlib` and `seaborn`

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Fake-News-Detection.git

2. Navigate to the project directory:
    cd Fake-News-Detection

3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate  # Windows

4. Install dependencies:
    pip install -r requirements.txt

Usage
To run the app:
    python app.py


## Folder Structure:

Fake-News-Detection/ │── data/ # 📂 Store raw & processed datasets │ ├── raw/ # Original datasets (CSV, JSON, etc.) │ ├── processed/ # Preprocessed datasets (cleaned data) │ ├── train.csv # Training data (if applicable) │ ├── test.csv # Test data (if applicable) │ │── notebooks/ # 📂 Jupyter Notebooks │ ├── 01_EDA.ipynb # Exploratory Data Analysis (EDA) │ ├── 02_Preprocessing.ipynb # Data Cleaning & Processing │ ├── 03_Modeling.ipynb # Model Training & Evaluation │ ├── 04_Deployment.ipynb # Deployment Code │ │── src/ # 📂 Source Code (Python scripts) │ ├── preprocess.py # Text cleaning & preprocessing │ ├── train_model.py # ML model training script │ ├── predict.py # Model inference script │ ├── config.py # Configuration settings (e.g., paths, parameters) │ │── models/ # 📂 Saved models & checkpoints │ ├── model.pkl # Trained ML model │ ├── vectorizer.pkl # Saved TF-IDF/Word2Vec model │ │── reports/ # 📂 Reports & results │ ├── accuracy_report.txt # Model performance report │ ├── visualizations/ # Plots, graphs, confusion matrix │ │── logs/ # 📂 Logs for debugging │ ├── training.log # Logs for training process │ │── app/ # 📂 Web App for deployment (Optional) │ ├── static/ # CSS, JS files (for frontend) │ ├── templates/ # HTML files │ ├── app.py # Flask/Streamlit backend script │ │── requirements.txt # Dependencies for the project │── README.md # Project Documentation │── .gitignore # Ignore unnecessary files in Git