import json
import random

from telebot.types import InputMediaPhoto


def gen_caption(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data_from_json = json.load(f)

    caption = f"{data_from_json['description']}\n"\
                  f"{data_from_json['city']}\n"\
                  f"{data_from_json['delivery']}\n"
    return caption


def card(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data_from_json = json.load(f)

    media_list = []

    for photo in data_from_json['mas_photos']:
        if not media_list:
            obj = InputMediaPhoto(photo, caption=gen_caption(json_file))
            media_list.append(obj)
        else:
            obj = InputMediaPhoto(photo)
            media_list.append(obj)

    return media_list


# print(card('38938.json'))


def gen_lot_id() -> int:
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    new_id = "".join([random.choice(numbers) for x in range(5)])
    return int(new_id)

# print(gen_lot_id())