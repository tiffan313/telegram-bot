import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

API_BASE = "https://api.alquran.cloud/v1"

# گرفتن لیست سوره‌ها
def get_surah_list():
    res = requests.get(f"{API_BASE}/surah")
    data = res.json()
    return data["data"]

# گرفتن آیه
def get_ayah(surah, ayah):
    res = requests.get(f"{API_BASE}/ayah/{surah}:{ayah}/editions/quran-uthmani,en.asad")
    data = res.json()["data"]
    arabic = data[0]["text"]
    translation = data[1]["text"]
    return arabic, translation


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
        "به ربات لایقه خوش اومدی 👋\nیکی رو انتخاب کن:",
        reply_markup=main_keyboard()
    )


# مرحله قرآن
@dp.message(lambda m: m.text == "📖 قرآن")
async def quran_menu(message: types.Message):
    surahs = get_surah_list()

    text = "📖 لیست سوره‌ها:\n\n"
    for s in surahs[:20]:  # فعلاً 20 تا اول برای سبک بودن
        text += f"{s['number']}. {s['name']} ({s['englishName']})\n"

    text += "\n✍️ برای دریافت آیه بنویس:\n/surah شماره سوره شماره آیه\nمثال:\n/surah 1 1"

    await message.answer(text)


# دستور دریافت آیه
@dp.message(lambda m: m.text and m.text.startswith("/surah"))
async def surah_handler(message: types.Message):
    try:
        _, surah, ayah = message.text.split()
        arabic, translation = get_ayah(surah, ayah)

        await message.answer(
            f"📖 قرآن\n\n"
            f"{arabic}\n\n"
            f"🇮🇷 ترجمه:\n{translation}"
        )
    except:
        await message.answer("فرمت اشتباهه!\nمثال: /surah 1 1")


@dp.message()
async def fallback(message: types.Message):
    await message.answer("از دکمه‌ها استفاده کن 👇", reply_markup=main_keyboard())


async def main():
    print("Lahegh bot running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
