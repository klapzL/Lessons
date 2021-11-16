capitals = dict(Канада = 'Оттава', Германия = 'Берлин', Россия = 'Москва')

print(capitals.keys()) # .keys вытаскивает ключи из словаря 
print(capitals.values()) # .values вытаскивает значения из словаря

# Проверка ключа
print('Германия' in capitals)
print('Берлин' in capitals)

# Проверка наличия значения
print("Оттава" in capitals.values())
print("Москва" in capitals["Россия"])

# Проверка пары ключ значение в словаре
print(capitals.get('Германия') == 'Берлин')
print(('Канада', 'Оттава') in capitals.items())

# Значение по умлочанию / setdefault
my_dict = {
	1: 'a',
	2: 'b',
}
my_dict[3] = 'c'
# if my_dict.get(4) is None:
# 	my_dict[4] = 'c'

my_dict.setdefault(4, 'four')
print(my_dict)
my_dict.setdefault(5)
print(my_dict[5])
