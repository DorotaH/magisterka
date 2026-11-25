MOD = 998244353


def count_good_permutations(n, s):
	# Count the number of good permutations
	from collections import defaultdict
	
	# Create dictionaries to store the indices of elements in the sequence
	idx_a = defaultdict(list)
	idx_b = defaultdict(list)
	
	for i, (a, b) in enumerate(s):
		idx_a[a].append(i)
		idx_b[b].append(i)
	
	# Function to count the number of permutations that keep the sequence good
	def count_good_permutations_for_list(idx):
		if not idx:
			return 1
		if len(idx) == 1:
			return 1
		
		# Sort indices based on the sequence values
		sorted_idx = sorted(idx, key=lambda i: s[i][1])
		# Calculate the number of valid permutations
		count = 0
		for i in range(len(sorted_idx)):
			count += count_good_permutations_for_list(sorted_idx[:i] + sorted_idx[i + 1:])
		return count
	
	# Calculate the number of good permutations for both sequences
	good_permutations = (count_good_permutations_for_list(idx_a) * count_good_permutations_for_list(idx_b)) % MOD
	
	return good_permutations


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
s = []
for i in range(n):
	a = int(data[i * 2 + 1])
	b = int(data[i * 2 + 2])
	s.append((a, b))

# Calculate and print the result
result = count_good_permutations(n, s)
print(result)
