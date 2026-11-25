def find_partition(n, sequence):
	# Dictionary to store numbers grouped by their multiples
	multiples = {i: [] for i in range(1, 8)}
	
	# Group numbers by their multiples
	for num in sequence:
		for i in range(1, 8):
			if num % i == 0 and num // i <= 7:
				multiples[i].append(num)
				break
	
	# Check if we can form groups of (a, b, c) where a < b < c and a divides b, b divides c
	groups = []
	for i in range(1, 8):
		if len(multiples[i]) >= 2:
			a = multiples[i][0]
			b = multiples[i][1]
			if 2 * a <= 7 and 2 * b <= 7 and b in multiples[2 * a] and 2 * a in multiples[2 * b]:
				groups.append((a, b, 2 * a))
				multiples[a].remove(a)
				multiples[b].remove(b)
				multiples[2 * a].remove(2 * a)
				multiples[2 * b].remove(2 * b)
	
	# If we have formed all groups, return them
	if len(groups) == n // 3:
		return '\n'.join(' '.join(map(str, group)) for group in groups)
	else:
		return '-1'


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Find and print the partition
result = find_partition(n, sequence)
print(result)
