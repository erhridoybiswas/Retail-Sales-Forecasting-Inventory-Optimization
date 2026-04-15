import pandas as pd

def create_features(df):
    df = df.copy()

    df["day"] = df["date"].dt.dayofweek

    df["lag1"] = df.groupby(["store_id","item_id"])["qty_sold"].shift(1)
    df["lag7"] = df.groupby(["store_id","item_id"])["qty_sold"].shift(7)

    df["rolling_mean"] = df.groupby(["store_id","item_id"])["qty_sold"].shift(1).rolling(7).mean()

    df = df.dropna()

    return df