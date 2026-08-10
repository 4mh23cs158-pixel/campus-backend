import random
import pandas as pd

# -----------------------------
# Complaint Categories
# -----------------------------

categories = {

    "Electrical": [
        "Fan not working",
        "Tube light fused",
        "Switch board damaged",
        "Power outage",
        "AC not working",
        "Projector not turning on"
    ],

    "Water": [
        "Water leakage",
        "No drinking water",
        "Tap broken",
        "Water overflowing",
        "Water pipeline damaged"
    ],

    "Internet": [
        "WiFi not working",
        "Internet is slow",
        "Network disconnected",
        "LAN cable damaged",
        "Router not working"
    ],

    "Furniture": [
        "Broken chair",
        "Broken desk",
        "Window damaged",
        "Door lock broken",
        "Bench damaged"
    ],

    "Cleaning": [
        "Garbage not collected",
        "Dirty classroom",
        "Washroom dirty",
        "Dust everywhere",
        "Bad smell in corridor"
    ],

    "Security": [
        "Unauthorized person entered",
        "CCTV not working",
        "Gate left open",
        "Security guard absent"
    ]

}

# -----------------------------
# Departments
# -----------------------------

department_map = {

    "Electrical":"Electrical",

    "Water":"Civil",

    "Internet":"IT",

    "Furniture":"Maintenance",

    "Cleaning":"Housekeeping",

    "Security":"Security"
}

# -----------------------------
# Priority
# -----------------------------




# -----------------------------
# Locations
# -----------------------------

locations = [

    "Block A",

    "Block B",

    "Block C",

    "Library",

    "Hostel",

    "Canteen",

    "Lab 1",

    "Lab 2",

    "Seminar Hall",

    "Parking Area"
]

# -----------------------------
# Dataset
# -----------------------------

rows = []

for i in range(1000):

    category = random.choice(list(categories.keys()))

    complaint = random.choice(categories[category])

    location = random.choice(locations)

    full_complaint = f"{complaint} in {location}"

    # -----------------------------
    # Dynamic Priority
    # -----------------------------
    if category == "Electrical":
        priority = random.choice(["Medium", "High", "Critical"])

    elif category == "Water":
        priority = random.choice(["Medium", "High"])

    elif category == "Internet":
        priority = random.choice(["Low", "Medium"])

    elif category == "Furniture":
        priority = random.choice(["Low", "Medium"])

    elif category == "Cleaning":
        priority = "Low"

    elif category == "Security":
        priority = random.choice(["High", "Critical"])

    rows.append({

        "complaint": full_complaint,

        "category": category,

        "priority": priority,

        "department": department_map[category]

    })
# -----------------------------
# Save Dataset
# -----------------------------

df = pd.DataFrame(rows)

df.to_csv(
    "datasets/complaints_dataset.csv",
    index=False
)

print("Dataset Generated Successfully")
print(df.head())