from fractions import Fraction


def max_water(n, T, a, t):
	from functools import reduce
	from operator import mul

	# Calculate the total maximum capacity of the taps
	total_capacity = sum(a)

	# If total capacity is zero, it's impossible to achieve any temperature
	if total_capacity == 0:
		return 0

	# Calculate the total maximum temperature of the taps
	total_temperature = sum(t)

	# If the desired temperature is zero, the maximum water is the total capacity
	if T == 0:
		return total_capacity

	# If the desired temperature is greater than the total maximum temperature, it's impossible
	if total_temperature < T:
		return 0

	# Calculate the total amount of water that would be delivered if all taps were at their maximum capacity
	total_water = reduce(mul, a, 1)

	return Fraction(total_water * T, total_temperature)


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
T = int(data[1])
a = list(map(int, data[2:2 + n]))
t = list(map(int, data[2 + n:]))

# Calculate the result
result = max_water(n, T, a, t)

# Print the result
print(result)
