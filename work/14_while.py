# summa = 0
# b = 101
# while b>=11:
# 	if b % 2 == 1:
# 		summa+=b
# 	b-=1

# print(summa)

# summa = 0
# d = 101
# while d >= 11:
# 	summa+=d
# 	d-=2

# print(summa)

# word = ""
# for i in my_list:
# 	word+=i

# print(word)

# my_list = ['a', 'p', 'p', 'l', 'e']
# ind = 0
# word = ""
# while ind < len(my_list):
# 	word+=my_list[ind]
# 	print(word)
# 	ind+=1

# print(word)

# Recovery Key:1884165-piei84igU7BMfEYJtoeFnMzqzsQF5VHqAjv6X3cR
# Direct Link:https://projecteuler.net/recovery=1884165-piei84igU7BMfEYJtoeFnMzqzsQF5VHqAjv6X3cR
# Generated:Wed, 27 Oct 2021, 14:13.51

# n = [12, 20, 1, 5, 3, 8]
# b = 0
# for i in n:
# 	if i % 2 == 0:
# 		b+=i

# print(b)

n = [12, 20, 1, 5, 3, 8]
i = 0
w = 0
while i < len(n):
	if n[i] % 2 == 0:
		w+=n[i]
	i+=1
print(w)

my_word = ['e','l','p','p','a']
b = ""
for i in my_word[4:-1:-1]:
	b+=i
print(b)

ind = len(my_word)-1
d = ""
while ind > -1:
	d+=my_word[ind]
	ind-=1

print(d)

summa = 0
while n:
	i = n.pop()
	if i % 2 == 0:
		summa+=1

print(summa)
