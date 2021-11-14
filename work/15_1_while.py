n = [12, 20, 1, 5, 3, 8]
summa = 0
while n:
	print(len(n))
	i = n.pop()
	if i % 2 == 0:
		summa += i

print(summa)


my_word = ['e','l','p','p','a']
w = ''
while my_word:
	l = my_word.pop()
	w += l

print(w)

numbers = [12, 20, 1, 5, 3, 8]
summa = 0
while numbers:
	n = numbers.pop()
	if n % 2 == 0:
		print(f"{n} - четное")
	else:
		print(f"{n} - нечетное")
else:
	print("Конец")
