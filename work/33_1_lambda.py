# result, remainder = divmod(16, 3)
# print(result, remainder)

# Анонимные функции
a = 16
square = lambda x: x*a
# print(square(1))

# Лямбда с переменной
adult = lambda age: age >= 18
print(adult(14))
print(adult(19))

# Лямбда без прикпреления к переменной

# Вызов анонимной функции
result = (lambda n: n * n)(10)
print(result)

# Определение и вызовы анонимной функции в одну строчку
print((lambda n: n * n)(10))

# Лямбда функция для сложения
summa = lambda x, y: x+y

print(summa(2, 8))