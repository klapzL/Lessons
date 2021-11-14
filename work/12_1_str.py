t1 = "lorem"
t2 = "ipsum"
print(id(t2))
r = t1 + " " + t2
print()
print(r)

# Строки нельзя изменять
# t1 = "hi"
# print(t1)

# t2[0] = "o"
# print(t2)

# del t2[-1]
# print(t2)

t2 = "Z" + t2[1:]
print(id(t2))
# print("X" + "Fdsg"[1:])