import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from tweet_cleaner import clean_tweet

# Load dataset
df = pd.read_csv("data/tweets.csv")

df['cleaned'] = df['text'].apply(clean_tweet)
X = df['cleaned']
y = df['airline_sentiment']


# TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
X_vect = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
