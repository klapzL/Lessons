# num = 600851475143
# divider = 2
# while num != 1:
# 	if num % divider == 0:
# 		num /= divider
# 		print(divider)
# 	divider+=1
# print(num)

# x = 994
# y = 999
# result = 0
# while True:
# 	if str(x * y) == str(x * y)[::-1]:
# 		print(x)
# 		print(y)
# 		result = x*y
# 		break
# 	y -= 1
# print(result)

nums = 1
num = 3000
for i in range(1,11):
	while nums <= 20:
		if num % nums == 0:
			nums += 1

print(nums)