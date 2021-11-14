text = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua
'''
my_list = []
letters = text.split()
for i in letters:
	leng = len(i)
	my_list.append(leng)
longest_word = max(my_list)
for i in letters:
	if len(i) == longest_word:
		print(i)
