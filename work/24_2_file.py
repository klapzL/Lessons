import os
import shutil

print('text существует?', os.path.exists('text/'))
if os.path.exists('text/'):
	shutil.rmtree('text/')

shutil.copy2('text.txt', 'C:/Users/User/Documents/emir/example')
