import joblib

from utils.preprocessing import clean_text

model = joblib.load(
    "trained_models/category_model.pkl"
)

vectorizer = joblib.load(
    "trained_models/vectorizer.pkl"
)


def predict_category(complaint: str):

    cleaned = clean_text(complaint)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    return prediction[0]