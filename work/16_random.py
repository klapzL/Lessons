import random 

# генерируем рандомное число от 0 до 1
# print(random.random())

# при заданном seed наборы чисел рандомные но повторяются
# random.seed(2)
# print(random.random())
# print(random.random())

# генерация целых от 10 до 100
print(random.randint(10, 100))

my_list = [1, 2, True, "hello", "world"]

print(random.choice(my_list))
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)
print(random.choice('zxcvbn'))

num_input = int(input("Введите цифру: "))
my_list = []
for _ in range(1, num_input+1):
	num_randint = random.randint(1, num_input)
	my_list.append(num_randint)

print(my_list)

my_list = []
while num_input > 0:
	num_rand = random.randint(1, num_input)
	my_list.append(num_rand)
	num_input-=1

print(my_list)

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user_input = int(input("Введите цифру: "))
empt_str1 = ""
for _ in range(1, user_input+1):
	password_random = random.choice(alph)
	empt_str1+=password_random
	print(empt_str1)


empt_str = ""
while user_input > 0:
	password_rand = random.choice(alph)
	print(empt_str+password_rand, end="")
	user_input-=1

# num_input = int(input("Введите цифру: "))
# my_list = []
# for _ in range(1, num_input+1):
# 	num_randint = random.randint(1, num_input)
# 	my_list.append(num_randint)

# print(my_list)1

# my_list = []
# while num_input > 0:
# 	num_rand = random.randint(1, num_input)
# 	my_list.append(num_rand)
# 	num_input-=1

# print(my_list)

# alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# user_input = int(input("Введите цифру: "))
# empt_str1 = ""
# for _ in range(1, user_input+1):
# 	password_random = random.choice(alph)
# 	empt_str1+=password_random
# 	print(empt_str1)


# empt_str = ""
# while user_input > 0:
# 	password_rand = random.choice(alph)
# 	print(empt_str+password_rand, end="")
# 	user_input-=1