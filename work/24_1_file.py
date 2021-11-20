import os
# Открытие файла с помощью with
counter = 0
with open('text1.txt', 'r', encoding='utf-8') as file:
	for line in file:
		counter += line.count(' the ')
		counter += line.count('The ')
print(counter)

dirs = os.scandir('C:/Users/User/Documents/')
# print(dirs)
for dir1 in dirs:
	if dir1.is_file():# Выбирает только файлы
		print(f'Это файл {dir1.name}')
	if dir1.is_dir():# Выбирает только подпапки
		print(f'Это папка {dir1.name}')

# Создание папки
if not os.path.exists('example'):
	os.mkdir('example/')

if not os.path.exists('text/'):
	os.makedirs('text/2021/example/')

# Удаление
if os.path.exists('example/'):
	os.remove('example/')

os.rmdir('text/2021')

