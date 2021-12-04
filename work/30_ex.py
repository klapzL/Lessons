def first_half(string):
	return string[:int(len(string)/2)]

# print(first_half('HelloThere'))

def extra_chars(word):
	sliced_word = word[-2::1]
	return sliced_word*3

text = 'Lorem ipsum dolor'
# print(extra_chars(text))

def combo_string(first, second):
	longest = ''
	shortest = ''
	if len(first) > len(second):
		longest+=first
		shortest+=second
	elif len(first) < len(second):
		longest+=second
		shortest+=first
	return shortest + longest + shortest


# print(combo_string('Hello', 'hi'))

def no_first_letter(first, second):
	first = first.replace(first[0], '')
	second = second.replace(second[0], '')
	return first+second

# print(no_first_letter('Hello', 'There'))

def make_abba(a,b):
	return a+b+b+a

# print(make_abba('Hi', 'Bye'))

def rotate_left(lst):
	last_elem = lst[::-1].pop()
	lst.remove(last_elem)
	lst.append(last_elem)
	return lst

# print(rotate_left([1,2,3]))

def no_first_letter1(first, second):
	return first[1:] + second[1:]

# print(no_first_letter1('Hello', 'There'))

def rotate_left1(lst):
	without_first = lst[1:]
	first_elem = str(lst[0])
	without_first.append(first_elem)
	return without_first

# print(rotate_left1([1,2,3]))

def double_letter(string):
	double_letters = ''
	for letters in string:
		double_letters+=letters*2
	return double_letters

print(double_letter('aAzy'))
