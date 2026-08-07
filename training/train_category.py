import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from utils.preprocessing import clean_text

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("datasets/complaints_dataset.csv")

# -----------------------------
# Clean Text
# -----------------------------

df["clean_text"] = df["complaint"].apply(clean_text)

# -----------------------------
# Features
# -----------------------------

X = df["clean_text"]

y = df["category"]

# -----------------------------
# TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X_vector,

    y,

    test_size=0.2,

    random_state=42

)

# -----------------------------
# Model
# -----------------------------

model = LogisticRegression(max_iter=1000)

model.fit(

    X_train,

    y_train

)

# -----------------------------
# Accuracy
# -----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(

    y_test,

    predictions

)

print(f"Accuracy : {accuracy*100:.2f}%")

# -----------------------------
# Save Model
# -----------------------------

os.makedirs("trained_models", exist_ok=True)

joblib.dump(

    model,

    "trained_models/category_model.pkl"

)

joblib.dump(

    vectorizer,

    "trained_models/vectorizer.pkl"

)

print("Model Saved Successfully")