import math


def max_games(n):
	return 1 + math.floor(math.log2(n))


# Read input
n = int(input().strip())

# Output the result
print(max_games(n))
