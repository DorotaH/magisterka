def min_complexity(n, p):
	# Separate the bulbs into even and odd
	even = [i for i in range(1, 1 + n) if i % 2 == 0]
	odd = [i for i in range(1, 1 + n) if i % 2 != 0]

	# Initialize the garland with the first bulb
	garland = [p[0]]

	# Place the bulbs back on the garland
	for i in range(1, n):
		if p[i] == 0:
			if garland[-1] % 2 == 0:
				garland.append(odd.pop(0))
			else:
				garland.append(even.pop(0))

	return sum(bool(garland[i] % 2 != garland[i - 1] % 2)
		for i in range(1, n))


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
p = list(map(int, data[1:]))

# Output the result
print(min_complexity(n, p))
