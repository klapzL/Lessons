# Списки
my_list = ["lorem", "ipsum", "dolor"]

# print(my_list)
# print(my_list[-2])
# print(my_list[::-1])

for item in my_list[::-1]:
	print(item)
# Добавление элементов в список
a = ["lorem"]
print(a)
a.append("ipsum")
print(a)
a.append("dolor")
print(a)

# Добавление элемента в любое место в списке, указав первым аргументом индекс
a.insert(0, "D")
print(a)
print(a.index("D"))

# Удаление элемента из списка
num = [6, 1, 11, 3, 56, 5, 6, 4, 7, 8, 5]
num.remove(6)
print(num)
num.remove(num[-1])
print(num)

# Удаление по индексу
print(num)
del num[-1]
print(num)

# Длина списка
print(len(num))

# Сортировка
num.sort()
print(num)

num2 = [1, 3, 6, 2, 5, 7, 1]
s_n2 = sorted(num2)
print(num2)
print(s_n2)

# Удаление элемента при помощи "pop"
print(num2)
d_e = num2.pop()
print("Удаленный элемент: ", d_e)
print("След. удаленный элемент: ", num2.pop())
print(num2)

# Удаляем второй элемент
d_e1 = num2.pop(2)
print(num2)
print(d_e1)