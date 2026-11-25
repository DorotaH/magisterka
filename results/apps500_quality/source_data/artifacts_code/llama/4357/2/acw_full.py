import sys


def main():
	# Read input from standard input
	A, B, C = map(int, input().split())

	# Generate all possible combinations of the values A, B, and C
	combinations = [
		(A, B, C),
		(A, C, B),
		(B, A, C),
		(B, C, A),
		(C, A, B),
		(C, B, A)
	]

	# Initialize the maximum allowance
	max_allowance = -float('inf')

	# Iterate over all combinations
	for a, b, c in combinations:
		# Calculate the allowance for the current combination
		allowance = a + b + c

		# Update the maximum allowance if necessary
		max_allowance = max(max_allowance, allowance)

	# Print the maximum allowance
	print(max_allowance)


if __name__ == "__main__":
	main()
