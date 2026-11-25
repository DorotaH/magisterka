import math


def years_to_larger(a, b):
	# Check if Limak is already larger than Bob
	return 0 if a > b else math.ceil(math.log2(b / a) - 1)


# Read input from standard input
a, b = map(int, input().split())

# Print the result
print(years_to_larger(a, b))
