t1 = "lorem"
t2 = "ipsumi"
print(t1*2)

#Метод find
print(t2.find("su"))
print(t2.find("sun"))

#Метод replace
print(t2.replace("с", "mlo"))

a = input("Введите ваше имя: ")
a = a.lower()
a = a.replace('a', '4')
a = a.replace('b', '8')
a = a.replace('e', '3')
a = a.replace('l', '1')
a = a.replace('o', '0')
a = a.replace('s', '5')
a = a.replace('t', '7')
print(a)
for i in a:
	if i.isdigit():
		print(i, end="")

