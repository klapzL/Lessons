# Условия / if, else
a = int(input("Введите ваш возраст: "))
if a >= 18:
	print("Вы совершенолетний")
else:
	print("Вы несовершеннолетний")
elif a != int:
	print("Введите корректный возраст")
num = int(input("Введите число: "))
if num > 10:
	print(num**2)

# > - больше
# < - меньше
# >= - больше и равно
# <= - меньше и равно
# == - проверка на равенство
# != - проверка на неравенство

password = (input("Введите пароль: "))
password1 = "qwerty54321"
if password != password1:
	print("Неверный пароль")
else:
	print("Пароль верный")

num = int(input("Введите число: "))
if num % 2 == 0:
	print("Your number is even")
else:
	print("Your number is odd")

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
if n1 > n2:
	print("Первое число больше второго")
elif n1 < n2:
	print("Второе число больше первого")
else:
	print("Оба числа равны")
