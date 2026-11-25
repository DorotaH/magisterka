def is_lucky(n):
	"""Check if a number is lucky."""
	return set(str(n)).issubset({'4', '7'})


def find_lucky(n):
	"""Find the 1-based index of a lucky number n."""
	i = 1
	while True:
		if is_lucky(i) and i == n:
			return i
		i += 1


# Read input from standard input
n = int(input())

# Find and print the 1-based index of the lucky number
print(find_lucky(n))
