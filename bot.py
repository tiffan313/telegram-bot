import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# کیبورد اصلی
def main_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📖 قرآن")],
            [types.KeyboardButton(text="📜 احادیث")],
            [types.KeyboardButton(text="🔎 جستجو")]
        ],
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "سلام 👋\nبه ربات *لایقه* خوش اومدی.\nیکی از بخش‌ها رو انتخاب کن:",
        reply_markup=main_keyboard(),
        parse_mode="Markdown"
    )

@dp.message()
async def handler(message: types.Message):
    text = message.text

    # قرآن
    if text == "📖 قرآن":
        await message.answer(
            "📖 بخش قرآن\n\nفعلاً در حال توسعه هست...\nبه زودی می‌تونی:\n- انتخاب سوره\n- انتخاب آیه\n- ترجمه و تفسیر"
        )

    # احادیث
    elif text == "📜 احادیث":
        await message.answer(
            "📜 بخش احادیث\n\nفعلاً در حال توسعه هست...\nبه زودی:\n- احادیث موضوعی\n- سرچ حدیث\n- متن عربی + ترجمه + شرح"
        )

    # جستجو
    elif text == "🔎 جستجو":
        await message.answer(
            "🔎 جستجو\n\nفعلاً آماده نیست...\nبه زودی می‌تونی هر آیه یا حدیثی رو سرچ کنی"
        )

    else:
        await message.answer("از دکمه‌ها استفاده کن 👇", reply_markup=main_keyboard())


async def main():
    print("Lahegh bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
