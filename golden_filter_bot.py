import os
import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.ok

def check_market_conditions():
    # Placeholder for Golden Filter logic
    return "✅ Golden Filter Scan Complete: No trade-worthy stock at the moment."

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"<b>Golden Filter Pro Alert</b> 📈
Time: {now}

"
    message += check_market_conditions()
    send_telegram_alert(message)
