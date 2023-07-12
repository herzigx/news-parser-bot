from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from configs import CATEGORIES

def buttons_news():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = []
    for category in CATEGORIES.keys():
        btn = KeyboardButton(text=category)
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def button_link(value):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Читать полностью', url=value)
    markup.add(btn)
    return markup


