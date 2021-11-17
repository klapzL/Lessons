# Работа с файлами / Working with files

file = open("text.txt")
text = file.read()
my_list = []
my_list.append(text)
print(text)
print(my_list)

file.close()
