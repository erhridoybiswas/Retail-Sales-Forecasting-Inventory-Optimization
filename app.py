from flask import Flask, render_template, request
import pandas as pd

from src.forecast import forecast
from src.inventory import calculate_inventory

# ✅ CREATE APP FIRST
app = Flask(__name__)

# Load data
df = pd.read_csv("data/processed/data.csv", parse_dates=["date"])

# ---------------- HOME ----------------
@app.route("/")
def home():
    stores = df["store_id"].unique()
    return render_template("index.html", stores=stores)

# ---------------- GET ITEMS ----------------
@app.route("/items/<store>")
def items(store):
    items = df[df["store_id"] == store]["item_id"].unique().tolist()
    return {"items": items}

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    store = request.form["store"]
    item = request.form["item"]

    group = df[(df["store_id"] == store) & (df["item_id"] == item)]

    fc = forecast(group)

    last = group.iloc[-1]

    inv = calculate_inventory(fc, last["stock_on_hand"], last["lead_time_days"])

    # Chart data
    chart_dates = fc["date"].astype(str).tolist()
    chart_values = fc["forecast"].tolist()

    return render_template(
        "result.html",
        forecast=fc.to_dict("records"),
        inv=inv,
        chart_dates=chart_dates,
        chart_values=chart_values,
        store=store,
        item=item
    )

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)