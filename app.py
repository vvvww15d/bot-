from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import os

# Инициализация
server = Flask(__name__)
TOKEN = os.environ.get("7982666292:AAGPSuo53vZMr2gnovIwIktxQcN1SJvIAdU")
PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = f"https://bot-z32z.onrender.com"  # ЗАМЕНИТЕ на ваш реальный URL

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("15Deploy", web_app={"url": "https://ggg123fffi.github.io/"})]]
    await update.message.reply_text("Приветствуем! Нажмите кнопку 👇", 
                                 reply_markup=InlineKeyboardMarkup(keyboard))

@server.route('/')
def home():
    return "Bot is running!"

@server.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), app.bot)
    app.update_queue.put(update)
    return 'ok'

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Установка webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        secret_token='WEBHOOK_SECRET'
    )
