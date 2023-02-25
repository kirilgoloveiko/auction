import json
import os

import telebot

from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import API_TOKEN
from helpers import card

bot = telebot.TeleBot(API_TOKEN)
CHANNEL_NAME = '@test_telegraph'



def write_down_message_id_to_json(message):
    message_id = message.message_id

    with open('38938.json', 'r', encoding='utf-8') as f:
        data_from_json = json.load(f)

    data_from_json['message_id'] = message_id

    with open('38938.json', 'w', encoding='utf-8') as f:
        json.dump(data_from_json, f, indent=4, ensure_ascii=False)

    print(message_id)


@bot.message_handler(content_types=['text'])
def any_text(message):
    if message.text == '/start':                                                     # !!!!!!!!!!!!!!!!
        bot.send_message(message.chat.id, 'It will work soon')
        # bot.send_media_group(CHANNEL_NAME, media=card('38938.json'))

    elif message.text == '/start2':
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton(text='Участвовать', url='https://t.me/denezhka_pridi_bot?'))
        msg = bot.send_photo(CHANNEL_NAME, photo='AgACAgIAAxkBAAOmY_k238kxTo-d4FqfuHAAAQFfW_-AAAJ1wjEb5m7RS0qniX-qX-_sAQADAgADcwADLgQ',
                       reply_markup=kb)
        write_down_message_id_to_json(msg)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    chat_id = call.message.chat.id






print("I'm ready")
bot.infinity_polling()