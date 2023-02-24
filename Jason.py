import json

with open('data.json', 'r') as f:
    data_from_json = json.load(f)

id_lot = 1234
value_dict = {'name': 'coin', 'desc': 'some text'}

if str(id_lot) not in data_from_json:
    data_from_json[id_lot] = value_dict

with open('data.json', 'w') as f:
    json.dump(data_from_json, f, indent=4, ensure_ascii=False)

