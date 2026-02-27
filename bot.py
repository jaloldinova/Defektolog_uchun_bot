import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties

API_TOKEN = "8724433109:AAFaX_cv8C3xYrcLnTIfHr4lcbmQfl1IQAw"

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📌 Konsultatsiya")],
            [KeyboardButton(text="🎓 Ustoz-shogird kursi")],
            [KeyboardButton(text="📚 Onlayn darsliklar")],
            [KeyboardButton(text="👤 O‘zim haqimda")]
        ],
        resize_keyboard=True
    )


@dp.message(Command("start"))
async def start_handler(message: Message):
    text = """
<b>Assalomu alaykum.</b>

Siz professional <b>Defektolog ABA terapevt Zikrilla Zohidjonovich platformasi</b>ga xush kelibsiz.

Bu yerda siz:
• Individual konsultatsiya  
• Mentorlik dasturi  
• Professional darsliklar  

xizmatlaridan foydalanishingiz mumkin.

Kerakli bo‘limni tanlang:
"""
    await message.answer(text, reply_markup=main_menu())

@dp.message(F.text == "📌 Konsultatsiya")
async def konsultatsiya_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Kursni sotib olish",
                    url="https://t.me/Zikrilla_zohidjonovich?text=Assalomu%20alaykum.%20Men%20KONSULTATSIYA%20xizmatini%20sotib%20olmoqchiman."
                )
            ]
        ]
    )
    text = """
<b>📌 Individual konsultatsiya</b>
Narxi: <b>150 000 so‘m</b>

✔ Muammoni aniqlash  
✔ Individual metodik reja  
✔ Professional tavsiyalar  
✔ Amaliy yo‘naltirish  
"""
    await message.answer(text, reply_markup=keyboard)


@dp.message(F.text == "🎓 Ustoz-shogird kursi")
async def ustoz_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Kursni sotib olish",
                    url="https://t.me/Zikrilla_zohidjonovich?text=Assalomu%20alaykum.%20Men%20USTOZ-SHOGIRD%20kursini%20sotib%20olmoqchiman."
                )
            ]
        ]
    )
    text = """
<b>🎓 Ustoz-shogird mentorlik dasturi</b>
Narxi: <b>250$</b>

✔ Shaxsiy nazorat  
✔ Real amaliy keyslar  
✔ Bosqichma-bosqich rivojlanish  
✔ Professional darajaga chiqish  
"""
    await message.answer(text, reply_markup=keyboard)


@dp.message(F.text == "📚 Onlayn darsliklar")
async def darslik_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Kursni sotib olish",
                    url="https://t.me/Zikrilla_zohidjonovich?text=Assalomu%20alaykum.%20Men%20ONLAYN%20DARSLIKLARNI%20sotib%20olmoqchiman."
                )
            ]
        ]
    )
    text = """
<b>📚 Professional onlayn darsliklar</b>
Narxi: <b>150$</b>

✔ PDF metodik qo‘llanmalar  
✔ Tayyor dars ishlanmalari  
✔ Amaliy mashg‘ulotlar  
✔ Doimiy foydalanish huquqi  
"""
    await message.answer(text, reply_markup=keyboard)


@dp.message(F.text == "👤 O‘zim haqimda")
async def about_handler(message: Message):
    text = """
<b>👤 Zikrilla Zohidjonovich</b>

👨‍🏫 Defektolog | ABA terapevt | Kurator

🎓 Nizomiy nomidagi Toshkent davlat pedagogika universiteti bakalavri
🇨🇦 Canada Azbuka ABA maktabi 3-modul bitiruvchisi

🏥 Farg‘ona shahridagi “Nurafshon” markazi kuratori

🏅 BTA Ambassador – Farg‘ona shahar

💬 Farzandingiz rivoji – bizning ustuvor vazifamiz!

📩 Konsultatsiya uchun murojaat qiling.

"""
    await message.answer(text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())