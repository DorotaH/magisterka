import sys


def count_valid_pairs(S):
	MOD = 2019
	count = 0
	prefix_sum = 0
	prefix_count = [0] * MOD
	
	for i, char in enumerate(S):
		digit = int(char)
		prefix_sum = (10 * prefix_sum + digit) % MOD
		count += prefix_count[prefix_sum]
		prefix_count[prefix_sum] += 1
	
	return count


# Read input from standard input
S = input().strip()

# Print the result
print(count_valid_pairs(S))
