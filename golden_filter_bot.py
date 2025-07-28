
import os
import time
import logging
import schedule
import asyncio
from telegram import Bot
from nsetools import Nse
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.INFO)

# Environment Variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)
nse = Nse()

async def send_alert(msg):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=msg)
        logging.info(f"Sent alert: {msg}")
    except Exception as e:
        logging.error(f"Error sending alert: {e}")

async def fetch_and_alert():
    watchlist = ['TCS', 'INFY', 'HINDUNILVR']
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    await send_alert(f"🔔 Volume Check Triggered at {now}")

    for stock in watchlist:
        try:
            q = nse.get_quote(stock)
            ltp = float(q['lastPrice'])
            logging.info(f"{stock} - LTP: {ltp}")
        except Exception as e:
            logging.error(f"Error fetching data for {stock}: {e}")

async def main():
    await fetch_and_alert()

if __name__ == "__main__":
    asyncio.run(main())
