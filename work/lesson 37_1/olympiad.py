a = ''
summa = 0
for i in range(100,1000):
	a = str(i)[1:]
	if int(a) * 9 == i:
		summa+=i

print(summa)
