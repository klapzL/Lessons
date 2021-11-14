from time import sleep

# i = 1
# Бесконечный цикл
# while True:
# 	print(i)
# 	sleep(2)
# 	i+=1


number = int(input("Введите любое полжительное число: "))
# i = 0
# while True:
# 	print(i)
# 	sleep(0.1)
# 	if i == number:
# 		break
# 	i+=1

i = 100
while True:
	if number == i:
		break
	elif number > i:
		print("Поменьше")
	elif number < i:
		print("Побольше")
	number = int(input("Введите любое поожительное число: "))

login = "qwerty123"
password = "123456"

while True:
	login_input = input("Ввдедите ваш логин: ")
	password_input = input("Ввдедите ваш пароль: ")
	if login_input == login and password_input == password:
		print("Вы успешно вошли в аккаунт")
		break
	else:
		print('Попробуйте ещё раз')
