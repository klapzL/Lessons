print(ord('A'))
print(ord('a'))
print(ord('B'))
print(ord('b'))

print(chr(98))

num_input = int(input("Введите цифру: "))
password = ''
for _ in range(num_input):
	password+=chr(random.randint(48, 122))

print(password)


print('a' < 'b')
print('apple' < 'pear')

user_input = input("Введите слово на английском: ")
my_list = []
str1 = ""
for i in user_input:
	a = ord(i) 
	my_list.append(a)
my_list.sort()

for x in my_list:
	str1+=str(chr(x))

print(str1)

user_input = input("Введите слово на английском: ")
empt_str = ""
for i in user_input:
	order = ord(i)+1
	if order == 91:
		order = 65
	if order == 123:
		order = 97
	empt_str+=chr(order)
	# empt_str = empt_str.replace('[', 'A')
	# empt_str = empt_str.replace('{', 'a')

print(empt_str)




