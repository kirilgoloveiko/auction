import telebot
from telebot.types import InputMediaPhoto
import json


bot = telebot.TeleBot('5790530956:AAHR5gW3d7Z7K1NWj81Ycej8zf4rHYUYhr4')


lsit_buf_photo = []

lot = {}

# lot = {
#     "id_admin": "id",
#     "mas_photos": ["photo1", "photo2","photo1", "photo2","photo1", "photo2","photo1"],
#     "description": "описание",
#     "city" : "город",
#     "delivery": "условия доставки",
#     "cost": "цена"
# }

def add_cost(message):
    if  len(message.text) <= 1 or message.content_type != "text":
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_cost)  
    else:
        lot["cost"] = message.text
        bot.send_message(message.from_user.id, "Лот успешно сформирован!")
        for x,y in lot.items():
            print(x,"  ",y)

def add_delivery(message):
    if  len(message.text) <= 1 or message.content_type != "text":
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_delivery)
    else:
        lot["delivery"] = message.text
        msg = bot.send_message(message.from_user.id, "Укажите стартовую цену лота")
        bot.register_next_step_handler(msg, add_cost)


def add_city(message):
    if  len(message.text) <= 1 or message.content_type != "text":
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_city)   
    else:
        lot["city"] = message.text
        msg = bot.send_message(message.from_user.id, "Условия доставки? (Почта /Самовывоз /Курьер)")
        bot.register_next_step_handler(msg, add_delivery)

def add_description(message):
    print(message.content_type)
    if  len(message.text) <= 1 or message.content_type != "text":
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте еще раз")
        bot.register_next_step_handler(msg, add_description)

    else:
        lot["description"] = message.text
        msg = bot.send_message(message.from_user.id, " Отличто! Описание добавлено. Укажите местонахождение (Город)")
        bot.register_next_step_handler(msg, add_city)

    

def Add_photo(message):
    print(message.content_type)
    if "id_admin" not in lot:
        bot.send_message(message.from_user.id, " Если хотите добавить лот, введите команду '/add_lot'")

    elif message.content_type !="photo" :
        msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте всетаки загрузить картинку ")
        bot.register_next_step_handler(msg, Add_photo)

    elif  message.content_type =="photo":
        lot["mas_photos"] = []
        if len(lot["mas_photos"]) <= 8 :
            lot["mas_photos"].append(message.photo[-1].file_id)

        msg = bot.send_message(message.from_user.id, "Хорошо! Теперь добавьте описание ")
        bot.register_next_step_handler(msg, add_description)


# @bot.message_handler(content_types= ["photo"])
# def Add_photo(message):
#     # print(message.content_type)
#     # print(message)
#     # сдесь будет проверка на права Админа
#     if message.content_type !="photo" :
#         msg = bot.send_message(message.from_user.id, "Что-то пошло не так, попробуйте всетаки загрузить картинку ")
#         bot.register_next_step_handler(msg, Add_photo)

#     elif len(lot["mas_photos"]) >= 8:
#         bot.send_message(message.from_user.id, "Достигнут лемит по количеству картинок")
#         msg = bot.send_message(message.from_user.id, "Пойдем дальше. Теперь добавьте описание ")
#         bot.register_next_step_handler(msg, add_description)


#     elif message.content_type =="photo" and len(lot["mas_photos"]) <= 8 :
#         lot["mas_photos"].append(message.photo[-1].file_id)


#         msg = bot.send_message(message.from_user.id, "Хорошо! Теперь добавьте описание ")
#         bot.register_next_step_handler(msg, add_description)
    
        
#     print(lot)



@bot.message_handler(content_types= ["text"])
def any_text(message):
    print(len(message.text))
 
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Добро пожаловать ✌🏻\n\nСкоро я начну работать')

    elif message.text == "":
        bot.send_message(message.from_user.id, 'Для начала работы бота необходимо прописать команду /start')

    elif message.text == '/add_lot':
        # сдесь будет проверка на права Админа
        lot["id_admin"] = message.from_user.id
        msg = bot.send_message(message.from_user.id, "Для началла пришлите не мене фото (не более 8шт.)")
        bot.register_next_step_handler(msg, Add_photo)
            

        
    

   


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    pass




print('Ready')
bot.infinity_polling(skip_pending=True)