# Словарь / Dictionary / dict
cities = {
	'Kyrgyzstan': 'Bishkek',
	'Russia': 'Moscow',
	'Canada': 'Ottawa',
	12: 'Hawaii'
}
print(cities, type(cities))
print(cities['Kyrgyzstan'])
print(cities[12])

some_data = {}
# some_data = dict()
print(some_data)
some_data['Jan'] = 31
some_data['Feb'] = 28
print(some_data)
# Измена значения сующествующего ключа
some_data['Feb'] = 29
print(some_data)

# Удаление ключа со значением
print(cities) # До удаления
del(cities[12])
print(cities) # Результат после удаления

# KeyError
# print(some_data[12])
print(cities.get(12, 0))
print(cities.get('Canada'))

# Проверка на наличие ключа
is_jan_in_dict = 'Jan' in some_data
print(is_jan_in_dict) # True
print(31 in some_data) # False

pupils = {
	'Emir':{
	'school': '8',
	'grade': '8',
	}
}
print(pupils)
print(pupils['Emir']['school'])
print(pupils['Emir']['grade'])
print(pupils.get('Emir', {'g'}))
