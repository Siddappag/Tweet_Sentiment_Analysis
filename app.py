import streamlit as st
import joblib
from tweet_cleaner import clean_tweet

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Page config
st.set_page_config(page_title="Tweet Sentiment Analysis", page_icon="📊", layout="centered")

# Custom CSS styles
st.markdown("""
    <style>
    .main {
        background-color: #0f1117;
        color: #ffffff;
        padding: 2rem;
    }
    .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
        font-size: 16px;
        border: 1px solid #555;
    }
    .sentiment-box {
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        margin-top: 1.5rem;
        text-align: center;
    }
    .positive { background-color: #16a34a20; color: #16a34a; border: 1px solid #16a34a; }
    .negative { background-color: #dc262620; color: #dc2626; border: 1px solid #dc2626; }
    .neutral  { background-color: #facc1520; color: #facc15; border: 1px solid #facc15; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("""
    <h1 style='
        text-align: center;
        background: -webkit-linear-gradient(#00FFD1, #007CF0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
    '>🔍 Tweet Emotion Classifier</h1>
""", unsafe_allow_html=True)

st.write("Enter a tweet below and see if it's **Positive**, **Negative**, or **Neutral**.")

# Input
tweet = st.text_area(" Your Tweet:", height=150)

# Predict button
if st.button("Analyze"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet to analyze.")
    else:
        cleaned = clean_tweet(tweet)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]

        # Show result with colored box
        if prediction == "positive":
            st.markdown(f"<div class='sentiment-box positive'>✅ Positive Sentiment</div>", unsafe_allow_html=True)
        elif prediction == "negative":
            st.markdown(f"<div class='sentiment-box negative'>❌ Negative Sentiment</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='sentiment-box neutral'>😐 Neutral Sentiment</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style="margin-top:2rem;">
    <div style='text-align: center; color: gray; font-size: 13px;'>
        Built with ❤️ by Siddappa | Sentiment Analysis ML Project
    </div>
""", unsafe_allow_html=True)