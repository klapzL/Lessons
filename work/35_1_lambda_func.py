# Reduce
from functools import reduce

numbers = [i for i in range(1,5)]
result = reduce(lambda a, b: a + b, numbers, 100)
# print(result)

###

letters = ['a','p','p','l','e']
result = reduce(lambda a, b: a + b, letters, '#')
# print(result)

###

numbers = [i for i in range(2, 11)]
result = reduce(lambda a, b: a * b, numbers)
# print(result)


my_numbers = [14.24, 15.32, 6.32]
print(list(map(lambda a :round(a ** 2, 3), my_numbers)))


###

my_numbers = [1001, 2021, 1991, 2006, 3002]
# print(list(filter(lambda a: str(a)[::-1] == str(a), my_numbers)))

###

n = 'lorem ipsum'
