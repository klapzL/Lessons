import json

d = {'name': 'Emir', 'age': 14, 'friends': ('Misha', 'Roma')}

dict_to_json = json.dumps(d)
# Кортеж превращается в массив всё остальное как в Python
print(dict_to_json)
json_to_dict = json.loads(dict_to_json)
# А массив превращается в список
print(json_to_dict)

# dumps - для сериализации (в JSON) в строку
# loads - для десериализации (из JSON) из строки
# dump - для сериализации в файл
# load - для десериализации из файла

with open('users.json', 'w') as f:
    json.dump(d, f, indent=2)

with open('users.json', 'r') as f: 
    users = json.load(f)
print('Десериализованный кусок данных', users)
