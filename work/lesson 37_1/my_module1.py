def average(a):
	summa = 0
	for i in a:
		if i.isdigit():
			summa += int(i)
	return summa / 5

def rise_in_price(menu):
	new_price = int(menu.values()) + 50

