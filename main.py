import json
import os

import telebot

from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import API_TOKEN
from helpers import card, gen_lot_id

bot = telebot.TeleBot(API_TOKEN)
CHANNEL_NAME = '@test_telegraph'

admin_input_lot = {}


class States(StatesGroup):
    description = State()
    city = State()


@bot.message_handler(state=States.description)
def get_description(message):
    admin_input_lot['id'] = gen_lot_id()
    admin_input_lot['Описание'] = message.text
    bot.set_state(message.from_user.id, States.city, message.chat.id)
    bot.send_message(message.chat.id, "Укажите гороlfdg")


@bot.message_handler(state=States.city)
def get_city(message):
    admin_input_lot['Город'] = message.text
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Применить', callback_data='apply'))
    bot.send_message(message.chat.id, text=card(admin_input_lot), reply_markup=kb)
    print(admin_input_lot)

    bot.delete_state(message.chat.id, message.chat.id)


@bot.message_handler(content_types=['text'])
def any_text(message):
    # if message.text == '/start':

    if message.text == '/add_lot':
        admin_input_lot = {}
        bot.set_state(message.from_user.id, States.description, message.chat.id)
        bot.send_message(message.chat.id, "Введите текстовое описание")


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    chat_id = call.message.chat.id

    if call.data == 'apply':
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton(text='Участвовать', url='https://t.me/denezhka_pridi_bot'))
        bot.send_message(CHANNEL_NAME, card(admin_input_lot), reply_markup=kb)




bot.add_custom_filter(custom_filters.StateFilter(bot))

print("I'm ready")
bot.infinity_polling()