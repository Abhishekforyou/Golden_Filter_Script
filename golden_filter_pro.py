import pandas as pd
from golden_utils import run_golden_filter
from telegram_notifier import send_telegram_alert

if __name__ == "__main__":
    results = run_golden_filter("nifty200_list.csv")
    for stock, data in results.items():
        message = f"📊 {stock}\nConfidence: {data['confidence']}%\nEntry Range: {data['entry']}\nTarget: {data['target']}\nSL: {data['stop_loss']}"
        send_telegram_alert(message)
