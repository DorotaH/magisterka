import math

n = int(input())
if n == 1:
	print(1)
else:
	print(2 if n % 2 == 0 else 3)
