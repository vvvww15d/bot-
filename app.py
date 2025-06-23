from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
import os
from flask import Flask, request

# Инициализация
TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 10000))

flask_app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("15Deploy", web_app={"url": "https://ggg123fffi.github.io/"})]]
    await update.message.reply_text("✅ Бот активен! Нажмите кнопку 👇", 
                                 reply_markup=InlineKeyboardMarkup(keyboard))

@flask_app.route('/')
def home():
    return "Bot is running and ready!"

@flask_app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    bot_app.update_queue.put(update)
    return 'ok'

if __name__ == '__main__':
    bot_app.add_handler(CommandHandler("start", start))
    
    # Автоматическое определение URL на Render
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook"
    
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=webhook_url,
        secret_token='RENDER_WEBHOOK_SECRET'  # Можно изменить на свой
    )
