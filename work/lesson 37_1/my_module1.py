def average(a):
	summa = 0
	for i in a:
		if i.isdigit():
			summa += int(i)
	return summa / 5

def rise_in_price(menu):
	a = dict()
	for key, value in menu.items():
		a[key] = value+50
	return a

def creating_third(dict1, dict2):
	dict3 = dict()
	for keys, values in dict1.items():
		dict3[keys] = values
	return dict3