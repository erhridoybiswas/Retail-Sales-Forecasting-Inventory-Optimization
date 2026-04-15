import pandas as pd
import joblib

model = joblib.load("models/model.joblib")

def forecast(group):
    group = group.sort_values("date").copy()

    last = group.iloc[-7:].copy()

    preds = []

    for i in range(7):
        lag1 = last["qty_sold"].iloc[-1]
        lag7 = last["qty_sold"].iloc[-7]
        rolling = last["qty_sold"].mean()

        X = [[lag1, lag7, rolling, last.iloc[-1]["date"].dayofweek]]

        pred = model.predict(X)[0]
        pred = max(0, int(pred))

        new_row = last.iloc[-1].copy()
        new_row["qty_sold"] = pred
        new_row["date"] = new_row["date"] + pd.Timedelta(days=1)

        last = pd.concat([last, pd.DataFrame([new_row])])

        preds.append({"date": new_row["date"], "forecast": pred})

    return pd.DataFrame(preds)