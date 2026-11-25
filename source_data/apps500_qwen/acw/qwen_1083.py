from collections import defaultdict


def count_subpermutations(n, a):
	count = 0
	seen = defaultdict(list)
	for i in range(n):
		seen[a[i]].append(i)
	for i in range(n):
		for j in range(i, n):
			subarray = a[i:1 + j]
			if sorted(subarray) == list(range(1, len(subarray) + 1)):
				count += 1
	return count


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_subpermutations(n, a))
