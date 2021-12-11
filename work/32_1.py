a = 1
b = 2
summa = 2
while a + b < 100:
	c = a + b
	a = b
	b = c
	# print(c)
	if c % 2 == 0:
		summa += c
	# print(a+b)

# print(summa)


def max_min_difference(lst):
	max_num = 0
	min_num = 0
	for i in lst:
		if i > max_num:
			max_num = i
		if i < max_num:
			min_num = i
			# if i < min_num:
	return max_num, min_num

print(max_min_difference([5,10,4,2,23,6,11]))
