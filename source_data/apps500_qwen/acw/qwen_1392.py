from collections import Counter

MOD = 998244353


def count_good_permutations(n, s):
	# Count occurrences of each first and second element
	first_count = Counter(a for a, b in s)
	second_count = Counter(b for a, b in s)
	
	# Calculate the number of good permutations
	good_permutations = 1
	for i in range(1, 1 + n):
		good_permutations = (good_permutations * (second_count[i] + first_count[i])) % MOD
	
	return good_permutations


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
s = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(n)]

# Calculate and print the result
result = count_good_permutations(n, s)
print(result)
