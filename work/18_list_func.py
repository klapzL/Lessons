# сортировка букв в слове по алфввиту
# word = input("Введите слово ")
# letters = sorted(word)
# result = ''
# for ch in letters:
# 	result += ch

# print(result)

############################
# word = input("Введите слово ")
# letters = list(word)
# letters.sort()
# sorted_word = ''.join(letters)
# print(sorted_word)
##########################
# user_input = input("Введите слово: ")
# my_list = []
# empty_str = ''
# for i in user_input:
# 	order = ord(i)
# 	my_list.append(order)
# my_list.sort()

# for x in my_list:
# 	empty_str += chr(x)

# print(empty_str)

letrs = ['a', 'pp', 'l', 'e']
word = '+'.join(letrs)
print(word)

words = ['hello', 'world']
phrase = ' '.join(words)
print(phrase)

# делим на буквы
letters = list('red apple')
print(letters)

# делим на слова
words = 'hello world'.split()
print(words)

words2 = 'helloworld'.split('o')
print(words2)

url = 'https://amazon.com/book/python'
parts = url.split('/')
print(parts)

str1 = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.
"""
letter = str1.split()
my_list = []
for i in letter:
	my_list.append(i[::-1])
print(' '.join(my_list))

