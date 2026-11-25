import math
import sys

r = int(input())

if 3 > r:
	print("NO")
	sys.exit()

x = int(math.sqrt(r - 1))
if (x * (1 + x) == r - 1):
	y = (r - x**2 - x - 1) // 2
	if y > 0:
		print(x, y)
	else:
		print("NO")
else:
	print("NO")
