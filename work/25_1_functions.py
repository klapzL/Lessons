# Функции / Functions

def my_func():
	print('Hello, World!')

# my_func()

def name():
	return 'lorem'# Подставляется значение

a = name()
# print(a)

# Параметры функии

def even(number): # Переменная 'number' может использоваться только в функции
	if number % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

print(even(4))
print(even(int(input())))

def summa(a, b):
	return a + b

print(summa(4, 5))

def longest_word(text):
	my_list = []
	f = ''
	letters = text.split()
	for i in letters:
		leng = len(i)
		my_list.append(leng)
	longest_word = max(my_list)
	for i in letters:
		if len(i) == longest_word:
			print(i)

text1 = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.
'''

print(longest_word(text1))

# def fahr(cels):
# 	return (cels*9/5)+32

# print(fahr(int(input())))
