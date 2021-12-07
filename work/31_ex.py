


def end_other(str1, str2):
	return str1.endswith(str2) or str2.endswith(str1)

print(end_other('pronoun', 'noun'))
print(end_other('Pronoun', 'noun'))
print(end_other('noun', 'pronoun'))
print(end_other('Noun', 'pronoun'))

def cat_dog_equal(catdog):
		return catdog.count('cat') == catdog.count('dog')

# print(cat_dog_equal('catdog'))
# print(cat_dog_equal('catcat'))
# print(cat_dog_equal('catdogdog'))

def count_code(string):
	result = 0
	# counter = 0
	# while True:
	# 	if string.index('co')+3 == string.index('e'):
	# 		result+=1
	for i in string:
		if i == 'c':
			if string[string.index(i)+1] == 'o':
				if string[string.index(i)+3] == 'e':
					result +=1
	return result

print(count_code('aacodeaa'))
print(count_code('cofeandcode'))