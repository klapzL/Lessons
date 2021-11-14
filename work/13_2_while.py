a = "Lorem "
for _ in range(20):
	print(a)

print("С помощью for _ in range")
for j in range(11):
	print(j)
for i in range(2,11,2):
	print(i)
print("С помощью while")
j = 0
while j<=10:
	print(j)
	j+=1
j = 2
while j<=10:
	print(j)
	j+=2

summa = 0
for i in range(10,101,2):
	summa+=i

print(summa)

summa = 0
for i in range(101):
	if i % 2 == 0:
		summa+=i

print(summa)

summa = 0
b = 0
while b<=100:
	if b % 2 == 0:
		summa+=b
	b+=1

print(summa)

summa = 0
d = 0
while d <= 100:
	summa+=d
	d+=2

print(summa)

