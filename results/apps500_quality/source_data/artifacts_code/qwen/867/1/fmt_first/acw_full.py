# Solution to the problem
def min_brains(N):
	# For N = 1, Heidi must take the only brain available
	return 1 if N == 1 else 2


# Read input
N = int(input().strip())

# Output the result
print(min_brains(N))
