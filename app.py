from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
import os

TOKEN = os.environ["BOT_TOKEN"]  # Токен из настроек Render

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("15Deploy", web_app={"url": "https://ggg123fffi.github.io/"})]]
    await update.message.reply_text("✅! Нажмите кнопку 👇", 
                                 reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Простой polling вместо webhook
    print("Бот запущен в режиме polling...")
    app.run_polling()
