# =====================================
# SPRINT 3 - MODEL BUILDING
# Medical Cost Prediction
# =====================================

# Step 1 - Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
import joblib


# =====================================
# Step 2 - Load Dataset
# =====================================
df = pd.read_csv("insurance_final_dataset.csv")

print("Dataset Loaded Successfully\n")


# =====================================
# Step 3 - Identify Input & Target
# =====================================
X = df.drop("charges", axis=1)
y = df["charges"]

print("Input Features:", list(X.columns))
print("Target Variable: charges")
print("ML Task: Regression")
print("Evaluation Metric: Mean Absolute Error (MAE)\n")


# =====================================
# Step 4 - Train Test Split (75:25)
# =====================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("Train-Test Split Completed\n")


# =====================================
# Step 5 - Data Preparation
# =====================================

# Numerical and Categorical columns
num_cols = ["age", "bmi", "children"]
cat_cols = ["sex", "smoker", "region"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(drop="first"), cat_cols)
    ]
)

print("Data Preprocessing Setup Done\n")


# =====================================
# Step 6 - Define Models (4 Models)
# =====================================

models = {
    "Linear Regression": LinearRegression(),
    "KNN": KNeighborsRegressor(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = {}

print("Training Models...\n")


# =====================================
# Step 7 - Train & Evaluate
# =====================================

for name, model in models.items():

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)

    results[name] = mae

    print(f"{name} MAE: {mae:.2f}")


# =====================================
# Step 8 - Model Comparison Plot
# =====================================

plt.figure(figsize=(8,5))
plt.bar(results.keys(), results.values())
plt.xticks(rotation=30)
plt.ylabel("Mean Absolute Error")
plt.title("Model Comparison (Lower MAE is Better)")
plt.tight_layout()
plt.show()


# =====================================
# Step 9 - Best Model Selection
# =====================================

best_model_name = min(results, key=results.get)

print("\nBest Model:", best_model_name)
print("Best MAE:", results[best_model_name])


# =====================================
# Step 10 - Save Best Model
# =====================================

best_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", models[best_model_name])
])

best_pipeline.fit(X_train, y_train)

joblib.dump(best_pipeline, "best_model.pkl")

print("\nBest model saved as best_model.pkl")
