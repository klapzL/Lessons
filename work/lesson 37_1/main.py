from my_module1 import average
from my_module1 import rise_in_price
from my_module1 import creating_third

# user_input = input('Введите пять чисел через пробел: ')
# print(int(average(user_input)))

menu1 = {
	'beef': 350,
	'burger': 200,
	'meatloaf': 500,
}
print(rise_in_price(menu1))

scores1 = {
	'KG': 20,
	'DE': 50,
	'RU': 10,
	'KZ': 150,
	'US': 220
}
scores2 = {
	'US': 100,
	'DE': 50,
	'IT': 12,
	'RU': 20
}
print(creating_third(scores1, scores2))

