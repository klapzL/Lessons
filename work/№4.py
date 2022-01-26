def card_num(num):
	index = 0
	for _ in range(len(num) - 4):
		for i in num:
			print(i)

print(card_num('1234 5678 9012 3456'))

# print('1234 5678 9012 3456'.replace(' ', ''))