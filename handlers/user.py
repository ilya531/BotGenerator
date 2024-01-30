import datetime
import random
import string
import telebot

from funcs.datetime_funcs import get_welcome
from init_bot import bot


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Я бот-пароль.\n\n' \
           f'Выберите функцию:\n' \
           f'/get_paswrd - Получить надёжный пароль \n' \
           f'/get_date - Получить сегодняшнюю дату'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['get_paswrd'])
def generate_password(message: telebot.types.Message, length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    ''.join(random.choice(characters) for i in range(length))
    password = ''.join(random.choice(characters) for i in range(length))
    text = f'Предлагаю такой пароль: {password} '
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['get_date'])
def get_date(message: telebot.types.Message):
    current_date = datetime.datetime.now()
    text = f'Сегодняшняя дата: {current_date.date()}'
    bot.send_message(message.chat.id, text)
