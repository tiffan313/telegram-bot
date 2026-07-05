import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

# کیبورد اصلی
keyboard = ReplyKeyboardMarkup(
    [
        ["📖 قرآن", "📜 احادیث"],
        ["🔍 جستجو"]
    ],
    resize_keyboard=True
)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nیکی از بخش‌ها رو انتخاب کن:",
        reply_markup=keyboard
    )

# هندل پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📖 قرآن":
        await update.message.reply_text(
            "📖 بخش قرآن\n\nفعلاً در نسخه اولیه هستیم.\nبه زودی امکان انتخاب سوره و آیه اضافه میشه."
        )

    elif text == "📜 احادیث":
        await update.message.reply_text(
            "📜 بخش احادیث\n\nفعلاً در نسخه اولیه هستیم.\nبه زودی احادیث موضوعی + عربی + ترجمه + شرح اضافه میشه."
        )

    elif text == "🔍 جستجو":
        await update.message.reply_text(
            "🔍 بخش جستجو\n\nبه زودی قابلیت سرچ آیه یا حدیث فعال میشه."
        )

    else:
        await update.message.reply_text("یکی از دکمه‌ها رو انتخاب کن 👇")

# ساخت اپ
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Lahegh bot is running...")
app.run_polling()
