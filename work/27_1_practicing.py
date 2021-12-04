
def cut0(digit):
	my_str = list(str(digit))
	for i in my_str[::-1]:
		print(i)
		print(my_str)
		if i == '0':
			my_str.pop()
		else:
			break
	return ''.join(my_str)

print(cut0(20300))
