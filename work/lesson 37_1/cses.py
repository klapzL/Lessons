n = int(input())

s = f'{n} '
while n != 1:
	if n % 2 == 0:
		n /= 2
		s = s + str(int(n)) + ' '
	else:
		n = n * 3 + 1
		s = s + str(int(n)) + ' '

print(s)