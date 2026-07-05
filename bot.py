from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = ReplyKeyboardMarkup(
    [
        ["قرآن 📖", "حدیث 📚"],
        ["جستجو 🔍"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋 یکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=keyboard
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("در حال توسعه 👷‍♂️")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Bot is running...")
    app.run_polling()
