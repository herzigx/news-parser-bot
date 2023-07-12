from aiogram import executor, Bot, Dispatcher
from aiogram.types import Message
import os
from dotenv import load_dotenv
from keyboard import buttons_news, button_link
from parsing import pars_gazeta
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Добро пожаловать в наш новостной бот')
    await show_category_news(message)
    # await message.answer('Добро пожаловать в наш новостной бот')


async def show_category_news(message: Message):
    await message.answer('Выберите категорию', reply_markup=buttons_news())


@dp.message_handler(content_types=['text'])
async def get_news_by_category(message: Message):
    text_category = message.text
    category_fun = pars_gazeta(get_value(text_category))
    for category in category_fun[::-1]:
        images = category.get('images')
        data_time = category.get('data_time')
        title = category.get('title')
        info = category.get('info')
        link = category.get('link')

        await message.answer_photo(photo=images, parse_mode='HTML', caption=f'''
<b>🕒 Дата:</b> {data_time}
<b>Заголовок:</b> {title}
<b>Описание:</b> {info}''', reply_markup=button_link(link))


executor.start_polling(dp)
