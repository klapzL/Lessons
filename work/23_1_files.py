# r = 'read' # Чтение файла
# w = 'write' # Перезаписывание содержимого
# a = 'append' # Если файл существует - дописывание в содержимое, не существет - создается новый
# r+ = 'read and write' # Чтение и перезапись
# a+ = 'read and append' # Если файл не существует - чтение и дописывание
# rb = 'read binary' # Чтение двоичных файлов
# wb+ = 'write and write binary'
# file1 = open('text.txt', 'r')
# print(file1.read())
# file1.close()

# file2 = open('text.txt', 'w')
# file2.write('Hello\nWorld')
# file2.close

file3 = open('text1.txt', 'a+')
print(file3.read())
file3.write('\nAppending')
file3.close()

# file4 = open('text.txt', 'r')
# lines = file4.read()
# for i in lines:
# 	print(i.rstrip())
# file4.close()

file4 = open('text.txt', 'r')
max_len = 0
max_line = ''
for i in file4:
	if len(i) > max_len:
		max_len = len(i)
		max_line = i
file4.close()
print(max_len, max_line)