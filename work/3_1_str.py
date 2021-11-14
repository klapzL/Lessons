# Строки / Strings / str 

# Тройные скобки используются для многострочных текстов

text1 = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

# Если в предложении используются двойные кавычки и если предложение "обёрнуто" в также двойные кавычки, то предложение должно быть "обёрнуто" одинарными кавычками

print(text1)

text2 = 'Алексей сказал:"Привет".'

print(text2)

text3 = "I don't know."

print(text3)

# Также можно "обернуть" предложение в тройные кавычки, если в предложении имеются и двойные и одинарнеые

text4 = '''Tom said: "I don't know"'''

print(text4)

# Также можно экранировать внутренние кавычки знаком "\" ставя его перед кавычкой (ставить надо после каждой кавычки)

text5 = "Алексей сказал:\"Привет\""

print(text5)

text6 = 'I don\'t know'

print(text6)