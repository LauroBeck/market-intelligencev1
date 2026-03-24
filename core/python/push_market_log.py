import json
from datetime import datetime
import os

market_data = {
    "timestamp": "2026-03-24 15:51:00-0400",
    "indices": {
        "NASDAQ": {"price": 21759.22, "change_pct": -0.85},
        "S&P500": {"price": 6555.15, "change_pct": -0.39},
        "DOW": {"price": 46123.59, "change_pct": -0.18}
    },
    "macro": {
        "VIX": 26.90,
        "2YR_YIELD": 3.92,
        "GOLD_SPOT": 4399.49
    },
    "top_news": [
        "Citadel Securities nets record $12B haul in 2025",
        "Stocks bounce from lows on hopes for US-Iran talks",
        "Iran says non-hostile ships can cross Hormuz"
    ]
}

def log_to_repo():
    filename = f"logs/market_final_{datetime.now().strftime('%H%M')}.json"
    os.makedirs('logs', exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(market_data, f, indent=4)
    print(f"Final Bell Logged: {filename} | VIX: {market_data['macro']['VIX']}")

if __name__ == "__main__":
    log_to_repo()
