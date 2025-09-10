 Tweet Sentiment Analysis

A simple and stylish machine learning web app built using Streamlit to classify the sentiment of tweets as Positive, Negative, or Neutral.


## 🚀 Live Demo
[Click here to try the app](https://siddappag-tweet-sentiment-analysis-app-cvje01.streamlit.app/)




 🌟 Features

- 🔍 Single tweet sentiment prediction
- 🌈 Beautiful dark-mode UI with gradient title and sentiment boxes
- 🧠 Trained machine learning model with TF-IDF vectorization
- 🧽 Preprocessing and cleaning of tweet text


---

## 🚀 How It Works

1. Clean the tweet using text preprocessing (stopwords removal, lowercasing, etc.)
2. Transform the cleaned tweet using a trained "TF-IDF Vectorizer"
3. Predict sentiment using a trained "Logistic regression" ML model 
4. Display the result with a color-coded box in the UI

---

## 🛠️ Techn Stack

- 🐍 Python
- 🎈 Streamlit
- 🤖 Scikit-learn
- 📦 Joblib
- 🧹 NLTK for text preprocessing

---

 📦 Installation

 1. Clone the repository

```bash
git clone https://github.com/Siddappag/tweet-sentiment-analysis.git
cd tweet-sentiment-analysis

Create a virtual environment (optional but recommended)

python -m venv venv

venv\Scripts\activate   # On Windows

3. Install dependencies

bash
pip install -r requirements.txt

4. Download NLTK stopwords (first time only)

python
import nltk
nltk.download('stopwords')

🧪 Running the App
bash
streamlit run app.py


Open your browser and go to http://localhost:8510


// Project Structure



├── app.py                     # Main Streamlit app
├── sentiment_model.pkl        # Trained ML model
├── vectorizer.pkl             # TF-IDF vectorizer
├── tweet_cleaner.py           # Preprocessing logic
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview


## 📸 App UI

![App Screenshot](c:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot 2025-06-29 004328.png)
