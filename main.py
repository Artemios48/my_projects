import telebot
from telebot import types
import time
import os
from parse import *
from TOKEN import *
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=["text"])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! Этот бот предназначен приносить смех и радость людям. \n Чтобы посмеятся введите любую цифру:')
    elif message.text.lower() in '123456789':
        bot.send_message(message.from_user.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.from_user.id, 'Введите любую цифру)')

bot.polling(none_stop=True, interval = 0)