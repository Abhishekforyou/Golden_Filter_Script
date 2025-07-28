import os
import requests
from datetime import datetime
import pytz
import time
import telegram

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def get_ist_time():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

def check_market_conditions():
    # Placeholder for Golden Filter logic
    return "✅ Golden Filter Scan Complete: No trade-worthy stock at the moment."

def send_telegram_alert():
    now = get_ist_time()
    message = f"<b>Golden Filter Pro Alert</b>\n🕒 Time: {now}\n\n"
    message += check_market_conditions()
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")

if __name__ == "__main__":
    print("Starting Golden Filter Bot...")
    send_telegram_alert()
    print("Message sent!")
