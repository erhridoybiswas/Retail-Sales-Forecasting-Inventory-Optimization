import numpy as np
from scipy.stats import norm

def calculate_inventory(forecast, on_hand, lead_time):

    demand = forecast["forecast"].head(lead_time).sum()

    std = forecast["forecast"].std()

    z = norm.ppf(0.95)

    safety_stock = z * std * (lead_time ** 0.5)

    reorder_point = demand + safety_stock

    eoq = np.sqrt((2 * 10000 * 100) / (20 * 0.2))

    order_qty = max(0, reorder_point - on_hand)

    return {
        "safety_stock": round(safety_stock,2),
        "reorder_point": round(reorder_point,2),
        "eoq": round(eoq,2),
        "order_qty": round(order_qty,2)
    }