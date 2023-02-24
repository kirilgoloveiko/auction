import random
lst_id_lot = []

def gen_id(lst):
    point = 0
    while point == 0:
        id = random.randint(1,99999)
        if id not in lst:
            lst.append(id)
            point +=1
            return id




print(gen_id(lst_id_lot))


