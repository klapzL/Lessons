# Множества может хранить в себе только уникальные элементы / sets
fruits = {'apple', 'pear', 'grape', 'apple'}
print(f'set {fruits}')

fruit_list = ['apple', 'pear', 'grape', 'apple']
print(f'list {fruit_list}')
fruit = set(fruit_list) # Из list в set (удаление дублированных элементов)
print(f'list to set {fruit}') 
fruit_list = list(fruit) # Из set в list
print(f'set to list {fruit_list}') 

my_set = {}
print(type(my_set)) # Не тип set

print(len(fruits)) # Длина set
