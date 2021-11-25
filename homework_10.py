def cap_letter(name):
	abrev = ''
	for letters in name:
		if letters.isupper():
			abrev+=letters
	return abrev

print(cap_letter('the Kyrgyz Republic'))

#######

def abrev(text):
	abrev = ''
	for words in text.split():
		if words[0].isupper():
			abrev+=words[0]
	return abrev

print(abrev('the Russian Federation'))

#######

def abreviature(abrev):
	abrev1 = ''
	for letters in abrev:
		ords = ord(letters)
		if ords > 59 and ords < 91:
			abrev1 += chr(ords)
	return abrev1

print(abreviature('the United States of America'))
