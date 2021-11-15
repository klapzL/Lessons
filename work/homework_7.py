import random

capitals = dict(Канада = 'Оттава', Германия = 'Берлин')
for country, capital in capitals.items():
	rand = random.choice(country.split())

user_input = input(f'Введите столицу страны {country}: ')
while True:
	if user_input == capital:
		print('Правильно')
		break
	else:
		user_input = input(f'Попробуйте ещё раз. Введите столицу страны {country}: ')
