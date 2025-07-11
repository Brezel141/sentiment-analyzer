from flask import Flask, render_template, request
import joblib
from scripts.preprocessing import clean_text

app = Flask(__name__)

# Load model and vectorizer once
model = joblib.load("models/logreg_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        review = request.form["review"]
        cleaned = clean_text(review)
        vector = tfidf.transform([cleaned])
        pred = model.predict(vector)[0]
        prediction = "Positive 😊" if pred == 1 else "Negative 😠"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
