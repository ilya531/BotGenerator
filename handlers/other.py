import telebot

from init_bot import bot


@bot.message_handler(func=lambda _: True)
def help_bit(message: telebot.types.Message):
    markup = telebot.util.quick_markup(
        {
            'Удивительная ссылка': {'url': 'https://frivclassic.online/'},
            'Полезная статья': {'url': 'https://python-scripts.com/books'}
        }
    )
    bot.reply_to(message, 'Может пригодится:', reply_markup=markup)


@bot.message_handler(func=lambda _: True)
def unknown_com(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неопознанная команда')