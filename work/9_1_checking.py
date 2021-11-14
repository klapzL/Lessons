d = 0
text = "Мне 18 лет, я родился в 2003 году"
for x in text:
	if x.isdigit():
		d+=1
print(d)

l = 0
for i in text:
	if i.isalpha():
		l+=1
print(l)

al = 0
for y in text:
	if y.isalnum():
		al+=1
print(al)
