n = input()
c = 0
s = ''
for i in n:
	if n.count(i) >= c:
		c = n.count(i)
		if i not in s:
			s = i
		else:
			s += i

print(s)