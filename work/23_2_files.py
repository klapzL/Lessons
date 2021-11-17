# file = open('ex.txt', 'w')
# all_lines = []
# while True:
# 	line = input()
# 	if line == 'q' or line == 'Q':
# 		break
# 	line += '\n'
# 	all_lines.append(line)

# file.writelines(all_lines)
# file.close()

file1 = open('text.txt' 'r')
text = file1.read()


# file2 = open('text.txt', 'r')
# lines = file2.read()
# lines = lines.split()
# counter = 0
# for line in lines:
# 	if line == 'the':
# 		counter+=1
# print(counter)
# file2.close()