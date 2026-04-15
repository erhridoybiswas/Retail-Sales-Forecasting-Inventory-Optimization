import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from src.features import create_features

def train():
    df = pd.read_csv("data/processed/data.csv", parse_dates=["date"])

    df = create_features(df)

    X = df[["lag1", "lag7", "rolling_mean", "day"]]
    y = df["qty_sold"]

    model = RandomForestRegressor()
    model.fit(X, y)

    joblib.dump(model, "models/model.joblib")

if __name__ == "__main__":
    train()