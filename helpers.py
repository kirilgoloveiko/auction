import random

d = {1329081957: {'Описание': 'Описание лота', 'Город': 'Минск'}}


def card(d: dict):
    text = f'Описание: <b>{d["Описание"]}</b>\n' \
           f'Город: <b>{d["Город"]}</b>\n'
    return text

# print(card(d))

def gen_lot_id() -> int:
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    new_id = "".join([random.choice(numbers) for x in range(5)])
    return int(new_id)

# print(gen_lot_id())