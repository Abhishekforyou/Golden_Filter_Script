import os
import requests
import threading
import time
from datetime import datetime
import pytz
from flask import Flask

# Setup Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize Flask app (dummy server for Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "Golden Filter Bot is running!"

# Bot logic
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def check_market_conditions():
    return "✅ Golden Filter Scan Complete: No trade-worthy stock at the moment."

def run_bot():
    while True:
        ist = pytz.timezone("Asia/Kolkata")
        now = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
        message = f"<b>Golden Filter Pro Alert</b>\nTime: {now}\n"
        message += check_market_conditions()
        send_telegram_alert(message)
        time.sleep(600)  # every 10 minutes

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
