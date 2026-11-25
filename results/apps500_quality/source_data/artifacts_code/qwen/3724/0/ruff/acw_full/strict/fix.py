from sys import stdin

MOD = 7 + 10**9


def count_distinct_strings(n, s):
	# Initialize the count of distinct strings
	count = 0
	# Initialize the previous character
	prev = None
	# Initialize the current character count
	current_count = 0

	for char in s:
		if char == prev:
			# If the current character is the same as the previous one, reset the count
			current_count = 0
		else:
			# If the current character is different, add the count of the previous character
			current_count += 1
			# Add the count of the current character
			current_count += 1
			# Update the previous character
			prev = char

	# The total number of distinct strings is the sum of the counts plus one
	count = 1 + current_count
	# Return the result modulo (10^9 + 7)
	return count % MOD


# Read input
n = int(stdin.readline().strip())
s = stdin.readline().strip()

# Output the result
print(count_distinct_strings(n, s))
