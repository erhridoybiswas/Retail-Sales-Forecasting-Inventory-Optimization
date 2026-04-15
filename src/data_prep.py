import pandas as pd

def prepare():
    df = pd.read_csv("data/raw/data.csv", parse_dates=["date"])

    df = df.drop_duplicates()
    df = df.fillna(0)
    df = df.sort_values(["store_id", "item_id", "date"])

    df.to_csv("data/processed/data.csv", index=False)

if __name__ == "__main__":
    prepare()