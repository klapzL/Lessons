# break - заканчивает
for i in range(1, 1001):
	if i >= 20:
		break
	print(i)


# continue - "передает"
a = [1,1,2,2,3,3,4,5,6,7,8,8,8,8,9]
b = []
for i in a:
	if i in b:
		continue
	else:
		b.append(i)
print(b)
