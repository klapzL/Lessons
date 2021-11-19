file1 = open('text.txt', 'r')
for line in file1:
	if len(line) < 70 or line.startswith('L'):
		line = line.rstrip()
		line = line.lstrip()
		print(line)

file2 = open('text1.txt', 'r')
lines = file2.read()
lines = lines.split()
counter = 0
for line in lines:
	if line == 'the':
		counter+=1
print(counter)
file2.close()
