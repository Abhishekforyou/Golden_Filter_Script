import os
import time
import logging
import schedule
from telegram import Bot
from nsetools import Nse
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)
nse = Nse()

def send_alert(msg):
    try:
        bot.send_message(chat_id=CHAT_ID, text=msg)
        logging.info(f"Sent alert: {msg}")
    except Exception as e:
        logging.error(f"Error sending alert: {e}")

def fetch_and_alert():
    watchlist = ['TCS', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'LAURUSLABS']
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    send_alert(f"🔔 Volume Check Triggered at {now}")

    for stock in watchlist:
        try:
            q = nse.get_quote(stock)
            ltp = float(q['lastPrice'])
            vol = int(q['quantityTraded'])
            avg_vol = int(q['averageQuantityTraded'])

            if vol > 1.5 * avg_vol:
                send_alert(f"📈 {stock} volume spike! Price: ₹{ltp}, Volume: {vol}")
        except Exception as e:
            logging.error(f"Error fetching {stock}: {e}")

schedule.every(10).minutes.do(fetch_and_alert)

if __name__ == "__main__":
    send_alert("🟢 Golden Filter Bot is now LIVE on Render!")
    while True:
        schedule.run_pending()
        time.sleep(1)
