def first_last(text):
	n_list = text.split()
	return f'{n_list[0]} {n_list[-1]}'

ex_text = 'lorem ipsum dolor'
print(first_last(ex_text))

def func(a = 1, x = True):
	pass

# print(ex_text.to_list())

def kwargs(*args, **kwargs):
	print(f'kwargs = {kwargs}')
	print(f'args = {args}')

kwargs(1,2,3,4,5,x=10, z = True)
