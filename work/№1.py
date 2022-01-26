def even_and_odd(lst):
	even = 0
	odd = 0
	for i in lst:
		if i % 2 == 0:
			even+=1
		else:
			odd+=1
	return f'Чётные = {even}\nНечётные = {odd}'

print(even_and_odd([1, 2, 3, 4, 5, 6, 7]))