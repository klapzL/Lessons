# my_list = {1,1,2,2,3,3,4,5,6,7,8,8,8,8,9}
# for i in my_list:
# 	print(i)

# my_list1 = [1,1,2,2,3,3,4,5,6,7,8,8,8,8,9]
# a = set(my_list1)
# for x in a:
# 	print(x)

my_list2 = [1,1,2,2,3,3,4,5,6,7,8,8,8,8,9]
for y in my_list2:
	if my_list2.count(y)>1:
		my_list2.remove(y)
		print(my_list2)