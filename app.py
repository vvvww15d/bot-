from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("15Deploy", web_app={"url": "https://ggg123fffi.github.io/"})]]
    await update.message.reply_text("Приветствуем дорогой другй! Нажми на кнопку 👇", reply_markup=InlineKeyboardMarkup(keyboard))

app = Application.builder().token("7982666292:AAGPSuo53vZMr2gnovIwIktxQcN1SJvIAdU").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()