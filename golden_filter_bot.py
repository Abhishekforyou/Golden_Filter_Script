import os
import requests
from datetime import datetime
import pytz
import threading
import time

# Get credentials from environment variables
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
    # Placeholder for your Golden Filter Pro logic
    return "✅ Golden Filter Scan Complete: No trade-worthy stock at the moment."

def run_bot():
    while True:
        ist = pytz.timezone("Asia/Kolkata")
        now = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
        message = f"<b>Golden Filter Pro Alert</b>\nTime: {now}\n"
        message += check_market_conditions()
        send_telegram_alert(message)

        time.sleep(600)  # Wait 10 minutes before next alert

if __name__ == "__main__":
    # Start bot in a separate thread
    threading.Thread(target=run_bot).start()

    # Keep the web service alive for Render
    while True:
        time.sleep(60)
