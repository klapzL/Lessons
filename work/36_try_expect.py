# Исключения
	# number = int(input())
	# result = 0
	# try:
	# 	result - 100/number
	# except ArithmeticError:
	# 	result = 100
	# print(result)

# number = input('Введи целое число: ')
# try:
# 	number_int = int(number)
# 	result = number_int ** 2
# 	print(result)
# 	print('Работает')
# except ValueError:
# 	print('Не работает. Введи целое число')

# try:
# 	i = 10
# 	while i < 20:
# 		print(i)
# except:
# 	print('Бесконеченый цикл')

# l = [1, 2, 3, 4]
# ind = input('Введите индес от 1 до 4: ')
# try:
# 	my_number = l[int(ind)-1]
# except IndexError:
# 	print('Слишком большой индекс')
# except ValueError:
# 	print('Введите целое число')
# else:
# 	print(my_number)
# finally:
# 	print('Удачи')

# password = input('Введите ваш пароль')
# real_password = 'qwerty'
# if real_password == password:
# 	print('Вы вошли')
# else:
# 	raise ValueError('Неверный пароль')

try:
	nums = input('Введите числа: ')
	print(sum(int(nums)))
except ValueError:
	print('Вы ввели не числа')
