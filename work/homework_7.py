import random

capitals = dict(Канада = 'Оттава', Германия = 'Берлин', Россия = 'Москва', Украина = 'Киев', Польша = 'Варшава')
my_list = []
rand_str = ''
for country in capitals:
	my_list.append(country.split())
	rand = random.choice(my_list)
rand_str = ''.join(rand)
user_input = input(f'Введите столицу страны {rand_str}: ')
while True:
	if user_input == capitals[rand_str]:
		print('Правильно')
		break
	else:
		user_input = input(f'Попробуйте ещё раз. Введите столицу страны {rand_str}: ')
