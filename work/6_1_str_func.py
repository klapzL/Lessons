# Функции строк

a = "lorem ipsum"
b = "LOREM IPSUM"

# Смена регистра:

print(a.capitalize())
print(a.upper())
print(b.lower())

# Проверка в начале и в конце:

print(a.startswith("L"))
print(a.startswith("lorem"))

print(a.upper().startswith('LOREM'))
print(a.capitalize().startswith('lorem'))
print(a.capitalize().startswith('Lorem ipsum'))

print(a.endswith('ipsum'))
print(a.endswith('lorem'))

# Проверка регистра

print(b.islower())
print(b.isupper())
print(a.islower())

# Проверка типа содержимого

#Проверка наличия букв

print("word".isalpha())

# Проверка наличия цифр

print("4324312".isdigit())
print("fdsg4324312".isdigit())

# Проверка наличия и букв и цифр

print("fdsg4324312".isalnum())
print("fdsg4324312!?".isalnum())
print("4324312".isalnum())
print("fdsg".isalnum())

# Подсчет и поиск
c = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
"""
print(c.count("o"))
print(c.count("se"))
print(c.count("SE"))
print(c.count("Lorem"))
print(c.count("lorem"))

# index показывает перво найденного
print(c.index('o'))
print(c.index('ip'))

print(c.find('o'))
print(c.find('f'))
