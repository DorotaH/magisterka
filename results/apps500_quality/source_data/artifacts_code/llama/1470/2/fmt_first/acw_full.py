import math
import sys

x = int(input())

n = 0
while True:
	n += 1
	if (3 * n + 2) >= x:
		break

print(n)
