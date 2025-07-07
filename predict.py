import joblib
from scripts.preprocessing import clean_text

# Load model and vectorizer
model = joblib.load("models/logreg_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Input sentence from user
text = input("Enter a review to analyze: ")

# Clean, transform, predict
cleaned = clean_text(text)
vector = tfidf.transform([cleaned])
prediction = model.predict(vector)[0]

# Output result
label = "positive" if prediction == 1 else "negative"
print(f"Predicted sentiment: {label}")
