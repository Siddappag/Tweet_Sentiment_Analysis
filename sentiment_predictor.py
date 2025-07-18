import joblib
from tweet_cleaner import clean_tweet

# Load model & vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(text):
    cleaned = clean_tweet(text)
    vect = vectorizer.transform([cleaned])
    prediction = model.predict(vect)
    return prediction[0]

# Example usage
if __name__ == "__main__":
    tweet = input("Enter a tweet: ")
    sentiment = predict_sentiment(tweet)
    print("Sentiment:", sentiment)
