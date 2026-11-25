import math

X = int(input())
max_power = 0

for b in range(1, int(math.sqrt(X)) + 1):
	p = 2
	while (bp := b ** p) <= X:
		max_power = max(max_power, bp)
		p += 1

print(max_power)
