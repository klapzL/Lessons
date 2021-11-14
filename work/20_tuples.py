# Кортежи / Tuples
# my_tuple = (1, 2, 3)
# print(my_tuple, type(my_tuple))

# empty_tuple = ()
# print(len(empty_tuple))

# one_element = (10,)
# print(type(one_element))

# empty_tuple = tuple()
# new_tuple = tuple('New Tuple')
# numbers = ([2,3,4])
# print(empty_tuple, type(empty_tuple))
# print(new_tuple, type(new_tuple))
# print(numbers, type(numbers))

# print(len(new_tuple))
# print(new_tuple[1:])

# # Распаковка и упаковка кортежей
# coordinates = 12.9, 98.6
# print(coordinates ,type(coordinates))

# x, y = coordinates
# print(x)
# print(y)

# name, age, height = 'Aleksey', 39, 183.4
# print(name)
# print(age)
# print(height)

# # Проверка на наличие
# letters = ('a', 'e', 'u',)
# print('x' in letters)
# print('a' in letters)

# # Изменение кортежей
# letters = ('a', 'e', 'u',)
# list_letters = list(letters)
# list_letters.pop()
# letters = tuple(list_letters)
# print(letters)

text = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua
'''
my_list = []
my_list1 = []
letters = text.split()
for i in letters:
	my_list.append(i)
	longest_word = max(len(my_list))
	print(my_list1(type))
	# if len(i) == max(my_list):
		# print(i)
