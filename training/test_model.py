import joblib

from utils.preprocessing import clean_text

model = joblib.load(
    "trained_models/category_model.pkl"
)

vectorizer = joblib.load(
    "trained_models/vectorizer.pkl"
)

while True:

    complaint = input("Complaint : ")

    complaint = clean_text(complaint)

    vector = vectorizer.transform([complaint])

    prediction = model.predict(vector)

    print()

    print("Predicted Category :", prediction[0])

    print()