import math

n = int(input())

if n in [1, 2]:
	print(1)
elif n == 3:
	print(2)
elif n == 4:
	print(3)
else:
	print(math.floor((1 + n) / 2))
