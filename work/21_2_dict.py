
cities = {
	'Kyrgyzstan': 'Bishkek',
	'Russia': 'Moscow',
	'Canada': 'Ottawa',
	'USA': 'Hawaii'
}
for key in cities: # Перебирание ключей словаря
	print(key)

for key in cities: # Польза перебирания
	print(f'{cities[key]} situated in {key}')

# ITEMS
print(cities.items())
for key, value in cities.items():
	print(f'{value} situated in {key}')
