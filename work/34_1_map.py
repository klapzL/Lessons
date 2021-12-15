# Map

numbers = [5,14,32,5,15,23]

numbers_plus_one = list(map(lambda n: n**2, numbers))

print(numbers_plus_one)

text = '1 2 3 4 5'
numbers_str = text.split()
numbers_sum = sum(list(map(lambda n: int(n), numbers_str)))
print(numbers_sum)

# Filter
import math

text = '2 3 1 5 3 4 6'
numbers_str = text.split()
num_lst = list(map(lambda i: int(i), numbers_str))
even_number = list(filter(lambda n: n % 2 == 1, num_lst))
print(math.prod(even_number))