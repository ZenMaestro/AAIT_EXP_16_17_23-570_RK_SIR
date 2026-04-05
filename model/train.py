import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_model():
    # Go up one level from 'model' to find 'data'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "data.csv")
    model_path = os.path.join(base_dir, "model", "model.pkl")

    print(f"Loading data from {data_path}")
    data = pd.read_csv(data_path)

    X = data[['study_hours', 'attendance', 'sleep']]
    y = data['marks']

    model = LinearRegression()
    model.fit(X, y)

    # Save model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
