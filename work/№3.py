def shuffle(lst):
	n_lst = []
	index = 0
	while index < len(lst)-1:
		n_lst.append(lst[index+1])
		n_lst.append(lst[index])
		index+=2
	if len(n_lst) != len(lst):
		n_lst.append(lst[-1])
	return n_lst

print(shuffle([1, 2, 3, 4, 5, 6, 7]))