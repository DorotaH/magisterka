from collections import defaultdict


def largest_number(n, cubes):
	# Dictionary to store possible digits for each position
	possible_digits = defaultdict(list)

	# Collect possible digits for each position (0-5)
	for i in range(6):
		for cube in cubes:
			possible_digits[i].append(cube[i])

	# Function to check if a number can be formed
	def can_form_number(num):
		for digit in str(num):
			if all(
				digit not in positions
				for positions in possible_digits.values()
			):
				return False
		return True

	# Find the largest number that can be formed
	for x in range(999999, 0, -1):
		if can_form_number(x):
			return x

	return 0


# Read input
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]

# Print the result
print(largest_number(n, cubes))
