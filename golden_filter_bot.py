import os
import logging
import schedule
import time
import datetime
from telegram import Bot, InputFile
from telegram.error import TelegramError
from PIL import Image

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Bot token and chat ID
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

# Image validation using Pillow
def is_valid_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception as e:
        logger.warning(f"Image validation failed: {e}")
        return False

# Core sending logic
def send_golden_filter_update():
    try:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        message = f"📈 Golden Filter Pro — Daily Stock Alert ({today})\n\n✅ Market is open. Here are your top picks for today."
        bot.send_message(chat_id=CHAT_ID, text=message)

        chart_path = "chart.jpg"  # Or your actual chart filename

        if os.path.exists(chart_path) and is_valid_image(chart_path):
            with open(chart_path, 'rb') as image:
                bot.send_photo(chat_id=CHAT_ID, photo=InputFile(image))
        else:
            logger.warning("Chart image missing or invalid format.")

    except TelegramError as e:
        logger.error(f"Telegram error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

# Schedule task (e.g., 9:00 AM IST)
schedule.every().day.at("09:00").do(send_golden_filter_update)

# Start scheduler
if __name__ == "__main__":
    logger.info("Golden Filter Bot started.")
    send_golden_filter_update()  # Optional: trigger immediately on startup
    while True:
        schedule.run_pending()
        time.sleep(30)
