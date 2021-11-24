# number = 1

# def example():
# 	number = 23
# 	print(number * 2)

# example()
# # print(number * 2)

# def example1(n):
# 	n = n+99
# 	return n

# print(example1(number))

# def full_name(surname, name):
# 	return f'{surname} {name}'

# print(full_name('Medetbekov', 'Emir'))

# def example2():
# 	print('До reuturn')
# 	return 1_000
# 	print('После return')

# print(example2())

# def calc(a, b, c):
# 	print(b)
# 	return a+b*2

# print(calc(1,5,9))

# def check_even(number):
# 	if number % 2 == 0:
# 		return True
# 	else:
# 		return False

# total = 0
# for i in range(1,21):
# 	if check_even(i):
# 		total+=1

# print(i)

# def palindrome(number):
# 	if str(number) == str(number)[::-1]:
# 		return True
# 	else:
# 		return False

# print(palindrome(30303))

def cap_letter(a):
	abrev = ''
	for letters in a:
		if letters.isupper():
			abrev+=letters
	return abrev

print(cap_letter('Kyrgyz Republic'))
