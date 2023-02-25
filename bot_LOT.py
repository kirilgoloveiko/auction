from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot.types import InputMediaPhoto

import json
import random
import telebot

bot = telebot.TeleBot('5790530956:AAHR5gW3d7Z7K1NWj81Ycej8zf4rHYUYhr4')



list_id_lots = []

lot = {}


lst_id_lot = []

def gen_id(lst):
    point = 0
    while point == 0:
        id = random.randint(1,99999)
        if id not in lst:
            lst.append(id)
            point +=1
            return id




'''
lot = {
    "id_admin": "id", +
    "id_lot": "id_lot", +
    "mas_photos": id_photo1, +
    "description": "описание", +
    "city" : "город", +
    "delivery": "условия доставки", +
    "cost": "цена", +
    "start_time": "старт публикации", -
    "finish_time": "конец аукциона" -
}
'''


def add_time(message):
    calendar, step = DetailedTelegramCalendar().build()

    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)

def add_cost(message):
    if message.content_type == "text" and len(message.text) > 1:
        try:
            cost = int(message.text)
            lot["cost"] = cost
            id_lots = gen_id(list_id_lots)
            lot["id_lot"] = id_lots
            with open('new_lots/'f'{id_lots}.json', 'w', encoding='utf-8') as f:
                json.dump(lot, f, ensure_ascii=False, indent=4)

            bot.send_message(message.from_user.id, "Покачто лот сформирован")
        except:
            msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
            bot.register_next_step_handler(msg, add_cost)  

def add_delivery(message):
    if message.content_type == "text" and len(message.text) > 1:
        lot["delivery"] = message.text
        msg = bot.send_message(message.from_user.id, "Укажите стартовую цену лота в рублях (100/ 200/ 5000)")
        bot.register_next_step_handler(msg, add_cost)
    else:
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_delivery)


def add_city(message):
    if message.content_type == "text" and len(message.text) > 1:
        lot["city"] = message.text
        msg = bot.send_message(message.from_user.id, "Условия доставки? (Почта /Самовывоз /Курьер)")
        bot.register_next_step_handler(msg, add_delivery)
    else:
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_city)   


# len(message.text) <= 1 or 

def add_description(message):
    print(message.content_type)
    if message.content_type == "text" and len(message.text) > 1:
        lot["description"] = message.text
        msg = bot.send_message(message.from_user.id, " Отличто! Описание добавлено. Укажите местонахождение (Город)")
        bot.register_next_step_handler(msg, add_city)
    else:
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_description)
    

def add_photo(message):
    if "id_admin" not in lot:
        bot.send_message(message.from_user.id, " Если хотите добавить лот, введите команду '/add_lot'")

    elif message.content_type !="photo" :
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте всетаки загрузить картинку ")
        bot.register_next_step_handler(msg, add_photo)

    elif  message.content_type =="photo":
        lot["mas_photos"] = message.photo[-1].file_id
        msg = bot.send_message(message.from_user.id, "Хорошо! Теперь добавьте описание ")
        bot.register_next_step_handler(msg, add_description)


@bot.message_handler(content_types= ["text"])
def any_text(message):

    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Добро пожаловать ✌🏻\n\nСкоро я начну работать')
        
    elif message.text == "":
        bot.send_message(message.from_user.id, 'Для начала работы бота необходимо прописать команду /start')

    elif message.text == '/add_lot':
        # сдесь будет проверка на права Админа
        lot["id_admin"] = message.from_user.id
        msg = bot.send_message(message.from_user.id, "Для началла пришлите не мене фото (не более 8шт.)")
        bot.register_next_step_handler(msg, add_photo)
            

        
    

   


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    result, key, step = DetailedTelegramCalendar().process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:

        bot.edit_message_text(f"You selected {result}",
                              call.message.chat.id,
                              call.message.message_id)




print('Ready')
bot.infinity_polling(skip_pending=True)