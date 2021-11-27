import random

def rand(jkp):
	jkp = jkp.split()
	return jkp[random.randint(0, 2)]
	random_el = random.choice(jkp)
	return random_el
text = 'камень ножницы бумага'
print(rand(text))
