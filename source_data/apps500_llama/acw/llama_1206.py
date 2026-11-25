import math
import sys


def solve(a1, b1, a2, b2):
	# Calculate the initial number of squares in each bar
	sq1 = a1 * b1
	sq2 = b2 * a2

	# Calculate the minimum number of squares in either bar
	min_sq = min(sq1, sq2)

	# Calculate the maximum number of squares in either bar
	max_sq = max(sq1, sq2)

	# Find the GCD of the two numbers
	gcd = math.gcd(a1, b1)
	gcd = math.gcd(gcd, a2)
	gcd = math.gcd(gcd, b2)

	# Initialize a list to store the possible sizes of the bars after the process
	sizes = []

	# Try all possible values of the GCD
	for i in range(gcd, 0, -1):
		# Check if the GCD is a divisor of the dimensions of the bars
		if a1 % i == 0 and b1 % i == 0 and a2 % i == 0 and b2 % i == 0:
			# Calculate the number of minutes it takes to reach the GCD
			minutes = 0
			if a1 % (i // 2) == 0 and b1 % (i // 2) == 0:
				minutes += 1
			if a2 % (i // 2) == 0 and b2 % (i // 2) == 0:
				minutes += 1

			# Check if we can reach a size of i × i in the minimum number of minutes
			if minutes == 0:
				sizes.append((a1 // i, b1 // i, minutes))

			# If not, try to chip off a third of the bar
			if a1 % (i // 3) == 0 and b1 % (i // 3) == 0:
				minutes += 1
			if a2 % (i // 3) == 0 and b2 % (i // 3) == 0:
				minutes += 1

			# Check if we can reach a size of i × i in the minimum number of minutes
			if minutes == 0:
				sizes.append((a1 // (i // 3), b1 // (i // 3), minutes))

	# If we found any possible sizes, return the minimum number of minutes and the possible sizes
	if sizes:
		minutes = min(sizes, key=lambda x: x[2])
		return minutes[2], str(minutes[0]) + " " + str(minutes[1]), str(minutes[2]) + " " + str((b1 // minutes[1]) * a2 // (a1 // minutes[0]))

	# If we didn't find any possible sizes, return -1
	return -1


# Read the input from standard input
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# Call the function to solve the problem
result = solve(a1, b1, a2, b2)

# Print the result
if result != -1:
	print(result[0])
	print(result[1])
	print(result[2])
else:
	print(result)
