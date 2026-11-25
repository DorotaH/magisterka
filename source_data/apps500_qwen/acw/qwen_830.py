import sys
from fractions import Fraction


def min_resistors(a, b):
	target = Fraction(a, b)
	count = 0

	while target != 1:
		if 1 < target:
			# Try to make the target by adding a resistor in series
			if 0 < target - 1:
				count += 1
				target -= 1
		elif 0 < 1 / target - 1:
			count += 1
			target = 1 / (1 / target - 1)

	return count + 1


# Read input
a, b = map(int, sys.stdin.read().split())

# Output the result
print(min_resistors(a, b))
