# Генератор списков / List comprehension
numbers = []
for i in range(1,11):
	numbers.append(i) 

print(numbers)

numbers2 = [i for i in range(1, 11)]
print(numbers2)

numbers3 = [i**2 for i in range(1,11)]
print(numbers3)

odd_nums = [i for i in range(1,16) if i % 2 == 1]
print(odd_nums)

nums = []
for x in nums:
	if x % 2 == 0:
		x = x ** 2
	nums.append(x)
print(nums)

my_str = 'axyz'
listt = [chr(ord(letter)+1) if ord(letter) != 122 else 'a' for letter in list(my_str)]
print(''.join(listt))

my_list = [[1,2,3],[4,5,6],[7,8,9]]
summa = 0
for sub_list in my_list:
	for x in sub_list:
		summa+=x
print(summa)

flattened = [i for sub_list in my_list for i in sub_list]
print(flattened)

my_list = [[1,2,3],[4,5,6],[7,8,9]]
count1 = 0 
for i in my_list:
	for x in i:
		count1+=1
print(count1)

new_list = [i for sub_list in my_list for i in sub_list]
print(len(new_list))

new_list1 = [len(sub_list) for sub_list in my_list]
print(sum(new_list1))

zeros = [0 for _ in range(10)]
print(zeros)
