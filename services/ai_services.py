from pathlib import Path
import joblib

from utils.preprocessing import clean_text


# Get the backend project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ML model paths
MODEL_PATH = BASE_DIR / "trained_models" / "category_model.pkl"
VECTORIZER_PATH = BASE_DIR / "trained_models" / "vectorizer.pkl"


# Load trained model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_category(complaint: str):

    cleaned = clean_text(complaint)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    return prediction[0]