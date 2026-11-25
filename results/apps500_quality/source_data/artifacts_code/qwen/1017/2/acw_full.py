import sys


def max_presents(n):
	return 1 if n in [1, 2] else (1 + n) // 2


# Read input from standard input
n = int(sys.stdin.read().strip())

# Print the result
print(max_presents(n))
