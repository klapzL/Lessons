n = int(input())
def less_than_n(lst):
	b = []
	for i in lst:
		if i < n:
			b.append(i)
	return b

print(less_than_n([2, 23, 34, 16, 6, 45]))