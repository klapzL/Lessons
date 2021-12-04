
def split_list(my_list, length):
	main_list = []
	for i in my_list:
		sub_list = []
		for j in range(length):
			sub_list.append(i)
		main_list.append(sub_list)
	return main_list

n_list = [1,3,5,7,9,11]
# print(split_list(n_list, 1))

def splitt(my_list, length):
	lst = []
	sub_lst = []
	counter = 0
	while counter < len(my_list):
		sub_lst.append(my_list[counter])
		if (counter+1) % length == 0:
			lst.append(sub_lst)
			sub_lst = []
		counter+=1

	return lst

print(splitt(n_list, 2))
