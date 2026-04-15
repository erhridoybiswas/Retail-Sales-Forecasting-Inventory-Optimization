import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=200)

    data = []

    for store in range(1, 4):
        for item in range(1, 6):
            base = np.random.randint(20, 50)

            for i, date in enumerate(dates):
                demand = base + 5*np.sin(i/7) + np.random.randint(-5, 5)
                demand = max(1, int(demand))

                data.append({
                    "date": date,
                    "store_id": f"S{store}",
                    "item_id": f"I{item}",
                    "qty_sold": demand,
                    "price": np.random.randint(10, 50),
                    "stock_on_hand": np.random.randint(20, 100),
                    "lead_time_days": np.random.randint(2, 7),
                    "ordering_cost": 100,
                    "unit_cost": 20,
                    "holding_rate": 0.2
                })

    df = pd.DataFrame(data)
    df.to_csv("data/raw/data.csv", index=False)

if __name__ == "__main__":
    generate_data()